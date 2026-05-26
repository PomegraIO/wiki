#!/usr/bin/env python3
"""Generate one writer-agent prompt per (category, sub-category) bucket.

Reads scripts/_gap_plan.json (built by plan_new_entries.py) and emits
scripts/_swarm_prompts/<category>__<subcat>.md. The orchestrator (the
parent Claude) dispatches one Haiku agent per prompt file using the
Agent tool.

Each prompt is self-contained:
  - the editorial contract (extracted from WIKI_AUTHORING_GUIDE.md)
  - the target directory
  - the gap (how many articles to write)
  - existing slugs in this bucket (to avoid duplicates)
  - the full cross-link allowlist (every slug that currently exists,
    so cross-links never fabricate URLs)
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PLAN = Path(__file__).resolve().parent / "_gap_plan.json"
OUT = Path(__file__).resolve().parent / "_swarm_prompts"


def build_allowlist() -> list[str]:
    """Every slug currently on disk — the cross-link allowlist."""
    return sorted(p.stem for p in CONTENT.rglob("*.md") if not p.stem.startswith("_"))


def prompt_for(bucket: dict, allowlist: list[str]) -> str:
    cat = bucket["category"]
    sub = bucket["subcat"]
    gap = bucket["gap"]
    target_dir = bucket["dir"]
    existing = bucket["existing_slugs"]

    # Trim allowlist preview to keep prompt manageable
    allowlist_str = "\n".join(allowlist)

    return f"""You are writing new entries for the Pomegra Wiki — a reader-friendly
encyclopedia of the financial world that ships at https://pomegra.io/wiki/.

# Your bucket
- Category: **{cat}**
- Sub-category: **{sub}**
- Target directory: `{target_dir}/`
- Number of new entries to write: **{gap}**
- Slugs already in this bucket (don't re-write these): {existing if existing else "(empty bucket)"}

# Your task
Pick {gap} concrete, well-defined finance topics that fit the **{cat}/{sub}** bucket.
Each topic must be something a thoughtful reader of `/wiki/{cat}/` would
plausibly want explained. Avoid overlap with the existing slugs above.
For each topic, create a new markdown file at `{target_dir}/<slug>.md`.

# Editorial contract (HARD requirements — non-negotiable)

**Length**: 900–1300 words. Substantial enough to be useful, short enough
that the reader finishes.

**Voice**: confident, magazine-editor tone. NOT a textbook, NOT a chatbot,
NOT marketing copy.
- Commit to definitions ("A stock is …", not "A stock can be thought of as …").
- One or two editorial flourishes per article — used sparingly, never forced.
- Mark contested claims ("Most economists use X; some prefer Y").
- Cut hedging filler ("essentially", "basically", "it's worth noting that").

**Must NOT appear (these are deal-breakers — the user will reject the article):**
- "Mermaid" as visible text. ```` ```mermaid ```` code fences are FINE if you
  use one, but never write the literal word "Mermaid" as a heading or caption.
- "Placeholder", "scaffolded", "coming soon", "[next article placeholder]",
  "BOOKS_PLAN", or any meta-commentary about authoring.
- AI tells — "as a wiki entry", "in this article we will", "as we discussed",
  "let's dive in", "I hope this helps".
- Engine names or implementation details — never "Hugo", "Markdown", "site
  generator", "page weight", etc.

**Structure** of every entry, in order:
1. Front matter (between `---`):
   ```yaml
   ---
   title: "Title Case Title"
   description: "One sentence (150-200 chars) — what this entry covers, used as the meta description and search snippet."
   ---
   ```
2. Lede paragraph: a single paragraph wrapped in single asterisks `*…*` — the
   markdown-italic lede that the CSS auto-styles. 2-4 sentences, plain language.
3. Optionally: a `<div class="wiki-hatnote">…</div>` disambiguation line.
4. Optionally: an `<aside class="wiki-infobox">` with key facts:
   ```html
   <aside class="wiki-infobox">
     <div class="wiki-infobox-title">{{Topic}} — key facts</div>
     <table>
       <tr><th>Type</th><td>…</td></tr>
       <tr><th>Issuer</th><td>…</td></tr>
       <tr><th>Typical use</th><td>…</td></tr>
     </table>
   </aside>
   ```
5. 4–6 `##` section headings — each a real claim or question, not a bare noun.
   Example: `## Why the curve usually slopes up` is better than `## The curve`.
6. Closing block:
   ```html
   <div class="wiki-seealso">
   <h2>See also</h2>
   <h3>Closely related</h3>
   <ul>
     <li><a href="/wiki/slug-1/">Title 1</a> — one-line gloss.</li>
     <li><a href="/wiki/slug-2/">Title 2</a> — one-line gloss.</li>
   </ul>
   <h3>Wider context</h3>
   <ul>
     <li><a href="/wiki/slug-3/">Title 3</a> — one-line gloss.</li>
   </ul>
   </div>
   ```

**Cross-links (CRITICAL — fabricated links break the wiki):**
- 5–12 inline cross-links per article using `[anchor text](/wiki/slug/)`.
- **EVERY link target slug MUST appear in the allowlist at the bottom of this
  prompt.** If a slug isn't on the list, don't link to it. Use the closest
  available slug or rephrase without a link. NEVER invent slugs.
- Trailing slash is required: `/wiki/foo/` not `/wiki/foo`.
- The leading `/wiki/` prefix is required — Hugo's `canonifyURLs` setting
  rewrites root-absolute links to include the base, but using `/wiki/` directly
  is unambiguous and survives renames.

# Output

For each of the {gap} new entries:
1. Pick a clear, specific slug (lowercase, hyphens, no spaces).
2. Write the file at `{target_dir}/<slug>.md` using the Write tool.
3. Do not stop until all {gap} files exist.

If you hit a hard ceiling (output budget, etc.) before finishing, list the
slugs you DID write at the end of your final response so the orchestrator
can dispatch a follow-up agent.

# Cross-link allowlist
The following {len(allowlist)} slugs exist in `content/` right now. You may
ONLY cross-link to these (always as `/wiki/<slug>/`). Adding a slug that
isn't on this list will silently break — the build will succeed but the
link will 404 for readers.

<allowlist>
{allowlist_str}
</allowlist>
"""


def main() -> int:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    allowlist = build_allowlist()
    OUT.mkdir(exist_ok=True)
    # Clean previous prompts
    for old in OUT.glob("*.md"):
        old.unlink()

    written = 0
    for bucket in plan:
        if bucket["gap"] == 0:
            continue
        name = f"{bucket['category']}__{bucket['subcat']}.md"
        (OUT / name).write_text(prompt_for(bucket, allowlist), encoding="utf-8")
        written += 1

    print(f"Wrote {written} prompts to {OUT}")
    print(f"Allowlist size: {len(allowlist)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

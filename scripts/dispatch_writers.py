#!/usr/bin/env python3
"""Phase 3 of the no-dup swarm: emit writer prompts with EXPLICIT file lists.

Reads scripts/_locked_plan.json and groups the locked entries into writer
batches (default ~14 per agent). Each prompt file in scripts/_writer_prompts/
lists the exact (slug, title, target path) assignments for that agent — the
agent has zero topic freedom and cannot collide with another agent. The
editorial contract + cross-link allowlist are baked in, same as before.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SCRIPTS = Path(__file__).resolve().parent
LOCKED = SCRIPTS / "_locked_plan.json"
OUT = SCRIPTS / "_writer_prompts"

BATCH = 13  # entries per writer agent


def allowlist_plus_planned(planned_slugs: list[str]) -> list[str]:
    """Existing slugs + every slug we are about to create this run.

    Including the planned slugs lets writers cross-link to sibling new
    entries — they are guaranteed to exist on disk by the end of the run.
    """
    existing = {p.stem for p in CONTENT.rglob("*.md") if not p.stem.startswith("_")}
    return sorted(existing | set(planned_slugs))


def prompt_for(batch_id: str, entries: list[dict], allowlist: list[str]) -> str:
    allowlist_str = "\n".join(allowlist)
    rows = "\n".join(
        f"{i+1}. `{(ROOT / e['dir'] / (e['slug'] + '.md')).as_posix()}`  —  title: \"{e['title']}\""
        + (f"  —  angle: {e['angle']}" if e.get("angle") else "")
        for i, e in enumerate(entries)
    )
    n = len(entries)
    return f"""You are writing finished entries for the Pomegra Wiki — a reader-friendly
encyclopedia of the financial world that ships at https://pomegra.io/wiki/.

# Your assignment (FIXED — do not deviate)
Write exactly these {n} entries. The filename, directory and title are
ASSIGNED. Do NOT invent your own topics, do NOT rename files, do NOT add
extras, do NOT skip any. Create each file at the EXACT ABSOLUTE path shown —
pass that absolute path verbatim to the Write tool. Do NOT prepend or append
any directory segments; do NOT nest the path inside itself.

{rows}

# Editorial contract (HARD requirements — non-negotiable)

**Length**: 900–1300 words. Substantial but finishable.

**Voice**: confident magazine-editor tone. NOT a textbook, NOT a chatbot,
NOT marketing copy.
- Commit to definitions ("A stock is …", not "can be thought of as …").
- One or two editorial flourishes per article, used sparingly.
- Mark contested claims ("Most economists use X; some prefer Y").
- Cut hedging filler ("essentially", "basically", "it's worth noting that").

**Must NOT appear (deal-breakers — the entry will be rejected):**
- The literal visible word "Mermaid". ```` ```mermaid ```` fences are FINE;
  captions must say "Decision tree" / "Flowchart" or have no caption.
- "Placeholder", "scaffolded", "coming soon", "TODO", meta-commentary.
- AI tells — "in this article we will", "let's dive in", "I hope this helps",
  "in summary", first-person opinion.
- Engine/tool names (Hugo, Markdown, etc.).

**Structure** of every entry, in order:
1. Front matter between `---`:
   ```yaml
   ---
   title: "The Assigned Title"
   description: "One sentence, 150-200 chars — what this entry covers."
   keywords:
     - 4 to 8 lowercase keyword phrases
   ---
   ```
   Use the EXACT assigned title. Do NOT put HTML in the description.
2. Lede: one paragraph wrapped in single asterisks `*…*`. 2–4 sentences,
   names the thing and locates it. Bold the entry name on first mention.
3. Optionally a `<div class="wiki-hatnote">…</div>` disambiguation line.
4. An `<aside class="wiki-infobox">` with a key-facts table (4–9 rows).
   Blank lines required around inner block elements so they parse.
5. 4–6 `##` section headings — each a real claim or question, not a bare
   noun. "## Why the curve usually slopes up" beats "## The curve".
6. Closing `<div class="wiki-seealso">` with `### Closely related` and
   `### Wider context` lists, each item a link plus a one-line gloss.

**Cross-links (CRITICAL — fabricated links break the wiki):**
- 5–12 inline cross-links per article using `[anchor](/wiki/slug/)`.
- EVERY target slug MUST be in the allowlist below. If a slug isn't listed,
  don't link it — reword instead. NEVER invent a slug.
- Trailing slash required: `/wiki/foo/` not `/wiki/foo`.
- The leading `/wiki/` prefix is required.

# Output
Use the Write tool to create each of the {n} files at its exact assigned
path. Do not stop until all {n} exist. If you hit an output limit, list the
slugs you DID write at the end so the orchestrator can finish them.

# Cross-link allowlist
You may ONLY cross-link to these {len(allowlist)} slugs (always as
`/wiki/<slug>/`). They include both entries already on disk and the entries
being written in this run, so linking to a sibling assignment is safe.

<allowlist>
{allowlist_str}
</allowlist>
"""


def main() -> int:
    locked = json.loads(LOCKED.read_text(encoding="utf-8"))
    planned_slugs = [e["slug"] for e in locked]
    allowlist = allowlist_plus_planned(planned_slugs)

    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()

    batches = [locked[i:i + BATCH] for i in range(0, len(locked), BATCH)]
    for idx, entries in enumerate(batches):
        bid = f"w{idx:02d}"
        # Ensure target dirs exist so writers never fail on mkdir.
        for e in entries:
            (ROOT / e["dir"]).mkdir(parents=True, exist_ok=True)
        (OUT / f"{bid}.md").write_text(prompt_for(bid, entries, allowlist), encoding="utf-8")

    print(f"locked entries: {len(locked)}")
    print(f"writer batches: {len(batches)} (<= {BATCH} each)")
    print(f"allowlist size: {len(allowlist)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

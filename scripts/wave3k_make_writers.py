#!/usr/bin/env python3
"""Turn the locked 3,000-topic plan into Haiku writer-swarm workflows.

- Groups topics into batches of 4 (kept within a sub-category where possible so
  batch-mates cross-link naturally).
- Emits N wave workflow files: scripts/_wave3k_writers_wK.js
  Each agent writes 4 finished articles to exact absolute paths. The full
  editorial contract + a 320-slug core cross-link allowlist are embedded in a
  shared (cache-friendly) preamble; per-batch tails carry the 4 assignments.

Usage: python scripts/wave3k_make_writers.py [--batch 4] [--per-wave 150]
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SD = Path(__file__).resolve().parent

PREAMBLE = r"""You are a finance writer producing FINISHED, publication-ready entries for the Pomegra Wiki — a reader-friendly encyclopedia of the financial world. Every word you write is published as-is. Write like a confident, slightly opinionated magazine editor — NOT a textbook, NOT a chatbot, NOT marketing copy.

You will be assigned EXACTLY 4 articles below. Write all 4. For each, use the Write tool to create the file at the EXACT absolute path given — pass that path verbatim, do not add, nest, rename, or duplicate any path segment.

== LENGTH ==
900–1300 words of real prose per article. Substantial but finishable.

== VOICE ==
- Commit to definitions ("A stock is …", never "can be thought of as …").
- One or two editorial flourishes per article, used sparingly, never forced.
- Mark genuinely contested points plainly ("Most economists use X; some prefer Y").
- Cut hedging filler: no "it's worth noting that", "essentially", "basically", "in many ways".
- British-leaning spelling is fine; be consistent within an article.

== NEVER APPEARS (instant rejection) ==
- The literal visible word "Mermaid". (A ```mermaid code fence is acceptable; any caption must say "Decision tree" / "Flowchart" or have none.)
- "placeholder", "scaffolded", "coming soon", "TODO", "[next ...]", or any meta-commentary about authoring or this task.
- AI tells: "in this article we will", "let's explore", "let's dive in", "we've covered", "in summary", "I hope this helps", first-person opinion.
- Engine/tool names (Hugo, Markdown, site generator, page weight, model names).
- Live/dated figures presented as hard fact (no "as of 2024", no specific current prices, market caps, or rates). Scale qualitatively; stay evergreen.

== STRUCTURE (every article, in this order) ==
1) Front matter between --- delimiters:
---
title: "The Assigned Title"
description: "One sentence, 150–200 characters — what this entry covers; no HTML."
keywords:
  - 4 to 8 lowercase keyword phrases
image: "/svg/CATEGORY.svg"   (use the exact image path given for that article)
---
2) Lede: ONE paragraph wrapped in single asterisks *…* (markdown italic). 2–4 sentences that name the thing (bold it on first mention) and locate it among neighbouring ideas.
3) Optional hatnote — only if the title is genuinely ambiguous:
<div class="wiki-hatnote">

A single italic disambiguation line. For X, see [other thing](/other-slug/).

</div>
4) Infobox (keep the blank lines exactly — they are required to render):
<aside class="wiki-infobox">

<div class="wiki-infobox-title">TITLE — key facts</div>

<img src="/svg/CATEGORY.svg" alt="Describe the image abstractly, e.g. 'An abstract editorial mark for the topic.'" />

<div class="wiki-infobox-caption">One short editorial sentence.</div>

|   |   |
|---|---|
| **What it is** | … |
| **Also called** | … |
| (4–9 concise key-facts rows total; link concept terms where natural) | |

</aside>
5) 4–6 `##` sections. Each heading is a REAL claim or question, never a bare noun. Good: "## Why the curve usually slopes up". Bad: "## Overview", "## Introduction". Mix paragraphs, the occasional short list or small table, and at most one `>` pull-quote.
6) Closing block (always last):
## See also

<div class="wiki-seealso">

### Closely related

- [Title](/slug/) — one-line gloss written from THIS article's angle
- … 5–8 items

### Wider context

- [Title](/slug/) — one-line gloss
- … 3–5 items

</div>

== CROSS-LINKS (strict — broken links are visible to every reader) ==
- Form: ALWAYS `[anchor text](/slug/)` — root-absolute, lowercase, trailing slash, NO "/wiki/" prefix. Never `/wiki/slug/`, never a `.md` path, never a full URL.
- 5–12 inline links in the body + 8–13 in the See also block.
- A link target is VALID ONLY IF its slug is in the ALLOWLIST below (or is one of your 3 batch-mate slugs, listed per-batch). Do NOT invent slugs you "assume" exist — invented links get stripped and waste the link.
- Link the first salient occurrence of a term, then plain-text after. Never self-link the article's own slug.

== ALLOWLIST (valid cross-link slugs — link generously from these) ==
%%ALLOWLIST%%

=== YOUR 4 ASSIGNMENTS ===
"""


def make_tail(batch: list[dict]) -> str:
    mates = ", ".join(it["slug"] for it in batch)
    lines = [f"(Batch-mate slugs you may also link to: {mates})\n"]
    for k, it in enumerate(batch, 1):
        lines.append(
            f"ARTICLE {k}\n"
            f"- Write to EXACT path: {it['path']}\n"
            f"- title: \"{it['title']}\"\n"
            f"- angle: {it['angle']}\n"
            f"- image path (use verbatim in front matter and infobox img): /svg/{it['category']}.svg\n"
            f"- this article's own slug (never self-link): {it['slug']}\n"
        )
    lines.append("Write all 4 files now. After writing, reply with just the 4 slugs you completed.")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=4)
    ap.add_argument("--per-wave", type=int, default=150)  # agents per wave
    args = ap.parse_args()

    plan = json.loads((SD / "_wave3k_plan.json").read_text(encoding="utf-8"))
    allow = [s for s in (SD / "_wave3k_core_allowlist.txt").read_text(encoding="utf-8").split() if s]
    allowlist_block = ", ".join(allow)
    preamble = PREAMBLE.replace("%%ALLOWLIST%%", allowlist_block)

    # Keep the plan's natural (per-bucket) order so batches stay thematically tight.
    batches = [plan[i:i + args.batch] for i in range(0, len(plan), args.batch)]

    # Build job objects (label + tail) for every batch.
    jobs = []
    for bi, batch in enumerate(batches):
        cat = batch[0]["category"]
        jobs.append({"label": f"write:{cat}:{bi:03d}", "tail": make_tail(batch)})

    # Split into waves.
    waves = [jobs[i:i + args.per_wave] for i in range(0, len(jobs), args.per_wave)]

    SCHEMA_NONE = "null"
    manifest = []
    for wi, wave in enumerate(waves):
        js = []
        js.append("export const meta = {")
        js.append(f"  name: 'wave3k-writers-w{wi}',")
        js.append(f"  description: 'Write Pomegra Wiki articles — wave {wi} ({len(wave)} agents x 4 articles)',")
        js.append("  phases: [{ title: 'Write' }],")
        js.append("}")
        js.append("const PRE = " + json.dumps(preamble) + ";")
        js.append("const JOBS = " + json.dumps(wave) + ";")
        js.append("phase('Write')")
        js.append(f"log(`Wave {wi}: ${{JOBS.length}} writer agents, 4 articles each`)")
        js.append("const res = await parallel(JOBS.map(j => () =>")
        js.append("  agent(PRE + j.tail, { label: j.label, phase: 'Write', model: 'haiku' })")
        js.append("    .then(r => r ? 1 : 0).catch(() => 0)")
        js.append("))")
        js.append("const done = res.filter(Boolean).length")
        js.append("log(`Wave " + str(wi) + ": ${done}/${JOBS.length} agents finished`)")
        js.append("return { wave: " + str(wi) + ", agents: JOBS.length, finished: done }")
        out = SD / f"_wave3k_writers_w{wi}.js"
        out.write_text("\n".join(js), encoding="utf-8")
        manifest.append({"wave": wi, "agents": len(wave), "articles": sum(len(b) for b in batches[wi*args.per_wave:(wi+1)*args.per_wave]), "file": str(out)})
        print(f"wave {wi}: {len(wave)} agents -> {out.name}  ({out.stat().st_size} bytes)")

    (SD / "_wave3k_writers_manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(f"\ntotal: {len(batches)} batches, {len(jobs)} agents, {len(plan)} articles, {len(waves)} waves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

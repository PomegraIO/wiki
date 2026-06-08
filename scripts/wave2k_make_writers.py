#!/usr/bin/env python3
"""Turn the locked 2,000 long-tail plan into Haiku writer-swarm waves.
Same engine as wave3k_make_writers, with an SEO targeting block + advice guard.
Usage: python scripts/wave2k_make_writers.py [--batch 4] [--per-wave 130]
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SD = Path(__file__).resolve().parent

PREAMBLE = r"""You are a finance writer producing FINISHED, publication-ready entries for the Pomegra Wiki — a reader-friendly encyclopedia of the financial world. Every word is published as-is. Write like a confident, plain-speaking magazine editor — NOT a textbook, NOT a chatbot, NOT marketing copy.

These entries target specific LONG-TAIL search queries, so they must directly and fully answer the question a searcher had in mind — while staying genuinely useful and evergreen.

You will be assigned EXACTLY 4 articles below. Write all 4. For each, use the Write tool to create the file at the EXACT absolute path given — pass that path verbatim; never add, nest, rename, or duplicate a path segment.

== SEO TARGETING (do this naturally — never keyword-stuff) ==
- Each assignment gives a target KEYWORD. Work it, or a natural close variant, into: the `description`, the FIRST sentence of the lede, and at least one `##` heading. It is already in the title.
- Open by answering the query directly in the first 1–2 sentences (the searcher should feel "yes, this is the page"), then go deeper.
- Cover the specifics the query implies — the comparison, the calculation, the threshold, the scenario, the example. Concrete worked examples and small tables help.

== EDUCATIONAL, NOT ADVICE (hard rule) ==
- Explain how things work and what factors decide an outcome. NEVER tell the reader to buy/sell/hold, never declare something "a good investment," never give personalised recommendations. Recast any "should I…" framing as "what determines whether…".
- Evergreen only: no current prices, rates, or dated ("as of 2024") figures as hard facts; scale qualitatively.

== LENGTH ==
900–1300 words of real prose per article.

== VOICE ==
- Commit to definitions. One or two editorial flourishes per article, used sparingly.
- Mark genuinely contested points plainly. Cut hedging filler ("it's worth noting that", "essentially", "basically").
- Consistent spelling within an article.

== NEVER APPEARS (instant rejection) ==
- The literal visible word "Mermaid" (a ```mermaid fence is fine; captions say "Decision tree"/"Flowchart" or none).
- "placeholder", "scaffolded", "coming soon", "TODO", meta-commentary about authoring or slugs.
- AI tells: "in this article we will", "let's explore", "let's dive in", "in summary", "I hope this helps", first-person opinion.
- Engine/tool names (Hugo, Markdown, etc.).

== STRUCTURE (every article, in order) ==
1) Front matter between --- delimiters:
---
title: "The Assigned Title"
description: "150–200 chars containing the target keyword; no HTML."
keywords:
  - 4 to 8 lowercase keyword phrases (include the target keyword)
image: "/svg/CATEGORY.svg"
---
2) Lede: ONE paragraph wrapped in *…* (markdown italic), 2–4 sentences, answering the query up front; bold the main term on first mention.
3) Optional hatnote (only if the title is genuinely ambiguous): <div class="wiki-hatnote"> … </div> with blank lines inside.
4) Infobox (keep blank lines exactly):
<aside class="wiki-infobox">

<div class="wiki-infobox-title">TITLE — key facts</div>

<img src="/svg/CATEGORY.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One short editorial sentence.</div>

|   |   |
|---|---|
| **Short answer** | … |
| (4–9 concise rows; link concept terms where natural) | |

</aside>
5) 4–6 `##` sections, each a REAL claim or question (good: "## How the 30-day window is counted"; bad: "## Overview"). At least one heading carries the keyword. Mix prose, the occasional short list or small table, at most one `>` pull-quote.
6) Closing block (always last):
## See also

<div class="wiki-seealso">

### Closely related

- [Title](/slug/) — one-line gloss from THIS article's angle
- … 5–8 items

### Wider context

- [Title](/slug/) — one-line gloss
- … 3–5 items

</div>

== CROSS-LINKS (strict — broken links are visible) ==
- Form ALWAYS `[anchor](/slug/)` — root-absolute, lowercase, trailing slash, NO "/wiki/" prefix. Never `/wiki/slug/`, never `.md`, never a full URL.
- 5–12 inline links + 8–13 in See also. Link a target ONLY if its slug is in the ALLOWLIST below or is one of your 3 batch-mate slugs. Don't invent slugs — invented links get stripped.
- Link first salient occurrence only; never self-link.

== ALLOWLIST (valid cross-link slugs) ==
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
            f"- target keyword: {it.get('keyword') or it['title']}\n"
            f"- angle (the query to answer): {it['angle']}\n"
            f"- image path (verbatim in front matter + infobox img): /svg/{it['category']}.svg\n"
            f"- this article's own slug (never self-link): {it['slug']}\n"
        )
    lines.append("Write all 4 files now. After writing, reply with just the 4 slugs you completed.")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=4)
    ap.add_argument("--per-wave", type=int, default=130)
    ap.add_argument("--conc", type=int, default=8, help="max concurrent agents per workflow")
    ap.add_argument("--plan", default="_wave2k_plan.json", help="input plan/missing file")
    args = ap.parse_args()

    plan = json.loads((SD / args.plan).read_text(encoding="utf-8"))
    allow = [s for s in (SD / "_wave2k_core_allowlist.txt").read_text(encoding="utf-8").split() if s]
    preamble = PREAMBLE.replace("%%ALLOWLIST%%", ", ".join(allow))

    batches = [plan[i:i + args.batch] for i in range(0, len(plan), args.batch)]
    jobs = [{"label": f"seo-write:{b[0]['category']}:{bi:03d}", "tail": make_tail(b)}
            for bi, b in enumerate(batches)]
    waves = [jobs[i:i + args.per_wave] for i in range(0, len(jobs), args.per_wave)]

    manifest = []
    for wi, wave in enumerate(waves):
        js = []
        js.append("export const meta = {")
        js.append(f"  name: 'wave2k-writers-w{wi}',")
        js.append(f"  description: 'Write long-tail Pomegra Wiki articles — wave {wi} ({len(wave)} agents x 4)',")
        js.append("  phases: [{ title: 'Write' }],")
        js.append("}")
        js.append("const PRE = " + json.dumps(preamble) + ";")
        js.append("const JOBS = " + json.dumps(wave) + ";")
        js.append(f"const CONC = {args.conc};")
        js.append("phase('Write')")
        js.append(f"log(`Wave {wi}: ${{JOBS.length}} writers x 4, concurrency ${{CONC}}`)")
        js.append("let done = 0;")
        js.append("for (let i = 0; i < JOBS.length; i += CONC) {")
        js.append("  const chunk = JOBS.slice(i, i + CONC);")
        js.append("  const res = await parallel(chunk.map(j => () =>")
        js.append("    agent(PRE + j.tail, { label: j.label, phase: 'Write', model: 'haiku' })")
        js.append("      .then(r => r ? 1 : 0).catch(() => 0)));")
        js.append("  done += res.filter(Boolean).length;")
        js.append(f"  log(`Wave {wi}: ${{done}}/${{JOBS.length}} done`);")
        js.append("}")
        js.append(f"return {{ wave: {wi}, agents: JOBS.length, finished: done }}")
        out = SD / f"_wave2k_writers_w{wi}.js"
        out.write_text("\n".join(js), encoding="utf-8")
        manifest.append({"wave": wi, "agents": len(wave), "file": str(out)})
        print(f"wave {wi}: {len(wave)} agents -> {out.name} ({out.stat().st_size} bytes)")
    (SD / "_wave2k_writers_manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(f"\ntotal: {len(batches)} batches, {len(jobs)} agents, {len(plan)} articles, {len(waves)} waves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

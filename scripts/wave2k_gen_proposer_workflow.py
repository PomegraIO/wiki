#!/usr/bin/env python3
"""Emit a Workflow JS that proposes 2,000 long-tail, low/medium-competition
keyword topics for the Pomegra Wiki (one Sonnet agent per subcategory)."""
from __future__ import annotations
import json
from pathlib import Path

SD = Path(__file__).resolve().parent
OUT = SD / "_wave2k_proposer_workflow.js"

PREAMBLE = """You are an SEO content strategist + finance editor choosing NEW article topics for the Pomegra Wiki (a reader-friendly encyclopedia of finance, already ~17,000 pages). GOAL: capture organic search traffic from LONG-TAIL, LOW/MEDIUM-COMPETITION keywords — the specific queries real people type that big sites under-serve.

WHAT MAKES A GOOD LONG-TAIL TARGET
- Specific, usually a 3–7 word query with clear intent. NOT a broad head term.
- Lower competition than the obvious one-word concept. Prefer the narrow, the specific, the situational.
- Genuine, answerable, evergreen finance question a wiki can answer well in ~1,000 words.
- High-yield long-tail patterns to mine:
  * Calculations / thresholds: "how is X taxed", "X 30-day rule", "how to calculate X", "minimum X to do Y".
  * Comparisons: "X vs Y", "X or Y for [goal]", "difference between X and Y".
  * Mechanics in a scenario: "what happens to X when Y", "how X works in a [situation]".
  * Persona / situation: "X for retirees", "X for self-employed", "X for a small account".
  * Narrow sub-concepts not yet covered, and "X explained with an example".

HARD RULES
- LOW or MEDIUM competition only. If the best phrasing is a high-competition head term (e.g. "what is a stock", "dividend"), SKIP it.
- Do NOT duplicate, or trivially rephrase, any existing slug listed in the assignment. No near-duplicates.
- Real, answerable topics only — no invented jargon, no clickbait, no get-rich/hype angles.
- Educational & evergreen: a topic may FRAME a decision ("when X makes sense") but must NOT be investment advice ("should I buy X"). No specific prices or dated figures.
- Concepts/questions only — not a specific company, ticker, fund, or named person.
- Quality over quantity: return FEWER than the quota rather than padding with weak or high-competition picks. Each distinct from the others.

FIELDS PER PROPOSAL
- slug: lowercase, hyphen-joined, ASCII, keyword-rich and URL-friendly (e.g. "how-are-etf-dividends-taxed", "preferred-stock-vs-bonds", "wash-sale-30-day-rule"). Globally unique.
- title: a clean Title Case headline that contains the target keyword and reads like an encyclopedia entry (e.g. "ETF Dividend Taxation", "Preferred Stock vs Bonds"). Question-form titles are allowed only when that IS the natural query.
- keyword: the exact long-tail search phrase you are targeting (lowercase).
- angle: ONE sentence on the specific question the article answers.
- competition: your honest estimate, "low" or "medium" (never include high-competition picks).

OUTPUT: return ONLY via the structured output tool. Up to the quota; fewer if needed.

=== YOUR ASSIGNMENT ===
"""

TAIL = """Category: {category}  ({cat_desc})
Sub-category: {subcat}
Propose UP TO {quota} long-tail topics for this bucket.
EXISTING SLUGS HERE (avoid these + near-duplicates): {existing}"""

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["category", "subcat", "dir", "proposals"],
    "properties": {
        "category": {"type": "string"}, "subcat": {"type": "string"}, "dir": {"type": "string"},
        "proposals": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["slug", "title", "keyword", "angle", "competition"],
            "properties": {
                "slug": {"type": "string"}, "title": {"type": "string"},
                "keyword": {"type": "string"}, "angle": {"type": "string"},
                "competition": {"type": "string", "enum": ["low", "medium"]},
            },
        }},
    },
}


def main() -> int:
    briefs = json.loads((SD / "_wave2k_briefs.json").read_text(encoding="utf-8"))
    jobs = []
    for b in briefs:
        existing = ", ".join(b["existing_slugs"]) if b["existing_slugs"] else "(none yet)"
        jobs.append({
            "label": f'seo:{b["category"]}/{b["subcat"]}',
            "cat": b["category"], "sub": b["subcat"], "dir": b["dir"],
            "tail": TAIL.format(category=b["category"], cat_desc=b["cat_desc"],
                                subcat=b["subcat"], quota=b["quota"], existing=existing),
        })
    js = []
    js.append("export const meta = {")
    js.append("  name: 'wave2k-seo-proposers',")
    js.append("  description: 'Propose 2,000 long-tail low/medium-competition wiki topics (one agent per subcategory)',")
    js.append("  phases: [{ title: 'Propose' }],")
    js.append("}")
    js.append("const PREAMBLE = " + json.dumps(PREAMBLE) + ";")
    js.append("const JOBS = " + json.dumps(jobs) + ";")
    js.append("const SCHEMA = " + json.dumps(SCHEMA) + ";")
    js.append("phase('Propose')")
    js.append("log(`Long-tail proposals across ${JOBS.length} buckets`)")
    js.append("const results = await parallel(JOBS.map(j => () =>")
    js.append("  agent(PREAMBLE + j.tail, { label: j.label, phase: 'Propose', schema: SCHEMA, model: 'sonnet' })")
    js.append("    .then(r => r ? { cat: j.cat, sub: j.sub, dir: j.dir, proposals: r.proposals || [] } : null)")
    js.append("))")
    js.append("const ok = results.filter(Boolean)")
    js.append("const total = ok.reduce((n, r) => n + r.proposals.length, 0)")
    js.append("log(`Got ${total} raw long-tail proposals from ${ok.length}/${JOBS.length} buckets`)")
    js.append("return { buckets: ok, totalProposals: total }")
    OUT.write_text("\n".join(js), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(jobs)} agents)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

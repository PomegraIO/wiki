#!/usr/bin/env python3
"""Emit a self-contained Workflow JS that proposes 3,000 new wiki topics.

Each (category, subcat) brief becomes one Sonnet agent with a fully-embedded
prompt (no file-reading needed at run time). The script returns an array of
per-bucket proposal objects, which the aggregator dedups + trims to 3,000.
"""
from __future__ import annotations
import json
from pathlib import Path

SD = Path(__file__).resolve().parent
OUT = SD / "_wave3k_proposer_workflow.js"

PREAMBLE = """You are a finance encyclopedia editor proposing NEW entry topics for the Pomegra Wiki — a reader-friendly reference covering the whole financial world. It already has ~14,000 pages, so your job is to surface the genuinely-distinct, established concepts NOT yet covered in the assigned bucket.

WHAT A GOOD PROPOSAL IS
- A REAL, established finance/economics concept an intelligent reader would look up — an instrument, mechanism, ratio, method, institution-type, phenomenon, rule, or strategy. Second- and third-tier concepts are exactly what we want; the obvious ones are already written.
- Specific and teachable on its own as a ~1,000-word article. Not a vague theme.
- Squarely inside the assigned category / sub-category.

HARD RULES
- Do NOT propose anything whose slug matches, or is a trivial rephrase of, an existing slug listed in the assignment. No near-duplicates.
- Do NOT propose a specific company, ticker, fund, or named person — concepts only (naming a person inside an angle is fine).
- Do NOT invent jargon or coin terms. Only concepts that genuinely exist in finance literature/practice.
- Quality over quantity: if the bucket is nearly exhausted of distinct real concepts, return FEWER than the quota. Never pad with filler or hair-splitting variants.
- Every proposal distinct from the others you return.

SLUG RULES
- slug: lowercase, hyphen-joined, ASCII, derived from the title (e.g. "Key Rate Duration" -> key-rate-duration). Globally unique and descriptive; avoid bare one-word slugs that could collide.
- title: Title Case, the natural name of the concept.
- angle: ONE sentence (<=18 words) stating the specific facet the article explains, so related topics don't blur.

OUTPUT: return ONLY via the structured output tool. Up to the quota; fewer if needed.

=== YOUR ASSIGNMENT ===
"""

TAIL = """Category: {category}  ({cat_desc})
Sub-category: {subcat}
Propose UP TO {quota} new topics for this bucket.
EXISTING SLUGS IN THIS BUCKET (avoid these and near-duplicates): {existing}"""

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["category", "subcat", "dir", "proposals"],
    "properties": {
        "category": {"type": "string"},
        "subcat": {"type": "string"},
        "dir": {"type": "string"},
        "proposals": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["slug", "title", "angle"],
                "properties": {
                    "slug": {"type": "string"},
                    "title": {"type": "string"},
                    "angle": {"type": "string"},
                },
            },
        },
    },
}


def main() -> int:
    briefs = json.loads((SD / "_wave3k_briefs.json").read_text(encoding="utf-8"))
    jobs = []
    for i, b in enumerate(briefs):
        existing = ", ".join(b["existing_slugs"]) if b["existing_slugs"] else "(none yet)"
        tail = TAIL.format(
            category=b["category"], cat_desc=b["cat_desc"], subcat=b["subcat"],
            quota=b["quota"], existing=existing,
        )
        jobs.append({
            "label": f'propose:{b["category"]}/{b["subcat"]}',
            "cat": b["category"], "sub": b["subcat"], "dir": b["dir"],
            "tail": tail,
        })

    js = []
    js.append("export const meta = {")
    js.append("  name: 'wave3k-proposers',")
    js.append("  description: 'Propose 3,000 new Pomegra Wiki concept topics (one agent per subcategory)',")
    js.append("  phases: [{ title: 'Propose' }],")
    js.append("}")
    js.append("const PREAMBLE = " + json.dumps(PREAMBLE) + ";")
    js.append("const JOBS = " + json.dumps(jobs) + ";")
    js.append("const SCHEMA = " + json.dumps(SCHEMA) + ";")
    js.append("phase('Propose')")
    js.append("log(`Proposing topics across ${JOBS.length} buckets`)")
    js.append("const results = await parallel(JOBS.map(j => () =>")
    js.append("  agent(PREAMBLE + j.tail, { label: j.label, phase: 'Propose', schema: SCHEMA, model: 'sonnet' })")
    js.append("    .then(r => r ? { cat: j.cat, sub: j.sub, dir: j.dir, proposals: r.proposals || [] } : null)")
    js.append("))")
    js.append("const ok = results.filter(Boolean)")
    js.append("const totalProposals = ok.reduce((n, r) => n + r.proposals.length, 0)")
    js.append("log(`Got ${totalProposals} raw proposals from ${ok.length}/${JOBS.length} buckets`)")
    js.append("return { buckets: ok, totalProposals }")

    OUT.write_text("\n".join(js), encoding="utf-8")
    print(f"wrote {OUT}  ({OUT.stat().st_size} bytes, {len(jobs)} agents)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

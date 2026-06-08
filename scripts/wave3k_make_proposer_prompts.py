#!/usr/bin/env python3
"""Generate one self-contained proposer prompt per subcategory brief.

Each file scripts/_wave3k_prompts/b###.md fully instructs a proposer agent to
return up-to-quota genuinely-distinct, established finance concepts for one
(category, subcat) bucket, avoiding the slugs already on disk. The agent reads
its file and emits structured JSON — no other context is needed.
"""
from __future__ import annotations
import json, shutil
from pathlib import Path

SD = Path(__file__).resolve().parent
OUT = SD / "_wave3k_prompts"

HEADER = """You are a finance encyclopedia editor proposing NEW entry topics for the \
Pomegra Wiki — a reader-friendly reference covering the whole financial world. \
The wiki already has ~14,000 pages, so your job is to find the genuinely-distinct, \
established concepts that are NOT yet covered in this bucket.

# Your bucket
- Category: **{category}**  ({cat_desc})
- Sub-category: **{subcat}**
- Propose UP TO **{quota}** new topics for this bucket.

# What a good proposal is
- A REAL, established finance/economics concept that an intelligent reader would \
plausibly look up — an instrument, mechanism, ratio, method, institution-type, \
phenomenon, rule, or strategy. Second- and third-tier concepts are exactly what \
we want; the obvious ones are already written.
- Specific and teachable on its own as a 1,000-word article. Not a vague theme.
- Squarely inside the **{category} / {subcat}** bucket.

# Hard rules
- Do NOT propose anything whose slug matches, or is a trivial rephrase of, an \
existing slug listed below. No near-duplicates.
- Do NOT propose a specific company, ticker, fund, or a named person (those live \
in other parts of the wiki). Concepts only. (Naming a person inside an *angle* is \
fine; the topic itself must be a concept.)
- Do NOT invent jargon or coin terms. Only concepts that genuinely exist in \
finance literature/practice.
- Quality over quantity. If the bucket is nearly exhausted of distinct real \
concepts, return FEWER than {quota} — never pad with filler or hair-splitting \
variations of the same idea.
- Each proposal must be distinct from the others you return.

# Slug rules
- `slug`: lowercase, words joined by single hyphens, ASCII only, derived from the \
title (e.g. "Key Rate Duration" -> `key-rate-duration`). Must be globally unique \
and descriptive enough to stand alone (avoid bare one-word slugs that could collide).
- `title`: Title Case, the natural name of the concept.
- `angle`: ONE sentence (max ~18 words) stating the specific thing the article \
explains — its distinct facet, so two related topics don't blur together.

# Existing slugs in THIS bucket (avoid these and their near-duplicates)
{existing}

# Output
Return ONLY via the structured output tool, with this exact shape:
{{ "category": "{category}", "subcat": "{subcat}", "dir": "{dir}",
   "proposals": [ {{ "slug": "...", "title": "...", "angle": "..." }}, ... ] }}
Aim for high-quality, non-overlapping topics. Up to {quota}; fewer if needed.
"""


def main() -> int:
    briefs = json.loads((SD / "_wave3k_briefs.json").read_text(encoding="utf-8"))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for i, b in enumerate(briefs):
        existing = b["existing_slugs"]
        existing_block = ", ".join(existing) if existing else "(none yet — this bucket is empty)"
        txt = HEADER.format(
            category=b["category"], cat_desc=b["cat_desc"], subcat=b["subcat"],
            quota=b["quota"], dir=b["dir"], existing=existing_block,
        )
        (OUT / f"b{i:03d}.md").write_text(txt, encoding="utf-8")
    # manifest used by the aggregator to know how many prompts exist
    (SD / "_wave3k_proposer_count.txt").write_text(str(len(briefs)), encoding="utf-8")
    print(f"wrote {len(briefs)} proposer prompts to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

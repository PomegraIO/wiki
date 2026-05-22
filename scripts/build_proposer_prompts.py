#!/usr/bin/env python3
"""Emit one proposer-agent prompt per brief in scripts/_proposer_prompts/.

A proposer only invents NAMES (slug + title + one-line angle) for genuinely
new finance topics in its assigned buckets, writing them to a JSON file. No
article bodies. The full taken-slug list is embedded so proposers avoid
collisions up front; the orchestrator dedups again centrally afterwards.
"""
from __future__ import annotations
import json
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
BRIEFS = SCRIPTS / "_proposer_briefs.json"
TAKEN = SCRIPTS / "_existing_slugs.txt"
OUT = SCRIPTS / "_proposer_prompts"


def prompt_for(brief: dict, taken_str: str) -> str:
    bucket_lines = []
    for b in brief["buckets"]:
        existing = ", ".join(b["existing_in_bucket"]) if b["existing_in_bucket"] else "(none yet)"
        bucket_lines.append(
            f"- **{b['category']}/{b['subcat']}** — propose **{b['propose']}** new topics.\n"
            f"  Already covered here (do NOT repeat): {existing}"
        )
    buckets_block = "\n".join(bucket_lines)
    total = brief["total_propose"]
    out_file = brief["out_file"]
    return f"""You are a finance encyclopedia editor planning new entries for the Pomegra
Wiki. Your ONLY job in this task is to propose NAMES for new articles — no
article bodies. You will output a JSON file of candidate topics.

# Your buckets and quotas
{buckets_block}

For each bucket, propose the requested number of concrete, well-defined,
DISTINCT finance topics that genuinely belong in that (category/sub-category)
and that a thoughtful reader would want explained. Topics must be real,
specific concepts — instruments, ratios, mechanisms, institutions, events,
strategies — not vague themes.

# Hard rules
- Every proposed slug MUST be brand new: it must NOT appear in the "already
  taken" list below, and must not duplicate another topic you propose.
- slug = lowercase, hyphen-separated, no spaces, ASCII only
  (e.g. `interest-rate-collar`, `sovereign-wealth-fund`).
- title = Title-case human name (e.g. "Interest Rate Collar").
- Keep topics non-overlapping: "covered call" and "covered-call strategy" are
  the same topic — pick one.
- Spread across the bucket's subject; don't cluster on near-synonyms.

# Output (use the Write tool)
Write a single JSON file to this exact path:
  `{out_file}`
The file must be a JSON array of objects, each with these keys:
  {{"slug": "...", "title": "...", "category": "...", "subcat": "...", "angle": "one short clause on what it covers"}}
Use the exact category and subcat strings from the bucket list above. Produce
about {total} objects total (the sum of the per-bucket quotas). Output ONLY
the JSON file via the Write tool — no prose reply needed beyond a one-line
confirmation.

# Already-taken slugs (NEVER propose any of these)
<taken>
{taken_str}
</taken>
"""


def main() -> int:
    briefs = json.loads(BRIEFS.read_text(encoding="utf-8"))
    taken_str = TAKEN.read_text(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()
    for brief in briefs:
        (OUT / f"{brief['proposer_id']}.md").write_text(prompt_for(brief, taken_str), encoding="utf-8")
    print(f"wrote {len(briefs)} proposer prompts to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

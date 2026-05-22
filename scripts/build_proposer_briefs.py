#!/usr/bin/env python3
"""Phase 1 of the no-dup swarm: split the gap buckets into proposer briefs.

Each proposer agent is handed a disjoint set of (category, sub-category)
buckets and asked to PROPOSE candidate (slug, title) pairs — names only, no
article bodies. The orchestrator then dedups every proposal against the
existing on-disk slugs and against each other BEFORE any writer runs. This is
the mechanism that prevents the duplicate-article waste: names are locked at
planning time.

Outputs:
  scripts/_proposer_briefs.json  — list of briefs, one per proposer agent
  scripts/_existing_slugs.txt    — the full taken-slug set (avoid list)
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SCRIPTS = Path(__file__).resolve().parent
GAP_PLAN = SCRIPTS / "_gap_plan.json"

# How many proposer agents to split the work across. Each covers a disjoint
# slice of the gap buckets, so cross-proposer collisions are unlikely (and
# central dedup catches any that slip through).
NUM_PROPOSERS = 14
# Ask for a small buffer above the gap so dedup attrition still leaves enough.
BUFFER = 1.35


def existing_slugs() -> list[str]:
    return sorted(p.stem for p in CONTENT.rglob("*.md") if not p.stem.startswith("_"))


def main() -> int:
    plan = json.loads(GAP_PLAN.read_text(encoding="utf-8"))
    gap_buckets = [b for b in plan if b["gap"] > 0]
    # Largest gaps first so they spread evenly across proposers.
    gap_buckets.sort(key=lambda b: b["gap"], reverse=True)

    # Round-robin buckets into proposer groups to balance total propose-count.
    groups: list[list[dict]] = [[] for _ in range(NUM_PROPOSERS)]
    loads = [0] * NUM_PROPOSERS
    for b in gap_buckets:
        i = loads.index(min(loads))
        propose = max(b["gap"], int(round(b["gap"] * BUFFER)))
        groups[i].append({
            "category": b["category"],
            "subcat": b["subcat"],
            "dir": b["dir"],
            "propose": propose,
            "existing_in_bucket": b["existing_slugs"],
        })
        loads[i] += propose

    briefs = []
    for idx, g in enumerate(groups):
        if not g:
            continue
        briefs.append({
            "proposer_id": f"p{idx:02d}",
            "buckets": g,
            "total_propose": sum(x["propose"] for x in g),
            "out_file": f"scripts/_proposals/p{idx:02d}.json",
        })

    (SCRIPTS / "_proposer_briefs.json").write_text(json.dumps(briefs, indent=2), encoding="utf-8")
    slugs = existing_slugs()
    (SCRIPTS / "_existing_slugs.txt").write_text("\n".join(slugs), encoding="utf-8")
    (SCRIPTS / "_proposals").mkdir(exist_ok=True)

    print(f"existing slugs (taken): {len(slugs)}")
    print(f"gap buckets: {len(gap_buckets)}")
    print(f"proposer briefs: {len(briefs)}")
    for b in briefs:
        print(f"  {b['proposer_id']}: {len(b['buckets'])} buckets, propose {b['total_propose']}")
    print(f"total to propose: {sum(b['total_propose'] for b in briefs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

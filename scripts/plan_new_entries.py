#!/usr/bin/env python3
"""Compute the gap between current and target entry counts per sub-category.

Writes scripts/_gap_plan.json describing where new articles need to land:
[
  {
    "category": "derivatives",
    "subcat": "option-strategies",
    "current": 0,
    "target": 30,
    "gap": 30,
    "dir": "content/derivatives/option-strategies",
    "existing_slugs": ["..."]
  },
  ...
]

Run scripts/migrate_into_subdirs.py first so the count reflects the new
structure. The swarm dispatcher reads this file and assigns batches.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT = Path(__file__).resolve().parent / "_gap_plan.json"


def main() -> int:
    plan = []
    total_gap = 0
    for cat, subcats in TAXONOMY.items():
        for subcat, target, _ in subcats:
            subdir = CONTENT / cat / subcat
            slugs = sorted(p.stem for p in subdir.glob("*.md")) if subdir.exists() else []
            current = len(slugs)
            gap = max(0, target - current)
            total_gap += gap
            plan.append({
                "category": cat,
                "subcat": subcat,
                "current": current,
                "target": target,
                "gap": gap,
                "dir": f"content/{cat}/{subcat}",
                "existing_slugs": slugs,
            })

    OUT.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    nonzero = [p for p in plan if p["gap"] > 0]
    print(f"Wrote {OUT}")
    print(f"sub-categories needing entries: {len(nonzero)}/{len(plan)}")
    print(f"total entries to write: {total_gap}")
    # Show the biggest gaps
    nonzero.sort(key=lambda p: p["gap"], reverse=True)
    print("\nLargest gaps (top 20):")
    for p in nonzero[:20]:
        print(f"  {p['gap']:4}  {p['category']}/{p['subcat']}  (have {p['current']}, want {p['target']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

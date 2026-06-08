#!/usr/bin/env python3
"""Dedup + trim proposer output to exactly 3,000, assign paths, lock the plan.

Reads scripts/_wave3k_proposals.json  (the proposer-workflow return value:
   { "buckets": [ {cat, sub, dir, proposals:[{slug,title,angle}]}, ... ] } )
Writes scripts/_wave3k_plan.json       (the locked, de-duplicated assignment list)
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

SD = Path(__file__).resolve().parent
ROOT = SD.parent
TARGET = 3000

SLUG_RX = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def norm_slug(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("_", "-").replace(" ", "-").replace("/", "-")
    s = re.sub(r"[^a-z0-9-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def main() -> int:
    existing = set((SD / "_wave3k_existing.txt").read_text(encoding="utf-8").split())
    data = json.loads((SD / "_wave3k_proposals.json").read_text(encoding="utf-8"))
    buckets = data["buckets"] if isinstance(data, dict) else data

    seen: set[str] = set()
    kept: list[dict] = []
    dropped_dup = dropped_existing = dropped_bad = 0
    by_bucket: dict[str, list[dict]] = {}

    for b in buckets:
        cat, sub = b["cat"], b["sub"]
        key = f"{cat}/{sub}"
        for p in b.get("proposals", []):
            slug = norm_slug(p.get("slug", ""))
            if not slug or not SLUG_RX.match(slug) or len(slug) < 3:
                dropped_bad += 1
                continue
            if slug in existing:
                dropped_existing += 1
                continue
            if slug in seen:
                dropped_dup += 1
                continue
            seen.add(slug)
            item = {
                "slug": slug,
                "title": p.get("title", "").strip() or slug.replace("-", " ").title(),
                "angle": p.get("angle", "").strip(),
                "category": cat,
                "subcat": sub,
            }
            kept.append(item)
            by_bucket.setdefault(key, []).append(item)

    print(f"raw kept (unique, valid, new): {len(kept)}")
    print(f"dropped — already exist: {dropped_existing}, intra-dup: {dropped_dup}, malformed: {dropped_bad}")

    # Trim to TARGET with a balanced round-robin drop from the largest buckets.
    if len(kept) > TARGET:
        excess = len(kept) - TARGET
        order = sorted(by_bucket.values(), key=len, reverse=True)
        drop_ids = set()
        while excess > 0:
            for lst in order:
                if len(lst) - sum(1 for x in lst if id(x) in drop_ids) <= 3:
                    continue  # keep at least 3 per bucket
                for x in reversed(lst):
                    if id(x) not in drop_ids:
                        drop_ids.add(id(x)); excess -= 1; break
                if excess == 0:
                    break
        kept = [x for x in kept if id(x) not in drop_ids]
        print(f"trimmed to {len(kept)} (balanced)")
    elif len(kept) < TARGET:
        print(f"** SHORTFALL: only {len(kept)} unique topics (< {TARGET}). Top-up pass needed. **")

    # Assign absolute output paths.
    for it in kept:
        rel = f"content/{it['category']}/{it['subcat']}/{it['slug']}.md"
        it["path"] = str((ROOT / rel).resolve()).replace("\\", "/")
        it["rel"] = rel

    (SD / "_wave3k_plan.json").write_text(json.dumps(kept, indent=1), encoding="utf-8")

    # Distribution report
    from collections import Counter
    cat_counts = Counter(it["category"] for it in kept)
    print(f"\nLOCKED {len(kept)} topics across {len(cat_counts)} categories")
    for c, n in cat_counts.most_common():
        print(f"  {n:4}  {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

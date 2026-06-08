#!/usr/bin/env python3
"""Dedup + trim wave-2k long-tail proposals to exactly 2,000, lock the plan.
Reads scripts/_seo3_proposals.json ; writes scripts/_seo3_plan.json .
Keeps keyword + competition fields. Drops any high-competition stragglers.
"""
from __future__ import annotations
import json, re, sys
from collections import Counter
from pathlib import Path

SD = Path(__file__).resolve().parent
ROOT = SD.parent
TARGET = 500
sys.path.insert(0, str(SD))
from wave3k_lock import norm_slug, SLUG_RX


def main() -> int:
    existing = set((SD / "_seo3_existing.txt").read_text(encoding="utf-8").split())
    data = json.loads((SD / "_seo3_proposals.json").read_text(encoding="utf-8"))
    buckets = data["buckets"]

    seen: set[str] = set()
    kept: list[dict] = []
    drop_dup = drop_exist = drop_bad = drop_comp = 0
    by_bucket: dict[str, list[dict]] = {}
    for b in buckets:
        cat, sub = b["cat"], b["sub"]
        for p in b.get("proposals", []):
            slug = norm_slug(p.get("slug", ""))
            if not slug or not SLUG_RX.match(slug) or len(slug) < 3:
                drop_bad += 1; continue
            if (p.get("competition") or "low").lower() == "high":
                drop_comp += 1; continue
            if slug in existing:
                drop_exist += 1; continue
            if slug in seen:
                drop_dup += 1; continue
            seen.add(slug)
            item = {
                "slug": slug,
                "title": (p.get("title") or slug.replace("-", " ").title()).strip(),
                "keyword": (p.get("keyword") or "").strip(),
                "angle": (p.get("angle") or "").strip(),
                "competition": (p.get("competition") or "low").strip().lower(),
                "category": cat, "subcat": sub,
            }
            kept.append(item)
            by_bucket.setdefault(f"{cat}/{sub}", []).append(item)

    print(f"raw kept (unique/valid/new): {len(kept)}")
    print(f"dropped — exist:{drop_exist} dup:{drop_dup} bad:{drop_bad} high-comp:{drop_comp}")

    if len(kept) > TARGET:
        from collections import deque
        queues = [deque(v) for v in by_bucket.values()]
        picked = []
        while len(picked) < TARGET and any(queues):
            for q in queues:
                if q:
                    picked.append(q.popleft())
                    if len(picked) >= TARGET:
                        break
        kept = picked
        print(f"trimmed to {len(kept)} (round-robin balanced)")
    elif len(kept) < TARGET:
        print(f"** SHORTFALL: {len(kept)} < {TARGET} — top-up pass needed **")

    for it in kept:
        rel = f"content/{it['category']}/{it['subcat']}/{it['slug']}.md"
        it["path"] = str((ROOT / rel).resolve()).replace("\\", "/")
        it["rel"] = rel
    (SD / "_seo3_plan.json").write_text(json.dumps(kept, indent=1), encoding="utf-8")

    cc = Counter(it["category"] for it in kept)
    comp = Counter(it["competition"] for it in kept)
    print(f"\nLOCKED {len(kept)} across {len(cc)} categories | competition mix: {dict(comp)}")
    for c, n in cc.most_common():
        print(f"  {n:4}  {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

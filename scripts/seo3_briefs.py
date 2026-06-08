#!/usr/bin/env python3
"""Wave-2k (SEO long-tail) planning: briefs for 2,000 new concept entries
targeted at low/medium-competition long-tail keywords.

Outputs (scripts/):
  _seo3_existing.txt        every slug on disk now (~17k after wave-3k) — global dedup set
  _seo3_core_allowlist.txt  top-N most-linked concept slugs — writer cross-link vocabulary
  _seo3_briefs.json         per (category,subcat) brief: intent-weighted quota + existing slugs

Quotas are weighted toward high-search-intent consumer areas (taxes, personal
finance, real estate, crypto, ...) where long-tail organic traffic concentrates.
"""
from __future__ import annotations
import json, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY
from wave3k_briefs import CAT_DESC  # reuse category one-liners

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SD = Path(__file__).resolve().parent

CORE_N = 360
TARGET_TOTAL = 500
OVERASK = 760  # sum of quotas before dedup/trim

# Search-intent weight per category (higher = more long-tail organic demand).
INTENT = {
    "personal-finance": 1.8, "taxes": 1.8, "real-estate": 1.5, "crypto": 1.5,
    "strategies": 1.2, "funds": 1.2, "ratios": 1.2, "technical-analysis": 1.2,
    "fixed-income": 1.1, "valuation": 1.1, "trading": 1.1, "equity": 1.1,
    "behavioral": 1.0, "commodities": 1.0, "forex": 1.0, "markets": 1.0,
    "accounting": 1.0, "derivatives": 0.9, "corporate": 0.9, "risk": 0.9,
    "people": 0.8, "regulation": 0.8, "macro": 0.8, "history": 0.7,
    "monetary": 0.7, "fiscal": 0.7, "institutions": 0.7,
}


def all_disk_slugs() -> set[str]:
    return {p.stem for p in CONTENT.rglob("*.md") if p.name != "_index.md"}


def core_allowlist(all_slugs: set[str]) -> list[str]:
    company = {p.stem for p in (CONTENT / "companies").rglob("*.md")}
    concept = all_slugs - company
    link_rx = re.compile(r'(?:\]\(|href=["\'])/([a-z0-9][a-z0-9-]*)/')
    counts: Counter[str] = Counter()
    for p in CONTENT.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in link_rx.finditer(txt):
            if m.group(1) in concept:
                counts[m.group(1)] += 1
    return sorted(s for s, _ in counts.most_common(CORE_N))


def main() -> int:
    all_slugs = all_disk_slugs()
    (SD / "_seo3_existing.txt").write_text("\n".join(sorted(all_slugs)), encoding="utf-8")
    core = core_allowlist(all_slugs)
    (SD / "_seo3_core_allowlist.txt").write_text("\n".join(core), encoding="utf-8")

    # weight each subcat by its category intent; scale so the total hits OVERASK
    weight_sum = 0.0
    subs = []
    for cat in TAXONOMY:
        for subcat, target, _kw in TAXONOMY[cat]:
            w = INTENT.get(cat, 1.0)
            subs.append((cat, subcat, w))
            weight_sum += w
    K = OVERASK / weight_sum

    briefs = []
    total = 0
    for i, (cat, subcat, w) in enumerate(subs):
        q = max(3, round(K * w))
        total += q
        d = CONTENT / cat / subcat
        existing = sorted(p.stem for p in d.glob("*.md")) if d.is_dir() else []
        briefs.append({
            "id": f"s{i:03d}", "category": cat, "subcat": subcat,
            "cat_desc": CAT_DESC.get(cat, cat), "dir": f"content/{cat}/{subcat}",
            "quota": q, "existing_slugs": existing,
        })
    (SD / "_seo3_briefs.json").write_text(json.dumps(briefs, indent=1), encoding="utf-8")
    print(f"disk slugs (dedup set): {len(all_slugs)}")
    print(f"core allowlist: {len(core)}")
    print(f"briefs: {len(briefs)} | sum quotas (over-ask): {total} | target {TARGET_TOTAL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

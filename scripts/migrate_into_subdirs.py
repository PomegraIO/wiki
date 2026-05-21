#!/usr/bin/env python3
"""Move every article in content/<category>/<slug>.md into
content/<category>/<sub-category>/<slug>.md.

Sub-category is decided by `taxonomy.category_for_slug` (keyword match
against the filename). Files that match no keyword land in the
`general/` bucket for that category.

Idempotent: articles already inside a sub-dir are left alone unless
their current location no longer matches the taxonomy — in which case
they are moved to the right bucket.

Hugo's permalink rule `'/**' = '/:contentbasename/'` makes this safe:
the URL stays /<slug>/ regardless of how deep the markdown file lives.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY, category_for_slug

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"


def main() -> int:
    moved = 0
    untouched = 0
    by_subcat: dict[str, int] = {}
    for cat in sorted(CONTENT.iterdir()):
        if not cat.is_dir():
            continue
        if cat.name not in TAXONOMY:
            print(f"[skip] {cat.name} — no taxonomy entry, leaving flat")
            continue

        # Walk every .md file in this category tree (current depth: 1 or 2).
        for md in cat.rglob("*.md"):
            if md.name.startswith("_"):
                continue
            slug = md.stem
            want_subcat = category_for_slug(cat.name, slug)
            target = cat / want_subcat / md.name
            if md.resolve() == target.resolve():
                untouched += 1
                by_subcat[f"{cat.name}/{want_subcat}"] = by_subcat.get(f"{cat.name}/{want_subcat}", 0) + 1
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            md.rename(target)
            moved += 1
            by_subcat[f"{cat.name}/{want_subcat}"] = by_subcat.get(f"{cat.name}/{want_subcat}", 0) + 1

    # Sanity: prune any now-empty intermediate directories that used to
    # hold articles directly (no children left).
    for cat in CONTENT.iterdir():
        if not cat.is_dir():
            continue
        for sub in list(cat.rglob("*")):
            if sub.is_dir() and not any(sub.iterdir()):
                sub.rmdir()

    print(f"moved={moved} untouched={untouched}")
    print(f"\nDistribution after migration:")
    for k in sorted(by_subcat):
        print(f"  {by_subcat[k]:4}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

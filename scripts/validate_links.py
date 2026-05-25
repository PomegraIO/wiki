#!/usr/bin/env python3
"""
validate_links.py — verify internal links in built company pages resolve.

After `hugo --gc --minify`, this scans the rendered HTML for a set of company
pages and confirms every internal href points at a directory that actually
exists in public/. Also flags the double-prefix bug (/wiki/wiki/).

Usage:
  python scripts/validate_links.py --letter z
  python scripts/validate_links.py --all
Run from repo root after a build.
"""
from __future__ import annotations
import argparse, glob, os, re, sys

PUBLIC = "public"
BASE = "https://pomegra.io/wiki/"


def rendered_pages(letter: str | None):
    # company slugs come from content filenames; rendered at public/<slug>/index.html
    pat = os.path.join("content", "companies", letter or "*", "*-stock.md")
    for md in sorted(glob.glob(pat)):
        slug = os.path.basename(md)[:-3]
        html = os.path.join(PUBLIC, slug, "index.html")
        if os.path.isfile(html):
            yield slug, html


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--letter")
    g.add_argument("--all", action="store_true")
    args = ap.parse_args()
    letter = None if args.all else args.letter.lower()

    href_rx = re.compile(r'href=["\']?(https://pomegra\.io/wiki/[^"\'\s>]+)')
    broken, double, checked, pages = [], [], 0, 0
    for slug, html in rendered_pages(letter):
        pages += 1
        txt = open(html, encoding="utf-8", errors="replace").read()
        for m in href_rx.finditer(txt):
            url = m.group(1)
            path = url[len(BASE):]              # e.g. "recession/"
            if path.startswith("wiki/"):
                double.append((slug, url)); continue
            target = path.split("#")[0].split("?")[0].rstrip("/")
            if not target:                      # site root
                continue
            # A page link is a single slug segment with no extension. Anything
            # with a "/" (img/x.png) or a "." (sitemap.xml) is a static asset.
            if "/" in target or "." in target:
                continue
            checked += 1
            if not os.path.isfile(os.path.join(PUBLIC, target, "index.html")):
                broken.append((slug, url))

    print(f"pages scanned: {pages}   internal links checked: {checked}")
    if double:
        print(f"\nDOUBLE-PREFIX (/wiki/wiki/) — {len(double)}:")
        for s, u in double[:50]:
            print(f"  {s}: {u}")
    if broken:
        print(f"\nBROKEN (target missing in public/) — {len(broken)}:")
        for s, u in broken[:50]:
            print(f"  {s}: {u}")
    if not broken and not double:
        print("\nOK — every internal link resolves, no double-prefix.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

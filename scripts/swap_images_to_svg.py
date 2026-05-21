#!/usr/bin/env python3
"""Replace every Picsum/Unsplash image URL in content/**/*.md with the
local category SVG at /svg/<category>.svg. The category is taken from the
article's parent directory.

Touches both:
- front-matter `image:` lines
- inline body `<img src="..."/>` tags (used in the existing in-body
  <aside class="wiki-infobox"> blocks)

Idempotent: any article whose image is already a /svg/<category>.svg URL
is left untouched.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
SVG_DIR = ROOT / 'static' / 'svg'

# Match either a stock-photo URL or an existing /svg/<cat>.svg that no
# longer matches the article's current location.
STOCK_HOSTS = re.compile(r'https?://(?:picsum\.photos|images\.unsplash\.com)/[^"\'\s)]+|/svg/[a-z-]+\.svg')

# Categories that have a matching /static/svg/<cat>.svg file.
ALLOWED = {p.stem for p in SVG_DIR.glob('*.svg')}


def category_for(path: Path) -> str:
    """Pick the subdirectory under content/ as the category; fall back to default."""
    rel = path.relative_to(CONTENT)
    parts = rel.parts
    if len(parts) >= 2 and parts[0] in ALLOWED:
        return parts[0]
    return 'default'


def process(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    cat = category_for(path)
    target = f'/svg/{cat}.svg'
    new = STOCK_HOSTS.sub(target, text)
    if new == text:
        return 0
    path.write_text(new, encoding='utf-8')
    return 1


def main() -> int:
    changed = 0
    total = 0
    for path in sorted(CONTENT.rglob('*.md')):
        total += 1
        changed += process(path)
    print(f'Rewrote stock-photo URLs in {changed} files (of {total}).')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""For each content/*.md, extract the first `<img src="...">` URL found in the
body and write it back as `image:` in the front matter (if not already set).
This unlocks Open Graph tags, the home-page featured-entry card, and any
future feature that wants the hero image of an article.

Idempotent. Run from project root:  python scripts/extract_hero_image.py
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

SKIP = {'_index.md', 'about.md', 'index-a-z.md'}
FRONT_MATTER_RE = re.compile(r'^(---\n)(.*?)(\n---\n)', re.DOTALL)
IMG_RE = re.compile(r'<img[^>]*\bsrc\s*=\s*"([^"]+)"', re.IGNORECASE)


def process(path: Path) -> bool:
    if path.name in SKIP:
        return False
    text = path.read_text(encoding='utf-8')
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return False
    fm = m.group(2)
    if re.search(r'^image\s*:', fm, re.MULTILINE):
        return False  # already set
    body = text[m.end():]
    img = IMG_RE.search(body)
    if not img:
        return False
    new_fm = fm.rstrip() + f'\nimage: "{img.group(1)}"'
    new_text = m.group(1) + new_fm + m.group(3) + body
    path.write_text(new_text, encoding='utf-8')
    return True


def main() -> None:
    n = 0
    for p in sorted(CONTENT.glob('*.md')):
        if process(p):
            n += 1
            print(f'  added image: {p.name}')
    print(f'Done. {n} files updated.')


if __name__ == '__main__':
    main()

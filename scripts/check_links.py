#!/usr/bin/env python3
"""Scan every content/**/*.md for cross-links and verify each target exists
on disk. Prints a broken-link report.

With `--fix`, rewrites broken links inline:
- markdown `[label](/bad-slug/)` -> plain text `label`
- raw HTML `<a href="/bad-slug/">label</a>` -> plain text `label`

Run from project root:
    python scripts/check_links.py
    python scripts/check_links.py --fix
"""
from __future__ import annotations
import argparse
import io
import re
import sys
from collections import defaultdict
from pathlib import Path

# Force UTF-8 stdout/stderr on Windows so report characters render
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

# Capture (label, slug) for markdown links.
MD_LINK_RE = re.compile(r'\[([^\]\n]+?)\]\(/([a-z0-9][a-z0-9-]*)/?\)')
# Capture (slug, label) for HTML anchors.
HTML_LINK_RE = re.compile(
    r'<a\s+[^>]*?\bhref=["\']/([a-z0-9][a-z0-9-]*)/?["\'][^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)

# Site-wide pages that are always valid targets.
SITE_PAGES = {'about', 'index-a-z'}


def article_slugs() -> set[str]:
    slugs: set[str] = set()
    for path in CONTENT.rglob('*.md'):
        if path.name == '_index.md':
            continue
        slugs.add(path.stem)
    return slugs | SITE_PAGES


def fix(text: str, valid: set[str]) -> tuple[str, int]:
    """Rewrite broken cross-links inline. Returns (new_text, fix_count)."""
    fixed = 0

    def md_sub(m):
        nonlocal fixed
        label, slug = m.group(1), m.group(2)
        if slug in valid:
            return m.group(0)
        fixed += 1
        return label  # strip the link, keep the label text

    def html_sub(m):
        nonlocal fixed
        slug = m.group(1)
        if slug in valid:
            return m.group(0)
        fixed += 1
        return m.group(2)  # inner HTML/text

    new_text = MD_LINK_RE.sub(md_sub, text)
    new_text = HTML_LINK_RE.sub(html_sub, new_text)
    return new_text, fixed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--fix', action='store_true', help='Rewrite broken links in place')
    args = parser.parse_args()

    valid = article_slugs()
    broken_by_file: dict[str, set[str]] = defaultdict(set)
    files_changed = 0
    total_files = 0
    total_links = 0
    total_fixed = 0

    for path in sorted(CONTENT.rglob('*.md')):
        total_files += 1
        text = path.read_text(encoding='utf-8')
        targets: set[str] = set()
        targets.update(m.group(2) for m in MD_LINK_RE.finditer(text))
        targets.update(m.group(1) for m in HTML_LINK_RE.finditer(text))
        total_links += len(targets)
        rel = path.relative_to(CONTENT).as_posix()
        for t in targets:
            if t not in valid:
                broken_by_file[rel].add(t)

        if args.fix:
            new_text, n = fix(text, valid)
            if n:
                path.write_text(new_text, encoding='utf-8')
                files_changed += 1
                total_fixed += n

    if args.fix:
        print(f'FIXED -- {total_fixed} broken links rewritten across {files_changed} files (of {total_files}).')
    else:
        if not broken_by_file:
            print(f'OK -- {total_links} unique cross-links across {total_files} files, all valid.')
            return 0
        total_broken = sum(len(v) for v in broken_by_file.values())
        print(f'BROKEN -- {total_broken} broken targets across {len(broken_by_file)} files (of {total_files}).')
        # Show top 30 most-broken files with a few examples
        worst = sorted(broken_by_file.items(), key=lambda kv: -len(kv[1]))[:30]
        for rel, slugs in worst:
            sample = sorted(slugs)[:4]
            print(f'  {rel} ({len(slugs)} broken): {", ".join("/" + s + "/" for s in sample)}')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

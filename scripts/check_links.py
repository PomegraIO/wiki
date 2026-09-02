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

# Capture (label, slug) for markdown links - both the canonical `/slug/` form
# and the legacy `/wiki/slug/` form (canonifyURLs resolves both to the same
# page, so a dangling target 404s identically in either spelling).
MD_LINK_RE = re.compile(r'\[([^\]\n]+?)\]\((?:/wiki)?/([a-z0-9][a-z0-9-]*)/?\)')
# Capture (slug, label) for HTML anchors.
HTML_LINK_RE = re.compile(
    r'<a\s+[^>]*?\bhref=["\'](?:/wiki)?/([a-z0-9][a-z0-9-]*)/?["\'][^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)

# Every markdown link destination (not just the well-formed ones above), so we
# can flag the shapes that resolve to crawlable 404s: no leading slash, an
# interior slash (category path / phantom /link/ route), a .md filename, or
# markdown syntax leaking into the destination. Search Console reported ~3.4k
# such URLs before this check existed. Images (`![alt](...)`) are excluded.
ANY_MD_TARGET_RE = re.compile(r'(?<!\!)\[[^\]\n]*\]\(\s*([^)\s]+)\s*\)')
ANY_HTML_HREF_RE = re.compile(r'<a\s+[^>]*?\bhref=["\']([^"\']+)["\']', re.IGNORECASE)
CANONICAL_TARGET_RE = re.compile(r'^/([a-z0-9][a-z0-9-]*)/?$')
LEGACY_WIKI_TARGET_RE = re.compile(r'^/wiki/([a-z0-9][a-z0-9-]*)/?$')
ALLOWED_TARGET_PREFIXES = ('http://', 'https://', 'mailto:', '#', '/#', '/img/', '/svg/', '/page/', '/wiki/img/')
ASSET_EXTENSIONS = ('.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.ico', '.pdf')


def classify_target(target: str) -> tuple[str, str | None]:
    """Return (kind, slug). kind is 'ok' (external/anchor/asset), 'slug' (a
    wiki entry to verify) or a malformed-shape label."""
    if target == '/' or target.startswith(ALLOWED_TARGET_PREFIXES):
        return 'ok', None  # wiki home, anchors, external, static assets
    if target.lower().endswith(ASSET_EXTENSIONS):
        return 'ok', None
    m = CANONICAL_TARGET_RE.match(target)
    if m:
        return 'slug', m.group(1)
    m = LEGACY_WIKI_TARGET_RE.match(target)
    if m:
        return 'slug', m.group(1)
    if target.startswith('/link/'):
        return 'phantom-link-route', None
    if target.endswith('.md') or target.endswith('.md/'):
        return 'md-filename', None
    if target.startswith('('):
        return 'unparsed-markdown', None
    if not target.startswith('/'):
        return 'relative-path', None
    if re.fullmatch(r'/(?:wiki/)?[A-Za-z0-9-]+/?', target):
        # Single segment that failed the lowercase match: nginx is
        # case-sensitive, so `/10-K/` never resolves to `/10-k/`.
        return 'uppercase-slug', None
    if target.rstrip('/').count('/') >= 2:
        return 'category-path', None
    return 'malformed', None

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
    parser.add_argument('--strict', action='store_true',
                        help='Exit non-zero on ANY broken or malformed link target (build gate)')
    args = parser.parse_args()

    valid = article_slugs()
    broken_by_file: dict[str, set[str]] = defaultdict(set)
    malformed_by_file: dict[str, list[tuple[str, str]]] = defaultdict(list)
    malformed_kinds: dict[str, int] = defaultdict(int)
    files_changed = 0
    total_files = 0
    total_links = 0
    total_fixed = 0

    for path in sorted(CONTENT.rglob('*.md')):
        total_files += 1
        # newline='' keeps CRLF/LF byte-for-byte so --fix never churns line endings.
        with path.open(encoding='utf-8', newline='') as fh:
            text = fh.read()
        targets: set[str] = set()
        targets.update(m.group(2) for m in MD_LINK_RE.finditer(text))
        targets.update(m.group(1) for m in HTML_LINK_RE.finditer(text))
        total_links += len(targets)
        rel = path.relative_to(CONTENT).as_posix()
        for t in targets:
            if t not in valid:
                broken_by_file[rel].add(t)

        # Shape check on every destination, including the ones the slug regexes
        # above cannot see (relative, nested, .md, /link/, unparsed markdown).
        raw_targets: set[str] = set()
        raw_targets.update(m.group(1) for m in ANY_MD_TARGET_RE.finditer(text))
        raw_targets.update(m.group(1) for m in ANY_HTML_HREF_RE.finditer(text))
        for t in raw_targets:
            kind, slug = classify_target(t)
            if kind == 'ok':
                continue
            if kind == 'slug':
                if slug not in valid:
                    broken_by_file[rel].add(slug)
                continue
            malformed_by_file[rel].append((kind, t))
            malformed_kinds[kind] += 1

        if args.fix:
            new_text, n = fix(text, valid)
            if n:
                with path.open('w', encoding='utf-8', newline='') as fh:
                    fh.write(new_text)
                files_changed += 1
                total_fixed += n

    rc = 0
    if args.fix:
        print(f'FIXED -- {total_fixed} broken links rewritten across {files_changed} files (of {total_files}).')
    else:
        if not broken_by_file:
            print(f'OK -- {total_links} unique cross-links across {total_files} files, all valid.')
        else:
            total_broken = sum(len(v) for v in broken_by_file.values())
            print(f'BROKEN -- {total_broken} broken targets across {len(broken_by_file)} files (of {total_files}).')
            # Show top 30 most-broken files with a few examples
            worst = sorted(broken_by_file.items(), key=lambda kv: -len(kv[1]))[:30]
            for rel, slugs in worst:
                sample = sorted(slugs)[:4]
                print(f'  {rel} ({len(slugs)} broken): {", ".join("/" + s + "/" for s in sample)}')
            rc = 1

    if malformed_by_file:
        total_malformed = sum(len(v) for v in malformed_by_file.values())
        print(f'MALFORMED -- {total_malformed} link targets across {len(malformed_by_file)} files '
              f'will resolve to 404s: ' + ', '.join(f'{k}={v}' for k, v in sorted(malformed_kinds.items())))
        worst = sorted(malformed_by_file.items(), key=lambda kv: -len(kv[1]))[:30]
        for rel, items in worst:
            sample = ', '.join(f'{t} [{k}]' for k, t in items[:3])
            print(f'  {rel} ({len(items)}): {sample}')
        print('  fix with: python3 scripts/fix_relative_links.py && python3 scripts/fix_malformed_links.py')
        rc = 1
    elif not args.fix:
        print(f'OK -- no malformed link targets (relative, category-path, /link/, .md).')

    if args.strict and rc:
        print('STRICT -- refusing to pass with broken or malformed links.', file=sys.stderr)
        return 1
    return rc if not args.fix else 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Apply (or revert) noindex front matter for a batch of wiki URLs.

Reads a batch file of wiki URLs (one per line, '#' comments and blanks
ignored — the format scripts/prune_candidates.py emits), maps each URL to its
content file by basename, and appends three keys to the front matter:

    noindex: true
    noindex_date: "YYYY-MM-DD"
    noindex_reason: "delisted"    # or "no-demand"

Editing is line-based (same approach as scripts/migrate.py): untouched keys
keep their exact formatting and order; the new keys land just before the
closing '---'. Idempotent both ways — a file that already has `noindex:` is
skipped on apply, and --revert strips exactly the three keys and is a no-op
when they are absent.

Run from project root:
    python scripts/apply_noindex.py --batch scripts/_noindex_batch1.txt --reason delisted --dry-run
    python scripts/apply_noindex.py --batch scripts/_noindex_batch1.txt --reason no-demand
    python scripts/apply_noindex.py --batch scripts/_noindex_batch1.txt --revert

(The keys only take effect once the layouts emit a robots meta tag for
`.Params.noindex` — coordinate with the template change before a real run.)
"""
from __future__ import annotations
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

# Tolerates the UTF-8 BOM + CRLF line endings some company pages carry;
# insertions reuse the file's own line-ending style so nothing else churns.
FRONT_MATTER_RE = re.compile(r'^(\ufeff?---\r?\n)(.*?\r?\n)(---\r?\n)', re.DOTALL)
NOINDEX_KEYS = ('noindex', 'noindex_date', 'noindex_reason')
KEY_LINE_RE = re.compile(r'^(?:' + '|'.join(NOINDEX_KEYS) + r')\s*:')


def basename_index() -> dict[str, Path]:
    idx: dict[str, Path] = {}
    for p in CONTENT.rglob('*.md'):
        if p.name == '_index.md':
            continue
        idx[p.stem] = p
    return idx


def wiki_slug(url: str) -> str | None:
    m = re.search(r'/wiki/([^/?#]+)', url)
    if m:
        return m.group(1)
    # tolerate bare slugs in the batch file
    s = url.strip().strip('/')
    return s if re.fullmatch(r'[a-z0-9-]+', s) else None


def read_exact(path: Path) -> str:
    """Read without universal-newline translation: Path.read_text would fold
    CRLF to LF and a later write would silently rewrite every line ending in
    the file (much of the corpus is CRLF). Bytes in, bytes out."""
    return path.read_bytes().decode('utf-8')


def write_exact(path: Path, text: str) -> None:
    path.write_bytes(text.encode('utf-8'))


def apply_one(path: Path, date: str, reason: str) -> str:
    """Returns 'changed' | 'already' | 'no-fm'."""
    text = read_exact(path)
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return 'no-fm'
    fm = m.group(2)
    if re.search(r'^noindex\s*:', fm, re.MULTILINE):
        return 'already'
    nl = '\r\n' if '\r\n' in fm else '\n'
    add = f'noindex: true{nl}noindex_date: "{date}"{nl}noindex_reason: "{reason}"{nl}'
    new_text = m.group(1) + fm + add + m.group(3) + text[m.end():]
    write_exact(path, new_text)
    return 'changed'


def revert_one(path: Path) -> str:
    """Returns 'changed' | 'already' | 'no-fm'."""
    text = read_exact(path)
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return 'no-fm'
    fm = m.group(2)
    kept = [ln for ln in fm.splitlines(keepends=True) if not KEY_LINE_RE.match(ln)]
    new_fm = ''.join(kept)
    if new_fm == fm:
        return 'already'
    write_exact(path, m.group(1) + new_fm + m.group(3) + text[m.end():])
    return 'changed'


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--batch', required=True, help='file of wiki URLs, one per line')
    ap.add_argument('--revert', action='store_true', help='remove the three noindex keys instead')
    ap.add_argument('--dry-run', action='store_true', help='report what would change, write nothing')
    ap.add_argument('--date', default=dt.date.today().isoformat(),
                    help='value for noindex_date (default: today)')
    ap.add_argument('--reason', choices=['delisted', 'no-demand'],
                    help='value for noindex_reason (required unless --revert)')
    args = ap.parse_args()
    if not args.revert and not args.reason:
        ap.error('--reason is required when applying (omit only with --revert)')

    idx = basename_index()
    counts = {'changed': 0, 'already': 0, 'no-fm': 0, 'not-found': 0}
    for line in Path(args.batch).read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        slug = wiki_slug(line)
        path = idx.get(slug) if slug else None
        if path is None:
            counts['not-found'] += 1
            print(f'  NOT FOUND: {line}')
            continue
        if args.dry_run:
            # simulate on a copy of the text without writing
            text = read_exact(path)
            m = FRONT_MATTER_RE.match(text)
            if not m:
                result = 'no-fm'
            elif args.revert:
                result = 'changed' if re.search(r'^noindex\s*:', m.group(2), re.MULTILINE) else 'already'
            else:
                result = 'already' if re.search(r'^noindex\s*:', m.group(2), re.MULTILINE) else 'changed'
        else:
            result = revert_one(path) if args.revert else apply_one(path, args.date, args.reason)
        counts[result] += 1
        if result != 'already':
            verb = 'would ' if args.dry_run else ''
            action = 'revert' if args.revert else 'noindex'
            print(f'  {verb}{action}: {path.relative_to(ROOT).as_posix()}' +
                  ('' if result != 'no-fm' else '  [NO FRONT MATTER]'))

    mode = 'REVERT' if args.revert else f'APPLY (reason={args.reason}, date={args.date})'
    if args.dry_run:
        mode += ' [dry-run — nothing written]'
    print(f'{mode}: changed={counts["changed"]} already={counts["already"]} '
          f'no-front-matter={counts["no-fm"]} not-found={counts["not-found"]}')
    return 0 if counts['not-found'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

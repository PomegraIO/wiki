#!/usr/bin/env python3
"""Merge many 1,000-row-capped GSC UI "Pages" exports into one full CSV.

The Search Console web UI caps every CSV export at 1,000 rows. To get the
uncapped page list without API credentials, export the Pages table once per
URL slice (filter "Page -> URLs containing pomegra.io/wiki/a", then /b, ...
/z, /0 ... /9) and drop every downloaded Pages.csv into scripts/_gsc_ui/
(any filename; sub-folders are fine). This script:

- reads every *.csv under scripts/_gsc_ui/
- dedupes by URL, keeping the MAX clicks/impressions seen (never summing:
  prune_candidates.load_gsc already sums duplicate slugs, so a page that
  appears in two overlapping slices must be collapsed here first)
- warns loudly about any input file with exactly 1,000 data rows — that
  slice hit the UI cap and must be split further (/wiki/aa, /wiki/ab, ...)
- writes scripts/_gsc_pages_full.csv in the UI header format
  (Top pages,Clicks,Impressions,CTR,Position), which drops straight into
  scripts/prune_candidates.py --gsc-full

Run from project root:
    python scripts/merge_gsc_exports.py
    python scripts/merge_gsc_exports.py --in scripts/_gsc_ui --out scripts/_gsc_pages_full.csv
"""
from __future__ import annotations
import argparse
import csv
import io
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

SD = Path(__file__).resolve().parent
DEFAULT_IN = SD / '_gsc_ui'
DEFAULT_OUT = SD / '_gsc_pages_full.csv'
UI_EXPORT_CAP = 1000


def parse_num(s: str) -> float:
    return float((s or '').replace(',', '').replace('%', '').strip() or 0)


def sniff_columns(header: list[str]) -> dict[str, int]:
    """Same sniffing rule as prune_candidates.load_gsc."""
    cols: dict[str, int] = {}
    for i, name in enumerate(header):
        n = name.strip().lower()
        if 'page' in n or n == 'url':
            cols.setdefault('url', i)
        elif 'click' in n:
            cols.setdefault('clicks', i)
        elif 'impression' in n:
            cols.setdefault('impressions', i)
        elif 'ctr' in n:
            cols.setdefault('ctr', i)
        elif 'position' in n:
            cols.setdefault('position', i)
    return cols


def read_export(path: Path) -> tuple[dict[str, tuple[int, int, str, str]], int]:
    rows: dict[str, tuple[int, int, str, str]] = {}
    total = 0
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return rows, 0
        cols = sniff_columns(header)
        if {'url', 'clicks', 'impressions'} - cols.keys():
            print(f'  ! {path.name}: could not sniff url/clicks/impressions from header {header} — skipped',
                  file=sys.stderr)
            return rows, 0
        for raw in reader:
            if not raw or not raw[cols['url']].strip():
                continue
            total += 1
            url = raw[cols['url']].strip()
            clicks = int(parse_num(raw[cols['clicks']]))
            imps = int(parse_num(raw[cols['impressions']]))
            ctr = raw[cols['ctr']] if 'ctr' in cols and cols['ctr'] < len(raw) else ''
            pos = raw[cols['position']] if 'position' in cols and cols['position'] < len(raw) else ''
            prev = rows.get(url)
            if prev is None or (clicks, imps) > (prev[0], prev[1]):
                rows[url] = (clicks, imps, ctr, pos)
    return rows, total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--in', dest='in_dir', default=str(DEFAULT_IN), help='folder of GSC UI Pages exports')
    ap.add_argument('--out', default=str(DEFAULT_OUT), help='merged CSV path')
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    files = sorted(p for p in in_dir.rglob('*.csv') if p.is_file())
    if not files:
        print(f'No CSV files under {in_dir}. Drop the GSC "Pages" exports there first.', file=sys.stderr)
        return 1

    merged: dict[str, tuple[int, int, str, str]] = {}
    capped: list[str] = []
    for path in files:
        rows, total = read_export(path)
        flag = ''
        if total == UI_EXPORT_CAP:
            capped.append(str(path.relative_to(in_dir)))
            flag = '   <-- CAPPED: split this slice further'
        print(f'  {path.relative_to(in_dir)}: {total} rows, {len(rows)} unique{flag}')
        for url, rec in rows.items():
            prev = merged.get(url)
            if prev is None or (rec[0], rec[1]) > (prev[0], prev[1]):
                merged[url] = rec

    out = Path(args.out)
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Top pages', 'Clicks', 'Impressions', 'CTR', 'Position'])
        for url, (clicks, imps, ctr, pos) in sorted(merged.items(), key=lambda kv: (-kv[1][0], -kv[1][1], kv[0])):
            w.writerow([url, clicks, imps, ctr, pos])

    wiki_rows = sum(1 for u in merged if '/wiki/' in u)
    stock_rows = sum(1 for u in merged if '/wiki/' in u and u.rstrip('/').endswith('-stock'))
    print()
    print(f'Wrote {out} — {len(merged)} unique URLs from {len(files)} file(s)')
    print(f'  /wiki/ URLs: {wiki_rows}   of which *-stock: {stock_rows}')
    if len(merged) == UI_EXPORT_CAP:
        print('  ! merged total is exactly 1,000 — prune_candidates.py will treat this as a capped TEST input',
              file=sys.stderr)
    if capped:
        print()
        print(f'WARNING: {len(capped)} export(s) hit the 1,000-row UI cap and are missing pages:', file=sys.stderr)
        for c in capped:
            print(f'  - {c}', file=sys.stderr)
        print('Re-export those slices with a longer prefix (e.g. /wiki/aa, /wiki/ab, ...) and re-run.',
              file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())

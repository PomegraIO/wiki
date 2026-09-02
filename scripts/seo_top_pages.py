#!/usr/bin/env python3
"""Rank /wiki/ pages by meta-rewrite upside from a GSC Pages export.

Reads a Google Search Console "Pages" CSV (UI export or the API export from
scripts/gsc_fetch_pages.py — headers are sniffed), keeps /wiki/ URLs, maps
each URL to its content file by basename (permalinks flatten every path to
the file's basename), joins current title/description, and computes

    upside = impressions * max(0, expected_ctr(position) - actual_ctr)

using a standard position->CTR curve. The top 300 rows by upside are written
to scripts/_meta_rewrite_batch.json for a meta-rewrite wave.

Run from project root:
    python scripts/seo_top_pages.py --gsc ../../pomui/data/seo/gsc/Pages.csv

Note: GSC UI exports are capped at 1,000 rows; use gsc_fetch_pages.py for a
full export.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
SD = Path(__file__).resolve().parent
OUT_JSON = SD / '_meta_rewrite_batch.json'
TOP_N = 300

# Tolerates the UTF-8 BOM + CRLF line endings some company pages carry.
FRONT_MATTER_RE = re.compile(r'^(\ufeff?---\r?\n)(.*?)(\r?\n---\r?\n)', re.DOTALL)

# Standard organic position -> expected CTR curve (industry-average shape).
CTR_CURVE = {
    1: 0.28, 2: 0.15, 3: 0.11, 4: 0.08, 5: 0.07,
    6: 0.05, 7: 0.045, 8: 0.04, 9: 0.035, 10: 0.03,
    11: 0.020, 12: 0.018, 13: 0.017, 14: 0.016, 15: 0.015,
    16: 0.014, 17: 0.013, 18: 0.012, 19: 0.011, 20: 0.010,
}


def expected_ctr(position: float) -> float:
    p = int(round(position))
    if p < 1:
        p = 1
    if p > 20:
        return 0.005
    return CTR_CURVE[p]


def fm_value(fm: str, key: str) -> str:
    m = re.search(rf'^{key}\s*:[ \t]*(.*)$', fm, re.MULTILINE)
    if not m:
        return ''
    val = m.group(1).strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in ('"', "'"):
        val = val[1:-1]
    return val


def sniff_columns(header: list[str]) -> dict[str, int]:
    """Map logical fields to column indexes from a GSC export header."""
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
    missing = {'url', 'clicks', 'impressions', 'ctr', 'position'} - cols.keys()
    if missing:
        raise SystemExit(f'could not sniff columns {sorted(missing)} from header {header}')
    return cols


def parse_num(s: str) -> float:
    return float(s.replace(',', '').replace('%', '').strip() or 0)


def parse_ctr(s: str) -> float:
    """'17.39%' -> 0.1739; bare '0.1739' passes through."""
    s = s.strip()
    if s.endswith('%'):
        return parse_num(s) / 100.0
    return parse_num(s)


def wiki_slug(url: str) -> str | None:
    m = re.search(r'/wiki/([^/?#]+)', url)
    return m.group(1) if m else None


def basename_index() -> dict[str, Path]:
    idx: dict[str, Path] = {}
    for p in CONTENT.rglob('*.md'):
        if p.name == '_index.md':
            continue
        idx[p.stem] = p
    return idx


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--gsc', required=True, help='path to GSC Pages CSV export')
    args = ap.parse_args()

    idx = basename_index()
    rows = []
    unmapped = []
    with open(args.gsc, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        cols = sniff_columns(header)
        for raw in reader:
            if not raw or not raw[cols['url']].strip():
                continue
            url = raw[cols['url']].strip()
            slug = wiki_slug(url)
            if not slug:
                continue  # not a /wiki/ URL
            path = idx.get(slug)
            if path is None:
                unmapped.append(url)
                continue
            impressions = int(parse_num(raw[cols['impressions']]))
            position = parse_num(raw[cols['position']])
            ctr = parse_ctr(raw[cols['ctr']])
            text = path.read_text(encoding='utf-8', errors='replace')
            m = FRONT_MATTER_RE.match(text)
            fm = m.group(2) if m else ''
            title = fm_value(fm, 'title')
            desc = fm_value(fm, 'description')
            upside = impressions * max(0.0, expected_ctr(position) - ctr)
            rows.append({
                'slug': slug,
                'path': path.relative_to(ROOT).as_posix(),
                'url': url,
                'impressions': impressions,
                'position': round(position, 2),
                'ctr': round(ctr, 4),
                'upside': round(upside, 1),
                'title': title,
                'title_len': len(title),
                'description': desc,
                'desc_len': len(desc),
            })

    rows.sort(key=lambda r: -r['upside'])
    top = rows[:TOP_N]
    OUT_JSON.write_text(json.dumps(top, indent=1, ensure_ascii=False), encoding='utf-8')

    print(f'wiki rows in export: {len(rows) + len(unmapped)}  mapped: {len(rows)}  unmapped: {len(unmapped)}')
    print(f'wrote top {len(top)} by upside -> {OUT_JSON.relative_to(ROOT).as_posix()}')
    if unmapped:
        print('unmapped URLs (no content file with that basename):')
        for u in unmapped[:20]:
            print(f'  {u}')
        if len(unmapped) > 20:
            print(f'  ... and {len(unmapped) - 20} more')
    print('top 10 by upside:')
    for r in top[:10]:
        print(f"  {r['upside']:>8.1f}  pos {r['position']:>5}  imp {r['impressions']:>7}  "
              f"ctr {r['ctr']:.2%}  /{r['slug']}/  (title {r['title_len']}c, desc {r['desc_len']}c)")
    return 0


if __name__ == '__main__':
    sys.exit(main())

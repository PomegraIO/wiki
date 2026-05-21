#!/usr/bin/env python3
"""Move the 30 root-level core articles into matching category subdirectories
so they pick up the same SVG hero, sister-entries, and backlink widgets as
the swarm-written articles.

URLs are unaffected — Hugo's `[permalinks.page]` is `/:contentbasename/`
so /stock.md and /equity/stock.md both serve at /stock/.

After moving, also rewrites each article's `image:` front-matter value
(which currently still points at /svg/default.svg) to match the new
category SVG.
"""
from __future__ import annotations
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

MAPPING = {
    'alpha':                    'ratios',
    'asset-allocation':         'strategies',
    'bear-market':              'markets',
    'beta':                     'ratios',
    'bond':                     'fixed-income',
    'broker':                   'institutions',
    'bull-market':              'markets',
    'central-bank':             'monetary',
    'compound-interest':        'personal-finance',
    'diversification':          'strategies',
    'dividend':                 'equity',
    'earnings-per-share':       'ratios',
    'etf':                      'funds',
    'federal-reserve':          'monetary',
    'hedge-fund':               'funds',
    'index-fund':               'funds',
    'inflation':                'macro',
    'initial-public-offering':  'corporate',
    'interest-rate':            'monetary',
    'market-capitalization':    'ratios',
    'mutual-fund':              'funds',
    'option':                   'derivatives',
    'price-to-earnings-ratio':  'ratios',
    'public-company':           'corporate',
    'recession':                'macro',
    'short-selling':            'trading',
    'stock':                    'equity',
    'stock-exchange':           'institutions',
    'stock-market':             'markets',
    'yield-curve':              'fixed-income',
}


def main() -> None:
    img_re = re.compile(r'(image:\s*["\']?)(/svg/[a-z-]+\.svg)(["\']?)')
    moved = 0
    for slug, cat in MAPPING.items():
        src = CONTENT / f'{slug}.md'
        if not src.exists():
            print(f'skip (missing): {slug}')
            continue
        dst_dir = CONTENT / cat
        dst_dir.mkdir(exist_ok=True)
        dst = dst_dir / f'{slug}.md'
        if dst.exists():
            print(f'skip (exists at target): {slug}')
            continue

        text = src.read_text(encoding='utf-8')
        new_text, n = img_re.subn(rf'\1/svg/{cat}.svg\3', text, count=1)
        if n:
            text = new_text

        dst.write_text(text, encoding='utf-8')
        src.unlink()
        moved += 1
        print(f'  {slug}.md -> {cat}/')

    print(f'Done. {moved} articles moved.')


if __name__ == '__main__':
    main()

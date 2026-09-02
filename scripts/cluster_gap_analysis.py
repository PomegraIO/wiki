#!/usr/bin/env python3
"""Find comparison-page and behavioral-finance content gaps with query evidence.

Inventories existing coverage (every *-vs-*.md slug+title, every
content/behavioral/ slug+title), then mines two demand sources:
- the GSC Queries export (pomui/data/seo/gsc/Queries.csv, 1,000-row UI cap)
- the "gap—wiki/learn candidate" table in pomui/data/seo/opportunities.md

and reports:
  (a) comparison-intent queries ("x vs y", "difference between x and y")
      with impressions/volume but no matching existing slug
  (b) behavioral-finance queries/terms not covered by existing behavioral/
      slugs
  (c) the top existing behavioral pages by GSC performance — the models an
      eventual behavioral wave should emulate

Every proposed topic is deduped against ALL existing content basenames and
the verdict is stated per entry ("no existing slug match" vs the covering
slug). Output: scripts/_cluster_gaps.md + headline counts on stdout.

Run from project root:
    python scripts/cluster_gap_analysis.py
    python scripts/cluster_gap_analysis.py --queries <csv> --opportunities <md> --pages <csv>
"""
from __future__ import annotations
import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
SD = Path(__file__).resolve().parent
OUT_MD = SD / '_cluster_gaps.md'

SEO_DIR = ROOT.parent.parent / 'pomui' / 'data' / 'seo'
DEFAULT_QUERIES = SEO_DIR / 'gsc' / 'Queries.csv'
DEFAULT_PAGES = SEO_DIR / 'gsc' / 'Pages.csv'
DEFAULT_OPPS = SEO_DIR / 'opportunities.md'

# Tolerates the UTF-8 BOM + CRLF line endings some company pages carry.
FRONT_MATTER_RE = re.compile(r'^(\ufeff?---\r?\n)(.*?)(\r?\n---\r?\n)', re.DOTALL)

VS_RE = re.compile(r'^(.*?)\s+vs\.?\s+(.*)$', re.IGNORECASE)
DIFF_RE = re.compile(r'difference\s+between\s+(.*?)\s+and\s+(.*)$', re.IGNORECASE)

# Terms that mark a query as behavioral-finance intent.
BEHAVIORAL_TERMS = [
    'bias', 'fallacy', 'aversion', 'behavioral finance', 'behavioural finance',
    'investor psychology', 'market psychology', 'herd', 'herding', 'fomo',
    'loss aversion', 'anchoring', 'overconfidence', 'sunk cost', 'disposition effect',
    'house money', 'mental accounting', 'prospect theory', 'endowment effect',
    'recency', 'hindsight', 'confirmation bias', 'framing effect', 'status quo bias',
    'regret', 'gambler', 'hot hand', 'availability heuristic', 'affect heuristic',
    'panic selling', 'revenge trading', 'overtrading',
]

# Common finance-brand abbreviations so "financial times vs wall street journal"
# matches an existing slug like ft-vs-wsj (and vice versa).
ALIASES = {
    'wall-street-journal': 'wsj', 'the-wall-street-journal': 'wsj',
    'financial-times': 'ft', 'the-financial-times': 'ft',
    's-p-500': 'sp-500', 'sp500': 'sp-500', 's-and-p-500': 'sp-500',
    'exchange-traded-fund': 'etf', 'exchange-traded-funds': 'etf',
    'mutual-funds': 'mutual-fund', 'stocks': 'stock', 'bonds': 'bond',
    'cryptocurrency': 'crypto', 'bitcoin': 'btc',
}


def slugify(s: str) -> str:
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s


def norm_term(s: str) -> str:
    slug = slugify(s)
    return ALIASES.get(slug, slug)


REV_ALIASES: dict[str, set[str]] = {}
for long, short in ALIASES.items():
    REV_ALIASES.setdefault(short, set()).add(long)


def term_variants(term: str) -> set[str]:
    return {term} | REV_ALIASES.get(term, set())


def has_token_seq(name: str, term: str) -> bool:
    """True when `term` appears in `name` on hyphen-token boundaries, so the
    term 'flow' does not match the company slug 'flow-stock' via substring."""
    return any(f'-{v}-' in f'-{name}-' for v in term_variants(term))


def load_titles(paths) -> dict[str, str]:
    out = {}
    for p in paths:
        text = p.read_text(encoding='utf-8', errors='replace')
        m = FRONT_MATTER_RE.match(text)
        title = ''
        if m:
            tm = re.search(r'^title\s*:\s*(.*)$', m.group(2), re.MULTILINE)
            if tm:
                title = tm.group(1).strip().strip('"\'')
        out[p.stem] = title
    return out


def parse_gsc_csv(path: Path, key_hint: str) -> list[dict]:
    rows = []
    with path.open(newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        cols: dict[str, int] = {}
        for i, name in enumerate(header):
            n = name.strip().lower()
            if key_hint in n:
                cols.setdefault('key', i)
            elif 'click' in n:
                cols.setdefault('clicks', i)
            elif 'impression' in n:
                cols.setdefault('impressions', i)
            elif 'position' in n:
                cols.setdefault('position', i)
        for raw in reader:
            if not raw or not raw[cols['key']].strip():
                continue
            rows.append({
                'key': raw[cols['key']].strip(),
                'clicks': int(float(raw[cols['clicks']].replace(',', '') or 0)),
                'impressions': int(float(raw[cols['impressions']].replace(',', '') or 0)),
                'position': float(raw[cols['position']].replace(',', '') or 0),
            })
    return rows


def parse_opportunities_gaps(path: Path) -> list[dict]:
    """Rows of the '## gap—wiki/learn candidate' table: keyword + volume."""
    rows = []
    in_section = False
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):
            in_section = 'gap' in line.lower() and 'wiki' in line.lower()
            continue
        if not in_section or not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 2 or cells[0].lower() == 'keyword' or set(cells[0]) <= {'-', ':', ' '}:
            continue
        vol = re.sub(r'[^0-9]', '', cells[1])
        rows.append({'keyword': cells[0], 'volume': int(vol) if vol else 0})
    return rows


def comparison_terms(q: str) -> tuple[str, str] | None:
    m = DIFF_RE.search(q) or VS_RE.match(q)
    if not m:
        return None
    a, b = norm_term(m.group(1)), norm_term(m.group(2))
    return (a, b) if a and b else None


def covering_slug(terms: tuple[str, str], basenames: set[str],
                  require_vs: bool = True) -> str | None:
    """An existing basename that contains both compared terms on token
    boundaries. With require_vs, the covering page must itself read as a
    comparison (a vs/versus/difference token) so 'stock vs flow' is not
    'covered' by the company page flow-stock.md."""
    a, b = terms
    for name in basenames:
        if not (has_token_seq(name, a) and has_token_seq(name, b)):
            continue
        tokens = set(name.split('-'))
        if not require_vs or tokens & {'vs', 'versus', 'difference', 'differences'}:
            return name
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--queries', default=str(DEFAULT_QUERIES))
    ap.add_argument('--pages', default=str(DEFAULT_PAGES))
    ap.add_argument('--opportunities', default=str(DEFAULT_OPPS))
    args = ap.parse_args()

    all_pages = [p for p in CONTENT.rglob('*.md') if p.name != '_index.md']
    all_basenames = {p.stem for p in all_pages}
    vs_pages = load_titles(p for p in all_pages if '-vs-' in p.stem)
    behavioral_pages = load_titles(p for p in all_pages
                                   if 'behavioral' in p.relative_to(CONTENT).parts[:1])

    queries = parse_gsc_csv(Path(args.queries), 'quer')
    gaps = parse_opportunities_gaps(Path(args.opportunities))

    # Non-wiki pomegra.io pages that already rank (from the Pages export):
    # a "gap" the /learn/ newswires chapter already serves is a cannibalisation
    # risk, not a green field — annotate rather than hide.
    external_pages: dict[str, str] = {}
    for row in parse_gsc_csv(Path(args.pages), 'page'):
        if '/wiki/' in row['key']:
            continue
        base = row['key'].rstrip('/').rsplit('/', 1)[-1]
        if re.fullmatch(r'[a-z0-9-]+', base):
            external_pages.setdefault(base, row['key'])

    # ---- (a) comparison-intent gaps -------------------------------------
    comp_rows = []
    seen: set[str] = set()
    for src, items in (('gsc', queries), ('opps', gaps)):
        for it in items:
            q = it['key'] if src == 'gsc' else it['keyword']
            terms = comparison_terms(q)
            if not terms:
                continue
            slug = slugify(q)
            if slug in seen:
                continue
            seen.add(slug)
            cover = covering_slug(terms, all_basenames)
            if cover is None and slug in all_basenames:
                cover = slug
            ext = None
            if cover is None:
                ext_base = covering_slug(terms, set(external_pages), require_vs=False)
                if ext_base:
                    ext = external_pages[ext_base]
            comp_rows.append({
                'query': q,
                'external': ext,
                'evidence': (f"{it['impressions']} impressions, {it['clicks']} clicks, "
                             f"pos {it['position']:.1f} (GSC)") if src == 'gsc'
                            else f"volume {it['volume']:,} (opportunities.md)",
                'weight': it['impressions'] if src == 'gsc' else it['volume'] / 100,
                'covered': cover,
            })
    comp_rows.sort(key=lambda r: -r['weight'])
    comp_gaps = [r for r in comp_rows if not r['covered']]

    # ---- (b) behavioral gaps --------------------------------------------
    behav_rows = []
    behav_basenames = set(behavioral_pages)
    seen.clear()
    for src, items in (('gsc', queries), ('opps', gaps)):
        for it in items:
            q = (it['key'] if src == 'gsc' else it['keyword']).lower()
            if not any(t in q for t in BEHAVIORAL_TERMS):
                continue
            slug = slugify(q)
            if slug in seen:
                continue
            seen.add(slug)
            tokens = [t for t in slug.split('-') if len(t) > 2]
            cover = next((n for n in behav_basenames
                          if sum(t in n for t in tokens) >= max(1, len(tokens) - 1)), None)
            exact = slug if slug in all_basenames else None
            behav_rows.append({
                'query': it['key'] if src == 'gsc' else it['keyword'],
                'evidence': (f"{it['impressions']} impressions, {it['clicks']} clicks (GSC)")
                            if src == 'gsc' else f"volume {it['volume']:,} (opportunities.md)",
                'weight': it['impressions'] if src == 'gsc' else it['volume'] / 100,
                'covered': exact or cover,
            })
    behav_rows.sort(key=lambda r: -r['weight'])
    behav_gaps = [r for r in behav_rows if not r['covered']]

    # ---- (c) top existing behavioral pages ------------------------------
    top_behav = []
    for row in parse_gsc_csv(Path(args.pages), 'page'):
        m = re.search(r'/wiki/([^/?#]+)', row['key'])
        if m and m.group(1) in behav_basenames:
            top_behav.append({'slug': m.group(1), **row})
    top_behav.sort(key=lambda r: (-r['clicks'], -r['impressions']))

    # ---- write report ----------------------------------------------------
    L = ['# Cluster gap analysis', '',
         f'Existing coverage: {len(vs_pages)} `*-vs-*` comparison pages, '
         f'{len(behavioral_pages)} behavioral/ pages, {len(all_basenames)} content basenames total.',
         f'Demand sources: {len(queries)} GSC queries (UI export, 1,000-row cap), '
         f'{len(gaps)} gap—wiki rows from opportunities.md.', '',
         f'## (a) Comparison-intent gaps — {len(comp_gaps)} of {len(comp_rows)} comparison queries uncovered', '']
    for r in comp_gaps[:40]:
        note = (f"; NOTE already ranking via {r['external']} — cannibalisation risk"
                if r.get('external') else '')
        L.append(f"- **{r['query']}** — {r['evidence']} — dedup: no existing slug match "
                 f"(proposed `{slugify(r['query'])}`){note}")
    L += ['', '### covered (for reference)', '']
    for r in comp_rows[:60]:
        if r['covered']:
            L.append(f"- {r['query']} — {r['evidence']} — covered by `/{r['covered']}/`")
    L += ['', f'## (b) Behavioral-finance gaps — {len(behav_gaps)} of {len(behav_rows)} behavioral queries uncovered', '']
    if not behav_rows:
        L += ['No behavioral-finance queries survive the demand sources: the capped '
              'GSC UI export cuts off around 14 impressions and the opportunities.md '
              'gap table is a truncated sample. Re-run against a full Search Analytics '
              'API queries export before concluding there is no behavioral demand — '
              'section (c) shows behavioral pages do earn clicks.', '']
    for r in behav_gaps[:40]:
        L.append(f"- **{r['query']}** — {r['evidence']} — dedup: no existing slug match "
                 f"(proposed `{slugify(r['query'])}`)")
    L += ['', '### covered (for reference)', '']
    for r in behav_rows[:60]:
        if r['covered']:
            L.append(f"- {r['query']} — {r['evidence']} — covered by `/{r['covered']}/`")
    L += ['', '## (c) Top existing behavioral pages (models for the wave)', '',
          '| Page | Clicks | Impressions | Position |', '|---|---:|---:|---:|']
    for r in top_behav[:15]:
        title = behavioral_pages.get(r['slug'], '')
        L.append(f"| `/{r['slug']}/` — {title} | {r['clicks']} | {r['impressions']} | {r['position']:.1f} |")
    L.append('')
    OUT_MD.write_text('\n'.join(L), encoding='utf-8')

    print(f'coverage: {len(vs_pages)} vs-pages, {len(behavioral_pages)} behavioral pages, '
          f'{len(all_basenames)} total basenames')
    print(f'demand: {len(queries)} GSC queries, {len(gaps)} opportunities gap—wiki rows')
    print(f'(a) comparison queries found: {len(comp_rows)}  uncovered: {len(comp_gaps)}')
    print(f'(b) behavioral queries found: {len(behav_rows)}  uncovered: {len(behav_gaps)}')
    print(f'(c) behavioral pages with GSC data: {len(top_behav)}')
    print(f'report -> {OUT_MD.relative_to(ROOT).as_posix()}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

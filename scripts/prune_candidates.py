#!/usr/bin/env python3
"""Rank company pages (content/companies/**/*-stock.md ONLY) for noindex pruning.

A company page survives if it shows any demand signal:
- its URL appears in the GSC pages export with clicks >= 1 or impressions >= 10
- its URL is an owned page in pomui/data/seo/keyword-page-map.json

Everything else is a prune candidate, ranked:
- tier 1: ticker fails validation against the live stocks API (delisted/bogus)
          -- only populated when --validate is given
- tier 2: ticker valid (or not validated) but zero GSC signal

Outputs (underscore-prefixed scratch, not committed):
- scripts/_noindex_batch1.txt  every prune candidate (or --batch-size N), tier-1 first, one per line
  (feed to scripts/apply_noindex.py; '#' comment lines are ignored there)
- scripts/_prune_report.md     summary counts
- scripts/_validate_cache.json per-symbol API responses (resumable cache)

Run from project root:
    python scripts/prune_candidates.py --gsc-full scripts/_gsc_pages_full.csv
    python scripts/prune_candidates.py --gsc-full ... --validate --max-validate 200
    python scripts/prune_candidates.py --gsc-full ... --validate --test-symbols AAPL,ZZZZ

CAUTION: a GSC *UI* export is capped at 1,000 rows and misses most pages'
signal — the script detects that and labels all output TEST. Use the full
API export from scripts/gsc_fetch_pages.py for a real pruning decision.

Note: https://pomegra.io/api/stocks/validate currently sits behind the
gateway's Keycloak OIDC redirect for anonymous callers. The script detects
the 302/401 ('auth-required'), stops validating, and never mis-files those
tickers as invalid. Pass --bearer-token (or set POMEGRA_BEARER) once an
API token is available.
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
COMPANIES = CONTENT / 'companies'
SD = Path(__file__).resolve().parent
BATCH_OUT = SD / '_noindex_batch1.txt'
REPORT_OUT = SD / '_prune_report.md'
CACHE_PATH = SD / '_validate_cache.json'

DEFAULT_KW_MAP = ROOT.parent.parent / 'pomui' / 'data' / 'seo' / 'keyword-page-map.json'
VALIDATE_URL = 'https://pomegra.io/api/stocks/validate?symbol={}'
THROTTLE_S = 0.5
UI_EXPORT_CAP = 1000

GSC_CLICKS_KEEP = 1      # keep the page if clicks >= this ...
GSC_IMPRESSIONS_KEEP = 10  # ... or impressions >= this


def slug_to_ticker(slug: str) -> str:
    """aapl-stock -> AAPL; brk-b-stock -> BRK.B (class-share hyphen -> dot)."""
    base = slug[:-len('-stock')] if slug.endswith('-stock') else slug
    return base.upper().replace('-', '.')


def wiki_slug(url: str) -> str | None:
    m = re.search(r'/wiki/([^/?#]+)', url)
    return m.group(1) if m else None


def parse_num(s: str) -> float:
    return float(s.replace(',', '').replace('%', '').strip() or 0)


def load_gsc(path: str) -> tuple[dict[str, tuple[int, int]], int]:
    """Return ({wiki slug: (clicks, impressions)}, total data rows)."""
    signal: dict[str, tuple[int, int]] = {}
    total = 0
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        cols: dict[str, int] = {}
        for i, name in enumerate(header):
            n = name.strip().lower()
            if 'page' in n or n == 'url':
                cols.setdefault('url', i)
            elif 'click' in n:
                cols.setdefault('clicks', i)
            elif 'impression' in n:
                cols.setdefault('impressions', i)
        if {'url', 'clicks', 'impressions'} - cols.keys():
            raise SystemExit(f'could not sniff url/clicks/impressions from header {header}')
        for raw in reader:
            if not raw or not raw[cols['url']].strip():
                continue
            total += 1
            slug = wiki_slug(raw[cols['url']])
            if not slug:
                continue
            c = int(parse_num(raw[cols['clicks']]))
            imp = int(parse_num(raw[cols['impressions']]))
            pc, pi = signal.get(slug, (0, 0))
            signal[slug] = (pc + c, pi + imp)
    return signal, total


def load_kw_map_slugs(path: Path) -> set[str]:
    if not path.exists():
        print(f'warning: keyword map not found at {path}; skipping that exclusion', file=sys.stderr)
        return set()
    data = json.loads(path.read_text(encoding='utf-8'))
    slugs = set()
    for url in data.values():
        s = wiki_slug(str(url))
        if s:
            slugs.add(s)
    return slugs


class Validator:
    """Throttled, cached, resumable ticker validation against the live API."""

    def __init__(self, bearer: str | None):
        self.bearer = bearer
        self.cache: dict[str, dict] = {}
        if CACHE_PATH.exists():
            self.cache = json.loads(CACHE_PATH.read_text(encoding='utf-8'))
        self.auth_blocked = False
        self.calls = 0

    def save(self) -> None:
        CACHE_PATH.write_text(json.dumps(self.cache, indent=1, sort_keys=True), encoding='utf-8')

    def check(self, symbol: str) -> dict:
        """Return cache entry {status, isValid, ...}; hits the network at most once per symbol."""
        hit = self.cache.get(symbol)
        if hit and hit.get('status') == 'ok':
            return hit
        if self.auth_blocked:
            return {'status': 'auth-required', 'isValid': None}
        if self.calls:
            time.sleep(THROTTLE_S)
        self.calls += 1
        url = VALIDATE_URL.format(urllib.parse.quote(symbol))
        req = urllib.request.Request(url, headers={'Accept': 'application/json',
                                                   'User-Agent': 'pomegra-wiki-prune/1.0'})
        if self.bearer:
            req.add_header('Authorization', f'Bearer {self.bearer}')
        entry: dict
        try:
            # The gateway 302s anonymous callers to Keycloak; don't follow it.
            class NoRedirect(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, *a, **kw):
                    return None
            opener = urllib.request.build_opener(NoRedirect)
            with opener.open(req, timeout=20) as resp:
                body = json.loads(resp.read().decode('utf-8'))
                entry = {'status': 'ok',
                         'isValid': bool(body.get('isValid')),
                         'validatedSymbol': body.get('validatedSymbol'),
                         'companyName': body.get('companyName'),
                         'errorMessage': body.get('errorMessage')}
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308, 401, 403):
                entry = {'status': 'auth-required', 'isValid': None, 'http': e.code}
                self.auth_blocked = True
            else:
                entry = {'status': 'error', 'isValid': None, 'http': e.code}
        except Exception as e:  # network trouble, bad JSON, timeout
            entry = {'status': 'error', 'isValid': None, 'error': str(e)[:200]}
        self.cache[symbol] = entry
        self.save()
        return entry


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--gsc-full', required=True,
                    help='full GSC pages CSV (from scripts/gsc_fetch_pages.py)')
    ap.add_argument('--keyword-map', default=str(DEFAULT_KW_MAP),
                    help=f'keyword->URL map (default: {DEFAULT_KW_MAP})')
    ap.add_argument('--validate', action='store_true',
                    help='hit the live stocks API to split tier 1 (invalid ticker) from tier 2')
    ap.add_argument('--max-validate', type=int, default=0,
                    help='cap network validations this run (0 = no cap); cache makes reruns resume')
    ap.add_argument('--bearer-token', default=os.environ.get('POMEGRA_BEARER') or None,
                    help='bearer token for the API gateway (or set POMEGRA_BEARER)')
    ap.add_argument('--batch-size', type=int, default=0,
                    help='cap the batch file at N URLs; 0 (default) writes every candidate')
    ap.add_argument('--test-symbols',
                    help='comma-separated symbols: just validate these, print results, and exit')
    args = ap.parse_args()

    if args.test_symbols:
        v = Validator(args.bearer_token)
        for sym in [s.strip() for s in args.test_symbols.split(',') if s.strip()]:
            print(f'  {sym:<8} -> {json.dumps(v.check(sym))}')
        print(f'{v.calls} network call(s); cache now {len(v.cache)} entries at {CACHE_PATH.name}')
        return 0

    signal, gsc_rows = load_gsc(args.gsc_full)
    capped = gsc_rows == UI_EXPORT_CAP
    kw_slugs = load_kw_map_slugs(Path(args.keyword_map))

    universe = sorted(COMPANIES.rglob('*-stock.md'))
    excluded_gsc, excluded_kw, candidates = 0, 0, []
    for p in universe:
        slug = p.stem
        c, imp = signal.get(slug, (0, 0))
        if c >= GSC_CLICKS_KEEP or imp >= GSC_IMPRESSIONS_KEEP:
            excluded_gsc += 1
            continue
        if slug in kw_slugs:
            excluded_kw += 1
            continue
        candidates.append(slug)

    tier1, tier2 = [], []
    validated = invalid = 0
    auth_note = ''
    if args.validate:
        v = Validator(args.bearer_token)
        for slug in candidates:
            if args.max_validate and v.calls >= args.max_validate:
                break
            entry = v.check(slug_to_ticker(slug))
            if entry['status'] == 'ok':
                validated += 1
                if entry['isValid'] is False:
                    invalid += 1
                    tier1.append(slug)
                    continue
            tier2.append(slug)
            if v.auth_blocked:
                auth_note = ('validation ABORTED: the API gateway requires auth '
                             '(302/401 to Keycloak); remaining candidates left in tier 2')
                break
        done = set(tier1) | set(tier2)
        tier2.extend(s for s in candidates if s not in done)
    else:
        tier2 = candidates

    batch = [f'https://pomegra.io/wiki/{s}/' for s in tier1 + tier2]
    if args.batch_size > 0:
        batch = batch[:args.batch_size]

    test_banner = ('# TEST OUTPUT — input GSC csv is a 1,000-row-capped UI export; most pages\n'
                   '# are missing their demand signal. Do NOT use for real pruning.\n') if capped else ''
    BATCH_OUT.write_text(test_banner + '\n'.join(batch) + '\n', encoding='utf-8')

    lines = [
        '# Prune candidates report' + (' — TEST RUN (capped UI export input)' if capped else ''),
        '',
        f'- GSC input: `{args.gsc_full}` ({gsc_rows} rows'
        + (', exactly at the 1,000-row UI cap — NOT a full export)' if capped else ')'),
        f'- company-page universe: {len(universe)}',
        f'- excluded — GSC signal (clicks>={GSC_CLICKS_KEEP} or impressions>={GSC_IMPRESSIONS_KEEP}): {excluded_gsc}',
        f'- excluded — owned in keyword-page-map.json: {excluded_kw}',
        f'- prune candidates: {len(candidates)}',
        f'- tier 1 (ticker fails validation): {len(tier1)}'
        + ('' if args.validate else '  (not populated — run with --validate)'),
        f'- tier 2 (valid/unvalidated, zero GSC signal): {len(tier2)}',
        f'- batch written: {len(batch)} URLs -> `{BATCH_OUT.name}` (tier 1 first)',
    ]
    if args.validate:
        lines.append(f'- validated (network + cache): {validated} ok, {invalid} invalid '
                     f'(cache: `{CACHE_PATH.name}`)')
    if auth_note:
        lines.append(f'- WARNING: {auth_note}')
    REPORT_OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print(f'\nreport -> {REPORT_OUT.relative_to(ROOT).as_posix()}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

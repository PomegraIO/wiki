#!/usr/bin/env python3
"""Fetch a FULL page-dimension Search Analytics export from the GSC API.

The Search Console web UI caps CSV exports at 1,000 rows; the API returns up
to 25,000 rows per request and supports paging via startRow, so this script
retrieves *every* page (default: URLs under /wiki/) for a 3-month window and
writes a CSV whose header matches the UI export format, so it drops straight
into scripts/seo_top_pages.py and scripts/prune_candidates.py.

One-time credential setup
-------------------------
1. Go to https://console.cloud.google.com/ and create (or pick) a project.
2. APIs & Services -> Library -> enable "Google Search Console API".
3. APIs & Services -> Credentials -> Create credentials -> OAuth client ID
   -> Application type: "Desktop app". Download the client secrets JSON.
   (If prompted, configure the OAuth consent screen first; External +
   test-user = the Google account that owns the pomegra.io GSC property.)
4. Save the JSON anywhere outside the repo, e.g. ~/gsc_client_secret.json.

First run opens a browser for consent and caches the refresh token at
scripts/_gsc_token.json (underscore-prefixed scratch file — do not commit).
Subsequent runs reuse the token silently; --credentials is then optional.

Dependencies (the only scripts/ tooling that needs pip packages):
    pip install google-api-python-client google-auth-oauthlib

Usage (from project root):
    python scripts/gsc_fetch_pages.py --credentials ~/gsc_client_secret.json
    python scripts/gsc_fetch_pages.py --prefix / --out scripts/_gsc_all_pages.csv
    python scripts/gsc_fetch_pages.py --site https://pomegra.io/ --days 28
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

SD = Path(__file__).resolve().parent
ROOT = SD.parent
TOKEN_PATH = SD / '_gsc_token.json'
DEFAULT_OUT = SD / '_gsc_pages_full.csv'

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
API_ROW_LIMIT = 25000  # per-request maximum; we page past it with startRow

try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print('Missing Google API libraries. This is the one script in scripts/ that\n'
          'needs pip packages. Install them with:\n\n'
          '    pip install google-api-python-client google-auth-oauthlib\n',
          file=sys.stderr)
    sys.exit(1)


def get_credentials(client_secrets: str | None) -> Credentials:
    creds: Credentials | None = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN_PATH.write_text(creds.to_json(), encoding='utf-8')
    if not creds or not creds.valid:
        if not client_secrets:
            raise SystemExit(
                f'No cached token at {TOKEN_PATH} and no --credentials given.\n'
                'Pass --credentials <path-to-oauth-desktop-client-secrets.json> '
                '(see module docstring for the one-time setup).')
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets, SCOPES)
        creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json(), encoding='utf-8')
        print(f'token cached at {TOKEN_PATH}')
    return creds


def fetch_all(service, site: str, start: str, end: str, prefix: str) -> list[dict]:
    """Page through the Search Analytics API until it runs dry."""
    rows: list[dict] = []
    start_row = 0
    while True:
        body = {
            'startDate': start,
            'endDate': end,
            'dimensions': ['page'],
            'rowLimit': API_ROW_LIMIT,
            'startRow': start_row,
            'dimensionFilterGroups': [{
                'filters': [{
                    'dimension': 'page',
                    'operator': 'contains',
                    'expression': prefix,
                }],
            }],
        }
        resp = service.searchanalytics().query(siteUrl=site, body=body).execute()
        batch = resp.get('rows', [])
        rows.extend(batch)
        print(f'  fetched {len(batch)} rows (total {len(rows)})')
        if len(batch) < API_ROW_LIMIT:
            return rows
        start_row += API_ROW_LIMIT


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--credentials', help='path to OAuth desktop-client secrets JSON '
                                          '(only needed until the token is cached)')
    ap.add_argument('--site', default='sc-domain:pomegra.io',
                    help='GSC property (default: sc-domain:pomegra.io; use '
                         'https://pomegra.io/ if yours is a URL-prefix property)')
    ap.add_argument('--prefix', default='/wiki/',
                    help='page-URL substring filter (default: /wiki/; use / for everything)')
    ap.add_argument('--days', type=int, default=90, help='window length in days (default: 90)')
    ap.add_argument('--out', default=str(DEFAULT_OUT), help=f'output CSV (default: {DEFAULT_OUT})')
    args = ap.parse_args()

    # GSC data lags ~2 days; end the window there so the last days are not zeros.
    end = dt.date.today() - dt.timedelta(days=2)
    start = end - dt.timedelta(days=args.days)

    creds = get_credentials(args.credentials)
    service = build('searchconsole', 'v1', credentials=creds)

    print(f'querying {args.site}  pages containing "{args.prefix}"  {start} .. {end}')
    rows = fetch_all(service, args.site, start.isoformat(), end.isoformat(), args.prefix)

    out = Path(args.out)
    with out.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        # Same header shape as the GSC UI "Pages" export, so downstream
        # scripts (seo_top_pages.py, prune_candidates.py) sniff it identically.
        w.writerow(['Top pages', 'Clicks', 'Impressions', 'CTR', 'Position'])
        for r in sorted(rows, key=lambda r: -r.get('clicks', 0)):
            w.writerow([
                r['keys'][0],
                int(r.get('clicks', 0)),
                int(r.get('impressions', 0)),
                f"{100 * r.get('ctr', 0):.2f}%",
                f"{r.get('position', 0):.2f}",
            ])
    print(f'wrote {len(rows)} rows -> {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Build a clean companies-first ticker source for the next ~3,000 -stock pages.

The prominent 11k tickers are on disk; the tail of the US universe is mostly
ETPs plus non-company securities (preferred series, warrants, SPAC units, baby
bonds). The SEC expanded source titles ETPs by their *issuer bank*, which is
useless for a writer. So we:

  * enrich each ticker's name from the NASDAQ/NYSE listing files (descriptive
    "Security Name" + reliable ETF flag),
  * EXCLUDE non-profile-able securities (preferreds, warrants, units, rights,
    notes/debentures, hyphenated derivative tickers),
  * classify the rest as ETP (profile as a fund) vs operating company,
  * order companies first (so every real company is in and gets the deeper
    tiers), then ETPs, capped at TARGET.

Writes scripts/_sec_tickers_w3k.json in the shape build_company_batches expects.
"""
from __future__ import annotations
import glob, json, os, re

SRC = "scripts/_sec_tickers_expanded.json"
OUT = "scripts/_sec_tickers_w3k.json"
TARGET = 3000

# Securities that are NOT a company and NOT a fund — drop entirely.
JUNK_RX = re.compile(
    r"\bPreferred\b|\bPfd\b|\bWarrant|\bRights?\b|\bUnits?\b|\bDepositary\b|"
    r"%\s|\bNotes?\b|\bDebentures?\b|\bSubordinat|\bSr\.? Notes|\bBaby Bond|"
    r"\bTrust Preferred\b|\bCapital Securities\b|\bConvertible Note",
    re.I,
)
# Names/tickers that denote a fund/ETP (profile as a fund, not a company).
FUND_RX = re.compile(
    r"\b(ETF|ETN|ETP|UCITS|Fund)\b|ProShares|Direxion|iShares|SPDR|Invesco|VanEck|"
    r"MicroSectors|GraniteShares|UltraPro|UltraShort|\bUltra\b|Leveraged|Inverse|"
    r"\b[23]X\b|Index Fund|Index ETN|Bitcoin Strategy|Futures Fund|YieldMax|"
    r"Roundhill|Global X|Defiance|Simplify|First Trust|WisdomTree|Pacer|Amplify",
    re.I,
)


def slug(t: str) -> str:
    return re.sub(r"[^a-z0-9-]", "-", str(t).lower()) + "-stock"


def listing_map() -> dict[str, dict]:
    """{SYM: {name, etf}} from NASDAQ Trader files (descriptive names, ETF flag)."""
    out: dict[str, dict] = {}
    for path, sym_i, name_i, etf_i in (("scripts/_nasdaqlisted.txt", 0, 1, 6),
                                       ("scripts/_otherlisted.txt", 0, 1, 4)):
        if not os.path.isfile(path):
            continue
        for ln in open(path, encoding="utf-8", errors="replace").read().splitlines()[1:]:
            if ln.startswith("File Creation Time"):
                continue
            c = ln.split("|")
            if len(c) <= max(sym_i, name_i, etf_i):
                continue
            out.setdefault(c[sym_i].strip().upper(),
                           {"name": c[name_i].strip(), "etf": c[etf_i].strip() == "Y"})
    return out


def main() -> int:
    have = {os.path.basename(p)[:-3]
            for p in glob.glob("content/companies/*/*-stock.md")}
    lm = listing_map()
    src = json.load(open(SRC, encoding="utf-8"))
    companies, etfs, seen = [], [], set()
    dropped_junk = 0
    for v in src.values():
        t = str(v.get("ticker", "")).strip()
        if not t:
            continue
        s = slug(t)
        if s in have or s in seen:
            continue
        seen.add(s)
        listing = lm.get(t.upper())
        # require a real US-exchange listing (drops OTC foreign duplicates,
        # issuer-titled OTC ETNs, and other deep-tail noise that the SEC source
        # carries but that we cannot profile cleanly)
        if not listing or not listing["name"]:
            dropped_junk += 1
            continue
        title = listing["name"]
        # drop non-profile-able securities (preferreds, warrants, units, notes, ...)
        if "-" in t or JUNK_RX.search(title):
            dropped_junk += 1
            continue
        is_etf = (listing["etf"]
                  or bool(FUND_RX.search(title))
                  or "ETN" in title.upper())
        rec = {"ticker": t, "title": title,
               "cik_str": v.get("cik_str", ""), "is_etf": is_etf}
        (etfs if is_etf else companies).append(rec)

    ordered = (companies + etfs)[:TARGET]
    out = {str(i): rec for i, rec in enumerate(ordered)}
    json.dump(out, open(OUT, "w", encoding="utf-8"), indent=1)

    ncomp = sum(1 for r in ordered if not r["is_etf"])
    print(f"available clean: companies={len(companies)} etfs={len(etfs)} (dropped junk={dropped_junk})")
    print(f"wrote {OUT}: {len(ordered)} tickers ({ncomp} companies, {len(ordered)-ncomp} ETPs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

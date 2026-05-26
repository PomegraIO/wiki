#!/usr/bin/env python3
"""Plan the next batch of company profiles from the SEC canonical ticker list.

Reads scripts/_sec_tickers.json (SEC's company_tickers.json, ordered by
prominence) and the company slugs already on disk, then reports the candidate
pool and how the next N would distribute. Writes nothing unless --emit.
"""
from __future__ import annotations
import argparse, glob, json, os, re

SEC = "scripts/_sec_tickers.json"
COMPANIES = "content/companies"


def slugify_ticker(t: str) -> str:
    return re.sub(r"[^a-z0-9-]", "-", t.lower()) + "-stock"


def existing_slugs() -> set[str]:
    return {os.path.basename(p)[:-3]
            for p in glob.glob(os.path.join(COMPANIES, "*", "*-stock.md"))}


def load_sec() -> list[dict]:
    d = json.load(open(SEC, encoding="utf-8"))
    rows = []
    for v in d.values():
        t = str(v["ticker"]).strip()
        if not t:
            continue
        rows.append({
            "ticker": t,
            "cik": str(v["cik_str"]).zfill(10),
            "name": v["title"].strip(),
            "slug": slugify_ticker(t),
        })
    return rows  # already in SEC prominence order


def first_letter(slug: str) -> str:
    c = slug[0]
    return c if c.isalpha() else "#"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000, help="size of next batch")
    ap.add_argument("--emit", help="write the locked plan JSON to this path")
    args = ap.parse_args()

    sec = load_sec()
    have = existing_slugs()
    sec_slugs = {r["slug"] for r in sec}

    # candidates = SEC rows not yet on disk, in prominence order, de-duplicated
    seen, candidates = set(), []
    for r in sec:
        if r["slug"] in have or r["slug"] in seen:
            continue
        seen.add(r["slug"])
        candidates.append(r)

    on_disk_in_sec = len(have & sec_slugs)
    print(f"SEC companies:            {len(sec)}")
    print(f"unique SEC slugs:         {len(sec_slugs)}")
    print(f"already on disk:          {len(have)}  ({on_disk_in_sec} of them are in the SEC list)")
    print(f"candidate pool (un-done): {len(candidates)}")
    print()

    nxt = candidates[: args.n]
    # letter distribution of the next N
    dist = {}
    for r in nxt:
        dist[first_letter(r["slug"])] = dist.get(first_letter(r["slug"]), 0) + 1
    print(f"next {len(nxt)} by SEC prominence — letter spread:")
    print("  " + "  ".join(f"{k}:{dist[k]}" for k in sorted(dist)))
    print(f"  rank-1 of batch: {nxt[0]['ticker']} ({nxt[0]['name']})")
    print(f"  rank-{len(nxt)} of batch: {nxt[-1]['ticker']} ({nxt[-1]['name']})")
    print("  first 15:", ", ".join(r["ticker"] for r in nxt[:15]))

    if args.emit:
        json.dump(nxt, open(args.emit, "w", encoding="utf-8"), indent=2)
        print(f"\nwrote {len(nxt)} planned companies -> {args.emit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

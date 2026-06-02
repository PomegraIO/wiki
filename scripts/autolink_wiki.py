#!/usr/bin/env python3
"""
autolink_wiki.py — fast, unified in-body cross-linker for company profiles.

Replaces the two slower passes (autolink_companies.py for finance *concepts*
and autolink_company_names.py for *peer companies*) with a single, much faster
matcher so the whole 11k-page company corpus can be enriched in ~1-2 minutes
instead of hours.

Why it's fast
-------------
The old scripts ran ~4,000-13,000 separate ``regex.finditer`` scans over every
file body (~1s/file -> ~3h for the corpus). This one compiles the dictionary
into a *first-token bucket map* and walks each body's word stream once, only
testing phrases that start with the current word. Full corpus ~90s.

What it links (Wikipedia-style: first mention only, never repeats)
------------------------------------------------------------------
* Finance **concepts** — any non-company entry whose title (or a curated
  synonym) appears in the prose: ``free cash flow``, ``operating margin``,
  ``recession``, ``network effect`` ... Single-word concept titles are gated
  by KEEP_SINGLES (the rest are too ambiguous).
* Peer **companies** — multi-word company names (``Goldman Sachs``, ``Taiwan
  Semiconductor``) admitted wholesale; single-word names only from the FAMOUS
  allowlist (built-in + scripts/_famous_singles.txt), matched CASE-SENSITIVELY
  (a bare ``Apple`` must be capitalised) and never from the STOP common-word
  set (``target``, ``visa``, ``snap`` ...).

Safety invariants (identical to the originals)
----------------------------------------------
* Allowlist-safe: a target slug must exist on disk, so no broken link is
  possible.
* Idempotent: a slug already linked in the file is skipped; re-runs add nothing.
* Surgical masking: front matter, the <aside> infobox, any HTML tag, existing
  links/images, fenced + inline code, bare URLs, and heading/blockquote/table
  lines are never touched.
* One link per slug, first occurrence, longest phrase wins at each position,
  never self-link, per-file cap.

Usage
-----
  python scripts/autolink_wiki.py --all --dry-run
  python scripts/autolink_wiki.py --letter z
  python scripts/autolink_wiki.py --all --cap 22
Run from the repo root.
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import re
import sys

CONTENT = "content"
COMPANIES = os.path.join(CONTENT, "companies")
DEFAULT_CAP = 22
MIN_PHRASE_LEN = 4

# --- concept dictionary tuning (ported from autolink_companies.py) ----------
KEEP_SINGLES = {
    "amortization", "depreciation", "goodwill", "ebitda", "dividend",
    "leverage", "securitization", "diversification", "inflation", "deflation",
    "recession", "stagflation", "hyperinflation", "disinflation", "liquidation",
    "merger", "acquisition", "demerger", "divestiture", "spin-off", "spinoff",
    "recapitalization", "restatement", "clawback", "foreclosure", "delinquency",
    "bond", "broker", "custodian", "mortgage", "nasdaq", "finra", "libor",
    "sofr", "backwardation", "contango", "convexity", "tranche", "stablecoin",
    "bitcoin", "ethereum", "underwriting", "moat",
}
STOP_SLUGS = {"about", "atlas", "stock", "share", "company", "public-company"}
SYNONYMS = {
    "10-k": "10-k", "10-q": "10-q", "annual report": "10-k",
    "free cash flow": "free-cash-flow", "gross margin": "gross-margin",
    "operating margin": "operating-margin", "balance sheet": "balance-sheet",
    "income statement": "income-statement", "cash flow statement": "cash-flow-statement",
    "recurring revenue": "recurring-revenue", "network effect": "network-effect",
    "network effects": "network-effect", "economies of scale": "economies-of-scale",
    "intangible assets": "intangible-assets", "deferred revenue": "deferred-revenue",
    "market capitalization": "market-capitalization", "market cap": "market-capitalization",
    "initial public offering": "ipo", "ipo": "ipo",
    "research and development": "research-and-development",
    "supply chain": "supply-chain", "gross profit": "gross-profit",
}

# --- company-name dictionary tuning (ported from autolink_company_names.py) --
SEC_DEFAULT = "scripts/_sec_tickers_expanded.json"
SUFFIX = re.compile(
    r"[,]?\s+(inc|inc\.|incorporated|corp|corp\.|corporation|co|co\.|company|"
    r"companies|ltd|ltd\.|limited|plc|llc|l\.l\.c\.|lp|l\.p\.|holdings|holding|"
    r"group|grp|n\.v\.|nv|s\.a\.|sa|ag|se|the|trust|reit|fund|class [a-c])\.?$",
    re.I,
)
FAMOUS_BUILTIN = {
    "nvidia", "microsoft", "tesla", "netflix", "intel", "oracle", "qualcomm",
    "broadcom", "salesforce", "adobe", "amazon", "alphabet", "google", "meta",
    "facebook", "apple", "disney", "boeing", "pfizer", "moderna", "chevron",
    "walmart", "costco", "starbucks", "nike", "mastercard", "paypal",
    "uber", "lyft", "airbnb", "spotify", "pinterest", "palantir",
    "snowflake", "datadog", "cloudflare", "zoom", "shopify", "coinbase",
    "robinhood", "ford", "stellantis", "rivian", "lucid", "intuit", "workday",
    "servicenow", "vmware", "accenture", "ibm", "cisco", "amd", "micron",
    "asml", "tsmc", "samsung", "sony", "nintendo", "comcast",
    "verizon", "starlink", "spacex", "stripe", "databricks", "anthropic",
    "openai", "twilio", "okta", "crowdstrike", "fortinet", "zscaler", "mongodb",
    "exxon", "conocophillips", "halliburton", "schlumberger", "caterpillar",
    "deere", "honeywell", "lockheed", "raytheon", "siemens", "philips",
    "unitedhealth", "humana", "cigna", "merck", "abbvie", "amgen", "gilead",
    "regeneron", "biogen", "novartis", "roche", "astrazeneca", "sanofi",
    "jpmorgan", "citigroup", "blackrock", "schwab", "fidelity",
    "ferrari", "porsche", "toyota", "honda", "volkswagen", "nestle", "unilever",
}
STOP = {
    "target", "visa", "snap", "match", "gap", "host", "public", "general",
    "american", "national", "first", "capital", "global", "united",
    "international", "centene", "carnival", "booking", "block", "applied",
    "lam", "square", "open", "energy", "power", "sun", "core", "peak", "summit",
    "vital", "vector", "paycom", "now", "go", "on", "up", "the", "select",
}

TOKEN_RX = re.compile(r"[A-Za-z0-9][A-Za-z0-9.'’&-]*")


def norm_token(tok: str) -> str:
    """Compare-form of a token: lowercase, drop apostrophes/dots."""
    return re.sub(r"[.'’]", "", tok.lower())


def tokenize(text: str):
    """Yield (norm, start, end) for each word-like token."""
    for m in TOKEN_RX.finditer(text):
        yield norm_token(m.group(0)), m.start(), m.end()


def load_famous() -> set[str]:
    fam = set(FAMOUS_BUILTIN)
    path = os.path.join("scripts", "_famous_singles.txt")
    if os.path.isfile(path):
        for line in open(path, encoding="utf-8"):
            w = line.strip().lower()
            if w and not w.startswith("#"):
                fam.add(w)
    return fam


def load_stop_phrases() -> set[str]:
    """Generic phrases that coincide with a company name and must never be
    linked (e.g. 'financial institutions', 'premium brands'). Built by the
    audit workflow into scripts/_stop_phrases.txt; matched case-insensitively."""
    stop: set[str] = set()
    path = os.path.join("scripts", "_stop_phrases.txt")
    if os.path.isfile(path):
        for line in open(path, encoding="utf-8"):
            w = line.strip().lower()
            if w and not w.startswith("#"):
                stop.add(w)
    return stop


def slugify_ticker(t: str) -> str:
    return re.sub(r"[^a-z0-9-]", "-", t.lower()) + "-stock"


def clean_name(title: str) -> str:
    n = title.strip()
    for _ in range(3):
        n2 = SUFFIX.sub("", n).strip().rstrip(",.")
        if n2 == n:
            break
        n = n2
    return n


def build_dictionary(sec_path: str):
    """Return (buckets, valid_slugs).

    buckets: dict first-norm-token -> list of (token_tuple, slug, case_sensitive),
    each bucket sorted longest-first so the longest phrase wins at a position.
    """
    # --- concept slugs + titles ---
    valid: set[str] = set()
    title_of: dict[str, str] = {}
    for path in glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True):
        norm = path.replace("\\", "/")
        if "/companies/" in norm:
            continue
        base = os.path.basename(path)
        if base in ("_index.md", "index-a-z.md", "about.md"):
            continue
        slug = base[:-3]
        valid.add(slug)
        try:
            txt = open(path, encoding="utf-8").read()
        except OSError:
            continue
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', txt, re.M)
        if m:
            title_of[slug] = m.group(1).strip()

    stop_phrases = load_stop_phrases()

    # phrase -> (slug, case_sensitive); first writer wins (concepts before companies)
    phrase_to: dict[str, tuple[str, bool]] = {}

    def admit_concept(phrase: str, slug: str) -> None:
        phrase = phrase.lower().strip()
        if len(phrase) < MIN_PHRASE_LEN or slug in STOP_SLUGS or slug not in valid:
            return
        if phrase in stop_phrases:
            return
        if len(phrase.split()) == 1 and slug not in KEEP_SINGLES:
            return
        phrase_to.setdefault(phrase, (slug, False))
        if not phrase.endswith("s"):
            phrase_to.setdefault(phrase + "s", (slug, False))

    for slug, title in title_of.items():
        admit_concept(re.sub(r"\s*\([^)]*\)\s*$", "", title).strip(), slug)
    for phrase, slug in SYNONYMS.items():
        admit_concept(phrase, slug)

    # --- company names ---
    company_slugs = {os.path.basename(p)[:-3]
                     for p in glob.glob(os.path.join(COMPANIES, "*", "*-stock.md"))}
    valid |= company_slugs
    famous = load_famous()
    if os.path.isfile(sec_path):
        sec = json.load(open(sec_path, encoding="utf-8"))
        for v in sec.values():
            if v.get("is_etf"):
                continue
            slug = slugify_ticker(str(v["ticker"]).strip())
            if slug not in company_slugs:
                continue
            name = clean_name(str(v["title"]))
            if len(name) < MIN_PHRASE_LEN:
                continue
            low = name.lower()
            if low in stop_phrases:          # generic phrase flagged by the audit
                continue
            words = name.split()
            if len(words) == 1:
                # single-word company: capitalised match only, FAMOUS, not STOP
                if low in STOP or low not in famous:
                    continue
                phrase_to.setdefault(low, (slug, True))
            else:
                # multi-word: unambiguous, case-insensitive
                phrase_to.setdefault(low, (slug, False))

    # --- bucket by first normalised token ---
    buckets: dict[str, list] = {}
    for phrase, (slug, cs) in phrase_to.items():
        toks = tuple(t for t, _, _ in tokenize(phrase))
        if not toks:
            continue
        buckets.setdefault(toks[0], []).append((toks, slug, cs))
    for k in buckets:
        buckets[k].sort(key=lambda x: len(x[0]), reverse=True)
    return buckets, valid


# --- masking + front matter (ported, unchanged in behaviour) ----------------
def build_mask(body: str) -> list[bool]:
    mask = [False] * len(body)

    def block(rx):
        for m in rx.finditer(body):
            for i in range(m.start(), m.end()):
                mask[i] = True

    block(re.compile(r"<aside\b.*?</aside>", re.S | re.I))
    block(re.compile(r"<[^>]+>"))
    block(re.compile(r"!?\[[^\]]*\]\([^)]*\)"))
    block(re.compile(r"```.*?```", re.S))
    block(re.compile(r"`[^`]*`"))
    block(re.compile(r"https?://\S+"))
    block(re.compile(r'["“”]'))   # never let an anchor span/contain a quote
    for m in re.finditer(r"^.*$", body, re.M):
        if m.group(0).lstrip()[:1] in ("#", ">", "|"):
            for i in range(m.start(), m.end()):
                mask[i] = True
    return mask


def split_front_matter(text: str):
    # Files may begin with a UTF-8 BOM; strip it before testing for "---" or
    # the whole front matter is mistaken for body and links get injected into
    # title/description/keywords (invalid YAML). The BOM is preserved on the
    # front-matter side so it stays at the top of the rewritten file.
    bom = ""
    if text and text[0] == "﻿":
        bom, text = "﻿", text[1:]
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            if nl != -1:
                return bom + text[: nl + 1], text[nl + 1:]
    return bom, text


def linked_slugs(text: str) -> set[str]:
    return set(re.findall(r"\]\((?:/wiki)?/([a-z0-9-]+)/\)", text))


def autolink_file(path, buckets, cap, dry) -> int:
    text = open(path, encoding="utf-8").read()
    fm, body = split_front_matter(text)
    mask = build_mask(body)
    used = linked_slugs(text)
    used.add(os.path.basename(path)[:-3])  # never self-link

    toks = list(tokenize(body))            # (norm, start, end)
    n = len(toks)
    edits: list[tuple[int, int, str]] = []
    added = 0
    i = 0
    while i < n and added < cap:
        cands = buckets.get(toks[i][0])
        if not cands:
            i += 1
            continue
        hit = None
        for phrase_toks, slug, cs in cands:        # longest first
            k = len(phrase_toks)
            if i + k > n or slug in used:
                continue
            if tuple(toks[i + j][0] for j in range(k)) != phrase_toks:
                continue
            s, e = toks[i][1], toks[i + k - 1][2]
            # keep trailing sentence punctuation out of the anchor text
            # ("bonds." -> link "bonds", period stays after the link)
            while e > s and body[e - 1] in ".,;:!?'’":
                e -= 1
            if any(mask[x] for x in range(s, e)):
                continue
            if cs and not body[s].isupper():       # single-word company: need capital
                continue
            hit = (s, e, slug, k)
            break
        if hit:
            s, e, slug, k = hit
            edits.append((s, e, f"[{body[s:e]}](/{slug}/)"))
            used.add(slug)
            added += 1
            i += k
        else:
            i += 1

    if added == 0 or dry:
        return added
    edits.sort()
    out, prev = [], 0
    for s, e, rep in edits:
        out.append(body[prev:s]); out.append(rep); prev = e
    out.append(body[prev:])
    open(path, "w", encoding="utf-8", newline="").write(fm + "".join(out))
    return added


def main() -> int:
    ap = argparse.ArgumentParser(description="Fast unified company autolinker.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--letter")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--cap", type=int, default=DEFAULT_CAP)
    ap.add_argument("--sec", default=SEC_DEFAULT, help="SEC ticker json for company names")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(COMPANIES):
        print(f"error: run from repo root (no {COMPANIES}/)", file=sys.stderr)
        return 2

    buckets, valid = build_dictionary(args.sec)
    nphr = sum(len(v) for v in buckets.values())
    print(f"dictionary: {nphr} phrases in {len(buckets)} buckets -> {len(valid)} valid slugs")

    files = sorted(glob.glob(os.path.join(
        COMPANIES, "*" if args.all else args.letter.lower(), "*-stock.md")))
    if not files:
        print("no company files matched", file=sys.stderr)
        return 1

    total, touched = 0, 0
    for f in files:
        added = autolink_file(f, buckets, args.cap, args.dry_run)
        if added:
            touched += 1
            total += added
    verb = "would add" if args.dry_run else "added"
    print(f"{verb} {total} links across {touched}/{len(files)} files "
          f"(avg {total/max(touched,1):.1f} per touched, cap {args.cap})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

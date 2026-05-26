#!/usr/bin/env python3
"""Link company NAMES mentioned in company profiles to their wiki pages.

Complements autolink_companies.py (which links finance *concepts*). A profile
that names a peer or competitor — "Intel", "Advanced Micro Devices",
"Taiwan Semiconductor" — should link to that company's page. This turns the
company corpus into a connected graph instead of isolated articles.

Precision strategy (company names are proper nouns; false positives read badly):
  * Only link to a company whose page exists on disk.
  * Multi-word names (>= 2 tokens after stripping legal suffixes) are admitted
    wholesale — they are unambiguous ("Berkshire Hathaway", "Goldman Sachs").
  * Single-word names are admitted ONLY from the curated FAMOUS set below
    (avoids "Block", "Match", "Gap", "Host", "Public"... mislinking).
  * Case-SENSITIVE matching with word boundaries (proper nouns are capitalised
    in prose), longest name first, one link per company, never self-link,
    capped per file.
  * Same masking as the concept linker (no infobox, headings, tables, quotes,
    code, existing links, URLs, front matter).

Usage:  python scripts/autolink_company_names.py --letter n --dry-run
        python scripts/autolink_company_names.py --all
Run from repo root.
"""
from __future__ import annotations
import argparse, glob, json, os, re

SEC = "scripts/_sec_tickers.json"
CONTENT = "content"
COMPANIES = "content/companies"
DEFAULT_CAP = 8
MIN_SINGLE_LEN = 3

# Legal suffixes / filler stripped from the end of a company name.
SUFFIX = re.compile(
    r"[,]?\s+(inc|inc\.|incorporated|corp|corp\.|corporation|co|co\.|company|"
    r"companies|ltd|ltd\.|limited|plc|llc|l\.l\.c\.|lp|l\.p\.|holdings|holding|"
    r"group|grp|n\.v\.|nv|s\.a\.|sa|ag|se|the|trust|reit|fund|class [a-c])\.?$",
    re.I,
)

# Distinctive single-word company names safe to link. Edit to taste.
FAMOUS = {
    "nvidia", "microsoft", "tesla", "netflix", "intel", "oracle", "qualcomm",
    "broadcom", "salesforce", "adobe", "amazon", "alphabet", "google", "meta",
    "facebook", "apple", "disney", "boeing", "pfizer", "moderna", "chevron",
    "walmart", "costco", "starbucks", "nike", "visa", "mastercard", "paypal",
    "uber", "lyft", "airbnb", "spotify", "snap", "pinterest", "palantir",
    "snowflake", "datadog", "cloudflare", "zoom", "shopify", "block", "coinbase",
    "robinhood", "ford", "stellantis", "rivian", "lucid", "intuit", "workday",
    "servicenow", "vmware", "accenture", "ibm", "cisco", "amd", "micron",
    "applied", "lam", "asml", "tsmc", "samsung", "sony", "nintendo", "comcast",
    "verizon", "starlink", "spacex", "stripe", "databricks", "anthropic",
    "openai", "twilio", "okta", "crowdstrike", "fortinet", "zscaler", "mongodb",
    "exxon", "conocophillips", "halliburton", "schlumberger", "caterpillar",
    "deere", "honeywell", "lockheed", "raytheon", "ge", "siemens", "philips",
    "unitedhealth", "humana", "cigna", "merck", "abbvie", "amgen", "gilead",
    "regeneron", "biogen", "novartis", "roche", "astrazeneca", "sanofi",
    "jpmorgan", "citigroup", "wells", "blackrock", "schwab", "fidelity",
    "mcdonald", "chipotle", "domino", "kroger", "target", "lowe", "carmax",
    "ferrari", "porsche", "toyota", "honda", "volkswagen", "nestle", "unilever",
}

# Common English words that are also company names — never link as bare words.
STOP = {
    "match", "gap", "host", "public", "general", "american", "national",
    "first", "capital", "global", "united", "international", "centene",
    "carnival", "booking", "block", "applied", "lam",  # ambiguous; require multiword
}


def slugify_ticker(t: str) -> str:
    return re.sub(r"[^a-z0-9-]", "-", t.lower()) + "-stock"


def clean_name(title: str) -> str:
    n = title.strip()
    for _ in range(3):                     # strip up to 3 trailing suffixes
        n2 = SUFFIX.sub("", n).strip().rstrip(",.")
        if n2 == n:
            break
        n = n2
    return n


def disk_company_slugs() -> set[str]:
    return {os.path.basename(p)[:-3]
            for p in glob.glob(os.path.join(COMPANIES, "*", "*-stock.md"))}


def build_name_dictionary():
    on_disk = disk_company_slugs()
    sec = json.load(open(SEC, encoding="utf-8"))
    name_to_slug: dict[str, str] = {}
    for v in sec.values():
        slug = slugify_ticker(str(v["ticker"]).strip())
        if slug not in on_disk:
            continue
        name = clean_name(v["title"])
        if len(name) < 4:
            continue
        low = name.lower()
        words = name.split()
        if len(words) == 1:
            if low in STOP or low not in FAMOUS or len(name) < MIN_SINGLE_LEN:
                continue
        # keep the longest name mapping to a given target
        if name not in name_to_slug:
            name_to_slug[name] = slug

    variants = []
    for name, slug in name_to_slug.items():
        # case-insensitive: SEC names are UPPERCASE, prose is Title Case. The
        # anchor uses the matched prose text, so casing stays natural.
        rx = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", re.I)
        variants.append((name, slug, rx))
    variants.sort(key=lambda x: len(x[0]), reverse=True)
    return variants


# --- masking + helpers shared in spirit with autolink_companies.py ----------
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
    for m in re.finditer(r"^.*$", body, re.M):
        if m.group(0).lstrip()[:1] in ("#", ">", "|"):
            for i in range(m.start(), m.end()):
                mask[i] = True
    return mask


def split_front_matter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            if nl != -1:
                return text[: nl + 1], text[nl + 1:]
    return "", text


def linked_slugs(text: str) -> set[str]:
    return set(re.findall(r"\]\((?:/wiki)?/([a-z0-9-]+)/\)", text))


def autolink_file(path, variants, cap, dry) -> int:
    text = open(path, encoding="utf-8").read()
    fm, body = split_front_matter(text)
    mask = build_mask(body)
    used = linked_slugs(text)
    used.add(os.path.basename(path)[:-3])      # never self-link
    occupied = [False] * len(body)
    edits, added = [], 0
    for name, slug, rx in variants:
        if added >= cap:
            break
        if slug in used:
            continue
        for m in rx.finditer(body):
            s, e = m.start(), m.end()
            if any(mask[i] or occupied[i] for i in range(s, e)):
                continue
            edits.append((s, e, f"[{body[s:e]}](/{slug}/)"))
            for i in range(s, e):
                occupied[i] = True
            used.add(slug)
            added += 1
            break
    if added and not dry:
        edits.sort()
        out, prev = [], 0
        for s, e, rep in edits:
            out.append(body[prev:s]); out.append(rep); prev = e
        out.append(body[prev:])
        open(path, "w", encoding="utf-8", newline="").write(fm + "".join(out))
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--letter")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--cap", type=int, default=DEFAULT_CAP)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    variants = build_name_dictionary()
    print(f"company-name dictionary: {len(variants)} names -> on-disk pages")
    files = sorted(glob.glob(os.path.join(
        COMPANIES, "*" if args.all else args.letter.lower(), "*-stock.md")))
    total, touched = 0, 0
    for f in files:
        n = autolink_file(f, variants, args.cap, args.dry_run)
        if n:
            touched += 1; total += n
            print(f"  {'[dry] ' if args.dry_run else ''}+{n} {os.path.basename(f)}")
    print(f"\n{'would add' if args.dry_run else 'added'} {total} company links "
          f"across {touched}/{len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

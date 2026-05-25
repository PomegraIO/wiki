#!/usr/bin/env python3
"""
autolink_companies.py — enrich company profiles with in-body cross-links.

Company entries (content/companies/<letter>/<ticker>-stock.md) historically
carry ~1 cross-link (the 10-K), which reads thin and templatish. This script
scans each company's prose and links the first occurrence of any phrase that
matches an existing concept entry's title, taking a page from ~1 to ~8-12
cross-links — all to slugs that provably exist on disk.

Design guarantees
-----------------
* Allowlist-safe: link targets are derived only from real content/*.md files.
* Idempotent: a slug already linked in the file is never linked again, so
  re-running adds nothing new.
* Surgical: front matter, the <aside> infobox, headings, tables, blockquotes,
  code, existing links/HTML and bare URLs are masked and never touched.
* Conservative: longest phrase wins at each position; one link per slug;
  a per-file cap; single-word terms only from a curated high-precision list.

Usage
-----
  python scripts/autolink_companies.py --letter z --dry-run   # report only
  python scripts/autolink_companies.py --letter z             # apply to z/
  python scripts/autolink_companies.py --all                  # every letter
  python scripts/autolink_companies.py --letter z --cap 12    # tune density

Run from the repo root.
"""
from __future__ import annotations
import argparse
import glob
import os
import re
import sys

CONTENT = "content"
COMPANIES = os.path.join(CONTENT, "companies")
DEFAULT_CAP = 12          # max links this script will ADD per file
MIN_PHRASE_LEN = 4        # ignore very short phrases

# --- Curated single-word allowlist -----------------------------------------
# Multi-word concept titles are precise enough to auto-link wholesale. Single
# words mostly are not ("lead", "gold", "alpha", "spread"...), so single-word
# titles are EXCLUDED by default and only the unambiguous, high-value finance
# terms below are re-admitted. Edit this set to tune precision.
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

# Slugs to never auto-link even if multi-word (too generic / would read odd).
STOP_SLUGS = {
    "about", "atlas", "stock", "share", "company", "public-company",
}

# Hand-curated synonyms: phrase -> slug. Added on top of the title dictionary
# to catch common surface forms that differ from the entry title.
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


def slug_exists(slug: str, valid: set[str]) -> bool:
    return slug in valid


def build_dictionary() -> tuple[list[tuple[str, str]], set[str]]:
    """Return (variants, valid_slugs).

    variants: list of (phrase_lower, slug), sorted longest-first, including a
    plural variant for each phrase.
    valid_slugs: every concept slug on disk (the allowlist).
    """
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

    phrase_to_slug: dict[str, str] = {}

    def admit(phrase: str, slug: str) -> None:
        phrase = phrase.lower().strip()
        if len(phrase) < MIN_PHRASE_LEN:
            return
        if slug in STOP_SLUGS or not slug_exists(slug, valid):
            return
        # single-word phrases gated by the curated allowlist
        if len(phrase.split()) == 1 and slug not in KEEP_SINGLES:
            return
        # prefer the longest phrase already mapped to a target on collision
        cur = phrase_to_slug.get(phrase)
        if cur is None:
            phrase_to_slug[phrase] = slug

    for slug, title in title_of.items():
        # drop a trailing parenthetical, e.g. "Earnings per share (EPS)"
        clean = re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()
        admit(clean, slug)
    for phrase, slug in SYNONYMS.items():
        admit(phrase, slug)

    # Build variant list with a simple plural form. Each variant carries a
    # precompiled regex so the per-file loop never recompiles (compiling ~4k
    # patterns once, not once per company file, keeps a full-corpus run fast).
    variants: list[tuple[str, str, re.Pattern]] = []
    seen: set[str] = set()
    for phrase, slug in phrase_to_slug.items():
        forms = [phrase]
        if not phrase.endswith("s"):
            forms.append(phrase + "s")
        for f in forms:
            if f not in seen:
                seen.add(f)
                rx = re.compile(r"(?<![\w-])" + re.escape(f) + r"(?![\w-])", re.I)
                variants.append((f, slug, rx))
    # longest first so "cash flow statement" beats "cash flow"
    variants.sort(key=lambda x: len(x[0]), reverse=True)
    return variants, valid


def build_mask(body: str) -> list[bool]:
    """Mark every character that must NOT be linkified."""
    mask = [False] * len(body)

    def block(rx: re.Pattern) -> None:
        for m in rx.finditer(body):
            for i in range(m.start(), m.end()):
                mask[i] = True

    # whole <aside>...</aside> infobox blocks (and any other HTML block)
    block(re.compile(r"<aside\b.*?</aside>", re.S | re.I))
    # any HTML tag
    block(re.compile(r"<[^>]+>"))
    # existing markdown links / images: [text](url)  and  ![alt](url)
    block(re.compile(r"!?\[[^\]]*\]\([^)]*\)"))
    # fenced code blocks and inline code
    block(re.compile(r"```.*?```", re.S))
    block(re.compile(r"`[^`]*`"))
    # bare URLs
    block(re.compile(r"https?://\S+"))
    # whole lines that are headings / blockquotes / table rows / bold-only
    for m in re.finditer(r"^.*$", body, re.M):
        line = m.group(0)
        stripped = line.lstrip()
        if stripped[:1] in ("#", ">", "|"):
            for i in range(m.start(), m.end()):
                mask[i] = True
    return mask


def existing_linked_slugs(text: str) -> set[str]:
    out = set()
    for m in re.finditer(r"\]\((?:/wiki)?/([a-z0-9-]+)/\)", text):
        out.add(m.group(1))
    return out


def split_front_matter(text: str) -> tuple[str, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            if nl != -1:
                return text[: nl + 1], text[nl + 1 :]
    return "", text


def autolink_file(path: str, variants, valid, cap, dry) -> int:
    text = open(path, encoding="utf-8").read()
    fm, body = split_front_matter(text)
    mask = build_mask(body)
    used = existing_linked_slugs(text)
    self_slug = os.path.basename(path)[:-3]
    used.add(self_slug)

    # collect non-overlapping accepted edits as (start, end, replacement)
    edits: list[tuple[int, int, str]] = []
    occupied = [False] * len(body)
    added = 0
    for phrase, slug, rx in variants:
        if added >= cap:
            break
        if slug in used:
            continue
        for m in rx.finditer(body):
            s, e = m.start(), m.end()
            if any(mask[i] or occupied[i] for i in range(s, e)):
                continue
            matched = body[s:e]
            edits.append((s, e, f"[{matched}](/{slug}/)"))
            for i in range(s, e):
                occupied[i] = True
            used.add(slug)
            added += 1
            break  # first occurrence of this slug only
        else:
            continue

    if added == 0:
        return 0
    if dry:
        return added
    edits.sort()
    out = []
    prev = 0
    for s, e, rep in edits:
        out.append(body[prev:s])
        out.append(rep)
        prev = e
    out.append(body[prev:])
    open(path, "w", encoding="utf-8", newline="").write(fm + "".join(out))
    return added


def main() -> int:
    ap = argparse.ArgumentParser(description="Autolink company profiles to concept entries.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--letter", help="single letter folder under content/companies, e.g. z")
    g.add_argument("--all", action="store_true", help="process every letter folder")
    ap.add_argument("--cap", type=int, default=DEFAULT_CAP, help="max links added per file")
    ap.add_argument("--dry-run", action="store_true", help="report counts, write nothing")
    args = ap.parse_args()

    if not os.path.isdir(COMPANIES):
        print(f"error: run from repo root (no {COMPANIES}/)", file=sys.stderr)
        return 2

    variants, valid = build_dictionary()
    print(f"dictionary: {len(variants)} phrase variants -> {len(valid)} valid slugs")

    if args.all:
        files = sorted(glob.glob(os.path.join(COMPANIES, "*", "*-stock.md")))
    else:
        letter = args.letter.lower()
        files = sorted(glob.glob(os.path.join(COMPANIES, letter, "*-stock.md")))
    if not files:
        print("no company files matched", file=sys.stderr)
        return 1

    total_added = 0
    touched = 0
    for f in files:
        n = autolink_file(f, variants, valid, args.cap, args.dry_run)
        if n:
            touched += 1
            total_added += n
            print(f"  {'[dry] ' if args.dry_run else ''}+{n:2d}  {os.path.basename(f)}")
    verb = "would add" if args.dry_run else "added"
    print(f"\n{verb} {total_added} links across {touched}/{len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

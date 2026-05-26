#!/usr/bin/env python3
"""Unwrap internal markdown links whose target slug does not exist on disk.

`[text](/slug/)` or `[text](/wiki/slug/)` -> `text`  when no content/**/slug.md
exists. Fixes fabricated links from writer agents and the pre-existing
hand-authored broken links in one idempotent pass. Concept-vs-company is
irrelevant — the only test is "does a file with that slug exist".

Usage:
  python scripts/fix_broken_links.py --letter n --dry-run
  python scripts/fix_broken_links.py --all
Run from repo root.
"""
from __future__ import annotations
import argparse, glob, os, re

CONTENT = "content"
COMPANIES = "content/companies"
LINK = re.compile(r"\[([^\]]+)\]\((?:/wiki)?/([a-z0-9-]+)/\)")


def valid_slugs() -> set[str]:
    return {os.path.basename(p)[:-3]
            for p in glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)
            if not os.path.basename(p).startswith("_")}


def fix_text(text: str, valid: set[str]) -> tuple[str, list[str]]:
    removed: list[str] = []

    def repl(m: re.Match) -> str:
        anchor, slug = m.group(1), m.group(2)
        if slug in valid:
            return m.group(0)
        removed.append(slug)
        return anchor  # unwrap to plain text

    return LINK.sub(repl, text), removed


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--letter")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    valid = valid_slugs()
    pat = os.path.join(COMPANIES, "*" if args.all else args.letter.lower(), "*-stock.md")
    files = sorted(glob.glob(pat))

    total, touched = 0, 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        fixed, removed = fix_text(text, valid)
        if removed:
            touched += 1
            total += len(removed)
            print(f"  {'[dry] ' if args.dry_run else ''}{os.path.basename(f)}: "
                  f"unwrapped {len(removed)} -> {sorted(set(removed))}")
            if not args.dry_run:
                open(f, "w", encoding="utf-8", newline="").write(fixed)
    verb = "would unwrap" if args.dry_run else "unwrapped"
    print(f"\n{verb} {total} broken links across {touched}/{len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

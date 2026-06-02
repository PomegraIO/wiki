#!/usr/bin/env python3
"""
clean_stop_links.py — remove generic-phrase -> company mislinks.

Earlier autolink runs (before the audit STOP-list existed) linked generic
noun phrases to a company that merely shares the name: ``[financial
institutions](/fisi-stock/)``, ``[national bank](/nbhc-stock/)``,
``[quantum computing](/qubt-stock/)``. This pass unlinks them — keeping the
visible text, dropping only the link — when:

  * the anchor text (normalised: lower-case, collapsed whitespace) is in the
    audited STOP set (scripts/_stop_phrases.txt), AND
  * the link target is a real COMPANY page (content/companies/<l>/<slug>.md).

Concept targets are never touched, so a legitimate ``[real estate](/real-estate/)``
stays. Anchor text is preserved verbatim, so prose reads unchanged.

Usage:
  python scripts/clean_stop_links.py --dry-run
  python scripts/clean_stop_links.py
Run from repo root.
"""
from __future__ import annotations
import argparse
import glob
import os
import re

LINK_RX = re.compile(r"\[([^\]\n]+?)\]\(/(?:wiki/)?([a-z0-9-]+)/\)")


def norm(text: str) -> str:
    return " ".join(text.lower().split())


def load_stop() -> set[str]:
    path = os.path.join("scripts", "_stop_phrases.txt")
    out: set[str] = set()
    if os.path.isfile(path):
        for line in open(path, encoding="utf-8"):
            w = line.strip()
            if w and not w.startswith("#"):
                out.add(norm(w))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    stop = load_stop()
    company_slugs = {os.path.basename(p)[:-3]
                     for p in glob.glob("content/companies/*/*-stock.md")}
    if not stop:
        print("no stop phrases loaded; nothing to do")
        return 0

    total_removed = 0
    files_touched = 0
    sample: list[str] = []

    for path in glob.glob("content/companies/*/*-stock.md"):
        text = open(path, encoding="utf-8").read()
        removed_here = 0

        def repl(m: re.Match) -> str:
            nonlocal removed_here
            label, slug = m.group(1), m.group(2)
            if slug in company_slugs and norm(label) in stop:
                removed_here += 1
                if len(sample) < 15:
                    sample.append(f"[{label}](/{slug}/)")
                return label                      # keep text, drop the link
            return m.group(0)

        new = LINK_RX.sub(repl, text)
        if removed_here:
            files_touched += 1
            total_removed += removed_here
            if not args.dry_run:
                open(path, "w", encoding="utf-8", newline="").write(new)

    verb = "would unlink" if args.dry_run else "unlinked"
    print(f"{verb} {total_removed} generic-phrase->company mislinks "
          f"across {files_touched} files")
    if sample:
        print("sample:")
        for s in sample:
            print("  ", s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

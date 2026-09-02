#!/usr/bin/env python3
"""Second-pass link fixer for malformed-target markdown links.

fix_relative_links.py caught bare-slug relative links (`](slug)`). A
broader corpus scan (2026-08-22, prompted by a GSC 404 sample where 630
of 1,000 sampled 404s were `/wiki/<page>/<junk>` nested paths) turned up
five more distinct authoring-tool bugs that ALSO produce crawlable 404s
or dead links, none of which the first pass's regex could see:

  1. Double-open-paren:  ]((/slug/)          -> ](/slug/)
     A stray extra "(" before an otherwise-correct absolute link.
  2. Zero-width-space:   ](​/slug/)     -> ](/slug/)
     A U+200B landed between "(" and "/", which most Markdown parsers
     do not treat as insignificant whitespace inside a link
     destination, so the link fails to parse as a link at all.
  3. Dot-relative:       ](./slug.md)        -> (/slug/) or unwrap
                         ](../slug/)
     Since `[permalinks.page] '/**' = '/:contentbasename/'` flattens
     every slug to the wiki root regardless of its content/ subdirectory,
     a dot-relative path resolves relative to the CURRENT PAGE's own
     URL, not to the target's real location — producing exactly the
     nested-path 404s GSC is reporting.
  4. Empty target:       ]()                 -> unwrap
     No destination at all.
  5. Leaked asset path:  (forex.svg) / (/forex.svg) / (/forex.svg/)
     A section icon (static/svg/forex.svg, used correctly elsewhere as
     an <img src>) leaking into inline links with unrelated labels
     (Settlement, Slippage, Hedge Fund, ...). There is no single-page
     forex hub to redirect these to, so they unwrap.

"Unwrap" = same behavior as check_links.py --fix and
fix_relative_links.py: drop the [ ]( ) wrapper, keep the visible label
text. Byte-faithful I/O (CRLF, occasional BOM) — see fix_relative_links.py
for why.

Usage (from repo root):
    python3 scripts/fix_malformed_links.py --dry-run
    python3 scripts/fix_malformed_links.py
Report -> scripts/_malformed_link_fixes.txt (gitignored scratch).
"""

import argparse
import os
import re
import sys

CONTENT = "content"
REPORT = "scripts/_malformed_link_fixes.txt"
ZWSP = "​"

DOUBLE_PAREN_RE = re.compile(r"\]\(\((/[a-z0-9-]+/)\)")
ZWSP_RE = re.compile(r"\]\(" + ZWSP + r"(/[a-z0-9./-]+)\)")
DOT_REL_RE = re.compile(r"\[([^\[\]]*)\]\(\.{1,2}/([a-z0-9-]+)(?:\.md)?/?\)")
EMPTY_RE = re.compile(r"\[([^\[\]]*)\]\(\)")
# Any section icon (static/svg/<section>.svg) leaking into an inline link, not
# just forex.svg - the same authoring bug hit commodities.svg, technical-analysis.svg, ...
FOREX_SVG_RE = re.compile(r"\[([^\[\]]*)\]\(/?[a-z0-9-]+\.svg/?\)")

# ---- Third pass (2026-09-02), prompted by the buckets the first two passes
# could not see because every earlier regex rejected an interior "/":
#
#   6. Phantom route:      ](/link/slug/)       -> ](/slug/)
#      55 links in 4 files pointed at a /link/ prefix that has never existed.
#   7. Category path:      ](/equity/slug/)     -> ](/slug/)
#                          ](/wiki/equity/slug/)
#      923 links in 78 files used the on-disk content/ sub-directory as if it
#      were part of the URL. It is not: hugo.toml flattens every entry to
#      /:contentbasename/. (The legacy 2-segment `](/wiki/slug/)` form is
#      deliberately left alone - canonifyURLs handles it and there are 31k.)
#   8. Markdown filename:  ](/slug.md)          -> ](/slug/)
#                          ](https://slug.md)
#      50 links in 6 files; Hugo does not resolve .md at these permalink
#      settings, and one writer invented a `https://federal-reserve.md` host.
#   9. Double-close residue: ](/slug/))         -> ](/slug/)
#                            [[x](/slug/))       -> [x](/slug/)
#      Left behind by rule 1 when the source was `[x]((/slug/))`. A "))" is
#      only treated as residue when the text before the link on that line has
#      no unmatched "(", so a legitimate "(see [x](/y/))" survives.
#  10. Junk target:          ](/.) ](/—) ](/])   -> unwrap
#      A lone punctuation mark where the slug should be.
#  11. Uppercase slug:       ](/10-K/) ](/AVGO-stock/) -> ](/10-k/) or unwrap
#      Slugs on disk are lowercase and nginx is case-sensitive, so the
#      mixed-case spelling is a 404 even when the entry exists.
LINK_ROUTE_RE = re.compile(r"\[([^\[\]]*)\]\(/link/([a-z0-9-]+)/?\)")
CATEGORY_PATH_RE = re.compile(r"\[([^\[\]]*)\]\(/((?:[a-z0-9-]+/)+)([a-z0-9-]+)/?\)")
MD_EXT_RE = re.compile(r"\[([^\[\]]*)\]\(/([a-z0-9-]+)\.md/?\)")
MD_HOST_RE = re.compile(r"\[([^\[\]]*)\]\(https?://([a-z0-9-]+)\.md/?\)")
DOUBLE_BRACKET_CLOSE_RE = re.compile(r"\[\[([^\[\]]*)\]\((/[a-z0-9-]+/)\)\)")
DOUBLE_CLOSE_RE = re.compile(r"\]\((/[a-z0-9-]+/)\)\)")
LINK_DEST_RE = re.compile(r"\]\([^)]*\)")  # for paren balancing of prose only
JUNK_TARGET_RE = re.compile(r"\[([^\[\]]*)\]\((?:/[.\]—–]/?|/wiki/{1,3}|/{2,3})\)")
#  14. Trailing junk after a good slug: ](/slug//) ](/slug/]) -> ](/slug/)
TRAILING_JUNK_RE = re.compile(r"\[([^\[\]]*)\]\(/((?:wiki/)?[a-z0-9-]+)(?://|/\])\)")
#  15. Apostrophe in slug:  ](/moody's/)        -> ](/moodys/) or unwrap
APOSTROPHE_RE = re.compile(r"\[([^\[\]]*)\]\(/([a-z0-9-]*['’][a-z0-9'’-]*)/?\)")
#  16. Placeholder host:    ](/https://example.com/) -> unwrap
#      A writer left the template's dummy URL in place.
EXAMPLE_HOST_RE = re.compile(r"\[([^\[\]]*)\]\(/?https?://(?:www\.)?example\.(?:com|org|net)/?[^)\s]*\)")
UPPERCASE_RE = re.compile(r"\[([^\[\]]*)\]\(/((?:wiki/)?[A-Za-z0-9-]*[A-Z][A-Za-z0-9-]*)/?\)")
#  12. Query-style slug:     ](/?stock/)         -> ](/stock/)
QUERY_SLUG_RE = re.compile(r"\[([^\[\]]*)\]\(/\?([a-z0-9-]+)/?\)")
#  13. Anchored section path: ](/regulators/#cftc) -> unwrap
#      Points at a heading on a hub page that does not exist as a URL.
ANCHORED_PATH_RE = re.compile(r"\[([^\[\]]*)\]\(/[a-z0-9-]+/#[A-Za-z0-9_-]*\)")


def existing_slugs():
    slugs = set()
    for root, _dirs, files in os.walk(CONTENT):
        for f in files:
            if f.endswith(".md"):
                slugs.add(f[:-3].lower())
    return slugs


def fix_text(text, slugs, log, relpath):
    changed = False

    def sub_double_paren(m):
        nonlocal changed
        changed = True
        log.append("double-paren\t%s\t%s" % (relpath, m.group(0)))
        return "](%s)" % m.group(1)

    text = DOUBLE_PAREN_RE.sub(sub_double_paren, text)

    def sub_zwsp(m):
        nonlocal changed
        changed = True
        log.append("zwsp\t%s\t%s" % (relpath, m.group(0)))
        return "](%s)" % m.group(1)

    text = ZWSP_RE.sub(sub_zwsp, text)

    def sub_dot_rel(m):
        nonlocal changed
        label, slug = m.group(1), m.group(2).lower()
        changed = True
        if slug in slugs:
            log.append("dot-rel-abs\t%s\t%s" % (relpath, m.group(0)))
            return "[%s](/%s/)" % (label, slug)
        log.append("dot-rel-unwrap\t%s\t%s" % (relpath, m.group(0)))
        return label

    text = DOT_REL_RE.sub(sub_dot_rel, text)

    def sub_empty(m):
        nonlocal changed
        changed = True
        log.append("empty-unwrap\t%s\t%s" % (relpath, m.group(0)))
        return m.group(1)

    text = EMPTY_RE.sub(sub_empty, text)

    def sub_forex(m):
        nonlocal changed
        changed = True
        log.append("forex-svg-unwrap\t%s\t%s" % (relpath, m.group(0)))
        return m.group(1)

    text = FOREX_SVG_RE.sub(sub_forex, text)

    def relink(kind, m, label, slug):
        """Rewrite to the flat /slug/ when it exists, else unwrap to the label."""
        nonlocal changed
        changed = True
        slug = slug.lower()
        if slug in slugs:
            log.append("%s-abs\t%s\t%s" % (kind, relpath, m.group(0)))
            return "[%s](/%s/)" % (label, slug)
        log.append("%s-unwrap\t%s\t%s" % (kind, relpath, m.group(0)))
        return label

    text = LINK_ROUTE_RE.sub(lambda m: relink("link-route", m, m.group(1), m.group(2)), text)

    def sub_category_path(m):
        prefix = m.group(2)  # e.g. "equity/" or "wiki/equity/" (always ends in "/")
        if prefix == "wiki/":
            return m.group(0)  # legacy /wiki/slug/ form - handled by canonifyURLs
        return relink("category-path", m, m.group(1), m.group(3))

    text = CATEGORY_PATH_RE.sub(sub_category_path, text)
    text = MD_EXT_RE.sub(lambda m: relink("md-ext", m, m.group(1), m.group(2)), text)
    text = MD_HOST_RE.sub(lambda m: relink("md-host", m, m.group(1), m.group(2)), text)

    def sub_double_bracket(m):
        nonlocal changed
        changed = True
        log.append("double-close\t%s\t%s" % (relpath, m.group(0)))
        return "[%s](%s)" % (m.group(1), m.group(2))

    def fix_double_close(line):
        def sub(m):
            nonlocal changed
            # Prose before the link, with other link destinations removed so
            # their parens do not count. An unmatched "(" there means the
            # trailing ")" closes a real parenthetical - leave it alone.
            prose = LINK_DEST_RE.sub("", line[: m.start()])
            if prose.count("(") > prose.count(")"):
                return m.group(0)
            changed = True
            log.append("double-close\t%s\t%s" % (relpath, m.group(0)))
            return "](%s)" % m.group(1)

        return DOUBLE_CLOSE_RE.sub(sub, line)

    if "))" in text:
        text = DOUBLE_BRACKET_CLOSE_RE.sub(sub_double_bracket, text)
        # splitlines(keepends=True) preserves CRLF/LF byte-for-byte.
        text = "".join(fix_double_close(l) for l in text.splitlines(keepends=True))

    def sub_junk(m):
        nonlocal changed
        changed = True
        log.append("junk-unwrap\t%s\t%s" % (relpath, m.group(0)))
        return m.group(1)

    text = JUNK_TARGET_RE.sub(sub_junk, text)

    text = UPPERCASE_RE.sub(
        lambda m: relink("uppercase", m, m.group(1), m.group(2).removeprefix("wiki/")), text
    )
    text = QUERY_SLUG_RE.sub(lambda m: relink("query-slug", m, m.group(1), m.group(2)), text)

    def sub_anchored(m):
        nonlocal changed
        changed = True
        log.append("anchored-unwrap\t%s\t%s" % (relpath, m.group(0)))
        return m.group(1)

    text = ANCHORED_PATH_RE.sub(sub_anchored, text)
    text = TRAILING_JUNK_RE.sub(
        lambda m: relink("trailing-junk", m, m.group(1), m.group(2).removeprefix("wiki/")), text
    )
    text = APOSTROPHE_RE.sub(
        lambda m: relink("apostrophe", m, m.group(1), re.sub(r"['’]", "", m.group(2))), text
    )

    def sub_example(m):
        nonlocal changed
        changed = True
        log.append("example-host-unwrap\t%s\t%s" % (relpath, m.group(0)))
        return m.group(1)

    text = EXAMPLE_HOST_RE.sub(sub_example, text)

    return text, changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    slugs = existing_slugs()
    log = []
    files_changed = 0
    for root, _dirs, files in os.walk(CONTENT):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", newline="") as fh:
                text = fh.read()
            new_text, changed = fix_text(text, slugs, log, path)
            if changed:
                files_changed += 1
                if not args.dry_run:
                    with open(path, "w", encoding="utf-8", newline="") as fh:
                        fh.write(new_text)

    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(log) + "\n")
    from collections import Counter
    counts = Counter(l.split("\t")[0] for l in log)
    mode = "DRY RUN — no files written" if args.dry_run else "applied"
    print("%s: %d fixes in %d files" % (mode, len(log), files_changed))
    for k, v in counts.most_common():
        print("  %-18s %d" % (k, v))
    print("detail -> %s" % REPORT)


if __name__ == "__main__":
    sys.exit(main())

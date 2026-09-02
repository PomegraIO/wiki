#!/usr/bin/env python3
"""Fix relative markdown links that 404 in production.

Cross-links in this wiki must be root-absolute with a trailing slash:
`[Stock](/stock/)`. A writer wave left ~650 links WITHOUT the leading
slash (`[Stock](stock)`, `[EPS](earnings-per-share/)`, even literal
`[term](glossary-link-not-included)` placeholders). Because the pages
live at `/wiki/<slug>/`, browsers resolve those relative to the current
page and produce crawlable 404s like `/wiki/bjdx-stock/BJDX` — GSC's
biggest 404 bucket (630 of a 1,000-row sample on 2026-08-22).

Rules, per inline link `[label](target)` where target has no scheme,
no leading `/` or `#`, and looks like a bare slug (letters/digits/
hyphens, optional `.md` suffix, optional trailing `/`):
  - slug exists in content/  -> rewrite to `](/slug/)`
  - slug does not exist      -> unwrap to plain `label`
    (same behaviour as check_links.py --fix; includes the
    `glossary-link-not-included` placeholders)

Byte-faithful like apply_noindex.py: files are CRLF with occasional
BOMs, so we read/write with newline='' and never reflow anything.

Usage (from repo root):
    python3 scripts/fix_relative_links.py --dry-run
    python3 scripts/fix_relative_links.py
Report written to scripts/_relative_link_fixes.txt (gitignored scratch).
"""

import argparse
import os
import re
import sys

CONTENT = "content"
REPORT = "scripts/_relative_link_fixes.txt"

# ](target) where target is a bare slug-ish token: no scheme, no leading
# '/' or '#', no interior '/', no dots except an optional '.md' suffix.
LINK_RE = re.compile(r"\]\(([A-Za-z0-9][A-Za-z0-9_-]*(?:\.md)?/?)\)")
# The matching '[label](' prefix, found by scanning back from the ']('.
LABEL_RE = re.compile(r"\[([^\[\]]*)\]$")


def existing_slugs():
    slugs = set()
    for root, _dirs, files in os.walk(CONTENT):
        for f in files:
            if f.endswith(".md"):
                slugs.add(f[:-3].lower())
    return slugs


def fix_text(text, slugs, log, relpath):
    out = []
    pos = 0
    changed = False
    for m in LINK_RE.finditer(text):
        target = m.group(1)
        slug = target[:-3] if target.endswith(".md") else target
        slug = slug.rstrip("/").lower()
        # find the [label] immediately before this ](
        head = text[pos:m.start() + 1]  # up to and including ']'
        lm = LABEL_RE.search(text[:m.start() + 1])
        if not lm:
            continue  # image or malformed; leave alone
        # skip image links ![alt](src)
        if lm.start() > 0 and text[lm.start() - 1] == "!":
            continue
        label = lm.group(1)
        if slug in slugs:
            replacement = "[%s](/%s/)" % (label, slug)
            action = "abs"
        else:
            replacement = label
            action = "unwrap"
        out.append(text[pos:lm.start()])
        out.append(replacement)
        pos = m.end()
        changed = True
        log.append("%s\t%s\t[%s](%s)" % (action, relpath, label, target))
    out.append(text[pos:])
    return "".join(out), changed


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
    n_abs = sum(1 for l in log if l.startswith("abs"))
    n_unwrap = sum(1 for l in log if l.startswith("unwrap"))
    mode = "DRY RUN — no files written" if args.dry_run else "applied"
    print("%s: %d links in %d files (%d -> absolute, %d unwrapped)"
          % (mode, len(log), files_changed, n_abs, n_unwrap))
    print("detail -> %s" % REPORT)


if __name__ == "__main__":
    sys.exit(main())

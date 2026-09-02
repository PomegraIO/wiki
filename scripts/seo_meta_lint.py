#!/usr/bin/env python3
"""Lint SEO meta front matter across content/**/*.md.

Flags:
- title longer than 60 chars
- description missing, shorter than 70, or longer than 160 chars
- duplicate titles (same title on 2+ pages)
- duplicate descriptions (same description on 2+ pages)
- seo_title longer than 60 chars (only when the key is present)

Writes scripts/_meta_audit.csv (path,issue,value,length) and prints summary
counts. Idempotent; read-only over content/.

Run from project root:
    python scripts/seo_meta_lint.py
    python scripts/seo_meta_lint.py --paths scripts/_batch_files.txt

`--paths` takes a file with one content path per line (absolute or
repo-relative) and restricts *reported* issues to those files. Duplicate
detection still runs against the whole corpus, so a batch rewrite that
collides with an existing page's title/description is caught.
"""
from __future__ import annotations
import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
SD = Path(__file__).resolve().parent
OUT_CSV = SD / '_meta_audit.csv'

# Tolerates the UTF-8 BOM + CRLF line endings some company pages carry.
FRONT_MATTER_RE = re.compile(r'^(\ufeff?---\r?\n)(.*?)(\r?\n---\r?\n)', re.DOTALL)

TITLE_MAX = 60
DESC_MIN = 70
DESC_MAX = 160


def fm_value(fm: str, key: str) -> str | None:
    """Return the (unquoted) scalar value of a top-level front-matter key."""
    m = re.search(rf'^{key}\s*:[ \t]*(.*)$', fm, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in ('"', "'"):
        val = val[1:-1]
    return val


def collect(paths: list[Path]) -> tuple[list[tuple[str, str, str, int]], dict[str, list[str]], dict[str, list[str]]]:
    """Return (per-file issues, title->paths, description->paths)."""
    issues: list[tuple[str, str, str, int]] = []
    by_title: dict[str, list[str]] = defaultdict(list)
    by_desc: dict[str, list[str]] = defaultdict(list)

    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding='utf-8', errors='replace')
        m = FRONT_MATTER_RE.match(text)
        if not m:
            issues.append((rel, 'no-front-matter', '', 0))
            continue
        fm = m.group(2)

        title = fm_value(fm, 'title')
        desc = fm_value(fm, 'description')
        seo_title = fm_value(fm, 'seo_title')

        if title:
            by_title[title].append(rel)
            if len(title) > TITLE_MAX:
                issues.append((rel, 'title-too-long', title, len(title)))
        else:
            issues.append((rel, 'title-missing', '', 0))

        if desc:
            by_desc[desc].append(rel)
            if len(desc) > DESC_MAX:
                issues.append((rel, 'desc-too-long', desc, len(desc)))
            elif len(desc) < DESC_MIN:
                issues.append((rel, 'desc-too-short', desc, len(desc)))
        else:
            issues.append((rel, 'desc-missing', '', 0))

        if seo_title is not None and len(seo_title) > TITLE_MAX:
            issues.append((rel, 'seo-title-too-long', seo_title, len(seo_title)))

    return issues, by_title, by_desc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--paths', help='file listing content paths to report on (one per line)')
    args = ap.parse_args()

    all_paths = sorted(p for p in CONTENT.rglob('*.md') if p.name != '_index.md')
    issues, by_title, by_desc = collect(all_paths)

    # Duplicate groups are computed over the full corpus.
    for title, rels in by_title.items():
        if len(rels) > 1:
            for rel in rels:
                issues.append((rel, 'dup-title', title, len(rels)))
    for desc, rels in by_desc.items():
        if len(rels) > 1:
            for rel in rels:
                issues.append((rel, 'dup-description', desc, len(rels)))

    if args.paths:
        wanted: set[str] = set()
        for line in Path(args.paths).read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line:
                continue
            p = Path(line)
            if not p.is_absolute():
                p = ROOT / line
            try:
                wanted.add(p.resolve().relative_to(ROOT).as_posix())
            except ValueError:
                wanted.add(line)
        issues = [it for it in issues if it[0] in wanted]
        print(f'restricted to {len(wanted)} listed files')

    issues.sort()
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['path', 'issue', 'value', 'length'])
        w.writerows(issues)

    counts: dict[str, int] = defaultdict(int)
    for _, issue, _, _ in issues:
        counts[issue] += 1
    print(f'scanned {len(all_paths)} files; {len(issues)} issue rows -> {OUT_CSV.relative_to(ROOT).as_posix()}')
    for issue in sorted(counts):
        print(f'  {issue:<20} {counts[issue]}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

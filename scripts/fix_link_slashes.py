#!/usr/bin/env python3
"""Append a trailing slash to every markdown cross-link of the form
`](/slug)`.

Hugo renders entries at `/wiki/<slug>/` with trailing slash. Without the
slash in the source link, the rendered HTML emits `/wiki/<slug>` and the
browser hits a 301 redirect on every cross-link — wasteful at 10k+ links.

Idempotent: runs are no-ops once every link is already terminated with `/`.
Skip anchors and external URLs — only touches root-relative slugs.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

# Markdown `](/slug)` — single-segment, lowercase + hyphens, no trailing /.
PAT = re.compile(r'\]\((/[a-z0-9][a-z0-9-]*)\)')


def process(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding='utf-8')
    fixes = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal fixes
        fixes += 1
        return f']({m.group(1)}/)'

    new = PAT.sub(repl, text)
    if new != text:
        path.write_text(new, encoding='utf-8')
    return (1 if new != text else 0, fixes)


def main() -> int:
    files = 0
    total = 0
    scanned = 0
    for path in sorted(CONTENT.rglob('*.md')):
        scanned += 1
        changed, fixes = process(path)
        files += changed
        total += fixes
    print(f'Scanned {scanned} files, edited {files}, added trailing / to {total} cross-links.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

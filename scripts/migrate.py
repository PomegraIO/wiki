#!/usr/bin/env python3
"""One-shot migration: strip Docusaurus-only front matter and the in-body H1
from each article in content/. Idempotent: running twice is harmless.
Run from the wiki/ project root: python scripts/migrate.py
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

# Front-matter keys to drop (Docusaurus-specific or now redundant).
DROP_KEYS = {
    'sidebar_label',
    'sidebar_position',
    'displayed_sidebar',
    'hide_table_of_contents',
    'slug',
}

# Articles where the body opens with `# Title` followed by an italic lede.
# Home / about / a-z index are handled separately.
SKIP_FILES = {'_index.md', 'about.md', 'index-a-z.md', 'index.md'}

FRONT_MATTER_RE = re.compile(r'^(---\n.*?\n---\n)', re.DOTALL)


def clean_front_matter(fm: str) -> str:
    """Drop unwanted keys from a YAML front-matter block (delimited by --- ... ---)."""
    out_lines = []
    skip_next_indent = False
    for line in fm.splitlines(keepends=True):
        # Skip continuation lines of a dropped key (indented under it)
        if skip_next_indent and line.startswith((' ', '\t')):
            continue
        skip_next_indent = False
        stripped = line.lstrip()
        # Lines like "key:" or "key: value"
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_-]*)\s*:', stripped)
        if m and m.group(1) in DROP_KEYS:
            # If this key has a multi-line value (key:\n  - val), skip its continuation.
            skip_next_indent = True
            continue
        out_lines.append(line)
    return ''.join(out_lines)


def strip_inbody_h1(body: str) -> str:
    """Remove the first `# Heading` line in the body (and any blank lines around it).
    Hugo's layout renders the article title from front matter."""
    lines = body.splitlines(keepends=True)
    out = []
    removed = False
    for line in lines:
        if not removed and re.match(r'^\s*#\s+\S', line):
            removed = True
            continue
        out.append(line)
    # collapse any double-leading blank lines
    text = ''.join(out)
    text = re.sub(r'^\n+', '', text)
    return text


def process(path: Path) -> bool:
    if path.name in SKIP_FILES:
        return False
    text = path.read_text(encoding='utf-8')
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return False
    fm = m.group(1)
    body = text[m.end():]
    new_fm = clean_front_matter(fm)
    new_body = strip_inbody_h1(body)
    new_text = new_fm + new_body
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(CONTENT.glob('*.md')):
        if process(path):
            changed += 1
            print(f'  cleaned: {path.name}')
    print(f'Done. {changed} files changed.')


if __name__ == '__main__':
    main()

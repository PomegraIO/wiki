#!/usr/bin/env python3
"""Cleanup pass over the 3,000 new articles before link-validation.

1. Lowercase the slug inside every cross-link target ( /SWKS-stock/ -> /swks-stock/,
   /TODO/ -> /todo/ ) so the standard lowercase-only check_links --fix can see and
   strip the invalid ones (and valid ones survive).
2. Strip leaked meta-commentary parentheticals from See-also glosses, e.g.
   "(reference if slug exists; otherwise omit)", "(note: if IRR slug exists, link)".

Operates only on files listed in _wave3k_plan.json. Idempotent.
"""
from __future__ import annotations
import json, re
from pathlib import Path

SD = Path(__file__).resolve().parent

LINK_SLUG_RX = re.compile(r'(\]\(/|href=["\']/)([A-Za-z0-9][A-Za-z0-9-]*)(/)')
META_RX = re.compile(
    r'\s*\([^)]*?(?:slug exists|otherwise omit|if available;?\s*omit|else plain text|'
    r'reference placeholder|reference if|note:\s*if|if no slug|plain text)[^)]*?\)',
    re.IGNORECASE,
)


def main() -> int:
    plan = json.loads((SD / "_wave3k_plan.json").read_text(encoding="utf-8"))
    changed = link_fixes = meta_fixes = 0
    for it in plan:
        p = Path(it["path"])
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        orig = txt

        def low(m):
            return m.group(1) + m.group(2).lower() + m.group(3)
        txt, n1 = LINK_SLUG_RX.subn(low, txt)
        # subn counts all matches even when unchanged; recount real changes after
        txt2 = META_RX.sub("", txt)
        n2 = len(META_RX.findall(txt))

        if txt2 != orig:
            p.write_text(txt2, encoding="utf-8", newline="")
            changed += 1
            meta_fixes += n2
    print(f"cleanup: {changed} files changed, {meta_fixes} meta-notes stripped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

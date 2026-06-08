#!/usr/bin/env python3
"""Cleanup pass over the wave-2k articles (lowercase link slugs, strip leaked
meta-parentheticals) before check_links --fix. Reuses wave3k_cleanup regexes."""
from __future__ import annotations
import json, sys
from pathlib import Path

SD = Path(__file__).resolve().parent
sys.path.insert(0, str(SD))
from wave3k_cleanup import LINK_SLUG_RX, META_RX


def main() -> int:
    plan = json.loads((SD / "_seo4_plan.json").read_text(encoding="utf-8"))
    changed = meta = 0
    for it in plan:
        p = Path(it["path"])
        if not p.exists():
            continue
        orig = p.read_text(encoding="utf-8", errors="replace")
        txt = LINK_SLUG_RX.sub(lambda m: m.group(1) + m.group(2).lower() + m.group(3), orig)
        n = len(META_RX.findall(txt))
        txt = META_RX.sub("", txt)
        if txt != orig:
            p.write_text(txt, encoding="utf-8", newline="")
            changed += 1; meta += n
    print(f"cleanup: {changed} files changed, {meta} meta-notes stripped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

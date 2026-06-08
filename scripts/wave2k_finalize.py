#!/usr/bin/env python3
"""Verify wave-2k: coverage, front matter, forbidden phrases, keyword presence.
Writes scripts/_wave2k_missing.json for a targeted retry wave."""
from __future__ import annotations
import json, re
from pathlib import Path

SD = Path(__file__).resolve().parent
FORBIDDEN = [r"\bplaceholder\b", r"\bscaffolded\b", r"coming soon", r"\bTODO\b",
             r"let's explore", r"let's dive", r"in this article we will",
             r"i hope this helps", r"\bMermaid\b", r"as an ai", r"as a language model"]
FRX = [re.compile(p, re.I) for p in FORBIDDEN]
WORD = re.compile(r"\b\w+\b")


def main() -> int:
    plan = json.loads((SD / "_wave2k_plan.json").read_text(encoding="utf-8"))
    missing, ok, short, nofm, forb, nokw = [], 0, [], [], [], 0
    for it in plan:
        p = Path(it["path"])
        if not p.exists():
            missing.append(it); continue
        ok += 1
        txt = p.read_text(encoding="utf-8", errors="replace")
        if not txt.lstrip().startswith("---"):
            nofm.append(it["rel"])
        if len(WORD.findall(txt)) < 650:
            short.append(it["rel"])
        for rx in FRX:
            m = rx.search(txt)
            if m:
                if rx.pattern == r"\bMermaid\b" and txt.lower().count("mermaid") == txt.lower().count("```mermaid"):
                    continue
                forb.append((it["rel"], m.group(0))); break
        kw = (it.get("keyword") or "").lower()
        if kw and kw not in txt.lower():
            nokw += 1
    (SD / "_wave2k_missing.json").write_text(json.dumps(missing, indent=1), encoding="utf-8")
    print(f"planned:{len(plan)} written:{ok} MISSING:{len(missing)} "
          f"no-fm:{len(nofm)} short:{len(short)} forbidden:{len(forb)} kw-absent:{nokw}")
    for rel, ph in forb[:20]:
        print(f"   forbidden '{ph}'  {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

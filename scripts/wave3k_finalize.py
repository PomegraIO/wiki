#!/usr/bin/env python3
"""Verify the 3,000-article wave: coverage, front matter, forbidden phrases.

Writes scripts/_wave3k_missing.json (planned topics with no file yet) so a
targeted retry wave can be generated. Prints a quality report.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

SD = Path(__file__).resolve().parent
ROOT = SD.parent

FORBIDDEN = [
    r"\bplaceholder\b", r"\bscaffolded\b", r"coming soon", r"\bTODO\b",
    r"let's explore", r"let's dive", r"in this article we will",
    r"i hope this helps", r"\bMermaid\b", r"as an ai", r"as a language model",
]
FORBIDDEN_RX = [re.compile(p, re.I) for p in FORBIDDEN]
WORD_RX = re.compile(r"\b\w+\b")


def main() -> int:
    plan = json.loads((SD / "_wave3k_plan.json").read_text(encoding="utf-8"))
    missing, ok = [], 0
    short, nofm, forbidden_hits = [], [], []
    for it in plan:
        p = Path(it["path"])
        if not p.exists():
            missing.append(it)
            continue
        ok += 1
        txt = p.read_text(encoding="utf-8", errors="replace")
        if not txt.lstrip().startswith("---"):
            nofm.append(it["rel"])
        words = len(WORD_RX.findall(txt))
        if words < 650:
            short.append((it["rel"], words))
        for rx in FORBIDDEN_RX:
            m = rx.search(txt)
            if m:
                # allow ```mermaid fence but not bare visible word
                if rx.pattern == r"\bMermaid\b" and "```mermaid" in txt.lower() and txt.lower().count("mermaid") == txt.lower().count("```mermaid"):
                    continue
                forbidden_hits.append((it["rel"], m.group(0)))
                break

    (SD / "_wave3k_missing.json").write_text(json.dumps(missing, indent=1), encoding="utf-8")
    print(f"planned: {len(plan)}")
    print(f"written: {ok}")
    print(f"MISSING (failed writes): {len(missing)}  -> _wave3k_missing.json")
    print(f"no front matter: {len(nofm)}")
    print(f"short (<650 words): {len(short)}")
    print(f"forbidden-phrase hits: {len(forbidden_hits)}")
    for rel, w in short[:15]:
        print(f"   short {w:5}w  {rel}")
    for rel, ph in forbidden_hits[:20]:
        print(f"   forbidden '{ph}'  {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

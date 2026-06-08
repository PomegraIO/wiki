#!/usr/bin/env python3
"""Collect wave-2k proposer results from workflow agent transcripts.
Usage: python scripts/seo4_collect.py <workflow_dir>
Writes scripts/_seo4_proposals.json = { "buckets": [ {cat,sub,dir,proposals} ] }.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

SD = Path(__file__).resolve().parent


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: seo4_collect.py <workflow_dir>", file=sys.stderr)
        return 2
    wdir = Path(sys.argv[1])
    by_agent: dict[str, dict] = {}
    for f in wdir.glob("agent-*.jsonl"):
        last = None
        for line in f.open(encoding="utf-8"):
            try:
                o = json.loads(line)
            except Exception:
                continue
            for c in (o.get("message", {}).get("content") or []):
                if isinstance(c, dict) and c.get("type") == "tool_use" \
                        and c.get("name") == "StructuredOutput" \
                        and isinstance(c.get("input"), dict) and "proposals" in c["input"]:
                    last = c["input"]
        if last is not None:
            by_agent[f.stem] = last
    buckets, total = [], 0
    for p in by_agent.values():
        props = p.get("proposals") or []
        buckets.append({"cat": p.get("category", ""), "sub": p.get("subcat", ""),
                        "dir": p.get("dir", ""), "proposals": props})
        total += len(props)
    (SD / "_seo4_proposals.json").write_text(
        json.dumps({"buckets": buckets, "totalProposals": total}, indent=1), encoding="utf-8")
    print(f"collected {len(buckets)} buckets, {total} raw proposals -> _seo4_proposals.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

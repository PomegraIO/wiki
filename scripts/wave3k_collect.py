#!/usr/bin/env python3
"""Collect proposer results straight from the workflow agent transcripts.

Robust against truncated workflow return values: scans every agent-*.jsonl in
the given workflow dir, takes each agent's LAST StructuredOutput payload, and
writes scripts/_wave3k_proposals.json as { "buckets": [ {cat,sub,dir,proposals} ] }.

Usage: python scripts/wave3k_collect.py <workflow_dir>
"""
from __future__ import annotations
import json, sys
from pathlib import Path

SD = Path(__file__).resolve().parent


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: wave3k_collect.py <workflow_dir>", file=sys.stderr)
        return 2
    wdir = Path(sys.argv[1])
    if not wdir.is_dir():
        print(f"not a dir: {wdir}", file=sys.stderr)
        return 2

    by_agent: dict[str, dict] = {}  # agentId -> last payload
    for f in wdir.glob("agent-*.jsonl"):
        last = None
        for line in f.open(encoding="utf-8"):
            try:
                o = json.loads(line)
            except Exception:
                continue
            msg = o.get("message", {})
            for c in (msg.get("content") or []):
                if isinstance(c, dict) and c.get("type") == "tool_use" \
                        and c.get("name") == "StructuredOutput" \
                        and isinstance(c.get("input"), dict) \
                        and "proposals" in c["input"]:
                    last = c["input"]
        if last is not None:
            aid = f.stem.replace("agent-", "")
            by_agent[aid] = last

    buckets = []
    total = 0
    for payload in by_agent.values():
        props = payload.get("proposals") or []
        buckets.append({
            "cat": payload.get("category", ""),
            "sub": payload.get("subcat", ""),
            "dir": payload.get("dir", ""),
            "proposals": props,
        })
        total += len(props)

    out = {"buckets": buckets, "totalProposals": total}
    (SD / "_wave3k_proposals.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"collected {len(buckets)} buckets, {total} raw proposals -> _wave3k_proposals.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

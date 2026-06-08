#!/usr/bin/env python3
"""Emit parallel Haiku writer workflows for the company/ETF batch prompts.

Each batch prompt (5 profiles) becomes one agent() call with the prompt embedded
inline. Batches are split into G groups -> G workflow JS files meant to run
concurrently (high parallelism: G x per-workflow-cap agents at once). Also emits
a small test workflow (first --test batches) to de-risk before the full launch.

Usage: python scripts/company_gen_workflows.py --groups 6 --test 3
"""
from __future__ import annotations
import argparse, glob, json, os

SD = os.path.dirname(os.path.abspath(__file__))
BATCH_DIR = os.path.join(SD, "_company_batches_w3k")


def emit(path: str, name: str, desc: str, jobs: list[dict]) -> int:
    js = []
    js.append("export const meta = {")
    js.append(f"  name: {json.dumps(name)},")
    js.append(f"  description: {json.dumps(desc)},")
    js.append("  phases: [{ title: 'Write' }],")
    js.append("}")
    js.append("const JOBS = " + json.dumps(jobs) + ";")
    js.append("phase('Write')")
    js.append(f"log(`{name}: ${{JOBS.length}} batch-agents x 5 profiles`)")
    js.append("const res = await parallel(JOBS.map(j => () =>")
    js.append("  agent(j.prompt, { label: j.label, phase: 'Write', model: 'haiku' })")
    js.append("    .then(r => r ? 1 : 0).catch(() => 0)))")
    js.append("const done = res.filter(Boolean).length")
    js.append(f"log(`{name}: ${{done}}/${{JOBS.length}} agents finished`)")
    js.append(f"return {{ group: {json.dumps(name)}, agents: JOBS.length, finished: done }}")
    open(path, "w", encoding="utf-8").write("\n".join(js))
    return os.path.getsize(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", type=int, default=6)
    ap.add_argument("--test", type=int, default=3)
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(BATCH_DIR, "b*.md")))
    jobs = []
    for f in files:
        bid = os.path.basename(f)[:-3]
        jobs.append({"label": f"co:{bid}", "prompt": open(f, encoding="utf-8").read()})

    # test workflow: first N batches
    if args.test > 0:
        sz = emit(os.path.join(SD, "_company_w3k_writers_test.js"),
                  "co-w3k-test", "Company/ETF writers — de-risk test", jobs[:args.test])
        print(f"test: {args.test} agents -> _company_w3k_writers_test.js ({sz} bytes)")

    # G groups covering ALL batches (round-robin so each group is mixed)
    groups = [[] for _ in range(args.groups)]
    for i, j in enumerate(jobs):
        groups[i % args.groups].append(j)
    for gi, g in enumerate(groups):
        sz = emit(os.path.join(SD, f"_company_w3k_writers_g{gi}.js"),
                  f"co-w3k-g{gi}", f"Company/ETF writers — group {gi}", g)
        print(f"group {gi}: {len(g)} agents -> _company_w3k_writers_g{gi}.js ({sz} bytes)")
    print(f"\ntotal: {len(jobs)} batches, {len(jobs)*5} profiles, {args.groups} parallel groups")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

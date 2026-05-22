#!/usr/bin/env python3
"""Phase 2 of the no-dup swarm: aggregate proposals into a locked plan.

Reads every scripts/_proposals/*.json, validates and dedups the candidate
slugs against the existing on-disk set AND against each other, then caps the
result to TARGET. The output, scripts/_locked_plan.json, is the authoritative
assignment: every writer agent will be told exactly which files to create,
so no agent ever picks a topic and no duplicate is ever written.

Run AFTER all proposer agents have finished.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SCRIPTS = Path(__file__).resolve().parent
PROPOSALS = SCRIPTS / "_proposals"

TARGET = 1000
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def existing_slugs() -> set[str]:
    return {p.stem for p in CONTENT.rglob("*.md") if not p.stem.startswith("_")}


def main() -> int:
    taken = existing_slugs()
    seen: set[str] = set()
    locked: list[dict] = []
    rejected = {"dup_existing": 0, "dup_proposal": 0, "bad_slug": 0, "missing_field": 0}

    files = sorted(PROPOSALS.glob("*.json"))
    raw = 0
    for f in files:
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"WARN: {f.name} is not valid JSON ({e}); skipping")
            continue
        for it in items:
            raw += 1
            slug = (it.get("slug") or "").strip().lower()
            title = (it.get("title") or "").strip()
            cat = (it.get("category") or "").strip()
            sub = (it.get("subcat") or "").strip()
            if not (slug and title and cat and sub):
                rejected["missing_field"] += 1
                continue
            if not SLUG_RE.match(slug):
                rejected["bad_slug"] += 1
                continue
            if slug in taken:
                rejected["dup_existing"] += 1
                continue
            if slug in seen:
                rejected["dup_proposal"] += 1
                continue
            seen.add(slug)
            locked.append({
                "slug": slug,
                "title": title,
                "category": cat,
                "subcat": sub,
                "dir": f"content/{cat}/{sub}",
                "angle": (it.get("angle") or "").strip(),
            })

    # Interleave by category so a cap doesn't starve later categories.
    from collections import defaultdict, deque
    by_cat: dict[str, deque] = defaultdict(deque)
    for item in locked:
        by_cat[item["category"]].append(item)
    interleaved: list[dict] = []
    cats = deque(by_cat.keys())
    while cats and len(interleaved) < len(locked):
        c = cats[0]
        if by_cat[c]:
            interleaved.append(by_cat[c].popleft())
            cats.rotate(-1)
        else:
            cats.popleft()

    final = interleaved[:TARGET]
    (SCRIPTS / "_locked_plan.json").write_text(json.dumps(final, indent=2), encoding="utf-8")

    print(f"proposal files: {len(files)}")
    print(f"raw candidates: {raw}")
    print(f"rejected: {rejected}")
    print(f"unique valid candidates: {len(locked)}")
    print(f"LOCKED (capped to {TARGET}): {len(final)}")
    if len(final) < TARGET:
        print(f"WARNING: only {len(final)} locked, short of {TARGET}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

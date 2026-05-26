#!/usr/bin/env python3
"""Build the locked plan + per-batch writer prompts for the next company swarm.

Pipeline:
  1. Take the next N SEC companies by prominence not yet on disk.
  2. Assign each a target dir (content/companies/<letter>/), a depth tier
     (by prominence rank), and a writing shape (rotated for variety).
  3. Partition into batches of 5 companies.
  4. Write the cross-link allowlist (every slug that will exist on disk) once,
     and one self-contained prompt per batch the Haiku writer agents read.

Outputs (all gitignored, regenerable):
  scripts/_companies_plan.json        the locked plan (1 row per company)
  scripts/_company_allowlist.txt      every valid cross-link slug
  scripts/_company_batches/bNNN.md    one prompt per 5-company batch

Run from repo root:  python scripts/build_company_batches.py --n 1000
"""
from __future__ import annotations
import argparse, glob, json, os, re

SEC = "scripts/_sec_tickers.json"
COMPANIES = "content/companies"
CONTENT = "content"
PLAN = "scripts/_companies_plan.json"
ALLOW = "scripts/_company_allowlist.txt"
BATCH_DIR = "scripts/_company_batches"
PER_BATCH = 5

SHAPES = [
    "Continuous essay — flowing prose, few or no subheadings, carried by narrative.",
    "Q&A — section headings phrased as the real questions a curious reader asks.",
    "Field notes — crisp, observational, slightly clipped; the analyst's notebook.",
    "Infobox-led — a strong key-facts aside up top, then prose that expands on it.",
    "Pull-quote driven — one memorable framed line, prose built around it.",
    "Segmented — organised around the company's business segments / product lines.",
    "Origin-to-now — chronological, founding through to the present shape of the firm.",
    "Plain-talk — short sentences, zero jargon, explain-to-a-smart-teenager register.",
    "Free choice — pick whatever structure best fits THIS company.",
]


def slugify_ticker(t: str) -> str:
    return re.sub(r"[^a-z0-9-]", "-", t.lower()) + "-stock"


def first_letter(slug: str) -> str:
    c = slug[0]
    return c if c.isalpha() else "0"


def tier_for(rank: int) -> tuple[str, str]:
    """rank is the company's 0-based position in the next-N batch."""
    if rank < 150:
        return ("major", "1,500–2,000 words — a major, storied, or complex firm. Go deep.")
    return ("ordinary", "900–1,300 words — an ordinary operating company. Substantial, not padded.")


def load_sec() -> list[dict]:
    d = json.load(open(SEC, encoding="utf-8"))
    out = []
    for v in d.values():
        t = str(v["ticker"]).strip()
        if t:
            out.append({"ticker": t, "cik": str(v["cik_str"]).zfill(10),
                        "name": v["title"].strip(), "slug": slugify_ticker(t)})
    return out


def existing_slugs() -> set[str]:
    return {os.path.basename(p)[:-3]
            for p in glob.glob(os.path.join(COMPANIES, "*", "*-stock.md"))}


def all_slugs_on_disk() -> list[str]:
    return sorted({os.path.basename(p)[:-3]
                   for p in glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)
                   if not os.path.basename(p).startswith("_")})


def build_plan(n: int) -> list[dict]:
    have, seen, plan = existing_slugs(), set(), []
    for r in load_sec():
        if r["slug"] in have or r["slug"] in seen:
            continue
        seen.add(r["slug"])
        rank = len(plan)
        tier, tier_desc = tier_for(rank)
        letter = first_letter(r["slug"])
        plan.append({**r, "rank": rank,
                     "dir": f"{COMPANIES}/{letter}",
                     "tier": tier, "tier_desc": tier_desc,
                     "shape": SHAPES[rank % len(SHAPES)]})
        if len(plan) >= n:
            break
    return plan


def prompt_for(batch_no: int, rows: list[dict]) -> str:
    assignments = []
    for r in rows:
        assignments.append(
            f"""### {r['name']} ({r['ticker']})
- **File to create:** `{r['dir']}/{r['slug']}.md`
- **SEC CIK:** {r['cik']}
- **Depth:** {r['tier_desc']}
- **Shape to use:** {r['shape']}""")
    assignments_str = "\n\n".join(assignments)
    return f"""You are a financial writer creating evergreen company profiles for the
Pomegra Wiki (a reader-friendly encyclopedia at https://pomegra.io/wiki/).
Write {len(rows)} company profiles — one file each, exactly as assigned below.

# Read first
Open and follow `WIKI_AUTHORING_GUIDE.md` section 9 ("Company entries"). The
company rules are DIFFERENT from concept entries. The exemplar to match for
depth and tone is `content/companies/a/aapl-stock.md` (Apple) — read it before
writing. Match its quality; never copy its headings or sentences.

# Hard rules (deal-breakers — the work is rejected if violated)
1. **No template.** Each of your {len(rows)} profiles must read as if a
   different writer learned that one business and wrote it fresh — distinct
   headings, ordering, and shape. Do NOT reuse boilerplate sentences or carry
   phrasing between companies. Use the assigned shape for each.
2. **Substantial, sized to the company** — hit the assigned word count with
   real substance about the actual business, never padding.
3. **Evergreen + accurate.** No live prices, market cap, P/E, revenue, or
   headcount as hard numbers; no "as of <year>"; scale only qualitatively.
   Write ONLY what is true of the company. Never invent history, products,
   segments, or figures. If unsure of a fact, omit it.
4. **Front matter** exactly:
   ```yaml
   ---
   title: "Company Name (TICKER)"
   description: "150–200 chars, no HTML — what the company is and does."
   keywords:
     - 4 to 8 keywords
   handwritten: true
   ---
   ```
   `handwritten: true` is mandatory (it is the resumability flag).
5. **Never write the literal word "Mermaid"** as visible text; no placeholder /
   "coming soon" / status language; no AI tells ("in this article", "let's
   explore", "I hope this helps"); no engine/tooling names; no investment advice.

# Ingredients (draw from these in a company-specific order — NOT a checklist)
What it is and its sector (early) · origin / history · how it makes money
(segments, what's recurring) · what makes it distinctive (moat, competition) ·
pressures and risks · how a reader would research it (10-K, what to watch).
Arrange however the company and the chosen shape call for.

# Cross-links — DO NOT ADD ANY
Write plain prose with NO markdown links at all. The orchestrator runs
automated linkers afterward that connect every profile to the relevant
concepts and peer companies far more reliably than hand-linking — and
hand-added links to slugs that don't exist break the wiki. So: no `[...](...)`
links anywhere in your output. Just write the company's name and the concepts
in plain text; they get linked automatically.

# Your {len(rows)} assignments — batch {batch_no:03d}

{assignments_str}

# Output
Write each file with the Write tool at the exact path given. Set
`handwritten: true`. Do not stop until all {len(rows)} files exist. End your
reply with the list of file paths you created.
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000)
    args = ap.parse_args()

    plan = build_plan(args.n)
    json.dump(plan, open(PLAN, "w", encoding="utf-8"), indent=2)

    allow = all_slugs_on_disk()
    planned = sorted(r["slug"] for r in plan)
    full = sorted(set(allow) | set(planned))   # include slugs that WILL exist
    open(ALLOW, "w", encoding="utf-8").write("\n".join(full) + "\n")

    os.makedirs(BATCH_DIR, exist_ok=True)
    for old in glob.glob(os.path.join(BATCH_DIR, "*.md")):
        os.remove(old)
    batches = [plan[i:i + PER_BATCH] for i in range(0, len(plan), PER_BATCH)]
    for i, rows in enumerate(batches):
        open(os.path.join(BATCH_DIR, f"b{i:03d}.md"), "w", encoding="utf-8").write(
            prompt_for(i, rows))

    print(f"planned companies: {len(plan)}")
    print(f"batches of {PER_BATCH}: {len(batches)}  -> {BATCH_DIR}/bNNN.md")
    print(f"allowlist slugs:   {len(full)}  -> {ALLOW}")
    print(f"tier split: major={sum(1 for r in plan if r['tier']=='major')}, "
          f"ordinary={sum(1 for r in plan if r['tier']=='ordinary')}")
    print(f"batch 000 covers: " + ", ".join(r['ticker'] for r in batches[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

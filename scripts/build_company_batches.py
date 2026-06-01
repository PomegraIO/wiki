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

# Subagents run with CWD = the parent workspace, not this repo root, so every
# path a writer agent touches (file to create, guide, exemplar) must be
# absolute. REPO_ROOT is derived from this file's location, forward-slashed so
# it reads cleanly inside the generated prompts on any host.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")).replace("\\", "/")
GUIDE_ABS = f"{REPO_ROOT}/WIKI_AUTHORING_GUIDE.md"
EXEMPLAR_ABS = f"{REPO_ROOT}/content/companies/a/aapl-stock.md"

# A per-batch analytical lens. Combined with the per-company SHAPE, this pushes
# framing apart so same-class firms (banks, BDCs, biotech, REITs — the overlap
# trap) don't converge on one template. Assigned round-robin by batch number.
LENSES = [
    "Lead with the customer: who buys from this company and what are they really paying for.",
    "Lead with the unit economics: where a dollar of revenue comes from and what it costs to earn.",
    "Frame it through competition: who it fights, and why it wins or loses those fights.",
    "Frame it through history: the decision or pivot that made it what it is today.",
    "Frame it through risk: the one or two things that could genuinely break this business.",
    "Frame it through the moat (or absence of one): what, if anything, keeps rivals out.",
    "Frame it through capital: how it funds itself and what it does with the cash it makes.",
    "Frame it geographically: where it operates and how place shapes the business.",
    "Frame it through the product line: what it actually makes or sells, concretely.",
    "Frame it through the industry it sits in: the sector's economics, then the firm's place in it.",
    "Frame it through change: what is shifting under this company right now.",
    "Frame it through the regulator: the rules that define the sandbox it plays in.",
    "Frame it through scale: what being big (or small) buys it, or denies it.",
    "Frame it through the supply chain: what it depends on upstream and serves downstream.",
    "Frame it through the founder/operator culture that still drives it.",
    "Frame it through cyclicality: how it behaves across boom and bust.",
]


def lens_for(batch_no: int) -> str:
    return LENSES[batch_no % len(LENSES)]

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
    """rank is the company's 0-based position in the next-N batch.

    This batch sits well past the megacaps (the prominent names are already on
    disk), so there is NO 'go deep to 2,000 words' tier here — that would only
    produce padding on mid- and small-caps. Size strictly to substance.
    """
    if rank < 120:
        return ("notable",
                "~1,100–1,500 words — among the more prominent of the remaining "
                "companies, with a real business to describe. Go reasonably deep, "
                "but only as far as there is genuine substance.")
    return ("sized",
            "Size to the substance, never to a target: ~900–1,300 words for a "
            "genuine operating company; ~500–750 words if it is a dormant shell, "
            "holding company, SPAC, or tiny micro-cap with little real operation. "
            "A thin business honestly has less to say — do not pad it.")


def load_sec(source: str = SEC) -> list[dict]:
    d = json.load(open(source, encoding="utf-8"))
    out = []
    for v in d.values():
        t = str(v["ticker"]).strip()
        if not t:
            continue
        cik_raw = str(v.get("cik_str", "")).strip()
        cik = cik_raw.zfill(10) if cik_raw and cik_raw not in ("0", "0000000000") else ""
        out.append({"ticker": t, "cik": cik,
                    "name": v["title"].strip(), "slug": slugify_ticker(t),
                    "is_etf": bool(v.get("is_etf", False))})
    return out


def existing_slugs() -> set[str]:
    return {os.path.basename(p)[:-3]
            for p in glob.glob(os.path.join(COMPANIES, "*", "*-stock.md"))}


def all_slugs_on_disk() -> list[str]:
    return sorted({os.path.basename(p)[:-3]
                   for p in glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)
                   if not os.path.basename(p).startswith("_")})


ETF_DEPTH = (
    "~500–900 words — profile the FUND, not a company. A broad, flagship or "
    "strategy-defining fund can run longer; a narrow single-stock or "
    "leveraged/inverse product honestly has little to say — keep it tight and "
    "specific to what THIS fund tracks. Never pad, never invent holdings or returns."
)


def build_plan(n: int, source: str = SEC) -> list[dict]:
    have, seen, plan = existing_slugs(), set(), []
    for r in load_sec(source):
        if r["slug"] in have or r["slug"] in seen:
            continue
        seen.add(r["slug"])
        rank = len(plan)
        tier, tier_desc = tier_for(rank)
        if r.get("is_etf"):
            tier, tier_desc = "etf", ETF_DEPTH
        letter = first_letter(r["slug"])
        plan.append({**r, "rank": rank,
                     "dir": f"{REPO_ROOT}/content/companies/{letter}",
                     "tier": tier, "tier_desc": tier_desc,
                     "shape": SHAPES[rank % len(SHAPES)]})
        if len(plan) >= n:
            break
    return plan


def prompt_for(batch_no: int, rows: list[dict]) -> str:
    assignments = []
    for r in rows:
        kind = ("Exchange-traded product (ETF/ETN) — profile it as a FUND, not an "
                "operating company") if r.get("is_etf") else "Operating company"
        cik_line = f"\n- **SEC CIK:** {r['cik']}" if r.get("cik") else ""
        assignments.append(
            f"""### {r['name']} ({r['ticker']})
- **File to create:** `{r['dir']}/{r['slug']}.md`
- **Type:** {kind}{cik_line}
- **Depth:** {r['tier_desc']}
- **Shape to use:** {r['shape']}""")
    assignments_str = "\n\n".join(assignments)
    has_etf = any(r.get("is_etf") for r in rows)
    etf_block = (
        "\n\n# Fund ingredients (for any assignment marked ETF/ETN — NOT the company set)\n"
        "What the fund is and what it tracks or holds (the index, theme, sector, or "
        "single underlying) · its objective and strategy · the issuer/sponsor and "
        "structure (plain ETF vs leveraged/inverse/ETN, and the daily-reset mechanics "
        "if leveraged) · costs and how it trades (expense ratio qualitatively, liquidity) "
        "· the real risks (tracking error, volatility decay for leveraged/inverse, "
        "concentration) · who it is for and how a reader would research it (the "
        "prospectus/fact sheet, the underlying index). Do NOT write about 'segments', "
        "'how it makes money', or a 10-K — a fund has none of those."
    ) if has_etf else ""
    return f"""You are a financial writer creating evergreen company profiles for the
Pomegra Wiki (a reader-friendly encyclopedia at https://pomegra.io/wiki/).
Write {len(rows)} company profiles — one file each, exactly as assigned below.

# Read first (both files, by absolute path)
1. `{GUIDE_ABS}` — section 9 ("Company entries"). The company rules are
   DIFFERENT from concept entries. Read §9 before writing.
2. `{EXEMPLAR_ABS}` (Apple) — the exemplar to match for depth and tone. Match
   its quality; never copy its headings or sentences.

# Framing lens for this batch
{lens_for(batch_no)}
Apply this lens as your DEFAULT angle of approach, but bend it to each company —
it is a starting vantage point, not a heading to copy. It exists so your five
profiles, and this batch versus the others, do not converge on one shape.

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
Arrange however the company and the chosen shape call for.{etf_block}

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
    ap.add_argument("--source", default=SEC,
                    help="ticker universe JSON (default company_tickers; "
                         "use _sec_tickers_expanded.json for the ETF wave)")
    ap.add_argument("--batch-dir", default=BATCH_DIR,
                    help="output dir for bNNN.md prompts (use a SEPARATE dir to "
                         "run a wave alongside another without clobbering it)")
    ap.add_argument("--plan", default=PLAN)
    ap.add_argument("--allow", default=ALLOW)
    args = ap.parse_args()

    batch_dir = args.batch_dir

    plan = build_plan(args.n, args.source)
    json.dump(plan, open(args.plan, "w", encoding="utf-8"), indent=2)

    allow = all_slugs_on_disk()
    planned = sorted(r["slug"] for r in plan)
    full = sorted(set(allow) | set(planned))   # include slugs that WILL exist
    open(args.allow, "w", encoding="utf-8").write("\n".join(full) + "\n")

    os.makedirs(batch_dir, exist_ok=True)
    for old in glob.glob(os.path.join(batch_dir, "*.md")):
        os.remove(old)
    batches = [plan[i:i + PER_BATCH] for i in range(0, len(plan), PER_BATCH)]
    for i, rows in enumerate(batches):
        open(os.path.join(batch_dir, f"b{i:03d}.md"), "w", encoding="utf-8").write(
            prompt_for(i, rows))

    print(f"planned companies: {len(plan)}")
    print(f"batches of {PER_BATCH}: {len(batches)}  -> {batch_dir}/bNNN.md")
    print(f"allowlist slugs:   {len(full)}  -> {args.allow}")
    from collections import Counter
    print(f"tier split: {dict(Counter(r['tier'] for r in plan))}")
    print(f"batch 000 covers: " + ", ".join(r['ticker'] for r in batches[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Wave-3k planning: build proposer briefs for 3,000 new concept entries.

Outputs (all under scripts/):
  _wave3k_existing.txt        every slug already on disk (concept + company) — global dedup set
  _wave3k_core_allowlist.txt  top-N most-linked concept slugs — the safe cross-link vocabulary for writers
  _wave3k_briefs.json         one proposer brief per (category, subcat): quota + existing slugs in that bucket

A proposer agent reads one brief and returns up-to-`quota` genuinely-distinct,
established finance concepts that are NOT already in `existing_slugs`. We
over-ask (sum of quotas > 3000) so the global dedup + trim has headroom.
"""
from __future__ import annotations
import json, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SD = Path(__file__).resolve().parent

CORE_N = 320            # size of the writer cross-link allowlist
TARGET_TOTAL = 3000

# Human-readable one-liners per category to orient the proposer.
CAT_DESC = {
    "equity": "shares and everything that happens to them — share classes, corporate actions, employee equity, offerings, depositary receipts, shareholder rights",
    "derivatives": "options, futures, forwards, swaps — their types, pricing models, the Greeks, and strategies",
    "fixed-income": "bonds and credit — government, corporate, municipal, structured credit, money-market, bond math, the yield curve",
    "funds": "pooled vehicles — ETFs, mutual funds, hedge funds, private equity, specialty funds and their economics",
    "forex": "currencies — pairs, regimes, FX derivatives, market mechanics, reserve currencies, intervention",
    "commodities": "physical markets — metals, energy, agriculture, livestock, the futures curve and commodity vehicles",
    "macro": "the macroeconomy — output, prices, labour, the business cycle, trade/balance of payments, growth theory",
    "monetary": "central banking — institutions, policy tools, the money supply, interest rates, frameworks",
    "fiscal": "government finance — budgets, debt, taxation policy, transfer programmes, multipliers, sovereign default",
    "ratios": "financial ratios — valuation, profitability, liquidity, solvency/leverage, efficiency, market risk",
    "accounting": "financial reporting — the statements, balance-sheet items, revenue recognition, cost allocation, standards/audit",
    "strategies": "investing styles — value, growth/momentum, factor, portfolio construction, rebalancing, quant, trading styles, rotation",
    "risk": "risk and its management — risk types, measurement, hedging, position management, regulatory capital",
    "behavioral": "behavioural finance — cognitive biases, loss aversion, herding, mental accounting, sentiment, market anomalies",
    "history": "financial history — crises, bubbles, structural shifts, famous trades, regulatory milestones",
    "people": "the people of finance — legendary investors, traders, economists, modern thinkers, activists and quants",
    "regulation": "rules and regulators — securities laws, regulators, market rules, AML/KYC, international regimes, compliance",
    "corporate": "corporate finance and control — M&A, takeover defences, LBOs, governance, capital policy, activism",
    "personal-finance": "household money — retirement accounts, savings, budgeting, credit/debt, insurance, homeownership, estate planning",
    "taxes": "investment taxation — capital gains, retirement tax, vehicle tax treatment, real-estate tax, estate/gift, AMT, the forms",
    "real-estate": "property — residential, commercial, mortgages, REITs, financing/investing metrics, operations",
    "trading": "market microstructure — order types, execution, structure, settlement/clearing, intraday phenomena, costs",
    "crypto": "digital assets — major chains, consensus, tokens/instruments, DeFi, custody/trading, scaling tech, tax/reg",
    "technical-analysis": "chart reading — candlesticks, chart patterns, support/resistance, trend and momentum indicators, volume, breadth",
    "institutions": "the plumbing — exchanges, index providers, rating agencies, clearinghouses, major firms, regulators",
    "valuation": "what a business is worth — DCF, multiples, residual income, dividend models, real options, private-company methods",
    "markets": "markets as systems — primary vs secondary, venues, market types, indices, mechanics, global markets",
}


def all_disk_slugs() -> set[str]:
    slugs = set()
    for p in CONTENT.rglob("*.md"):
        if p.name == "_index.md":
            continue
        slugs.add(p.stem)
    return slugs


def concept_slugs_by_subcat() -> dict[tuple[str, str], list[str]]:
    out: dict[tuple[str, str], list[str]] = {}
    for cat in TAXONOMY:
        for subcat, _t, _kw in TAXONOMY[cat]:
            d = CONTENT / cat / subcat
            out[(cat, subcat)] = sorted(p.stem for p in d.glob("*.md")) if d.is_dir() else []
    return out


def core_allowlist(all_slugs: set[str]) -> list[str]:
    """Top-N most-linked-to *concept* slugs — the high-utility hub vocabulary."""
    company = {p.stem for p in (CONTENT / "companies").rglob("*.md")}
    concept = all_slugs - company
    link_rx = re.compile(r'(?:\]\(|href=["\'])/([a-z0-9][a-z0-9-]*)/')
    counts: Counter[str] = Counter()
    for p in CONTENT.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in link_rx.finditer(txt):
            s = m.group(1)
            if s in concept:
                counts[s] += 1
    top = [s for s, _ in counts.most_common(CORE_N)]
    return sorted(top)


def quota_for(target: int) -> int:
    return min(28, max(8, round(target * 1.4)))


def main() -> int:
    all_slugs = all_disk_slugs()
    (SD / "_wave3k_existing.txt").write_text("\n".join(sorted(all_slugs)), encoding="utf-8")

    core = core_allowlist(all_slugs)
    (SD / "_wave3k_core_allowlist.txt").write_text("\n".join(core), encoding="utf-8")

    by_sub = concept_slugs_by_subcat()
    briefs = []
    bid = 0
    total_quota = 0
    for cat in TAXONOMY:
        for subcat, target, _kw in TAXONOMY[cat]:
            q = quota_for(target)
            total_quota += q
            briefs.append({
                "id": f"b{bid:03d}",
                "category": cat,
                "subcat": subcat,
                "cat_desc": CAT_DESC.get(cat, cat),
                "dir": f"content/{cat}/{subcat}",
                "quota": q,
                "existing_slugs": by_sub[(cat, subcat)],
            })
            bid += 1

    (SD / "_wave3k_briefs.json").write_text(json.dumps(briefs, indent=1), encoding="utf-8")
    print(f"disk slugs (global dedup set): {len(all_slugs)}")
    print(f"core allowlist: {len(core)} hub slugs")
    print(f"proposer briefs: {len(briefs)} (one per subcat)")
    print(f"sum of quotas (over-ask): {total_quota}  (target unique {TARGET_TOTAL})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

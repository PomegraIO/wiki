---
title: "Active Share: Measuring True Fund Activeness"
description: "Active share quantifies what percent of a fund's portfolio differs from its benchmark. A high active share is necessary but not sufficient for outperformance."
keywords:
  - active share fund metric
  - fund portfolio tracking error
  - active management performance metric
  - benchmark deviation measurement
  - fund activeness calculation
image: /svg/funds.svg
---

*The **active share** metric measures what percentage of a [mutual fund's](/mutual-fund/) or [ETF's](/etf/) holdings differ from its stated [benchmark](/actively-managed-fund/). A fund claiming to be actively managed but sitting 95% identical to its index is not truly active—it is a [closet indexer](/actively-managed-fund/). Active share separates real active managers from beta-heavy funds charging active fees for passive exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Active Share — Key Facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Active share measures true portfolio divergence from a benchmark.</div>

|   |   |
|---|---|
| **Formula** | 0.5 × Σ \|weight in fund - weight in benchmark\| |
| **Range** | 0 (exact index) to 1.0 (completely different) |
| **Typical passive** | 0–3% |
| **Closet indexing** | 20–40% |
| **Truly active** | 60%+ |
| **Outperformance link** | Necessary, not sufficient |

</aside>

## Definition and Calculation

Active share is a simple measure of how different a fund's holdings are from its benchmark index. It is calculated as half the sum of the absolute differences in weight for every holding:

$$\text{Active Share} = 0.5 \times \sum_{i=1}^{n} |\text{weight}_{\text{fund},i} - \text{weight}_{\text{benchmark},i}|$$

Example: Suppose a fund and its benchmark both hold 10 stocks. The fund holds:

| Stock | Fund Weight | Benchmark Weight | Absolute Difference |
|---|---|---|---|
| A | 15% | 10% | 5% |
| B | 12% | 12% | 0% |
| C | 10% | 15% | 5% |
| D | 8% | 8% | 0% |
| E | 7% | 10% | 3% |
| F | 6% | 10% | 4% |
| G | 10% | 8% | 2% |
| H | 9% | 10% | 1% |
| I | 12% | 10% | 2% |
| J | 11% | 7% | 4% |
| **Total** | 100% | 100% | 26% |

Active Share = 0.5 × 26% = **13%**

This fund has a low active share. It is overweighting some stocks (A, G, I, J) and underweighting others (C, E, F), but the net divergence is small. The fund still looks much like the benchmark.

## The Spectrum: Passive to Truly Active

**Passive and index funds** have active shares near 0–3%. They are designed to track the benchmark, so holdings and weights match almost exactly.

**Closet indexers** are the problem. A fund claims to actively manage but holds 60–80% of its portfolio in benchmark stocks at near-benchmark weights, with only small bets on a handful of others. Active share typically runs 20–40%. The manager is taking on [tracking error](/active-etf/) and [volatility](/historical-volatility/) without betting meaningfully different from the index, so they underperform after fees while marketing themselves as active.

**Truly active funds** have active shares of 60%+. They may hold 40% of stocks in the benchmark but at radically different weights, plus 60% in holdings outside the benchmark entirely. Or they may hold mostly benchmark stocks but weight them very differently. Either way, the portfolio is genuinely distinct.

Some specialized or [concentrated portfolios](/concentration-risk/) exceed 90% active share—they are barely correlated to their stated benchmark at all.

## Why Active Share Matters

Active share is a necessary but insufficient condition for outperformance. A fund with 80% active share is *doing something* differently. Whether that something adds value depends on skill, market conditions, and fees.

The relationship is empirical. Research by Petajisto and others has found:

- **High active share + low fees**: Higher odds of outperformance
- **High active share + high fees**: Odds favor underperformance (the active bets don't cover the fee drag)
- **Low active share + any fees**: Almost always underperforms (passive exposure with active fees)

A fund with 15% active share and a 0.50% [expense ratio](/expense-ratio/) is charging active fees to deliver passive-like returns. It will almost certainly lag its benchmark over time.

A fund with 75% active share and a 0.70% expense ratio has a shot—the active positions might generate alpha. But there is no guarantee.

## Active Share vs. Alpha

Active share measures *divergence*, not *quality of divergence*. A manager with 70% active share could be picking winners or picking losers. Active share just tells you the manager is trying something different.

[Alpha](/alpha/) is the excess return the manager actually delivers beyond the benchmark. A low-active-share fund will rarely generate positive alpha because it is tethered to the index. A high-active-share fund *could* generate alpha—but often does not.

Some of the best performers have moderate active share (40–60%) in concentrated thematic or value strategies. Some of the worst have very high active share but make expensive mistakes. The number alone does not predict success.

## Closet Indexing and Fee Transparency

Active share revealed widespread closet indexing in the 2000s and 2010s. Funds were charging 1.0–1.5% annual fees while holding portfolios that diverged from their benchmark by only 25–35%. Once passive [index funds](/index-fund/) and [ETFs](/etf/) offered the same exposure at 0.05–0.20%, investors had no reason to pay for the illusion of active management.

This transparency has pushed the industry in two directions:

1. **Genuine active funds** have sharpened their bets and accepted higher active share to justify fees.
2. **Closet indexers** have either closed or rebranded as lower-cost core holdings, accepting that they are pseudo-passive.

Active share is now a screening tool for investors. Before paying a 0.75% active [management fee](/management-fee/), check the active share. Below 40%, you are overpaying. Above 70%, the manager is taking meaningful bets.

## Limitations of Active Share

Active share has blind spots:

**Volatility asymmetry**: A fund could be +5% overweight in 10 stocks and -5% underweight in 10 others, generating a 50% active share. But if the over- and underweighted stocks move together, the portfolio will track the benchmark closely and deliver little independent return.

**Market cap distortion**: A fund equal-weighting small-cap stocks while the benchmark is [market-capitalization-weighted](/market-capitalization/) will have high active share but similar systematic risk and return drivers.

**Sector vs. stock selection**: A fund might have low active share in stock selection within a sector but massive bets on sector rotation. Active share misses this dimension.

**Execution quality**: High active share without skill is just high volatility and underperformance. Skill matters more than the number.

## See also

<div class="wiki-seealso">

### Closely related

- [Actively managed fund](/actively-managed-fund/) — the category active share measures
- [Index fund](/index-fund/) — the benchmark alternative
- [Expense ratio](/expense-ratio/) — the cost that determines whether active beats passive
- [Alpha](/alpha/) — the excess return active managers should deliver
- [Tracking error](/active-etf/) — the volatility of divergence from benchmark

### Wider context

- [Mutual fund](/mutual-fund/) — the broader fund universe
- [ETF](/etf/) — another fund structure where active share applies
- [Sharpe ratio](/sharpe-ratio/) — risk-adjusted return comparison
- [Market capitalization](/market-capitalization/) — how benchmarks weight holdings

</div>

---
title: "How the Momentum Factor Is Calculated"
description: "Explains how the momentum factor is calculated: the standard 12-1 month lookback window, skip-month convention, and why these choices matter."
keywords:
  - momentum factor calculation
  - how momentum is calculated
  - 12-1 month momentum
  - factor investing momentum
  - momentum lookback window
  - skip-month momentum
---

*The **momentum factor** is calculated by ranking stocks on their past returns over a fixed lookback period—typically the most recent 12 months, excluding the most recent month (the "12-1" convention). Stocks with the highest returns form a long portfolio; those with the worst returns form a short portfolio. The factor return is the difference between these two [portfolios](/index-fund/), capturing the excess return from betting on "winners" versus "losers." The skip-month convention and the 12-month window are not arbitrary; they reflect decades of academic research on which choices yield the most consistent [risk-adjusted](/sharpe-ratio/) returns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Momentum Factor — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for investment strategies." />

<div class="wiki-infobox-caption">The momentum factor's calculation method—the lookback window and skip-month rule—directly drives its realized performance.</div>

|   |   |
|---|---|
| **Standard formula** | Return over months 2–13 (skip month 1) |
| **Typical holding period** | 1 month (rebalance monthly) |
| **Ranking rule** | Long the top quintile or decile; short the bottom |
| **Transaction costs** | Higher than [passive indexing](/index-fund/); turnover ~20–40% monthly |
| **Historical [alpha](/alpha/)** | ~0.4–0.7% per month (before costs), declining over time |
| **Sector exposure** | Not pure factor; captures [value](/value-investing/), [small-cap](/sp-500-index/), and growth tilts |

</aside>

## The 12-1 Month Lookback

The canonical **momentum factor** looks at stock returns from month 2 through month 13 of the past year, skipping the most recent month (month 1). So if today is June 15, 2025, a portfolio constructed today ranks stocks on returns from May 2024 through April 2025, excluding May 2025.

Why 12 months? Early research by Jegadeesh and Titman (1993) found that a 12-month lookback captured the strongest momentum effect—stocks that outperformed over the prior year tended to outperform the next month. Shorter windows (3 or 6 months) also worked but were noisier. Longer windows (24+ months) weakened the signal, because very old returns mattered less than recent ones.

Why skip the most recent month? Empirically, the month immediately after a large move often reverses. This is called **short-term reversal** and is driven by transaction costs, bid-ask bounce, and other microstructure frictions. By skipping month 1, the momentum factor avoids this noise and captures the "true" trend that persists into the next month.

### Worked Example

Consider three stocks over the past 13 months (with month 13 being the oldest):

| Month | Stock A | Stock B | Stock C |
|-------|---------|---------|---------|
| 13–2 (12 months ago to 2 months ago) | +120% cumulative | −20% cumulative | +80% cumulative |
| 1 (most recent) | −5% | +10% | +2% |
| **12-1 return** | **+120%** | **−20%** | **+80%** |

All three stocks had different performance in the most recent month, but when ranking on the 12-1 return, Stock A leads (+120%), then Stock C (+80%), then Stock B (−20%). A momentum portfolio long Stock A and short Stock B would have ranked them correctly despite the recent month's noise.

## Rebalancing Frequency and Turnover

The standard momentum factor is rebalanced every month. On the first trading day of each month, you re-rank all stocks by their 12-1 return, liquidate the old portfolio, and build a new one. This high turnover—typically 20–40% of the portfolio per month—introduces [transaction costs](/interest-coverage-ratio/) that eat into returns.

Some practitioners use quarterly or semi-annual rebalancing to reduce turnover. But academic studies show that monthly rebalancing is where the momentum signal is strongest; the farther you stretch the holding period, the weaker the effect. This is a key difference between momentum and, say, [value investing](/value-investing/), where the signal is durable over longer horizons.

## Long-Short Construction and Quintiles

In a typical academic study, the momentum factor is constructed as a **quintile spread**: rank all stocks by their 12-1 return and divide them into five groups (quintiles). The long leg holds the top 20% (highest past returns); the short leg holds the bottom 20% (lowest past returns). The factor return is (long portfolio return) − (short portfolio return).

In a decile spread, you divide into ten groups and use the top and bottom 10%. Decile spreads are more extreme and capture stronger momentum, but they are also more volatile and harder to implement in practice (buying tiny amounts of each stock).

Practitioners deploying momentum as an [actively managed fund](/actively-managed-fund/) might use a gentler approach: buy the top quintile and hold it in a long-only [portfolio](/index-fund/), avoiding the short-selling costs and regulatory friction of the short leg. The trade-off is that you capture less of the momentum factor's return, but you also reduce [turnover](/index-fund/) and simplify implementation.

## Why These Choices Matter: Empirical Evidence

Academic research has documented that small tweaks to the momentum formula produce large performance swings:

- **14-month vs. 12-month window**: The 14-month window (skipping the same past month) actually works better in some markets and time periods, but the 12-month window is the standard.
- **Skip-month vs. no skip**: Removing the skip-month rule can cut momentum's average return in half, because the short-term reversal signal is so strong.
- **Holding period**: A 1-month holding period maximizes the momentum factor's return; a 6-month holding period yields weaker returns.
- **Rebalancing frequency**: Weekly or daily rebalancing introduces too much noise; monthly is the sweet spot.

These empirical regularities are **not** universal across markets and time periods. Momentum is strongest in large-cap, high-liquidity stocks, and weaker in small-caps. It works better in trending markets and breaks down during crises when correlations spike.

## Practical Implementation: ETFs and Funds

Momentum [factors](/factor-investing/) are available through [ETFs](/etf/) and [actively managed funds](/actively-managed-fund/). Many implement the 12-1 rule, but some use variants like 11-1 (skip two months) or 6-1 (shorter lookback). Transaction costs are real; a momentum [ETF](/etf/) might underperform the published factor return by 0.2–0.4% per year because of [bid-ask spreads](/bid-ask-spread/), fund fees, and cash drag.

Investors considering a momentum [factor](/factor-investing/) bet should understand that the returns published in academic papers are "clean" returns—they do not account for the difficulty of actually short-selling in many markets, nor the slippage from rebalancing. Real-world momentum returns are smaller, but momentum remains one of the most robust [factors](/factor-investing/) in financial markets.

## See also

<div class="wiki-seealso">

### Closely related

- [Factor Investing](/factor-investing/) — the broader framework for systematic [factor](/factor-investing/) strategies
- [Value Investing](/value-investing/) — another popular [factor](/factor-investing/); longer-lived than momentum
- [Alpha](/alpha/) — the excess return the momentum [factor](/factor-investing/) seeks to capture
- [Sharpe Ratio](/sharpe-ratio/) — how to measure [factor](/factor-investing/) [risk](/market-risk/)-adjusted returns
- [Trend Following](/trend-following/) — related strategy using longer-term price trends

### Wider context

- [Active ETF](/active-etf/) — how momentum is deployed in tradeable funds
- [Index Fund](/index-fund/) — passive alternative; low [turnover](/index-fund/) but no momentum [alpha](/alpha/)
- [Diversification](/diversification/) — why momentum [factors](/factor-investing/) work in a balanced [portfolio](/index-fund/)
- [Market Cycle](/market-cycle/) — momentum can break down in certain market regimes

</div>

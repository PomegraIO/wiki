---
title: "Volume-Weighted Average Price"
description: "An intraday benchmark price reflecting the average price paid across all shares traded, weighted by transaction volume."
keywords:
  - VWAP
  - volume-weighted average price
  - execution benchmark
  - intraday metric
  - trading performance
  - order execution
image: /svg/technical-analysis.svg
---

*The **Volume-Weighted Average Price** (VWAP) is the average price at which a stock trades throughout a single trading day, weighted by the volume transacted at each price level. It serves as a neutral intraday benchmark for execution quality: if a trader buys below VWAP, they've done well; if they sell above it, similarly. VWAP anchors institutional trading algorithms and passive performance assessment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VWAP — the benchmark</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis and metrics." />

<div class="wiki-infobox-caption">The fair midpoint price for a day's trading.</div>

|   |   |
|---|---|
| **What it is** | Sum of (price × volume) divided by total volume, calculated continuously intraday |
| **Formula** | VWAP = Σ(price × volume) / Σ(volume) |
| **Time frame** | Single trading day (resets daily) |
| **Use case** | Execution quality assessment, algorithmic trading reference |
| **Also called** | VWAP benchmark, volume-weighted price |
| **Key advantage** | Objective, volume-grounded, independent of trader intent |

</aside>

## Why volume-weighting matters

Imagine a stock trades at £100 on a single share, then £101 on 10 million shares. The simple arithmetic mean is £100.50, but that misrepresents the market. Ten million shares changed hands at £101; one share at £100. If you were a buyer that day, you paid closer to £101 on average. VWAP captures that reality by weighting each price by the volume transacted, yielding a volume-adjusted average.

This distinction is not academic. Institutional investors managing billions daily cannot ignore execution costs. They deploy [algorithmic-trading](/algorithmic-trading/) systems and manual traders to minimize slippage—the difference between the benchmark price and the actual executed price. VWAP is the benchmark of choice because it is objective, observable in real-time, and purely mechanical. It removes negotiation and subjectivity from execution reporting.

## The calculation: continuous and incremental

VWAP is calculated tick-by-tick (or bar-by-bar) as:

$$\text{VWAP} = \frac{\sum (\text{Price}_i \times \text{Volume}_i)}{\sum \text{Volume}_i}$$

In practice, a trader or algorithm maintains a running tally. Suppose in the first hour of trading, the stock trades at £100 on 500,000 shares and £101 on 300,000 shares. The cumulative numerator is (100 × 500,000) + (101 × 300,000) = 80,300,000. The cumulative denominator is 800,000. Early VWAP is 80,300,000 / 800,000 ≈ £100.375.

As more trades execute throughout the day, the numerator and denominator both grow. A large block trade at a high price (say, 1 million shares at £102) shifts VWAP up. A series of small retail sales at £99 pull it down. The final VWAP at market close is the true volume-weighted average for the entire session.

## VWAP as an algorithmic trading anchor

Most large asset managers and brokers run execution algorithms designed to beat VWAP. A "VWAP algo" receives a big order (sell 5 million shares of Apple stock throughout the day) and slices it into smaller tranches, timing them to execute near VWAP rather than in one lump, which would crater the price.

The appeal is straightforward. If you can execute a large sale at prices near or above VWAP, you've beaten the average and generated alpha. Conversely, if your execution price is significantly below VWAP (for a sale) or above VWAP (for a buy), you've underperformed the benchmark and triggered scrutiny from the asset owner.

This is why VWAP is sometimes called the "fair price" for the day. It is not a prediction of where the stock "should" trade, but rather an objective summary of what actually traded and at what prices. It is the null hypothesis against which execution quality is measured.

## VWAP versus time-weighted average price

A related but distinct benchmark is the time-weighted average price (TWAP), which treats each minute (or other time unit) equally, regardless of volume. If a stock trades at £100 in minute 1 (on 100 shares) and £102 in minute 2 (on 1 million shares), TWAP is simply (100 + 102) / 2 = £101. VWAP, in contrast, is heavily skewed toward the £102 minute because that is where the volume happened: (100 × 100 + 102 × 1,000,000) / (100 + 1,000,000) ≈ £101.998.

TWAP is useful when the goal is to mimic passive execution spread evenly across the day, independent of where volume clusters. VWAP is useful when the goal is to match the actual volume-weighted midpoint. For most institutional traders, VWAP is the tougher benchmark to beat and therefore the more credible one.

## VWAP in retail and technical trading

Beyond institutional execution, some retail traders use VWAP as a technical indicator on intraday charts. A stock climbing above its VWAP is viewed as bullish (more aggressive buying above the day's fair price), while price falling below VWAP is viewed as bearish. Some traders use VWAP as an intraday support or resistance level, buying near VWAP on pullbacks in an uptrend or shorting near VWAP on pullbacks in a downtrend.

The efficacy of VWAP as a predictive trading signal is mixed. In choppy markets with no directional trend, VWAP acts like a magnet for mean-reversion trades. In strong trending markets, price often remains well above or below VWAP for hours, and mean-reversion trades fail. Retail traders should treat VWAP as one input among many—useful for execution measurement, suggestive but not conclusive for direction.

## Limitations and considerations

**VWAP is backward-looking.** It summarizes what has already happened. It does not predict where the stock will trade after market close or the next day. Using VWAP as a predictive technical signal requires the assumption that traders will continue to trade around the same price zone, which is fragile.

**VWAP assumes fair market conditions.** In gapped opens (stock opens at £105 after closing at £100), VWAP can be skewed if most volume comes early. Similarly, extreme intraday gaps (a mid-session news announcement that moves the stock 5%) create two distinct VWAP regimes. A trader executing across such an event will find VWAP less meaningful.

**Data sources vary.** VWAP calculated from [consolidated tape](/consolidated-tape/) (the official exchange volume) differs from VWAP calculated including [dark pools](/dark-pools/) and [after-hours trading](/after-hours-trading/). An off-exchange trade of 100,000 shares does not appear in the official VWAP feed, yet it still occurred and at a price. Institutional traders managing VWAP tightly must decide whether to include or exclude off-exchange volume.

**VWAP is intraday only.** Once the market closes, the final VWAP for the day is fixed. It does not roll forward to the next day. Traders planning to execute over multiple days must use cumulative algorithms or other methods; VWAP is not suitable for multi-day benchmarks.

## Practical use in execution management

A large asset manager selling a £100 million stake over a week will typically split it into daily tranches and measure each day's execution against that day's VWAP. If the manager can sell at an average of 0.5% above VWAP across the week, the execution is rated as high quality. Brokers compete on VWAP outperformance; algorithms are tuned and backtested to beat it.

For traders using passive algorithms (those designed to minimise market impact rather than maximise price), beating VWAP is the baseline expectation, not an ambitious target. The skill is in sizing and timing tranches so that the algo's final execution price stays within 1–2 basis points of VWAP. Deviation beyond that signals slippage or poor execution and invites scrutiny.

## See also

<div class="wiki-seealso">

### Closely related

- [On-balance volume](/on-balance-volume/) — cumulative volume flow indicator
- Volume — the component underlying VWAP
- Execution quality — what VWAP measures
- [Algorithmic trading](/algorithmic-trading/) — the primary use case for VWAP
- [Bid-ask spread](/bid-ask-spread/) — closely related to execution costs around VWAP
- Time-weighted average price — an alternative intraday benchmark

### Wider context

- Trading — the broader context for execution measurement
- Market impact — the cost that VWAP-based execution aims to minimise
- Technical analysis — VWAP as an intraday chart tool

</div>

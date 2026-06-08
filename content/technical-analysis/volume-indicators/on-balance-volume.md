---
title: "On-Balance Volume"
description: "A cumulative volume indicator that adds or subtracts daily volume based on price direction, confirming trend strength or divergence."
keywords:
  - on-balance volume
  - OBV
  - volume indicator
  - price confirmation
  - trend strength
  - technical analysis
image: /svg/technical-analysis.svg
---

*The **On-Balance Volume** (OBV) indicator, created by Joseph Granville in 1963, treats volume as a running tally that climbs when price closes higher and falls when price closes lower. It rests on a simple premise: if professional accumulation or distribution is driving a price move, volume should flow in the same direction. Divergence between price and OBV often precedes reversals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">On-Balance Volume — the mechanics</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis and charting." />

<div class="wiki-infobox-caption">Cumulative volume weighted by direction.</div>

|   |   |
|---|---|
| **What it is** | A running sum of volume, added on up-days, subtracted on down-days |
| **Formula** | If close > prior close: OBV = prior OBV + volume; else OBV = prior OBV − volume |
| **Range** | Unbounded; starts at 0 or an arbitrary baseline |
| **Best used with** | Price charts; lookback periods vary (no fixed cycle) |
| **Signal type** | Confirmation, divergence detection |
| **Invented** | 1963 by Joseph Granville |

</aside>

## The logic: volume confirms intention

Granville's insight was deceptively straightforward. A stock rallying from £50 to £55 on 100 shares of volume looks different from the same price move on 10 million shares. The 100-share rally could be a random tick; the 10-million-share rally suggests deliberate institutional buying. OBV codifies this intuition: volume is a meter of market intention, and if a price trend lacks volume support, it is fragile.

When a stock rises and OBV rises with it, the trend has conviction. Buyers are stepping in aggressively. When a stock falls and OBV falls with it, sellers are in control. But when a stock rises and OBV stalls or falls—a divergence—the rally lacks sponsorship and often reverses. This is the core signal OBV generates.

## The calculation: running cumulative volume

OBV is one of the simplest indicators to compute:

1. Start with an arbitrary baseline (often zero, sometimes the prior day's OBV).
2. Each day, compare the close to the previous close.
3. If today's close > yesterday's close: add today's volume to the running total.
4. If today's close < yesterday's close: subtract today's volume from the running total.
5. If today's close = yesterday's close: the OBV remains unchanged.

Over weeks or months, OBV accumulates into a trend line. A rising OBV trend suggests sustained buying pressure; a falling OBV suggests distribution and selling.

The result is not a bounded oscillator like relative-strength-index (which ranges 0–100) or [stochastic-oscillator](/stochastic-oscillator/) (which also ranges 0–100). OBV is unbounded and paths-dependent, making it less suitable for overbought/oversold levels and more suitable for trend confirmation and divergence spotting.

## Practical interpretation: three core signals

**Trend Confirmation.** When price and OBV rise together over weeks, the uptrend is backed by volume. It is healthy. A technician gains confidence that institutions are accumulating, not retail speculation. Conversely, rising price with falling or flat OBV is a red flag—the rally is built on thin air and likely to fail.

**Divergence.** The most actionable OBV signal is a divergence: price makes a new high, but OBV fails to confirm it (makes a lower high than it did at the prior price peak). This suggests that even though the stock is hitting new highs, the number of shares changing hands is declining. Buyers are running out of ammunition. Many traders interpret a price-OBV divergence as a sell signal, particularly in uptrends, as it often precedes a pullback or reversal.

**Support and Resistance.** Some technicians draw horizontal lines on OBV (similar to price support/resistance) and trade around those levels. If OBV has repeatedly bounced off a level (say, a running total of 50 million), a breach of that level can signal a shift in intermediate direction—more aggressive selling or, conversely, accumulation breaking through historic distribution levels.

## Why OBV is less predictive than its reputation suggests

OBV enjoyed a surge of popularity in the 1970s and remains widely cited by retail traders and newsletters. But academic research has been mixed. Studies find that OBV as a standalone predictor of next-period returns is weak. A divergence observed on a chart yesterday does not reliably predict a reversal in the next 5–10 days. Volume is often noisy—a 20% spike in volume one day may reflect headline risk, index rebalancing, or options expiration rather than a deep shift in supply and demand.

Additionally, OBV is sensitive to data quality and corporate actions. A stock split doubles the volume denominator; a merger or spinoff can distort historical volume. Charting services often adjust historical volumes for splits, but errors persist. A trader comparing OBV across a split point can be misled.

## OBV in modern markets

Electronic trading and retail participation have complicated OBV's interpretation. In the 1960s, Granville's era, large institutional trades moved the [market-maker-trading](/market-maker-trading/) and signalled real accumulation. Today, algorithmic trading and high-frequency trading execute large orders in small tranches, disguising real institutional intent. A 500,000-share sell order might be chopped into 5,000-share micro-orders across a second, obscuring the true direction of pressure. OBV still registers volume, but the signal quality is degraded.

Moreover, [after-hours-trading](/after-hours-trading/) and dark pools route millions of shares outside the consolidated tape, creating blind spots in what OBV can see. A technician using only official market volume is missing a significant portion of true trading intent.

## Practical application: a blended approach

Experienced technicians rarely rely on OBV in isolation. Instead, they combine it with:

- **Price momentum indicators** like the moving-average-convergence-divergence (MACD) to identify momentum weakness alongside volume weakness.
- **Order flow analysis** (where available) to gauge the aggressiveness of bids versus asks, which OBV cannot capture.
- **Relative strength** to distinguish strong uptrends (rising price, rising OBV, RSI in 60–80 zone) from exhaustion rallies (rising price, flat OBV, RSI in 80+ zone).
- **Support and resistance levels** on the price chart, because a volume divergence at a resistance level is more meaningful than in the middle of a trend.

OBV works best as a confirmation tool. If a stock is breaking out above a resistance level and OBV confirms with a surge, the breakout has credibility. If price breaks out but OBV lags, the trader should be skeptical.

## See also

<div class="wiki-seealso">

### Closely related

- Volume — the raw data underlying OBV
- [Volume-weighted average price](/volume-weighted-average-price/) — an alternative volume-based metric
- Price confirmation — the core concept OBV operationalizes
- Relative strength index — a complementary momentum indicator
- Moving average convergence divergence — a trend-following indicator often paired with OBV
- Technical analysis — the broader discipline

### Wider context

- Chart patterns — OBV helps validate breakouts and reversals
- Accumulation and distribution — a related OBV-style indicator
- [Momentum investing](/momentum-investing/) — a style that sometimes uses OBV signals

</div>

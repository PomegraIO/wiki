---
title: "OBV On-Balance Volume"
description: "Cumulative volume indicator that adds or subtracts daily volume based on price direction, revealing money flow conviction."
keywords:
  - obv on-balance-volume
  - volume indicator
  - money flow
  - momentum confirmation
---

*A **On-Balance Volume (OBV)** is a momentum indicator that accumulates [volume](/wiki/volume-breadth-divergence/) on an up/down basis: when price closes higher, that day's volume is added to a running total; when price closes lower, volume is subtracted. The resulting cumulative line reveals whether [volume](/wiki/volume-breadth-divergence/) is flowing into or out of a security, confirming or contradicting price trends.*

OBV is simple in construction but powerful in application. A price uptrend on declining OBV signals weak conviction (price rises, but few shares changing hands = distribution); a price downtrend on rising OBV signals strong selling pressure (price falls, high volume = capitulation). Traders use OBV to validate price moves and detect reversals early.

<aside class="wiki-infobox">

| Item | Detail |
|---|---|
| **Calculation** | Cumulative: if close > prior close, add volume; if close < prior close, subtract volume |
| **Output** | Absolute number (OBV line) from starting point, or standardized vs. price |
| **Timeframe** | Any period (5-min, hourly, daily, weekly); most common on daily charts |
| **Interpretation** | Rising OBV = money flowing in (bullish); falling OBV = money flowing out (bearish) |
| **Divergence** | Price makes new high but OBV does not = warning of reversal |
| **Confirmation** | Price breaks above [resistance](/wiki/resistance-zone-ceiling/), OBV confirms = strong break |

</aside>

## Calculation: simplicity and power

OBV is calculated as:

```
If close(today) > close(yesterday):
    OBV(today) = OBV(yesterday) + volume(today)

If close(today) < close(yesterday):
    OBV(today) = OBV(yesterday) - volume(today)

If close(today) = close(yesterday):
    OBV(today) = OBV(yesterday)  [unchanged]
```

The result is a cumulative line that oscillates upward and downward based on whether volume is associated with up or down days.

**Example**:
- Day 1: Close $100, volume 1M shares → OBV = 0 + 1M = 1M
- Day 2: Close $101, volume 800K shares → OBV = 1M + 800K = 1.8M (price up, add volume)
- Day 3: Close $99, volume 1.2M shares → OBV = 1.8M − 1.2M = 600K (price down, subtract volume)
- Day 4: Close $100, volume 500K shares → OBV = 600K (price unchanged, OBV flat)

The OBV line's shape tells the story: is [volume](/wiki/volume-breadth-divergence/) consistently flowing into the stock (steadily rising OBV), or is it ambiguous (oscillating OBV)?

## OBV divergence: the key signal

**Bullish divergence**: Price makes a new low, but OBV does not. This suggests selling pressure (price falling) is weakening (lower [volume](/wiki/volume-breadth-divergence/)). Fewer shares are changing hands on the way down, a sign of capitulation ending. Reversal is often imminent.

**Bearish divergence**: Price makes a new high, but OBV does not. The stock is rallying, but [volume](/wiki/volume-breadth-divergence/) is not increasing to support the rally. This is called "distribution"—smart money is selling into the rally while retail and momentum buyers are pushing price up. The rally is fragile and often reverses sharply.

The intuition: price moves are only meaningful if backed by [volume](/wiki/volume-breadth-divergence/). A price surge on low [volume](/wiki/volume-breadth-divergence/) is a failed rally; a price crash on high [volume](/wiki/volume-breadth-divergence/) is panic selling.

## Trend confirmation

**Strong uptrend**: Price makes new highs while OBV also makes new highs. This confirms the uptrend is healthy; money is flowing in at a scale that supports higher prices.

**Weak uptrend**: Price makes new highs, but OBV lags or declines. Distribution is underway; the rally is running out of fuel.

A trader seeing a price break above [resistance](/wiki/resistance-zone-ceiling/) might wait to see if OBV also breaks above its prior level before committing capital. If OBV breaks first, the buy signal is strong.

## OBV in practice: typical patterns

**Accumulation phase**: OBV rises steadily while price is relatively flat or drifting sideways. Smart money is quietly building a position. When price eventually breaks out, the move is often sharp and sustained.

**Distribution phase**: OBV rises briefly, then declines while price remains elevated. Insiders or institutions are selling into strength, preparing for a decline.

**Capitulation/Liquidation**: Price crashes on a massive spike in OBV (down). Everyone is selling at once. This often marks a bottom, followed by a bounce.

**Consolidation**: OBV oscillates without clear trend while price is flat. No consensus. Breakout direction (up or down) is ambiguous until OBV breaks decisively one way.

## Limitations and criticisms

**Assumption: volume = intent**: OBV assumes that high [volume](/wiki/volume-breadth-divergence/) on down days means genuine panic selling. But [algorithmic trading](/wiki/algorithmic-trading/), [market makers](/wiki/market-makers/) hedging, or rebalancing can create high [volume](/wiki/volume-breadth-divergence/) without conviction.

**Gap interpretation**: OBV does not distinguish between price gaps (large intraday moves) and normal oscillations. A stock might gap up 3% on opening news, then close unchanged; OBV stays flat, missing the intraday volume surge.

**Scaling issues**: OBV is unbounded. A stock with 1 billion shares trading daily will have OBV in the billions; a micro-cap with 100K daily shares will have OBV in the hundreds. Comparing OBV across stocks directly is meaningless.

**Lagging indicator**: OBV is derived from price and [volume](/wiki/volume-breadth-divergence/); it is not independent. A sophisticated trader might anticipate [volume](/wiki/volume-breadth-divergence/) inflows before they appear in OBV.

## Variants and enhancements

**OBV momentum**: Instead of plotting cumulative OBV, traders plot the rate of change of OBV (OBV today − OBV 14 days ago). This smooths out the jitter and shows whether [volume](/wiki/volume-breadth-divergence/) is accelerating or decelerating.

**OBV normalization**: Dividing OBV by average [volume](/wiki/volume-breadth-divergence/) or stock price to normalize across stocks and time periods.

**Chaikin Money Flow (CMF)**: A variant that weights [volume](/wiki/volume-breadth-divergence/) by how much of the day the stock traded above or below its midpoint. If a stock closes near its high, CMF gives it more bullish weight than OBV does.

**Accumulation/Distribution Line**: Another variant that considers not just up/down days, but where in the range (high/low/close) the price ended.

## OBV in the age of electronic trading

Modern [high-frequency trading](/wiki/high-frequency-trading/) and passive flows have changed the information content of [volume](/wiki/volume-breadth-divergence/). A [market maker](/wiki/market-makers/) quoting tightly (high [volume](/wiki/volume-breadth-divergence/)) is providing liquidity, not expressing conviction about direction. Passive index [rebalancing](/wiki/asset-rebalancing/) can create [volume](/wiki/volume-breadth-divergence/) spikes unrelated to fundamental news.

Sophisticated traders now supplement OBV with:
- **Large-block trade analysis**: Filtering out small [market maker](/wiki/market-makers/) quotes and focusing on block trades (typically >10K shares), which are more likely to represent real institutional interest.
- **Volume-weighted price**: VWAP (volume-weighted average price) tracks whether trading is concentrated at high or low prices within the day.
- **Smart money detection**: Algorithms that infer "smart" buying/selling by analyzing how price reacts to [volume](/wiki/volume-breadth-divergence/) spikes (if price rises on a [volume](/wiki/volume-breadth-divergence/) spike, the spike was likely bullish).

## Practical trade setup: OBV breakout

A common OBV-based setup:
1. Price is in a [consolidation](/wiki/consolidation-accounting/) range, OBV is oscillating sideways.
2. Price breaks above [resistance](/wiki/resistance-zone-ceiling/), and OBV simultaneously breaks above a prior OBV high.
3. Buy on the break, place [stop-loss](/wiki/stop-order/) below the [consolidation](/wiki/consolidation-accounting/) low.
4. Target: the next [resistance](/wiki/resistance-zone-ceiling/) level or a [moving average](/wiki/support-and-resistance/) acting as [support](/wiki/support-zone-floor/).

The logic: OBV confirmation reduces false breakout risk. Without OBV confirmation, the breakout may be a "dead cat bounce" (short-lived rally on low conviction).

<div class="wiki-seealso">

### Closely related
- [Volume Breadth Divergence](/wiki/volume-breadth-divergence/) — Relationship between price and trading volume trends
- [Accumulation Distribution Line](/wiki/accumulation-distribution-line/) — Volume-based momentum indicator incorporating price position
- [Chaikin Oscillator](/wiki/chaikin-oscillator/) — Momentum oscillator based on accumulation/distribution
- [Momentum Investing](/wiki/momentum-investing/) — Strategy based on price trends and continuation

### Wider context
- Technical Analysis — Study of price and volume patterns to predict price movements
- Indicators Momentum — Oscillators and indicators measuring trend strength
- [Support and Resistance](/wiki/support-and-resistance/) — Price zones where buying/selling pressure emerges
- [Divergence](/wiki/disposition-effect/) — Price and indicator moving in opposite directions

</div>

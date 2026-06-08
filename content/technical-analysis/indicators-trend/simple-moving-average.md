---
title: "Simple Moving Average"
description: "The arithmetic mean of price over a fixed window that smooths noise and reveals underlying trend."
keywords:
  - moving average
  - technical analysis
  - trend indicator
  - price smoothing
  - sma
  - support resistance
  - trend following
image: "/svg/technical-analysis.svg"
---

*A **simple moving average** (SMA) is the arithmetic mean of an asset's closing prices over a fixed number of periods (e.g., the average of the last 20 days). It smooths daily noise, makes trends visible, and often acts as dynamic support or resistance—a baseline against which to judge whether prices are stretched or retracing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Simple Moving Average — the trend baseline</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">The foundation of trend-following strategies and visual chart analysis.</div>

|   |   |
|---|---|
| **What it is** | Arithmetic mean of closing prices over N periods |
| **Formula** | (P1 + P2 + … + PN) / N |
| **Common windows** | 10, 20, 50, 100, 200 days |
| **Lag** | Significant: SMA reacts slowly to recent price moves |
| **Strengths** | Simple, universal, identifies trends visually |
| **Weaknesses** | All prior bars weighted equally; old data drags response time |
| **Best for** | Confirming trends, not predicting inflection points |

</aside>

## Why arithmetic simplicity works at scale

Charts without moving averages are chaos: every tick and rumour sends prices spasming up and down. A 20-day SMA collapses that chaos into a single line, showing the *true* direction beneath the noise. If a stock is closing USD 100, USD 99, USD 101, USD 98, USD 102 (jitter), the 20-day SMA might be USD 99.50—the signal that sentiment is roughly flat, not the contradictory jumps the raw data suggest.

The arithmetic mean is deliberately naive. Every day is weighted equally: the price from 20 days ago matters exactly as much as yesterday's. This sounds dumb—shouldn't recent price matter more?—but it's a feature, not a bug. A simple average is robust to one-day spikes and rumours. A company announces bad earnings and the stock drops USD 5 in one session; the 200-day SMA barely budges. Next week, reality reasserts, and the stock recovers halfway. The SMA stays calm, capturing the *regime* rather than the *shock*.

That said, the lag is real. By definition, an SMA is behind the price. If a stock is rallying sharply, the SMA lags the leading edge of the move, only catching up as the average incorporates new highs. Traders who want quicker response use exponential moving averages (which weight recent data more) or other techniques. But for confirming an existing trend (is the rally still in place?), the lag is acceptable.

## Visual support, resistance, and trend confirmation

When you plot an SMA on a chart, it often acts as a "magnet" for price. An uptrend keeps the price above the 50-day SMA; when it breaks below, it's a signal the uptrend may be stalling or reversing. A downtrend keeps price below the line; a break above is a potential reversal warning. This is not magic—it's an artifact of how large traders and institutions use moving averages to size positions and set stops.

Institutions often cluster their buy orders just above a major SMA (a "support level") and sell orders just below (a "resistance level"). If enough institutions do this, price is mechanically pushed back toward the line by waves of buying and selling. It becomes self-fulfilling: price bounces off the SMA because everyone *expects* it to.

The 200-day SMA is sacred in many trading systems. Equities trading above their 200-day SMA are considered to be in an uptrend; those below are in a downtrend. Many traders refuse to short a stock that's above its 200-day average, and many refuse to buy one below it. This creates a psychological boundary: the moment a stock breaks above or below its 200-day line, breakout traders pile in, accelerating the move. The line is not predictive; it's descriptive of the current regime and acts as a trigger for herd behaviour.

## Golden cross, death cross, and multiple-SMA strategies

A classic signal is the **golden cross**: when a faster moving average (50-day) crosses above a slower one (200-day). This is read as a shift to bullish momentum—short-term strength surpassing long-term weakness. The opposite, a **death cross** (50-day falling below 200-day), is read as a warning that short-term momentum is breaking and downtrend risk is rising.

These crossovers are not prophetic. They confirm that the regime has *already changed*, making them useful for trend-followers but dangerous for contrarians. A golden cross often appears months into a rally, after the easy gains are done. A death cross often appears when a stock has already crashed 30%. But for traders whose only view is "follow the trend," these signals are entry and exit points—simple, mechanical, and no opinions required.

Some traders layer three or more moving averages (50, 100, 200) to create a "ribbon" that shows the strength and durability of the trend. If all three are in order (50 > 100 > 200 on an uptrend), the trend is strong and confirmed. If they're tangled, the market is consolidating or choppy.

## Moving average convergence-divergence (MACD)

The SMA is not a self-contained tool; it's a building block. The MACD (moving average convergence-divergence) is a popular momentum indicator built on moving averages: it plots the difference between a 12-day and 26-day exponential moving average, plus a 9-day SMA of that difference (called the "signal line"). When the MACD crosses above the signal line, it's a bullish indicator; when it crosses below, bearish.

MACD smooths moving averages into momentum signals. The original SMA is about trend direction (up or down); MACD is about *acceleration* (is the trend speeding or slowing?). Traders combine them: if the price is above the 50-day SMA (uptrend confirmed) *and* the MACD is above its signal line (momentum positive), they're more likely to initiate a long position. If only one condition is met, the signal is weaker.

## The lag problem and the hunt for faster alternatives

The fundamental criticism of the SMA is that it's always behind the price. A 20-day SMA only reflects the last 20 days of data; any reversal in the last few days is invisible because it's swamped by prior days' closes. For a stock rallying from USD 90 to USD 110 over 10 days, the 20-day SMA (incorporating the prior 10 days of slower uptrend and earlier consolidation) might be USD 100—already USD 10 behind the market, signalling a retreat that hasn't happened yet.

Exponential moving averages (EMA) weight recent data exponentially higher, responding faster but becoming more sensitive to noise. Weighted moving averages (WMA) apply linearly increasing weights to older data. Volume-weighted moving averages (VWMA) weight by trading volume, treating high-volume closes as more "true." Adaptive moving averages adjust their window based on volatility. None of these solve the fundamental lag; they only choose which lag is acceptable to you.

For chart-based traders and momentum followers, the lag doesn't matter. The SMA confirms the trend after it's underway. For day traders hunting inflection points and reversals, the SMA is too slow—they need finer tools.

## When moving averages fail: range-bound markets

Moving averages shine in directional (trending) markets. They're disastrous in sideways, range-bound choppy markets. If a stock trades between USD 90 and USD 110 for six months, a 50-day SMA will sit somewhere in the middle (around USD 100) and signal nothing—every buy signal is whipsawed, every sell signal reverses.

In range-bound conditions, moving-average crossovers trigger "false breaks" repeatedly. A price spike above the 50-day SMA is read as bullish; the trader goes long; price rolls back into the range and stops out. The SMA strategy becomes a money-losing oscillator, profitable only in the brief windows when the range breaks and a real trend forms.

Institutions are aware of this. In calm, choppy markets, they reduce position size or switch to mean-reversion strategies (buying dips to the SMA, selling rallies above it). In explosive trending markets, they lean into momentum strategies that use moving average signals as confirmation.

## See also

<div class="wiki-seealso">

### Closely related

- Support and Resistance — price levels where buying and selling cluster
- Trend — directional movement that moving averages reveal
- Momentum — speed of price change; distinct from direction
- [Exponential Moving Average](/exponential-moving-average/) — faster-responding variant weighting recent data higher
- Moving Average Convergence-Divergence — momentum indicator built from moving averages

### Wider context

- Technical Analysis — chart-based price prediction and pattern recognition
- Breakout — price burst through resistance or support
- Mean Reversion — prices tend to return to historical average over time
- [Volatility Smile](/volatility-smile/) — how price distribution shapes trading signals
- [Trend Following](/trend-following/) — strategy betting directional momentum persists

</div>

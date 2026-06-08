---
title: "Stochastic Oscillator: How It Works"
description: "The stochastic oscillator measures where a stock's price sits within its recent range using %K and %D lines. Learn how it works, what overbought and oversold mean, and how to avoid false signals."
keywords:
  - stochastic oscillator
  - how does it work
  - technical analysis
  - overbought oversold
  - momentum indicator
  - "%K %D"
---

*The **stochastic oscillator** is a momentum indicator that compares a stock's closing price to its range over a lookback period, expressing the result as a percentage from 0 to 100. It consists of two lines: **%K** (the raw calculation) and **%D** (a smoothed average). Readings above 80 are called overbought; below 20, oversold. But in strong trends, overbought can persist for weeks, so traders must distinguish between ranging markets (where the oscillator is reliable) and trending markets (where it generates false signals).*

<div class="wiki-hatnote">

This article explains the stochastic oscillator's calculation and interpretation. For a broader view of momentum indicators, see the entry on technical analysis.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stochastic Oscillator: How It Works — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">A stochastic oscillator uses the price range to identify overbought and oversold conditions, but works best in sideways markets.</div>

|   |   |
|---|---|
| **%K formula** | (Close − Low over N periods) / (High − Low over N periods) × 100 |
| **%D line** | 3-period simple moving average of %K (the smoothed version) |
| **Standard period** | N = 14 periods (14 days, 14 weeks, etc., depending on timeframe) |
| **Overbought signal** | %K or %D above 80 |
| **Oversold signal** | %K or %D below 20 |
| **Best use case** | Ranging or oscillating markets |
| **Weakness** | Stays overbought/oversold for long stretches in strong trends |

</aside>

## The Calculation: %K and %D

The **%K line** is the core of the stochastic oscillator. It asks: within the past N periods, where does today's close sit in the range from the lowest low to the highest high?

The formula is:

```
%K = [(Close − Lowest Low over N periods) / (Highest High − Lowest Low over N periods)] × 100
```

For a 14-period stochastic (the most common setting), you look back 14 periods (14 days, 14 weeks, etc.). If the 14-day high is $110, the 14-day low is $90, and today's close is $103, then:

```
%K = [(103 − 90) / (110 − 90)] × 100 = (13 / 20) × 100 = 65
```

A %K of 65 means the close is 65% of the way from the low to the high over the past 14 days—near the top of the range but not at the extreme.

The **%D line** is a 3-period simple moving average of %K. This smoothing reduces noise and often generates cleaner buy/sell signals. When %K crosses above %D, some traders view it as a bullish signal (especially if both are below 50). When %K crosses below %D, it is a bearish signal.

## Overbought and Oversold Thresholds

**Overbought**: When %K rises above 80, the price is in the upper extreme of the recent range. In a healthy uptrend, this can happen repeatedly without warning of a reversal. The assumption behind the overbought label is that the price has stretched too far and is "due" to pull back—a mean reversion bet.

**Oversold**: When %K drops below 20, the price has fallen to the lower extreme. Again, in a strong downtrend, oversold readings can persist.

A key insight: **overbought and oversold do not mean the price will reverse immediately**. They signal the price is at an extreme *within the recent range*, not that a reversal is guaranteed. Many traders interpret extreme readings as a *setup for* a reversal, not a reversal itself—they wait for confirmation, such as a close back into the middle of the range or a divergence with the price.

## Trending Markets: False Signals

The stochastic oscillator shines in **ranging markets**—periods when price oscillates between a stable floor and ceiling without a clear directional trend. In a ranging market, %K bouncing from 20 to 80 and back is meaningful: the range is the relevant context.

But in a strong **uptrend**, the stochastic stays overbought (above 80) for weeks or months. The price keeps hitting new 14-day highs, so the recent high keeps climbing, and the %K remains elevated. A trader relying on overbought readings to short or bet on a reversal will lose money repeatedly. The oscillator is not broken; it is simply not the right tool for trend-following. The trend is the context, and the price can stay extreme within it indefinitely.

Similarly, in a strong downtrend, %K stays oversold. The low keeps falling, and the close keeps near the bottom of the recent range. An oversold reading does not predict a bounce; the trend persists.

## Divergence: A More Reliable Signal

A more reliable use of the stochastic is **divergence**. When the price makes a new high but the stochastic fails to make a new high, it suggests momentum is waning—the oscillator is saying "the price climbed, but the interior distribution of the recent range is not confirming it."

For example:
- Price rallies from $95 to $110 (new high). %K hits 95, then falls to 85 on a pullback.
- Price rallies again and tags $112 (new high). But %K only reaches 80 (lower than the prior 95).

This **bearish divergence** signals that the uptrend may be losing steam. Experienced traders watch for divergences as a sign to tighten stops or reduce size in overbought conditions.

Conversely, in a downtrend:
- Price falls to $75 (new low). %K hits 5.
- Price rallies to $78, then falls again and tags $74 (new low). But %K only reaches 15 (higher than the prior 5).

This **bullish divergence** signals the downtrend may be weakening.

## Fast vs. Slow Stochastic

Traders sometimes adjust the parameters:

- **Fast stochastic**: The raw %K and a 3-period moving average of %K as the signal line. This is sensitive and generates more signals but more noise.
- **Slow stochastic**: The 3-period moving average of %K becomes the new %K line; the signal is a 3-period average of that. This is smoother and often preferred for trending analysis.

The default 14-period lookback can also be shortened (e.g., 9 periods for more sensitivity in shorter timeframes) or lengthened (e.g., 21 periods for longer-term analysis).

## Interpretation Rules

1. **In a range**: Overbought/oversold readings are meaningful. Buy near 20; sell near 80 (but confirm with other signals).
2. **In an uptrend**: Ignore standalone overbought readings. Look for bearish divergence before shorting.
3. **In a downtrend**: Ignore standalone oversold readings. Look for bullish divergence before buying.
4. **Crossovers**: %K crossing above %D can signal the start of a new move within the range, but this is noisy without trend context.
5. **Confirmation**: Always confirm stochastic signals with price action—support/resistance levels, candlestick patterns, volume—before trading.

## Common Mistakes

Many new traders treat overbought/oversold as immediate reversal signals and fade (bet against) strong trends. This usually fails because the oscillator is *descriptive* (the price is extreme within the range) but not *predictive* (the trend will continue). A trader shorting a stock because %K is above 80 in a bull market is fighting momentum and often gets stopped out.

A second mistake is trading every crossover of %K and %D without regard to the broader market structure. Crossovers are noisy; they mean little without context.

## See also

<div class="wiki-seealso">

### Closely related

- [Momentum investing](/momentum-investing/) — the broader discipline of trading price trends and extremes
- [Support and resistance](/support-and-resistance/) — price levels that anchor range-bound markets and interact with oscillator signals
- [Moving average](/moving-average/) — the underlying smoothing mechanism in the %D line and in trend identification
- [Historical volatility](/historical-volatility/) — the range's width and how the oscillator scales with it
- [Price-to-earnings ratio](/price-to-earnings-ratio/) — a fundamental counterpoint to purely technical signals

### Wider context

- [Market cycle](/market-cycle/) — the range and trend phases that determine whether the stochastic is useful
- [Trend following](/trend-following/) — why oscillators alone are insufficient for trending strategy
- [Volatility smile](/volatility-smile/) — related extreme-event behavior in options markets
- [Overconfidence bias](/overconfidence-bias/) — why traders over-rely on indicator signals

</div>
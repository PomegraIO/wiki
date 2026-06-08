---
title: "Aroon Indicator"
description: "An oscillator measuring the elapsed time since a recent high or low to gauge trend strength and momentum."
keywords:
  - aroon indicator
  - aroon up
  - aroon down
  - trend strength
  - technical analysis
  - momentum
image: "/svg/technical-analysis.svg"
---

*The **Aroon Indicator** measures the number of bars since the most recent high (Aroon Up) and the most recent low (Aroon Down), then scales each to 0–100. Developed by technician Tushar Chande in 1995, the Aroon reveals trend strength and potential reversals by tracking *how recently* price made its highs and lows, not how far it moved.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Aroon Indicator — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Track recent highs and lows to detect when dominance is shifting.</div>

|   |   |
|---|---|
| **What it is** | Two lines measuring bars since highest high and lowest low |
| **Creator** | Tushar Chande (1995) |
| **Aroon Up** | (Periods − bars since high) ÷ Periods × 100 |
| **Aroon Down** | (Periods − bars since low) ÷ Periods × 100 |
| **Scale** | 0–100 for each line |
| **Typical lookback** | 25 periods |
| **Crossover zones** | Convergence at 50 signals momentum shift |
| **Best for** | Identifying trend initiation and exhaustion |
| **Strength** | Clean, intuitive logic; leads traditional oscillators |
| **Limitation** | Can lag in choppy, sideways ranges |

</aside>

## Why "when" matters more than "how much"

Most momentum indicators focus on the *magnitude* of price change: how much price moved up versus down, how fast it climbed, how steeply it fell. The Aroon inverts this focus. It asks: **when did the high and low happen?**

In an uptrend, the most recent high is fresh—maybe 1 or 2 bars old. The most recent low is stale—perhaps 15 bars old. This recency difference reveals trend strength: if Aroon Up (high recency) is rising and Aroon Down (low recency) is falling, the trend is *gaining power*, not losing it. Conversely, if both lines are converging toward the middle, trend strength is evaporating, and a reversal may be imminent.

This time-based logic is more forward-looking than price-based momentum. You see dominance shifting before magnitude reverses, making the Aroon an early-warning system for trend breaks.

## How the calculation works

The Aroon formula is straightforward. Over your chosen lookback period (typically 25 bars), count how many bars ago the highest high occurred. Call this **HighBars**. Count how many bars ago the lowest low occurred. Call this **LowBars**. Then:

**Aroon Up = (Periods − HighBars) ÷ Periods × 100**

**Aroon Down = (Periods − LowBars) ÷ Periods × 100**

If the high occurred 2 bars ago in a 25-bar window, Aroon Up is **(25 − 2) ÷ 25 × 100 = 92**. If the low occurred 20 bars ago, Aroon Down is **(25 − 20) ÷ 25 × 100 = 20**. The Up line is near the top; the Down line is near the bottom. Classic uptrend.

As bars pass without a new high, Aroon Up decays. If 25 bars have passed since the last high, Aroon Up falls to zero. But the *moment* a new high appears, it resets to 100. This binary logic—reset on new extreme or decay steadily—creates clean, readable signals with no smoothing or lag.

## Reading the crossover and the 50 zone

The Aroon signal is most powerful at **crossovers**. When Aroon Up crosses above Aroon Down, an uptrend is initiating. The Down line is decaying (lows are old), while the Up line is gaining (highs are fresh). This is a bullish shift in dominance.

When Aroon Down crosses above Aroon Up, the reverse: lows are becoming more recent than highs, signalling downtrend initiation. In a strong trend, one line sits near 100 while the other camps near 0. In a choppy, range-bound market, both lines oscillate around 50, crossing repeatedly and producing false signals.

The **50 zone is critical**. When both lines converge near 50, neither highs nor lows are recent—price is choppy and rangy. As trend emerges, one line shoots toward 100 while the other collapses toward 0. If both lines approach or cross the 50 midline, be alert: a trend may be ending or a transition from one direction to another is underway.

## Trend initiation and strength

The Aroon excels at detecting the *start* of a trend before it has moved far. Imagine price has been ranging for weeks. Aroon Up and Aroon Down are both dancing around 50. Then, suddenly, price makes a new high. Aroon Up jumps to 100. The next bar doesn't make a new high, but Aroon Up is still 96—recent highs are dominating. Buyers have seized control.

This clarity is why swing traders and trend-following systems love the Aroon. You do not need a trend to be large to see it starting; you only need highs to be recent. In contrast, moving average crossovers or MACD signals often lag by several bars, letting the best part of a trend slip away before they confirm.

The Aroon also shows *strength degradation*. In a mature uptrend, if the high was 10 bars ago and the low was 15 bars ago, Aroon Up is 60 and Aroon Down is 40. The trend is still biased up, but highs are less recent—strength is fading. This is often the first warning that a pullback or reversal is coming, before price actually reverses.

## Adjusting the lookback period

The default 25-period Aroon suits daily charts and 4-hour swings. Shorter lookbacks (14, 9) expose fast, intraday trends; longer ones (50, 100) smooth out noise and track multi-week or multi-month structural trends.

A 14-period Aroon is sensitive and whippy, crossing repeatedly in choppy conditions. A 50-period Aroon is smoother but slower to confirm new trends. Backtesting on your own timeframe and asset is essential. In highly liquid, trending assets (major equity indices), longer periods work well. In thin, gap-prone instruments, shorter periods often perform better.

## When Aroon works and when it falters

The Aroon shines in trending markets and at the boundary between trends and ranges. Initiation signals (crossovers) are often clean, and strength degradation often precedes reversals by a bar or two. You can trade the Aroon almost as a standalone system in these environments.

The Aroon struggles in choppy, sideways ranges. When price oscillates without a clear direction, both Aroon lines dance between 40 and 60, generating frequent false crossovers. Each new local high or low resets one line toward 100, then decay pulls it back down. The result is whipsaws.

To filter false signals, many traders add a trend filter or volatility check. Trade Aroon crossovers only when ATR (Average True Range) is elevated or when a moving average confirms the broader trend direction. This prevents you from shorting Aroon Down crossovers in an overall uptrend, or going long Aroon Up crossovers in a downtrend.

## Aroon versus other trend tools

Unlike RSI or Stochastic oscillator, which measure momentum magnitude, the Aroon measures recency of extremes. This makes it complementary rather than redundant. A high RSI reading means *current* momentum is strong; high Aroon Up means *recent* highs are being made *and* sustained.

The Aroon is also less bounded than RSI. RSI moves between 0 and 100 but spends most time in the 30–70 range in steady trends. The Aroon, with two independent lines, offers more nuance: you can see Aroon Up at 100 (fresh highs) and Aroon Down at 40 (stale lows) simultaneously, clearly depicting an uptrend. RSI alone would show 70, which many read as "overbought," a misleading label in a young, strong trend.

## See also

<div class="wiki-seealso">

### Closely related

- ADX — measures trend strength using directional movement and volatility
- Aroon oscillator — the difference between Aroon Up and Aroon Down as a single line
- Moving average — trend confirmation tool using average price over time
- RSI — momentum oscillator measuring up-closes versus down-closes
- MACD — trend momentum using exponential moving average divergence
- Trend — sustained directional price moves and their characteristics

### Wider context

- Technical analysis — price and volume pattern recognition for trading
- Momentum — rate of change and directional strength
- Trend initiation — early signals of new trends forming
- Trend exhaustion — declining strength and reversal proximity
- Volatility — price swings and market regime detection

</div>

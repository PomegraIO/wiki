---
title: "True Strength Index Settings: Choosing the Right Periods"
description: "How TSI period inputs control noise reduction versus responsiveness, with preset configurations for intraday, swing, and position trading timeframes."
keywords:
  - true strength index period settings
  - tsi settings configuration
  - true strength index periods
  - tsi parameters
  - double exponential moving average
  - momentum indicator settings
image: "/svg/technical-analysis.svg"
---

*The **True Strength Index** (TSI) applies two sequential [exponential moving averages](/moving-average/) to price momentum, and the two period parameters—long and short—interact to control the balance between noise suppression and signal responsiveness. Choosing the right periods depends on timeframe, volatility, and whether you prioritize filter smoothness or rapid reversal detection.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TSI Settings — configuration by timeframe</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis and price charts." />

<div class="wiki-infobox-caption">Two EMA periods determine how much the TSI filters noise and how quickly it responds to price turns.</div>

|   |   |   |
|---|---|---|
| **Timeframe** | **Long EMA** | **Short EMA** |
| Intraday (5–15 min) | 13–25 | 5–7 |
| Swing (4H–1D) | 25–28 | 13–15 |
| Position (Weekly+) | 50+ | 20–25 |
| Momentum focus | Shorter | 5–10 |
| Trend filter focus | 40–50 | 10–15 |

</aside>

## How the TSI Works: The Two Smoothing Layers

The True Strength Index applies two sequential exponential moving averages to the rate of change of price (momentum), then scales and expands the result. Unlike a single-EMA [moving average](/moving-average/), this double-smoothing design creates a filter that removes more noise while still tracking turning points.

The **first (long) EMA** smooths the momentum line over a longer period. The **second (short) EMA** re-smooths the output of the first, creating compounded noise reduction. The combination means fewer false signals but also delayed entry signals.

The original design, published by William Blau, used a long EMA of 25 bars and a short EMA of 13 bars for daily charts. However, these are starting points, not universal rules. The optimal periods depend on:

- **Chart timeframe**: A 1-minute chart requires much shorter periods than a weekly chart.
- **Market volatility**: Choppy, sideways markets benefit from longer periods; trending markets tolerate shorter, more responsive settings.
- **Trading style**: Day traders want rapid signals; position traders want robust trend confirmation.

## The Long EMA: Primary Noise Filter

The long EMA (applied first to momentum) does the heavy lifting in noise reduction. Longer periods smooth out whipsaws and false breakouts. Shorter long periods preserve more sensitivity to price movement but allow more noise through.

**Common long EMA values:**

- **13–15 bars**: Responsive to intraday moves; suitable for 5-minute and 15-minute charts.
- **25–28 bars**: The default for daily/4-hour charts; good balance of smoothing and responsiveness.
- **50+ bars**: Heavy smoothing for weekly or monthly charts; captures primary trends only.

Increasing the long EMA from 25 to 50 will roughly halve the number of TSI crossovers (fewer trades), while shortening it to 13 will roughly double them. The trade-off is timing: longer periods lag; shorter periods whip.

## The Short EMA: Secondary Filter and Shape

The short EMA (applied to the output of the long EMA) adds a second layer of smoothing and determines how aggressively the indicator curves. Shorter short-period EMAs make the TSI more angular and responsive to momentum changes; longer short-period EMAs make it rounder and smoother.

**Common short EMA values:**

- **5–7 bars**: High responsiveness; every shift in momentum shows up quickly. Suitable for intraday timeframes and momentum fades.
- **13–15 bars**: Medium smoothing; good for 4-hour and daily charts when you want brisk signal change without whipping.
- **20–25 bars**: Heavy secondary smoothing; reduces the impact of short-term noise spikes.

The short EMA is typically 30–50% of the long EMA period, though traders sometimes experiment with wider ratios (e.g., long 28, short 5) to preserve sensitivity.

## Presets by Timeframe and Style

### Intraday (5–15 minute charts)
- **Balanced:** Long 13, Short 6
- **Responsive:** Long 10, Short 5
- **Filtered:** Long 20, Short 7

Intraday charts have high noise and frequent reversals. Shorter periods allow the TSI to capture microtrends and momentum fades without clipping too much real price action. A long EMA of 13 or less is standard because 25 bars on a 5-minute chart already spans over 2 hours—too much delay for a day trader.

### Swing Trading (4-hour to daily charts)
- **Standard:** Long 25, Short 13 (Blau's original)
- **Faster:** Long 22, Short 11
- **Slower:** Long 28, Short 14

This is the sweet spot for many traders. The long EMA of 25 covers roughly 5–6 trading days on a daily chart, removing intraday noise while preserving swing turns. The short EMA of 13 adds responsive second-layer smoothing.

### Position Trading (Weekly and higher)
- **Standard:** Long 50, Short 20
- **Extended:** Long 60, Short 25

Position traders care about regime and primary trend, not intraday gyrations. A long EMA of 50 on a weekly chart spans a full year, filtering out seasonal and cyclical noise to isolate the multi-month trend.

### Momentum/Counter-Trend Focus
- **Long:** 20–25
- **Short:** 5–7

If you are hunting momentum reversals (e.g., overbought/oversold bounces), use shorter periods so the TSI reacts quickly to momentum shifts. Pair this with levels (±25, ±50) to identify extremes.

## Fine-Tuning in Practice

Once you have chosen a baseline preset, adjust within this framework:

1. **Too many false signals?** Increase the long EMA by 3–5 bars, or increase the short EMA by 2–3 bars. More smoothing trades frequency for reliability.

2. **Signals lag your entries by multiple bars?** Shorten the long EMA by 3–5 bars, or reduce the short EMA by 2 bars. More responsiveness costs you some noise immunity.

3. **Signals cluster in choppy markets?** Increase the long EMA significantly (25 → 40, or 50 → 70). This prevents the TSI from whipping into the oversold/overbought zone every few bars.

4. **Missing short momentum flips?** Use asymmetric ratios: keep the long period moderate (22–28) but cut the short period to 5–6. This preserves the primary trend filter while sharpening inflection detection.

## The Signal Line and Centerline

Most TSI implementations include a signal line (an EMA of the TSI itself, often 5–7 bars) and the TSI centerline at zero. Traders use TSI-to-signal crosses for entry and TSI crossings of the centerline for trend confirmation. These mechanics do not change with parameter adjustment, but the frequency and reliability of signals do.

A TSI that crosses its signal line every 2–3 bars indicates the parameters are too responsive for your market. A TSI that waits 15–20 bars between crosses indicates the parameters are too slow.

## Testing Your Settings

No preset is universal. The best approach:

1. Set a baseline appropriate to your timeframe (use the presets above as a starting point).
2. Backtest 50–100 trades on recent data with TSI entry and exit rules you plan to use.
3. Count false signals (trades that lose money on noise reversals) and missed signals (times the TSI failed to catch a real turn).
4. If false signals dominate, extend the long EMA by 2–5 bars.
5. If missed signals dominate, shorten both periods by 1–3 bars.
6. Record the final settings and stick with them for at least one live trading cycle before tweaking again.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average](/moving-average/) — the exponential moving average foundation of TSI
- [Momentum Investing](/momentum-investing/) — trading strategy exploiting the rates of change TSI measures
- [Trend Following](/trend-following/) — strategy using TSI for trend confirmation
- [Support and Resistance](/support-and-resistance/) — levels TSI crossovers often coincide with
- Technical Analysis — broader discipline of price-based trading signals

### Wider context

- Indicator — category of price-derived decision tools
- [Historical Volatility](/historical-volatility/) — volatility measurement affecting optimal TSI tuning
- [Price Discovery](/price-discovery/) — process TSI attempts to filter from noise
- [Market Timing](/market-timing/) — discipline using indicators like TSI

</div>

---
title: "RSI Relative Strength"
description: "Momentum oscillator measuring the magnitude of recent price changes to identify overbought and oversold conditions."
keywords:
  - rsi
  - relative strength index
  - momentum indicator
  - overbought oversold
---

*The **Relative Strength Index (RSI)** is a momentum oscillator that bounces between 0 and 100, flagging when a security has risen or fallen so sharply over a short window that a reversal is likely. RSI above 70 is commonly deemed overbought; below 30, oversold. It is one of the most widely used indicators in technical analysis, implemented by nearly every trading platform.*

<aside class="wiki-infobox">

| Factor | Detail |
|--------|--------|
| **Formula** | RS = Avg Gain / Avg Loss; RSI = 100 − (100 / (1 + RS)) |
| **Period** | Typically 14 bars (days, hours, minutes) |
| **Range** | 0 to 100 |
| **Overbought** | > 70 (often 80 in strong uptrends) |
| **Oversold** | < 30 (often 20 in strong downtrends) |
| **Smoothing** | Wilder's Method (exponential moving average) |
| **Signals** | Divergence, centerline crosses, extremes |

</aside>

## Construction and interpretation

RSI is calculated over a lookback period (usually 14 bars). For each bar, you measure the up-close change (if positive) or the down-close change (if negative). You then average the ups over the period and the downs over the period, forming a [ratio](/wiki/correlation-coefficient/) called Relative Strength (RS). The RSI formula normalizes RS into a 0–100 scale:

RSI = 100 − (100 / (1 + RS))

An RSI of 50 means the average gain equals the average loss (neutral momentum). An RSI of 70 means up moves have outpaced down moves significantly; an RSI of 30 means the reverse. The oscillator is **not** a price forecast; it is a measure of the *intensity* of recent moves, useful for timing entry and exit rather than direction.

## Overbought and oversold signals

The most widespread use of RSI is identifying extremes. A reading above 70 suggests the security has been rising so sharply that a pullback or consolidation is probable. Below 30, a rally is probable. These thresholds are not inviolable; they are heuristics. In a strong [bull market](/wiki/bull-market/), RSI can remain above 70 for weeks; in a bear market, below 30 for longer.

Professional traders adjust thresholds to market regime. During high [volatility](/wiki/volatility-smile/), 80 and 20 are more meaningful. During calm periods, 60 and 40 may trigger reversals. [Algorithmic traders](/wiki/algorithmic-trading/) often backtest optimal thresholds for specific securities.

## Divergences: price vs. momentum

A **bullish divergence** occurs when price makes a new low but RSI makes a higher low. This suggests downward momentum is fading even as price is still falling — a potential bottom. A **bearish divergence** is the mirror: price makes a new high but RSI makes a lower high, suggesting upward momentum is weakening ahead of a top.

Divergences are among the most reliable signals from RSI and are heavily watched by swing traders. However, they are not perfect; momentum can diverge for a long time before price actually reverses. Combining RSI divergence with other signals (e.g., [support and resistance](/wiki/support-and-resistance/), [volume](/wiki/volume-profile-support/)) increases confidence.

## Centerline crosses and transitions

RSI moving from below 50 to above 50 is read as a shift to positive momentum; the reverse, a shift to negative momentum. These crosses are less flashy than overbought/oversold extremes but can be useful for longer-term traders. A security that crosses above the 50 line on a [weekly chart](/wiki/candlestick-chart/) is often transitioning from a downtrend to an uptrend.

## Period length and timeframe

A 14-period RSI is standard, but the indicator can be calculated at any period. Shorter periods (e.g., 5-bar RSI) are more volatile and trigger more signals; longer periods (e.g., 21-bar RSI) are smoother. Intraday traders often use 5 or 9; swing traders use 14 or 21. The right period depends on the trading horizon: a signal relevant to an [options expiration](/wiki/option-expiration/) schedule is useless to a buy-and-hold investor.

## Limitations and misuse

RSI is a *relative* measure, not an absolute one. It does not account for [volume](/wiki/volume-breadth-divergence/), [price acceleration](/wiki/price-acceleration-strategy/), or fundamental catalysts. A stock can be "overbought" and still rise for months if earnings growth is accelerating. Equally, RSI can remain oversold during a corporate crisis as shareholders capitulate. Using RSI in isolation leads to many false signals; it is best combined with [chart patterns](/wiki/head-and-shoulders/), [moving averages](/wiki/moving-average/), and price action.

Retail traders sometimes mechanically buy oversold stocks or short overbought stocks without considering the broader context. This is known as "fighting the [trend](/wiki/trendline/)." Professionals use RSI as one signal among many and always ask: *Is the trend still intact? Why is RSI at this extreme?*

## RSI and mean reversion

RSI's effectiveness stems from mean reversion: very strong moves tend to exhaust and consolidate. When RSI is 80, the security has likely moved so far in one direction that some reversal is due. But "due" does not mean "imminent." Positions can overshoot RSI extremes for extended periods, especially during [momentum](/wiki/momentum-investing/) rallies or panics. A [contrarian](/wiki/contrarian-investing/) using RSI must have conviction in mean reversion and capital to wait out the bounce.

## Comparison to other momentum indicators

The [MACD](/wiki/macd-indicator/) (moving average convergence divergence) is another popular oscillator, but it uses price-based moving averages rather than up/down averages. The [Stochastic Oscillator](/wiki/stochastic-oscillator/) compares the close to the high–low range over the period. The [Williams R](/wiki/williams-r-indicator/) is similarly structured. All three measure momentum; RSI is the most intuitive and widely understood.

<div class="wiki-seealso">

### Closely related
- Technical Analysis — discipline of price-pattern analysis
- [Momentum Investing](/wiki/momentum-investing/) — strategy around trend continuation
- Overbought Oversold — extremes in momentum
- [Candlestick Chart](/wiki/candlestick-chart/) — charting format for RSI overlay
- [Support and Resistance](/wiki/support-and-resistance/) — price levels RSI helps confirm

### Wider context
- [Mean Reversion](/wiki/mean-reversion-investing/) — reversion to average after extremes
- [Volume Breadth](/wiki/volume-breadth-divergence/) — alternative momentum measure
- [Algorithmic Trading](/wiki/algorithmic-trading/) — systematic RSI application
- [MACD Indicator](/wiki/macd-indicator/) — alternative oscillator
- [Trend Following](/wiki/trend-following/) — long-term momentum strategy

</div>

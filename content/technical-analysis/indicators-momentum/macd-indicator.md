---
title: "MACD Indicator"
description: "Moving average convergence-divergence oscillator that measures momentum via the gap between fast and slow exponential moving averages."
keywords:
  - momentum indicator
  - moving average
  - signal line
  - trend following
  - technical analysis
---

*The **MACD** (moving average convergence-divergence) indicator measures price momentum by tracking the distance between a fast 12-period and slow 26-period exponential moving average. When the gap widens, momentum accelerates; when it narrows and crosses, the trend may reverse. A signal line (9-period EMA of MACD) and histogram help traders spot entries and exits.*

<aside class="wiki-infobox">

| Component | Period | Calculation |
|-----------|--------|-------------|
| **Fast EMA** | 12 | Shorter-term average |
| **Slow EMA** | 26 | Longer-term average |
| **MACD line** | — | Fast EMA minus slow EMA |
| **Signal line** | 9 | EMA of MACD |
| **Histogram** | — | MACD minus signal line |
| **Zero line** | — | Point where fast = slow |

</aside>

## How MACD combines two moving averages into a single oscillator

The MACD line is simply the 12-period exponential moving average minus the 26-period exponential moving average. When price is in a strong uptrend, the fast average pulls ahead of the slow average, pushing MACD into positive territory. In a downtrend, the fast average falls below the slow average, and MACD turns negative.

The magic lies in the simplicity: MACD captures momentum as a single number on a chart. When MACD is rising, momentum is strengthening. When MACD is falling (even if price is still rising), momentum is weakening.

## Signal line and histogram: the second and third layers

Traders rarely trade MACD in isolation. Instead, they plot a 9-period exponential moving average of MACD itself, called the **signal line**. When the MACD line crosses *above* the signal line, many traders interpret that as a bullish momentum signal. When MACD crosses *below* the signal line, that is often read as bearish.

The **histogram** is simply the distance between MACD and its signal line. A growing positive histogram means bullish momentum is accelerating; a shrinking positive histogram suggests momentum is fading even if price hasn't reversed yet. This histogram divergence is often the earliest warning of a coming reversal.

## Zero-line crosses as trend-transition signals

When MACD crosses the zero line (where fast EMA equals slow EMA), the trend is shifting. A cross above zero is a potential buy signal; a cross below zero is a potential sell signal. Most [trend-following](/wiki/trend-following/) traders wait for zero-line crosses as confirmation of a change in the structure of the move.

These crosses lag price slightly because MACD is derived from moving averages, which are inherently lagging indicators. That trade-off—lag for smoothing—is the whole reason moving-average-based tools are so popular in technical analysis.

## Divergence as a reversal warning

MACD divergence occurs when price makes a new high or low but MACD does not. For example, if a stock rallies to a new high but MACD stays below its previous peak, the divergence suggests momentum is weakening even as price is rising. Many traders treat this as a warning signal that the rally is running out of steam.

Bullish divergence (price down, MACD up) and bearish divergence (price up, MACD down) are subjective to identify on a chart but can offer weeks of advance warning before a reversal.

## Strengths: simplicity and availability

MACD is one of the most popular indicators worldwide because it is easily interpreted, included in virtually every charting platform, and effective on multiple timeframes. A trader can apply the same logic to daily, hourly, or 15-minute charts. It works on [stocks](/wiki/stock/), [commodities](/wiki/commodity-futures-rolling/), [forex](/wiki/forex-leverage/), and [crypto](/wiki/cryptocurrency-exchange/).

The math is transparent, and the default periods (12, 26, 9) have been validated across decades of trading. Beginners find it intuitive; professionals use it as one input in broader trading systems.

## Limitations: lag and whipsaws in choppy markets

MACD lags price by design. In a sharp reversal, MACD may confirm the turn several days after price has already moved. In choppy, sideways markets, MACD generates false crosses of the signal line, triggering trades that are quickly reversed. Many traders use MACD in combination with other indicators (support-resistance, volatility measures, [candlestick patterns](/wiki/candlestick-pattern/)) to filter out whipsaws.

MACD also does not incorporate volume, so a high-MACD reading on low volume may be unreliable.

## Comparing to other momentum tools

MACD is a trend-following momentum tool. The [RSI (relative strength index)](/wiki/rsi-relative-strength/) is an oscillator bounded between 0 and 100, useful for overbought/oversold identification. The [Stochastic](/wiki/stochastic-oscillator/) is another oscillator that compares close price to the range. MACD is smoother and less prone to extreme readings than oscillators; RSI and Stochastic are better at identifying reversal points in tight ranges.

<div class="wiki-seealso">

### Closely related
- [Momentum indicator](/wiki/momentum-investing/) — the broader class of tools measuring velocity
- Exponential moving average — the core calculation MACD is built on
- Signal line — the 9-period EMA that generates crosses
- [Candlestick pattern](/wiki/candlestick-pattern/) — often confirmed by MACD divergence

### Wider context
- [Trend following](/wiki/trend-following/) — trading strategy MACD supports
- Technical analysis — discipline in which MACD is a standard tool
- [Momentum investing](/wiki/momentum-investing/) — longer-term strategy using momentum themes
- [Volatility](/wiki/volatility-index-option/) — environmental factor affecting MACD reliability

</div>

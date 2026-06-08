---
title: "Awesome Oscillator Indicator"
description: "Bill Williams' Awesome Oscillator: construction from moving average differences, saucer and zero-line setups, and application in momentum analysis."
keywords:
  - awesome oscillator indicator
  - awesome oscillator trading
  - awesome oscillator setup
  - ao indicator
  - bill williams oscillator
  - saucer momentum setup
image: /svg/technical-analysis.svg
---

*The **Awesome Oscillator** is Bill Williams' momentum indicator built from the difference between a 5-period and 34-period simple moving average of the midpoint (high + low) / 2. It measures whether the "awesome" force (fast-moving average minus slow-moving average) is accelerating or decelerating. The saucer pattern (bars rising before crossing zero) and zero-line crossings are the canonical trade setups.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Awesome Oscillator Indicator — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A momentum divergence tool with named setups, popular among swing traders and day traders.</div>

|   |   |
|---|---|
| **Constructed from** | SMA(5) − SMA(34) of (H+L)/2 |
| **Data range** | Typically unbounded (can be -∞ to +∞) |
| **Visual representation** | Histogram bars (red/green) around zero line |
| **Key setups** | Saucer, zero-line cross, divergence |
| **Best timeframe** | 4-hour, daily, intraday (5m–30m) |
| **Signal lag** | Moderate; lags sharp price moves 1–2 bars |
| **Confirmation tool** | Works best with price action, not standalone |

</aside>

## Construction: two moving averages of the midpoint

The Awesome Oscillator (AO) starts with the midpoint of each bar: (High + Low) / 2. This is the "awesome" price—the center of the bar's range, removed from the noise of open and close prices.

Next, the indicator applies two simple moving averages:
- **SMA(5)** of the midpoint: the short-term average, reacting quickly to recent bars.
- **SMA(34)** of the midpoint: the long-term average, moving slowly and representing the baseline momentum.

The Awesome Oscillator is the difference: **AO = SMA(5) − SMA(34)**.

When the short average is above the long average, momentum is positive (AO bar is green, above zero). When the short average is below the long average, momentum is negative (AO bar is red, below zero). The distance between the two averages tells you the magnitude of the momentum shift.

This construction is simpler and more transparent than indicators like MACD, which use exponential averages. The 5 and 34 period choices are arbitrary but traditional—Bill Williams published them, they became standard, and they have proven robust across decades of trading. Some traders customize to 5 and 35, or 4 and 32, with minimal practical difference.

## The saucer setup: momentum acceleration into trend reversal

The most famous Awesome Oscillator pattern is the **saucer**—a sequence of three bars where the AO bars are all above (or below) the zero line and form a U-shape (for bullish) or inverted U (for bearish). The pattern signals momentum acceleration into a potential trend reversal.

**Bullish saucer** (entry setup for a long):
1. AO is below zero and red (negative momentum).
2. Bar 1 of saucer: AO rises but stays below zero (still red, but rising).
3. Bar 2 of saucer: AO rises further and crosses above zero (turning green).
4. Bar 3 of saucer: AO continues higher (green bar, confirming acceleration).

The saucer tells a story: momentum was negative, but the short average is catching up to the long average and is about to cross above it. This coincides with price typically finding a bottom or consolidation zone. The instant the AO crosses zero (bar 2), momentum has flipped—the short average is above the long average for the first time in several bars.

A trader using the saucer setup would enter a long on bar 3 or on the first close above resistance (often the high of bar 2). The setup is specific and visual, reducing false signals compared to a general "AO above zero" signal.

**Bearish saucer** mirrors this:
1. AO is above zero and green.
2. Bar 1: AO falls but stays above zero (still green, but declining).
3. Bar 2: AO falls and crosses below zero (turning red).
4. Bar 3: AO continues lower (red bar, confirming deceleration into downtrend).

The saucer is much stronger than a raw zero-line cross because it captures momentum acceleration, not just reversal. Price reversals often fail in the first bar or two; the continuation into bar 3 confirms the shift is real.

## Zero-line crossings: simple momentum regime change

While the saucer is the named setup, the **zero-line crossing** is the mechanical heart of AO trading. When AO crosses from negative to positive, the 5-period average has just crossed above the 34-period average—momentum's direction has flipped. When it crosses from positive to negative, the reverse has happened.

Unlike the saucer, which waits for confirmation, a zero-line cross is a raw signal. AO crosses above zero → buy. AO crosses below zero → sell or exit longs. This is simpler but noisier; in choppy markets, the zero line is crossed repeatedly, generating whipsaws.

The saucer pattern occurs at a zero-line crossing but filters for acceleration (all three bars continuing in the same direction). This dramatically improves signal quality. Roughly 60–70% of raw zero-line crossings result in a real follow-through move, while 80–90% of saucer patterns do (depending on timeframe and market).

## Divergence signals: when momentum diverges from price

Momentum oscillators often signal tops and bottoms through divergence—price makes a new high or low, but the oscillator does not. The Awesome Oscillator is no exception.

**Bullish divergence** (often precedes a reversal higher):
- Price makes a lower low (falls below a prior swing low).
- Awesome Oscillator makes a higher low (the red bars in the dip are less negative than before).

This signals that despite the lower price, momentum is improving—the short average is less far below the long average than it was. Buyers are stepping in earlier in the dip.

**Bearish divergence** (often precedes a reversal lower):
- Price makes a higher high (rallies above a prior swing high).
- Awesome Oscillator makes a lower high (the green bars in the rally are less positive than before).

Price is reaching new highs, but momentum is weakening—the short average is not pulling as far ahead of the long average. Sellers are appearing earlier in the rally.

Divergences are qualitative—they require visual inspection to spot. They are not as objective as the saucer or zero-line patterns, so they are better used as additional confirmation rather than standalone signals. Many false divergences occur in choppy markets where price whipsaws and the oscillator doesn't yet confirm.

## Comparing Awesome Oscillator to MACD and ROC

The Awesome Oscillator occupies the middle ground between ROC (Rate of Change) and MACD. ROC compares current price to a fixed past bar; MACD uses exponential averages of price. The Awesome Oscillator uses simple averages of the range midpoint.

ROC is faster and noisier. MACD is smoother and more popular across institutional platforms. The Awesome Oscillator is in between—fast enough to catch intraday swings, smooth enough to filter some choppy noise, and visual enough (histogram bars) to highlight saucer patterns intuitively.

In terms of predictive power, they are roughly equivalent. Choosing between them is more about familiarity and community than about objective superiority. Swing traders who learned Bill Williams' systems use AO. MACD users rarely switch.

## Sensitivity to timeframe and volatility

Like all moving-average-based oscillators, the Awesome Oscillator responds to timeframe. On a 1-minute chart, the 5-period average covers 5 minutes of data, and the 34-period average covers 34 minutes. On a daily chart, they cover 5 and 34 days.

The result is that AO is "slow" on intraday timeframes (1–5 minute) because the moving averages are still relatively long. Many intraday traders using AO shorten to 4 and 20 periods, or 3 and 15, to get faster reactions. The key is maintaining the ratio and the principle—a short and long average of the midpoint.

Volatility also affects AO. In a volatile market where the range (high minus low) expands, the midpoint swings further, and the moving averages react more sharply. In a calm market with tight ranges, the AO may stay near zero for days, generating few signals. This is not a flaw—it reflects true momentum—but it means AO is less useful in low-volatility consolidations.

## Practical trading with the Awesome Oscillator

Most traders combine the AO with price action. The saucer or zero-line cross signals the setup, but price must confirm. If AO shows a bullish saucer but price is making lower lows, the signal is weakened. If AO's saucer occurs at a support level (from prior swings or a moving average), the confluence is strong.

A typical workflow:
1. Scan for saucer patterns on your primary timeframe (daily, 4-hour).
2. Confirm with price structure (support, resistance, failed prior swing).
3. Enter on bar 3 of the saucer or on the first breakout of the saucer's high (bullish) or low (bearish).
4. Exit when AO crosses back through zero (first warning) or when price invalidates the setup (breaks below support).

Zero-line crossings alone produce more false signals and are better used as confirmations of other indicators or price patterns rather than standalone entries.

## Limitations and when the Awesome Oscillator fails

In strong trending markets, AO stays in one direction (all green bars or all red bars) for weeks or months. It does not revert to zero—momentum doesn't "reset." This means AO is useless for timing entries in mid-trend (you'll only get whipsaw reversals). It shines at trend starts and reversals, not continuations.

In choppy, consolidating markets, saucers and zero-line crosses happen constantly, and most fail. The indicator generates noise, not signal. Filtering requires additional structure—volume, price pattern, support/resistance.

AO also lags sharp, gap-style moves. A stock gaps up 5% on open; AO's moving averages are still catching up. By the time AO reflects the gap, price is already 3–4% higher, and the early fill has been missed. This is why AO works better on bars of consistent duration (daily, 4-hour) than on sub-minute timeframes.

## See also

<div class="wiki-seealso">

### Closely related

- MACD Indicator — similar momentum construction using exponential averages
- Rate of Change (ROC) — simpler momentum measurement, faster and noisier
- Moving Averages — the SMA building blocks of AO
- [Momentum Oscillator Centerline Crossover](/momentum-oscillator-centerline-crossover/) — zero-line logic across oscillator families
- [RSI Period Settings: 14 vs 9](/rsi-period-settings-14-vs-9/) — oscillator sensitivity tuning

### Wider context

- Technical Analysis — overview of price-based analytical methods
- Divergence in Oscillators — top and bottom signaling across indicators
- Trend Confirmation and Reversal — when momentum shifts signal real changes
- Bill Williams' Trading Systems — context for AO within a broader methodology

</div>

---
title: "Kaufman Adaptive Moving Average vs EMA"
description: "KAMA adapts its responsiveness based on market volatility and noise, while EMA uses a fixed smoothing constant, making each suited to different trending conditions."
keywords:
  - kaufman adaptive moving average vs ema
  - kama indicator
  - adaptive moving average
  - ema vs kama
image: /svg/technical-analysis.svg
---

*The **Kaufman Adaptive Moving Average (KAMA)** adjusts its lag dynamically in response to trend direction and noise levels, while an **Exponential Moving Average (EMA)** applies a fixed smoothing factor regardless of market conditions. KAMA tends to grip trends tighter and produce fewer whipsaws in choppy markets; EMA responds faster in clean, directional moves but can lag during confusion.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">KAMA vs EMA — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">Adaptive lag outperforms fixed smoothing in choppy regimes.</div>

|   |   |
|---|---|
| **KAMA lag** | Adjusts based on efficiency ratio (trend vs noise) |
| **EMA lag** | Constant, depends on period alone |
| **KAMA in trends** | Responsive; follows cleanly |
| **KAMA in chop** | Flatter, less whipsaw; "sleeps" in sideways |
| **EMA in trends** | Fast and simple; good for fast exits |
| **EMA in chop** | Frequent false crosses; more losses |
| **Computational ease** | EMA is simpler; KAMA has multiple steps |
| **Typical KAMA period** | 10–50 (efficiency lookback 2–34) |
| **Typical EMA period** | 12, 26, 50, 200 |

</aside>

## The core difference: fixed versus adaptive

An EMA applies the same **smoothing constant** (alpha) to every bar. A 12-period EMA always assigns 15% weight to today's price and 85% to yesterday's EMA value. This consistency is elegant and fast; it's also inflexible. When price chops sideways, the EMA darts back and forth, generating false crosses against the price.

KAMA recalculates its lag based on the **efficiency ratio (ER)**, a measure of trend strength relative to volatility. On a clean uptrend, KAMA's smoothing constant rises, making it snappier. During choppy consolidation, KAMA's constant shrinks, and the line becomes nearly flat—a built-in noise filter.

## The efficiency ratio: KAMA's secret

The efficiency ratio is a simple fraction:

**ER = (Sum of absolute price changes over N periods) ÷ (Sum of absolute direction changes over N periods)**

- **Numerator:** how far price has moved overall (trend distance).
- **Denominator:** how much price bounced around (total volatility).

An ER close to 1.0 means price moved a long way with few reversals—a clean trend. An ER close to 0.0 means price went nowhere (many reversals, little net movement)—chop.

KAMA uses ER to modulate its smoothing constant between a **slow constant** (for noise) and a **fast constant** (for trends). When ER = 1, KAMA uses the fast constant. When ER = 0, KAMA uses the slow constant.

## KAMA's behavior in trending markets

In a strong uptrend with an ER near 1.0, KAMA adopts a fast smoothing constant (often equivalent to a 2-period or 5-period EMA). The line hugs the price closely and responds quickly to turns. Entry and exit signals arrive early.

The upside: you catch reversals sooner and stay in winning trades longer.

The downside: KAMA can still be whipsawed if the trend breaks suddenly. It's not a shield against reversals; it's just faster.

## KAMA's behavior in choppy markets

In a sideways or choppy range where ER is low (say, 0.3), KAMA's smoothing constant becomes very slow (equivalent to a 30-period or 50-period EMA). The line flattens. Price can oscillate around it without KAMA moving much.

This is the chief advantage: fewer false crosses. A trader holding a KAMA-based position filter will sit through small reversals without exiting. Only when the ER rises again—a genuine trend emerges—does KAMA accelerate and generate a fresh signal.

## When an EMA still wins

An EMA shines when:

1. **The market is already trending cleanly.** EMA's simplicity and speed feel natural; you don't pay a cognitive cost for KAMA's complexity.

2. **You want instant responsiveness.** A 12-period EMA reacts to every new bar; KAMA lags behind by definition because it recalculates ER first.

3. **You're trading very short timeframes (minutes, seconds).** KAMA's period parameters become unwieldy; EMA's fixed constant is easier to code and execute.

4. **You're comfortable with more entries and exits.** EMA's false signals can be a feature if you're scaling in and out or running a very short-term system.

## When KAMA wins

1. **Your market is choppy or choppy-trending.** Crypto, small-cap equities, emerging markets—anything with high noise—benefits from KAMA's adaptive lag.

2. **You want to reduce whipsaw losses.** KAMA's flattening in sideways markets keeps you out of countertrend noise.

3. **You're trading longer timeframes (4-hour, daily, weekly).** The efficiency ratio has more data to work with; KAMA's decisions are more statistically grounded.

4. **You use KAMA for trend filtering, not entry timing.** Confirming that a trend exists (KAMA rising or falling, price above/below KAMA) is a use case where KAMA excels over EMA.

## A practical comparison setup

Suppose you're trading a daily chart.

**EMA approach:** Use a 50-period EMA. Long when price is above the 50-EMA and the 50-EMA is rising. Short when price is below and the 50-EMA is falling. The setup is clear but generates frequent false signals in chop.

**KAMA approach:** Use a 50-period KAMA (with efficiency lookback of, say, 10 periods). Long when price is above the KAMA and the KAMA is rising, **and** the efficiency ratio is above 0.5 (confirming some trend exists). This added filter eliminates many chop-based false signals.

Or use both: KAMA as your primary trend filter, EMA as your entry trigger within confirmed KAMA trends. KAMA confirms direction; EMA times the dip.

## Calculation: a quick sketch

**EMA:** EMA(today) = Price(today) × alpha + EMA(yesterday) × (1 − alpha), where alpha = 2 ÷ (period + 1).

**KAMA:** 
1. Calculate efficiency ratio (ER).
2. Fastest constant = 2 ÷ (2 + 1) = 0.666.
3. Slowest constant = 2 ÷ (slowest period + 1).
4. Smoothed constant = ER × (fastest − slowest) + slowest.
5. KAMA(today) = Price(today) × smoothed constant + KAMA(yesterday) × (1 − smoothed constant).

Most modern charting platforms calculate KAMA automatically; understanding the logic is more useful than hand-computing it.

## Adapting parameters to your market

KAMA's flexibility is also a choice burden. Common parameter sets:

- **Fast KAMA (10-period lookback, 2–30 range for fastest/slowest):** Responsive; closer to EMA behavior.
- **Medium KAMA (20-period lookback, 2–50 range):** Balanced; good for daily timeframes.
- **Slow KAMA (34-period lookback, 2–100 range):** Smoothest; good for weekly/monthly and noisy assets.

Backtest a few combinations on your chosen market and timeframe. KAMA is powerful but requires tuning.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average Ribbon Explained](/moving-average-ribbon-explained/) — stacking multiple MAs to see trend texture
- [Moving Average Slope as a Trend Filter](/moving-average-slope-as-trend-filter/) — measuring MA angle for momentum confirmation
- [Ichimoku Cloud Trend Signals](/ichimoku-cloud-trend-signals/) — another adaptive system for trend and reversal
- [Historical Volatility](/historical-volatility/) — measuring price noise, which KAMA filters against

### Wider context

- [Momentum Investing](/momentum-investing/) — trend following and MA-based systems
- [Market Timing](/market-timing/) — entry and exit discipline
- [Value At Risk](/value-at-risk/) — quantifying losses from bad entries and false signals

</div>

---
title: "TEMA vs EMA: How Triple Smoothing Reduces Lag"
description: "TEMA removes lag through a triple-exponential formula but introduces overshoot. Learn the math and trade-off between responsiveness and false moves."
keywords:
  - tema vs ema lag reduction
  - triple exponential moving average
  - tema indicator
  - ema lag
  - smoothing overshoot
  - technical analysis lag
---

*The **TEMA vs EMA lag reduction** comparison reveals how a **triple exponential moving average** accelerates price tracking by subtracting lagged averages from the formula. TEMA responds 2–3 bars faster than a single EMA, but the acceleration introduces **overshoot**—the line overshoots price at turning points, generating false signals in choppy conditions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TEMA and EMA — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">TEMA cuts lag through derivative correction, but pays in overshoot cost.</div>

|   |   |
|---|---|
| **Formula** | EMA: exponential smoothing; TEMA: 3×EMA₁ − 3×EMA₂ + EMA₃ |
| **Lag reduction** | TEMA ~40–50% faster than EMA at same period |
| **Lag in bars (14-period)** | EMA: ~5.5 bars; TEMA: ~2.5 bars |
| **Overshoot tendency** | EMA: minimal; TEMA: moderate to high |
| **Calculation complexity** | EMA: simple; TEMA: requires three nested EMAs |
| **Whipsaw rate** | EMA: low; TEMA: higher in choppy markets |
| **Best use case** | TEMA: trend entry confirmation; EMA: trend filtering |

</aside>

## The mathematics: why TEMA cuts lag

A standard **EMA** at period 14 calculates a weighted average, with more recent bars weighted higher. The result is a smooth line that lags price by approximately 5.5 bars (half the period, as a rule of thumb).

**TEMA** (Triple Exponential Moving Average) uses three nested EMAs to correct that lag:

**TEMA = 3 × EMA₁ − 3 × EMA₂ + EMA₃**

where:
- EMA₁ = normal 14-period EMA of price
- EMA₂ = 14-period EMA of EMA₁
- EMA₃ = 14-period EMA of EMA₂

The formula subtracts the "doubly lagged" EMA₂ and adds back the "triply lagged" EMA₃. This structure approximates the first and second derivatives of price movement, effectively de-lagging the moving average. The result is a line that hugs price 2–3 bars faster than the original EMA.

For a 14-period setting:
- EMA lag: ~5.5 bars
- TEMA lag: ~2.5 bars
- Improvement: roughly 55% reduction

## Quantifying the lag reduction

A practical example on a daily chart during an uptrend:

| Bar | Price | 14-EMA | 14-TEMA | EMA lag | TEMA lag |
|-----|-------|--------|---------|---------|----------|
| 1   | 100   | 99.2   | 99.5    | —       | —        |
| 5   | 105   | 101.8  | 103.2   | ~3 bars behind | ~2 bars behind |
| 10  | 110   | 105.5  | 108.8   | ~4 bars behind | ~2 bars behind |
| 15  | 115   | 110.2  | 113.5   | ~5 bars behind | ~2.5 bars behind |

As price accelerates higher, the **EMA gradually catches up**, but at any given moment it is running 5+ bars slow. **TEMA reacts faster** because the formula de-lags the moving average mathematically. On a 1-hour chart, this 2–3 bar advantage translates to a few minutes—a critical edge in intraday trading.

## The overshoot problem

The speed of TEMA comes at a cost: **overshoot at turning points**.

When price reverses sharply, the derivative-based formula in TEMA overcompensates. The line can spike well ahead of price, then fall back. This creates false signals—a TEMA cross above price that looks like a breakout but reverses within a few bars.

Example: price rallies from 100 to 115 over 10 bars, then drops 5 points to 110. A 14-EMA will still be in the 109–112 range, trailing the move. A 14-TEMA might spike to 113–114 (overshoot), catching the rally but then whipping back as the reversal is confirmed. A trader using TEMA as a signal line sees a false crossover.

By contrast, a **standard EMA overshoots much less**. Its smoothing is inherently conservative, so turning points are gentler and fewer false signals occur. The trade-off is slower entry confirmation.

## Lag reduction vs overshoot in context

**Which is worse: lag or overshoot?**

- **Lag** (EMA problem): You miss the start of a move. You enter a trend 5 bars late, sacrificing the beginning of the profit.
- **Overshoot** (TEMA problem): You enter early, but the turn-around can eject you quickly. You accumulate whipsaws and false signal costs.

For trend-following, many traders prefer lag to overshoot. A slightly late entry into a strong trend often profits more than an early entry that whips out. For mean-reversion strategies, TEMA's overshoot is more tolerable—you're betting on the reversal, so overshoot signals the extreme you're trading against.

## Practical use cases for TEMA

**Best for TEMA:**
- **Intraday momentum entry** where you want to catch the first few bars of a move.
- **Trend acceleration confirmation** where TEMA crossing above EMA signals a trend strengthening.
- **Volatility spikes** where you want to capitalize on the first surge before reversal.
- **Short-term swing trading** on 4-hour and 1-hour charts where lag costs are high.

**Where TEMA struggles:**
- **Choppy, ranging markets** where overshoot produces constant false crossovers.
- **News-driven volatility** where price gaps and reverses rapidly.
- **Long-term position trading** where 2–3 bars of lag makes no difference to a weeks-long trend.

## Practical use cases for EMA

**Best for EMA:**
- **Trend filtering** where you want a non-responsive baseline ("price above 20-EMA = uptrend").
- **Crossover systems** where two EMAs (e.g., 8 and 21) signal changes smoothly.
- **Divergence detection** where you want robust, non-noisy reference.
- **Portfolio-level trend** on weekly or monthly charts where lag is irrelevant.

## Combining TEMA and EMA for signal generation

A hybrid approach uses **both indicators as a confirmation system**:

1. Use a longer **EMA (e.g., 21 or 34)** as a trend filter and support/resistance line.
2. Use a shorter **TEMA (e.g., 8 or 14)** for entry timing.
3. Trade entries where TEMA crosses in the direction of the EMA trend.

For example:
- Long signal: TEMA crosses above EMA while price is above the 21-EMA trend filter.
- Exit signal: TEMA closes back below EMA, or price breaks the 21-EMA trend filter.

This pairing reduces TEMA's false signals (because you require EMA confirmation) while preserving the lag-reduction benefit. You get roughly 70% of the speed gain with 30% of the whipsaw cost.

## Adjusting period for different timeframes

**TEMA period is timeframe-dependent:**

- **5-minute chart:** 5–7 period TEMA for intraday scalping.
- **1-hour chart:** 8–12 period TEMA for short-term swing entry.
- **4-hour chart:** 12–14 period TEMA for medium-term trend confirmation.
- **Daily chart:** 20–30 period TEMA for position entry, if used at all.

Shorter periods amplify the lag-reduction but increase overshoot. Many day traders use a 9-period TEMA as the entry signal and a 21-period EMA as the trend filter. Weekly traders often skip TEMA entirely and rely on EMA or [moving-average](/moving-average/) ribbons.

## When overshoot becomes an advantage

In **fast-moving, volatile trends** (e.g., breakout after earnings), TEMA's overshoot can be an asset. The line reaches the extreme first, signaling "something big is happening" before price fully moves. A trader can use TEMA overshoot as an early alert to switch into [Bollinger Bands](/bollinger-bands/) or ATR-based stops for the actual trade entry.

In **mean-reversion contexts**, TEMA's overshoot flags the overstretched move you want to fade. A spike in TEMA above price signals an exhaustion point, and the reversal is not a false signal—it's the exact opposite: it's the move you're trading against.

## See also

<div class="wiki-seealso">

### Closely related

- EMA indicator — Foundation of TEMA; simpler, lower-lag alternative
- [Moving average](/moving-average/) — General smoothing concepts and lag theory
- [Bollinger Bands](/bollinger-bands/) — Volatility context for TEMA overshoot
- MACD — Alternative derivative-based momentum indicator

### Wider context

- [Trend-following](/trend-following/) — Strategy class TEMA serves
- [Support and resistance](/support-and-resistance/) — Using TEMA as dynamic levels
- [DMI Plus and Minus](/dmi-plus-minus-directional-movement/) — Complementary directional filter
- [Supertrend vs Parabolic SAR](/supertrend-vs-parabolic-sar-comparison/) — Lag and overshoot in stop systems

</div>

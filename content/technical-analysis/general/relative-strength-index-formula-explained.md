---
title: "Relative Strength Index Formula Explained"
description: "How is RSI calculated? Step-by-step walkthrough of the relative strength index formula with worked numeric examples."
keywords:
  - rsi calculation formula
  - relative strength index formula explained
  - how to calculate rsi
  - average gain loss rsi
image: /svg/technical-analysis.svg
---

*The **Relative Strength Index (RSI)** is calculated by comparing the magnitude of recent gains to recent losses over a standard 14-period window, using a smoothed average that confuses many traders—this article walks through the math step-by-step with concrete numbers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">RSI Formula — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The RSI distills price momentum into a single 0–100 score.</div>

|   |   |
|---|---|
| **Period** | 14 bars (default; can be 7, 21, or custom) |
| **Range** | 0 to 100 |
| **Overbought signal** | RSI > 70 (often treated as reversal warning) |
| **Oversold signal** | RSI < 30 (often treated as reversal opportunity) |
| **Key complexity** | The "smoothed" average gain/loss uses an exponential moving average, not a simple mean |
| **Lag** | Moves slower than raw price; most responsive on the first bar |

</aside>

## The three-step formula

The RSI is built in three stages: calculate gains and losses, smooth them, then compute the ratio.

**Step 1: Identify gains and losses.** For each of the last 14 periods, record the price change. If price rises, that's a gain; if it falls, record a loss (as a positive number). If price is flat, both are zero.

**Step 2: Smooth the averages.** Sum the gains from all 14 periods and divide by 14. Do the same for losses. This gives an initial "simple average gain" and "simple average loss." 

Here's the confusing part: after the first calculation, subsequent periods use an exponential smoothing formula instead of a simple rolling average. Each new smoothed average is:

- **New Smoothed Gain** = (Previous Smoothed Gain × 13 + Current Gain) ÷ 14
- **New Smoothed Loss** = (Previous Smoothed Loss × 13 + Current Loss) ÷ 14

This weighting (13 and 14) gives the most recent bar less influence than a simple average would, which is why RSI lags behind raw price momentum.

**Step 3: Calculate RS and RSI.** The Relative Strength (RS) is:

RS = Smoothed Average Gain ÷ Smoothed Average Loss

Then convert to 0–100 scale:

RSI = 100 − (100 ÷ (1 + RS))

Or equivalently:

RSI = (RS ÷ (1 + RS)) × 100

## Worked example with 14 daily closes

Suppose we have 15 daily closes starting at 100:

| Day | Close | Change | Gain | Loss |
|-----|-------|--------|------|------|
| 1   | 100   | —      | —    | —    |
| 2   | 102   | +2     | 2    | 0    |
| 3   | 103   | +1     | 1    | 0    |
| 4   | 101   | −2     | 0    | 2    |
| 5   | 104   | +3     | 3    | 0    |
| 6   | 103   | −1     | 0    | 1    |
| 7   | 105   | +2     | 2    | 0    |
| 8   | 104   | −1     | 0    | 1    |
| 9   | 106   | +2     | 2    | 0    |
| 10  | 108   | +2     | 2    | 0    |
| 11  | 107   | −1     | 0    | 1    |
| 12  | 109   | +2     | 2    | 0    |
| 13  | 110   | +1     | 1    | 0    |
| 14  | 111   | +1     | 1    | 0    |
| 15  | 109   | −2     | 0    | 2    |

For day 15, we use days 2–15 (14 changes total).

Sum of gains = 2 + 1 + 0 + 3 + 0 + 2 + 0 + 2 + 2 + 0 + 2 + 1 + 1 + 0 = 16
Sum of losses = 0 + 0 + 2 + 0 + 1 + 0 + 1 + 0 + 0 + 1 + 0 + 0 + 0 + 2 = 7

Initial smoothed gain = 16 ÷ 14 = 1.14
Initial smoothed loss = 7 ÷ 14 = 0.50

RS = 1.14 ÷ 0.50 = 2.28

RSI = 100 − (100 ÷ (1 + 2.28)) = 100 − (100 ÷ 3.28) = 100 − 30.49 = **69.51**

An RSI of 69.51 sits just below the 70 overbought threshold, suggesting the rally may be losing steam—though that interpretation depends on [price action](/support-and-resistance/), volume, and the broader [trend](/momentum-investing/).

## Why the smoothing matters

Many textbooks state the formula but gloss over the exponential smoothing, which is why traders often replicate RSI values incorrectly in spreadsheets. The 13:14 weighting is arbitrary—Wilder, who invented RSI in 1978, chose it to roughly match the smoothing used in his [Average True Range](/volatility-smile/) indicator—but it does mean the RSI responds more slowly to sharp reversals than a simple 14-period momentum calculation would.

A price crash on day 15 that doubles losses will not immediately flip RSI from 69 to 30; the smoothed average loss rises gradually, so RSI declines over several bars instead of one.

## RSI across different periods

Traders adjust the period length for faster or slower signals. A 7-period RSI swings more wildly, crossing the 70 and 30 lines frequently—useful for [swing trading](/momentum-investing/) but prone to whipsaw in choppy markets. A 21-period RSI irons out noise and suits longer-term [trend-following](/trend-following/), but misses short-term reversals.

The calculation method remains identical; only the denominator changes (7 instead of 14, for instance), and the smoothing multiplier adjusts accordingly (6 instead of 13).

## Common pitfalls

**Treating 70/30 as buy/sell signals alone.** An RSI reading above 70 in a strong uptrend is not automatically a sell. Many rallies sustain RSI > 70 for weeks. Confirm with [price action](/support-and-resistance/) and volume.

**Ignoring divergence.** If price makes a new high but RSI fails to, that divergence—called [bearish divergence](/momentum-investing/)—often precedes reversals. Conversely, bullish divergence (price low, RSI high) can signal strength returning.

**Over-smoothing.** Using a 50-period RSI filters out so much noise that it lags price by 10+ bars, making it nearly useless for timing entries.

## See also

<div class="wiki-seealso">

### Closely related

- [Momentum Investing](/momentum-investing/) — using price and rate-of-change indicators to trade
- [Support and Resistance](/support-and-resistance/) — identifying price levels where reversals often occur
- [Moving Average](/moving-average/) — another smoothing technique used in technical analysis
- [Volatility Smile](/volatility-smile/) — how volatility varies with price levels

### Wider context

- Technical Analysis — price-based trading frameworks
- [Trend Following](/trend-following/) — profiting from sustained directional moves
- [Market Timing](/market-timing/) — the challenge of entry and exit decisions
- [Overconfidence Bias](/overconfidence-bias/) — the psychological pitfall of over-relying on single indicators

</div>

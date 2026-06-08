---
title: "Parabolic SAR Acceleration Factor"
description: "A parameter in Parabolic SAR that controls how aggressively the stop level accelerates toward price, tuning sensitivity to trend reversals."
keywords:
  - parabolic sar
  - acceleration factor
  - stop and reverse
  - trend reversal
  - trailing stop
  - extreme point
image: "/svg/technical-analysis.svg"
---

*The **Parabolic SAR Acceleration Factor** (SAR = Stop and Reverse) is a tuning parameter that governs how quickly the Parabolic SAR's stop level converges on price as an uptrend or downtrend accelerates. Traders adjust the initial step and maximum acceleration values to match market volatility and desired signal responsiveness, controlling the balance between early exits and whipsaw tolerance.*

## Parabolic SAR Basics

Parabolic SAR is a trend-following indicator that plots a trailing stop level beneath (in uptrends) or above (in downtrends) price. As the trend unfolds and makes new extremes, the stop accelerates toward price, tightening progressively. When price closes on the opposite side of the stop, the indicator reverses and flips the stop to the other side.

The stop's acceleration depends on two parameters: the **initial step** (often 0.02 or 2%) and the **maximum step** (often 0.20 or 20%). These values determine how fast the SAR converges as the trend proves itself.

## The Acceleration Mechanism

The SAR calculation follows this logic:

1. **Establish a trend and initial stop:** Place the SAR below price in an uptrend, above it in a downtrend.
2. **Track the Extreme Point (EP):** Record the highest price (in uptrends) or lowest price (in downtrends) seen since the trend began.
3. **Accelerate the SAR:** Each bar, increment the SAR toward price using: SAR(new) = SAR(old) + Acceleration × (EP − SAR).
4. **Cap the acceleration:** If acceleration rises above the maximum step, lock it at that maximum.
5. **Reverse on a close:** If price closes on the opposite side of the SAR, flip the trend and reset the acceleration to the initial step.

The acceleration factor itself starts at the initial step (e.g., 0.02) and increases by the step amount each time a new extreme point is set. This means a dynamic uptrend with multiple new highs will accelerate the SAR faster than a stalled or weak uptrend.

## Initial Step vs. Maximum Step

The **initial step** (e.g., 0.02) governs how quickly the SAR moves off the reversal point. A value of 0.02 means the stop moves 2% closer to price each bar, assuming no new extremes. This slow initial pace helps traders exit gracefully without whipsaw on minor pullbacks.

The **maximum step** (e.g., 0.20) caps the acceleration. Once reached, the SAR can move at most 20% per bar toward price. This prevents the SAR from accelerating so aggressively that it almost touches the current bar, which would cause immediate reversals and false signals.

## Tuning the Parameters

**Standard settings (0.02 initial, 0.20 max):** Designed for daily charts and moderate timeframes. Often a good starting point; strikes a balance between early trend capture and avoiding constant reversals.

**More aggressive (0.03–0.05 initial, 0.25–0.30 max):** Better for fast-moving markets and intraday timeframes. The SAR closes the gap to price more quickly, generating earlier exit signals and faster reversals when the trend breaks. Useful for traders who prefer tight stops and frequent signal changes.

**More conservative (0.01 initial, 0.10–0.15 max):** Suits slower markets and position trading. The SAR accelerates very slowly, allowing for deeper retracements before reversing. Useful for traders who want to stay in trends longer, even if it means tighter stops when reversals finally arrive.

## Parabolic SAR as a Trailing Stop

Parabolic SAR's most popular application is as an automatic trailing stop loss. Enter a long trade when SAR reverses to an uptrend; place a sell stop at the SAR level. As price climbs and new highs are set, the SAR automatically adjusts upward, protecting profits while leaving room for the trend to run.

The acceleration factor controls how aggressively the stop tightens. A 0.02/0.20 setting gives the trend room to breathe; a 0.05/0.30 setting locks in gains faster but risks exiting before the trend exhausts itself.

## Practical Examples

**Swing trading:** A trader enters a long position when SAR flips from downtrend to uptrend. Using 0.02/0.20 parameters, the SAR sits 3–5% below price initially, rising gradually. Each new swing high accelerates the SAR closer, tightening the stop as the trend strengthens. If price closes below the SAR on a pullback, the trade exits with a mechanical signal—no discretion needed.

**Intraday scalping:** A 5-minute chart with 0.04/0.25 parameters produces faster signals. The SAR closes to price more aggressively, exiting small gains quickly and re-entering on the next reversal. This suits traders who want frequent small winners over occasional large ones.

**Position trading:** On a weekly chart, 0.01/0.10 parameters allow the SAR to lag price by 10–15%, accommodating multi-week trends. Reversals are rare and come only after substantial breaks in the trend structure.

## When SAR Reverses

A SAR reversal signals a trend exhaustion. In a long trade, when price closes below the SAR (and the SAR crosses above price), the indicator declares the uptrend over and flips to a downtrend. The SAR then sits above price and begins descending, ready to catch a short entry or confirm an exit.

The **Extreme Point resets** on reversal. If an uptrend reverses to a downtrend, the new EP becomes the highest price seen during that uptrend. The acceleration drops back to the initial step, so the new downtrend SAR accelerates slowly at first and only speeds up if new lows are broken.

## SAR Pitfalls and Limitations

**Whipsaw in choppy markets:** When price oscillates without a clear trend, SAR reverses repeatedly, generating many false signals. Traders often filter reversals with volume (only trade reversals on volume spikes) or RSI (only trade if RSI is not already extreme).

**Lag in explosive gaps:** If price gaps past the SAR (e.g., a stock gap-up on earnings), the indicator flips immediately without giving the trader a chance to exit at a reasonable price. In gap-prone securities, some traders reduce maximum step or use mental stops independent of SAR.

**No volatility adaptation:** Unlike ATR-based indicators, Parabolic SAR does not adjust its step values based on volatility. A quiet stock and a volatile stock with the same parameters will behave very differently. Traders often manually adjust the max step higher for volatile names and lower for stable ones.

**SAR as entry signal:** Traders often misuse SAR as a primary entry trigger. SAR reversals are better suited as exit signals. For entries, combine SAR with price action, support and resistance levels, or [DEMA crossovers](/dema-double-ema/) to filter the direction.

## Optimization and Market Adaptation

Many traders test Parabolic SAR parameters across a range of historical data to find settings that produce the best win rate on their target market. A stock that trends cleanly might profit from 0.05/0.25 (aggressive). A choppy, range-bound asset might do better with 0.01/0.08 (conservative).

Some systems backtest across multiple parameter sets and automatically switch based on recent volatility. If ATR is high, they increase the max step; if ATR is low, they decrease it. This keeps SAR responsive to current market conditions.

## See also

<div class="wiki-seealso">

### Closely related

- Average True Range (ATR) — volatility measure that some traders use to set SAR parameters dynamically
- [Supertrend Indicator](/supertrend-indicator/) — similar trend-following indicator using ATR bands; often compared to SAR
- [Moving Average](/moving-average/) — simpler trend filter; sometimes combined with SAR for confirmation
- Stop Loss — how to set and use SAR as a dynamic trailing stop
- Support and Resistance — levels where SAR often aligns with key price structure

### Wider context

- Technical Analysis — chart-based trading methods
- [Trend Following](/trend-following/) — systematic approach that Parabolic SAR anchors
- Price Action — manual chart reading paired with SAR signals
- Volatility — how market regime affects SAR parameter choice

</div>

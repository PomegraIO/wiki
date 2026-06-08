---
title: "Detrended Price Oscillator vs MACD"
description: "Detrended Price Oscillator isolates cycles by removing trend, while MACD follows momentum; each serves different market conditions and trader goals."
keywords:
  - detrended price oscillator vs macd
  - dpo oscillator
  - macd momentum
  - trend vs cycle trading
  - technical analysis comparison
image: "/svg/technical-analysis.svg"
---

*The **Detrended Price Oscillator** (DPO) and **MACD** are both built on moving averages but serve opposite analytical purposes. DPO strips away the trend to expose hidden cyclical patterns within a larger move, while MACD tracks trend momentum directly. Choosing between them hinges on whether you're hunting for reversals within a trend or confirming the trend's direction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DPO vs MACD — Key Differences</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One removes trend to find cycles; the other follows trend itself.</div>

|   |   |
|---|---|
| **Detrended Price Oscillator** | Removes trend; isolates cyclical swings |
| **MACD** | Follows momentum; confirms trend direction |
| **DPO signal type** | Overbought/oversold swings, reversal timing |
| **MACD signal type** | Crossovers; trend strength changes |
| **Best in** | Range-bound, cyclical markets |
| **Best in** | Strong trending markets |
| **Lag characteristic** | Intentional; aligns bars with cycles |
| **Lag characteristic** | Inherent; trade-off for smoothing |

</aside>

## How DPO Removes Trend

The Detrended Price Oscillator subtracts a displaced moving average from the current price. "Displaced" means the moving average is shifted backward (e.g., instead of using the last 21 days' prices, it uses the 21 days before that). This deliberate lag aligns the moving average with the midpoint of the cycle you're analyzing, revealing the price swings around the trend without showing the trend itself.

The result is an oscillator that oscillates around zero, swinging above zero when price is stronger than the detrended average and below when price is weaker. Because the trend is removed, the DPO can't tell you whether the overall market is up or down—only whether price is locally hot or cold relative to its cycle.

This design makes DPO particularly useful in markets that are cycling up and down within a broader range. A trader might use DPO to identify the peak of a short-term rally (when DPO is at an extreme high) and then fade it, or identify the trough (DPO at an extreme low) and buy the rebound.

## How MACD Follows Momentum

MACD subtracts a 26-period exponential moving average (EMA) from a 12-period EMA. Both moving averages follow the trend; the difference between them measures how quickly momentum is changing. When the 12-period EMA is well above the 26-period EMA, momentum is strong and upward. When the 12-period EMA is below the 26-period EMA, momentum is slowing or reversing downward.

MACD's signal line—a 9-period EMA of MACD itself—creates a momentum-following oscillator that generates crossover signals. A bullish signal occurs when MACD crosses above its signal line; a bearish signal when it crosses below.

Because both EMAs follow the trend, MACD rises in uptrends and falls in downtrends. It can't tell you when a trend is exhausted on its own; it only confirms that momentum is accelerating or decelerating. For trend traders, that's the whole point.

## DPO in Practice: Catching Reversals Within a Move

Suppose the S&P 500 is in a sustained uptrend but price has jumped 8% in two weeks. A trader using DPO might notice that the oscillator is at an extreme high—a signal that the short-term cycle within this longer uptrend is overbought. Rather than trying to pick the exact reversal bar, the DPO user can place a contrarian short-term trade or tighten stops, betting on a pullback.

DPO shines in sideways or gently sloping markets where cycles repeat frequently. A stock oscillating between $50 and $60 will produce clear DPO extremes at the top and bottom of each swing. A trader can fade the tops and buy the bottoms, riding the cycle.

The downside: DPO is unhelpful in strong directional markets. If a stock is in a relentless uptrend, DPO will keep bouncing off its zero line from above—not useful for a breakout trader. And because DPO's displacement introduces lag, it may signal an overbought swing just as the trend accelerates further.

## MACD in Practice: Confirming and Timing Trend Changes

A trader watching a stock consolidate on declining MACD (momentum weakening even though price holds its ground) might be on high alert for a reversal. When MACD finally rolls over and crosses below its signal line, it confirms that the rally is exhausted. That signal, combined with a close below support, triggers a short trade.

Conversely, MACD climbing into positive territory and crossing above its signal line—especially while price is above a key moving average—signals that a new uptrend is underway. A buyer can enter with confidence, knowing momentum is in their favor.

MACD is the go-to tool for traders who want to follow the trend, not fight it. It works best when markets are trending and trending hard. In choppy, range-bound environments, MACD flips back and forth across the zero line, generating false signals. That's where DPO excels.

## Combining Both Tools

Some traders use both indicators in tandem. Use [MACD](/how-to-read-macd-crossover/) to confirm the direction of the trend; use DPO to spot the moments within that trend where price is stretched and likely to pull back. 

For example: MACD confirms an uptrend (crossing above its signal line on a close above a 50-day EMA). Price runs up 5%, and DPO hits an extreme high. The trader tightens stops or takes partial profits, expecting a pullback. If the uptrend is healthy, price will dip, DPO will fall back toward zero, and the trader can add back to the position.

This approach avoids fighting the trend (MACD's job) while capturing short-term reversals within the trend (DPO's job).

## Context: When Each Tool Shines

Use DPO when markets are range-bound or cycling—when the dominant price pattern is oscillation rather than breakout. Use it to spot overbought and oversold extremes within a broader move. DPO is less useful in strong breakout markets where trend exhaustion is measured in weeks, not days.

Use MACD when you're trading breakouts or sustained trends. MACD confirms the start of a new trend direction and warns when momentum is faltering. MACD is less useful in choppy, directionless markets where momentum keeps reversing without generating sustainable moves.

For swing traders working multi-day timeframes, combining both can be powerful: MACD guides the direction, DPO guides the timing. Neither is perfect on its own, but together they cover each other's blind spots.

## See also

<div class="wiki-seealso">

### Closely related

- [How to Read a MACD Crossover](/how-to-read-macd-crossover/) — MACD signals and trend confirmation
- [TRIX Indicator: Triple-Smoothed EMA Momentum](/trix-indicator-triple-smoothed-ema/) — Another trend-following momentum oscillator
- [Momentum Indicators for Swing Trading](/momentum-indicator-for-swing-trading/) — Comparing RSI, Stochastic, and other oscillators
- [Moving Average](/moving-average/) — Foundations of trend-following tools
- Overbought and Oversold — Interpreting extreme oscillator readings

### Wider context

- Technical Analysis — Overview of price and momentum analysis
- [Algorithmic Trading](/algorithmic-trading/) — Systematic signal generation
- [Volatility Smile](/volatility-smile/) — Market regime and uncertainty

</div>
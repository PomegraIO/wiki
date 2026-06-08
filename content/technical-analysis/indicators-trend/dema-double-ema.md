---
title: "Double Exponential Moving Average"
description: "A trend-following indicator that applies exponential smoothing twice to cut response lag in half compared to standard EMAs."
keywords:
  - dema
  - exponential moving average
  - trend following
  - technical analysis
  - moving average lag
  - price momentum
image: "/svg/technical-analysis.svg"
---

*The **Double Exponential Moving Average** (DEMA) is a smoothed-trend indicator that halves the lag of a conventional [exponential moving average](/exponential-moving-average/) by subtracting a second EMA pass from the first. Introduced by trader Patrick Mulloy in 1994, DEMA responds faster to price changes while still filtering noise, making it popular with swing traders and momentum-following systems.*

## How DEMA Construction Works

DEMA is built from two exponential moving averages calculated in sequence:

1. Calculate a standard EMA over the chosen period (e.g., 21 bars).
2. Calculate a second EMA of that first EMA (EMA of EMA).
3. Subtract the second EMA from the first and double the result.

In formula form: DEMA = (2 × EMA) − EMA(EMA).

This double subtraction removes the lagging component introduced by exponential smoothing. A standard EMA lags price because it assigns more weight to recent bars while still including older prices. By using the rate of change between the first and second smoothing, DEMA "predicts" where the average is heading and pulls the trend line forward.

The result is a line that hugs turning points much more tightly than a single EMA—making it far more responsive to shifts in momentum direction.

## Why Traders Choose DEMA Over Simple EMAs

The practical advantage is speed. A 21-period EMA on a daily chart might lag price turns by 2–3 bars. A 21-period DEMA often catches the same turn within 1 bar, or even within the current candle on intraday charts. For swing traders using [price-discovery](/price-discovery/) and breakout signals, that extra responsiveness can mean entry fills much closer to actual trend reversals.

The trade-off is slight—DEMA is more whipsaw-prone than a single EMA because it's sharper. In choppy, sideways markets, a DEMA will generate more false signals. Traders typically combine DEMA with confirmation filters: a check that price is above or below an ATR band, a second moving average, or a [momentum indicator](/momentum-trading/) like RSI to reduce noise.

## Practical Use Cases

**Swing trading entries:** A DEMA crossover below support often marks the start of a downtrend before a standard EMA breaks that level. Traders use this earlier signal to establish short positions or tighten stops on long entries.

**Trend confirmation:** Two DEMAs plotted at different periods (e.g., 13 and 34) create a faster version of the common two-line moving average system. Crossovers above or below one another confirm trend shifts without the lag of longer EMAs.

**Scalp and intraday:** On 5- or 15-minute charts, a single DEMA often replaces a slower triple-EMA setup, cutting response time significantly while keeping the visual clean.

## DEMA Across Timeframes

DEMA behaviour varies with the lookback period:

- **Shorter periods** (8–13 bars): Highly responsive but prone to whipsaw. Best used in strong trends or with aggressive profit-taking discipline.
- **Medium periods** (20–34 bars): The sweet spot for many swing traders; balances response speed with enough filtering for reliable [sector rotation](/sector-rotation/) or mean-reversion plays.
- **Longer periods** (50+ bars): Functions as a slower trend line; less whipsaw but also less responsive to early-stage reversals.

The effective lag depends on volatility and market regime. In sideways markets, DEMA may oscillate around price; in trending markets, it forms clean support or resistance.

## Common Pitfalls

Many traders believe DEMA is a standalone signal. It is not. A DEMA rising alone does not confirm a buy; instead, look for price to cross above DEMA, or for DEMA to flatten after a steep climb (signalling loss of momentum). Likewise, a falling DEMA does not guarantee a sell—pair it with volume, RSI extremes, or resistance levels to filter false breaks.

DEMA can also lag in highly gapped or limit-move markets, where price jumps past the indicator before the EMA recalculation captures the move. In such cases, traders often revert to simpler tools or order-flow analysis.

## Variants and Customisation

Some traders use **triple EMAs** (TEMA), applying the subtraction logic a third time to cut lag even further—but at the cost of increased whipsaw. Others blend DEMA with the original EMA in a weighted average to find a middle ground between speed and reliability.

Indicator platforms like TradingView allow users to adjust the EMA period and apply DEMA to non-price data: volume, ATR, or RSI. A DEMA of volume, for instance, can highlight when momentum is accelerating or fading beneath price moves.

## See also

<div class="wiki-seealso">

### Closely related

- [Exponential Moving Average](/exponential-moving-average/) — the single-pass smoothing that DEMA improves upon
- ATR-Volatility Bands — confirmation filter to reduce DEMA whipsaw in choppy markets
- [Moving Average Crossover](/moving-average-crossover/) — two-line systems using DEMA for faster signal generation
- [Momentum Trading](/momentum-trading/) — using DEMA with rate-of-change filters to confirm trend strength

### Wider context

- Technical Analysis — overview of chart-based trading methods
- [Trend Following](/trend-following/) — systematic approach that often anchors on moving averages like DEMA
- [Price Discovery](/price-discovery/) — how indicators like DEMA identify early trend shifts
- Support and Resistance — levels where DEMA often acts as dynamic support or resistance

</div>

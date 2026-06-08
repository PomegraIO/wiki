---
title: "Supertrend Indicator"
description: "An ATR-based indicator that generates buy and sell signals by comparing price to adaptive volatility bands that flip between uptrend and downtrend states."
keywords:
  - supertrend
  - atr bands
  - trend indicator
  - volatility bands
  - buy sell signals
  - average true range
image: "/svg/technical-analysis.svg"
---

*The **Supertrend** is a trend-following indicator that wraps Average True Range (ATR) around a moving average, producing clean directional signals when price crosses bands that flip between "buy" and "sell" states. Popular for its simplicity and low lag, Supertrend is widely used in algorithmic trading, swing systems, and even long-term position management.*

## How Supertrend Calculates

Supertrend starts with two basic inputs:

1. A lookback period for ATR and the moving average (commonly 10 bars).
2. A multiplier for the ATR distance (typically 3.0).

The indicator then calculates:

- **Basic Upper Band** = (High + Low) / 2 + (Multiplier × ATR)
- **Basic Lower Band** = (High + Low) / 2 − (Multiplier × ATR)

These bands are the HL/2 midpoint (similar to a simple moving average of highs and lows) offset by a volatility-adjusted distance. The final upper and lower bands are then "finalized" by ensuring they never move against the trend—the upper band ratchets down if price closes below it, and the lower band ratchets up if price closes above it.

The indicator then assigns a state: if the final band is below price, the trend is "up" (bullish); if above, it's "down" (bearish). A signal fires when price crosses from one side to the other.

## Clean Entry and Exit Signals

Supertrend's main appeal is its binary nature. Unlike [moving averages](/moving-average/) or [DEMA](/dema-double-ema/) that remain on one side of price, Supertrend's bands flip to act as both support (in uptrends) and resistance (in downtrends). This produces clear rules:

**Buy signal:** When price closes above the lower band and the indicator flips to an uptrend state.

**Sell signal:** When price closes below the upper band and the indicator flips to a downtrend state.

No ambiguity, no interpretation—the signal is a crossover. For algorithmic traders and systematic players, this clarity is invaluable. For discretionary traders, it offers a mechanical anchor that reduces emotion and overthinking.

## Adjusting the Multiplier

The ATR multiplier controls how tight or loose the bands sit:

- **Multiplier 2.0–2.5:** Very tight bands; frequent signals but more false breaks. Suits volatile, choppy markets where mean reversion trades are common.
- **Multiplier 3.0:** The standard; strikes a balance. Works well in trending markets and most timeframes.
- **Multiplier 4.0–5.0:** Loose bands; fewer signals, higher win rate, but may miss early-stage trend moves. Better for longer timeframes or position traders content to enter late.

Higher multipliers also produce deeper retracements before reversal signals—useful for traders who want to see strong confirmation before abandoning a trend. Lower multipliers catch nearly every minor pullback, which can backfire in choppy conditions.

## Why ATR Matters

Using ATR instead of fixed bands or standard deviation means the bands automatically widen during volatile periods and contract when price is calm. This adaptive feature helps Supertrend avoid false signals in quiet markets (where tight bands would whip) and avoid over-tightening during explosions (where loose bands would flatten the signals).

A quiet, low-volatility consolidation produces narrow bands that turn and reverse quickly. An explosive breakout widdens the bands, allowing price room to trend before hitting a reversal signal. This behaviour aligns well with how traders actually manage risk: tighter stops in calm markets, wider ones in volatile runs.

## Practical Use Across Timeframes

**Daily charts (swing trading):** A 10-period Supertrend with 3.0 multiplier often marks swing-level support and resistance. Traders use crossovers as entries and watch for second touches of the band as risk points.

**1-hour and 4-hour charts (intraday):** Supertrend excels on medium-term intraday timeframes. The signals are responsive enough to catch momentum shifts within a session, yet filtered enough to avoid scalp-level noise.

**15-minute charts (scalping):** A 5–7 period Supertrend works here, but increasing the multiplier to 3.5–4.0 helps cut false signals inherent to low-timeframe volatility.

**Weekly charts (position trading):** A 14–20 period Supertrend serves as a macro-trend filter. Many traders use a weekly Supertrend to confirm the long-term direction before taking trades on shorter timeframes.

## Supertrend as a Trailing Stop

Many traders use the Supertrend band as a dynamic stop loss. In an uptrend, they place a sell stop just below the lower band; if price closes below it, they exit the position. This avoids the rigidity of fixed-dollar or percentage stops and automatically adjusts as volatility shifts.

For trend-following systems, this approach reduces the need to manually adjust stops. The indicator does it automatically based on ATR, so stops widen in explosive rallies and tighten as volatility settles.

## Common Pitfalls

**Over-trading on false breaks:** Supertrend can whipsaw in sideways markets. When price oscillates around the midline, bands flip rapidly. Traders should filter signals with volume (only trade breaks on high volume) or confirm with RSI extremes or other momentum indicators.

**Lag on very fast moves:** In gap-limit moves or flash crashes, Supertrend may be rendered obsolete. ATR takes 10 bars (or whatever period is set) to calculate; if price jumps 5% overnight, the band recalculates with a huge gap already baked in. In such cases, revert to support and resistance levels or price-action analysis.

**Period and multiplier mismatch:** A very short period (e.g., 5 bars) with a high multiplier (e.g., 5.0) produces nearly flat bands that don't signal often enough. Conversely, a long period (e.g., 30 bars) with a low multiplier (e.g., 2.0) generates false breaks constantly. Tune the parameters to your timeframe and market regime.

## Supertrend + Confirmation

Sophisticated traders combine Supertrend with a secondary filter. For example:

- Trade Supertrend crossovers only if the [50-period EMA](/exponential-moving-average/) is also in the same direction (EMA above price for uptrends, below for downtrends).
- Ignore Supertrend sell signals if RSI is below 30 (oversold, likely to bounce).
- Require volume to be above its 20-period average before taking a signal.

These additions reduce whipsaw without removing the mechanical clarity Supertrend provides.

## See also

<div class="wiki-seealso">

### Closely related

- Average True Range (ATR) — the volatility input that sizes Supertrend bands
- [Moving Average](/moving-average/) — simpler trend tool; Supertrend adds ATR bands for entry and exit
- [DEMA (Double Exponential Moving Average)](/dema-double-ema/) — faster-responding trend line; often used alongside Supertrend for confirmation
- [Linear Regression Channel](/linear-regression-channel/) — statistical trend bands; less responsive than Supertrend but potentially more robust
- Support and Resistance — static levels that Supertrend bands often align with

### Wider context

- Technical Analysis — chart-based trading foundations
- [Trend Following](/trend-following/) — systematic approach that Supertrend anchors
- Stop Loss — how to use Supertrend bands as dynamic exits
- Price Action — manual chart reading that complements Supertrend signals

</div>

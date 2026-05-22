---
title: "Williams %R Indicator"
description: "Overbought-oversold momentum oscillator tracking price position within recent trading range."
keywords:
  - williams r
  - overbought oversold
  - momentum indicator
  - technical analysis
  - stochastic
  - oscillator
---

*The **Williams %R** (Williams Percent Range) is a momentum oscillator that measures where the current closing price sits within the highest high and lowest low of a lookback period. Priced between 0 and −100, it identifies overbought and oversold conditions in equities and commodities.*

<aside class="wiki-infobox">

| Metric | Value |
|--------|-------|
| **Range** | −100 to 0 |
| **Typical Lookback Period** | 14 bars |
| **Overbought Threshold** | −20 or above |
| **Oversold Threshold** | −80 or below |
| **Interpretation** | Mean-reversion / extremes signal reversal risk |
| **Best For** | Equities, forex, commodities |
| **Creator** | Larry Williams (1973) |

</aside>

## What the %R measures

Williams %R is the inverse of the [stochastic oscillator](/wiki/stochastic-oscillator/) — same concept, inverted scale. It calculates:

```
%R = −100 × (Highest High − Close) / (Highest High − Lowest Low)
```

Over a typical 14-bar window, if price closes at the *highest* high, %R = 0. If it closes at the *lowest* low, %R = −100. Mid-range closes register between these poles. The inversion (0 to −100 rather than 0 to 100) was Williams' choice; both forms track identical momentum.

## Why traders use extremes to time entries

When %R approaches −20, the close has compressed into the *upper* band — signal of overbought price. Many traders treat this as a warning flag for potential pullback or short entry. Conversely, %R below −80 signals oversold conditions, where [mean reversion](/wiki/mean-reversion-investing/) trades expect a snap-back higher.

The key assumption: extreme closes relative to recent range reflect temporary excess, not sustainable trend. A stock that touches −20 within minutes may reverse by day's end; one stuck above −30 for a week suggests trend strength and breaks the overbought signal. Context matters.

## Comparison to stochastic

[Stochastic oscillators](/wiki/stochastic-oscillator/) and Williams %R are near-identical mechanics — Larry Williams designed %R partly in response to stochastic criticism. Both use a 14-period high-low range. The practical difference:
- Stochastic adds a smoothed moving average (K-line and D-line), which filters noise but lags signal.
- Williams %R is the raw calculation, more reactive but noisier.

Traders choose based on tolerance for false signals. Slower stochastic suits swing traders holding days or weeks; raw Williams %R works for intraday scalpers.

## When %R fails to predict reversals

Pure overbought-oversold signals are unreliable in [strong uptrends](/wiki/bull-market/) or [downtrends](/wiki/bear-market/). During a sustained rally, a stock may stay above −30 for weeks while continuing to climb — the "overbought" label masks accelerating momentum. Similarly, in washouts, oversold reads persist as price plummets further.

This blind spot is why skilled traders use Williams %R **in combination with trend confirmation**. A −80 read in a downtrend is less trustworthy than a −80 read after a sharp intraday spike following a calm period. [Price action](/wiki/price-discovery/), volume, and broader market context are the filters.

## Interpretation across timeframes

A 14-bar Williams %R on a daily chart captures extreme closes within the last ~2–3 weeks of trading. The same instrument on a 1-minute chart captures ~14 minutes of price action. This matters: a −20 reading on the minute chart is not the same as −20 on the daily. Intraday traders use shorter periods (5–10 bars); swing and position traders use 14–21 bars.

## Practical use in entry and exit logic

Many traders weave Williams %R into decision rules:

- **Entry trigger**: Buy at %R = −80 after a multi-day sell-off in an otherwise healthy stock, on the assumption of quick mean-reversion bounce.
- **Exit signal**: Close a [long position](/wiki/long-volatility/) when %R climbs above −20, locking gains ahead of potential pullback.
- **Confirmation**: Cross %R below −50 in alignment with a confirmed [support-level](/wiki/support-and-resistance/) break signals conviction in the downmove, not just a spike.

The weakness: mechanical rules (buy every −80, sell every −20) routinely trigger false signals. Markets reward traders who use the oscillator as a *prompt to look closer*, not a self-contained system.

## Divergence spotting

When price makes a new high but %R fails to reach −20 (or new low but %R stays above −80), the indicator signals waning momentum — a [divergence](/wiki/momentum-investing/) pattern many technicians track. This can precede a trend reversal, especially if confirmed by other signals like decreasing [volume](/wiki/volume-breadth-divergence/) or a failed [breakout](/wiki/breakout-trading/).

<div class="wiki-seealso">

### Closely related
- [Stochastic Oscillator](/wiki/stochastic-oscillator/) — Nearly identical mechanic with smoothing applied
- [Relative Strength Index (RSI)](/wiki/rsi-relative-strength/) — Alternative momentum gauge using price changes vs. range
- [Overbought](/wiki/overbought-oversold/) — Theoretical basis for reversal signals

### Wider context
- [Momentum Investing](/wiki/momentum-investing/) — Trend-following strategy contrasting mean-reversion trades
- [Technical Analysis](/wiki/technical-analysis/) — Framework encompassing all oscillator-based methods
- [Support and Resistance](/wiki/support-and-resistance/) — Price levels where reversals cluster
- [Divergence](/wiki/momentum-investing/) — Divergence patterns in price vs. indicator
- [Mean Reversion](/wiki/mean-reversion-investing/) — Assumption underlying overbought-oversold logic

</div>

---
title: "ADX Below 20: Using a Weak-Trend Filter to Avoid False Signals"
description: "What an ADX reading below 20 means for trend strength, why trend crossovers fail in flat markets, and how traders use the threshold to switch off trend-following rules."
keywords:
  - adx below 20
  - adx weak trend
  - average directional index
  - trend filter trading
  - false signals
image: "/svg/technical-analysis.svg"
---

*An **ADX reading below 20** signals a weak or absent trend, and traders use this as a filter to mute [trend-following](/trend-following/) signals that fire in choppy, sideways markets. A moving average crossover that works brilliantly in a trending market becomes a money-losing whipsaw when ADX is below 20, so professionals switch off those signals and wait for the trend to strengthen.*

## What ADX measures

The **Average Directional Index (ADX)** quantifies trend strength on a scale of 0 to 100, independent of direction. An ADX of 50 signals a powerful trend; an ADX of 10 signals virtually no directional momentum.

- **ADX above 40:** Very strong trend.
- **ADX 30–40:** Strong trend.
- **ADX 20–30:** Moderate trend.
- **ADX below 20:** Weak or absent trend (sideways, choppy, or consolidation).

The index doesn't tell you whether the trend is up or down—it only measures how forceful the directional movement is. A stock can be rallying sharply (strong trend) or rising slowly (weak trend). ADX distinguishes between them.

## The false-signal problem in weak trends

Here's the practical trap: A standard [moving average](/moving-average/) crossover (e.g., the 50-day crossing above the 200-day) is a classic trend-following signal. It works beautifully when a strong trend emerges, catching the move early.

But in a choppy market, moving averages cross **constantly**, firing false signals on every small bounce. You buy on a 50/200 crossover, the stock dips 3%, your stop-loss hits, you exit at a loss. Then the stock bounces again, the averages cross, you buy again, and repeat. Whipsaws drain capital and rack up transaction costs.

The common thread in these failed trades: **ADX is below 20**. The market lacks conviction. The bounces feel random because there's no underlying directional force.

## Using ADX below 20 as a filter

The solution is simple: **Ignore trend-following signals when ADX is below 20.**

Here's a practical rule:

1. You're running a trend-following system: buy when the 50-day MA crosses above the 200-day MA.
2. Before you enter, check the ADX.
3. If ADX is above 20, take the signal.
4. If ADX is below 20, **skip the signal**. Wait for the trend to develop.

This single rule cuts whipsaw losses significantly. You miss some false winners (trades that might have worked by random walk alone), but you avoid many more losers.

## Back-testing the threshold

Research consistently shows that **ADX below 20** is a breakpoint for trend-trading profitability:

- Trades taken when ADX is above 20: ~55–60% win rate, positive expectancy.
- Trades taken when ADX is below 20: ~40–50% win rate, often negative.

The exact threshold varies by market, timeframe, and strategy, but 20 is a widely accepted rule of thumb. Some traders use 25 or 30 (stricter, fewer signals but higher quality). Others use 15 (looser, more signals but more whipsaws).

For [momentum investing](/momentum-investing/) or trend-following [funds](/index-fund/), ADX below 20 is a red flag to reduce position sizes or hedge.

## ADX below 20 in different market regimes

**In a bull market:** ADX below 20 signals a pause or consolidation within the larger uptrend. Dip-buying often works, but moving average crossovers are dangerous. You might wait for ADX to climb above 20 again before re-entering.

**In a bear market:** ADX below 20 signals reduced selling pressure. Traders may pause short positions or lighten up, waiting for conviction to return.

**In a sideways market:** ADX below 20 is the norm. Trend-following is useless. Range-trading or mean reversion strategies work better.

## The complement to ADX: directional indicators

ADX shows trend strength, but not direction. That's where the **+DI (positive directional indicator)** and **-DI (negative directional indicator)** come in, part of the same Wilder's DMI system:

- **+DI above -DI:** Uptrend (if ADX is above 20).
- **-DI above +DI:** Downtrend (if ADX is above 20).
- **+DI and -DI near or crossing:** Trend weakening (low ADX confirms).

A complete filter might be:

> Take a **buy signal** only if:
> 1. ADX > 20 (trend is strong)
> 2. +DI > -DI (uptrend confirmed)
> 3. 50-MA > 200-MA (trend-following signal fires)

This three-way confluence reduces false signals dramatically.

## Limitations of the ADX filter

**Lagging.** ADX is calculated from the last 14 periods of price action (by default). It lags in real time and may not warn you of a trend collapse until damage is already done. A trend can weaken fast, but ADX takes time to fall.

**Whipsaws at the threshold.** ADX oscillates around 20. A reading of 19 vs. 21 shouldn't be make-or-break, but rule-based systems treat it that way. Smoothing (e.g., using the 5-period MA of ADX) helps.

**Over-filtering.** Using too many filters can eliminate so many signals that you miss the best trends. ADX below 20 is a filter, not a ban. Some traders use it as a *position sizing* tool (trade smaller if ADX < 20) rather than an off/on switch.

**Different markets, different thresholds.** In a high-volatility index like the Russell 2000, ADX may rarely exceed 30. In a stable blue-chip stock, ADX might hover around 20. No single threshold fits all assets.

## Practical entry for traders

Many traders implement ADX filtering as:

1. **Scan for ADX > 20** at the start of each week. Identify which securities are in trends.
2. **Trade only those.** Use moving average crossovers, breakouts, or [momentum](/momentum-investing/) signals on trending assets.
3. **Pause or scale down** when ADX < 20. Reduce size or avoid new signals.
4. **Exit signals on ADX collapse.** If ADX drops sharply below 20, consider closing trades early (a trend is dying).

This approach removes the emotion of "is this a real trend?" from the decision. The system answers it mechanically.

## ADX below 20 in [volatility](/volatility-smile/) analysis

Low ADX often correlates with **low implied volatility** (options are cheap, because the market expects low movement) and **high realized volatility** (actual price swings but no direction). This mismatch can create opportunities for options traders (volatility arbitrage) but is treacherous for directional traders.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average](/moving-average/) — the trend signal complemented by ADX filtering.
- [Trend Following](/trend-following/) — the broader strategy; ADX is a risk filter.
- [Support and Resistance](/support-and-resistance/) — price levels that often define trends.
- [Volatility Smile](/volatility-smile/) — options pricing when ADX is low.
- [Momentum Investing](/momentum-investing/) — trades ADX as a signal of momentum strength.

### Wider context

- Technical Analysis — the discipline of which ADX is one tool.
- [Market Timing](/market-timing/) — the pitfall that ADX filtering helps avoid.
- [Beta](/beta/) — statistical trend strength; ADX is price-action based.

</div>

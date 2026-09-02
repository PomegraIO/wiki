---
title: "ADX Directional Movement"
description: "A technical indicator measuring the strength of a price trend (up or down), ranging from 0 to 100, independent of direction."
keywords:
  - average directional index
  - trend strength
  - technical analysis
  - momentum indicator
  - directional movement
---

*The **Average Directional Index (ADX)** is a technical indicator that quantifies how strong a price trend is, regardless of whether the trend is up or down. Unlike many [momentum indicators](/wiki/momentum-factor/) that signal direction, the ADX isolates pure trend strength on a 0–100 scale, making it a powerful filter for distinguishing genuine trends from noise.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|----------|--------|
| **Creator** | J. Welles Wilder Jr. (1978) |
| **Components** | +DI (positive directional), −DI (negative directional), ADX line |
| **Scale** | 0–100; higher = stronger trend |
| **Strength threshold** | <20: weak; 20–40: developing trend; >40: strong; >60: very strong |
| **Ideal use** | Trend confirmation; filter for [trend-following](/wiki/trend-following/) strategies |
| **Lag** | Smoothing (14-period default) means late signal on trend reversals |
| **Best conditions** | Strong trending markets; less useful in sideways/choppy ranges |

</aside>

## The three components: +DI, −DI, and ADX

The ADX is built from three line:

**Positive Directional Indicator (+DI).** Measures the strength of upward price movement. If today's high exceeds yesterday's high by more than today's low exceeds yesterday's low (upward momentum), the +DI increases. Over time, a rising +DI signals strengthening uptrends.

**Negative Directional Indicator (−DI).** Measures the strength of downward price movement. If today's low is lower than yesterday's low by more than today's high exceeds yesterday's high, the −DI increases. Rising −DI signals strengthening downtrends.

**Average Directional Index (ADX).** The smoothed (typically 14-period average) measure of the absolute difference between +DI and −DI, normalized to 0–100. Rising ADX means the stronger of the two directional forces is accelerating — i.e., a trend is strengthening, regardless of which direction.

## Interpreting ADX levels

**ADX below 20.** The trend is weak or non-existent. Price may be choppy, sideways, or directionless. Trend-following strategies often skip these conditions.

**ADX 20–40.** A trend is forming or developing. The indicator is not yet at full strength, but directional movement is emerging. This is often when traders enter trend-following positions, betting the trend will strengthen.

**ADX 40–60.** A strong trend is in place. The market is decisively moving in one direction. Momentum strategies prosper.

**ADX above 60.** An exceptionally strong trend. Price is in powerful motion; mean reversion traders sometimes prepare to fade the move (betting it reverses), while trend followers stay on board.

## Using +DI and −DI crossovers

The relative position of +DI and −DI adds signal:

- **+DI above −DI.** Uptrend in force. The difference between them amplifies as the uptrend strengthens.
- **−DI above +DI.** Downtrend in force.
- **+DI and −DI close together.** Weak directional movement; the two forces are balanced.
- **Crossover.** When +DI crosses above −DI, some traders read this as an uptrend beginning. Conversely, −DI crossing above +DI can signal a downtrend start.

## ADX as a trend filter, not a predictor

A critical insight: the ADX tells you the current trend strength, not whether the trend will continue or reverse. A high ADX doesn't mean prices will keep rising; it means the current uptrend is strong. When a trend is mature and strong, reversals often happen shortly after.

This is why ADX is best used as a **filter** rather than a standalone trading signal:

**In trend-following systems.** A trader might enter breakouts only when ADX is above 30, ensuring they're trading in a legitimate trend, not noise. Once ADX falls below 20, they exit trend positions because the trend has weakened.

**In mean-reversion systems.** Some traders look for **high ADX with price near [resistance](/wiki/support-and-resistance/) or [support](/wiki/support-zone-floor/)**, betting the strong trend has exhausted itself at a technical level and will reverse.

**Combined with moving averages.** A trader might use a rising 50-day moving average (trend direction) and ADX > 30 (trend strength) together, trading only when both align.

## Practical examples

**Uptrend scenario.** A stock rallies from $80 to $120 over two months. +DI is above −DI and rising. ADX climbs from 25 to 50, confirming the uptrend strengthens. A trend-following trader holds longs. When ADX begins to fall from 50 toward 30, even though the stock is still rising, the trader considers lightening up — the trend is losing thrust.

**Reversal scenario.** A stock has rallied from $100 to $140, with ADX now at 65 (very strong uptrend). Price approaches a major resistance level. A mean-reversion trader might sell or short, betting the strong trend has run into selling pressure. ADX begins to fall. Soon, price rolls over. The mean-reversion trade profits.

**Sideways scenario.** A stock trades between $50 and $55 for weeks. ADX sits at 15 (very weak). Neither +DI nor −DI dominates. A trend-following system avoids trading. A [range-trading](/wiki/range-trading/) system might buy at support and sell at resistance, using the weak ADX as a signal that breakout trades are unlikely to work.

## Lag and limitations

The ADX is a **lagging indicator** — it smooths past directional movement. This means:

- **Late entries.** By the time ADX signals a strong trend (rises above 40), the trend is already well-established and some profit is already taken.
- **Late exits.** When a trend reverses, ADX falls slowly, potentially keeping you in the trade longer than ideal.
- **False signals in choppy markets.** In highly volatile, choppy markets, ADX can spike briefly on random swings, triggering false signals.

Combining ADX with [leading indicators](/wiki/leading-indicator/) (e.g., [RSI](/wiki/rsi-relative-strength/), [MACD](/wiki/macd-indicator/)) can help mitigate lag.

## Variants and refinements

**ADX momentum.** Some traders plot the slope of the ADX line itself — rising slope means the trend is accelerating, falling slope means deceleration. This adds a layer of momentum insight.

**ADX crossovers with price levels.** Some use ADX > 40 as a mechanical filter in [algorithmic trading](/wiki/algorithmic-trading/) systems, ignoring trade signals when the filter is not met.

**Multiframe ADX.** A trader might check ADX on multiple timeframes — if ADX is high on a daily chart but low on a 4-hour chart, the daily trend is strong but short-term is choppy, shaping position size and exit strategy.

## Comparison to other trend-strength indicators

**[ATR (Average True Range)](/wiki/atr-true-range/).** Measures volatility, not trend strength. High ATR means large moves; ADX tells you if those moves have directional intent.

**Bollinger Bands.** Mark price ranges; don't directly measure trend strength.

**[MACD](/wiki/macd-indicator/).** Shows momentum and trend direction; ADX adds a pure strength dimension.

**Slope of moving average.** The steeper the slope, the stronger the trend; ADX quantifies the same concept more systematically.

## Sector and market conditions

ADX works well in:
- Trending markets (stocks, commodities, forex during trend cycles).
- Liquid, high-volume instruments (ADX is based on directional changes, which require reliable data).

ADX is less useful in:
- Choppy, sideways markets (constant ADX < 20).
- Low-liquidity stocks (noise can distort directional signals).
- Highly ranged-bound, mean-reverting instruments.

## Integration into trading systems

Professional trend-following systems often employ ADX as a core filter:
- **Entry.** Trend signal triggered only when ADX > 30 (rising trend confirmed).
- **Position sizing.** Larger positions when ADX > 50 (strong trend supports higher conviction).
- **Exit.** Close positions when ADX < 20 (trend has broken down).

This approach reduces losses in choppy markets and amplifies gains in strong trends.

<div class="wiki-seealso">

### Closely related
- [Momentum Factor](/wiki/momentum-factor/) — Market acceleration and directional strength
- [Trend Following](/wiki/trend-following/) — Strategy based on directional price movement
- Moving Averages — Price trend direction indicator
- [RSI (Relative Strength Index)](/wiki/rsi-relative-strength/) — Momentum and overbought/oversold conditions

### Wider context
- Technical Analysis — Price and volume patterns
- [Support and Resistance](/wiki/support-and-resistance/) — Technical levels ADX helps confirm
- [Algorithmic Trading](/wiki/algorithmic-trading/) — Systems that employ ADX as a filter
- [Volatility](/wiki/volatility-factor-performance/) — Market movement amplitude

</div>

---
title: "Accumulation Distribution"
description: "A price-volume indicator that tracks whether institutional buying (accumulation) or selling (distribution) is happening within price movements."
keywords:
  - accumulation distribution line
  - volume analysis indicator
  - price volume relationship
  - institutional buying pressure
---

*The **accumulation/distribution** (A/D) line is a technical analysis indicator that combines [price](/wiki/stock-market/) and [volume](/wiki/volume-breadth-divergence/) to assess whether a [security](/wiki/common-stock/) is in an **accumulation phase** (smart money or institutions building [positions](/wiki/position-trading/)) or a **distribution phase** (smart money exiting positions). A divergence between A/D and [price](/wiki/stock-market/)—for example, price rising while A/D falls—suggests the rally lacks conviction and may reverse, providing a warning to [traders](/wiki/trading-halts/) before the crowd realizes.*

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Calculation basis** | [Closing price](/wiki/closing-print/) position within the day's [high-low](/wiki/ohlc-bar-chart/) range × daily [volume](/wiki/volume-breadth-divergence/) |
| **Interpretation** | Rising A/D: accumulation (bullish); falling A/D: distribution (bearish) |
| **Signal divergence** | Price ↑ but A/D ↓ suggests weak rally; price ↓ but A/D ↑ suggests accumulation into weakness |
| **Timeframe** | Works on all charts: intraday, daily, weekly |
| **Popularity** | Widely used by swing traders and position traders; less reliable in sideways markets |

</aside>

## The intuition: price close relative to daily range

The A/D indicator is rooted in a simple premise: **where a security closes within its daily [high-low](/wiki/ohlc-bar-chart/) range reveals institutional intent**. If a stock opens at $100, trades up to $105, then closes at $103 on heavy [volume](/wiki/volume-breadth-divergence/), the [close](/wiki/closing-print/) is near the high of the day. This suggests buying pressure (buyers pushed price up and held it), accumulation. Conversely, if a stock opens at $100, rallies to $105, then falls to $101 on heavy [volume](/wiki/volume-breadth-divergence/), the [close](/wiki/closing-print/) near the low suggests selling pressure, distribution.

The A/D line quantifies this. For each bar (daily, hourly, or minute), the indicator calculates:

**Money Flow Multiplier** = (Close – Low) / (High – Low)

If the [close](/wiki/closing-print/) is exactly at the high, the multiplier is 1.0 (pure buying). If the [close](/wiki/closing-print/) is at the low, the multiplier is 0.0 (pure selling). If the [close](/wiki/closing-print/) is midway, it is 0.5 (neutral). This multiplier is then multiplied by the day's [volume](/wiki/volume-breadth-divergence/), creating a "money flow" value that is added (or subtracted if negative) to a running total—the A/D line.

## Interpreting divergences

The A/D line's power lies in **divergence from price**. Consider three scenarios:

**Scenario 1: Bullish divergence (accumulation into weakness)**. A stock falls from $50 to $40 over two weeks on declining [volume](/wiki/volume-breadth-divergence/), but the A/D line is rising or flat. This suggests big buyers are stepping in on the [dip](/wiki/mean-reversion-investing/), accumulating positions. A reversal up is likely; the smart money is loading the boat.

**Scenario 2: Bearish divergence (distribution into strength)**. A stock rises from $50 to $55 over two weeks on declining [volume](/wiki/volume-breadth-divergence/) and falling A/D. This suggests smart money is unloading positions despite the price rise—a red flag. The rally lacks institutional support and may reverse sharply.

**Scenario 3: Confirmation**. A stock rises on rising [volume](/wiki/volume-breadth-divergence/) and rising A/D. This is textbook accumulation; the trend is likely to continue. Conversely, a fall on falling [volume](/wiki/volume-breadth-divergence/) and falling A/D is weak selling that may stall.

[Traders](/wiki/trading-halts/) scan for divergences using A/D charts. Many [swing traders](/wiki/swing-trading/) treat a bearish divergence (price up, A/D down) as a short signal—exit long [positions](/wiki/position-trading/) or establish [short positions](/wiki/short-selling/) in anticipation of a reversal.

## Relationship to other volume indicators

The A/D line is one of several [volume indicators](/wiki/volume-breadth-divergence/), each measuring different aspects of price-[volume](/wiki/volume-breadth-divergence/) interaction:

- **[On-Balance Volume](/wiki/obv-on-balance-volume/)** (OBV): A cumulative [volume](/wiki/volume-breadth-divergence/) indicator that adds [volume](/wiki/volume-breadth-divergence/) on up days and subtracts on down days. OBV is simpler than A/D but does not account for where the [close](/wiki/closing-print/) falls within the day's range.

- **[Money Flow Index](/wiki/money-flow-index/)** (MFI): Like [relative strength index](/wiki/rsi-relative-strength/) (RSI) but incorporates [volume](/wiki/volume-breadth-divergence/). MFI ranges from 0–100 and identifies overbought and oversold conditions.

- **[Chaikin Oscillator](/wiki/chaikin-oscillator/)**: Applies moving averages to the A/D line to generate signals.

The A/D line is less a standalone signal than a **confirmation tool**—use it alongside [price action](/wiki/price-discovery/), [support and resistance](/wiki/support-resistance-basics/), and other technical indicators to increase conviction.

## Limitations and caveats

A/D divergences are not foolproof. Several pitfalls:

1. **[Sideways markets](/wiki/flat-market/)**: When a security trades in a range with no [trend](/wiki/trendline/), the A/D line oscillates without clear direction, generating false signals.

2. **[Manipulation](/wiki/market-surveillance/)**: Smart money can feint, pushing price up on light [volume](/wiki/volume-breadth-divergence/) to trigger buy stops, then selling on the spike. A/D will lag behind the manipulation.

3. **[Earnings gaps](/wiki/overnight-gap/)**: If a security gaps up on earnings, the next day's A/D may show divergence not because smart money is dumping, but because buyers have already capitulated on the gap.

4. **[Thin liquidity](/wiki/liquidity-risk/)**: In [stocks](/wiki/common-stock/) with low [volume](/wiki/volume-breadth-divergence/), a few large trades skew the A/D line and create false signals.

5. **Time horizon mismatch**: A short-term trader using daily A/D may miss a long-term accumulation pattern visible only on weekly charts.

## Practical application in swing trading

[Swing traders](/wiki/swing-trading/) often use A/D in a three-step process:

1. **Identify a [support level](/wiki/support-resistance-basics/)**: e.g., a stock bounces off $45 three times.
2. **Watch for a divergence**: Price falls below $45, but A/D holds up or rises. This indicates accumulation.
3. **Enter on reversal**: When price bounces back above $45 on rising [volume](/wiki/volume-breadth-divergence/) and rising A/D, go [long](/wiki/long-call-ladder/).

Conversely, at [resistance](/wiki/resistance-zone-ceiling/), a bearish divergence (price ↑, A/D ↓) is a short setup. This discipline ensures [trades](/wiki/trade-reporting/) are only taken when volume confirms the move.

## Limitations of technical analysis as a whole

A/D is a technical analysis tool, and all such tools operate on the assumption that price history and [volume](/wiki/volume-breadth-divergence/) patterns repeat. This is contested by efficient market advocates who argue [stocks](/wiki/common-stock/) are fairly priced and technical signals are noise. [Fundamental investors](/wiki/fundamental-investing/) dismiss A/D as distraction from [earnings](/wiki/earnings-per-share/) and [cash flow](/wiki/cash-flow-statement/).

However, A/D has some empirical support. Studies show that [price-volume](/wiki/volume-breadth-divergence/) divergences do predict reversals at above-random rates, particularly at key [support](/wiki/support-resistance-basics/) and [resistance](/wiki/resistance-zone-ceiling/) levels. A/D is most useful as one signal among many, not as a standalone oracle.

<div class="wiki-seealso">

### Closely related
- [On-Balance Volume](/wiki/obv-on-balance-volume/) — A simpler cumulative volume indicator
- [Price-Volume Relationship](/wiki/volume-breadth-divergence/) — How volume confirms or contradicts price moves
- [Chaikin Oscillator](/wiki/chaikin-oscillator/) — Moving average of the A/D line for smoother signals

### Wider context
- Technical Analysis — The broader discipline of price and volume pattern recognition
- [Support and Resistance](/wiki/support-resistance-basics/) — Price levels where A/D divergences are most meaningful
- [Swing Trading](/wiki/swing-trading/) — Short-term trading strategy that relies heavily on volume indicators

</div>

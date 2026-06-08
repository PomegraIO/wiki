---
title: "Average True Range (ATR) Explained"
description: "How Average True Range measures volatility, how it is calculated from true ranges, and how traders use it for stops and position sizing."
keywords:
  - average true range explained
  - atr indicator volatility
  - true range calculation
  - atr stop-loss
  - position sizing volatility
image: /svg/technical-analysis.svg
---

*The **Average True Range (ATR)** is a [volatility](/volatility-smile/) metric that measures the average of the true range—the largest of: today's high minus low, today's high minus yesterday's close, or yesterday's close minus today's low. Traders use ATR to set [stop-loss](/stock/) distances and size positions based on market chop rather than a fixed dollar amount or percentage.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Average True Range — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">A dynamic measure of how much price typically moves in one period.</div>

|   |   |
|---|---|
| **True Range (TR)** | max(H−L, H−Pc, L−Pc) where H=high, L=low, Pc=prior close |
| **ATR formula** | 14-period moving average of true range (most common period) |
| **Direction-neutral** | ATR measures magnitude, not direction of moves |
| **Stop-loss rule** | Place stops 1–3 × ATR away from entry to avoid random chop |
| **Position sizing** | Smaller positions in high-ATR environments, larger in low-ATR |
| **Regime indicator** | Rising ATR signals increasing volatility; falling ATR signals low volatility |
| **Time frame sensitive** | Daily ATR differs from hourly ATR; scale accordingly |

</aside>

## The concept of true range

The **true range** is the foundation of ATR. On any given day, price might move from open to high to low and back, and the high-low range tells one part of the story. But price can also gap significantly from the prior close.

True range accounts for gaps:

**TR = max(H − L, H − Pc, L − Pc)**

Where:
- H = today's high
- L = today's low
- Pc = yesterday's close

This three-value comparison captures the full extent of the move, including any overnight or between-session gaps.

**Example**: 
- Yesterday closed at 100.
- Today high is 103, low is 99.
- H − L = 3
- H − Pc = 103 − 100 = 3
- L − Pc = 99 − 100 = −1 (absolute value = 1)
- True Range = max(3, 3, 1) = 3

If there had been a gap:
- Yesterday closed at 100.
- Today opens at 102 (gap up), high is 105, low is 101.
- H − L = 4
- H − Pc = 105 − 100 = 5
- L − Pc = 101 − 100 = 1
- True Range = max(4, 5, 1) = 5

The true range correctly captures the 5-point extent of the move, not just the 4-point intraday range.

## Calculating ATR

The Average True Range is simply the **moving average of true range** values over a lookback period. The standard is 14 periods (14 days on a daily chart, 14 hours on an hourly chart, etc.).

**Step 1**: Calculate true range for each of the past 14 periods.
**Step 2**: Sum those 14 true range values.
**Step 3**: Divide by 14 to get the average.

On subsequent days, a new true range is calculated, and the average is recalculated using the most recent 14 values (an exponential moving average variant is sometimes used for faster responsiveness).

**Example** (daily chart):
- Day 1 TR: 2.5
- Day 2 TR: 3.1
- Day 3 TR: 1.8
- ... (through day 14)
- Sum of 14 days' TR: 42
- ATR = 42 / 14 = 3.0

This means the average true range over the past 14 days is 3.0 points. On the next day, a new day's true range is added, the oldest day is dropped, and ATR is recalculated.

## What ATR measures: volatility, not direction

Critical: **ATR measures how much price moves, not which direction it moves.** A stock that gaps up 5 points has the same contribution to ATR as a stock that gaps down 5 points.

This is why ATR is called a "volatility indicator," not a "directional indicator." High ATR means big moves are common (in either direction). Low ATR means price is grinding sideways.

This direction-neutrality is a feature: it lets traders set risk-appropriate stops regardless of whether they are long or short. If ATR is 10 on a $100 stock, a reasonable stop might be 10–15 points away. If ATR is 1 on a $100 stock, a stop might be 1–2 points away.

## Using ATR to set stop-loss levels

The most common use of ATR is determining stop-loss distance.

**For a long trade**:
- Entry: $100
- ATR: $3
- Stop-loss: $100 − 2 × ATR = $100 − $6 = $94

**For a short trade**:
- Entry: $100
- ATR: $3
- Stop-loss: $100 + 2 × ATR = $100 + $6 = $106

Multipliers of 1, 1.5, 2, or 3 × ATR are common. A 1 × ATR stop is tight and will be hit frequently by chop. A 2–3 × ATR stop gives price more room to breathe before hitting a stop.

The benefit: stops adjust automatically as volatility changes. In a calm market, ATR is low, so stops are tight. In a volatile market, ATR is high, so stops are looser—protecting you from being stopped out by random noise.

## Using ATR for position sizing

If you have a fixed dollar risk per trade (say, $500), ATR helps determine position size:

**Position Size = Risk $ / (ATR × Price units per contract)**

In high-volatility environments (high ATR), this formula naturally reduces position size, because the stop is farther away. In low-volatility environments (low ATR), the formula increases position size, because the stop is closer.

This is a form of **volatility-adjusted risk management**. Instead of risking the same percentage on every trade, you risk the same absolute dollar amount, adjusted for the volatility of the instrument you're trading. A volatile penny stock gets a smaller position than a liquid blue-chip stock at the same dollar risk.

## ATR as a volatility regime indicator

Rising ATR signals increasing volatility. This is often a warning sign:

- At the end of a trend, volatility often increases as the trend exhausts (more whipsaws, more profit-taking).
- Before an earnings announcement or economic event, ATR often rises (or implied volatility in options rises).
- After a break in support or resistance, ATR often spikes higher.

Falling ATR signals declining volatility—price is grinding in a narrower range. This is often a sign of consolidation before a breakout or a calm, directionless market.

Traders use ATR regimes to adjust their strategies:
- In high-ATR regimes, they tighten stops, take profits faster, and may reduce position size.
- In low-ATR regimes, they may take larger positions and be more patient with winning trades.

## Comparing ATR across time frames

ATR on a daily chart is not directly comparable to ATR on a hourly chart. A stock's daily ATR might be $5, but its hourly ATR might be $1. The scales are different.

To compare, traders normalize ATR as a percentage of price:

**ATR % = (ATR / Price) × 100**

A stock at $100 with ATR of $5 has ATR % of 5%. A stock at $200 with ATR of $8 has ATR % of 4%. The second stock is less volatile relative to its price.

## ATR and [average true range](/average-true-range-explained/) in different market conditions

**Trending markets**: ATR tends to rise during strong trends because larger daily moves occur. Breakout traders like high-ATR markets because big moves are more likely.

**Ranging markets**: ATR tends to stay low and stable. Range traders like low-ATR markets because chop is predictable and wicks don't break far outside the range.

**At turning points**: ATR often increases before a reversal—volatility rises as conviction weakens. A sharp drop in ATR after a rise can signal consolidation before a breakout.

## Combining ATR with other indicators

ATR is often combined with other technicals for confirmation:

- **ATR expansion + breakout above resistance = higher odds of success.**
- **Rising ATR + falling moving average crossover = stronger downtrend signal.**
- **High ATR + doji candle = indecision at high volatility; expect a move soon.**

[Moving averages](/moving-average/) and trend lines work well with ATR: if price is above the moving average and ATR is rising, the trend is accelerating. If price is below the moving average and ATR is falling, the trend is weakening.

## Limitations of ATR

ATR is not perfect:

- **Lagging**: ATR reacts to price action after it occurs. A sudden gap can cause ATR to spike one day after a big move.
- **Not predictive**: High ATR today doesn't guarantee high ATR tomorrow. A period of calm can follow extreme volatility.
- **Context-dependent**: An ATR of 5 is high for a $100 stock but low for a $500 stock. Compare ATR % or compare to historical ATR for the same instrument.
- **Gap risk**: ATR accounts for gaps but cannot predict their direction or magnitude. A stock can gap $20 with an ATR of $3.

## See also

<div class="wiki-seealso">

### Closely related

- [How to Read Candlestick Wicks](/how-to-read-candlestick-wicks/) — Understanding the price extremes that ATR measures
- [Moving Average](/moving-average/) — Combining ATR with trend-following indicators
- [Price Discovery](/price-discovery/) — ATR as a measure of market-participant disagreement

### Wider context

- [Volatility Smile](/volatility-smile/) — Implied volatility in options; complementary to realized ATR
- Technical Analysis — ATR within the broader toolkit of chart analysis
- [Risk Management](/stock/) — Position sizing and stop-loss strategy using ATR
- [Market Timing](/market-timing/) — Using ATR to time entry and exit signals

</div>

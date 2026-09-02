---
title: "Pivot Point Levels"
description: "Support and resistance levels calculated from the prior trading day's OHLC data."
keywords:
  - pivot points
  - support and resistance
  - daily levels
  - technical analysis
  - ohlc data
---

*A **pivot point level** is a support or [resistance](/wiki/support-and-resistance/) price derived mathematically from the prior day's high, low, open, and close. Traders use these levels as objective benchmarks for intraday reversals, without relying on subjective chart reading.*

<div class="wiki-hatnote">For the broader concept of support and resistance, see <a href="/wiki/support-and-resistance/">/support-and-resistance/</a>.</div>

<aside class="wiki-infobox">

| Element | Formula |
|---|---|
| **Pivot (P)** | (High + Low + Close) / 3 |
| **Support 1 (S1)** | (P × 2) − High |
| **Resistance 1 (R1)** | (P × 2) − Low |
| **Support 2 (S2)** | P − (High − Low) |
| **Resistance 2 (R2)** | P + (High − Low) |
| **Mid-Pivot** | (P + S1) / 2 or (P + R1) / 2 |
| Time frame | Intraday (based on prior day) |
| Frequency | Daily (reset each market open) |
| Use case | Day traders, short-term directional entry/exit |

</aside>

## The core calculation

The **pivot point** itself is the average of the prior day's high, low, and close—a weighted midpoint. From there, traders calculate two support levels (S1 and S2) below the pivot and two resistance levels (R1 and R2) above it. These five levels divide the trading range into zones.

The logic is mechanical: if yesterday's range was $100–$110 and it closed at $108, the pivot is roughly $106. Support 1 (closer to the pivot) would be around $104; Resistance 1 around $108. The assumption is that mean-reverting moves within the prior range stay somewhat orderly.

## Why traders believe in pivot points

Several forces support the idea:

1. **Psychology and order clustering** — if many traders use the same pivot calculation, their buy and sell orders converge at the same levels, creating self-fulfilling [support zones](/wiki/support-zone-floor/).

2. **Mean reversion** — intraday prices tend to revert toward yesterday's midpoint if no major news arrives.

3. **Simplicity** — unlike [trend lines](/wiki/trendline/) or moving averages, pivot levels require no judgment or discretion. Every trader gets the same number.

4. **Institutional usage** — [market makers](/wiki/market-makers/) and [algorithmic traders](/wiki/algorithmic-trading/) often use pivot points as reference prices for [order placement](/wiki/order-types/) and [bid-ask spread](/wiki/bid-ask-spread/) management.

## Variations in the formula

The classic formula above (using H, L, C equally) is sometimes called **Standard Pivots**. Variants exist:

- **Fibonacci Pivots** — use [Fibonacci levels](/wiki/fibonacci-levels/) (0.618, 1.0, 1.618) applied to the H−L range instead of simple arithmetic.

- **Woodie's Pivots** — weight the close double: `(Close + Close + High + Low) / 4`, then calculate support/resistance the same way. Emphasizes recent price action.

- **Camarilla Pivots** — divide H−L into quarters and calculate tight support/resistance bands. Often used for [day trading](/wiki/day-trading/) in narrow-range markets.

- **DeMark Pivots** — a more complex algorithm based on open and close location within the H−L range. Often produces asymmetric levels.

The choice matters in practice. Fibonacci pivots tend to be wider (further from the pivot). Woodie's and Camarilla pivots create tighter, more frequent turnover zones.

## Using pivots for entry and exit

A common intraday scheme:

1. **Open bias** — if price opens above the pivot, assume uptrend; target R1 or R2 for profit. If below, assume downtrend; target S1 or S2.

2. **Reversal play** — if price approaches R2 resistance without breaking through, take profit and reverse to short. Similarly for S2.

3. **Breakout confirmation** — if price closes above R2 on volume, the pivot system "breaks"—yesterday's logic no longer holds, and the trader abandons the levels and switches to trend-following ([momentum](/wiki/momentum-investing/)).

4. **Risk stops** — place [stop-loss orders](/wiki/stop-order/) just beyond S2 (if long) or R2 (if short) to limit [tail risk](/wiki/tail-risk/).

## Pivot points vs. dynamic support/resistance

Pivot levels are **static and recalculate daily**. This differs from other methods:

- **Trendlines** — drawn subjectively; don't reset daily.
- **Moving averages** — update continuously as new data arrives.
- **Previous swing highs/lows** — pivot points are more systematic (formula-driven) than visual swings but less intuitive.

The strength of pivots is objectivity; the weakness is that yesterday's range does *not* always contain today's price action. A [gap](/wiki/overnight-gap/) or major news release (earnings, Fed decision) can send the price far beyond all five pivot levels by 9:31 a.m., rendering the levels irrelevant.

## Effectiveness in different asset classes

Pivots work best in:
- **Equities with decent intraday liquidity** — large-cap [stocks](/wiki/stock/) with tight spreads and high [order-book depth](/wiki/order-book-depth/).
- **Liquid [forex](/wiki/forex-leverage/) pairs** (EUR/USD, GBP/USD) — pivots are widely used; the self-fulfilling effect is strong.
- **Futures contracts** — [commodity futures](/wiki/futures-contract/) and [index futures](/wiki/volatility-index-futures/) with tight [tick](/wiki/tick-size-regime/) sizing.

Pivots are less reliable in:
- **Low-liquidity names** — microcaps and thinly traded securities.
- **High-volatility environments** — spikes and crashes easily breach all pivot levels.
- **News-driven markets** — [earnings surprises](/wiki/earnings-surprise-strategy/) or geopolitical events can render pivots obsolete in seconds.

## Combining pivots with other indicators

Most traders don't rely on pivots alone. Common additions:

- **[Momentum indicators](/wiki/momentum-factor/)** ([RSI](/wiki/rsi-relative-strength/), [MACD](/wiki/macd-indicator/)) — confirm whether price is overbought or oversold near pivot levels.
- **Volume profile** — heavy volume near pivot points strengthens the level; light volume weakens it.
- **Moving averages** — use daily 50-MA or 200-MA as a macro filter. Don't fade the major trend near pivots.
- **[Volatility measures](/wiki/implied-volatility/)** — on high-volatility days, pivot levels widen and become less reliable.

## Pitfalls and overfitting

- **Assuming yesterday's range persists** — pivot levels are *derived* from yesterday but tell you nothing about today's range. A volatile opening gap often negates the calculation.
- **Overreliance on one level** — traders often fixate on R1 or S1 and ignore the bigger technical context.
- **Backtesting bias** — pivot point systems backtest well on past data (because the formula is fixed) but may underperform in real time due to changing correlations and trading participation.

<div class="wiki-seealso">

### Closely related
- [Support and resistance](/wiki/support-and-resistance/) — the foundational concept
- [Support zone (floor)](/wiki/support-zone-floor/) — how price clusters at key levels
- [Resistance zone (ceiling)](/wiki/resistance-zone-ceiling/) — upper bound of traded price ranges
- Technical analysis — broader framework
- [Day trading](/wiki/day-trading/) — primary use case for pivot points

### Wider context
- [Fibonacci levels](/wiki/fibonacci-levels/) — alternative mathematical levels for support/resistance
- [Trendline](/wiki/trendline/) — subjective (non-formula) approach to levels
- [Volume profile support](/wiki/volume-profile-support/) — price levels backed by trading volume
- [Bid-ask spread](/wiki/bid-ask-spread/) — how support/resistance levels interact with market structure
- [Order routing logic](/wiki/order-routing-logic/) — how traders place orders near pivot levels

</div>

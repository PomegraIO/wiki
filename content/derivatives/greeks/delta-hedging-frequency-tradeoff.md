---
title: "Delta Hedging Frequency: Costs vs Accuracy Tradeoff"
description: "Delta hedging frequency determines how often you rebalance a delta-neutral book to lock in gamma profit. Learn the tradeoff between transaction costs and hedging accuracy."
keywords:
  - delta hedging frequency tradeoff
  - delta hedging rebalance
  - gamma profit delta hedge
  - option book management
  - dynamic hedging
  - transaction costs hedging
image: /svg/derivatives.svg
---

*The optimal **delta hedging frequency** balances two forces: **gamma profit** (gains from rehedging after price moves) and **transaction costs** (spreads and commissions from frequent trades). A delta-neutral book drifts with price moves; rehedging captures the realized volatility but costs money with each trade. Rehedge too often and costs eat returns; too rarely and gamma exposure accumulates, risking large losses when markets move sharply.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delta Hedging Frequency — The Tradeoff</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Frequent rehedges lock in gamma gains but bleed transaction costs; sparse rehedges save costs but tolerate drift.</div>

|   |   |
|---|---|
| **Rehedge trigger** | Delta threshold (e.g., rehedge when delta drifts 0.10) or time-based (daily, hourly) |
| **Gamma profit** | Realized from price moves between rehedges; larger moves = larger profit |
| **Transaction costs** | Bid-ask spread, commissions, and market impact; scale with notional |
| **Optimal frequency** | Depends on [volatility](/historical-volatility/), spread, and position size |
| **Practical rule** | Rehedge when delta threshold breached (e.g., |delta|>0.10) |
| **Gamma exposure risk** | Unhedged gamma after rehedge; gap risk if market gaps overnight |
| **Realized vs implied** | Profit when realized volatility exceeds implied; loss when it falls short |
| **Intraday management** | High-frequency traders rehedge continuously; dealers rehedge daily or weekly |

</aside>

## The Gamma and Delta Problem

A trader who sells [options](/option/) is **short gamma**—when the underlying price moves, the [delta](/delta/) of the position changes. If you sell a call option, your position was delta-neutral at inception, but a 2% price rise makes it negative delta (you've effectively shorted the stock). To stay delta-neutral, you must buy stock to offset.

Conversely, a 2% price drop makes your position positive delta, so you must sell stock to rehedge.

This rehedging—buying low and selling high—is profitable. It's called **gamma profit** or **gamma scalping**. But each trade costs money: a [bid-ask spread](/bid-ask-spread/), commissions, and potentially market impact.

## The Rehedging Interval Question

The trader must choose: rehedge after every 0.5% move? Daily? Weekly? The answer depends on comparing gamma profit from frequent rehedges against the cost of making those trades.

**Example: A $10 million book**

A trader is short a 6-month [call option](/call-option/) on a stock. She delta-hedges by holding the underlying stock, rebalancing as the stock price moves.
- Initial position: delta-neutral (long stock, short call).
- Stock rises 2%: delta becomes -0.20 (short $200k notional). She buys $200k stock to rehedge.
- Stock falls 1%: delta becomes +0.15 (long $150k notional). She sells $150k stock to rehedge.

Each rehedge costs 3 basis points in [bid-ask spread](/bid-ask-spread/) and 1 basis point in commissions—4 basis points, or 0.04%. On a $200k trade, that's $80.

Over a month, she rehedges 20 times: 20 × $80 = $1,600 in costs.

But if the stock realized volatility is 25% annualized, she's capturing gamma profit of roughly $3,000 over the month—netting $1,400.

If she rehedges only 5 times a month, costs drop to $400, but gamma profit shrinks because she misses some small moves. The net might be $2,000—better.

If she rehedges 40 times, costs hit $3,200, wiping out the $3,000 in gamma profit. Worse.

## Delta Thresholds vs Time-Based Schedules

Traders use two rehedging approaches:

**Delta-threshold rehedging:** Rehedge whenever delta drifts beyond a threshold—e.g., |delta| > 0.10 (meaning position is no longer close to delta-neutral). This is responsive; you act when drift matters, not on a calendar.

**Time-based rehedging:** Rehedge at fixed intervals—daily, every 4 hours, hourly. Simple to implement but ignores market quietness. In calm markets, daily rehedges waste capital; in volatile markets, they're insufficient.

Most professional traders use delta thresholds because they adapt to volatility. In calm markets, thresholds are breached rarely; in volatile markets, rehedges happen frequently, which is correct—more volatility means more gamma profit available, justifying more hedges.

## Realized vs Implied Volatility

The profitability of gamma trading hinges on a key insight: **gamma profit depends on realized volatility, not the implied volatility at which you sold the option.**

If you sell a call with 20% implied [volatility](/historical-volatility/), pricing it at $2, but the stock's actual volatility (realized volatility) is 25%, you'll profit on gamma—your rehedges will generate more profit than the option's theta decay cost.

If realized volatility turns out to be 15%, you'll lose on gamma.

Optimal rehedging frequency must account for expected realized volatility. High volatility justifies frequent rehedges; low volatility suggests sparse rehedges to save on costs.

## The Math (Simplified)

The break-even rehedging frequency is roughly:

```
Optimal rehedges per period ≈ sqrt(Volatility × Bid-Ask Spread / Gamma)
```

Higher volatility → more rehedges (more drift to capture).
Wider spread → fewer rehedges (costs are higher).
Larger gamma → more rehedges (each trade is more profitable).

For a large bank trading in a liquid market (tight spreads, large notional), rehedging multiple times per day is profitable. A small trader in a wide-spread product might rehedge weekly.

## Practical Intervals by Market Type

**Liquid equity index options:**
- Rehedge when delta drifts 0.05–0.10.
- High volatility: rehedge 50–100+ times per day.
- Low volatility: rehedge 5–10 times per day.

**Single-stock options (moderate liquidity):**
- Rehedge when delta drifts 0.10–0.20.
- Typical: 10–30 rehedges per day.

**Commodity futures options (variable liquidity):**
- Rehedge when delta drifts 0.20–0.50.
- Typical: 5–10 rehedges per day; sometimes daily.

**Exotic or illiquid options:**
- Rehedge daily or weekly.
- Wider spreads mean costs dominate.

## The Gap Risk Hidden Cost

Rehedging assumes you can execute at fair prices. In fast markets—earnings announcements, central bank decisions, stock halts—the underlying can gap 5%, 10%, or more in seconds. Your delta-neutral position becomes massively unhedged until you rehedge, and the rehedge might execute at a bad price.

This **gap risk** or **overnight risk** is the hidden cost of sparse rehedging. Daily rehedges miss intraday gaps; trading only in certain hours misses overnight moves.

Professionals manage gap risk by using [options](/option/) to hedge the gamma (buying a wider option to cap loss), or by sizing positions to tolerate a plausible gap.

## Relationship to Theta Decay

A short option position loses value daily via **theta**—the option's time decay. A short call loses roughly $50 per day (say) due to theta.

Gamma profit, if realized volatility is as expected, offsets or exceeds theta loss. But sparse rehedging means you miss some volatility, so theta isn't fully offset, and your position bleeds.

Frequent rehedging locks in gamma, but high transaction costs can consume the theta benefit.

The sweet spot is where: (Gamma Profit from Optimal Rehedge Frequency) > (Theta Loss) − (Transaction Costs).

## Rehedging Frequency and Leverage

Traders with leverage (margin) must rehedge more carefully. A sharp overnight gap could trigger a [margin call](/margin-call-forex/), forcing a liquidation at a bad price. This risk incentivizes intraday rehedging—staying closer to delta-neutral to avoid margin breaches.

Unleveraged desks tolerate wider gamma drift.

## Technology and High-Frequency Rehedging

Algorithmic traders rehedge continuously—microseconds after a market move, algorithms adjust delta. This captures maximum gamma profit in liquid markets but only works where:
- Spreads are tight (penny spreads or tighter).
- Commissions are nearly zero.
- Latency is minimal (microseconds).

For manual traders or smaller desks, this is infeasible.

## Practical Decision Framework

To set your rehedging frequency:

1. **Estimate realized volatility** over your holding horizon.
2. **Measure the bid-ask spread** in your underlying and any hedging vehicle.
3. **Calculate the gamma** of your short position (your broker's Greeks will show this).
4. **Solve for break-even rehedges**: if (gamma profit from daily rehedging) > (transaction costs from daily rehedging), then rehedge daily. Repeat for other frequencies.
5. **Account for gap risk**: if overnight gaps are plausible, include their cost, and adjust frequency upward.

For most traders, a delta-threshold rule (rehedge if |delta| > some threshold) is simpler and adapts better than a rigid schedule.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — rate of option value change with underlying price
- [Gamma](/gamma/) — rate of delta change; the crux of gamma trading
- [Theta](/theta/) — daily time decay of option value
- [Option](/option/) — definition and mechanics
- [Bid-Ask Spread](/bid-ask-spread/) — transaction cost of rehedging
- [Derivatives Hedging](/derivatives-hedging/) — broader hedging strategies

### Wider context

- [Volatility Smile](/volatility-smile/) — how implied vol varies by strike
- [Historical Volatility](/historical-volatility/) — realized vol measurement
- [Vega](/vega/) — sensitivity to implied volatility changes
- [Interest Rate Risk](/interest-rate-risk/) — affects option pricing and hedging
- [Margin Call Forex](/margin-call-forex/) — leverage risk from unhedged drift

</div>

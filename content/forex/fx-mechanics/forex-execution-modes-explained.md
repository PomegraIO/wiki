---
title: "Forex Execution Modes: Instant vs Market Execution"
description: "Forex execution modes determine how broker orders fill: instant execution allows requoting while market execution fills at the available price with no broker discretion."
keywords:
  - forex instant execution vs market execution
  - forex order execution modes
  - broker requoting practice
  - market execution forex
  - forex trading mechanics
image: /svg/forex.svg
---

*The **forex instant execution vs market execution** distinction determines whether your broker can reject (requote) your order or must fill it at the market price when the order is triggered. The choice affects slippage, spread, and conflict of interest.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Execution Modes — Comparison</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two paths from order submission to fill; one favors the broker, one favors the trader.</div>

|   |   |
|---|---|
| **Instant execution** | Broker can refuse or requote; fills at broker's offered price |
| **Market execution** | Broker must fill or reject; no requoting; fills at market price |
| **Requoting risk** | High in instant; zero in market execution |
| **Spread control** | Broker sets spread in instant; market spreads in market mode |
| **Slippage** | Common in instant; rare in market execution |
| **Broker incentive** | Instant can widen spreads; market execution limits it |
| **Typical spreads** | Instant: 1–3+ pips; Market: 0.5–1.5 pips |

</aside>

## The Two Models Defined

When you submit a forex order in a retail trading platform, the broker receives it and must decide: fill it as-is, or reject and offer a different price.

**Instant execution** (also called "market execution" in some brokers' marketing, though this is misleading) allows the broker to accept or reject your order. If the market has moved or the broker's liquidity has tightened, the broker can requote you—offer a different price than the one you originally clicked. You can accept the new price or cancel the trade. During volatile news events or low-liquidity hours, requoting becomes frequent and spreads widen dramatically.

**Market execution** (true market execution, not the marketing name) guarantees that your order will either fill at the best available market price or be rejected outright. No requoting. No discretion. The trade either goes through at the current market rate or doesn't—the trader decides within milliseconds. This is also called "no-dealing-desk" (NDD) or "ECN/STP" execution.

## Requoting and Conflict of Interest

Requoting is the key friction. In instant execution mode, a trader submits an order to buy EUR/USD at 1.0900. Between the click and the broker's server receiving it (milliseconds, but real time), the price moves to 1.0905. The broker can choose to:

1. Fill the order at 1.0900 as requested (taking a loss if they've already hedged at a worse price).
2. Requote the trader at 1.0905 or worse.
3. Reject the order entirely with a "unable to execute" message.

This creates a structural conflict of interest. A broker using instant execution has an incentive to widen spreads (the difference between bid and ask) and requote traders during volatile moves. The trader bears the risk of slippage; the broker profits from it.

In market execution, the broker has no discretion to requote. The order either hits the best available bid or ask on the actual forex market (or an ECN liquidity pool), or it's rejected. The trader gets the fill they requested or no fill—no middle ground.

## What Slippage Really Is

Slippage occurs when your order fills at a worse price than the one you saw on your screen. In instant execution, slippage can come from:

- **Genuine market movement** (the price truly moved between your click and the broker's fill).
- **Broker requoting** (the broker widened the spread to capture the move).
- **Latency** (network delay between your order and the broker's server).

In market execution, slippage is typically just genuine market movement. If you order a market order (not a pending order) on an ECN, it fills at the current bid/ask, and that's final. No requoting means no broker-imposed slippage.

## Spreads and Transaction Costs

Instant execution brokers typically quote wider spreads (1–3 pips on major pairs) because they bear inventory risk and can requote to manage it. Market execution brokers (ECN/STP) typically quote tighter spreads (0.5–1.5 pips) because they're passing orders directly to liquidity providers and earning a small commission.

A trader holding a position for hours or days pays the spread each way (buying at the ask, selling at the bid). Over a year of trading, the difference between 1-pip spreads and 3-pip spreads is material.

Market execution brokers often charge a flat commission per round-turn trade (e.g., $10 per 100,000 units). This transparency can be preferable to the hidden cost of wider spreads, though it requires calculation to compare.

## Liquidity Events and Requoting

Requoting spikes during:

- **News releases** (central bank announcements, employment data) when volatility jumps.
- **Low-liquidity hours** (Asia session, weekends).
- **Thin market conditions** (fewer counterparties, wider institutional spreads).

A trader placing a limit order during a major economic announcement on an instant execution platform may face repeated requotes—especially if the order is "against the momentum" (e.g., a sell order as the price rallies). Some brokers may simply reject such orders outright.

Market execution platforms also experience re-quotes in extreme conditions, but they're less common because the broker isn't profiting from requoting—it's just passing market conditions through.

## Pending Orders and Slippage

The difference becomes vivid with pending orders. Say you set a buy limit order for EUR/USD at 1.0850, below the current market price of 1.0900. Price falls, and your order triggers.

**Instant execution:** The broker's server receives the trigger and may requote. If price has fallen to 1.0847, the broker can quote you 1.0847, 1.0845, or reject. You click yes or cancel. Slippage is likely.

**Market execution:** The order fills at the best market price available when the trigger fires—likely 1.0850 or better. No requoting. The fill is what you see.

## The Practical Trade-Off for Retail Traders

For scalpers and news traders, market execution is almost always superior. The elimination of requoting and the tighter spreads mean lower transaction costs and fewer surprises.

For longer-term traders (swing or position traders), the difference matters less. A trader holding for hours or days might not even notice the spread difference. However, market execution platforms are often more expensive (commission-based), so the math must be run per trade size.

For very small accounts, instant execution with wider spreads might be cheaper than market execution's fixed commissions. But as position size grows, market execution's lower per-pip cost typically wins.

## Regulatory Context

[Regulation](/dodd-frank-act/) has increasingly pressured brokers toward transparency. Brokers are now required to disclose execution mode and average spreads. However, "execution mode" is often vague in marketing—some brokers claim "market execution" while still operating an instant execution model.

True market execution platforms typically boast ECN or STP branding, which signals direct connection to institutional liquidity pools rather than broker-provided quotes.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask-spread](/bid-ask-spread/) — How spreads are calculated and vary by liquidity
- [Market-order](/market-order/) — Order type and fill behavior under each execution mode
- [Limit-order](/limit-order/) — Pending orders and their execution mechanics
- [Leverage-ratio-forex](/leverage-ratio-forex/) — Position sizing and margin context
- [Spot-exchange-rate](/spot-exchange-rate/) — Market rate vs broker quote
- [Slippage](/slippage/) — Cost of execution delays and requoting

### Wider context

- [Currency-risk](/currency-risk/) — Why traders hedge and need reliable execution
- [Over-the-counter-market](/over-the-counter-market/) — Decentralized forex market structure
- [Broker](/broker/) — Role and incentive structures in execution
- [Dodd-frank-act](/dodd-frank-act/) — US regulatory framework for forex brokers

</div>

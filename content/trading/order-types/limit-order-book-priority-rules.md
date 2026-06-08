---
title: "Limit Order Book Priority Rules"
description: "How limit order book priority rules determine which orders execute first using price-time priority and pro-rata allocation on exchanges."
keywords:
  - limit order book priority rules
  - price-time priority
  - order queue position
  - order execution sequence
  - matching engine
  - pro-rata allocation
---

*When multiple buyers bid the same price or multiple sellers ask the same price, **limit order book priority rules** determine which order executes first. Most major exchanges use **price-time priority** — the best price wins, and among equal prices, whoever arrived earliest wins — though some venues apply pro-rata methods for large orders or specific asset classes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit Order Book Priority Rules — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Queue position is money: a trader three seconds ahead at the same price gets priority to fill.</div>

|   |   |
|---|---|
| **Primary rule** | Price-time priority on most equity and futures exchanges |
| **Price priority** | Higher bid (buy side) or lower ask (sell side) executes first |
| **Time priority** | Among equal prices, earliest arrival wins |
| **Alternative** | Pro-rata allocation (splits volume by order size, not timestamp) |
| **Applies to** | [Limit orders](/limit-order/) resting in the order book |
| **Market orders** | Execute immediately at best available price; no queue |
| **Exchange variation** | Nasdaq, NYSE, CME, ICE may differ; some have tiered rules |

</aside>

## How Price-Time Priority Works

The order book is a live queue ranked by price first, then time within each price level. On the buy side, the highest bid sits at the front; on the sell side, the lowest ask sits at the front. Within each price level — say, all orders to buy at $50 — they queue by arrival time. The earliest limit order to hit that price gets filled first when a new market order or aggressive limit order arrives.

This is why microseconds matter in professional trading. A trader's buy order posted at 9:30:00.000125 gets priority over an identical buy at $50 placed at 9:30:00.000145, even though both humans perceived them as simultaneous. The exchange's matching engine records timestamps to nanosecond precision and honors them.

Time priority creates a **queue position** — your spot in line. You cannot leap ahead of earlier orders at the same price by canceling and resubmitting. That is why [brokers](/broker/) and exchanges publish their order queue depth: traders want to know how much volume ahead of them must execute before their order fills.

## Price Priority Always Wins

Price priority is inviolate. A sell order at $49.95 never queues behind a sell at $50, even if the $50 order arrived first. The lower price is the "best ask," and it will fill before the higher ask.

Likewise, a buy order at $50.05 gets filled before a buy at $50, regardless of when each arrived. This ensures [price discovery](/price-discovery/) works: the market price reflects the best available rates, not the historical timing of orders.

This matters most when gaps occur. If the market ticks from $50.00 to $50.10, all resting buy orders at $50 that got no fill (because buy demand was light) will not suddenly jump ahead of existing sell orders at $50.09. The $50.09 sellers still wait their turn within the $50.09 level; they do not retroactively become "time priority" over later $50.00 buyers.

## Pro-Rata and Tiered Allocations

Not every exchange uses pure price-time. Futures exchanges and options venues sometimes apply **pro-rata allocation** at a given price level. Instead of filling the oldest order first, the exchange allocates incoming volume proportionally to resting orders' sizes.

Example: at $50, there are resting sell orders of 100 shares (placed at 9:30:00) and 200 shares (placed at 9:30:01). A buy market order arrives for 300 shares. Under price-time, the 100-share order fills first, then 200 of the 200-share order, leaving 0 unfilled. Under pro-rata, the incoming 300 shares split: 100 × (100/300) = 33 shares to the first order, 100 × (200/300) = 67 shares to the second.

Pro-rata discourages "order splitting" — the practice of placing many small orders to jump the queue. But it also weakens time priority, so traders cannot rely on being first. Most equity exchanges (Nasdaq, NYSE) stick with price-time because it is simpler and favors honest market participants over gaming tactics.

Some exchanges use **tiered rules**: pure price-time for retail [orders](/limit-order/), pro-rata above a size threshold, or dedicated price levels for market makers. The CME, for example, applies pro-rata in some futures pits and price-time in others.

## What Triggers Execution?

A resting limit order in the book executes when a new [market order](/market-order/) or aggressive limit order matches it. Market orders **sweep** the book: they consume the best-priced resting orders until the market order is fully filled or the book runs out of supply.

If a buy market order for 500 shares arrives and there are sell orders of 200 at $50.00, 150 at $50.01, and 200 at $50.02, the market order executes: 200 at $50.00 (priority), then 150 at $50.01, then 150 of the 200 at $50.02. The last 50 shares at $50.02 remain resting. No time priority needed here — the market order is "taker," not a "maker" in the book.

Incoming limit orders can also trigger existing orders, but only if they cross the [bid-ask spread](/bid-ask-spread/). A new limit buy at $50.05 does not touch resting sell orders at $50 (it is aggressive and crosses up to the best ask). These aggressive limit orders also execute immediately at the best price, obeying price-time on the sell side.

## Impact on Trading Costs and Latency

Order book priority matters most to traders using [limit orders](/limit-order/). If you place a limit order to buy 1,000 shares and there are already 5,000 shares ahead of you at that price, you will not fill quickly. You might wait for hours or cancel unfilled.

This creates an incentive to either (a) be first by posting early (hence the arms race in execution speed), (b) accept a worse price to move to the front of a less-crowded level, or (c) use a market order to guarantee immediate execution but accept the [bid-ask spread](/bid-ask-spread/).

Latency-sensitive traders exploit this. High-frequency trading firms position servers near exchange data centers to post and cancel orders faster, bumping them ahead of retail or slower institutional traders at the same price. Regulators monitor this but allow it under fair-access rules.

## Special Cases and Exceptions

**Block trades** on alternative trading venues (ATSs) sometimes bypass the order book and execute privately negotiated sizes at agreed prices, then report to the exchange. These do not compete with book orders.

**Depth limits**: some brokers or exchanges publish only the top 10 price levels to prevent information leakage. The full book still applies for matching; you just cannot see all queues.

**Halt and resumption**: when trading halts and restarts, the order book position resets; all orders that were queued are re-posted and ordered by the new open price, not by old timestamps. This prevents pre-halt orders from unfairly dominating the open.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — a price-specific order that rests in the book until filled or canceled
- [Market Order](/market-order/) — executes immediately at best available price, sweeping the book
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between the highest buy and lowest sell, shaped by order book depth
- [Price Discovery](/price-discovery/) — how prices emerge from supply and demand in the order book
- [Market Maker](/market-maker-trading/) — provides liquidity and maintains tighter spreads by posting orders in the book
- [Alternative Trading System](/alternative-trading-system/) — private venues with their own queue rules
- [Latency Arbitrage](/algorithmic-trading/) — exploiting speed differences in order submission

### Wider context

- [Stock Exchange](/stock-exchange/) — where order books are maintained and matched
- [Broker](/broker/) — executes your orders, choosing which venue's book to route to
- [Algorithmic Trading](/algorithmic-trading/) — uses order book data to time submissions and fills
- [Market Impact](/market-risk/) — how large orders affect price while moving through the book

</div>

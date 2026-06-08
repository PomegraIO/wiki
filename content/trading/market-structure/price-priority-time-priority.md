---
title: "Price-Time Priority"
description: "The exchange matching rule that fills better-priced orders first and gives the earliest-arriving orders priority among same-price orders."
keywords:
  - price-time priority
  - order priority
  - price priority
  - time priority
  - exchange matching
  - queue discipline
image: /svg/trading.svg
---

*When multiple sell orders sit in the [limit order book](/limit-order-book/) at different prices, which one gets filled first when a buyer arrives? The answer is governed by **price-time priority**, a simple but foundational rule: fill the best price first; within that price, fill the earliest order first. This rule ensures fairness and [price discovery](/price-discovery/), and it shapes how traders strategize.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Price-Time Priority — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The core rule that determines which order gets filled when multiple orders compete.</div>

|   |   |
|---|---|
| **What it is** | Exchange matching rule: better price always fills first; same price fills by arrival time |
| **Applies to** | All [limit orders](/limit-order/) in the [limit order book](/limit-order-book/) |
| **Price side** | Best bid (highest) fills first; best ask (lowest) fills first |
| **Time side** | Among orders at same price level, earliest timestamp wins |
| **Regulatory basis** | [Reg NMS](/reg-nms-order-protection-rule/); standard on all major US exchanges |
| **Exceptions** | Rare; can be overridden by special order types (not standard) |
| **Stakes** | Critical for fairness and prevents traders from jumping the queue via price manipulation |

</aside>

## The two tiers of priority

Price-time priority has two components, applied in strict order. **Price priority** is absolute: no [limit order](/limit-order/) at a worse price can fill before one at a better price, regardless of arrival time. If a sell limit order sits in the book at $100.00 and another arrives at $99.99, the $100.00 order will fill first when a buyer arrives. The $99.99 order is a worse offer (the seller is accepting less), so it must wait until the $100.00 order is exhausted or cancelled.

**Time priority** operates only within a single price level. If two sell orders both sit at $100.00, and the first arrived at 9:30:00.001 and the second at 9:30:00.002, the first order fills first when a buyer comes along. This is sometimes called "first come, first served" or "fifo" (first in, first out) matching, though that term is less precise since price tier always comes first.

## Why the rule works

Price-time priority has two practical benefits. First, it ensures that every trader receives the best available price without exception. If better prices exist, they are always tried first. This enforces [Reg NMS](/reg-nms-order-protection-rule/)'s principle that no venue can trade at a worse price than the best bid or ask in the system.

Second, it provides fairness and predictability. A trader who places a [limit order](/limit-order/) knows exactly where they stand: ahead of all later arrivals at the same price, and behind only better-priced orders. This predictability encourages traders to place orders and leave them resting, rather than constantly withdrawing and re-entering them to game the queue. The rule also prevents a trader from jumping ahead by any mechanism—no "priority fee" or special status can bump you ahead of better prices.

## The queue and order positioning

Within a single price level, orders form a queue. The oldest order is at the head; new arrivals join the tail. When a [market order](/market-order/) arrives to buy, it consumes the head of the queue—the oldest sell order at the best ask—before touching the second order in line. This queue discipline is enforced by the exchange's matching engine.

Traders place orders strategically with queue position in mind. A trader who wants to fill quickly might place an order at a price slightly better than the current best, jumping ahead to the head of a new price level. A trader willing to wait might place an order at the current best bid or ask, accepting queue position and hoping for a fill later. High-frequency traders obsess over microsecond-level timing to secure the best queue positions at key prices.

## Variations and special order types

Most orders follow standard price-time priority, but some exchanges allow special order types that deviate. A "reserve order" (also called an "iceberg order") shows only a fraction of its size to the book; as the visible portion fills, more is revealed. The timestamp for the hidden portion is often the same as the visible portion, so the entire order shares the same queue position, rather than the fresh batch being treated as a new arrival.

An "all-or-none" order requires the entire size to fill at once or not at all; these orders may be held off the book and matched differently. Some venues offer "post-only" orders that are placed with the express goal of providing liquidity and queue position, not of immediately buying or selling. The regulatory and practical details vary by venue, but the broad principle—better price first, then earliest arrival—is standard.

## Impact on trading strategies

Price-time priority shapes how traders use [limit orders](/limit-order/) versus [market orders](/market-order/). A trader who submits a limit order and hits the best offer is guaranteed to get in front of most later traders at that price. But if prices move against them, they risk being "run over"—a better price arrives and drains their order first.

This has driven algorithmic trading techniques like "order slicing," where a trader submits a limit order for a small amount to test whether the price is real, or uses high-frequency cancellations to maintain queue position without committing to the order. The SEC has periodically scrutinized these strategies as potential market abuse.

## The role in price discovery

Price-time priority contributes to [price discovery](/price-discovery/) by ensuring that the [limit order book](/limit-order-book/) reflects the true supply and demand at each price level. The queue at $100.00 tells other traders how much supply is willing to sell at that price in that order. Knowing the order in which those shares will fill helps traders estimate the impact of their own large orders.

If prices were determined by factors other than price and time—say, a lottery or broker favoritism—traders would lose confidence in the fairness of execution and might demand wider bid-ask [spreads](/bid-ask-spread/) as compensation for execution risk. The simplicity and transparency of the price-time rule supports tighter spreads and deeper markets.

## Enforcement and disputes

Exchanges monitor their matching engines to ensure price-time priority is enforced correctly. A malfunction that violates priority—say, filling a worse-priced order before a better one—is a serious incident and may trigger manual reconciliation or regulatory investigation. For retail traders, disputes about queue position rarely arise because their orders are small and matching is automatic. For large institutional traders, queue position can be worth millions of dollars, and order routing and timing are carefully engineered.

The SEC has also investigated whether certain brokers or venues were failing to enforce price-time priority correctly. Most substantiated violations result in restitution to harmed traders and penalties to the venue.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order Book](/limit-order-book/) — where orders are queued by price-time priority
- [Limit Order](/limit-order/) — the order type subject to this rule
- [Market Order](/market-order/) — executed against the queue
- [Bid-Ask Spread](/bid-ask-spread/) — affected by queue depth
- [Reg NMS Order Protection Rule](/reg-nms-order-protection-rule/) — regulatory framework
- [Price Discovery](/price-discovery/) — enabled by transparent priority

### Wider context

- [Stock Exchange](/stock-exchange/) — enforces matching rules
- [Order Internalization](/order-internalization/) — bypass the queue
- [Broker](/broker/) — must comply with routing and priority rules
- [Algorithmic Trading](/algorithmic-trading/) — uses queue dynamics strategically
- [Market Maker](/market-maker-trading/) — often ahead in the book due to early arrival

</div>

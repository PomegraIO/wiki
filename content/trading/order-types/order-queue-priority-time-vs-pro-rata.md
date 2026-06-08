---
title: "Order Queue Priority: Time-Pro-Rata vs Pure Time"
description: "How time-priority and pro-rata matching algorithms determine fill probability for limit orders in different markets and exchanges."
keywords:
  - order queue priority time pro rata
  - limit order matching algorithm
  - exchange queue priority
  - futures market order matching
  - time-priority versus pro-rata
image: "/svg/trading.svg"
---

*When multiple traders place limit orders at the same price, the exchange's queue-matching algorithm determines who gets filled first — either strictly by time of arrival, or split pro-rata among all orders at that price level. This choice reshapes incentives around order size and order placement speed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Queue Priority — Key Facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and order flow." />

<div class="wiki-infobox-caption">How matching rules reward time, size, or a blend of both.</div>

|   |   |
|---|---|
| **Time-priority (FIFO)** | First order placed is first order filled; size does not matter |
| **Pro-rata matching** | Orders at same price filled proportionally to their size |
| **Hybrid** | Some exchanges use time-first, then pro-rata for remainder |
| **Cancellation speed** | Critical in time-priority; less relevant in pro-rata |
| **Reward for aggressiveness** | Weaker in pro-rata; strong in pure time-priority |
| **Common venues** | Equities (time-priority); many futures (pro-rata) |

</aside>

## Why Queue Priority Rules Matter

When you place a [limit order](/limit-order/) at a price level where other traders are already waiting, you join a queue. That queue decides whether you earn a fill based on arrival sequence or order size. The distinction creates different incentive structures.

In a **time-priority** system, the first trader at a price gets first access when buy or sell interest arrives. Your edge is speed: if you place your order one second before a competitor, you go first. This favors traders with low-latency technology and tight [bid-ask spreads](/bid-ask-spread/).

In a **pro-rata** system, the exchange divides each incoming market order among all resting limit orders at that price, in proportion to their size. If you represent 25% of the total size at a price level, you fill 25% of any incoming volume. Size — not speed — determines your share.

## Time-Priority (FIFO) Mechanics

Equity markets in the United States, including the [NYSE](/new-york-stock-exchange/) and [Nasdaq](/nasdaq/), use strict time-priority for limit orders. The first order to reach the matching engine at a given price level has priority.

This rule has practical consequences. A trader must cancel and resubmit an order to change its terms (quantity or limit price). The new order goes to the back of the queue. In fast-moving markets, this cancellation-and-resubmit cycle can be exploited: a high-speed trader might cancel their order just as a large incoming order approaches, step out of the way, and rejoin the queue after the bulk of that order has filled at less favorable prices for slower traders.

Time-priority encourages:
- **Investment in low-latency infrastructure.** Exchanges collocate servers and offer "co-location" services to let trading firms place hardware near matching engines.
- **Frequent small orders.** Breaking a large order into pieces and releasing them gradually can improve fill prices but risks losing priority by cancelling and resubmitting.
- **Attention to order placement timing.** A fraction of a millisecond matters.

## Pro-Rata Matching

Many [futures contracts](/futures-contract/), especially in the U.S. through the CME and ICE, use pro-rata matching. When an incoming order arrives, it fills resting orders proportionally to their displayed size, regardless of when each was placed.

Under pro-rata rules, if the book at a given price shows orders of 100 contracts, 200 contracts, and 150 contracts (450 total), and a market order for 450 contracts comes in, each resting order fills pro-rata: the first gets 100 shares of the incoming order, the second gets 200, the third gets 150. The order in which they were placed is irrelevant.

This system rewards:
- **Larger order sizes.** Your edge scales with the amount of capital you commit to a resting order.
- **Patience.** Staying in the queue longer and visible is advantageous; you are not racing the clock.
- **Simpler operations.** Cancellation and resubmission don't degrade your position; you are evaluated on size alone.

Pro-rata matching creates different [market-maker](/market-maker-trading/) behavior. Market makers may post larger sizes to guarantee a pro-rata share of flow, whereas in time-priority systems, large orders are a disadvantage because they block smaller orders ahead of them in the queue.

## Hybrid and Variant Approaches

Not all venues are purely time-priority or purely pro-rata. Some exchanges use hybrid schemes:

- **Time-first pro-rata.** An incoming order fills the earliest orders at a price level in full (or in time-priority order) until a threshold is reached, then switches to pro-rata for the remainder.
- **Size-weighted time.** Some systems weight both time and size, creating a blended priority.
- **Volume-weighted price bands.** A few venues use different rules depending on whether orders are within a certain size range.

The CME offers both mechanisms across different product classes, so traders routing to multiple futures must understand each contract's specific matching algorithm.

## Impact on [Order Execution](/price-discovery/) and Strategy

The choice of matching rule influences how traders structure orders:

| Aspect | Time-Priority | Pro-Rata |
|--------|---------------|----------|
| **Small order advantage** | High | Low |
| **Large order advantage** | Low | High |
| **Speed technology value** | Very high | Low |
| **Visible order size effect** | Can hide size (icebergs) | Encourages visible size |
| **Queue jumping incentive** | High | Irrelevant |
| **Cancellation cost** | Severe (lose priority) | None |

In time-priority markets, some traders use [iceberg orders](/limit-order/) — submitting only a small visible quantity while hiding large resting size — to maintain priority without appearing to block the market. In pro-rata venues, iceberg orders are less valuable because hidden size does not count toward your pro-rata share anyway.

## Strategic Implications for Traders

**Time-priority traders** benefit from:
- Algorithmic execution that splits orders into small pieces and times releases for speed.
- Staying in the queue continuously; long waits are rewarded.
- Monitoring the shape and depth of the order book to time placement just before expected flow.

**Pro-rata traders** benefit from:
- Larger position sizes relative to total book size.
- Patient capital that is comfortable sitting in queues for hours or days.
- Understanding the typical rate of order flow so they can size appropriately.

An [algorithmic trading](/algorithmic-trading/) strategy designed for a time-priority venue may underperform in a pro-rata one, and vice versa. Firms routing to multiple venues must maintain different execution tactics for each matching model.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — order type and queue mechanics
- [Market order](/market-order/) — immediate execution, fills from the resting queue
- [Market maker trading](/market-maker-trading/) — provides liquidity and manages queue strategy
- [Algorithmic trading](/algorithmic-trading/) — execution techniques tuned to venue rules
- [Price discovery](/price-discovery/) — how matching rules affect market information flow

### Wider context

- [Futures contract](/futures-contract/) — products that commonly use pro-rata matching
- [Stock exchange](/stock-exchange/) — equities venues predominantly time-priority
- [Nasdaq](/nasdaq/) — major time-priority equity market
- [Over-the-counter market](/over-the-counter-market/) — alternative to exchange queues

</div>

---
title: "Order Queue Priority Rules in Exchange Matching Engines"
description: "Order queue priority rules on exchanges determine which limit orders fill first—price-time, pro-rata, or price-size—affecting your fill probability and execution speed."
keywords:
  - order queue priority rules exchange
  - price-time priority
  - pro-rata allocation
  - price-size priority
  - limit order matching
---

*The **order queue priority rules** set by exchanges determine which [limit orders](/limit-order/) fill first when multiple buyers or sellers are at the same best price. The three main models—price-time priority, pro-rata allocation, and price-size priority—each create different incentives for order timing and sizing, directly affecting a trader's likelihood of execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Queue Priority Rules — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Matching rules shape queue position and execution odds.</div>

|   |   |
|---|---|
| **Price-time priority** | First by price, then by arrival time (most common in equities) |
| **Pro-rata priority** | Share of execution proportional to order size, not time |
| **Price-size priority** | Large orders at the best price rank higher than small ones |
| **Impact on traders** | Timing, size, and venue choice all affect fill probability |
| **Best case** | Early arrival at a price level with price-time priority |
| **Worst case** | Late arrival at pro-rata venue with small order size |

</aside>

## The three main priority models

Exchanges choose one of three core systems to rank orders at the same price level. Each system creates a different "queue" and changes the strategist's calculus.

**Price-time priority** (also called FIFO) is the most common in equities and many futures markets. Orders at the best price fill before orders at worse prices. Within the same price level, orders that arrived first fill before orders that arrived later. If 100 sellers are at $50.00 and you submit a buy order at $50.00, you go behind those 100 sellers in the queue. You fill only after their shares are exhausted. This creates a simple incentive: arrive early at a price level, or don't bother.

**Pro-rata priority** allocates execution proportionally by order size. If the market depth at $50.00 is 10,000 shares split among five sellers, and a buyer comes in with a 5,000-share order, the buyer fills proportionally from each seller based on their size, not the order in which those sellers arrived. A seller with 3,000 shares at $50.00 gets 1,500 of the 5,000 shares filled. Pro-rata systems reward larger orders and reduce the value of being first in time.

**Price-size priority** allocates based on a combination of price and size, often favouring larger orders at the best price. Some exchanges use a hybrid: the largest orders at the best price fill first, then smaller orders. This creates an incentive to post large sizes and can disadvantage small traders.

## How price-time priority shapes the queue

Under price-time priority—the system most equity traders know—the order book is literally a queue. Imagine a [bid-ask spread](/bid-ask-spread-and-execution-cost/) with the best bid at $49.99 and the best ask at $50.00. If three sell orders sit at $50.00 (one for 500 shares, one for 1,000, one for 2,000), they will fill in that order: the 500 first, then the 1,000, then the 2,000. A new sell order arriving at $50.00 goes to the back of the queue.

This system is transparent and predictable. Your fill probability depends on how many shares are ahead of you at your price level and how much volume is hitting that price. If there are 10,000 shares ahead of you at your limit price and a market buy order comes in for 15,000, you fill partially. If a market sell comes in for 5,000, you fill zero.

The time-priority component creates a first-mover advantage. Traders who arrive at a price level early harvest a lower market impact and skip the queue entirely. This is why high-frequency traders pay for co-located servers near exchange matching engines—they want to be first in the queue at a new price level.

## Pro-rata allocation and the size-posting strategy

Pro-rata priority flips the game. Under pro-rata, your queue position depends on your order size relative to others at the same price, not when you arrived. This favours large block orders and discourages both queue-jumping (arriving incrementally to stay ahead) and time-priority arbitrage.

Suppose the ask side has 50,000 total shares at $50.00, divided into ten orders of varying sizes. A large buyer submits a 20,000-share order at $50.00. Instead of filling from the oldest 20,000 shares, the exchange allocates fills from all ten sellers proportionally to their sizes. This means even the most recent seller gets a slice of the fill, as long as they posted a reasonable size.

Pro-rata systems are popular in more illiquid or institutional markets (e.g., futures, some FX venues) where large orders are common and traders prefer to avoid queue-jumping altogether. The disadvantage: small traders with small orders get proportionally tiny fills, incentivizing them to post larger sizes or place [pegged orders](/pegged-order-types/) to get a better share.

## Price-size priority and order book depth

Some venues use price-size priority to reward liquidity posting. An order's rank depends first on price, then on the size it contributes. Larger orders rank higher within the same price level. This system aims to attract visible volume to the order book and reduce the incentive to "hide" large orders in dark pools.

Under price-size priority, a 50,000-share order at $50.00 will fill before a 1,000-share order at the same price, even if the small order arrived first. This creates an incentive for traders to post large, visible sizes. However, it also discourages retail or small-block traders from participating directly; they end up at the back of the queue no matter when they arrive.

## Strategic implications for different trader types

A [market maker](/market-maker-trading/) under price-time priority wants to post the tightest [bid-ask spread](/bid-ask-spread-and-execution-cost/) and sit at the best price. Being first in the queue at a price tier guarantees fills on incoming market orders.

A block trader under pro-rata priority posts a large size, knowing that even if others arrive later, the trader will still get a proportional share of incoming volume. A [small retail trader](/active-etf/) in a price-time system might use [pegged orders](/pegged-order-types/) or [limit orders](/limit-order/) at less popular price tiers to avoid being deep in a queue.

High-frequency traders exploit price-time priority by minimizing latency. In pro-rata systems, the emphasis shifts to size and price discovery. In price-size systems, the focus returns to size, but with less advantage to speed.

## Matching engines and the exchange choice

Each major exchange publishes its queue priority rules. The [New York Stock Exchange (NYSE)](/new-york-stock-exchange/) uses price-time priority for most orders. The [NASDAQ](/nasdaq/) primarily uses price-time priority as well, though some [order types](/limit-order/) have modified rules. Futures exchanges like the Chicago Mercantile Exchange (CME) use variants; some contracts use price-time, while others use pro-rata or a hybrid.

If you trade the same security across two venues with different priority rules, your execution odds change. A 1,000-share limit order at the same price will fill faster at a price-time exchange if you arrive early, but it will fill proportionally faster at a pro-rata exchange if larger orders are present.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — an order that executes only at or better than a specified price
- [Fill-or-Kill Order Explained](/fill-or-kill-order-explained/) — all-or-nothing execution with no queue resting
- [Pegged Order Types](/pegged-order-types/) — orders that automatically track the best bid or ask
- [Bid-Ask Spread as an Execution Cost](/bid-ask-spread-and-execution-cost/) — how spread and depth affect execution
- [Market Order](/market-order/) — an order that fills immediately at the best available price

### Wider context

- [Stock Exchange](/stock-exchange/) — venue that operates matching engine and sets priority rules
- [Market Maker](/market-maker-trading/) — trader who posts bids and offers and benefits from queue position
- [High-Frequency Trading](/high-frequency-trading/) — uses latency arbitrage and queue positioning strategies

</div>

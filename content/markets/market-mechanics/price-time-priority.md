---
title: "Price-Time Priority"
description: "The two-level queue rule that governs order matching in continuous-auction markets: best price first, then earliest arrival at that price."
keywords:
  - price-time priority
  - order matching
  - price level
  - time priority
  - limit order queue
  - fifo matching
image: "/svg/markets.svg"
---

*[Price-time priority](/price-time-priority/) is the fundamental matching rule in continuous-auction [stock exchanges](/stock-exchange/) like the [NYSE](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/). It states that all orders at the best [bid-ask](/bid-ask-spread/) price level are matched in chronological order—earliest arrival first—before any orders at a worse price are considered. This rule ensures fairness, discourages manipulation, and allows traders to understand their position in the queue.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Price-Time Priority — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and mechanics." />

<div class="wiki-infobox-caption">The universal queue rule that determines order execution sequence: highest price (for buyers), lowest price (for sellers), then arrival time.</div>

|   |   |
|---|---|
| **What it is** | Two-tier matching algorithm: best price level first, then chronological (FIFO) at that price |
| **Applies to** | Equities on [NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), and most [exchange](/stock-exchange/) and [ECN](/alternative-trading-system/) venues |
| **Implementation** | Electronic matching engine that compares every incoming order to resting orders in the book |
| **Benefits** | Transparent queue, discourages queue-jumping, fair treatment of similar orders |
| **Exemptions** | [Call auctions](/stock-exchange/) (opening/closing) use different logic; some [alternative trading systems](/alternative-trading-system/) may use other rules |
| **Related rules** | [Trade-through protection](/trade-through-protection/) (no worse-price execution), [locked and crossed markets](/locked-and-crossed-markets/) (price-time prevents exploitation) |

</aside>

## The continuous auction and the order book

Every [stock exchange](/stock-exchange/) maintains an **order book**—an electronic ledger of all unexecuted buy and sell orders. A typical book looks like this:

**BUYERS (bids)**        **SELLERS (asks)**
$50.05 — 500 shares    $50.10 — 1,000 shares
$50.00 — 2,000 shares  $50.15 — 500 shares
$49.95 — 300 shares    $50.20 — 2,000 shares

The best bid (highest buyer price) is $50.05; the best ask (lowest seller price) is $50.10. The [bid-ask spread](/bid-ask-spread/) is $0.05.

In a **continuous auction** (the default mode on most exchanges throughout the trading day), orders arrive stream-by-stream. When a new buy order arrives, the matching engine checks: does it overlap with any sell orders? If yes, it trades. If no, it joins the buy side of the book.

Price-time priority governs this process. It answers two questions:
1. **Which order executes first?** The one at the best price.
2. **If multiple orders sit at the best price, which executes first?** The oldest one.

## Price-level logic

The first tier of price-time priority is straightforward: **price first**.

Suppose a market order arrives to buy 1,000 shares. The matching engine looks at the ask side (the sellers). The best ask is $50.10. The engine matches the new buy order with the resting sell orders at $50.10 first, executing as much as possible at that price. Only after the $50.10 level is fully satisfied does the engine consider $50.15, and so on.

Why? Because traders who placed sell orders at $50.10 are offering the lowest price—the most competitive, the most liquid. By law of [price discovery](/price-discovery/), the market should transact there first. Allowing a worse price to jump the queue would be a trade-through—a violation of basic market integrity.

Similarly, a sell order arriving in the market is matched against buy orders at the *best bid* first ($50.05 in the example), before considering $50.00 or lower.

## Time-level logic (queue position)

The second tier addresses a common tie: what if multiple orders sit at the same price level?

Imagine the ask side has:
- 500 shares @ $50.10, placed at 10:00:00
- 300 shares @ $50.10, placed at 10:00:05
- 200 shares @ $50.10, placed at 10:00:10

When a market buy order for 900 shares arrives at 10:00:30, which sellers match first?

**Price-time priority says: the earliest arrival.** The 500 shares placed at 10:00:00 execute first, then the 300 shares placed at 10:00:05, and finally 100 of the 200 shares placed at 10:00:10.

This fairness principle is called **FIFO** (first-in, first-out). It rewards patience: if you place a [limit order](/limit-order/) willing to sell at $50.10, and no better bids appear, you will execute in the order you arrived, not because you're lucky or connected.

## Why price-time matters for market integrity

Price-time priority is not decorative; it prevents several forms of market abuse:

**Queue-jumping:** Without time priority, a [market maker](/market-maker-trading/) could place an order, then withdraw and re-place it moments later with a new timestamp, jumping ahead of other orders at the same price. This would be unfair and would make the queue unpredictable.

**Layering and spoofing:** High-frequency traders could place large visible orders to create a false impression of supply, then quickly cancel them to disrupt the queue. Price-time priority, combined with surveillance, discourages this.

**Latency arbitrage abuse:** A trader with a faster connection might otherwise place an order and immediately cancel it if the market moved against them, effectively "testing" the book with no risk. Time priority makes such strategies less viable.

By committing orders to the queue in a transparent, predictable way, price-time priority encourages genuine [price discovery](/price-discovery/) and deters short-term manipulation.

## Interaction with market vs. limit orders

**[Market orders](/market-order/)** (buy or sell immediately at any price) bypass the queue. They execute at the best available price, consuming the highest-priced bids or lowest-priced asks, and take the "other side" of someone's resting [limit order](/limit-order/).

**[Limit orders](/limit-order/)** (buy or sell only at a specified price or better) join the queue at a price level. They sit in the book, waiting to be matched.

Price-time priority applies to the resting [limit orders](/limit-order/). When a [market order](/market-order/) or an aggressive [limit order](/limit-order/) arrives, it matches resting [limit orders](/limit-order/) in price-time order. The oldest [limit order](/limit-order/) at the best price executes first; the newer ones wait.

This is why [limit order](/limit-order/) placement time is crucial. A trader who places a sell [limit order](/limit-order/) at $50.10 at 10:00:00 will execute ahead of a trader who places at $50.10 at 10:00:01, assuming no better bids arrive between placements.

## Open-outcry (floor) trading and price-time

Most [stock exchanges](/stock-exchange/) today are fully electronic and implement price-time priority through software. But historically, open-outcry (human) trading on the [NYSE](/new-york-stock-exchange/) floor also followed price-time concepts. A [specialist](/stock-exchange/) (the human market maker) would match buy and sell orders at the best price, then in time order.

Open-outcry is nearly extinct, but the principle endures: fairness and transparency require that orders at the same price are not randomly chosen. They must follow a predictable rule, and chronological order is the fairest and most enforceable rule.

## Exceptions: call auctions

Price-time priority applies during **continuous trading** (the default mode). But at the [opening and closing auctions](/stock-exchange/) on [NYSE](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/), a different rule applies: all orders (regardless of arrival time) at the opening or closing price execute simultaneously at the same price, without regard to time.

This makes sense: the opening [auction](/stock-exchange/) aggregates overnight orders, and an order placed at 9:20 am is no more "early" than one placed at 9:25 am if both were waiting for the 9:30 am open. The time-priority rule re-engages once continuous trading begins.

## Implementation and the electronic era

Modern exchanges execute price-time priority through **matching engines**—software that processes incoming orders in nanosecond-scale intervals. The engine assigns a timestamp to every order (based on the exchange's clock, synchronized to nanosecond precision) and uses that timestamp as the tiebreaker at each price level.

This precision matters. Two orders might appear simultaneous to a human eye, but the matching engine sees one as arrived 1 microsecond before the other and places it higher in the queue. Traders pay for co-location (placing their servers next to the exchange's servers) to shave microseconds off latency and improve queue position.

The result is that price-time priority, though described simply, operates at the edge of human perception. A trader cannot queue-jump through misbehaviour; the system is automatic and verifiable.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — The price gap that price-time priority helps minimize through fair execution.
- [Trade-Through Protection](/trade-through-protection/) — The complementary rule ensuring orders don't skip price levels to worse prices.
- [Locked and Crossed Markets](/locked-and-crossed-markets/) — Anomalies that price-time priority (via venue rules) helps prevent.
- [Circuit Breaker and Trading Halt](/circuit-breaker-trading-halt/) — Rules that pause trading and reset the queue during extreme volatility.
- [Market Order](/market-order/) — An order that executes immediately, matching against resting orders by price-time.
- [Limit Order](/limit-order/) — An order that joins the queue and waits to be matched in price-time sequence.
- [Market Maker Trading](/market-maker-trading/) — The professionals who continuously quote and interact with the price-time queue.

### Wider context

- [Stock Exchange](/stock-exchange/) — The venue where price-time priority is enforced via the matching engine.
- [Price Discovery](/price-discovery/) — The continuous process of finding equilibrium, fair through price-time fairness.
- [Alternative Trading System](/alternative-trading-system/) — ECNs and other venues that may implement price-time priority differently.
- [SEC](/securities-and-exchange-commission/) — The regulator that mandates price-time rules via Reg NMS.
- [Equity ETF](/equity-etf/) — Baskets of stocks whose individual components all use price-time matching.

</div>

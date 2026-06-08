---
title: "Queue Priority in a Limit Order Book"
description: "Queue priority in a limit order book determines which resting orders fill first. Price-time, pro-rata, and hybrid rules reward early placement or large stakes differently."
keywords:
  - queue priority limit order book
  - price-time priority trading
  - pro-rata allocation
  - market order execution
  - order book priority rules
---

*When a market order hits a **limit order book**, it does not fill all resting orders at that price equally. The queue—the ranking of which orders fill first—is determined by the exchange's **priority rule**: price-time (first-in-first-out by arrival), pro-rata (allocated by size), or a hybrid. Different rules reward different strategies and affect the incentive to post passive liquidity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Queue priority in limit order books — Three main rules</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">How the exchange decides who gets filled when liquidity is tight.</div>

|   |   |   |
|---|---|---|
| **Rule** | **Example** | **Incentive** |
| **Price-time** | FIFO within price level; earliest order fills first | Post early, be passive |
| **Pro-rata** | Allocate by size, not arrival; largest order fills first | Post large size, be aggressive |
| **Price-broker-time** | Pro-rata within broker, then time across brokers | Rewards broker flow concentration |
| **Used by** | NYSE, NASDAQ, CME | LSE, Eurex | |
| **Advantage** | Predictable, simple, rewards patience | Rewards size, discourages spoofing | |
| **Disadvantage** | Encourages queue-jumping, layering | Can discriminate against small orders | |

</aside>

## The limit order book and passive/aggressive fill

When a trader submits a [limit order](/limit-order/), it waits ("rests") in the order book. When a [market order](/market-order/) arrives from another trader, it consumes the waiting liquidity. The question is: which resting limit order gets filled?

If there are multiple limit orders at the best price, a priority rule decides. This matters enormously because:

- **Passive traders** (those who posted limit orders) want to know their probability of being filled, which depends on queue position.
- **Predatory traders** want to avoid paying for stale liquidity; they want to fill against the oldest, potentially least-informed orders.
- **Liquidity providers** (market makers, prop traders) need predictable queue rules to price their bids and offers.

The venue chooses the rule. No universal standard exists.

## Price-time (FIFO) priority

The **price-time rule**, also called FIFO (first-in-first-out), prioritizes resting orders by (1) price (best bids and offers first) and then (2) time of arrival. The earliest order at a given price fills before later arrivals at the same price.

**Example**: The limit order book shows three bids at $100:

- Order A (yours): 100 shares, entered at 9:30:05 AM
- Order B: 200 shares, entered at 9:30:08 AM
- Order C: 50 shares, entered at 9:30:10 AM

A market sell order for 250 shares arrives at 9:30:15 AM. Under price-time:

- Order A fills 100 shares (first arrival)
- Order B fills 150 shares (200 available, but only 150 left to fill)
- Order C does not fill (no shares remaining)

Price-time is **deterministic and transparent**. You know your position in the queue the moment your order is accepted.

**Used by**: NYSE, NASDAQ, CME (equities and futures), most traditional stock exchanges.

**Strengths**:
- Simple for traders to understand: post early, rest patiently, you will be filled first.
- Discourages aggressive manipulation (you cannot jump ahead by resubmitting).

**Weaknesses**:
- Incentivizes queue-jumping: traders submit many small orders to "get in line," then cancel and resubmit later orders to move to the front. This clutters the book.
- Layering: a trader might place a large visible order early, then layer smaller orders behind it, hoping the large order gets hit and the smaller orders follow. The smaller orders are then canceled.
- Latency arbitrage: high-frequency traders can observe fills and react faster than slower traders, effectively jumping ahead.

## Pro-rata priority

The **pro-rata rule** allocates incoming fill volume to resting orders proportionally to their size, not by arrival time. The largest orders get the most fill.

**Example**: Same book as before:

- Order A (yours): 100 shares at $100, time 9:30:05
- Order B: 200 shares at $100, time 9:30:08
- Order C: 50 shares at $100, time 9:30:10

A market sell for 350 shares arrives. Total resting size at $100 is 350 shares (100 + 200 + 50).

Under pro-rata, the incoming order fills proportionally:
- Order A gets (100 / 350) × 350 = 100 shares
- Order B gets (200 / 350) × 350 = 200 shares
- Order C gets (50 / 350) × 350 = 50 shares

All three orders are partially filled in proportion to their posted size.

**Used by**: Eurex (European equity derivatives), LSE (some venues), CBOE (options).

**Strengths**:
- Rewards market makers and large liquidity providers for posting size, incentivizing passive liquidity.
- Reduces incentive to layer or queue-jump (size, not arrival, determines fill).
- Each order has a predictable fill rate based on its share of total depth at the price level.

**Weaknesses**:
- Unclear until the fill happens: a trader posting 100 shares does not know upfront whether they will get 50 or 100 fills.
- Incentivizes posting lots of small orders instead of one large order (to avoid the pro-rata dilution). This fragments the book.
- Potentially unfavorable for retail or algorithmic traders with smaller, frequent orders.

## Price-broker-time (hybrid)

Some venues use **price-broker-time** (also called depth then time), a hybrid:

1. Orders are ranked by price (best bids/offers first).
2. At each price, orders from different brokers are allocated pro-rata by size.
3. Within each broker, orders are allocated FIFO by arrival.

This accommodates broker consolidation (large brokers may have multiple orders in the book from different clients) while rewarding aggregate broker size.

**Used by**: Some Eurex-listed products, Nasdaq MRX (options).

**Effect**: A large broker with multiple small orders at a price level might get priority over a smaller broker with one large order, because the large broker's aggregate size is measured across its clients.

## Order book priority and strategy incentives

The priority rule shapes behavior:

**Under price-time**:
- Traders want to "get in line" early, creating a race to post at the open.
- Market makers post defensive, small quantities to avoid being hit too quickly.
- Stale orders (submitted long ago) are valuable; they fill first. This is why high-frequency traders can exploit order book structure by observing old orders that are about to move.

**Under pro-rata**:
- Traders want to post *size* to increase fill probability, not just arrive early.
- Market makers post larger spreads but bigger sizes, confident they will get allocated a share of the incoming flow.
- Queue position is less valuable because size matters more.

## Latency and real-world complications

In practice, **latency arbitrage** undermines both rules. A faster trader can observe that a market order has been sent and react before slower traders see the fill. On truly electronic exchanges with negligible latency dispersion, this is minimal. But on venues with significant latency variation, it becomes a real tax on slower participants.

Additionally, many markets have **peak-queue** or **queue-jump** protection rules: if too much order flow is arriving in quick succession, the exchange might reset allocation rules or impose delays to prevent gaming. These vary by exchange.

## Worked example: market impact and queue position

Imagine you are a liquidity provider deciding how to post size in a stock:

**Scenario 1: Price-time venue (e.g., NASDAQ)**

You post 10,000 shares at the bid at 10:00:00 AM. You are first in queue. At 10:00:05 AM, another provider posts 20,000 shares at the same bid. At 10:00:15 AM, a $2 million market sell order hits the bid. Your 10,000 shares fill first, then 10,000 of the second provider's 20,000 shares fill.

Your advantage is being early. You managed queue position risk by arriving first.

**Scenario 2: Pro-rata venue (e.g., Eurex)**

You post 10,000 shares, the other provider posts 20,000 shares. The $2 million market order hits. You are allocated (10,000 / 30,000) × 30,000 = 10,000 shares; the other provider gets 20,000. Size determined it, not arrival.

Your advantage is size. You must post enough to guarantee fill, so you might post 20,000 shares instead, accepting more risk in return for a larger allocation.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — An order to buy or sell at a specific price or better, which waits in the book
- [Market Order](/market-order/) — An order to buy or sell immediately at the best available price
- [Bid-Ask Spread](/bid-ask-spread/) — The gap between the best bid and offer; queue priority affects it
- [Market Maker](/market-maker-trading/) — Liquidity providers who depend on queue rules to manage risk
- [Order Book](/limit-order/) — The book of resting orders; its structure and priority rules

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — Automated strategies that exploit queue mechanics
- [Market Microstructure](/price-discovery/) — The mechanics of how trades happen and prices form
- [Latency Arbitrage](/execution-risk/) — Faster traders exploiting slower ones
- [Execution Risk](/execution-risk/) — Uncertainty in filling an order
- [Stock Exchange](/stock-exchange/) — The venue that sets and enforces priority rules

</div>

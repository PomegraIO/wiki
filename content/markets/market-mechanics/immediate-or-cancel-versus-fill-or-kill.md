---
title: "Immediate-or-Cancel vs Fill-or-Kill Mechanics"
description: "How these two all-or-none immediacy instructions differ in whether partial fills are accepted and how each interacts with order-book sweep logic."
keywords:
  - immediate-or-cancel
  - fill-or-kill
  - order types
  - order execution
  - partial fills
image: "/svg/markets.svg"
---

*An **Immediate-or-Cancel (IOC)** order accepts partial fills against available [market](/stock-market/) depth and cancels any unmatched remainder instantly, whereas a **Fill-or-Kill (FOK)** order rejects the entire order if it cannot execute in one atomic trade without queuing. Both order types demand immediate [price discovery](/price-discovery/), but differ in flexibility: IOC is more forgiving, FOK is all-or-nothing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">IOC vs FOK — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for financial market mechanics." />

<div class="wiki-infobox-caption">Two immediacy order instructions that enforce instant execution or cancellation, with different thresholds for acceptable fill ratios.</div>

|   |   |
|---|---|
| **What they are** | Time-in-force rules that demand immediate execution or instant cancellation |
| **IOC meaning** | Immediate-or-Cancel: fill what you can, cancel the rest |
| **FOK meaning** | Fill-or-Kill: fill all or nothing |
| **Partial fills** | IOC allows them; FOK prohibits them |
| **Queuing** | Neither order queues; both expire if not instantly executable |
| **Order book interaction** | IOC sweeps available liquidity; FOK checks total depth first |
| **Use case** | IOC for block traders, FOK for ultra-time-sensitive strategies |
| **Exchange support** | Most [U.S. stock exchanges](/stock-exchange/) and [Nasdaq](/nasdaq/) support both |

</aside>

## The immediate-or-cancel order

An **Immediate-or-Cancel (IOC)** order arrives at the [exchange](/stock-exchange/) and executes instantly against all available [liquidity](/liquidity-risk/) at the best available [price](/price-discovery/). Whatever portion of the order is not filled against the standing [limit order](/limit-order/) book is cancelled; it does not post as a new [bid](/bid-ask-spread/) or ask on the [order book](/limit-order/).

Suppose you submit a buy IOC for 50,000 shares at $100 or better. The [exchange](/stock-exchange/) sweeps the [order book](/limit-order/) from top to bottom:

- 10,000 shares are available at $99.99 — matched.
- 20,000 shares are available at $100.00 — matched.
- Only 15,000 shares remain at $100.01.
- Your IOC accepts 30,000 shares total and cancels the remaining 20,000 shares.

The IOC order never sits on the [order book](/limit-order/); it is inherently aggressive and executes at whatever prices are currently displayed. This mechanic appeals to algorithmic traders and block traders who want to **sweep liquidity** from an equity or [bond](/bond/) [limit order](/limit-order/) book without leaving a footprint for other traders to react to.

## The fill-or-kill order

A **Fill-or-Kill (FOK)** order is stricter. It checks the entire [order book](/limit-order/) to confirm that the full requested quantity is available at acceptable prices *before* executing anything. If the full order cannot be matched in a single transaction, the entire FOK is cancelled immediately—no partial fills.

Using the same example: you submit a buy FOK for 50,000 shares at $100 or better. The [exchange](/stock-exchange/) conducts a **pre-trade check** to determine whether 50,000 shares exist at or better than $100. If only 30,000 are available at that price level or better, the entire FOK cancels. Zero shares trade; the order vanishes.

FOK is atomic—all or nothing. It is used by traders with extreme time sensitivity or those whose strategy requires committing to a trade size without scaling back. A hedge fund executing a [merger](/merger/) arbitrage hedge, for instance, might use FOK: they need the full position executed at a known price, or they would rather cancel and reassess.

## How they differ in order-book sweep logic

The distinction matters during high-volatility or illiquid periods:

| Feature | IOC | FOK |
|---------|-----|-----|
| Accepts partial fills | Yes | No |
| Leaves orders on book | No | No |
| Checks full depth before executing | No | Yes |
| Cancels remainder on first unfilled portion | Yes (automatic) | Entire order (if any shortfall) |
| Time to execution | Immediate | Immediate or instant cancellation |

**IOC is greedy**: it takes what it can get and walks away. **FOK is disciplined**: it confirms the full prize is available before committing.

## Market-maker and liquidity interactions

[Market makers](/market-maker-trading/) and [brokers](/broker/) see IOC and FOK orders differently. An IOC is often interpreted as a **sweep order** that will consume all visible liquidity at multiple price levels—[market makers](/market-maker-trading/) expect to be partially filled if they are not at the absolute best price. By contrast, a FOK signals that the submitter has already evaluated total available depth and wants the full amount or nothing.

In practice, **most liquidity-seeking orders are IOC**, not FOK. An IOC allows a trader to grab most of an intended position quickly while canceling the unfilled remainder; the trader can then resubmit smaller IOC orders to chase remaining shares. FOK is rarer and often signals either a time-critical decision (must have all 100,000 shares *now*) or a liquidity test (checking whether a large block can be absorbed at all).

## Interaction with circuit breakers and market volatility

During periods of high [volatility](/market-risk/), exchange circuit breakers may widen acceptable price bands or impose temporary halts. IOC orders submitted during these windows are more likely to experience slippage—they execute at worse prices as [market makers](/market-maker-trading/) widen [spreads](/bid-ask-spread/) to manage inventory risk.

FOK orders, meanwhile, may simply cancel during stress because the pre-trade check fails. This is actually a feature: FOK prevents traders from accidentally over-committing at panic prices. IOC, by contrast, can result in surprisingly bad fills during crashes—a trader expecting 50,000 shares at roughly $100 might end up with a mix: 30,000 at $99, 15,000 at $101, and 5,000 at $103, all within milliseconds.

## The distinction from all-or-none and good-til-date orders

IOC and FOK should not be confused with **all-or-none (AON)** orders, which are willing to queue on the [order book](/limit-order/) until the full quantity is matched (or a time threshold expires). AON trades away immediacy for the guarantee that if the trade executes, it is all 50,000 shares or nothing.

Similarly, **good-til-date (GTD)** orders sit on the [order book](/limit-order/) for hours or days, waiting for someone to cross them. Neither IOC nor FOK has that patience; both expire if not instantly executable.

## Practical use cases

**IOC** dominates:
- Algorithmic traders executing large positions in tranches
- Block traders sweeping liquidity from multiple venues
- High-frequency traders capturing brief price dislocations
- Retail traders using routers that split orders across multiple [exchanges](/stock-exchange/)

**FOK** is niche:
- Ultra-time-sensitive hedges (e.g., during a [merger](/merger/) announcement)
- Traders testing whether a rumoured large block is genuinely available
- Execution brokers who must guarantee a client a full fill at a known price or cancel entirely
- Options traders during final seconds before [expiration](/expiration-date/), where the time value is near zero and any partial execution ruins the risk profile

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — Order resting on the book at a specified price, often swept by IOC orders
- [Market order](/market-order/) — Aggressive order filled immediately, similar in immediacy to IOC
- [Bid-ask spread](/bid-ask-spread/) — The cost of immediacy captured by IOC orders
- [Order book](/limit-order/) — The book of resting bids and asks that IOC and FOK sweep against
- [Stock exchange](/stock-exchange/) — Venue that matches IOC and FOK orders
- [Algorithmic trading](/algorithmic-trading/) — Automated systems that frequently use IOC to execute large positions
- [Market maker](/market-maker-trading/) — Dealer who receives and processes IOC and FOK orders

### Wider context

- [Price discovery](/price-discovery/) — The process of finding true market price through order execution
- [Nasdaq](/nasdaq/) — Exchange supporting both IOC and FOK order types
- [New York Stock Exchange](/new-york-stock-exchange/) — Exchange with IOC and FOK support
- [Liquidity risk](/liquidity-risk/) — Risk that IOC fills at worse prices during low-liquidity periods
- [Market risk](/market-risk/) — Risk that spreads widen and FOK orders cancel during volatility
- [Merger](/merger/) — Event that may trigger time-sensitive FOK orders

</div>

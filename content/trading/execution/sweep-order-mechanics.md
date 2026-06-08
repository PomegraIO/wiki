---
title: "Sweep Order Mechanics"
description: "Sweep-to-fill orders simultaneously hit multiple exchanges or price levels to fill large quantities quickly, routing across venues under Reg NMS intermarket sweep rules."
keywords:
  - sweep order mechanics
  - sweep to fill order
  - intermarket sweep order
  - iso order
  - multiple venue execution
  - reg nms sweep rules
image: "/svg/trading.svg"
---

*A **sweep order** (or sweep-to-fill order) is an execution instruction that simultaneously routes buy or sell orders to multiple trading venues or price levels to quickly accumulate a large quantity. This strategy is particularly useful for institutional traders who need to fill substantial positions without being forced to wait at a single venue or accept a deteriorating [bid-ask spread](/bid-ask-spread/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sweep Order Mechanics — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A coordinated multi-venue execution designed to source large quantities while respecting best-price rules.</div>

|   |   |
|---|---|
| **Definition** | An order that simultaneously accesses multiple exchanges or price levels to fill a large size |
| **Typical use case** | Institutional block execution, large position entry/exit |
| **Execution style** | Sequential or near-simultaneous fills across venues |
| **Regulatory framework** | SEC Regulation NMS Intermarket Sweep Rule (Rule 10b-5) |
| **Key advantage** | Speed and volume accumulation without queue wait |
| **Primary cost** | Partial fills at inferior prices on secondary venues |
| **Venue routing** | NYSE, NASDAQ, regional exchanges, market-makers, dark pools |

</aside>

## What a Sweep Order Does

When a trader needs to buy or sell a block so large that a single venue can't (or won't) fill it all at the best available price, a sweep order distributes the order across multiple destinations simultaneously. Rather than submitting a 500,000-share buy order to one exchange and waiting to see if it fills, the trader's algo splits the order: perhaps 100,000 to NASDAQ, 150,000 to NYSE, 100,000 to a regional exchange, and 150,000 to a [market maker](/market-maker-trading/) or [broker](/broker/).

Each destination receives an order to buy at (or sometimes above) the national best bid price. If NASDAQ's best offer is $50.02 and NYSE's best offer is $50.03, a sweep order might hit both simultaneously—purchasing the available quantity at NASDAQ at $50.02 and then sweeping to NYSE at $50.03 to get more shares. The trader accepts some "price improvement" loss (paying higher prices on secondary venues) in exchange for filling quickly and accumulating the full block without waiting.

The distinguishing feature is simultaneity or near-simultaneity. The orders are executed in a tight sequence—milliseconds apart—rather than sequentially, where you'd fill venue A, then check venue B, then check venue C. This parallel approach is what allows large orders to find liquidity across the market without creating unnecessary delays.

## Intermarket Sweep Rule (Reg NMS Context)

The SEC's Regulation National Market System (Reg NMS) set rules about how and when a [broker](/broker/) or trader can use sweep orders. Specifically, the Intermarket Sweep Rule (Rule 10b-5) permits traders to bypass the ordinary sequencing of orders across venues—the traditional "best price first" rule—provided they simultaneously sweep all venues.

Here's the regulatory logic: Under the standard best execution rule, if NASDAQ has shares for sale at $50.02 and NYSE has shares at $50.03, you must hit NASDAQ first. This protects retail and small traders from being jumped ahead of better prices. However, if you're an institutional trader and you need a large block, waiting to hit NASDAQ, then NYSE, then every other venue sequentially would take forever and could allow the market to move against you.

The Intermarket Sweep Rule carves out an exception: if you're prepared to send orders to *every* venue with a published quote simultaneously, you don't have to wait for each one to execute in sequence. This is the legal backbone of sweep-order execution.

In practice, a [broker](/broker/) or [algorithmic trading](/algorithmic-trading/) system must ensure that:
1. The sweep order is sent to all material venues at approximately the same time.
2. Each venue receives an order priced at least at the national best bid or offer, not below it.
3. The trading system or broker documents and maintains records of the sweep.

## How Sweep Orders Get Routed and Filled

When you submit a sweep order through your broker or execution venue, the order typically goes to an execution algo that breaks it into pieces and routes across venues. The routing logic considers:

- **Liquidity available at each venue:** How many shares is each exchange, market maker, or dark pool offering at the best price?
- **Latency and reliability:** Which venues can be reached fastest and most reliably?
- **Market depth:** Are there additional shares available at the next price level on any venue?

For a 500,000-share buy order, the algo might discover:
- NASDAQ has 80,000 shares at $50.02
- NYSE has 120,000 shares at $50.02
- Citadel (a large [market maker](/market-maker-trading/)) has 150,000 shares at $50.03
- A dark pool has 100,000 shares at $50.02

The sweep algo routes orders to all four destinations. NASDAQ and NYSE and the dark pool fill at $50.02; Citadel fills at $50.03. Total execution: 450,000 shares. If more shares are needed, the algo might widen prices or route to additional venues.

The entire sequence—from order submission to final confirmation—can occur in a few hundred milliseconds.

## Sweep Orders vs. Iceberg Orders

A [sweep order](/bid-ask-spread/) is sometimes confused with an iceberg order, but they're different tools. An iceberg order is a single large order that is internally broken into small, visible "chunks" at a single venue. You submit an iceberg order for 500,000 shares, but only 50,000 is visible to the market at any one time. As that 50,000 fills, the next 50,000 becomes visible.

A sweep order, by contrast, is explicitly multi-venue from the start and doesn't hide its size; it immediately reaches out to multiple exchanges or market makers. Icebergs are useful when you want to minimize market impact by hiding your size; sweeps are useful when you want speed and can tolerate some price concessions.

Some execution strategies combine the two: use an iceberg at your primary venue while simultaneously sweeping other venues for additional liquidity.

## When Sweeps Work Best

Sweep orders are most effective in liquid, widely-distributed markets. If you're buying large caps or [indices](/sp-500-index/) where every major exchange and market maker trades the security, a sweep can tap a broad pool of liquidity. The more venues that have competing quotes, the more likely a sweep will find enough size without pushing prices too far.

In less liquid securities or during volatile market conditions, a sweep might exhaust the available liquidity at the best prices and force you to pay more on secondary venues. Some traders use sweeps for the first phase of a large order (getting the "easy" liquidity across multiple venues) and then switch to a more patient algorithm (like VWAP or POV) for the remaining size.

In highly fragmented markets—where liquidity is scattered—sweeps can be very effective because they can tap many small pockets of supply or demand simultaneously. In centralized markets with a dominant exchange, sweeps are less valuable because most liquidity sits in one place anyway.

## See also

<div class="wiki-seealso">

### Closely related

- [Arrival Price Benchmark in Trading](/arrival-price-benchmark-trading/) — how sweep execution performance is measured
- [Market Maker Trading](/market-maker-trading/) — the other side of sweep orders; how market makers provide liquidity
- [Algorithmic Trading](/algorithmic-trading/) — the execution strategies and systems that implement sweeps
- [Bid-Ask Spread](/bid-ask-spread/) — the immediate cost of trading across venues
- [Liquidity Risk](/liquidity-risk/) — why large orders may not find depth at a single venue

### Wider context

- [Stock Exchange](/stock-exchange/) — the venues being swept
- [Broker](/broker/) — the intermediary responsible for complying with sweep rules
- [Best Execution](/fair-value/) — the regulatory principle underlying Reg NMS and sweep rules
- [Market Microstructure](/fair-value/) — how order routing and venue fragmentation evolved

</div>

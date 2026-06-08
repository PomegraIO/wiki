---
title: "Minimum Quantity Order"
description: "An order instruction that cancels if fewer than a specified number of shares can be filled."
keywords:
  - minimum quantity order
  - all-or-nothing order
  - order routing
  - order types
  - execution instruction
image: "/svg/trading.svg"
---

*A **minimum quantity order** is an [order](/stock-exchange/) instruction requiring a broker to cancel the entire [limit order](/limit-order/) if the specified minimum number of shares cannot be filled immediately. This type of instruction protects traders from receiving partial fills that fall short of their intended position size.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Minimum Quantity Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading execution." />

<div class="wiki-infobox-caption">A conditional order instruction designed to prevent undersized fills.</div>

|   |   |
|---|---|
| **What it is** | An order with a minimum-fill threshold; if unfilled in full, it cancels |
| **Also called** | All-or-nothing (AON); minimum execution size |
| **Who uses it** | Institutional traders, portfolio managers, algorithmic systems |
| **Related to** | [Limit order](/limit-order/), [Market order](/market-order/), Order routing |
| **Trade-off** | Lower execution certainty for certainty of position size |

</aside>

## How it works

A minimum quantity order specifies two numbers: the total size the trader wishes to buy or sell, and the minimum number of shares that must be filled in a single execution. If the [broker](/broker/) cannot match at least that minimum, the order is rejected or cancelled rather than partially filled.

Example: a trader places an order to buy 10,000 shares of a stock with a minimum of 8,000 shares. If only 7,000 shares are available at the limit price, the entire order is cancelled. The trader either accepts 10,000 shares or receives nothing at that price level.

This instruction is most common in equity markets where [market impact](/market-risk/) and partial fills create fragmentation costs. A [limit order](/limit-order/) without a minimum might fill 3,000 shares at $50.00, leaving the trader with a smaller position than intended and forcing a second, separate order.

## Why traders use them

The primary motive is operational simplicity. Managing multiple small fills across different venues and times introduces settlement complexity, tracking overhead, and exposure timing mismatch. A minimum quantity order eliminates the half-filled position that requires immediate re-execution.

For portfolio managers running [tactical asset allocation](/asset-allocation/) shifts, receiving 60% of the desired position in one price window and needing to chase the remaining 40% at potentially worse prices is inefficient. The minimum quantity instruction ensures the manager either receives the full intended exposure or preserves cash and liquidity for other decisions.

Institutional traders also use minima to enforce internal risk controls. A portfolio manager might require that any position addition be at least 5,000 shares to justify the compliance, valuation, and reporting overhead.

## Execution mechanics

Most brokers and [market makers](/market-maker-trading/) can accept and honour minimum quantity riders on orders. The instruction is typically flagged in the order message sent to the venue—marked as an AON (all-or-nothing) order or tagged with the minimum share count.

On an [exchange](/stock-exchange/), an all-or-nothing order sits in the order book but executes only when the aggregate available liquidity at the order price meets or exceeds the stated minimum. If it never does within a set time window (often a single trading day), the order expires unfilled.

In [over-the-counter (OTC) markets](/over-the-counter-market/), the trader's broker negotiates with [counterparty](/counterparty-risk/) dealers and may attempt to source the full quantity from a single dealer or bundle multiple dealer quotations. If the minimum cannot be met, the trade is typically declined.

## Trade-offs and risks

The primary trade-off is execution certainty. By insisting on a minimum fill, the trader accepts a higher probability of no fill rather than a partial fill. In illiquid or fast-moving markets, a strict minimum might mean the order expires without execution while prices move away.

For small or narrowly-traded securities, a high minimum can be impractical—if average daily volume is 20,000 shares and the trader requires a 15,000-share minimum, execution becomes contingent on market depth that may not materialise frequently.

Additionally, some venues charge higher fees or apply different handling to all-or-nothing orders, recognising the operational complexity of monitoring and expiring them at order expiration.

## Variants and related instructions

An **all-or-nothing (AON) order** is the strictest form: the entire order size is the minimum. There is no partial fill under any circumstance.

A **good-for-the-day (GFD) order** with a minimum quantity allows the minimum to be met across multiple partial fills throughout a single trading day, provided each partial fill respects the per-transaction minimum.

**Iceberg orders** (also called reserve orders) use a different mechanism: only a visible portion of the order is displayed in the order book, and additional shares are revealed as the visible portion fills. Iceberg orders are designed to hide total intention from the market to reduce market impact, not to enforce a fill minimum.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — an order executed only at a specified price or better
- [Market order](/market-order/) — an order executed immediately at the best available price
- Order routing — the process of directing an order to a trading venue
- [Execution shortfall decomposition](/execution-shortfall-decomposition/) — breaking total cost into delay, impact, and timing components
- [Pre-trade analytics](/pre-trade-analytics/) — modelling expected costs and market impact before submission
- [Market maker trading](/market-maker-trading/) — dealers who provide continuous bid-ask liquidity

### Wider context

- [Broker](/broker/) — an intermediary executing orders on behalf of clients
- [Stock exchange](/stock-exchange/) — a regulated venue for buying and selling securities
- [Over-the-counter market](/over-the-counter-market/) — decentralised trading between dealers outside exchanges
- [Counterparty risk](/counterparty-risk/) — the risk that a trading counterparty fails to settle
- [Bid-ask spread](/bid-ask-spread/) — the difference between buying and selling prices
- [Market impact](/market-risk/) — the cost of moving market prices through large orders

</div>

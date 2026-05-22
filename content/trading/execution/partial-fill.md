---
title: "Partial Fill"
description: "Execution of only a portion of an order when full immediate execution is unavailable."
keywords:
  - partial fill
  - order execution
  - liquidity constraint
  - remaining order
  - execution quality
---

*A **partial fill** occurs when an exchange or broker executes only a fraction of a submitted order, leaving the remainder open to be filled at a later price. In liquid markets, the event is rare; in thin instruments or large orders, it is routine.*

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Trigger** | Insufficient liquidity at current price to satisfy entire order |
| **Order Types** | Happens with market orders and some limit orders |
| **Remainder Status** | Usually remains open unless explicitly cancelled or expires |
| **Execution Venues** | More common in OTC, thin equities, and crypto |
| **Time Horizon** | Microseconds (illiquid equities) to hours (OTC bonds) |
| **Cost** | Potential slippage if remainder fills at worse price |

</aside>

## How partial fills arise

When an investor submits a large [market order](/wiki/market-order-execution/) in a stock with modest trading volume, the [order book](/wiki/order-book-depth/) may have only 10,000 shares available at the current [bid](/wiki/bid-ask-spread/). If the order is for 50,000 shares, the first 10,000 execute instantly at the market price, and the remainder either waits for new liquidity to appear, or the investor cancels what remains.

Partial fills are governed by the exchange rulebook and the order instruction itself. An order marked [All-or-None](/wiki/all-or-none/) (AON) will not execute at all if the full quantity is not available. A [Fill-or-Kill](/wiki/fill-or-kill/) (FOK) order will execute whatever can fill immediately and cancel the rest automatically. A standard [limit order](/wiki/limit-order/) with no special instruction will sit, executing in tranches as liquidity arrives.

In [high-frequency trading](/wiki/high-frequency-trading/) and stock [index](/wiki/sp-500-index/) futures, partial fills are invisible—the order is typically fully filled within milliseconds. In less liquid markets (small-cap stocks, corporate bonds, [cryptocurrency](/wiki/bitcoin/)), partial fills are expected and commonplace.

## Implications for traders

The risk of a partial fill is **execution drift**: the remainder of the order fills at a worse price. A trader trying to buy 100,000 shares of a thinly traded stock might get 30,000 shares at $50 (the initial [market price](/wiki/market-order-execution/)), then watch the stock rise to $51.50 as additional demand comes in, forcing the remaining 70,000 shares to fill at higher prices. The weighted average [arrival price](/wiki/arrival-price/) deteriorates.

Sophisticated traders mitigate this by using [algorithmic execution](/wiki/algorithmic-execution-benchmark/) strategies—breaking large orders into smaller tranches and releasing them over time, or using [participation orders](/wiki/volume-participation-order/) that scale to market volume. [Implementation shortfall](/wiki/implementation-shortfall/)—the gap between the price at order submission and the final execution price—includes the cost of partial fills.

For retail investors on simple [market orders](/wiki/market-order/), partial fills are usually transparent and immaterial. A 500-share order in Apple will fill completely in microseconds. But a 100,000-share order in a micro-cap stock may fill 40,000 at the original price, leaving 60,000 dangling—and the trader must actively cancel the remainder or risk a much worse fill later.

## Regulatory and venue-specific nuances

Major exchanges ([NYSE](/wiki/new-york-stock-exchange/), [Nasdaq](/wiki/nasdaq/)) have [best-execution](/wiki/best-execution-rules/) rules that push brokers to minimize [market impact](/wiki/market-impact-cost/) and achieve full fills at competitive prices. A broker that consistently leaves portions of customer orders unfilled and stranded might be violating these rules.

In [OTC markets](/wiki/over-the-counter-market/)—where bonds, currencies, and less-liquid equities trade—partial fills are the norm. A [dealer](/wiki/broker/) offering $5 million of a corporate bond might have only $2 million actually available and will offer that, leaving the customer to source the remainder elsewhere or scale back the order.

[Block trades](/wiki/block-trading-platform/) sometimes execute in multiple tranches by design. An institutional investor wanting to unload a large block might negotiate a price with a [block trader](/wiki/block-trade-mechanics/), then the trader splits the block into smaller pieces to distribute across its client network, each piece potentially executing at slightly different times and prices.

## Partial fills and cost basis

Tax and accounting rules require each partial fill to be recorded as a separate transaction for [cost basis](/wiki/cost-basis/) and [wash-sale](/wiki/wash-sale/) tracking. A 100-share order that fills 40 shares at $50, then 60 shares at $51, creates two separate lots with different [basis](/wiki/basis-risk/). If the investor later sells, the sequence and timing of fills matters for [tax-loss harvesting](/wiki/tax-loss-harvesting/) or [long-term capital gains](/wiki/long-term-capital-gain-tax/) treatment.

For traders using [specific identification basis](/wiki/specific-identification-basis/) strategies, partial fills introduce additional accounting friction. This is why some [algorithmic trading](/wiki/algorithmic-trading/) systems are designed to minimize the number of fills per order—not just to reduce slippage, but to simplify compliance and cost tracking.

## Partial fills in crypto and decentralized venues

In [decentralized exchanges](/wiki/decentralized-exchange-mechanics/) (DEXs), partial fills are handled differently. An [automated market maker](/wiki/automated-market-maker/) (AMM) will execute a trade against its liquidity pool up to the depth available, then the transaction either reverts entirely or the user accepts a reduced fill. Most DEX interfaces let users set a [slippage tolerance](/wiki/slippage/), which caps the price move they will accept; if the full order cannot fill within that tolerance, the transaction reverts.

<div class="wiki-seealso">

### Closely related

- [All-or-None](/wiki/all-or-none/) — Order instruction rejecting partial fills.
- [Fill-or-Kill](/wiki/fill-or-kill/) — Auto-cancel remainder if not fully filled immediately.
- [Order types](/wiki/order-types/) — Spectrum of instructions governing fill behavior.

### Wider context

- [Execution quality analysis](/wiki/execution-quality-analysis/) — Measuring slippage across multiple fills.
- [Implementation shortfall](/wiki/implementation-shortfall/) — Total cost including drift from partial fills.
- [Algorithmic trading](/wiki/algorithmic-trading/) — Techniques to minimize execution drift.

</div>

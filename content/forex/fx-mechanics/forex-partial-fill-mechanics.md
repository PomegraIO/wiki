---
title: "Partial Fill in Forex Orders Explained"
description: "A partial fill in forex occurs when your order is executed in pieces across different counterparties because no single liquidity provider can fill the entire size."
keywords:
  - partial fill forex
  - what is partial fill forex trading
  - forex order execution
  - liquidity fragmentation
  - order splitting forex
  - multiple counterparties forex
---

*A **partial fill** in forex occurs when a trader's order is executed in multiple pieces rather than as a single transaction. Because the [forex market](/stock-market/) is decentralized and liquidity is fragmented across multiple dealers and electronic communication networks, a large order may be filled by combining contracts from different counterparties — and the trader's platform shows each segment as a separate or grouped execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Partial Fill in Forex — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex trading." />

<div class="wiki-infobox-caption">No single forex dealer holds all the liquidity; large orders get split and filled incrementally.</div>

|   |   |
|---|---|
| **Trigger** | Order size exceeds the liquidity available from a single dealer or best price tier |
| **Execution** | Broker or ECN routes pieces to multiple counterparties; fills arrive in sequence or near-simultaneously |
| **What trader sees** | One or more executions at potentially different prices; order status shows "Partially Filled" until complete |
| **Timing** | Segments can fill in milliseconds or over minutes, depending on liquidity and order urgency |
| **Price impact** | Larger orders may see incrementally worse prices as they move through dealer quotation hierarchy |
| **Cost** | Partial fills can increase [bid-ask spread](/bid-ask-spread/) costs and slippage if not on same price tier |
| **Venue** | Happens in both [over-the-counter](/over-the-counter-market/) dealer markets and electronic communication networks |

</aside>

## Why Partial Fills Happen in Forex

The forex market has no single central [order book](/market-order/) like a stock exchange. Instead, liquidity is distributed: large banks run their own dealing desks, non-bank dealers quote prices electronically, and many trades happen directly between two counterparties without a public record. When a trader submits a large order, they are not automatically matched to one source of liquidity. Instead, their broker or the electronic system searches for the best available prices and executes what it can from each available counterparty.

If a trader wants to sell 5 million euros against the dollar, and one dealer is quoting only for 2 million at the best price, the system will fill 2 million with that dealer and then move to the next-best price source for the remaining 3 million. The order is "partial" not because it was rejected, but because it was too large to be filled entirely by the first counterparty.

Liquidity in forex is thickest at the [bid-ask spread](/bid-ask-spread/) — the price at which a dealer is willing to buy (bid) and sell (ask). For major pairs like EUR/USD at normal hours, dealers will quote tight spreads for routine sizes (say, up to 10 million). For larger sizes, the liquidity thins; dealers either step back and offer tighter prices only for smaller amounts, or they require wider spreads to compensate for the risk of taking on large positions.

## How a Partial Fill Is Executed

When a trader places a market order on a broker's platform, the order goes to the broker's liquidity aggregation system. This system:

1. **Checks available liquidity.** It queries multiple [market makers](/market-maker-trading/) (dealers and liquidity providers) to see what size they can fill and at what price.

2. **Routes to the best source first.** The order is sent to the counterparty quoting the best price and will likely fill as much as that counterparty is willing to accept.

3. **Routes the remainder.** Any unfilled portion is immediately sent to the next-best price source, and so on.

4. **Sends back confirmations.** Each fill is reported to the trader's account, sometimes as a single combined trade (if the platform consolidates them) or as separate executions with timestamps.

The entire process often happens in milliseconds. Modern platforms aggregate liquidity so seamlessly that a trader may not even notice a partial fill — the order appears to execute at slightly worse than the best-quoted price, which reflects the fact that additional liquidity came from a second-tier source.

## What a Trader Sees on Their Platform

Most broker platforms display the outcome of a partial fill in one of two ways:

**Consolidated view**: The platform shows a single trade record with an average [execution price](/price-discovery/). A trader who sells 5 million EUR and gets 2 million at 1.1010 and 3 million at 1.1008 may see one line item showing "5M EUR sold at 1.1009" (the weighted average).

**Detailed view**: The platform lists each segment separately, with timestamps and prices. A trader who wants to see exactly which dealer filled which piece can inspect the trade history.

The order status in the platform will show "Partially Filled" while the order is being split across counterparties, and "Filled" once all requested volume is allocated. If liquidity dries up and a portion cannot be filled within a set time, the remaining portion may be cancelled or left pending, depending on the [order type](/market-order/).

## Partial Fills and Slippage

A **partial fill** is closely related to [slippage](/bid-ask-spread/) — the difference between the price a trader expected and the price actually executed. When an order is large and gets routed to multiple counterparties, slippage is common for two reasons:

1. **Worse prices from secondary sources.** The best price is reserved for smaller sizes. As the order eats through liquidity, it encounters wider spreads.

2. **Market movement during routing.** If the order execution takes several seconds or minutes, market prices can shift. The second and third fills may occur at materially different prices than the first.

A trader who submits a 10 million unit order expects to see some slippage proportional to the size. Brokers often quote a "maximum slippage" or "acceptable slippage" range so that traders can cancel if the fill quality falls outside expectations.

## Partial Fills in Different Order Types

**Market orders** are the most common source of partial fills. Because the trader has agreed to accept the best available price immediately, the broker will fill what it can at each price level.

**Limit orders** — where a trader specifies a maximum (buy) or minimum (sell) price — can also be partially filled. If a limit order to buy 5 million at 1.1000 arrives and only 2 million is available at that price, the trader's platform may show "Partially Filled" at 1.1000, with 3 million remaining. The remainder stays pending until more liquidity appears at 1.1000 or better, or the trader cancels it.

**[Iceberg orders](/limit-order/)** — where only a small visible portion is displayed to the market — can also result in partial fills of the visible layer, with more hidden portions waiting to execute.

## Mechanics of Partial Fills in Major Pairs vs Exotic Pairs

In major pairs (EUR/USD, GBP/USD, USD/JPY), liquidity is abundant. A 5 million unit order will usually fill entirely in one go at the best available price, or in two tiers if it is unusually large. Partial fills are common but typically only involve a small price difference between segments.

In [exotic pairs](/currency-risk/) (say, USD/ZAR or EUR/SGD) or during low-liquidity hours, the same 5 million order might be split across five or six dealers, with each subsequent segment facing progressively worse prices. The [volatility](/currency-volatility/) in the fill price can be significant.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — The cost differential that varies with order size and liquidity
- [Market Order](/market-order/) — The order type most likely to result in a partial fill
- [Limit Order](/limit-order/) — Order type where partial fills are visible and can be monitored
- [Market Maker Trading](/market-maker-trading/) — The dealers who provide liquidity and set quotation tiers
- [Over-the-Counter Market](/over-the-counter-market/) — The decentralized venue where most forex trades occur
- [Price Discovery](/price-discovery/) — How prices emerge from distributed liquidity sources

### Wider context

- [Stock Market](/stock-market/) — Centralized venues contrast with decentralized forex
- [Slippage](/bid-ask-spread/) — The broader cost of trading in fragmented markets
- [Currency Risk](/currency-risk/) — Why traders care about execution precision in forex
- [Algorithmic Trading](/algorithmic-trading/) — Systems designed to minimize slippage on large orders

</div>

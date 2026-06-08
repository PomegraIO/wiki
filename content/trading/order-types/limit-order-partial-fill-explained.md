---
title: "Limit Order Partial Fill Explained"
description: "How a limit order can be partially filled across multiple transactions, how the unfilled shares remain active, and the cost implications for traders."
keywords:
  - limit order partial fill explained
  - partial execution limit order
  - unfilled limit order remainder
  - market depth and order fills
image: "/svg/trading.svg"
---

*A **limit order partial fill** occurs when only a portion of the shares or contracts in a limit order are executed, leaving the remainder open in the order book awaiting more counterparties at the limit price. If a trader places a limit order to buy 1,000 shares at $50 and only 600 shares become available at that price, the trader receives 600 shares and still has a live order for 400 shares waiting in the queue.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Partial Fills — execution mechanics</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and orders." />

<div class="wiki-infobox-caption">Limit orders split across multiple fills until cancelled or fully matched.</div>

|   |   |
|---|---|
| **Original order size** | Total shares or contracts you want to trade |
| **Filled amount** | Shares executed in the first trade match(es) |
| **Unfilled remainder** | Open quantity still waiting in the order book |
| **Price guarantee** | All fills occur at or better than the limit price |
| **Time priority** | Unfilled remainder maintains your original queue position |
| **Cancellation** | You can cancel the unfilled portion at any time |
| **Commission impact** | You may pay fees on each partial fill separately |

</aside>

## Why Partial Fills Happen

The securities markets operate on a continuous auction basis. When you place a [limit-order](/limit-order/) to buy 1,000 shares of a stock at $50 per share, you are saying: "I will buy up to 1,000 shares at this price or lower." The exchange then looks for sellers willing to transact at your price.

If only 400 sellers offer stock at $50 (or better) in the next moment, your order fills for 400 shares. But you still want the remaining 600 shares at your limit price. Rather than cancel your order and resubmit it, the exchange keeps your order in the book. You now have a live order for 600 shares, waiting for more sellers to arrive.

This is a partial fill. It is the default behavior of limit orders in most markets.

## Market Depth and Availability

Whether you get a partial fill depends on market depth—how many buy and sell orders exist at each price level.

Consider an example in stock trading:

- You place a limit order to buy 1,000 shares of Company X at $50.
- The current market shows:
  - 500 shares offered at $50 (from several sellers)
  - 700 shares offered at $50.01
  - 300 shares offered at $50.02

Your order matches the 500 shares at $50 immediately. Your order is now partially filled: 500 shares executed, 500 shares remain.

At this point, you have two options:
1. **Wait:** Your remaining 500-share order stays in the book. If more sellers arrive at $50, you will fill more shares.
2. **Cancel:** You withdraw the remaining 500 shares and exit the position entirely.

You cannot automatically access the 700 shares at $50.01 because your limit order specifies $50—you are not willing to pay $50.01. If you wanted those shares, you would need to cancel and resubmit at a higher price.

## Time Priority and Queue Position

In most markets, when multiple limit orders sit at the same price, they are filled in the order they were placed. This is called **time priority** or **price-time priority**.

If you place your 1,000-share limit order to buy at $50 at 9:31 a.m., and another trader places a 500-share limit buy order at the same price at 9:31:02 a.m., your order is ahead in the queue. If only 800 shares become available for sale at $50, you get 800 of your 1,000, and the second trader gets 0 (they must wait until you are satisfied or your order is cancelled).

When your order partially fills, your *unfilled remainder* keeps its original timestamp. It does not move to the back of the queue; it stays in its original position. This matters when liquidity is tight and every millisecond of queue advantage counts.

## Execution Across Multiple Trades

Partial fills often occur in *multiple increments*. You might see:

- **9:30:15 a.m.** — 200 shares filled
- **9:30:52 a.m.** — 150 shares filled
- **10:02:30 a.m.** — 300 shares filled
- Remainder: 350 shares still open

Each increment may execute at your exact limit price, or at a better price if the market moves favorably. (If you placed a buy order at $50 and the market prices drop, you might get fills at $49.99 or lower, which is better for you.)

You do not control which increments occur or when. You are subject to incoming sell orders that match your price.

## Cost Implications of Partial Fills

**Commission structure:** Many brokers charge a commission (or a per-share fee) on every execution. If your order fills in four separate increments, you might pay four separate commission charges—one per partial fill. With a flat $10 per-trade commission, you could pay $40 total instead of $10 for a single large fill. This is why traders sometimes prefer to hit a market order if liquidity is available at their price, accepting a slightly worse fill to avoid multiple commissions.

However, many modern brokers offer commission-free trading, which removes this cost advantage.

**Slippage and fill quality:** Because your unfilled remainder waits in the book, prices may move against you before the order fills. If you are buying and the stock price rises, your order might never fill (you set your limit at the old price). Conversely, if prices fall, you might get a better fill on your unfilled remainder.

**Timing and capital efficiency:** Partial fills can delay capital deployment. If you have $50,000 and want to buy 1,000 shares at $50 per share, a partial fill of 600 shares leaves $20,000 undeployed. This capital sits idle until the remaining 400 shares either fill or you cancel the order.

## Partial Fill vs. All-or-None Orders

Some traders want to avoid partial fills entirely. They can use an **all-or-none (AON)** restriction on their limit order. An AON order will only execute if the entire quantity can be filled in a single trade. If only 600 of 1,000 shares are available at the limit price, the order does not execute at all; it waits in the book for 1,000 shares to become available simultaneously.

AON orders are less likely to fill quickly because the bar for execution is higher. They are useful when a trader wants to avoid the commission costs or operational complexity of multiple partial fills.

## Cancelling the Unfilled Remainder

If your limit order is partially filled and you change your mind about buying the remaining shares, you can cancel the unfilled portion. Most brokers allow you to cancel a portion of an open order (called a **partial cancel**) or the entire remaining order.

When you cancel, your order is removed from the book immediately. Any future fills require you to place a new order.

## Partial Fills in Options and Futures

The same logic applies to options and futures contracts. If you place a limit order for 100 call option contracts at a specific price, you might receive a partial fill of 40 contracts, with 60 still waiting. For futures, a limit order to sell 10 contracts of a commodity might fill 3 contracts at your limit price, leaving 7 in the book.

The main difference is that options and futures markets are smaller than equity markets, so partial fills may occur more frequently due to lower liquidity at each price level.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — The order type that enables partial fills
- [Market Order](/market-order/) — Executes immediately in full but at potentially worse prices than a limit order
- [Bid-Ask Spread](/bid-ask-spread/) — The gap between buy and sell prices that affects limit order fill likelihood
- [Market Maker (Trading)](/market-maker-trading/) — Liquidity providers who facilitate fills of limit orders
- [Price Discovery](/price-discovery/) — How market participants' orders establish prices at which partial fills occur

### Wider context

- [Stock Exchange](/stock-exchange/) — Venue where limit orders are queued and partially filled
- [Futures Contract](/futures-contract/) — Used for leveraged exposure where partial fills also apply
- [Option](/option/) — Derivatives with order books subject to partial fills
- [Execution Risk](/execution-risk/) — The risk that partial fills and order slippage introduce

</div>
---
title: "Market Peg Order"
description: "An order type that automatically pegs to the opposite-side best quote, aggressively tracking the far touch of the spread and executing at variable prices."
keywords:
  - market peg order
  - pegged order
  - aggressive execution
  - best ask
  - best bid
image: "/svg/trading.svg"
---

*A **market peg order** is a [limit order](/limit-order/) that automatically adjusts its limit price to track the best offer on the opposite side of the [bid-ask spread](/bid-ask-spread/). For a buyer, it pegs to the ask; for a seller, it pegs to the bid. Unlike a [primary peg order](/primary-peg-order/), which is passive and conservative, a market peg order is aggressive—it chases the far touch of the spread and is far more likely to execute quickly, though often at less favourable prices.*

## The aggressive peg mechanism

Suppose you want to buy 10,000 shares when the market is bid $99.95 at ask $100.00. A [primary peg order](/primary-peg-order/) would peg to the $99.95 bid (your side), offering to buy at the price others are willing to sell at. You are passive.

A market peg order does the opposite. It pegs to the $100.00 ask (the opposite side)—the price sellers want to receive. Your order automatically becomes a buy order at $100.00, willing to pay what sellers want right now. As the ask moves, your order follows it upward. If sellers move to $100.05, your order moves to $100.05. You are essentially saying: "Always fill me at whatever sellers want, right now."

This is aggressive because you are paying the spread. You are willing to accept whatever the [market](/stock-market/) is quoting, not waiting for the market to come to you.

## Why traders use market peg orders

The main attraction is execution certainty. A market peg order is far more likely to execute than a [primary peg order](/primary-peg-order/), especially in fast or thin markets. By chasing the offer, you almost guarantee a fill—your order will execute as long as there is any volume at the pegged price.

For traders executing large positions or managing time-sensitive flows, this certainty is worth the cost of the spread. An algorithmic desk executing $100 million of stock might use market peg orders to ensure the entire position is filled within a target time window, accepting that it will pay spreads rather than risk partial fills.

Market peg orders are also useful for hedging. If you are short a stock and need to cover that short quickly, a market peg order to buy will execute promptly, allowing you to unwind the position without delay. The cost of the spread is the price of certainty.

## Relationship to market and limit orders

A market peg order sits between a pure [market order](/market-order/) and a [limit order](/limit-order/) on the spectrum of aggressiveness:

A **market order** executes immediately at any available price, with no limit. You may overpay or undershoot by a large amount if liquidity is sparse.

A **market peg order** executes as quickly as possible but respects a moving limit that tracks the opposite-side best quote. You still pay the spread, but you do not go beyond it. Your worst-case price is capped by the far touch of the spread at any given moment.

A **limit order** sits at a fixed price and waits for the market to come to it. It may never fill, but if it does, you get the price you specified.

A market peg order sacrifices the patience of a limit order for the speed of a market order, while staying within the bounded cost of the spread.

## Regulatory treatment

Like all pegged orders, market peg orders are defined and regulated under Regulation National Market System (Reg NMS). The [Securities and Exchange Commission](/securities-and-exchange-commission/) requires that:

- Market peg orders clearly identify themselves as such to venues and clearing systems
- The opposite-side best quote is tracked in real time, and the peg adjusts automatically
- The order never goes beyond the pegged price (it never trades worse than the opposite-side quote)

This clarity allows venues like [NASDAQ](/nasdaq/) and the [NYSE](/new-york-stock-exchange/) to handle market peg orders efficiently and report them accurately.

## Practical execution dynamics

In a stable market, a market peg order behaves like a patient market order—it fills relatively quickly at a modest spread. But in a volatile or thin market, the mechanics become interesting:

If the spread is widening, a buy market peg order keeps chasing the rising ask. In extreme cases, if sellers are fleeing and the ask is moving up sharply, your pegged order will race upward with it, potentially filling at much worse prices than you expected.

Conversely, if the market is tightening (the spread shrinking), a market peg order gets a better price as the opposite-side quote improves. A buy market peg order pegged to the ask benefits if sellers lower their asking price.

Market peg orders are also sensitive to the speed of the venue's peg mechanism. Some exchanges update pegs more frequently than others. A slower venue might cause your pegged order to lag behind actual market prices, leading to delayed execution or worse fill prices.

## Risk: slippage in fast markets

The main risk with market peg orders is slippage in rapidly moving markets. If the market is crashing and sellers are jumping ahead of each other, a sell market peg order pegged to the bid will chase the bid downward in real time, potentially selling at progressively lower prices as your pegged limit follows the falling market.

This can be controlled by setting a hard limit price outside the peg mechanism—some venues allow "market peg orders with a limit"—but the basic market peg order has no such protection.

## Contrast with primary peg orders

The distinction between market peg and primary peg is fundamental:

| | Primary Peg | Market Peg |
|---|---|---|
| **Pegs to** | Same-side best price (bid for buyers) | Opposite-side best price (ask for buyers) |
| **Aggressiveness** | Passive; sits within the spread | Aggressive; pays the spread |
| **Execution likelihood** | Moderate; waits for market to come | High; chases the market |
| **Price certainty** | Higher; unlikely to overpay | Lower; likely to pay spread |

## See also

<div class="wiki-seealso">

### Closely related

- [Primary Peg Order](/primary-peg-order/) — passive pegged order that sits on the same side of the spread
- [Limit Order](/limit-order/) — fixed-price order; base type for pegged variants
- [Market Order](/market-order/) — immediate execution at any price; most aggressive order type
- [Bid-Ask Spread](/bid-ask-spread/) — the gap that market peg orders traverse
- [Order Book](/stock-exchange/) — the queue where pegged orders rest and adjust
- [Intermarket Sweep Order](/intermarket-sweep-order/) — aggressive order that may trigger pegged resting orders

### Wider context

- [Regulation National Market System](/regulation-sho/) — framework defining peg order rules and protections
- [Best Bid and Offer](/regulation-sho/) — the quotes that market peg orders track
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of pegged order execution
- [Stock Exchange](/stock-exchange/) — venue routing and executing pegged orders
- [Algorithmic Trading](/algorithmic-trading/) — primary user of market peg orders for fast execution

</div>

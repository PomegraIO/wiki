---
title: "Fill-or-Kill Order Explained"
description: "A fill-or-kill order explained: executes immediately at the limit price or cancels entirely, preventing partial fills and allowing traders to move on."
keywords:
  - fill or kill order explained
  - fok order
  - all or nothing order
  - immediate execution
  - partial fill prevention
---

*A **fill-or-kill (FOK) order** is an instruction to buy or sell a security immediately at the specified limit price or cancel automatically if even a partial fill cannot be obtained right away. It eliminates the risk of a partial position and forces a clean execution decision: either the entire order fills in the current market moment, or the order disappears.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fill-or-Kill — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">All-or-nothing execution on demand: go full or go home.</div>

|   |   |
|---|---|
| **Instruction** | Fill the entire order quantity immediately or cancel |
| **Fill requirement** | 100% at or better than the limit price, in one instant |
| **Partial fill** | Rejected; order cancels if only partial match exists |
| **Time in market** | Milliseconds; no queue persistence |
| **Best for** | Small positions, hostile conditions, no partial hedges |
| **Contrast** | [Immediate-or-cancel](/immediate-or-cancel/) allows partial fills and rests nothing |

</aside>

## How fill-or-kill differs from immediate-or-cancel

Traders often confuse **fill-or-kill (FOK)** with **immediate-or-cancel (IOC)** because both orders vanish if they cannot fill immediately. The critical difference lies in what "fill" means.

An IOC order will accept ANY fill—one share, one thousand shares, or one million—as long as it matches the limit price right now. Once the available quantity is exhausted, the unfilled remainder cancels. A FOK order, by contrast, demands the entire quantity in one simultaneous fill. If the market depth at your limit price is 900 shares and you want 1,000, the IOC fills 900 and cancels the 100; the FOK cancels the entire 1,000 order and leaves nothing in the [order queue](/order-queue-priority-rules/).

This distinction matters most in thin markets or during fast-moving price action. An IOC might accidentally give you a partial position when you truly wanted either the full stake or zero. A FOK forces the exchange's matching engine to answer a binary question: "Is the entire quantity available right now?" No ambiguity, no partial liability.

## The mechanics of execution and cancellation

When you submit a FOK order, the exchange's matching engine checks the market depth against your limit price instantly. On the buy side, it scans the best ask; on the sell side, the best bid. If enough shares are available at or better than your limit, the order fills completely and the instruction expires. If the full quantity is not available, the order cancels immediately without leaving any resting order.

This all-or-nothing logic happens in microseconds. The exchange never places your order on the [bid-ask spread](/bid-ask-spread-and-execution-cost/) or into the order book waiting for future matches. FOK orders have no queue position because they have no queue persistence. This is why FOK is sometimes called a "do-not-route" order—it gives the market a single chance to match you, and if the chance fails, you get nothing.

Algorithmically, exchanges handle FOK by checking the current order book snapshot at the moment of arrival. If the aggregate size at the best price (or prices, for partial pegs) meets the order size, a complete fill occurs. If not, the order is dead on arrival.

## When traders use fill-or-kill orders

FOK orders are popular in four broad situations:

**Small traders taking a tactical position.** If you want to buy exactly 5,000 shares of a liquid stock at the market open, and you don't want to be left with 4,900 and then chase the market, FOK ensures you either get the full 5,000 or walk away clean. No awkward fractional stake hanging around.

**Hedgers eliminating adverse selection risk.** Suppose a market maker just sold 10 million dollars of bonds and needs to buy them back immediately to rebalance. A FOK order tells the counter-parties: "Take it or leave it, but I'm not sitting around waiting." This prevents the awkward scenario where you fill 70% and the remaining 30% slips into an IOC that gets a worse price two seconds later.

**Traders in fast or volatile markets.** During earnings announcements or central bank decisions, prices move in the time it takes to reach the order queue. A FOK order acknowledges this reality: execute now or don't execute at all. Waiting for a fill one second from now might mean a 2% worse price.

**Algorithmic indifference to partial fills.** Some trading systems (e.g., certain arbitrage bots or spread traders) build in logic that says: "If I don't get the full leg of my hedge right now, I want to abort and re-evaluate the whole trade." FOK is the blunt-force way to enforce that rule.

## Contrast with day orders and good-til-cancelled

A FOK order is neither a day order nor a [good-til-cancelled (GTC) order](/gtc-order/). Day orders and GTC orders can rest in the exchange book; they have queue position and wait for future fills. FOK orders do not. They either fill in the first instant or disappear entirely. This makes FOK ideal when you need zero, and it makes it unsuitable when you're willing to wait for a partial fill.

If you want to place an order that persists across hours or days but enforces an all-or-nothing condition over the lifetime of the order, you would need special logic at your broker or trading venue—not a standard FOK. Standard FOK is always a one-shot execution.

## The cost of an unsuccessful fill-or-kill

When a FOK order fails—meaning the required shares are not available—you get nothing. There is no second chance, no resting remainder, no partial consolation fill. From a trader's perspective, this is both a feature and a cost. The feature is clarity and no residual position risk. The cost is opportunity loss: if the market moves in your favour a moment later and you regret not accepting a partial fill, you have no recourse. The IOC order would have grabbed what it could; the FOK left you with zero.

This is why FOK orders are typically used for urgent, tactical needs rather than patient accumulation strategies.

## See also

<div class="wiki-seealso">

### Closely related

- [Immediate-or-cancel order](/immediate-or-cancel/) — accepts any size match right now, cancels the rest
- [Order Queue Priority Rules in Exchange Matching Engines](/order-queue-priority-rules/) — how limit order position determines fill probability
- [Limit Order](/limit-order/) — an order that fills only at a specified price or better
- [Market Order](/market-order/) — an order that fills immediately at the best available price
- [Bid-Ask Spread as an Execution Cost](/bid-ask-spread-and-execution-cost/) — how the spread translates into transaction costs

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — automated strategies using order types and execution logic
- [Broker](/broker/) — intermediary that routes your orders to exchanges or market makers
- [Stock Exchange](/stock-exchange/) — venue that matches buy and sell orders

</div>

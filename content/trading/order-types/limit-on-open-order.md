---
title: "Limit on Open Order"
description: "An opening-auction order that executes only if the opening price satisfies the specified limit condition."
keywords:
  - limit on open
  - opening auction
  - order execution
  - price discipline
  - opening price
image: "/svg/trading.svg"
---

*A **limit on open order** (LOO) is an instruction to buy or sell exclusively during the opening auction if the opening price meets the limit. If the opening price does not satisfy the condition, the order expires without execution, ensuring the trader avoids entry at an unfavourable opening price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit on Open Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark representing order mechanics and execution." />

<div class="wiki-infobox-caption">A precision opening-time order, useful for traders who target the first price discovery of the day.</div>

|   |   |
|---|---|
| **What it is** | A conditional order that executes only during the opening auction if the opening price meets the limit |
| **Execution timing** | Only at the opening auction (start of regular trading) |
| **Trigger condition** | Opening price must satisfy the specified limit |
| **If not met** | Order automatically expires without execution |
| **Typical use** | Capturing opening-price opportunities, avoiding gap-up or gap-down losses |
| **Risk** | May not execute, leaving the trader without an intended position |

</aside>

## Why the opening price matters

The opening price is the first price established through an auction process at the start of the regular trading session. For many traders—particularly those managing overnight risk or responding to overnight news—the opening price is the natural reference point for the day's trading. It represents the market's initial consensus after processing information from after-hours news, earnings announcements, or geopolitical events. A **limit on open order** allows a trader to act on overnight developments with price discipline: buy or sell only if the opening auction clears at an acceptable level, otherwise stand aside. This is especially valuable for traders who want to avoid the volatility spike that often follows the opening bell.

## The opening auction mechanics

At market open, the exchange collects all incoming buy and sell orders, including limit-on-open orders, and runs an opening auction to find the clearing price. Participants submit orders with limits, and the exchange matches them to establish the day's first official price. A limit-on-open order enters this process with a specified limit: if the clearing price is on the correct side of the limit, the order fills; if not, it is cancelled. The opening price is then disseminated to all market participants simultaneously, and regular continuous trading begins.

## The overnight gap problem

Stock prices often gap significantly from the previous close—sometimes opening 5% or more higher or lower—if major news breaks outside trading hours. A trader expecting a modest increase in a security but who finds it has gapped up 8% at the open faces an unwelcome choice: chase the stock at a worse price, or miss the move. A limit-on-open order solves this by setting a maximum (for a buy) or minimum (for a sell) acceptable opening price. If the gap is too large, the order doesn't execute, and the trader avoids overpaying for the position.

## Institutional use and portfolio timing

Large institutional traders often use limit-on-open orders when they need to enter positions on the opening but refuse to pay more than a pre-calculated fair-value price. A portfolio manager might determine that a stock's intrinsic value, accounting for overnight news, is $50, and place a limit-on-open buy order at that level. If the market opens at $51 or above, the order does not fill, signalling to the manager that the market has repriced the stock above her valuation. This enforces discipline and prevents emotional overtrading.

## How it differs from standard limit orders

A standard [limit order](/limit-order/) placed at market open may fill during the opening auction but equally may sit in the queue and fill minutes or hours later during continuous trading. A limit-on-open order has a single opportunity: the opening auction. If it doesn't fill there, it expires. This all-or-nothing structure makes sense for traders who specifically want the opening price as their reference, not just any price within their limit.

## Execution and certainty

Once the opening auction concludes and the official opening price is published, limit-on-open orders are immediately resolved: either they filled or they cancelled. The trader knows the outcome within seconds. This certainty reduces ambiguity and allows portfolio managers to synchronize opening-time trades across multiple securities or funds with minimal operational risk.

## See also

<div class="wiki-seealso">

### Closely related

- Market on Open Order — similar timing but executes at any opening price
- [Limit Order](/limit-order/) — intraday variant that fills at any time the price is touched
- [Limit on Close Order](/limit-on-close-order/) — analogous order type for the closing auction
- [One Cancels Other Order](/one-cancels-other-order/) — paired order structure for conditional execution
- [Stock Exchange](/stock-exchange/) — venue where opening auctions occur
- [Price Discovery](/price-discovery/) — how opening prices are established

### Wider context

- [Order Types](/order-types/) — taxonomy of trading instructions
- [Market Order](/market-order/) — counterpoint: executes at any price without condition
- Gap Analysis — overnight price jumps that create opportunities for LOO
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulates order practices
- [Bid-Ask Spread](/bid-ask-spread/) — the spread at opening relative to previous close

</div>

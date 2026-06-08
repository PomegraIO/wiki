---
title: "Limit on Close Order"
description: "A closing-auction order that executes only if the final price meets the specified limit, allowing traders to target a closing benchmark."
keywords:
  - limit on close
  - closing auction
  - order execution
  - trading mechanics
  - price targets
image: "/svg/trading.svg"
---

*A **limit on close order** (LOC) is an instruction to buy or sell at the closing auction if and only if the final price satisfies the limit condition. The order cancels automatically if the closing price is not met, ensuring the trader avoids execution at an unfavourable price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit on Close Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark representing order mechanics and execution." />

<div class="wiki-infobox-caption">A precision closing-time order, useful for targeting predictable final prices.</div>

|   |   |
|---|---|
| **What it is** | A conditional order that executes only at the closing auction if price conditions are met |
| **Execution timing** | Only during the closing auction (end of regular trading) |
| **Trigger condition** | Closing price must meet the specified limit |
| **If not met** | Order automatically cancels without execution |
| **Typical use** | Capturing closing prices, avoiding intraday volatility |
| **Risk** | May not execute, leaving trader without a position |

</aside>

## Why traders use the closing price as a benchmark

The closing price serves as the day's official settlement price—the figure quoted in financial statements, reported in the news, and used to calculate returns for the day. For portfolio managers and fund traders, executing at the close is not incidental but strategic: it anchors a day's trading, locks in a widely-watched reference price, and aligns with the timing of other closing transactions. A **limit on close order** lets a trader impose a price discipline: execute only if the close is favourable, otherwise stay out. This is especially useful when the trader has a target entry or exit price that reflects fundamental value or strategy, and will accept missing the trade rather than overpaying (or underpricing) at the close.

## The closing auction and order queuing

Stock exchanges run a closing auction during the final seconds of the trading day—typically one minute before the official close. During this window, all closing orders (both marketable and conditional) are collected and ranked by price and then by arrival time. A limit on close order enters this queue with a specified limit price. If the closing price calculated by the auction falls on the correct side of that limit, the order fills; otherwise it expires. The exchange publishes the official closing price after the auction completes, so the trader knows immediately whether execution occurred.

## Advantages for both sides of the market

For a buyer, a limit-on-close order to purchase below a threshold ensures the final position is not acquired above the acceptable price. For a seller, the order guarantees no fill below the limit—useful when the trader believes intraday weakness or supply will push the close lower and wants to capture that drop. Because the order is deterministic (fill or cancel, no partial fillings on the close in most systems) and keyed to an objective reference point, it removes discretion and emotion from the decision to trade.

## How it differs from intraday limit orders

An ordinary [limit order](/limit-order/) during the trading day will execute as soon as the price touches the limit, and may fill multiple times in increments. A limit on close order is exclusively reserved for the closing auction and will execute once, in full, if the closing price qualifies. This distinction matters: a trader targeting the close specifically would use LOC; a trader who is flexible about intraday execution would use a standard limit order that may fill much earlier.

## Practical constraints and settlement

Not all order types are available on all exchanges or in all markets. Most major equity exchanges support limit-on-close orders for equities and ETFs. Some traders use them in conjunction with market-on-close orders on the opposite side of a position to hedge the timing risk—for instance, selling at market and buying back on close if the final price drops. However, the order does not guarantee partial fills or scale: either it executes in full at the close or it does not.

The availability of closing-price data to the public immediately after the close makes LOC orders predictable: traders can verify in real time whether their orders filled and at what price. This transparency stands in contrast to less regulated order types and venues where final price discovery is opaque.

## See also

<div class="wiki-seealso">

### Closely related

- Market on Close Order — similar timing but executes at any closing price
- [Limit Order](/limit-order/) — intraday variant that fills as soon as price is touched
- [One Cancels Other Order](/one-cancels-other-order/) — paired order structure for conditional execution
- [Limit on Open Order](/limit-on-open-order/) — analogous order type for the opening auction
- [Stock Exchange](/stock-exchange/) — venue where closing auctions occur
- [Price Discovery](/price-discovery/) — how final prices are established

### Wider context

- [Order Types](/order-types/) — taxonomy of trading instructions
- [Market Order](/market-order/) — counterpoint: immediate execution regardless of price
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulates order practices
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between closing prices and quotes
- [Market Maker Trading](/market-maker-trading/) — mechanism that clears closing auctions

</div>

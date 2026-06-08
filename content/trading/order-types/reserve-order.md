---
title: "Reserve Order"
description: "An exchange mechanism that displays only a small visible quantity while a hidden reserve portion refreshes as the visible portion is traded."
keywords:
  - reserve order
  - iceberg order
  - hidden quantity
  - trading mechanics
  - order transparency
image: "/svg/trading.svg"
---

*A **reserve order** (also called an "iceberg" order) is a large order where only a small tranche is displayed on the public order book. As the visible portion is traded, the exchange automatically refreshes it from the hidden reserve, keeping the reserve amount confidential until execution. This structure allows institutional traders to trade large sizes without signalling their full intention to the market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reserve Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark representing order mechanics and execution." />

<div class="wiki-infobox-caption">Stealth ordering that reveals size only as execution occurs.</div>

|   |   |
|---|---|
| **What it is** | An order with a visible portion and a hidden reserve that replenishes as the visible tranche fills |
| **Also called** | Iceberg order, hidden order, reserve quantity |
| **Visible quantity** | A small tranche displayed on the order book |
| **Hidden reserve** | Remaining quantity not disclosed to other market participants |
| **Execution** | As visible tranche fills, reserve automatically refreshes the display |
| **Typical user** | Large institutional traders, hedge funds, block traders |
| **Market impact** | Minimizes information leakage about order size |

</aside>

## The problem of large orders and market impact

When a major investor wants to buy or sell a large block—say, 500,000 shares—submitting the entire order to the market book immediately reveals that size to all other participants. Rival traders, seeing the massive order, can front-run it: anticipate the big buyer's intent, buy ahead of the order, drive up the price, and sell at a profit. The large trader pays a premium (called "market impact") simply because her intention is visible. A **reserve order** solves this by keeping the size hidden: only a slice is shown—perhaps 10,000 shares—and once those 10,000 trade, the next 10,000 automatically appear, and so on, until the full 500,000 is complete.

## How it works on the exchange

When a trader (usually via her [broker](/broker/)) submits a reserve order, the exchange's matching engine receives both the visible quantity and the hidden reserve total. The order book displays only the visible tranche to all other traders. As [market orders](/market-order/) or [limit orders](/limit-order/) match against the visible tranche, the exchange automatically replenishes the visible portion from the hidden reserve. The hidden reserve size is NOT revealed to market participants—they see only that the visible tranche keeps refreshing, which may appear as a persistent order that doesn't shrink as it trades. From a casual observer's perspective, the stock has a sticky buyer or seller at that price level; in reality, it's a single massive order fragmenting itself.

## Anonymity and execution quality

The main benefit of a reserve order is execution efficiency. By hiding the full size, the trader avoids signalling distress or aggressive intent, which keeps other traders from gaming the price. A trader buying 500,000 shares at hidden reserve reduces her average execution price compared to submitting the full size all at once. Institutional traders, hedge funds, and asset managers all use reserve orders routinely when deploying large capital. For them, the concealment of size is worth the slight operational overhead of working with a [broker](/broker/) that supports the order type.

## Iceberg terminology

The term "iceberg" comes from the metaphor: the visible portion is the "tip" above the waterline, and the bulk of the order is hidden beneath. The name is universal across exchanges—London, NASDAQ, Tokyo—and traders use it interchangeably with "reserve order." Some exchanges and brokers offer variations, such as a reserve order that allows the visible quantity to be customized (e.g., show 5,000 shares, refresh 5,000 at a time) or a reserve order with a time-based refresh instead of fill-based.

## Exchange rules and disclosure

Exchanges have rules about reserve orders to prevent abuse and maintain fair market access. Most major exchanges allow reserve orders but require the trader to disclose the total size to the exchange (even if hidden from other participants) and to set a minimum visible quantity. Some exchanges, like the [New York Stock Exchange](/new-york-stock-exchange/), explicitly accommodate and regulate reserve orders; others, like some off-exchange venues, treat them as proprietary features. Regulators are generally permissive of reserve orders because the goal—reducing market impact—aligns with efficient capital formation, but exchanges monitor for signs of "layering" (placing fake orders to simulate demand) or manipulation.

## Not a substitute for transparency

A reserve order is a tactical tool for large traders but does not replace fundamental market transparency. Sophisticated market participants (including [market makers](/market-maker-trading/) and algorithmic traders) can often infer the presence of a reserve order by observing that a single price level attracts repeated matching despite appearing stable in quantity. Additionally, exchanges and regulators have access to full order data (including reserve portions) for monitoring and enforcement. The reserve order hides the size from casual observers and retail traders, not from professional participants or regulators.

## Comparison to other large-order techniques

A trader with a large order can also choose to **work the order**—submit small [market orders](/market-order/) or [limit orders](/limit-order/) throughout the day, manually controlling pace and disclosure. This gives more control but requires active monitoring. Alternatively, a trader can use a [dark pool](/dark-pool/) or off-exchange [alternative trading system](/alternative-trading-system/), where large blocks trade away from the public order book entirely. A reserve order splits the difference: the order is on-exchange (so it gets public-market pricing and liquidity), but the size is strategically concealed.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — executes at the best available price without limit
- [Limit Order](/limit-order/) — executes only at or better than a specified price
- [One Cancels Other Order](/one-cancels-other-order/) — paired order for conditional execution
- [Limit on Close Order](/limit-on-close-order/) — timing-based order at the closing auction
- [Limit on Open Order](/limit-on-open-order/) — timing-based order at the opening auction
- [Market Maker Trading](/market-maker-trading/) — how reserve orders interact with liquidity provision

### Wider context

- [Order Types](/order-types/) — taxonomy of trading instructions
- Order Book — the queue of pending buy and sell orders
- [Broker](/broker/) — intermediary that submits and manages reserve orders
- [Alternative Trading System](/alternative-trading-system/) — off-exchange venues where large trades occur
- [Price Discovery](/price-discovery/) — how reserve orders affect market pricing
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulates order practices and market manipulation

</div>

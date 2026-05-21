---
title: "Lit order"
description: "A lit order is any order that is visible on the public order book. When you place a limit order on a lit exchange, everyone can see your order size and price. Contrast with hidden orders in dark pools."
keywords:
  - lit order
  - public order book
  - limit order
  - visible order
image: "https://picsum.photos/seed/lit-order/900/600"
---

*A **lit order** is any order that is visible on the public order book of a [lit venue](/lit-venue) (a public exchange or trading venue). When you place a [limit order](/limit-order) to buy 1,000 shares at $50 on the NYSE, everyone can see it — traders, algorithms, and market makers. Lit orders form the backbone of price discovery and fair trading, but they expose your size and strategy to the market.*

<div class="wiki-hatnote">

For orders hidden from public view, see [hidden order](/hidden-order), [iceberg order](/iceberg-order), and [dark pool](/dark-pool). For the venues themselves, see [lit venue](/lit-venue) and [dark pool](/dark-pool).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lit order — key facts</div>

<img src="https://picsum.photos/seed/lit-order/900/600" alt="An order book showing visible limit orders" />

<div class="wiki-infobox-caption">The public order book shows all lit orders: size and price visible to everyone.</div>

|   |   |
|---|---|
| **What it is** | Any order visible on the public order book |
| **Typical form** | Limit order posted to an exchange |
| **Visibility** | Full: price, size, and timestamp visible to all |
| **Who can see** | All market participants, algorithms, data feeds |
| **Advantage** | Contributes to price discovery and fair pricing |
| **Disadvantage** | Large orders can be "front-run" or avoided by counterparties |
| **Venues** | NYSE, NASDAQ, and other public exchanges |

</aside>

## How lit orders create a visible market

When you place a [limit order](/limit-order) on a lit venue, it joins the order book alongside every other order. The order book is public — it is displayed in real time on every trading terminal, data feed, and broker platform. Traders watching can see:

- **Price:** The level at which your order is willing to trade.
- **Size:** How many shares (or contracts) you are offering.
- **Time priority:** When your order was placed (orders at the same price fill in sequence).
- **Side:** Whether your order is a buy or sell.

This transparency is fundamental to a fair, efficient market. Prices in the order book reflect real supply and demand, and anyone can trade against any visible order.

## The advantage: price discovery

Lit orders are the engine of price discovery. When market participants see $50 million in buy orders stacked below the market and only $500,000 in sell orders above, they understand that buyers are hungry and prices are likely to rise. Lit orders reveal the authentic demand.

Exchanges have an incentive to be lit (to attract order flow) because lit venues become information centers. Traders go to where the price action is most transparent.

## The disadvantage: information leakage

The moment you post a lit order, sophisticated traders (especially [algorithmic](/algorithmic-trading) and [high-frequency traders](/high-frequency-trading)) can see your intention. If you place a 10,000-share buy order at $50, algorithms know a buyer is hungry. Some may:

- **Front-run** you: buy shares ahead of you to capture the appreciation as you push the price up.
- **Avoid you:** pull their sell orders and wait for you to move on to other venues.
- **Trade against you** at worse prices: knowing you will eventually buy, they raise the ask.

Large institutional traders managing client money are especially concerned about information leakage. A 10,000-share buy in a thin stock can move the market significantly, and intelligent counterparties know this.

## Lit orders vs. hidden orders and dark pools

| Venue type | Visibility | Use case | Advantage | Disadvantage |
|---|---|---|---|---|
| **Lit venue** | Full; in order book | Most retail; price discovery | Transparent, fair | Front-running risk; size exposed |
| **Dark pool** | Hidden; no quotes | Large blocks | Size secrecy | Less price transparency; conflicts of interest |
| **Iceberg order** | Partial; visible tip | Large orders on lit venues | Size disguised, still transparent | Complexity; not available everywhere |

## Lit venues in the U.S. equity market

The major lit venues are:

- **Exchanges:** NYSE, NASDAQ, and various smaller exchanges (CBOE, EDGX, etc.).
- **All display** their order books publicly in real time.
- **Retail traders** placing orders on a broker are usually routing to one of these venues.

By regulation (Reg NMS), orders on lit venues have [best execution](/best-execution) protection and price-time priority — you are guaranteed to fill at the best available price, and your order gets priority if you were first.

## When you want to be lit

**Price discovery:** If you are trying to understand the fair value of a security, lit orders help. Prices are set by supply and demand in lit markets.

**Retail trading:** Most retail traders post lit limit orders on the major exchanges. It is simple and fast.

**Urgent exits:** If you need to sell and want certainty of execution, a [market order](/market-order) on a lit venue is the fastest way out.

## When you want to be hidden

**Large orders:** If you are buying or selling a large block, posting it lit can move the market against you. A [dark pool](/dark-pool) or [iceberg order](/iceberg-order) is more discreet.

**Algos:** Professional algorithms managing large orders deliberately split them across lit and dark venues, trying to find pockets of liquidity without moving the price too much.

## Lit orders and market manipulation

Posting a lit order commits you to trading (if someone hits it). Posting orders with no intent to trade (or posting and pulling repeatedly to create the illusion of demand) is called "spoofing" and is illegal under Dodd-Frank. Lit markets are policed for this.

## See also

<div class="wiki-seealso">

### Closely related

- [Lit venue](/lit-venue) — public exchange where lit orders live
- [Dark pool](/dark-pool) — private venue where orders are hidden
- [Hidden order](/hidden-order) — limit order not visible in the public book
- [Iceberg order](/iceberg-order) — large order with only a small visible slice
- Order book — the repository of all lit orders

### Execution and trading

- [Limit order](/limit-order) — the typical form of a lit order
- [Market order](/market-order) — immediate execution against lit orders
- Price-time priority — how lit orders are prioritized

### Regulatory and market structure

- [Best execution](/best-execution) — you get the best available price on lit venues
- Reg NMS — regulation protecting lit-order trading
- [NBBO](/nbbo) — the best bid-offer across all lit venues
- Trade-through rule — orders must hit the best-priced lit order first

### Advanced topics

- [Algorithmic trading](/algorithmic-trading) — uses lit and dark venues strategically
- [High-frequency trading](/high-frequency-trading) — plays lit-market microstructure
- [Smart order router](/smart-order-router) — routes to best lit venue

</div>

---
title: "Full Order Depth"
description: "Full order depth refers to visibility of all buy and sell orders in an order book, not just the best bid and ask. Showing full depth increases transparency but requires more bandwidth and processing power. Most retail investors see only the best bid-ask; institutions see deeper levels."
keywords:
  - order depth
  - order book
  - level 2
  - level 3
  - market depth
  - liquidity display
image: "/svg/markets.svg"
---

*The **order book depth** (or **market depth**) refers to the quantity of buy and sell orders available at each price level. **Full order depth** is the complete list of all orders, from the best bid to the worst bid (lowest to highest prices) and from the best ask to the worst ask (highest to lowest). Level 1 data shows only the best bid-ask; Level 2 shows top 5–10 levels; Level 3 shows all orders. Deeper visibility improves traders' understanding of liquidity but requires more data to transmit.*

<div class="wiki-hatnote">

This entry is about order book visibility. For trading data more broadly, see [market data](/stock-market/); for data feeds providing this, see [direct market data feed](/market-data-feed-direct/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Full Order Depth — key facts</div>

<img src="/svg/markets.svg" alt="A Level 3 order book showing all bids and asks at each price level" />

<div class="wiki-infobox-caption">Full order depth provides complete liquidity visibility.</div>

|   |   |
|---|---|
| **Level 1** | Best bid/ask only; free or low-cost |
| **Level 2** | Top 5–10 price levels; moderate cost |
| **Level 3** | All orders, full depth; high cost |
| **Data size** | Increases dramatically with depth |
| **Update frequency** | Sub-millisecond for active stocks |
| **Typical users** | Level 1: retail; Level 2+: institutions, traders |
| **Latency impact** | Deeper depth = more data = more latency |

</aside>

## Order book structure and levels

An order book displays all available buy and sell interest:

**Bid side (descending):**
```
$150.00 — 1,000 shares
$149.99 — 2,500 shares
$149.98 — 3,200 shares
... deeper levels ...
$149.50 — 10,000 shares
```

**Ask side (ascending):**
```
$150.01 — 1,500 shares
$150.02 — 2,000 shares
$150.03 — 3,500 shares
... deeper levels ...
$150.50 — 15,000 shares
```

The **spread** (best ask minus best bid) is $0.01 in this example.

## Level 1 data

Level 1 is the simplest, most widely available data:

- Best bid: $150.00
- Best ask: $150.01
- Bid size: 1,000
- Ask size: 1,500

Level 1 is sufficient for casual investors to understand the current market price. Most retail brokers and financial websites display Level 1 only.

## Level 2 data

Level 2 includes the top 5–20 price levels on each side:

```
Bid Side          Ask Side
$150.00 1000      $150.01 1500
$149.99 2500      $150.02 2000
$149.98 3200      $150.03 3500
$149.97 4500      $150.04 5000
$149.96 6000      $150.05 7500
```

Level 2 data helps traders assess liquidity and understand where larger orders might execute. It reveals, for instance, that $150.05 ask has 7,500 shares available, meaning a buyer wanting 10,000 shares would move to higher prices.

Level 2 data costs $100–$500 per month and is commonly used by active traders.

## Level 3 data

Level 3 (also called **full book** or **full depth**) shows all orders:

- Every bid and ask at every price level, down to the deepest.
- Order IDs and sizes.
- For some venues, anonymized trader identities.

For an active stock like Apple, the full order book might have hundreds or thousands of orders visible. Level 3 data is the most informative but also the most data-intensive and expensive.

Level 3 is used by high-frequency traders, market makers, and advanced algorithmic traders who need complete information. Cost: $1,000–$10,000+ per month.

## Data transmission and latency

Deeper order book depth requires more data to transmit:

- Level 1: ~100 bytes per update.
- Level 2: ~1 KB per update.
- Level 3: ~10–100 KB per update (depending on order count).

On an active stock trading thousands of times per second, Level 3 data can be massive, creating latency challenges. Systems must be optimized to handle this volume.

This is why high-frequency traders often use [direct market data feeds](/market-data-feed-direct/) and co-locate their servers near exchange data centers: the bandwidth requirements make remote data reception slower.

## Liquidity assessment via depth

Order depth helps traders understand liquidity:

**Deep book (much size at many levels):** Liquid; large orders can be executed without significant price movement.

**Thin book (little size, sparse levels):** Illiquid; a large order will move the price.

Example:
- Apple (AAPL): Often 10,000+ shares available within $0.01 of the mid-price. Very liquid.
- Small-cap stock: May have only 100–500 shares available within $0.10 of the mid-price. Illiquid.

## Iceberg orders and hidden depth

Not all depth is visible. **Iceberg orders** show only a portion of the total size:

A trader wants to buy 100,000 shares but posts only 10,000 visible with an additional 90,000 hidden. The order book shows 10,000; when 10,000 is filled, another 10,000 appears.

This allows traders to accumulate large positions without revealing their intent and moving the price against themselves.

## Dark pools and hidden orders

[Dark pools](/dark-pool-detail/) do not publish any order depth; orders are completely hidden until executed. This contrasts with [lit venues](/lit-venue-detail/), which show full order depth.

The choice between [lit venues](/lit-venue-detail/) (transparent) and [dark pools](/dark-pool-detail/) (opaque) involves a trade-off: transparency vs. ability to hide large orders.

## Data distribution

**Exchanges and [alternative trading systems](/alternative-trading-system/)** publish order depth via their data feeds.

**Data vendors** (Bloomberg, Refinitiv, eSpeed) bundle order depth with other market data.

**Brokers** typically show Level 1 or Level 2 to retail customers; professional customers can subscribe to Level 3.

## Regulatory transparency mandates

Under [Reg NMS](/reg-nms-detail/) and [MiFID II](/mifid-ii-trading/), venues must publish order depth to ensure fair and efficient markets. However, the mandated depth varies:

- [Lit venues](/lit-venue-detail/) must publish best bid-ask.
- Deeper levels are often available but at a cost.

The question of how much depth should be free vs. paid is ongoing.

## See also

<div class="wiki-seealso">

### Closely related

- [Order book](/stock-market/) — what order depth displays
- [Market data](/stock-market/) — order depth is a component
- [Direct market data feed](/market-data-feed-direct/) — provides full depth
- [Liquidity](/secondary-market/) — assessed via depth
- [Bid-ask spread](/stock-market/) — visible via Level 1 depth

### Wider context

- [Price discovery](/stock-market/) — aided by full depth visibility
- [Transparency](/stock-market/) — full depth increases this
- [High-frequency trading](/stock-market/) — exploits depth information
- [Iceberg orders](/stock-market/) — hide depth
- [Dark pools](/dark-pool-detail/) — provide no depth visibility

</div>

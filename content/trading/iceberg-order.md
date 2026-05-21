---
title: "Iceberg order"
description: "An iceberg order is a large order placed on a lit venue with only a small visible portion ('the tip') shown to the market. As the visible portion fills, more of the order is revealed. The iceberg remains mostly hidden beneath the surface."
keywords:
  - iceberg order
  - hidden order
  - large order
  - execution
image: "/svg/trading.svg"
---

*An **iceberg order** is a large [limit order](/limit-order) on a lit order book with only a small visible portion. When that visible portion fills, more shares are automatically revealed, like an iceberg with most of its mass below the water's surface. It allows large traders to accumulate or distribute size while keeping the market mostly unaware of their full intent.*

<div class="wiki-hatnote">

For fully visible orders, see [lit order](/lit-order). For fully hidden orders in a private venue, see [dark pool](/dark-pool).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iceberg order — key facts</div>

<img src="/svg/trading.svg" alt="An iceberg with most of its mass underwater, representing a large hidden order" />

<div class="wiki-infobox-caption">Like an iceberg, most of the order's size stays hidden beneath the surface.</div>

|   |   |
|---|---|
| **What it is** | Large order with only visible "tip" shown, rest hidden |
| **Visible portion** | Small slice (e.g., 1% or 5% of total) |
| **Hidden portion** | Majority of the order; revealed as visible portion fills |
| **Time priority** | Full size gets time priority at the price level |
| **Duration** | Day, GTC, or GTD (order persists until all shares fill or you cancel) |
| **Typical use** | Large blocks, minimizing market impact and information leakage |

</aside>

## How an iceberg order works

You want to buy 100,000 shares of a stock at $50. Instead of placing a visible 100,000-share order (which would spook sellers), you place an iceberg order:

- **Total size:** 100,000 shares
- **Visible size (tip):** 10,000 shares

The market sees a 10,000-share buy order at $50. Sellers trade against it. When all 10,000 are filled:
- The next 10,000 are automatically displayed.
- The market still thinks there is a 10,000-share order; it does not see the remaining 80,000 hiding.
- The process repeats until all 100,000 shares are bought or you cancel.

## Iceberg vs. hidden order

In practice, "iceberg order" and "hidden order" are often used as synonyms. Both refer to orders where most of the size is concealed. The term "iceberg" is more evocative (most of the mass is underwater), while "hidden" is more literal (size is hidden).

Most exchanges use the term "iceberg order" in their order-entry forms.

## Why use icebergs?

**Market impact.** If you post a 100,000-share buy order visibly, the market knows you are hungry. Sellers will hold out for a higher price or simply avoid you. By showing only 10,000, you look like a smaller buyer, and sellers are more willing to trade.

**Information leakage.** Sophisticated traders and algorithms watch the order book. They can infer your strategy from your order size and timing. An iceberg limits what they can infer — they see only the tip.

**Execution continuity.** An iceberg maintains time priority for your entire size. If you instead placed ten separate 10,000-share orders over time, the later orders would have later time stamps and lower priority.

## Iceberg mechanics: time priority

This is critical: your entire iceberg gets time priority at the moment you place the order.

**Example:** At 10:00 a.m., you place an iceberg order to buy 100,000 at $50 (visible: 10,000). At 10:05 a.m., another trader places a regular visible 50,000-share order at $50. If both are still waiting, yours fills before theirs, because you got there first.

When fills come in (say, 5,000 shares, 5,000 shares, 40,000 shares), your remaining 50,000 have priority over the 10:05 a.m. order.

## Icebergs in different venues

Most major exchanges support icebergs, but specifics vary:

- **NYSE:** Supports iceberg orders; minimum visible size rules apply (typically at least 100 shares or some percentage of total).
- **NASDAQ:** Similar support; specific rules on minimum display size.
- **Options exchanges:** Variable support; some support icebergs, others do not.
- **Futures exchanges:** Often support; CME, ICE, and others have iceberg capability.

Check your exchange's rules.

## The risk of icebergs: "gunning"

An iceberg reveals your intent gradually. Sophisticated traders know this. They can "gun" your iceberg — identify it and trade against it repeatedly, trying to pull you in at bad prices.

**Example:** A trader sees a 10,000-share buy order appearing repeatedly at $50. They infer there is an iceberg (100,000 total?) and decide to sell you pieces at $50, forcing your iceberg to slowly climb into their ask. By the time you are done, you paid $50.05 average instead of $50.

This is why professional traders using icebergs often vary their visible size or use other tactics (dark pools, block traders, etc.) to avoid predictability.

## Iceberg orders and minimum fill size

Some iceberg orders allow a "minimum fill size" specification: your order will not display its next tranche unless the previous tranche had at least X shares. This prevents extremely small fills that would leave your iceberg awkwardly small.

For example: iceberg of 100,000 (visible: 10,000), with minimum fill size 5,000. If only 2,000 shares are traded, the order does not reveal the next tranche until at least 5,000 have filled.

## Iceberg vs. VWAP and TWAP

Icebergs are a simple mechanism for hiding size. More sophisticated traders use [algorithmic orders](/algorithmic-trading) like [VWAP](/vwap-order) and [TWAP](/twap-order) orders, which break the order into many small pieces and execute them over time to minimize market impact and achieve an average price.

An iceberg is "dumb" (it reveals in fixed visible slices). VWAP and TWAP are "smart" (they analyze volumes and prices to optimize execution).

## When to use icebergs

**Large blocks where you want to stay on lit venues.** If you want the regulatory protection and price-time priority of a lit exchange but do not want to advertise your full size, an iceberg is ideal.

**Buys and sells where you want gradual accumulation.** Over several minutes or hours, you want to build a large position without moving the market much.

**When dark pools are too opaque.** If you want more transparency than a dark pool but more concealment than a fully visible order, an iceberg is the compromise.

## When NOT to use icebergs

**Small orders.** A 1,000-share iceberg makes no sense.

**When you need execution urgently.** An iceberg reveals slowly. If you need to exit quickly, use a [market order](/market-order) or visible [limit order](/limit-order).

**When predictability is your enemy.** In highly algorithmic markets, the slow reveal of an iceberg can be exploited. You might be better off with a [dark pool](/dark-pool) or block trading desk.

## See also

<div class="wiki-seealso">

### Closely related

- [Hidden order](/hidden-order) — same concept; different name
- [Dark pool](/dark-pool) — fully hidden private venue alternative
- [Lit order](/lit-order) — fully visible public order
- Order book — where icebergs show their tips

### Algorithmic and large-order execution

- [VWAP order](/vwap-order) — volume-weighted average price
- [TWAP order](/twap-order) — time-weighted average price
- [Algorithmic trading](/algorithmic-trading) — optimal order slicing
- Block trading — using brokers for very large blocks

### Market impact and strategy

- Market impact — how large orders move prices
- Information leakage — what the market can infer
- Front-running — exploiting visible orders
- Slippage — cost of execution

### Regulatory

- [Lit venue](/lit-venue) — public exchange
- Price-time priority — icebergs maintain this
- [Best execution](/best-execution) — regulatory obligation to get best prices

</div>

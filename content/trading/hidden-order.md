---
title: "Hidden order"
description: "A hidden order (or iceberg-variant) is a limit order that is not visible on the public order book. Only a small 'display size' is shown; the true size remains hidden until the visible portion fills."
keywords:
  - hidden order
  - stealth order
  - order book
  - execution
image: "https://picsum.photos/seed/hidden-order/900/600"
---

*A **hidden order** is a [limit order](/limit-order) placed on a public exchange (a lit venue) but with most or all of its size concealed from the public order book. When the visible portion fills, a new visible slice is revealed. Hidden orders let large traders avoid tipping off the market to their full intent, while still getting the price-time priority of a public order.*

<div class="wiki-hatnote">

For orders visible to everyone, see [lit order](/lit-order). For orders hidden in a private venue, see [dark pool](/dark-pool). For a hybrid approach, see [iceberg order](/iceberg-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hidden order — key facts</div>

<img src="https://picsum.photos/seed/hidden-order/900/600" alt="An order book showing a hidden order's visible tip" />

<div class="wiki-infobox-caption">Hidden order: only the visible size is shown; true size is concealed.</div>

|   |   |
|---|---|
| **What it is** | Limit order on lit venue with most size hidden |
| **Visibility** | Visible size shown; total size hidden |
| **Time priority** | Full size gets time priority at the price level |
| **Execution** | Fills in small chunks; hidden portion replenishes visible portion |
| **Good for** | Large orders where size concealment matters |
| **Downside** | More complex; not available on all exchanges |

</aside>

## How hidden orders work

When you place a hidden order, you specify two things: your total size and a display size. Only the display size appears in the public order book.

**Example:** You want to buy 100,000 shares at $50. You place a hidden order with:
- **Total size:** 100,000 shares
- **Display size:** 10,000 shares

What the market sees is a 10,000-share buy order at $50. But 100,000 shares are actually waiting. When 10,000 shares trade (your visible order fills), 10,000 more are revealed, and so on.

## Hidden order vs. iceberg order

The terms "hidden order" and "iceberg order" are often used interchangeably, though some venues distinguish them:

- **Iceberg order:** Typically on a lit venue; visible portion and total size are both submitted. The exchange manages the reveals.
- **Hidden order:** Might be exchange-specific terminology; same mechanics as an iceberg.

For practical purposes, they are the same: you set a visible "tip" and the exchange conceals the rest.

## Why hide order size?

**Information leakage.** If a trader places a 100,000-share order visibly, algorithms immediately know a large player is active. They might:
- **Front-run** you: buy ahead to capture the move you will create.
- **Avoid** you: pull sell orders and wait for you to move on.
- **Trade against** you: buy at worse prices, knowing you will push the price.

A hidden order limits this intel. The market sees only 10,000 shares; it does not know 90,000 more are waiting.

**Cleaner execution.** By hiding the size, you avoid moving the market as visibly. The price may still move, but more gradually.

## Mechanics: time priority and reveals

Hidden orders get **time priority for the full size** at the price level. If you place a hidden order (100,000 total, 10,000 display) before another trader places a visible 50,000-share order at the same price, your hidden order has time priority for all 100,000.

When 10,000 shares of your hidden order fill, the remaining 90,000 do not lose time priority. The next 10,000 shares are revealed, and so on. You maintain your place in line for the entire duration.

## Hidden order restrictions

Not all exchanges support hidden orders, and restrictions vary:

- **U.S. equities (NYSE, NASDAQ, etc.):** Widely supported, though specific display size rules may apply.
- **Options:** Some venues support hidden orders; others do not.
- **Futures:** Varies by exchange.
- **International venues:** Behavior varies by country and exchange.

Check your exchange's rules.

## Hidden orders vs. dark pools

| Feature | Hidden order (on lit venue) | [Dark pool](/dark-pool) |
|---|---|---|
| **Venue** | Public exchange | Private venue |
| **Visibility** | Small tip shown; rest hidden | No public visibility |
| **Price discovery** | Contributes (via visible tip) | Does not contribute; opaque |
| **Execution quality** | Subject to lit-venue rules (price-time priority, trade-through rules) | Subject to venue's rules; less transparent |
| **Compliance** | Fully regulated (like all lit orders) | Lighter regulation (but still regulated) |

A hidden order is a "halfway" solution: you get some size concealment while staying on a lit venue.

## Practical example: large block with hidden order

Suppose you are an institution that needs to sell 1 million shares of a large-cap stock, and you want to minimize market impact. You might:

1. Place a hidden order on the lit venue: 1,000,000 total, 50,000 display. The market sees 50,000; the rest is concealed.
2. Over the course of hours or days, the hidden order gradually sells as buyers accumulate.
3. You keep most of your size hidden, avoiding panic selling or algorithmic detection.
4. The lit order gives you price-time priority and regulatory protection.

An alternative would be to use a [dark pool](/dark-pool), but the dark pool gives you no time priority and relies on the venue's fair execution.

## Minimum display size rules

Exchanges often impose minimum display size requirements. For example, an exchange might require that at least 10% of your total size be displayed, or at least 100 shares (whichever is larger). These rules prevent traders from hiding 99.9% of their order.

## Hidden orders and information asymmetry

Hidden orders create a small information advantage: you know the full size, but the market does not. Regulators tolerate this in the name of allowing large traders to execute with less market impact. However, if hidden orders are used abusively (e.g., to mislead other traders about available liquidity), they can run afoul of market manipulation rules.

## When to use hidden orders

**Large blocks in liquid names.** If you are selling a large position in a well-traded stock, a hidden order lets you execute with less fanfare than a fully visible order.

**Wanting to stay on lit venues.** If you prefer the regulatory protection and price-time priority of a lit venue but want some size concealment, a hidden order is the tool.

## When hidden orders do not help

**In thin markets.** If liquidity is already scarce, hiding your size does not help much — the market knows that large size is needed and will figure it out.

**For small orders.** A hidden order for 1,000 shares makes no sense. The overhead is not worth the benefit.

**If speed is critical.** Hiding your size might extend execution time; if you need to exit quickly, a [market order](/market-order) or visible [limit order](/limit-order) is better.

## See also

<div class="wiki-seealso">

### Closely related

- [Iceberg order](/iceberg-order) — same thing; different terminology
- [Dark pool](/dark-pool) — fully hidden venue alternative
- [Lit order](/lit-order) — fully visible public order
- Order book — where hidden orders partially show

### Execution and strategy

- Block trading — large orders; hidden orders common
- Market impact — how large orders move prices
- [Algorithmic trading](/algorithmic-trading) — uses hidden orders to minimize impact
- Slippage — cost of large visible orders

### Regulatory context

- [Lit venue](/lit-venue) — public exchange
- Price-time priority — hidden orders maintain this
- Trade-through rule — applies to hidden orders
- [Best execution](/best-execution) — using hidden orders for best prices

</div>

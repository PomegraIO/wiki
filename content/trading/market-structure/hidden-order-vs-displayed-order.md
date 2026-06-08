---
title: "Hidden Orders vs Displayed Orders: How Execution Differs"
description: "How hidden and displayed orders interact in limit order books, why traders choose each type, and how they are prioritized during matching and execution."
keywords:
  - hidden order vs displayed order execution
  - non-displayed orders trading
  - iceberg orders limit order book
  - order execution priority
  - dark pool trading
image: "/svg/trading.svg"
---

*A **hidden order vs displayed order** difference is fundamental to modern market structure: displayed orders appear in the public quote and are visible to all traders, while hidden (non-displayed) orders sit in the book but do not appear on the tape until they execute. Traders use hidden orders to avoid tipping their hand; matching engines prioritize visible orders first.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hidden vs Displayed Orders — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Order visibility and timing drive execution probability and price improvement.</div>

|   |   |
|---|---|
| **Displayed order** | Visible to all market participants in the order book and quote; improves market depth |
| **Hidden (non-displayed)** | Not shown publicly until execution; does not build visible liquidity |
| **Iceberg order** | A hidden order with a small visible "tip" that refreshes as shares execute |
| **Matching priority** | Displayed orders typically get filled first when price matches; hidden executes after |
| **Use case** | Hidden: avoid telegraphing large trades; Displayed: provide liquidity, capture rebates |
| **Execution risk** | Hidden orders may not fill if price moves; displayed orders face information leakage |

</aside>

## The Core Mechanic: Visibility and the Order Book

In an electronic exchange, a **limit order** sits in the order book until matched. The exchange's matching engine shows some orders to the market (displayed) and keeps others private (hidden).

A **displayed order** appears in the real-time book snapshot sent to market data subscribers. If you place a displayed limit order to buy 1,000 shares at $50.00, everyone on the exchange can see that your order is there. Your presence helps set the [bid-ask spread](/bid-ask-spread/): if the best displayed ask is $50.10, your $50 bid tightens the bid-ask spread.

A **hidden order** does not show up in the public book. If you place a hidden order to buy 1,000 shares at $50.00, market participants see nothing—your order is invisible to the quote. Only when a sell order crosses your price and executes against your hidden order will the trade appear on the tape.

This distinction matters because in a [limit order book](/limit-order-book/), order priority—who gets filled first—depends partly on visibility. Displayed orders at a given price typically have priority over hidden orders at the same price, because displayed orders were advertised to the market and may have attracted other traders relying on the visible quote.

## Why Traders Hide Orders

A trader with a large buy order faces a dilemma. If they display the full size, competitors will see it and likely move prices against them—a phenomenon called **information leakage** or **adverse selection**.

Example: You want to buy 50,000 shares of a stock. If you display all 50,000 at once, sellers see the large size and immediately raise their asking prices, anticipating that you're desperate and will chase the offer. Your average fill price gets worse.

To avoid this, traders use **hidden orders** (also called "dark" orders in some venues). By hiding the full quantity, they prevent other traders from inferring their intent and repricing against them. A hidden order can sit at a price until it executes; no one outside the exchange knows it's there.

The tradeoff: a hidden order has **lower execution priority**. If the book has 1,000 displayed shares at your price and 1,000 hidden shares at your price, and 500 shares come in to sell, the displayed order gets priority. Your hidden order waits.

## Iceberg Orders: The Hybrid

An **iceberg order** is a hidden order with a small visible "tip." The exchange shows, say, 500 shares on the quote, but the actual order is 50,000 shares. As the visible 500 shares execute, the exchange automatically refreshes the visible portion to another 500, keeping the tip floating.

Icebergs give traders a middle ground: they keep the main order hidden (avoiding the information leak), but they contribute some visible liquidity to the market and may get some benefit from being partially visible.

The visible tip of an iceberg gets displayed-order priority, so it fills first. Once those 500 shares are done, the next 500 "tip" pops up and goes to the back of the queue at that price again. This is slower than a fully displayed order but less obvious than a pure hidden order.

Exchanges handle iceberg details differently. Some refresh the tip automatically; some require the trader to cancel and resubmit. Some cap the visible size as a percent of typical volume (to prevent icebergs from dominating the book). Most major venues (NYSE, NASDAQ) support them.

## Matching Engine Priority Rules

Each exchange publishes its matching logic. In most cases:

1. **Price priority**: An order at a better price executes first, regardless of visibility.
2. **Display priority at same price**: A displayed order placed before a hidden order at the same price gets filled first.
3. **Time priority within display/hidden**: Among displayed orders at the same price, the one placed first is filled first; same for hidden orders.

So if the book looks like:

```
Bid side (best to worst):
50.00 — 1,000 shares displayed (order A, placed 10:00:00)
50.00 — 2,000 shares hidden (order B, placed 09:59:00)
49.99 — 500 shares displayed (order C)
```

An incoming sell order for 500 shares at $50.00 would hit order A first (displayed, placed earlier). If 1,500 shares come in to sell, order A gets 1,000, then order B gets 500 (and now has 1,500 left in the queue).

This priority structure is why displayed orders are more attractive to passive [market makers](/market-maker-trading/): they're more likely to get filled, and they provide a public record of liquidity that other traders rely on.

## Exchange Rebates and Incentives

Many exchanges offer rebates for **adding liquidity** with displayed orders—roughly $0.0001 to $0.0005 per share—and charge fees for **removing liquidity** (executing against displayed orders). This creates a financial incentive to display orders.

Hidden orders don't add liquidity (as far as the market can see), so they don't earn rebates and often face the full removal fee. This cost can erode the benefit of hiding from information leakage, especially for smaller orders where the adverse selection cost is low anyway.

High-frequency traders and market makers often run displayed orders, because the rebate structure pays them to provide visible liquidity. Longer-term investors or institutions with large blocks more often hide orders, accepting lower fill rates in exchange for a shot at a better execution price (since they avoid telegraphing intent).

## Execution Risks and Trade-offs

**Hidden orders** face:
- **Lower execution probability**: Less visible, so fewer traders "see" the price and cross it.
- **Price movement risk**: If the market moves away from your price, your hidden order never fills. You miss the opportunity.
- **No fill certainty**: You're betting that the price will come back to you.

**Displayed orders** face:
- **Information leakage**: Competitors infer your intent and move prices against you.
- **Slippage on large orders**: If everyone sees you need to buy 50,000 shares, they'll front-run or raise prices as you're buying.
- **Execution pressure**: You may end up chasing the market and paying worse prices.

Neither choice is always better. A small order or a trade on a liquid stock (where moves are tight) might be fine displayed. A huge order or a less-liquid name might be hidden to avoid moving the market, even if it means lower fill probability.

## Partial Fills and Minimum Quantity Orders

Exchanges also let traders set **minimum quantity** requirements (e.g., "only fill me if at least 500 shares cross at once") and allow **partial fills** of hidden orders. These tools let traders manage the tradeoff.

A hidden order with a high minimum might sit unfilled, but when it does fill, it knows it got a meaningful size execution. A hidden order with no minimum might fill in small drabs and dabs, creating high transaction costs.

Different venues offer different tools. NASDAQ offers hidden orders and icebergs on all securities; some [alternative trading systems](/alternative-trading-system/) (ATS) or [dark pools](/dark-pool/) offer more flexible hidden order types. Regulatory scrutiny of dark pools has tightened over the past decade, with stricter rules on when exchanges must display orders and when they can accept non-displayed orders.

## Real-World Example: A Mutual Fund's Large Sell

Imagine a mutual fund wants to sell 100,000 shares of Company X. If they display all 100,000, the market immediately understands there's a forced seller, and bid prices crater.

The fund's trader might instead:
- Place a hidden order to sell 20,000 shares at the best bid.
- Place an iceberg order with a 5,000-share tip, also to sell.
- Place another hidden order to sell 50,000 more shares at a slightly worse price.
- Drip the remaining 25,000 shares into the market over 30 minutes via smaller displayed orders.

This approach hides the total supply, avoids panicking the market, and likely achieves a better average fill price than dumping all 100,000 shares at once. The fund accepted the risk that some of their hidden orders never filled, but the reduction in market impact was worth it.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order Book](/limit-order-book/) — the data structure holding all orders and their priority
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between best bid and best ask, affected by order visibility
- [Market Maker Trading](/market-maker-trading/) — traders who provide displayed liquidity for rebates
- [Alternative Trading System](/alternative-trading-system/) — venues that match trades outside public exchanges
- [Price Discovery](/price-discovery/) — how visible order flow helps markets converge to fair value

### Wider context

- [Stock Exchange](/stock-exchange/) — where displayed and hidden orders are matched
- Order Execution — general mechanics of filling trades
- Information Asymmetry — why traders hide orders to prevent others from exploiting information

</div>
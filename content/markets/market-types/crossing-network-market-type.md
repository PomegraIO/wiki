---
title: "Crossing Network: How Off-Exchange Matching Works"
description: "A crossing network matches buy and sell orders at a reference price without routing to an exchange. Learn how they differ from dark pools and serve institutional traders."
keywords:
  - crossing network market type
  - crossing network trading
  - off-exchange matching
  - dark pool vs crossing network
  - institutional order matching
image: "/svg/markets.svg"
---

*A **crossing network** is a private order-matching system that executes buy and sell orders at a reference price (typically the midpoint of the bid-ask spread, or a quoted market price) without routing to a lit exchange. Unlike [dark pools](/dark-pool/), which match orders at undisclosed prices and compete with exchange prices, crossing networks explicitly reference existing market quotes and are used primarily by institutions seeking to minimize **market impact** and **trading costs** without exposing intent to the broader market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crossing Network — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure." />

<div class="wiki-infobox-caption">Institutional matching at a reference price; off-exchange, but price-transparent to the broader market.</div>

|   |   |
|---|---|
| **Reference price** | Usually the midpoint of the current bid-ask spread, or last-sale price on an exchange. |
| **Order types** | Institutional block orders; typically no retail participants. |
| **Price visibility** | Matched orders settle at the reference price; the crossing itself is not displayed live. |
| **Market impact** | Lower than routing to an exchange because the cross does not reveal the order size before execution. |
| **Regulation** | SEC-regulated as an [alternative-trading-system](/alternative-trading-system/); must follow Regulation SHO and order protection rules. |
| **vs. Dark pools** | Crossing networks use transparent reference prices; dark pools negotiate prices and can step ahead of quoted spreads. |
| **Speed** | Slower than lit exchanges; operates on batch or periodic cross schedules. |

</aside>

## How a Crossing Network Executes a Trade

A crossing network is a venue—much like an exchange—but one that does not display order books in real time. Instead, it accumulates orders over a period (often a few seconds to minutes) and then crosses (matches) buy and sell orders at a reference price, usually the midpoint of the current exchange bid-ask spread.

Here is a simplified example: Suppose a pension fund wants to buy 100,000 shares of a stock. The bid-ask spread on the New York Stock Exchange is $50.00 bid, $50.02 ask. The pension fund submits a non-displayed buy order to a crossing network. Meanwhile, a mutual fund has a sell order for 100,000 shares in the same network. At the periodic cross, the network matches them at $50.01 (the midpoint). Neither order touched the lit market; neither revealed its size to other traders.

The critical feature is the **reference price**. The crossing network does not let buyers and sellers negotiate a price in isolation. Instead, it ties the execution to an external benchmark—the market price. This distinguishes crossing networks from dark pools, where prices can be negotiated independently.

Because the orders do not interact with the lit exchange order book, the crossing avoids **market impact**. If the pension fund had sent its 100,000-share order directly to the NYSE, the market would have seen it and likely pushed the price higher as sellers demanded more to supply the huge volume. By crossing in a hidden venue at the midpoint, the institution saves on the implied cost of moving the market.

## Reference Pricing: Why It Matters

The choice of reference price is crucial. Most crossing networks use the midpoint of the current spread because it is objective and does not favor buyer or seller. Some allow participants to specify other reference prices—the last sale, the opening price of the day, or a volume-weighted average price over a period.

Tying the price to an external market benchmark creates **price transparency** at the moment of execution. Everyone knows that a cross in the network happened at a predictable price, even if they did not see it live. This differs markedly from a dark pool, where a buyer and seller might negotiate a price between the displayed spread—say, $50.005—that no one else on the lit market knows about.

This transparency is why crossing networks are considered more fair and more aligned with markets. They do not allow market participants to trade at prices that contradict the broader market.

## Crossing Networks vs. Dark Pools: Key Differences

The distinction between crossing networks and [dark pools](/dark-pool/) is important because they serve different purposes and face different regulatory scrutiny.

| Feature | Crossing Network | Dark Pool |
|---------|------------------|-----------|
| **Price discovery** | Reference external market (transparent) | Negotiated or internal (opaque) |
| **Order visibility** | Orders not displayed live | Orders not displayed live |
| **Execution price** | Midpoint of spread or fixed external reference | Can be anywhere within or outside the spread |
| **Market impact** | Reduces slippage for large orders | Also hides order size, reduces impact |
| **Regulatory intent** | Facilitate block trading without distorting lit prices | Allow flexible pricing for complex trades |
| **Speed** | Periodic batch processing | Faster; can process continuously |

A dark pool might allow a buyer and seller to meet at a price the buyer negotiates to be cheaper than the posted ask, creating an advantage over lit-market traders. A crossing network locks in the objective midpoint, so neither party gets an informational advantage.

In practice, the line blurs. Many dark pools offer "reference price" crosses (where an order crosses at the NBBO midpoint), alongside negotiated crossing and other functionality. But the distinction in intent remains: crossing networks aim to be price-transparent proxies for the lit market; dark pools aim to offer confidential, flexible pricing.

## Why Institutions Use Crossing Networks

Large institutional traders use crossing networks for block trades—orders so large that routing them directly to an exchange would move the market significantly. A pension fund or mutual fund with a 500,000-share order for a mid-cap stock might absorb a multi-cent price move if it showed that size on the exchange. In a crossing network, both the buyer and seller hide their size, and both benefit from a midpoint cross.

Crossing networks also appeal to traders who value **algorithm minimization**. If an institution wants to execute a large order with the least market disturbance, the crossing network—by preventing price discovery—is often preferable to breaking the order into smaller lit-market slices over time, each of which moves the price.

Additionally, crossing networks are used by institutions that are indifferent to execution price as long as it is fair. A portfolio rebalancing trade, for example, where a fund is swapping one stock for another of similar value, might benefit from a quick, hidden cross rather than advertising the trade and inviting information-leaking moves.

## Regulation of Crossing Networks

Crossing networks are **alternative trading systems (ATS)** under SEC Regulation SHO and related rules. They must register with the SEC and follow strict guidelines:

- **Order protection**: Crossing networks cannot execute trades that step ahead of protected quotations on lit exchanges. If the NBBO bid is $50.00, the crossing network cannot fill a sell order at $49.99.
- **Record-keeping**: All crosses must be recorded, timestamped, and reported to the SEC.
- **Fair access**: Members must agree to non-discriminatory access terms.
- **Transparency**: The network must publish statistics on order flow and execution quality.

Because crossing networks are not exchanges, they do not have the same stringent market-maker obligations or price-continuity requirements. This gives them operational flexibility but also subjects them to stricter oversight of potential abuses. If a crossing network were used to pump-and-dump a stock or to systematically step ahead of the market, the SEC can shut it down or impose fines.

## Periodic Crossing and Batch Processing

Crossing networks typically operate on a **periodic crossing** schedule rather than continuous matching. A network might cross orders every 5 seconds, 30 seconds, or at specific times during the trading day. This batching reduces system complexity and gives traders a window to accumulate order interest.

The batching also affects market dynamics. If you know a cross is coming in 30 seconds, you might hold your order in the network, hoping for a better fill. But you also know that if no matching order appears, your order will not fill at all. This creates a tension between the benefit of low market impact and the risk of non-execution.

Some crossing networks operate continuous crossing—matching orders the moment a pair arrives—but this is less common because it requires more sophisticated systems and resembles exchange operations more closely.

## Market Share and Adoption

Crossing networks have a smaller share of overall market volume than lit exchanges or dark pools. Most institutional traders use a mix: lit exchanges for price discovery and smaller orders, dark pools for flexible pricing on large blocks, and crossing networks for certain block trades where both parties accept midpoint pricing.

The largest crossing networks in the US include those operated by exchanges themselves (NYSE Crossing, Nasdaq Crossing) and independent networks. Because they serve a niche—large institutional blocks where both parties benefit from a reference price—they remain stable but never capture the majority of trading volume.

## See also

<div class="wiki-seealso">

### Closely related

- [Dark pool](/dark-pool/) — How off-exchange venues negotiate prices independently of the lit market.
- [Alternative trading system](/alternative-trading-system/) — Regulatory definition and compliance framework for ATS.
- Market impact — The cost of moving prices through trading; how crossing networks reduce it.
- [Bid-ask spread](/bid-ask-spread/) — Pricing mechanism that crossing networks reference.
- [Block trade](/block-trade/) — Large institutional orders; a primary use case for crossing networks.
- [NBBO](/nbbo/) — National Best Bid and Offer; the baseline for crossing-network reference prices.

### Wider context

- [Stock exchange](/stock-exchange/) — Lit markets; the benchmark for crossing-network pricing.
- Order routing — How brokers choose venues; crossing networks as an alternative routing choice.
- [Market microstructure](/market-microstructure/) — Structure of financial markets and the role of different venue types.
- Securities and Exchange Commission — Regulator of crossing networks and other ATS.

</div>

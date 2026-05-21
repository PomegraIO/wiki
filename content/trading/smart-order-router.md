---
title: "Smart order router"
description: "A smart order router (SOR) is an algorithmic system that automatically routes your order to the venue offering the best price. It checks multiple exchanges and dark pools simultaneously and splits the order across them to achieve best execution."
keywords:
  - smart order router
  - SOR
  - order routing
  - best execution
image: "https://picsum.photos/seed/smart-order-router/900/600"
---

*A **smart order router (SOR)** is an [algorithmic trading](/algorithmic-trading) system that automatically routes your order to whichever venue (exchange or dark pool) offers the best price at that moment. If you place a buy order for 10,000 shares, the SOR checks the NASDAQ, NYSE, and multiple dark pools, finds the best ask prices across them, and splits your order accordingly — buying 3,000 from NASDAQ, 4,000 from NYSE, 3,000 from a dark pool — all in milliseconds. The result: best execution.*

<div class="wiki-hatnote">

For manual order placement, see [limit order](/limit-order) and [market order](/market-order). For venue-specific trading, see [lit venue](/lit-venue) and [dark pool](/dark-pool).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Smart order router — key facts</div>

<img src="https://picsum.photos/seed/smart-order-router/900/600" alt="A diagram showing order routing across multiple venues" />

<div class="wiki-infobox-caption">SOR checks multiple venues and routes to achieve best combined price.</div>

|   |   |
|---|---|
| **What it is** | Algorithm that routes orders to best-priced venues |
| **Execution speed** | Milliseconds; checks all venues simultaneously |
| **Venues included** | Lit exchanges, dark pools, broker ECNs |
| **Benefit** | Best execution; lower average price |
| **Complexity** | Varies; basic (price-only) to complex (volume, liquidity, latency) |

</aside>

## How a smart order router works

You submit a market order to buy 10,000 shares of Apple through your broker. The SOR:

1. **Checks all available venues:**
   - NASDAQ ask: $150.02 (5,000 shares available)
   - NYSE ask: $150.03 (8,000 shares available)
   - Citadel dark pool ask: $150.01 (2,000 shares available)
   - Virtu dark pool ask: $150.02 (3,000 shares available)

2. **Calculates optimal routing:**
   - Buy 2,000 from Citadel at $150.01 (best price)
   - Buy 3,000 from Virtu at $150.02 (next best)
   - Buy 5,000 from NASDAQ at $150.02
   - Buy 0 from NYSE (worst price at $150.03)

3. **Executes across venues** in milliseconds.

4. **Result:** Your average fill price is $150.015, much better than NYSE's $150.03.

Without a SOR, your broker might have routed all 10,000 to one venue (perhaps their own affiliate), getting a worse price.

## Lit vs. dark venue routing

SORs route to:

**Lit exchanges:** NYSE, NASDAQ, regional exchanges (EDGX, EDGA, etc.). These have transparent order books and are subject to [best execution](/best-execution) rules.

**Dark pools:** Citadel, Virtu, Liquidnet, and others. Price is often the midpoint of the lit-market spread; fills are not guaranteed.

**Broker ECNs:** Electronic communication networks operated by brokers (e.g., a broker's internal system).

A modern SOR balances lit and dark routing: hitting lit venues for certainty and regulation, hitting dark pools for potential price improvement and discretion.

## SOR benefits

**Best execution:** By checking all venues, you get the best combined price rather than the price at one venue.

**Improved average price:** For large orders split across multiple venues, the average price is often noticeably better.

**Regulatory compliance:** SORs help brokers meet [best execution](/best-execution) obligations under Reg NMS and similar regulations.

**Transparent process:** Brokers can report exactly where your order went and at what prices.

## Challenges and trade-offs

**Complexity:** A sophisticated SOR might account for:
- Current bid-ask at each venue.
- Volume available at each level.
- Latency to each venue.
- Whether a venue's quote will still be there by the time your order reaches it (latency can cause stale quotes).

**Stale quotes:** By the time your order reaches a venue, the price might have moved. A SOR must account for this risk.

**Hidden liquidity:** Dark pools' best prices are not always visible until after you trade. A SOR cannot always know the dark pool's true best price in advance.

**Splitting order flow:** Routing across multiple venues can fragment your order, leading to:
- Higher execution costs (multiple venue fees).
- Delayed partial fills (some pieces fill later).
- Information leakage (multiple venues see pieces of your order, revealing your intent).

## SOR and regulation

Reg NMS and [best execution](/best-execution) rules require that:
- Brokers use SORs (or equivalent) to achieve best prices.
- SORs must account for all venues, not just exchanges with affiliate relationships.
- Brokers must regularly review and test their SORs.

Brokers that do not have adequate SORs can face regulatory action.

## Payment for order flow and conflicts

Some brokers operate SORs that secretly route orders to affiliated brokers or market makers, even if better prices are available elsewhere. This is called [payment for order flow](/payment-for-order-flow) (PFOF) and is controversial.

**Concern:** A broker that receives kickbacks from a dark pool might route orders there even if lit venues offer better prices.

**Regulation:** SEC and FINRA require disclosure of PFOF arrangements. However, the incentive misalignment persists.

## SOR implementation

**Broker-operated:** Most large brokers (Schwab, Fidelity, Interactive Brokers) operate their own SORs and improve them continuously.

**Third-party vendors:** Some brokers license SOR technology from firms like Portware, Orion, or others.

**Market-wide systems:** Some exchanges operate "best execution" systems that route across multiple venues.

## Limitations of SOR

**Cannot guarantee best execution if prices change:** By the time your order travels to a venue, the best price might be gone.

**Dark pool opaqueness:** Hidden prices in dark pools are not visible; a SOR cannot account for them.

**Latency sensitivity:** In fast markets, latency (delay in routing) can cause your order to miss the best prices.

## Real-world example

You place a market order to sell 5,000 shares of Microsoft:

- NASDAQ bid: $320.50 (all-or-none, minimum 2,000 share)
- NYSE bid: $320.49
- Goldman Sachs dark pool bid: $320.48
- Morgan Stanley dark pool bid: $320.515

Your broker's SOR:
- Sells 2,000 to Goldman's dark pool at $320.515 (best price, but limited)
- Sells 3,000 to NASDAQ at $320.50

Average fill price: $320.504. Versus if you had hit NYSE's bid of $320.49, you would have gotten $320.49. The SOR saved you 1.4 cents per share × 5,000 = $70.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic trading](/algorithmic-trading) — parent category
- [Best execution](/best-execution) — regulatory goal of SORs
- [Lit venue](/lit-venue) — public exchanges SOR routes to
- [Dark pool](/dark-pool) — private venues SOR routes to

### Order routing and execution

- [VWAP order](/vwap-order) — algorithmic execution targeting volume-weighted price
- [TWAP order](/twap-order) — time-weighted execution
- [Market order](/market-order) — often routed via SOR
- [Limit order](/limit-order) — routed via SOR to best venue

### Regulatory and quality

- Reg NMS — requires SORs to achieve best prices
- [NBBO](/nbbo) — national best bid-offer; SOR targets this
- [Payment for order flow](/payment-for-order-flow) — creates SOR conflicts
- Trade-through rule — protects best prices

### Market structure

- Order book — SOR checks these across venues
- Liquidity — SOR finds best liquidity across venues
- Venue competition — SORs enable competition

</div>

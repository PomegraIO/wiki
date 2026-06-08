---
title: "Smart Order Router: How Order Routing Affects Execution"
description: "A smart order router automatically splits and directs your orders across trading venues to get you the best price. Here's how it works and what it means for you."
keywords:
  - smart order router
  - order routing execution
  - venue routing broker
  - best execution trading
  - order splitting venues
image: /svg/trading.svg
---

*A **smart order router** (SOR) is automated software that breaks up your orders and sends them to different exchanges and trading venues in real time, all to catch the best available prices. The router's job is to minimize what you pay (or maximize what you receive) by spreading your order across multiple markets simultaneously—and doing it faster than any human could.*

<div class="wiki-hatnote">

This article covers the mechanics of smart order routing as it affects individual traders and institutional orders. For related concepts, see [market-maker-trading](/market-maker-trading/) and execution-quality-trading.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Smart Order Router — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">Order routers optimize fills across multiple venues in milliseconds.</div>

|   |   |
|---|---|
| **Core function** | Splits orders and directs them to achieve best execution |
| **Primary users** | Brokers, institutional traders, retail platforms |
| **Speed** | Operates in milliseconds; continuously monitors each venue |
| **Legal obligation** | Brokers must demonstrate reasonable efforts toward best execution |
| **Key metric** | Effective spread vs. quoted spread |
| **Venues routed to** | Stock exchanges, alternative trading systems, market makers |

</aside>

## What smart order routers actually do

When you place an order through most brokers, especially for a large size, your order doesn't go to a single exchange. A smart order router automatically divides it and sends portions to multiple venues—NYSE, NASDAQ, regional exchanges, alternative trading systems, or wholesalers—based on where it can get the tightest [bid-ask-spread](/bid-ask-spread/) or fastest execution at a given moment.

The router works by continuously sampling the [best bid and offer](/price-discovery/) across all connected venues. If you want to buy 10,000 shares, the router might send 2,000 to NYSE, 3,000 to NASDAQ, 2,000 to an ATS, and 3,000 directly to a wholesaler—all in the same millisecond—whichever offers the best execution at that instant. As orders fill and the market moves, the router re-evaluates and sends any unfilled remainder to the next-best venue.

This is fundamentally different from a simple "send-to-primary-exchange" approach. In the old model, your entire order would land on one venue and wait. With a router, you get concurrent routing to multiple places, which statistically improves your odds of filling at or near the best price.

## How execution quality is measured

Brokers are legally required under regulations like Reg SHO and FINRA Rule 5310 to demonstrate **reasonable efforts** to achieve best execution. For stocks, this typically means:

- Comparing the [effective spread](/bid-ask-spread/) you actually paid against the quoted national best bid and offer (NBBO) at the time of your order.
- Evaluating order size, speed, and likelihood of execution.
- Reviewing the venues used and their execution statistics.

A smart order router is a broker's primary tool for proving it met this obligation. The router's logs show which venues received which portions of your order and what prices were available at each moment. If a broker used inferior routers or venues, and you consistently got worse fills than the NBBO offered, that becomes a compliance and liability issue.

For retail traders, this means your broker's router quality directly affects how much you pay or receive. A sophisticated, low-latency router that connects to more venues will typically beat a basic router that only uses one or two exchanges.

## Venues included in routing decisions

A smart order router connects to multiple types of trading venues:

| Venue type | Characteristics | Routing priority |
|---|---|---|
| **Primary exchanges** (NYSE, NASDAQ) | High volume, transparent pricing, regulatory oversight | Usually included first for large orders |
| **Regional exchanges** | Smaller volumes, lower fees, sometimes better pricing in illiquid stocks | Included for size and spread optimization |
| **Alternative trading systems (ATS)** | Smaller, faster, sometimes less transparent; higher wholesale volumes | Often used when spreads are tight |
| **Wholesalers / market makers** | Direct connections to firms like Citadel, Virtu, Jump Trading | Often fastest fill for certain stocks; controversial for retail orders |

The router weights each venue based on historical execution quality for that particular order size and stock. Over time, it learns which venues reliably give tight spreads and fast fills, and adjusts its algorithm accordingly.

## What happens with retail orders

Most retail brokers do not own proprietary smart order routers—they use third-party routing networks or sell order flow. This is a critical distinction. A broker that accepts payment for routing retail orders to a specific wholesaler (called **payment for order flow**, or PFOF) may not route to the venue with the absolute best price; instead, it routes to the highest bidder for that order.

This doesn't necessarily mean you get a bad fill. Wholesalers like Citadel Securities are highly competitive and have incentive to offer tight spreads (otherwise they'd lose order flow to rivals). But the router is optimizing for broker revenue, not purely for your execution quality. Regulators allow this under the assumption that wholesalers' spreads stay within a few cents of the NBBO, which often they do.

Brokers that do not accept PFOF (or disclose it clearly) typically use faster, more neutral routers that genuinely optimize across public exchanges first.

## Latency and order routing speed

A key advantage of smart order routing is **latency arbitrage**—the router can exploit millisecond price differences across venues faster than any single trader can react. If NASDAQ shows a better bid for Apple stock than NYSE, the SOR can route a portion of a buy order to NASDAQ before the NYSE data feed even updates on your screen.

This speed works in your favor when it means getting a better fill than you would have received at a single venue, but it also explains why institutional and high-frequency traders invest heavily in low-latency technology. They want their own orders to be processed by routers before retail orders, and they want their routers to see price improvements before retail routers do.

For retail traders, the practical implication is: the router your broker uses will always be faster than anything you can do manually. If you place a [market-order](/market-order/), the router will find the best price at that nanosecond. You cannot beat that by trying to time your order to a specific venue.

## Common misconceptions

**"My broker is sending my order to one venue."** If your order is routed through a modern broker platform, an SOR is almost certainly active—even if you don't see it. The router splits the order internally and across multiple venues simultaneously.

**"Smart routing always gets me the absolute best price."** Routers optimize for best *reasonable* execution within your broker's setup. If your broker uses PFOF, the router may not send your order to the exchange with the tightest spread. Regulators allow this, but it's not "absolute best."

**"I can see which venue my order went to."** Most brokers do not surface this information to retail traders in real time, though some disclose it in order confirmations. Your broker's system will know; you may not.

## See also

<div class="wiki-seealso">

### Closely related

- [Market-Maker-Trading](/market-maker-trading/) — How wholesalers and exchange market makers interact with routed orders
- [Bid-Ask-Spread](/bid-ask-spread/) — The spread your router is trying to minimize
- [Market-Order](/market-order/) — How routers handle immediate execution requests
- [Limit-Order](/limit-order/) — Routing behavior differs for price-protected orders
- [Price-Discovery](/price-discovery/) — How routers monitor and react to changing venue quotes
- [Broker](/broker/) — Role of the broker's technology in order routing quality

### Wider context

- [Stock-Exchange](/stock-exchange/) — The venues that routers connect to
- [Finra](/finra/) — Regulator that enforces best-execution rules
- [Securities-And-Exchange-Commission](/securities-and-exchange-commission/) — Oversees order routing and wholesaler relationships
- [Market-Risk](/market-risk/) — Execution risk is a form of market friction

</div>
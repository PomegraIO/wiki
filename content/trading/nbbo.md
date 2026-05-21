---
title: "NBBO"
description: "The NBBO (national best bid and offer) is the best buy price and best sell price across all U.S. stock exchanges at any given moment. It is the reference point for fair pricing and regulatory compliance under Reg NMS."
keywords:
  - NBBO
  - national best bid and offer
  - best price
  - market quotation
image: "/svg/trading.svg"
---

*The **NBBO** (national best bid and offer) is the highest bid and lowest ask across all U.S. stock exchanges and venues at a given instant. If NASDAQ quotes Apple at $150.00 bid / $150.01 ask, and NYSE quotes $150.005 bid / $150.02 ask, the NBBO is $150.00 bid (best NASDAQ bid) and $150.01 ask (best NASDAQ ask). The NBBO is the law: Reg NMS requires that your order cannot execute at a worse price than the NBBO, and brokers must route to achieve NBBO (or better).*

<div class="wiki-hatnote">

For price discovery, see [lit venue](/lit-venue). For routing to achieve NBBO, see [smart order router](/smart-order-router). For the regulation, see Reg NMS.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NBBO — key facts</div>

<img src="/svg/trading.svg" alt="Multiple exchange quotes converging to NBBO" />

<div class="wiki-infobox-caption">NBBO: the best bid and ask across all U.S. venues, updated in real time.</div>

|   |   |
|---|---|
| **What it is** | Best bid and ask across all U.S. exchanges |
| **Updated** | Continuously (hundreds of times per second) |
| **Who tracks it** | SIPs (Securities Information Processors); all brokers have access |
| **Uses** | Price comparison, best execution, trade-through rule compliance |
| **Regulation** | Central to Reg NMS; brokers must not trade through NBBO |

</aside>

## How NBBO works

At any given instant, the NBBO consists of:

- **Best bid:** The highest price anyone is willing to pay, across all U.S. venues.
- **Best ask:** The lowest price anyone is willing to sell at, across all U.S. venues.

**Example:**

| Venue | Bid | Ask |
|---|---|---|
| NASDAQ | $150.00 | $150.02 |
| NYSE | $150.005 | $150.01 |
| CBOE | $149.99 | $150.03 |
| Dark pool (Citadel) | $150.005 | $150.015 |

**NBBO: $150.00 bid (NASDAQ) / $150.01 ask (NYSE)**

The NBBO represents the tightest spread available across all venues. If you want to buy, the best available ask is $150.01 (on NYSE). If you want to sell, the best available bid is $150.00 (on NASDAQ).

## Who provides NBBO data?

**Securities Information Processors (SIPs):** The SEC-regulated systems that collect quote and trade data from all exchanges and disseminate it publicly.

- **UTP SIP:** For NASDAQ-listed stocks.
- **CTA SIP:** For NYSE and other listed stocks.

These update the NBBO hundreds of times per second and distribute it to all market participants.

## NBBO and the trade-through rule

Reg NMS's trade-through rule states: **Your order cannot execute at a worse price than the NBBO.**

**Example:** NBBO is $150.00 bid / $150.01 ask. Your broker receives a buy order and routes to NASDAQ, where the ask is $150.02. This would be a "trade-through" — you would buy at $150.02 when the NBBO (best ask) is $150.01. This is illegal (with exceptions).

Your broker must either:
- Route to NYSE where the ask is $150.01 (the NBBO).
- Or use a smart order router to find the NBBO and route there first.

## NBBO and best execution

NBBO is central to [best execution](/best-execution):

- Brokers must route orders to achieve prices equal to or better than NBBO.
- Best execution rules require checking all venues (including dark pools) to ensure you are getting NBBO or better.
- Regular audits must verify that the broker's routing achieves this.

## The NBBO across dark pools

An interesting complexity: dark pools are not included in the NBBO calculation. Dark pools are opaque; their bid-ask is not visible.

This means:
- A dark pool might have a better price than the NBBO.
- But the NBBO (calculated from lit venues only) does not reflect it.
- Brokers route to dark pools as an alternative to NBBO, but dark pool execution is not "forced" by the NBBO rule.

## NBBO latency and race conditions

In fast markets, NBBO becomes a "moving target." By the time your order reaches the NBBO venue, the quote might have moved. Modern regulation allows for brief latency — you cannot be faulted for a trade-through if the NBBO changed between when your order was submitted and when it was routed.

However, [high-frequency traders](/high-frequency-trading) exploit latency: they can see NBBO changes slightly before retail traders' orders arrive, allowing them to trade ahead.

## Exceptions to the trade-through rule

The trade-through rule has some exceptions:
- **Executions** at the NBBO are always okay (no exception needed).
- **Stability exceptions:** In fast markets or system outages, brokers can trade-through temporarily.
- **Inactive quotes:** If a venue's NBBO quote is not genuinely available (the venue is down), the trade-through is not a violation.

## NBBO for different asset classes

- **Equities:** NBBO is clearly defined by Reg NMS.
- **Options:** Similar NBBO rules apply through the Options Regulatory Authority.
- **Futures:** Exchanges operate NBBO-like rules internally, but the national SIPs do not aggregate across futures exchanges.

## Historical context: why NBBO was created

Before Reg NMS (2007), different exchanges quoted different prices for the same stock. Brokers could route to the most convenient venue without seeking best prices. This led to market fragmentation and poor prices for retail investors.

Reg NMS and the creation of NBBO mandated price unity: all venues show prices simultaneously, and brokers must seek the best price across all of them.

## See also

<div class="wiki-seealso">

### Closely related

- Bid-ask spread — the spread reflects NBBO
- [Best execution](/best-execution) — regulatory goal tied to NBBO
- Trade-through rule — enforces NBBO compliance
- [Smart order router](/smart-order-router) — routes to achieve NBBO

### Market structure and venues

- [Lit venue](/lit-venue) — exchanges contribute to NBBO
- [Dark pool](/dark-pool) — not part of NBBO, but offers alternative prices
- Order book — where bids and asks that form NBBO sit
- [Stock exchange](/stock-exchange) — sources of NBBO quotes

### Regulation and compliance

- Reg NMS — mandates NBBO and trade-through rule
- SEC — defines and enforces NBBO
- SIP — Securities Information Processor that calculates NBBO
- Order protection rule — related safeguard

### Execution and pricing

- [Market order](/market-order) — executes at NBBO (best available)
- [Limit order](/limit-order) — priced relative to NBBO
- **Quote dissemination** — NBBO is published in real time

</div>

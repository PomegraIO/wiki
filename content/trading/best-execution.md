---
title: "Best execution"
description: "Best execution is a regulatory obligation requiring brokers to obtain the most favorable terms available for their customer orders. This means seeking the best prices, lowest fees, and fastest execution across all available venues."
keywords:
  - best execution
  - regulatory obligation
  - order routing
  - trading
image: "/svg/trading.svg"
---

*Best execution is a fundamental rule: brokers must obtain the best possible prices and terms for their customers' orders. In the U.S., this is mandated by Reg NMS and [FINRA](/finra) rules. It means checking multiple venues (exchanges, dark pools, market makers), routing orders to achieve the best price, and regularly auditing whether the execution quality is truly best. Brokers that fail to provide best execution face regulatory penalties.*

<div class="wiki-hatnote">

For how routing works, see [smart order router](/smart-order-router). For venues where orders execute, see [lit venue](/lit-venue) and [dark pool](/dark-pool).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Best execution — key facts</div>

<img src="/svg/trading.svg" alt="A trading terminal showing multiple venues and prices" />

<div class="wiki-infobox-caption">Best execution: broker checks multiple venues to find the best price.</div>

|   |   |
|---|---|
| **What it is** | Regulatory obligation to achieve best prices for customers |
| **Required by** | SEC (Reg NMS), FINRA, and other regulators |
| **Factors considered** | Price, execution speed, size, likelihood of fill |
| **Venues checked** | All lit exchanges, dark pools, and broker ECNs |
| **Audit requirement** | Brokers must regularly test whether execution is truly best |
| **Consequence of failure** | Regulatory action, fines, restitution to customers |

</aside>

## What is "best execution"?

Best execution does not simply mean "lowest price." It considers multiple factors:

**Price:** The primary factor; brokers should route to achieve the best bid (for sells) or ask (for buys).

**Speed:** Execution should be fast; latency matters, especially for market orders.

**Size:** Can you get your entire order filled, or will you face a partial fill and have to resubmit?

**Likelihood of fill:** Is the price/size reliable, or might the order be rejected?

**Cost:** Are exchange fees or other costs lower at one venue vs. another?

**Overall quality:** The combination of the above should be optimal.

For example: Venue A offers a slightly better price ($150.02 vs. $150.021) but might not fill your 10,000-share order quickly. Venue B offers a slightly worse price but will fill the entire order immediately. Best execution might be Venue B, depending on the circumstances.

## Regulation of best execution

**U.S. equity markets:**
- Regulation NMS (Reg NMS) mandates best execution.
- [FINRA Rule 5310](/finra) requires member brokers to have best execution policies.
- Brokers must document their routing logic and test it regularly.

**International:**
- European Union: MiFID II requires best execution.
- Other countries have similar rules.

**Enforcement:**
- The SEC and FINRA audit brokers' best execution compliance.
- Violations can result in fines, restitution to customers, and regulatory sanctions.

## How brokers meet best execution

**Smart order routing:** Brokers use [smart order routers](/smart-order-router) to check all venues simultaneously and route to the best venue(s).

**Regular audits:** Brokers must periodically review their routing:
- Did we achieve best execution? 
- Are any venues consistently offering better prices?
- Should we adjust our routing logic?

**Documentation:** Brokers must document their best execution policies and make them available to customers (usually in the broker's terms and conditions).

**Conflict management:** If the broker operates a market-making desk or has [payment-for-order-flow](/payment-for-order-flow) arrangements, it must ensure those relationships do not compromise best execution for customers.

## The challenge: trade-offs

Best execution is not always straightforward. Consider:

- A lit exchange offers price $150.00 (best), but with 1,000 shares available.
- A dark pool offers price $149.98 (worse), but with 10,000 shares available.
- You want to buy 8,000 shares.

Is it better to split between the two (get some at $150.00 but most at $149.98, average $149.99)? Or just hit the dark pool at $149.98? Best execution requires judgment and analysis.

## Best execution and dark pools

A controversial aspect of best execution is the role of dark pools. Dark pools often offer mid-market pricing (the midpoint of the lit-market spread). A broker might route to a dark pool even though:

- The lit market's best ask is $150.02.
- The dark pool quotes $150.01 (midpoint).
- But the dark pool is not required to fill your entire order; the lit market will.

Is this best execution? Regulators say yes, if the probability-weighted execution is better. But critics argue dark pools reduce price discovery and harm retail investors.

## Best execution and payment for order flow

[Payment for order flow](/payment-for-order-flow) creates a tension with best execution:

- A broker receives payment for routing orders to a particular market maker.
- That market maker might not offer the absolute best price.
- The broker must justify routing there as consistent with best execution (arguing the market maker's price is competitive).

Regulators scrutinize PFOF arrangements to ensure brokers are not sacrificing customer prices for payment.

## Real-world example

You place a market buy order for 1,000 shares of Apple with your broker. Your broker's system:

1. Checks NASDAQ: ask $150.02
2. Checks NYSE: ask $150.025
3. Checks Citadel dark pool: $150.015
4. Checks Morgan Stanley dark pool: $150.02
5. Checks Goldman Sachs dark pool: $150.01 (1,000 shares available)

Best execution analysis:
- Goldman has the best price at $150.01 but only 1,000 shares (exactly what you need).
- Route entire order to Goldman at $150.01.

Result: You buy 1,000 shares at $150.01. Best execution achieved.

If the broker had routed to NASDAQ at $150.02, you would have paid $10 more ($0.01 × 1,000 shares). The broker would have violated best execution.

## Retail vs. institutional best execution

**Retail:** Brokers have general best execution obligations, but execution quality is often averaged across many small orders. Your individual $1,000 order might not get intensive optimization.

**Institutional:** Brokers typically agree to specific best execution standards (e.g., achieve VWAP within 1 basis point). Institutions actively monitor and negotiate better terms.

## The future of best execution

As technology improves and more venues emerge (especially abroad), best execution obligations will likely become more complex. Brokers will need:
- Faster routing systems.
- Better monitoring and auditing.
- Clearer conflict management.

Regulators will continue to evolve best execution standards to balance broker incentives with customer protection.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart order router](/smart-order-router) — tool brokers use to achieve best execution
- Regulation NMS — mandates best execution
- MiFID II Best Execution — European equivalent
- Trade-through rule — protects prices on lit venues

### Order routing and venues

- [Lit venue](/lit-venue) — public exchange for best execution
- [Dark pool](/dark-pool) — alternative venue raising best execution questions
- [NBBO](/nbbo) — national best bid-offer; best execution targets this
- [Payment for order flow](/payment-for-order-flow) — potential conflict with best execution

### Execution and quality

- [Market order](/market-order) — execution subject to best execution rules
- [Limit order](/limit-order) — routed for best execution
- Slippage — cost that best execution rules try to minimize
- Execution quality — metrics tracking actual fills

### Regulatory

- [FINRA](/finra) — enforces best execution
- SEC — writes best execution rules
- [Reg SHO](/regulation-sho) — related short-sale rules

</div>

---
title: "Reg NMS Trade-Through Rule Explained"
description: "Reg NMS trade-through rule explained: the specific prohibition against bypassing better prices, which orders are exempt, and how it differs from broader order protection."
keywords:
  - reg nms trade-through rule explained
  - trade-through prohibition
  - market regulation order protection
  - best execution requirement
  - securities exchange rules
image: /svg/regulation.svg
---

*The trade-through rule within Regulation NMS (National Market System) is a core prohibition in U.S. stock markets: a [broker](/broker/) or exchange cannot knowingly execute a trade at a worse price when a better price is available elsewhere. This seemingly simple rule shapes market structure, [liquidity](/liquidity-risk/), and order routing. Understanding what it forbids, which orders are exempt, and where its boundaries lie is essential for traders and compliance professionals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg NMS Trade-Through Rule — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The rule that prevents exchanges from offering worse prices than competitors.</div>

|   |   |
|---|---|
| **Rule identifier** | SEC Rule 10b-5-1 within Reg NMS |
| **Core prohibition** | Execute at a worse price when better price exists |
| **Applies to** | Stock trades in listed securities across all venues |
| **Enforcement** | [SEC](/securities-and-exchange-commission/), [FINRA](/finra/), self-regulatory organizations |
| **Main exemptions** | Odd-lot orders, orders with explicit instructions, manual broker routing |
| **Interplay with** | Order protection rule (price), market data rules (transparency) |

</aside>

## What the Trade-Through Rule Does

The **trade-through rule** forbids executing a customer order at a price worse than the best displayed price available at another market venue at the moment the order is submitted. In practice: if the S&P 500 is trading at $460 on the New York Stock Exchange and $459.99 on NASDAQ, an exchange or broker cannot execute a sell order at $459.98 when the NYSE is posting a better (higher) price. To do so would be a trade-through—a trade executed in violation of a better price elsewhere.

The rule applies across all U.S. stock exchanges and alternative trading systems (ATSs). It is one of three core pillars of Reg NMS, alongside the [order protection rule](/reg-nms-trade-through-rule-explained/) (which addresses order execution quality) and the market data rules (which govern quote dissemination).

Mechanically, the rule is enforced by order-routing systems. When an exchange or broker receives an order, its system checks the National Best Bid and Offer (NBBO)—the best prices available across all venues at that moment. If the order can be filled at a price better than or equal to the NBBO, execution is clean. If the only way to fill the order is at a worse price, the broker has two choices: route the order to the venue with the NBBO, or reject it and let the customer decide whether to accept a worse fill.

## Which Orders Are Exempt

Not all orders face the trade-through prohibition. Key exemptions include:

**Odd-lot orders** (fewer than 100 shares) are exempt. If you sell 50 shares, the trade-through rule does not apply. This is partly because odd-lot liquidity is fragmented and the administrative burden of checking every small order across venues was deemed excessive. In practice, odd-lot fills often happen outside the NBBO because liquidity is thinner and spreads wider.

**Orders with explicit instructions** from the customer bypass the rule. If you tell your broker "execute on NYSE no matter what the NBBO says," and you do so in writing or via a system that logs the instruction, your broker can honor that request without triggering a violation. This opt-out is rare for retail investors but common in institutional trading where a client wants execution on a specific exchange for strategic reasons.

**Orders routed by a manual broker** (human broker, not electronic system) have more flexibility. A broker manually executing a trade and exercising reasonable judgment is given some slack, particularly in fast-moving markets. The rule does not require the broker to break off a fill to chase a one-cent improvement on another venue.

**Short-sale orders** and **orders involving volatility halts** or circuit breakers are handled differently. When trading is halted, the NBBO may be stale, and trade-through compliance is suspended until trading resumes.

## Trade-Through vs. Order Protection

The trade-through rule is often confused with the broader order protection rule (also part of Reg NMS). They are related but distinct.

The **trade-through rule** forbids execution at a price worse than the best available elsewhere.

The **order protection rule** (Rule 10b-5-2) requires that orders receive the benefit of the best displayed price at any venue. If an exchange displays a bid of $100 and an order arrives to buy at $100.10, it must be offered the chance to trade at $100, not forced to trade at $100.10.

In practice, the trade-through rule is the tighter of the two. A broker cannot even initiate a trade-through, whereas the order protection rule ensures an order is not passed by without a fair shot at better prices. Trade-through is about venue-to-venue comparison; order protection is about fairness to the arriving order.

## The Incremental Penny and Practical Boundaries

The rule applies at the penny level, but with gray areas. If the NBBO is $100.00 × $100.01 (bid and ask), and you have a sell order, you should offer it to the $100.00 bid before executing elsewhere at $99.99. But if the price moves to $99.99 × $100.00 by the time your order routes, there is no trade-through because $99.99 is now the best bid.

This microsecond-level race condition is real. Markets are asynchronous. Prices update at different venues at different moments, and the NBBO is a snapshot that may be stale by nanoseconds by the time a trade executes. Regulators and exchanges tolerate small race conditions under a "reasonable efforts" standard rather than demanding atomically simultaneous execution.

## Why the Rule Matters

The trade-through rule creates incentives for [price discovery](/price-discovery/). If every exchange knows that customers can instantly compare prices and avoid being traded through, exchanges compete on pricing. A venue that habitually prices worse than competitors will lose order flow. This is a primary mechanism for market fragmentation and competition among [exchanges](/stock-exchange/).

The rule also protects retail and institutional investors from having their orders filled at obviously worse prices than available elsewhere. Without it, an exchange could post a wide spread and know that order routers would be forced to fill there even if better prices existed on a rival exchange.

However, the rule also has costs. It adds latency (routers must check the NBBO before executing). It fragments execution across venues, which can make [liquidity](/liquidity-risk/) less concentrated and increases slippage in fast-moving markets. Some argue that the rule protects passive displayed [liquidity](/liquidity-risk/) but may disadvantage active traders who benefit from information asymmetries.

## Enforcement and Real-World Gaps

The [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/) enforce the trade-through rule through examinations and case-by-case enforcement. Brokers are expected to have systems that block trade-throughs before they occur. When violations happen, they are treated as failures of controls rather than intentional misconduct (in most cases).

In practice, not every trade-through is detected or prosecuted. High-frequency trading firms, dark pools, and alternative trading systems have all faced enforcement actions for systematic trade-through violations. But the rule's effectiveness depends on the quality of a broker's order-routing infrastructure, and small brokers may have less sophisticated systems than large institutions.

## See also

<div class="wiki-seealso">

### Closely related

- [Order protection rule](/reg-nms-trade-through-rule-explained/) — Broader Reg NMS framework
- [National Best Bid and Offer (NBBO)](/bid-ask-spread/) — The price standard enforced by the rule
- [Broker](/broker/) — Entity responsible for avoiding trade-throughs
- [Stock exchange](/stock-exchange/) — Venues subject to the rule
- [Alternative trading system](/alternative-trading-system/) — ATS participation in Reg NMS

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Primary enforcer
- [FINRA](/finra/) — Self-regulatory organization role
- [Price discovery](/price-discovery/) — Market function enabled by competition
- [Market maker](/market-maker-trading/) — Liquidity provider impacted by the rule

</div>

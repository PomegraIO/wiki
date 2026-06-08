---
title: "National Best Bid and Offer"
description: "A regulatory requirement that brokers must execute client orders at the best available price across all lit trading venues."
keywords:
  - nbbo
  - quote aggregation
  - best execution
  - price improvement
image: "/svg/markets.svg"
---

*The **National Best Bid and Offer** (NBBO) is the highest bid price and lowest offer price visible across all regulated US equity trading venues at any moment. Brokers are required by law to route customer orders to execute at or better than the NBBO, ensuring that a buyer gets the best available ask price and a seller gets the best available bid—even if different venues offer those prices simultaneously.*

## The fragmentation problem it solves

Before the NBBO rule, a trader could place a market order with a broker and execute at a terrible price simply because the broker routed internally or to a single venue, even when a better price existed elsewhere. If Island's order book showed 1,000 shares for sale at $50.00 and your broker's internal pool showed 1,000 shares at $50.05, the broker could legally fill you at $50.05 and pocket the difference—without disclosure.

The NBBO requirement, born from Regulation SHO (2005) and formalized through subsequent SEC guidance, mandates that this cannot happen. The broker must check all lit venues in real time, identify the consolidated best prices, and route the order to capture them. If no single venue has the entire order available at the best prices, the broker must split the order across venues.

## How NBBO is calculated

The NBBO aggregates quotes from all registered stock exchanges (NYSE, NASDAQ, BATS, etc.) and eligible [alternative trading systems](/alternative-trading-system/). A real-time data feed compiles every bid and ask, finds the highest bid and lowest ask, timestamped to microseconds. That consolidated quote becomes the reference for best execution.

The calculation is straightforward in principle: best bid = max(all bids); best ask = min(all asks). But the implementation is complex. Venues update quotes constantly. A split-second delay between venues means quotes at different price levels briefly exist simultaneously. Professional traders exploit these arbitrage windows. A trader might see stale quotes from a slower feed and route orders based on outdated NBBO.

## Locked and crossed markets

When the best bid on one venue equals the best ask on another, the market is "locked." When the best bid exceeds the best ask, it is "crossed." These conditions last microseconds before arbitrage or trade execution eliminates them, but during that window, the NBBO is ambiguous. SEC rules and exchange rules permit certain exceptions: locked/crossed markets are tolerated briefly, and some intraday price improvement mechanisms (like [order routing](/broker/) to [alternative trading systems](/alternative-trading-system/)) are exempted if they provide measurable benefit.

## Impact on fragmentation and retail quality

The NBBO rule did not prevent [market fragmentation](/market-fragmentation/); instead, it forced venues to compete on who could offer the best prices at high volume. A retail order for 100 shares must execute at the NBBO, but a larger order might strip through multiple venues at progressively worse prices as liquidity thins.

For retail traders, the NBBO guarantee improved outcomes materially. Spreads narrowed across most liquid stocks. However, the rule's effectiveness depends on broker compliance. Some brokers offer payment for order flow (rebates from market makers) in exchange for routing to non-NBBO venues, as long as execution is still NBBO. Others use their own dark pools, which are outside the NBBO calculation and operate under different rules.

## The role of market data

NBBO requires real-time dissemination of all venue quotes. The SEC mandates that exchanges and ATSs publish their best bid and offer immediately, feeding into consolidated data feeds operated by industry groups like SIFMA. These feeds supply the NBBO to brokers, data vendors, and the public.

The cost of accessing real-time NBBO data is substantial. Broker firms, market makers, and professional traders subscribe to premium feeds that deliver NBBO with minimal latency. Retail investors often rely on delayed or lower-quality feeds. This information asymmetry can matter: a professional trader sees the true NBBO microseconds before it arrives at a retail broker's system, allowing them to front-run orders or redirect their own flow accordingly.

## Enforcement and exceptions

The SEC monitors NBBO compliance through surveillance programs and broker audits. Violations—failing to execute at the NBBO when possible—result in fines and enforcement actions. The penalties have reached tens of millions of dollars for large firms.

That said, the NBBO rule has technical limits. Some order types, like [marketable limit orders](/market-order/) that interact with prices inside the NBBO, fall into grey zones. [Directed orders](/broker/) routed to a specific venue may execute worse than NBBO under certain logic. And retail orders small enough to be filled in a single [alternative trading system](/alternative-trading-system/) may execute at the best NBBO rather than the absolute best available on smaller venues.

## See also

<div class="wiki-seealso">

### Closely related

- [Electronic Communication Network](/electronic-communication-network/) — automated venues that compete to post the best NBBO prices
- [Alternative Trading System](/alternative-trading-system/) — regulated off-exchange venues included in NBBO calculation
- [Market Fragmentation](/market-fragmentation/) — the structural reality that NBBO addresses but does not eliminate
- [Broker](/broker/) — firms responsible for executing orders at or better than NBBO
- [Price Discovery](/price-discovery/) — how consolidated quote visibility improves market pricing
- [Bid-Ask Spread](/bid-ask-spread/) — narrowed by NBBO competition
- [Over-the-Counter Market](/over-the-counter-market/) — lacks unified NBBO oversight for many securities

### Wider context

- [Market Maker Trading](/market-maker-trading/) — NBBO forces makers to compete on price
- [Stock Exchange](/stock-exchange/) — primary venues included in NBBO feeds
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator that enforces best execution rules

</div>

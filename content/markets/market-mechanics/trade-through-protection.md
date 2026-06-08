---
title: "Trade-Through Protection"
description: "A Regulation NMS requirement that brokers must route orders to execute at the best available price across venues rather than at an inferior price locally."
keywords:
  - trade-through protection
  - reg nms
  - order routing
  - best execution
  - nbbo
  - market fragmentation
image: "/svg/markets.svg"
---

*[Trade-through protection](/trade-through-protection/) is a core principle of [Regulation NMS](/securities-and-exchange-commission/) that prohibits a [broker](/broker/) from executing a customer's order at a price worse than the best available price displayed on another venue at that moment. If the national best bid is $50.00 and the national best ask is $50.05, a broker cannot fill a buy order at $50.06, nor can it fill a sell order at $49.99 without first routing to the venue displaying the better price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade-Through Protection — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and mechanics." />

<div class="wiki-infobox-caption">A regulatory safeguard that forces competition between venues and ensures order execution at the fairest available price.</div>

|   |   |
|---|---|
| **What it is** | Rule under Reg NMS (2007) prohibiting execution at prices worse than the [NBBO](/stock-exchange/) |
| **Applies to** | Equities, most securities traded across [exchanges](/stock-exchange/) and [alternative trading systems](/alternative-trading-system/) |
| **NBBO definition** | Best bid and best ask aggregated from all venues (via the SIP—Securities Information Processor) |
| **Broker obligation** | Must route orders to achieve best execution or risk liability |
| **Penalties** | [SEC](/securities-and-exchange-commission/) enforcement, fines, customer refunds for trade-through losses |
| **Exceptions** | Certain venue-specific orders, intermarket sweep orders (ISOs), and defined block trades |

</aside>

## The fragmentation problem that created the rule

Before [Regulation NMS](/securities-and-exchange-commission/) was adopted in 2005 (and went live in 2007), US [equity markets](/stock-exchange/) were highly fragmented but loosely coordinated. The [NYSE](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) dominated, but dozens of regional exchanges and electronic communication networks (ECNs) also listed the same securities. Each venue had its own [bid-ask spread](/bid-ask-spread/) and its own order queue.

The problem was straightforward: a [broker](/broker/) could execute a customer's order on its preferred venue (where it had favourable economics or a direct connection) even if another venue was displaying a materially better price. For example, a customer wanted to buy 1,000 shares of a stock. The best ask on Venue A was $50.00, but the customer's [broker](/broker/) had a thick [market maker](/market-maker-trading/) relationship on Venue B, where the ask was $50.05. Without a rule, the [broker](/broker/) might route to Venue B, costing the customer $50 per share unnecessarily.

Multiplied across millions of trades, these "trade-throughs"—executions at worse prices than displayed elsewhere—cost investors billions annually. The [SEC](/securities-and-exchange-commission/) recognized this as a market-integrity failure and introduced Reg NMS to impose a unified standard: brokers must route to the best available price, regardless of venue affinity or order flow rebates.

## How trade-through protection works

The mechanism relies on a concept called the **National Best Bid and Offer** (NBBO). The [SEC](/securities-and-exchange-commission/) mandates that all exchanges and venues broadcast their best bid (the highest price any buyer will pay) and best ask (the lowest price any seller will accept) to a central aggregator known as the [Securities Information Processor](/securities-and-exchange-commission/) (SIP).

The SIP collects these quotes in real-time and publishes a consolidated NBBO: the highest bid and lowest ask across all venues. That NBBO becomes the regulatory standard for "best price."

Under the [Order Protection Rule](/securities-and-exchange-commission/) (part of Reg NMS), a [broker](/broker/) cannot execute a customer's order at a price worse than the current NBBO. Concretely:

- If you place a **buy order** and the NBBO ask is $50.05, your [broker](/broker/) must either fill you at $50.05 or better, or explain why (e.g., the ask moved before the order could be routed).
- If you place a **sell order** and the NBBO bid is $50.00, your [broker](/broker/) must either fill you at $50.00 or better, or justify any shortfall.

The burden of proof is on the [broker](/broker/). If you execute at $50.10 on a buy order when the NBBO was $50.05, the [SEC](/securities-and-exchange-commission/) can treat that as a trade-through violation. The [broker](/broker/) must refund the difference or face enforcement action.

## Latency and the complications of "best price"

In theory, trade-through protection is clean: check the NBBO, route to the venue displaying it, execute. In practice, latency ruins this simplicity.

The NBBO is transmitted over a network to traders and brokers. That transmission takes time—tens to hundreds of milliseconds. Meanwhile, the actual quotes on individual venues may have moved. A trader with a direct connection to Venue A might see Venue A's price in real-time, while the NBBO feed they receive (aggregated and transmitted by the SIP) is slightly stale. If Venue A has just improved its bid, but the NBBO hasn't been updated yet, the trader might trade at Venue A at a price that would have been a trade-through if measured against the "true" (but not yet publicly known) NBBO.

The [SEC](/securities-and-exchange-commission/) recognizes this latency reality and allows a brief grace period. If a [broker](/broker/) routes in good faith to execute at the NBBO as displayed at the moment of order arrival, and the market moves before execution completes, that's generally not a trade-through violation. The key test is intent: did the [broker](/broker/) attempt to route for best execution?

## Order routing and broker incentives

Trade-through protection also interacts with **order routing**—the decision of where to send an order. Before Reg NMS, brokers had wide discretion. They could route to venues with rebates, to preferred [market makers](/market-maker-trading/), or to internal pools. Reg NMS doesn't forbid rebates or preferences, but it subordinates them to the trade-through rule: best price comes first.

Modern brokers use sophisticated routing algorithms to execute the "fastest best price"—they scan multiple venues, identify the NBBO, and route automatically. For very large orders (blocks), a [broker](/broker/) might negotiate with a [market maker](/market-maker-trading/) away from the exchange floor, but even then, the final price must satisfy the NBBO or be disclosed as an exception.

The result is that venues compete intensely on price. If Venue A's ask is $50.05 and Venue B's is $50.00, all order flow wanting the best execution routes to Venue B. Venue A must either match $50.00 or tighten its spread to stay competitive. This venue-level price competition is the competitive benefit of trade-through protection.

## Exceptions and fine print

Trade-through protection has important exceptions:

**Intermarket Sweep Orders (ISOs):** A [broker](/broker/) can place simultaneous orders on multiple venues to "sweep" the best prices at each. If an ISO is properly flagged, the [broker](/broker/) doesn't violate trade-through rules even if some fills occur while better prices appear on other venues—the order sweeps them all at once.

**Venue-Specific Orders:** If a customer specifies a particular venue ("buy on NYSE"), the [broker](/broker/) can route there even if the NBBO is better elsewhere. The customer has opted out of trade-through protection by choice.

**Block Trades:** Large block trades (typically 10,000+ shares) conducted away from the venue often receive relief from the strict NBBO standard, as long as they are reported within prescribed timeframes.

**Closing Auction Imbalances:** During the [opening and closing auctions](/stock-exchange/) on NYSE and NASDAQ, there are explicit exceptions to allow auction prices to differ from the NBBO.

## Enforcement and violations

The [SEC](/securities-and-exchange-commission/) monitors trade-through compliance through data feeds and periodic audits of major [brokers](/broker/). When a violation is found—a pattern of executions at prices worse than the NBBO—the [SEC](/securities-and-exchange-commission/) can:

- Issue a **cease-and-desist order** requiring the [broker](/broker/) to implement better controls.
- Impose **fines**, often in the millions (major brokers have paid $10–50+ million for systemic trade-through violations).
- Require **customer refunds** for the aggregate amount of overpayment.

High-profile settlements include JPMorgan and Morgan Stanley, who were found to have routed orders to less-efficient internal pools without proper NBBO compliance, costing customers millions.

## See also

<div class="wiki-seealso">

### Closely related

- [Locked and Crossed Markets](/locked-and-crossed-markets/) — Pricing anomalies where trade-through protection is tested by latency and fragmentation.
- [Price-Time Priority](/price-time-priority/) — The queue rule that determines which orders execute first once a venue is selected.
- [Bid-Ask Spread](/bid-ask-spread/) — The cost of immediacy, which trade-through protection helps minimise by forcing venue competition.
- [Market Maker Trading](/market-maker-trading/) — The professionals who quote on multiple venues and face trade-through incentives.
- [Alternative Trading System](/alternative-trading-system/) — ECNs and other non-exchange venues that benefit from trade-through rules.
- [Broker](/broker/) — The intermediary responsible for implementing best execution.
- [Circuit Breaker and Trading Halt](/circuit-breaker-trading-halt/) — Rules that pause trading when conditions become disorderly.

### Wider context

- [Stock Exchange](/stock-exchange/) — The primary venues regulated under Reg NMS.
- [SEC](/securities-and-exchange-commission/) — The regulator that adopted and enforces Regulation NMS.
- [Price Discovery](/price-discovery/) — The process of finding equilibrium, enhanced by trade-through protection's venue competition.
- [Equity ETF](/equity-etf/) — Baskets of stocks whose components all fall under trade-through rules.
- [Over-the-Counter Market](/over-the-counter-market/) — OTC trading (less regulated) where trade-through rules do not apply.

</div>

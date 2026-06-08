---
title: "Reg NMS Order Protection Rule Explained"
description: "Reg NMS Rule 611 (Order Protection Rule) prohibits trade-throughs and requires intermarket sweep obligations, forcing brokers to route orders to the best prices across venues."
keywords:
  - reg nms order protection rule
  - rule 611 trade through prohibition
  - intermarket sweep obligation
  - order routing rules
  - market protection
image: "/svg/markets.svg"
---

*Regulation NMS Rule 611, the **Order Protection Rule**, forbids brokers from executing an order at a worse price when a better price is available on another exchange. The rule also imposes an **intermarket sweep obligation** (ISO), requiring aggressive orders to simultaneously check all venues for better prices. Together, these rules ensure orders are routed efficiently and customers get the best bid or offer available.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg NMS Order Protection Rule — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for markets." />

<div class="wiki-infobox-caption">Rule 611: The trade-through ban and sweep rules that govern multi-venue order routing.</div>

|   |   |
|---|---|
| **Rule number** | 611; part of Regulation National Market System (Reg NMS) |
| **Effective date** | June 10, 2007 (revised 2024 with subpenny quote rule) |
| **Core obligation** | No execution at a worse price when better price is publicly available |
| **Venues covered** | All exchanges, ATSs, and [market makers](/market-maker-trading/) |
| **Intermarket Sweep Obligation (ISO)** | Aggressive orders must simultaneously route to all better prices |
| **Exemptions** | Certain order types (orders at market opening, closing auctions, directed orders) |
| **Enforcement** | SEC and [FINRA](/finra/) |

</aside>

## The core rule: no trade-throughs

Rule 611 is deceptively simple: if your broker receives an order to buy 100 shares at $50.00 or better, and a different exchange is displaying a seller at $49.95, your broker **cannot** execute you at $50.00 on its home exchange. Your broker must route the order to the exchange showing $49.95, or simultaneously send orders to all venues showing better prices.

A **trade-through** is an execution that violates this rule. If $49.95 is available and you are filled at $50.00 instead, your broker has traded through the better price—a breach.

Before Reg NMS (pre-2007), this problem was rampant. The fragmentation of U.S. equity trading across dozens of small exchanges meant that the best prices were scattered. A retail investor could pay a worse price than the best publicly available quote. Rule 611 was designed to end that.

## How the intermarket sweep obligation (ISO) works

Rule 611's second mechanism is the **Intermarket Sweep Obligation** (ISO). When a broker receives an aggressive order (market order or an order priced to execute across multiple exchanges), the broker cannot simply pick one venue and route there. Instead, the broker must simultaneously route portions of the order to **all venues showing a better price**.

**Worked example:** You place a market order to buy 500 shares. The current market is:
- Exchange A: Best ask (seller) at $50.00 (500 shares available)
- Exchange B: Best ask at $49.95 (300 shares available)
- Exchange C: Best ask at $50.05 (200 shares available)

Your broker must NOT send all 500 shares to Exchange A (the trade-through violation). Instead, under ISO, your broker simultaneously routes:
- 300 shares to Exchange B at $49.95
- 200 shares to Exchange A at $50.00 (the remaining best ask)

You receive 500 shares: 300 at $49.95 and 200 at $50.00. The average price is $49.98 instead of $50.00. That is the benefit of Rule 611.

## What trade-throughs the rule does NOT prevent

Rule 611 has exemptions for orders that cannot realistically check all venues:

1. **Closing and opening auctions.** The opening cross and closing auctions on major exchanges operate outside normal rule 611 constraints because their price-setting mechanism is not comparable to continuous trading.

2. **Orders during price improvements.** If an order is routed to an exchange that is offering a price improvement (trading slightly better than the best publicly quoted price), the order may execute there even if another venue shows the same quoted price.

3. **Directed orders.** A broker receiving a specific instruction from a customer to route to a particular exchange is exempt from Rule 611 if the customer explicitly directs the routing.

4. **Certain order types.** Some orders, such as orders routed to market makers in the over-the-counter market or certain bond markets, operate under different rules.

The exemptions preserve the ability of sophisticated traders and institutions to make routing choices, even if those choices are suboptimal, when they direct them explicitly.

## Practical routing mechanics

In reality, brokers rely on routing software and algorithms to comply with Rule 611 automatically. A modern broker's order management system receives your order, checks the stock's current best bid and ask across all venues (the **national best bid and offer**, or NBBO), and routes accordingly.

For passive orders (limit orders that do not immediately execute), the mechanics are simpler. Your limit order sits on the exchange where your broker entered it. If another exchange shows a better price, another trader's order routed there will execute first. No simultaneous routing is required for passive orders; you simply get filled in the order you were entered relative to other orders at that venue.

For aggressive orders (market orders or orders pricing to execute across venues), routing software fragments the order across venues to honor the ISO requirement. This happens in milliseconds.

## Subpenny trades and price improvement

A subtlety: Rule 611 allows trade-throughs if the executing venue is offering a **price improvement** (a price *within* the spread that is better than the best publicly quoted ask or bid, but still inside the NBBO).

For example, if the NBBO is $50.00 bid / $50.05 asked, a dealer could fill you at $50.02 (inside the spread, better than the asking price of $50.05) without triggering Rule 611, even if no other venue is showing $50.02.

Price improvements are especially common in large block trades, where dealers hold inventory and cross the trade internally at favorable prices.

## Exceptions: ATSs and alternative venues

The rule applies to all venues—exchanges, ATSs ([alternative trading systems](/alternative-trading-system/)), dark pools, and broker-dealers acting as [market makers](/market-maker-trading/). However, ATSs and dark pools are permitted to have order types (like "reserve orders" or "block orders") that do not display their full size to the market. These dark orders are outside the NBBO calculation, so Rule 611 cannot force a trade-through of a price that is not publicly available.

This creates a tension: Rule 611 protects publicly visible best prices, but it does not protect hidden sizes in dark pools. A smart order router may see $49.95 on a lit exchange and $49.90 in a dark pool's hidden reserve. The dark pool's reserve order is not part of the NBBO, so routing to the lit exchange at $49.95 does not violate Rule 611, even though a better price was available.

## Enforcement and market impact

The SEC and [FINRA](/finra/) monitor compliance. Large brokers have been fined for Rule 611 violations, typically stemming from routing systems that fail to check all venues or improperly exempt trades.

For retail investors, Rule 611's main impact is reassurance: your limit order is less likely to be filled at a worse price than the national best. For institutional traders, the rule increases execution complexity and cost—fragmented orders, more latency, more counterparties.

High-frequency traders use sophisticated algorithms to exploit the milliseconds between venues, profiting from the friction that Rule 611 creates. The rule protects the best publicly visible price, but it does not prevent arbitrage of those microsecond timing gaps.

## See also

<div class="wiki-seealso">

### Closely related

- [Price Discovery](/price-discovery/) — the process Rule 611 aims to improve
- [Market Maker Trading](/market-maker-trading/) — the counterparties affected by order routing
- [Bid-Ask Spread](/bid-ask-spread/) — the gap Rule 611 helps narrow
- [Alternative Trading System](/alternative-trading-system/) — venues subject to Rule 611
- [Market Order](/market-order/) — the order type most affected by ISO requirements
- [Limit Order](/limit-order/) — treated differently under Rule 611 mechanics

### Wider context

- Regulation NMS — broader framework (note: this is your own slug; link removed to prevent self-reference)
- [Stock Exchange](/stock-exchange/) — venues governed by Rule 611
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of Reg NMS
- [Fragmented Market](/fragmented-market/) — market structure Rule 611 was designed to address

</div>

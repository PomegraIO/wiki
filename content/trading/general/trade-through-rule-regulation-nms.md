---
title: "Trade-Through Rule and Regulation NMS"
description: "The trade-through rule requires brokers to route orders to the venue with the best displayed price; Reg NMS defines when this obligation applies."
keywords:
  - trade through rule
  - regulation nms
  - order routing rules
  - best execution nms
  - trade through exception
image: /svg/trading.svg
---

*The **trade-through rule** is a core mandate under **Regulation NMS** (National Market System): brokers must route customer buy and sell orders to whichever [stock exchange](/stock-exchange/) or trading venue is currently displaying the best price, rather than executing on a less favorable venue for convenience or profit. This rule is meant to ensure that retail and institutional traders get the best available price—the "best bid or offer" (BBO)—across all connected markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade-Through Rule — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A mandatory price-protection rule enforced by the SEC to prevent deliberate order-routing shortcuts.</div>

|   |   |
|---|---|
| **Rule name** | Trade-through Rule (Section 11a-1 of Reg NMS) |
| **Core mandate** | Route to best displayed price; cannot execute at worse price if better price is available |
| **Scope** | U.S. equities (stocks); largely applies to lit venues ([stock exchanges](/stock-exchange/), electronic communication networks) |
| **Enforcer** | [Securities and Exchange Commission](/securities-and-exchange-commission/) and [FINRA](/finra/) (self-regulatory organization) |
| **Exceptions** | Manual orders, small orders, orders in halted stocks, [alternative trading systems](/alternative-trading-system/) with specific procedures |
| **Penalty** | Regulatory fines, restitution to customers, loss of order-routing privileges |

</aside>

## Why the Rule Exists

Before Regulation NMS (adopted in 2005), the U.S. [stock market](/stock-market/) was fragmented across multiple exchanges and trading venues—the [New York Stock Exchange](/new-york-stock-exchange/), the [NASDAQ](/nasdaq/), regional exchanges, and electronic communication networks (ECNs). Each venue displayed its own bids and offers, but there was no single consolidated view.

This fragmentation created an obvious abuse: a [broker](/broker/) could execute a customer's buy order on the [NYSE](/new-york-stock-exchange/) at $50.00 when NASDAQ was displaying $49.95. The broker pocketed the $0.05 spread and the customer never knew a better price existed. This was called a "trade-through."

For retail investors placing orders through brokers, the broker had a fiduciary duty to seek best execution, but in practice that duty was loose. For institutional traders, trade-throughs meant lost savings multiplied across thousands of shares.

Regulation NMS, enacted by the [Securities and Exchange Commission](/securities-and-exchange-commission/), introduced the trade-through rule to eliminate this practice: if a better price is displayed anywhere in the national market system, a broker *cannot* knowingly execute at a worse price.

## How the Rule Works

The mechanics are straightforward:

1. **A broker receives a customer buy order.** The customer wants to buy 1,000 shares of Apple stock.

2. **The broker queries the "market."** Modern systems use a consolidated quote feed (the [Consolidated Tape Association](/price-discovery/) data) that aggregates the best bid and offer prices from all major U.S. exchanges and venues in real-time. The broker sees:
   - NYSE: $150.00 bid, $150.01 ask
   - NASDAQ: $150.02 bid, $150.03 ask
   - ARCA (a regional exchange): $150.01 bid, $150.02 ask

3. **The broker routes to the best ask.** For a buy order, the broker must route to the venue offering the **lowest ask price**. In this case, the NYSE has the best ask at $150.01. The broker sends the order to NYSE.

4. **If the best price has "size" (depth), the broker must respect it.** If the NYSE is showing an ask of $150.01 for 5,000 shares and the customer order is for 1,000 shares, the broker routes the whole order to NYSE.

5. **If the best price is too small to fill the entire order, the broker splits the order.** If NYSE shows $150.01 for only 300 shares, the broker sends 300 to NYSE at $150.01, then routes the remaining 700 shares to the next-best venue (say, ARCA at $150.02).

The rule applies to [limit orders](/limit-order/) (orders with a customer-specified price) and [market orders](/market-order/) (orders willing to accept the current market price).

## Exceptions to the Rule

Not all trades must follow the rule. **Specific exceptions exist:**

- **Manual orders.** If a [broker](/broker/) receives a phone order and manually executes it (rather than using an automated routing system), the trade-through rule does not apply. However, [FINRA](/finra/) rules still require best execution, so the exception is narrow.
- **Small orders.** Orders below a certain size (the "De Minimis" exception) are exempt if they meet specific conditions. The standard is 100 shares or less, though this is indexed to market conditions.
- **[Alternative trading systems](/alternative-trading-system/) (dark pools, wholesalers).** Trades on non-lit venues (where prices are not publicly displayed) are exempt, provided the ATS follows specific procedures and discloses its trading practices.
- **Halted or suspended securities.** If a stock's trading is halted by the exchange, the trade-through rule is suspended.
- **Opening and closing auctions.** Trades in the opening and closing auctions may have different rule applications.

The most contentious exception is **[alternative trading systems](/alternative-trading-system/)**—private trading venues (so-called "dark pools") where buyers and sellers trade without displaying quotes publicly. Brokers can route orders to dark pools even if a better price is displayed on a lit exchange, provided the dark pool has explicit approval to operate as an exception to the rule and discloses its practices.

Criticism of this exception has persisted: dark pools can internalize customer orders (fill them in-house) at prices inside the national best bid/offer without displaying those prices publicly. Defenders argue dark pools provide liquidity and price improvement; critics argue they are "trade-throughs in disguise."

## Implementation and Compliance

Brokers implement the rule through order management systems that:

- Query real-time market data (bid/ask quotes from all venues).
- Rank venues by price and available size.
- Route or split orders automatically.
- Log and audit order destinations to prove compliance.

[FINRA](/finra/) and the [Securities and Exchange Commission](/securities-and-exchange-commission/) conduct routine compliance examinations of brokers' order-routing practices. Brokers must produce evidence that orders were routed to the best price, and if they cannot, they face fines and restitution orders.

High-profile violations have resulted in fines of tens of millions of dollars. For example, if a broker can be shown to have systematically routed orders to a preferred venue despite worse pricing, or to an in-house wholesaler when lit exchanges had better prices, the broker must pay back the difference to customers and face regulatory penalties.

## What the Rule Does Not Require

The rule is about **price**, not speed or other factors. A broker does not have to route to the venue with the fastest execution, the lowest fees, or the most liquidity. It only ensures the best price at the moment of execution.

The rule also does not dictate how a broker manages its relationships with exchanges, wholesalers, or market makers. A broker can have preferred routing relationships and can accept rebates or other inducements—provided the best-price rule is still respected. If a preferred venue does not have the best price, the order goes elsewhere.

## Market Impact and Outcomes

Since Reg NMS took effect, the rule has:

- **Narrowed bid-ask spreads.** Competition for order flow improved pricing. The average [bid-ask spread](/bid-ask-spread/) for liquid stocks tightened from fractions of a cent (historically 1/8 or 1/16 of a dollar) to pennies or sub-pennies. For high-volume stocks, spreads are often 1 cent or less.
- **Increased order fragmentation.** As venues competed for orders, the market fragmented further. A single customer order might now be split across three or four venues. Some argue this has reduced overall market transparency.
- **Driven growth in [alternative trading systems](/alternative-trading-system/) (dark pools).** The exception for dark pools has allowed them to grow, and some observers worry that too much trading now happens off-exchange.

For retail traders and most investors, the rule is invisible but beneficial: prices are tighter and the risk of egregious trade-throughs is eliminated. For institutions and market structure specialists, the rule remains contentious, with ongoing debate about whether it achieves its goals in a fragmented market.

## See also

<div class="wiki-seealso">

### Closely related

- [Stock Exchange](/stock-exchange/) — the venues where prices are displayed and orders are routed
- [Bid-Ask Spread](/bid-ask-spread/) — the price difference the rule aims to minimize
- [Alternative Trading System](/alternative-trading-system/) — the venues exempt from the rule under specific conditions
- [Broker](/broker/) — the intermediary responsible for routing orders in compliance

### Wider context

- [Price Discovery](/price-discovery/) — how rule-based order routing supports efficient pricing
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator that enforces Reg NMS
- [FINRA](/finra/) — the self-regulatory organization that audits broker compliance
- [Market-Maker Trading](/market-maker-trading/) — how liquidity providers interact with the rule

</div>

---
title: "Internal Market"
description: "How brokers execute client orders against their own inventory, bypassing exchanges while meeting price commitments."
keywords:
  - broker internalization
  - proprietary trading
  - order execution
  - price improvement
  - venue competition
image: "/svg/markets.svg"
---

*An **internal market** is a trading system where a broker executes client orders against its own inventory or internal pool rather than routing them to an exchange or third-party market maker. The broker acts as both principal and intermediary, capturing the spread while remaining obligated to respect price protections and execution quality standards.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Internal Market — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and trading venues." />

<div class="wiki-infobox-caption">Broker internalisation shifted market structure from exchange-dominated order routing to retail venues and dark pools.</div>

|   |   |
|---|---|
| **What it is** | Broker-executed trade against firm proprietary inventory |
| **Also called** | Internalization, proprietary matching, in-house execution |
| **When it occurs** | Retail orders, small trades, passive strategies |
| **Price requirement** | Must meet or beat [national best bid/offer](/bid-ask-spread/) |
| **Venue type** | Non-exchange, unlit order flow |
| **Regulatory framework** | SEC Rule 10b-5, Regulation SHO, best execution duty |
| **Key tension** | Broker profit vs. retail investor interest alignment |

</aside>

## The economics of internalisation

Broker internalization fundamentally reorders the market structure that prevailed for decades. Before the 1990s, retail and institutional brokers routed most equity orders to the New York Stock Exchange or other registered exchanges, where their clients competed on a centralized [order book](/price-discovery/). The exchange collected fees, market makers posted liquidity, and order routing was largely a mechanical process.

The profitability of internalization lies in the spread. If a stock trades $100.00 bid / $100.05 ask on the exchange, an internalizing broker can print an order at $100.01 (between the spread) and pocket $0.01 per share. With millions of retail orders daily, this captures meaningful profit. The broker's incentive is subtle but powerful: route customer orders into its own market, improve the price marginally relative to what the exchange quote is, and earn the bid-ask edge without sharing it with exchange specialists or market makers.

This structure emerged in full force after U.S. regulation shifted in the 1990s. The SEC's Order Handling Rules and later Regulation SHO required brokers to honor customer limit orders and maintain price protection, but explicitly permitted them to internalize orders if they offered execution at prices equal to or better than the [national best bid and offer](/bid-ask-spread/). The incentive was immediate: brokers built internal execution engines, matched order flow internally, and became venues themselves.

## Price improvement and the appearance of competition

The appeal of internalization to retail investors sounds straightforward: a better price than what's posted on the exchange. If you place a limit order to sell at $100.02 and the market is $99.98 / $100.05, your broker's internal system can fill you at $100.02 (or sometimes $100.03 or $100.04 if liquidity permits). The customer pockets the benefit.

In practice, price improvement is real but modest. Studies consistently find that retail orders internalized by brokers receive fills 0.01 to 0.03 cents better than the national best bid/offer. For a 100-share retail order, this matters little; for a million-share institutional order, it can mean thousands of dollars. Yet the broker retains enough spread to make the business model work.

This creates an apparent competitive equilibrium: brokers compete to offer price improvement, which benefits the customer. However, the competition is constrained. The largest brokers (Charles Schwab, Interactive Brokers, E*Trade, Fidelity) have developed sophisticated internal matching engines and can access their own pools of internal order flow. Their scale makes price improvement easier to sustain. Smaller brokers or those with less order flow must sell their order flow to wholesalers—payment for order flow—a related but distinct model.

## Order routing obligations and the dual role

A broker internalizing orders faces a legal bind: it must act as both principal (taking risk, earning the spread) and trustee (obligated to execute at best available prices, disclose conflicts, and comply with best execution rules). U.S. securities law, particularly under SEC rules derived from Regulation SHO and the Dodd-Frank Act's mandate for best execution, requires brokers to document their routing logic. If a customer's order can be filled at a better price elsewhere, the broker must route it there or offer the customer the choice.

In practice, brokers must show that their internal price is competitive. They are required to monitor [market-maker](/market-maker-trading/) quotes and exchange depth-of-book data. If the exchange best bid is $100.01 and the broker wants to fill a sell order at $100.02, that's clearly acceptable. But if the market later moves to $100.05 / $100.10 and the broker continues filling orders at $100.02, that violates the duty.

This obligation creates friction. Large brokers and wholesalers invest in real-time market monitoring systems to ensure they are not systematically worse than exchange prices. They set alert thresholds, maintain execution quality metrics, and publish reports on fill prices. Regulatory scrutiny has intensified in recent years, with the SEC questioning whether some brokers' internal prices truly reflect the best available prices or whether they profit by executing slightly worse than they could.

## The rise of retail order flow and market fragmentation

The growth of retail investing—accelerated by zero-commission trading and smartphone apps—has made internalization a dominant fixture of U.S. equity markets. Brokerages like Robinhood, Charles Schwab, and others handle millions of retail orders daily. Most of these orders are internalized or sold to wholesalers rather than routed to exchanges.

This fragmentation has had broad consequences. Exchange volume has shrunk as a percentage of total equity trading. The [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) handle a smaller share of retail order flow than they did in 2000. Dark pools, alternative trading systems, and broker internal systems collectively execute a larger share. This has created a paradox: stock quotes appear instantly on screens worldwide, but the actual execution happens in venues most market participants cannot observe.

The bifurcation has also affected price discovery. Traditional price discovery—the process by which supply and demand determine fair prices—relied on visible order books at centralized exchanges. With order flow fragmented across internal systems and dark pools, price discovery has become murkier. Retail investors may see exchange quotes that do not reflect where most volume is actually trading.

## Conflicts and regulatory debate

The fundamental conflict in internalization is irresolvable: the broker profits from the spread, which means it is incentivized to internalize marginal orders and route only the most difficult ones elsewhere. A broker's internal system may have less liquidity than an exchange, and therefore may struggle to fill large orders competitively. This creates a natural sorting: easy, profitable orders stay internal; hard, low-margin orders go to exchanges or other venues.

Regulators and academics have long debated whether this is efficient or exploitative. Some argue internalization is pro-competitive and benefits customers through price improvement and immediacy. Others contend it fragments the market, reduces transparency, and transfers order flow profits from customers to brokers. The SEC has launched investigations into payment for order flow, retail customer execution quality, and broker conflicts of interest, though a comprehensive fix remains elusive.

The presence of robust retail trading venues (Robinhood, Zero-commission brokers) has sharpened the tension. If a broker offers free commission and price improvement through internalization, it must fund that advantage somehow. Order flow monetization (selling internalized flow to wholesalers, taking the spread on internalized orders, or both) is the answer. Whether this ultimately harms or helps the retail customer depends on whether the prices and execution quality remain competitive with alternatives.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the margin a broker or market maker captures on internal execution
- [Market maker](/market-maker-trading/) — the intermediary role brokers assume when internalizing orders
- [Price discovery](/price-discovery/) — how centralized vs. fragmented venues affect price formation
- [Over-the-counter market](/over-the-counter-market/) — unlit, dealer-intermediated trading in contrast to exchange visibility
- [Payment for order flow](/payment-for-order-flow/) — the related model where brokers sell order flow to wholesalers
- [Broker](/broker/) — the intermediary role and execution obligation
- [Alternative trading system](/alternative-trading-system/) — competing venues for order execution

### Wider context

- [Market maker](/market-maker-trading/) — how market structure depends on liquidity provision
- [Stock exchange](/stock-exchange/) — centralized trading infrastructure that internal markets bypass
- [Securities and exchange commission](/securities-and-exchange-commission/) — regulates best execution duties and internalization standards
- [Locked market](/locked-market/) — anomaly in quote coherence across venues
- [One-sided market](/one-sided-market/) — severe imbalance in bid/ask conditions

</div>

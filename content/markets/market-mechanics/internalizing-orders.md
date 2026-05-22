---
title: "Internalizing Orders"
description: "Broker-dealer matching customer buy and sell orders internally before sending to exchange."
keywords:
  - order internalization
  - broker dealer
  - matching orders
  - market mechanics
---

*When a **broker-dealer internalizes orders**, it matches a customer's buy order against another customer's sell order (or its own inventory) without routing the order to an exchange. The trade occurs inside the broker's system at a negotiated price, and the broker typically captures the [bid-ask spread](/wiki/bid-ask-spread/) as profit. Internalization is common in [alternative trading systems](/wiki/alternative-trading-system/) and is subject to [best execution](/wiki/best-execution/) rules.*

<aside class="wiki-infobox">

| Aspect | Details |
|---|---|
| **Mechanism** | Broker matches buy and sell internally |
| **Price** | At or inside the NBBO (National Best Bid Offer) |
| **Execution speed** | Often faster than exchange routing |
| **Profit model** | Broker captures spread; order-flow revenue |
| **Regulation** | Subject to SEC Regulation SHO, best execution |
| **Primary venues** | Dark pools, ATS, internalization systems |

</aside>

## How order internalization works

A customer places a buy order for 1,000 shares of a stock. Instead of routing it to the [exchange](/wiki/stock-exchange/), the broker checks its own order book or network of clients. If another client has an open sell order for the same quantity at an acceptable price, the broker matches them internally.

Example: Stock XYZ has an [NBBO](/wiki/nbbo/) (best bid-ask across all exchanges) of $50.00 bid / $50.10 ask. A buy order arrives at $50.05. Instead of sending it to the exchange where it might fill at $50.10 (the ask), the broker matches it internally with a sell order at $50.05, capturing the $0.05/share spread ($50 profit on 1,000 shares). Both customers are happy: the buyer paid less than the ask, the seller got more than the bid, and the broker keeps the difference.

## Execution speed and liquidity

Internalization is rapid because it bypasses the exchange's matching engine and the latency of network routing. For a client, an internalized trade executes in microseconds, versus milliseconds for exchange routing. This speed is valuable in fast-moving markets or large block trades where delay risks price slippage.

Internalization also provides liquidity to brokers that can aggregate order flow from many clients. A broker with 10,000 retail clients might see enough buy and sell orders in a given second to match them internally without external execution, then net the flows and hedge remaining imbalances on the exchange or with market makers.

## Best execution and regulatory constraints

SEC [Regulation SHO](/wiki/regulation-sho/) and the [best execution](/wiki/best-execution-rules/) rule require that brokers executing customer orders provide the best reasonably available terms. A broker cannot internalize an order if it would systematically give customers worse execution than the exchange. In theory, if the exchange offers a better price than internal matching, the broker must route to the exchange.

In practice, regulators recognize that internal matching at or near NBBO, plus speed and certainty of execution, may constitute "best execution" even if it's not the absolute best available at that microsecond. The NBBO is a market-wide benchmark, not a guarantee that every broker matches it.

## Payment for order flow and conflicts of interest

Many brokers that internalize orders also receive [payment for order flow](/wiki/payment-for-order-flow/) (PFOF) from [market makers](/wiki/market-makers/) or [dark pools](/wiki/dark-pool/). This creates a conflict: the broker earns more revenue from routing the order to a particular venue (which pays PFOF) than from internalizing it. Regulators require disclosure of PFOF and monitoring to ensure it doesn't incentivize worse execution.

Retail brokers have been criticized for heavy use of PFOF. For example, a broker might internalize only orders it can match internally with low latency, but route the rest to a dark pool partner that pays PFOF. The customer doesn't always know which venue their order went to or whether execution quality suffered.

## Dark pools and internalization

[Dark pools](/wiki/dark-pool-detail/) are private trading venues operated by brokers or exchanges where large blocks trade without pre-trade price transparency. They are a form of order internalization: orders are crossed within the dark pool's system before the trade is reported. Dark pools enable large institutional traders to trade large blocks without the price impact of exchange execution, but critics argue they fragment liquidity and create information asymmetries.

A retail customer typically doesn't trade directly in dark pools; their broker may route their orders to dark pools operated by the broker or partners. Transparency about dark pool routing and execution quality is a key regulatory issue.

## Market impact and institutional context

For institutional investors, order internalization is a double-edged sword. Internalization within a broker's block trading desk can reduce market impact—a $50 million block is less likely to move the market if matched internally than if it hits the exchange's order book. But internalization also reduces exchange transparency and can create information asymmetries if the broker uses order flow information to trade ahead of clients.

## Technological arms race

As exchanges have innovated, broker internalization systems have evolved to compete. Broker internalization engines use algorithms similar to exchange matching engines: order types (limit orders, market orders, pegged orders), priority rules (price-time), and matching logic (FIFO) are mirrored in internal systems. Some brokers have invested heavily in colocation and smart order routing to balance internal matching with external execution to achieve best execution.

## SEC scrutiny and market quality

The SEC periodically scrutinizes broker internalization to ensure it isn't systematically harming execution quality. In 2021, the SEC fined Charles Schwab and E-TRADE for failures in the best execution rule, including inadequate oversight of internalization venues.

## Internalization versus exchange routing

From a trader's perspective, the choice between internalization and exchange routing is largely invisible. Most retail orders are routed through the broker's order management system, which decides where to route based on algorithms designed (in theory) to optimize for execution quality. Institutional traders can often specify preferences: "internalize first, then route to exchange" or "exchange only."

The prevalence of internalization means that a significant portion of equity trading never touches an exchange's public order book, reducing price discovery efficiency in some securities. This is why regulators monitor the share of on-exchange versus off-exchange execution and require post-trade reporting (trade reports appear on the consolidated tape shortly after execution, whether they occurred on-exchange or off).

<div class="wiki-seealso">

### Closely related
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — Broker profit from internalization
- [Best Execution](/wiki/best-execution-rules/) — Regulatory constraint on internalization
- [Dark Pool](/wiki/dark-pool-detail/) — Institutional internalization venue
- [NBBO (National Best Bid Offer)](/wiki/nbbo/) — Price benchmark for internalization
- [Alternative Trading System](/wiki/alternative-trading-system/) — Regulated internalization venue
- [Payment for Order Flow](/wiki/payment-for-order-flow/) — Conflict of interest in routing

### Wider context
- [Market Maker](/wiki/market-makers/) — Alternative execution source
- [Stock Exchange](/wiki/stock-exchange/) — Primary venue for comparison
- [Regulation SHO](/wiki/regulation-sho/) — Regulatory framework
- [Consolidated Tape](/wiki/consolidated-tape/) — Trade reporting system
- [Order Types](/wiki/order-types/) — Internalization logic

</div>

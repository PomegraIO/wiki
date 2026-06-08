---
title: "Order Routing Network"
description: "Electronic infrastructure that receives, directs, and logs client orders from brokers to one or more execution venues in real time."
keywords:
  - order routing
  - order management system
  - execution venue
  - broker infrastructure
  - order routing network
  - best execution
image: "/svg/markets.svg"
---

*An **order routing network** is the telecommunications and computing infrastructure that a [broker](/broker/) uses to receive orders from clients, determine the best execution venue, transmit orders to that venue (and others, if necessary), track fills, and report back to the client. It is the nervous system connecting a brokerage to the stock exchanges and alternative trading venues, handling both the logistics and the compliance burden of order distribution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Routing Network — infrastructure bridging clients and venues</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark representing market venues and trading infrastructure." />

<div class="wiki-infobox-caption">The electronic plumbing of modern brokerage operations.</div>

|   |   |
|---|---|
| **What it is** | Systems and communications links for transmitting orders from brokers to execution venues |
| **Also called** | Order management system (OMS), execution management system (EMS), smart order router |
| **Components** | Client interface, routing engine, venue connectivity, audit trail logging |
| **Participants** | Brokers, exchanges, alternative trading systems, market data vendors |
| **Regulatory role** | Supports best execution and order audit trail compliance |
| **Latency** | Millisecond to microsecond range (depending on distance and infrastructure) |

</aside>

## The broker's role in connecting client to venue

When a retail investor places a stock order on a brokerage app or website, that order does not magically appear on a stock exchange. It must travel through one or more intermediaries—chiefly the broker—before it reaches the [central limit order book](/central-limit-order-book/) or [market maker](/market-maker-trading/) that will actually execute it. The order routing network is the set of systems that brokers operate (or lease from third parties) to manage this flow. It receives the client's order, decides where to send it, executes on behalf of the client, and returns the confirmation.

For a simple domestic stock order, the routing path is often straightforward: the broker receives the order, routes it to the primary exchange (such as the NYSE or Nasdaq) where the stock is listed, waits for a fill, and reports back. But modern markets are complex. A stock might trade on multiple venues simultaneously—the primary listing exchange, multiple alternative trading systems, and various dealer platforms. The routing network must decide not just whether to route to one venue or many, but also in what size, and with what urgency. A small retail order might be routed to a single venue; a large institutional block might be split across several to minimize market impact.

## Smart routing and algorithmic execution

Large brokers and investment banks operate sophisticated routing systems that use real-time market data to decide where to send each order. These smart order routers (SORs) query the [bid-ask spreads](/bid-ask-spread/) and available [depth](/central-limit-order-book/) on multiple venues and choose the venue (or venues) offering the best execution. If the primary exchange has a wide spread but a lit alternative trading system is tighter, the router may send the order to the ATS instead. If multiple venues have similar prices, the router might split the order to increase the chance of swift execution and to avoid concentrating risk in a single venue.

Algorithmic execution systems take this further. A large institutional order—say, a mutual fund or pension plan buying 100,000 shares—is broken into smaller child orders and sent to the market in waves over minutes or hours, using algorithms that adjust pace and venue based on incoming market data. This strategy is designed to minimize market impact and achieve an average price close to the volume-weighted average price (VWAP) of the market during the execution window. The order routing network is the infrastructure that enables this dynamic, data-driven execution.

## Venue connectivity and latency

Each order routing network must maintain connectivity to every venue the broker wants to access. For brokers serving retail clients, this typically means direct electronic links to all major US exchanges (NYSE, Nasdaq, etc.), ECNs (such as BATS or IEX), and perhaps a few key ATSs. For brokers serving institutional clients, the network might also include access to overseas exchanges and bond platforms. Each connection is a distinct telecommunications channel—a fiber-optic link or a leased line from the broker's facility to the venue's data center.

Latency—the delay between when an order is sent and when the venue receives it—matters enormously in electronic markets. A retail order might tolerate a latency of tens of milliseconds; institutional execution algorithms and especially high-frequency traders operate at microsecond scales. Major brokers and exchanges have invested billions in low-latency infrastructure, placing servers in the same data centers as exchange matching engines to shave milliseconds off round-trip time. The order routing network is thus not just a logical system but a physical, geographically distributed infrastructure that competes on speed.

## Compliance and audit trail requirements

Regulators require brokers to maintain detailed audit trails of all orders received, modified, cancelled, and executed. An order routing network must log every event: when the order was received from the client, where it was routed, what fill (if any) was returned, and when the client was notified. These records must be preserved for years and made available to regulators on demand. The Securities and Exchange Commission and the Financial Industry Regulatory Authority (FINRA) have explicit rules governing order record-keeping, and violations can result in substantial fines.

The audit trail serves another critical purpose: demonstrating that the broker has executed orders in accordance with the "best execution" rule. Brokers are obligated to achieve the most favorable overall execution terms reasonably available for each order. By documenting that an order was routed to the venue with the tightest spread or deepest available liquidity at the time, the broker creates a record of having performed due diligence. Should a client dispute a fill price, the audit trail proves the broker's actions. For institutional clients, brokers now commonly show detailed routing reports and execution analysis, so the client can assess whether the broker is genuinely prioritizing their interests.

## Fragmentation and market impact

The proliferation of trading venues has created a fragmentation problem. If the same stock trades on ten different venues, each with its own partial order book, then the true [market price](/price-discovery/) is distributed across all ten rather than concentrated in one. An order routing network must solve this fragmentation by aggregating or comparing prices across venues, a task that grows harder as venue count rises. Some regulatory jurisdictions have responded by requiring brokers to route to the "best bid or offer" across all venues—a regulation that sounds simple but requires brokers to connect to many venues and update their routing logic constantly.

High-frequency traders sometimes exploit fragmentation by identifying price discrepancies (say, a stock trading at $100.01 on one venue and $100.00 on another) and routing orders to profit from the gap. The order routing networks of smaller brokers may not update quickly enough to avoid being adversely selected by these traders. This is an arms race: better-resourced brokers invest in faster networks, and others fall behind, which is why order routing infrastructure is often a key competitive advantage for large firms.

## Broker selection and route selection disclosure

Retail brokers must disclose to their customers which venues they route orders to and how those choices are made. Some brokers explicitly state that they route small retail orders to specific venues in exchange for rebates or kickbacks—a practice that, while disclosed and technically legal, raises questions about conflicts of interest. Institutions often demand that brokers justify their routing logic and regularly audit the brokers' fill quality. The rise of "Robinhood economics" and commission-free retail trading has intensified scrutiny of routing practices, because if brokers are not charging commissions, they must be making money somewhere else—and order routing economics (via venue rebates, payment for order flow, or principal trading) is a major source.

Regulators in the US and Europe have tightened rules around payment for order flow and venue selection transparency. The SEC's Reg SHO and broader Rule 10b-5 framework require that brokers not route to venues that are unsuitable for the client's interests. In Europe, MiFID II requires brokers to execute on venues that offer best execution, taking into account not just price and speed but also the likelihood of execution and settlement. These rules push brokers toward more independent, data-driven routing decisions rather than routing based on rebate offers.

## See also

<div class="wiki-seealso">

### Closely related

- [Broker](/broker/) — the firm operating the order routing network
- [Central limit order book](/central-limit-order-book/) — the destination where orders are routed for execution
- [Alternative trading system](/alternative-trading-system/) — competing venues to which orders may be routed
- [Market maker](/market-maker-trading/) — dealers receiving routed orders and providing execution
- [Best execution](/best-execution/) — the regulatory obligation that routing networks must satisfy
- [Bid-ask spread](/bid-ask-spread/) — a key input to smart routing decisions

### Wider context

- [Stock exchange](/stock-exchange/) — the primary destination for routed orders
- Market impact — unintended price movement caused by routed orders
- [Securities and exchange commission](/securities-and-exchange-commission/) — regulator of routing and audit trail rules
- [Market microstructure](/market-microstructure/) — the academic field studying order routing and execution

</div>
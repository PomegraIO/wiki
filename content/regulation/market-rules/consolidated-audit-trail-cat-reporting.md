---
title: "Consolidated Audit Trail (CAT) Reporting"
description: "SEC's Consolidated Audit Trail system requiring broker-dealers and exchanges to report detailed order and trade lifecycle data for market surveillance."
keywords:
  - consolidated audit trail CAT
  - CAT reporting requirements
  - SEC market surveillance
  - order tracking system
  - broker reporting obligations
image: /svg/regulation.svg
---

*The **Consolidated Audit Trail (CAT)** is an SEC-mandated infrastructure system that captures nearly every order and trade event across U.S. equities and options markets. Broker-dealers and exchanges must report detailed information about order origination, routing, execution, cancellation, and settlement to a central repository. CAT allows regulators to reconstruct the market impact of any trade, identify market manipulation or insider trading, and respond to systemic events in near real-time—giving the SEC unprecedented visibility into market-wide trading behavior.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CAT Reporting — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A unified audit trail enabling SEC surveillance of all trading activity.</div>

|   |   |
|---|---|
| **Mandate** | SEC rule 17 CFR 242.613 (adopted 2012, phased rollout 2016–2018) |
| **Who reports** | All broker-dealers and stock exchanges; options exchanges added 2021 |
| **What gets reported** | Orders, executions, cancellations, modifications, clearing details, routing |
| **Data fields** | Time, symbol, qty, price, account, customer ID, originating venue, execution venue |
| **Time window** | Real-time or within seconds of order event (hard deadline: same-day EOD) |
| **Storage** | CAT Reporter (centralized third-party processor for data ingestion and queries) |
| **Retention** | 6 years (matching SEC record-retention rules) |
| **Access** | SEC, FINRA, exchange surveillance staff; restricted from public |

</aside>

## The Need for a Unified Audit Trail

Before CAT, the SEC relied on fragmented data: each exchange reported its own trades, each broker kept its own order records, and piecing together the full history of a single trade across venues and intermediaries was time-consuming. When a suspected market manipulation or insider-trading case emerged, investigators had to manually request files from dozens of broker-dealers and exchanges, a process that could take weeks.

CAT centralizes this. Every order event—origination, routing, rerouting, partial fills, cancellations—flows into a single system. A regulator can now search by account, trader, symbol, or time window and instantly see the entire order lifecycle across all U.S. venues. This was impossible before 2018 and has become a cornerstone of the SEC's surveillance infrastructure.

## What Gets Reported and When

**Core reportable events:**

1. **Order initiation**: When a customer or proprietary trader submits an order to a broker.
2. **Broker routing**: When the broker sends the order to an exchange or alternative trading system.
3. **Execution**: When the order fills, including partial fills and multiple legs.
4. **Modification**: When an order is amended (price, size, etc.).
5. **Cancellation**: When an order is cancelled before filling.
6. **Clearing and settlement**: Trade details passed to clearinghouses (e.g., DTC for equities, OCC for options).

**Critical data points:**

- Unique order ID (assigned by the originating venue)
- Account number and customer identifier
- Security symbol and CUSIP
- Side (buy or sell), quantity, and price
- Time stamps down to the millisecond
- Venue codes (where it was entered, where it executed)
- Trader identity (for compliance and cross-reference)
- Account owner type (retail, institutional, proprietary, etc.)
- Clearing firm and settlement details

**Reporting timeline:**

Broker-dealers must report to CAT same-day (by end of business), but practically, large brokers push near-real-time feeds. The system processes millions of orders per day and makes data available to the SEC's surveillance team within hours.

## How CAT Supports Market Surveillance

The SEC uses CAT data to:

### Detect Market Manipulation

If a trader or group of traders buys a large quantity of a micro-cap stock moments before a positive announcement, CAT shows the exact timing, account, and routing. Regulators can cross-reference news events, insider filing databases, and social-media chatter to establish a pattern consistent with insider trading or front-running.

### Monitor Layering and Spoofing

Layering (placing and canceling large orders to create false impressions of demand) and spoofing (similar but with intent to profit from the resulting price move) are prosecutable under the Dodd-Frank Act. CAT makes these patterns visible: rapid-fire orders in the same account, high cancellation-to-fill ratios, and orders that disappear moments after a move in the expected direction.

### Enforce Short-Sale Compliance

The SEC uses CAT to audit [Reg SHO locate requirement](/reg-sho-locate-requirement/) compliance. CAT records the designation "short" or "short exempt" on every short-sale order, so regulators can cross-check against broker records of actual locates and identify unlocated short sales.

### Reconstruct Flash Crashes and Circuit-Breaker Events

During market disruptions (like the 2010 flash crash), CAT data lets the SEC trace precisely which orders triggered which price moves, which venues experienced congestion, and where the cascade began. This information informs policy responses and identifies bad actors who deliberately triggered instability.

### Investigate Broker Misconduct

If a broker is accused of front-running its customers (trading ahead of customer orders), CAT provides a comprehensive record: timestamps showing the broker's own trades relative to customer orders, routing patterns, and profit metrics that can prove or disprove the allegation.

## Phased Rollout and Coverage

CAT deployment occurred in phases:

- **Phase 1 (2016)**: Large brokers (size-tier 1) began reporting.
- **Phase 2 (2017–2018)**: Mid-sized and smaller brokers added; exchanges expanded coverage.
- **Options coverage (2021)**: Options exchanges and brokers added options-trade reporting.

Not all securities are equally covered. CAT is mandatory for:

- All U.S. equities (stocks) and listed options.
- Over-the-counter equities traded on alternative systems (ATS).
- Municipal and corporate bonds (added in phases; still expanding).

Foreign equities and some exotic derivatives are not fully integrated, though the SEC is pushing for broader coverage.

## Burden and Compliance Costs

CAT compliance is not free. Brokers and exchanges incur significant IT, operations, and legal costs to:

- Redesign order-management systems to capture and timestamp every event.
- Integrate with the CAT Reporter infrastructure.
- Map internal account and customer identifiers to regulatory standards.
- Build validation and audit procedures to ensure data accuracy.

Large brokers budgeted tens of millions of dollars for CAT systems. Smaller firms faced proportionally higher per-trade costs, creating a compliance disparity that sparked debate about fair cost allocation.

## Data Quality and False Positives

One challenge: CAT is only as good as the data fed into it. Errors in time stamping, account coding, or order routing create noise in surveillance. The SEC and FINRA have had to build extensive data-cleaning and validation logic to filter out false signals. A single missing field or misclassified order type can obscure a real manipulation case or generate false accusations.

## Privacy and Access Controls

CAT data is highly sensitive: it reveals customer order patterns, account sizes, and trading strategies. Access is restricted:

- SEC enforcement, examination, and surveillance teams can query CAT.
- Exchange surveillance operations can access data for their own markets.
- FINRA has limited access for disciplinary investigations.
- The data is not public; market participants cannot request their own CAT information directly from the SEC.

This creates a trust issue: brokers and traders must accept that their order and trade data is subject to surveillance, but they cannot audit the accuracy of what is stored about them.

## Relationship to Market Integrity Rules

CAT feeds into enforcement of other regulations:

- **Clearly Erroneous Trade Cancellation**: CAT timestamps help exchanges verify the NBBO at the moment of trade.
- **Reg SHO**: CAT captures short-sale designations, used to police naked short selling.
- **Dodd-Frank Manipulation Rules**: layering, spoofing, and other manipulations are detected via CAT pattern analysis.
- **Market Maker Quoting Obligations**: CAT records help FINRA monitor continuous quoting compliance.

## See also

<div class="wiki-seealso">

### Closely related

- [Clearly Erroneous Trade Cancellation](/clearly-erroneous-trade-cancellation/) — CAT data used to verify NBBO deviations
- [Reg SHO Locate Requirement](/reg-sho-locate-requirement/) — CAT captures short-sale designations and routing
- [Market Maker Quoting Obligations](/market-maker-quoting-obligations/) — CAT monitors quote continuity and size
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the CAT mandating authority
- [Price Discovery](/price-discovery/) — CAT surveillance supports fair price formation

### Wider context

- [Stock Exchange](/stock-exchange/) — primary CAT reporting venues
- [Broker](/broker/) — responsible for reporting order and trade details
- [Alternative Trading System](/alternative-trading-system/) — also subject to CAT rules
- Market Manipulation — behavior detected and prevented through CAT
- [Dodd-Frank Act](/dodd-frank-act/) — legislation that strengthened CAT mandate

</div>

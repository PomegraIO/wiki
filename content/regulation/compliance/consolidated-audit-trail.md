---
title: "Consolidated Audit Trail"
description: "SEC system tracking market transactions across venues for surveillance, enforcement, and post-trade audit."
keywords:
  - consolidated audit trail
  - CAT
  - market surveillance
  - trade reporting
  - regulatory compliance
---

*The **Consolidated Audit Trail** (CAT) is a U.S. Securities and Exchange Commission (SEC) mandate requiring brokers, exchanges, and other market participants to submit standardized transaction data into a unified database. Launched in December 2021, CAT aims to create a complete, chronological record of every equity and options trade—from order placement to execution to cancellation—enabling the SEC to reconstruct market events, detect [market manipulation](/wiki/market-surveillance/), and enforce insider trading rules.*

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| **Regulator** | U.S. Securities and Exchange Commission (SEC) |
| **Launch date** | December 2021 (phased) |
| **Scope** | All U.S. equities and listed options |
| **Data captured** | Order-level (not just executions) |
| **Participants** | Brokers, market makers, exchanges, SROs |
| **Key ID** | OATS ID (Order Audit Trail System) predecessor) |

</aside>

## The pre-CAT landscape and need for consolidation

Before CAT, U.S. market surveillance was fragmented. Exchanges reported trades through the [consolidated tape](/wiki/consolidated-tape/), but order-level data—when a trader placed a limit order, when it was modified, when it was cancelled—lived on separate exchange systems. Brokers kept their own records. The SEC and [FINRA](/wiki/finra/) had to piece together market events by subpoenaing multiple parties and reconciling timestamps, order IDs, and execution records. The process was slow and error-prone.

The fragmentation became painfully clear during the 2010 [flash crash](/wiki/flash-crash-2010/). The SEC took weeks to reconstruct what happened because order data was scattered across venues. CAT was designed to solve this: one central database, standardized format, same timestamp protocol, all orders and executions recorded at the point of entry.

## What CAT captures and how it works

CAT mandates submission of order information at the earliest point: when a customer places an order with a broker, not just when it executes. Participants must report the account holder's identity (or a anonymized identifier if retail), the order price, size, time, instrument, side (buy/sell), order type, and any modifications or cancellations. When the order executes (fully or partially), execution details are reported: execution price, size, time, and counterparty code.

The SEC chose a phased rollout. Reporting began with large brokers in 2021, widening to all brokers by 2024. The identifier scheme uses a "CAT ID"—an opaque reference number assigned to each customer account and market participant, protecting customer privacy while allowing the SEC to follow order flow through the system.

Participants submit data through one of several approved CAT Reporting Processors—third-party vendors who validate, format, and upload the data to the central repository. This reduces load on the SEC's systems and distributes reporting infrastructure across the industry.

## Surveillance and pattern detection

With full order-level data, the SEC's algorithms can detect patterns impossible to spot before. A classic example: layering or spoofing. A trader places a large sell order (not intending to execute it), watches the market move on the perceived supply, then cancels the order. With CAT, the SEC can see the order lifetime, cancellation pattern, and correlation with subsequent executions in the trader's account. Sophisticated detection algorithms flag suspicious patterns: orders modified before execution, concentrations of cancellations at key price levels, coordinated activity across multiple accounts.

CAT also enables faster response to real-time market stress. If [circuit breakers](/wiki/circuit-breaker/) trigger or volatility spikes, the SEC can quickly access CAT data to understand whether market makers were present, who was exiting, and what order flow looked like. This was valuable during the 2020 March volatility spike and the 2021 meme-stock rallies.

## Challenges and operational complexity

Reporting to CAT is expensive. Brokers and market makers had to build new reporting pipelines, integrate CAT messaging standards, and maintain data quality. Smaller firms faced disproportionate cost burden. Some smaller brokers outsourced reporting to the CAT Reporting Processors rather than build in-house systems. The industry estimated compliance costs at $200+ million to build systems and ongoing millions annually to maintain them.

Data quality became an early problem. Participants submitted conflicting timestamps, malformed identifiers, and incomplete records. The SEC and SROs spent 2022–2023 validating and reconciling. Some data remained unusable. The SEC has published guidance on common errors (incorrect account identifiers, missing executing venue codes) and imposed penalties for gross violations.

Cross-venue order tracking introduced technical challenges. An order placed at a broker might route to multiple exchanges before executing; CAT requires tracking across all venues. If one venue is slow to report, the consolidated picture is incomplete. Latency and data aggregation are ongoing sources of friction.

## Privacy and market-structure implications

CAT's use of anonymized customer identifiers raised privacy concerns among investors. While names are not published, the data contains enough detail (account size, trading pattern, order submission times) to potentially re-identify large traders. The SEC has committed to safeguarding CAT data; access is limited to authorized staff and law enforcement under subpoena.

From a market-structure perspective, CAT empowers the SEC to enforce rules far more precisely. Patterns that were once invisible—cancellation rates by market maker, order-placement timing relative to volatility spikes, execution quality correlation with order size—are now measurable. Some argue this drives more rigorous market making and execution quality; others worry it chills legitimate market making and imposes compliance costs that disadvantage smaller participants.

## Future expansion and integration

The SEC has proposed expanding CAT to fixed-income markets (corporate bonds, Treasury securities). Government bonds see $600+ billion in daily trading volume, but audit trails are even more fragmented than equities. Building CAT infrastructure for bonds would be a multi-year project but would provide unprecedented [market surveillance](/wiki/market-surveillance/) capability for the Fed and SEC to monitor financial stability.

<div class="wiki-seealso">

### Closely related
- [Market Surveillance](/wiki/market-surveillance/) — The enforcement use case driving CAT
- [Consolidated Tape](/wiki/consolidated-tape/) — Real-time trade reporting that CAT supplements
- [FINRA](/wiki/finra/) — Co-regulator with enforcement roles using CAT
- [Trade Reporting](/wiki/trade-reporting/) — Broader reporting framework for OTC trades

### Wider context
- [Flash Crash 2010](/wiki/flash-crash-2010/) — Catalyst for CAT regulatory focus
- [Best Execution](/wiki/best-execution/) — Broker obligation enforceable via CAT analysis
- [Securities and Exchange Commission](/wiki/securities-and-exchange-commission/) — Principal regulator
- [Insider Trading Definition](/wiki/insider-trading-definition/) — Enforcement area enhanced by CAT

</div>

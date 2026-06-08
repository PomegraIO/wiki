---
title: "Straight-Through Processing"
description: "Automated end-to-end workflow that moves a trade from execution through confirmation, settlement, and reporting without manual re-keying or human intervention."
keywords:
  - straight-through processing
  - stp
  - trade automation
  - settlement automation
  - trade lifecycle
image: "/svg/institutions.svg"
---

*Straight-through processing, or **STP**, is the complete automation of a trade's lifecycle from initial execution through to final settlement and regulatory reporting. Rather than passing confirmations, instructions, and position updates between systems manually—a workflow prone to re-entry errors, delays, and reconciliation breaks—STP pipelines move electronic messages directly from a trading platform to settlement systems to custodians to regulators. A single trade data file, confirmed once at execution, flows uninterrupted to all downstream parties.*

<div class="wiki-hatnote">

For the institutions that operate this infrastructure, see Clearinghouses. For what happens when the pipeline breaks, see [Failed settlement](/failed-settlement/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Straight-Through Processing — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions and regulatory frameworks." />

<div class="wiki-infobox-caption">Automation that eliminates manual re-keying, cuts settlement timelines, and reduces operational risk.</div>

|   |   |
|---|---|
| **What it is** | End-to-end electronic automation of trade lifecycle from execution to settlement |
| **Scope** | Trade matching, confirmation, netting, settlement instruction, cash/collateral movement, reporting |
| **Benefit** | Speed, accuracy, cost reduction, shorter settlement cycles (e.g., T+0 or T+1 vs. T+3) |
| **Requirement** | Standardised message formats (FIX, ISO 20022), consistent data definitions, integrated systems |
| **Manual exceptions** | Rare; typically only bespoke or failed trades requiring human intervention |
| **Regulatory support** | Dodd-Frank, EMIR, and most post-2008 rules mandate STP where feasible |

</aside>

## The problem STP solves

Before widespread automation, a single trade could involve dozens of handoffs. A trader on an exchange floor might shout a buy order to a specialist, who matches it with a seller. A runner scribbles the price and quantity on a ticket. The ticket moves to a "cage" clerk, who types it into an internal settlement system. The clerk checks that the buyer and seller agree on all terms. A separate team produces a paper confirmation sent to the counterparty. The counterparty's operations team receives it, re-enters the data into their own system, compares it to their internal record, and sends back an acknowledgement. Meanwhile, a back-office team is separately preparing settlement instructions to a custodian.

Every handoff is a point of failure. A clerk might misread a ticket. The buyer's system and seller's system might disagree on the quantity or settlement date. A confirmation might be lost in the mail. Reconciling discrepancies could take days. In high-volume markets, operational backlogs piled up, creating "fails" and collateral disputes.

STP eliminates these handoffs. Once a trade is executed, the electronic record is final. That record flows automatically to clearing, to settlement, to custody, to reporting. No re-keying. No reconciliation. No delays.

## The technical architecture

At the core of STP is **standardised messaging**. The financial industry has adopted protocols like **FIX** (Financial Information Exchange) for trading, and increasingly **ISO 20022** for settlement and reporting. A trade executed on one system is encoded in a standard message format that any other system can parse and act upon.

The workflow typically looks like this:

1. **Trade execution:** A buyer and seller agree on a transaction on an exchange or electronic communication network. The trade is timestamped and electronically recorded.

2. **Automatic matching and confirmation:** The exchange's matching engine confirms that both sides agree on the core terms (security, quantity, price, settlement date). An electronic confirmation message is auto-generated and sent to both parties' systems.

3. **Netting and clearing:** If the trade is subject to clearing, it is sent to the clearinghouse, which novates it and nets it against other trades from the same clearing member on the same settlement date. The CCP sends back a clearing confirmation.

4. **Settlement instruction:** The buyer's and seller's settlement systems automatically generate instructions to move cash and securities. These instructions are sent electronically to custodians, depositories, and payment systems.

5. **Final settlement:** Custodians and central securities depositories (such as Euroclear or the Depository Trust Company) receive the instructions, verify collateral and entitlements, and execute the transfer of securities and cash.

6. **Regulatory reporting:** Trade details are simultaneously sent to trade repositories and regulators, who receive standardised machine-readable data that can be aggregated without manual consolidation.

Each step happens in near-real-time. If a discrepancy arises—say, the buyer's system shows T+1 settlement but the seller's shows T+2—most modern STP systems flag it immediately as an exception rather than allowing it to fester until settlement date.

## Speed, cost, and risk reduction

STP has been a driver of shorter settlement cycles. When settlement was T+3 or T+5, the pipeline took days and manual exception handling was the norm. As markets automated, settlement compressed to T+2, then T+1. Some markets now operate on same-day (T+0) settlement for certain asset classes.

Shorter cycles shrink [settlement risk](/failed-settlement/). If a counterparty fails one day after trade rather than five days after, the exposure window is compressed and less interest accrues. For a buyer financing a purchase with an overnight repo, shorter settlement reduces financing costs.

Cost reduction is equally significant. Manual processing of a single trade—confirmation, reconciliation, settlement instruction—can cost a financial institution between USD 10 and 50 per trade. At scale, across millions of daily trades, that is billions in annual operational expense. STP reduces per-trade cost to a fraction of a dollar or eliminates it entirely.

Risk reduction comes from fewer errors and faster detection of problems. A manual reconciliation process might not catch a settlement discrepancy for days. An automated STP pipeline flags it within minutes and can route it to a small team of exceptions specialists who handle only genuinely ambiguous cases.

## Barriers and remaining gaps

Despite regulatory mandates and economic incentives, STP adoption is incomplete. A few barriers persist:

**Bespoke and OTC derivatives:** A highly customised swap between two banks has unique features that do not fit standardised message templates. Such trades still rely on manual confirmation and settlement, though clearing mandates have pushed some OTC trades toward standardised termsheets that enable clearing and partial automation.

**Legacy system integration:** Older financial institutions have invested heavily in decades-old settlement systems. Upgrading or replacing them is expensive and risky. A small regional bank might lack the capital to fully automate its back office, creating pockets of manual processing.

**Cross-border complexity:** A trade involving a US buyer, European seller, and Japanese custodian must navigate three different regulatory regimes, settlement timelines, and holiday calendars. Messages must be translated and reconciled at each border.

**Emerging markets:** Markets with less developed infrastructure (smaller CCPs, fewer integrated custodians, slower messaging networks) often cannot achieve end-to-end STP.

**Human exceptions:** Even the best STP system has a tail of exceptions—failed authentication, missing data fields, identity mismatches. These require human judgment and phone calls to resolve.

## Regulatory push and post-2008 momentum

The [Dodd-Frank Act](/dodd-frank-act/) and EMIR explicitly mandate STP for eligible derivatives and securities. Regulators recognised that operational breakdowns and settlement delays were amplifying systemic risk during the 2008 crisis. By forcing automation, regulators aimed to compress settlement cycles and reduce the number of concurrent exposures in the system.

Central banks, including the Federal Reserve and the European Central Bank, have also invested in their own STP-enabling infrastructure. Real-Time Gross Settlement systems (RTGS) and payments systems that support instant settlement have grown more prevalent, allowing trades to settle within seconds rather than hours or days.

The trend toward T+0 and same-day settlement, while still in pilot phases in most markets, depends entirely on STP maturity. Without full end-to-end automation, same-day settlement creates unacceptable operational risk.

## See also

<div class="wiki-seealso">

### Closely related

- Clearinghouses — the institutions operating STP infrastructure for cleared trades
- [Failed settlement](/failed-settlement/) — the operational failures STP is designed to prevent
- [Clearing mandate](/clearing-mandate-emir-dodd-frank/) — regulatory requirement driving STP adoption
- [Trade compression](/trade-compression/) — automated netting that depends on STP data quality
- [Over-the-counter market](/over-the-counter-market/) — bilateral market where STP adoption lags

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — US legislation mandating STP for eligible trades
- [Securities and exchange commission](/securities-and-exchange-commission/) — US regulator overseeing STP standards
- [Counterparty risk](/counterparty-risk/) — the credit exposure compressed by faster settlement
- [Systemic risk](/systemic-risk/) — the interconnection risk reduced by automated processing

</div>

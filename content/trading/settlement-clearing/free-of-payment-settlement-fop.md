---
title: "Free of Payment Settlement (FoP): When and Why It Is Used"
description: "Free of payment settlement (FoP) transfers securities without simultaneous cash payment, used for reorganizations, settlement errors, and system delays. Key risks and mechanics explained."
keywords:
  - free of payment settlement
  - fop settlement
  - securities transfer without cash
  - settlement procedures
  - clearing mechanics
image: "/svg/trading.svg"
---

*A **free of payment settlement** moves securities from one party to another without the cash leg arriving at the same time. FoP settles when reorganizations, technical failures, or market conventions require asset transfers to proceed ahead of payment, leaving both sides exposed to timing risk.*

<div class="wiki-hatnote">

This article covers FoP as a settlement mechanism and its role in standard market operations. It does not address the separate use of FoP as a financing technique in repurchase agreements or other derivative strategies.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FoP Settlement — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Securities move first; cash follows later or not at all in FoP settlement.</div>

|   |   |
|---|---|
| **Definition** | Transfer of securities without simultaneous cash payment |
| **Primary use cases** | Corporate actions, settlement fails, market emergencies |
| **Cash timing** | Usually within 1–3 business days; may be days later or indefinite |
| **Principal risk** | Receiver holds securities; payer holds cash. Either side can default before the other leg clears. |
| **Market frequency** | Routine for [corporate-action-settlement-complications](/corporate-action-settlement-complications/); uncommon for spot trades |
| **Settlement finality** | Securities transfer is final; cash transfer is pending |

</aside>

## How FoP Settlement Works

In a standard **free of payment settlement**, the securities leg of a trade settles in full on the agreed date, but the cash leg does not. The seller transfers shares to the buyer through the clearing system; simultaneously, the cash amount that the buyer owes sits in suspension. The buyer now owns the securities but has not yet paid. The seller has paid out securities but has not yet received the cash.

This decoupling of the two legs is the defining feature of FoP. In a [repurchase-agreement](/repurchase-agreement/), which can also use FoP mechanics, the receiver (borrower of securities) deliberately delays payment to finance a position. But in most market FoP transactions, the delay is not intentional financing—it is a operational necessity or a temporary bridge.

The cash typically settles within one to three business days. In some cases (particularly around [corporate-action-settlement-complications](/corporate-action-settlement-complications/)), the cash may never settle at all in the original trade; instead, the securities are adjusted in quantity or the cash is replaced by alternative consideration (new shares, warrants, or cash from a different source).

## When FoP Is Used: The Main Scenarios

### Corporate Reorganizations

The most routine use of FoP settlement is during corporate mergers, acquisitions, and restructurings. When a company announces a merger in which shares of Target Corp will be exchanged for shares of Acquirer Inc., the exchange ratio is fixed on announcement, but the merger does not close for weeks or months. 

Shareholders who own Target shares before the merger must still hold them and receive them in settlement when the merger closes. However, the cash value that the acquirer will pay out—whether in the form of new shares, a dividend, a rights payment, or a cash distribution—may not be finalized in amount or timing until legal and regulatory approvals are secured.

The depository and clearing system will often move Target shares into FoP status: they settle without cash, held in segregated accounts or subject to restrictions, until the final terms and settlement amount for the reorganization are confirmed. The cash leg then settles once the merger legally completes.

### Settlement Failures and Contingency

When a trade cannot settle on its scheduled [settlement-date](/settlement-risk-vs-counterparty-risk/) because one counterparty or a critical system is unavailable, market procedures may allow settlement of the securities leg in FoP to prevent a broader disruption. This keeps the books moving and buys time for the cash leg to clear when the system comes back online.

Similarly, if a cash payment system (such as a central bank wire or [FEDWIRE](/federal-reserve/)) is temporarily unavailable, a clearinghouse may accept the securities delivery in FoP and hold the cash obligation until the payment system recovers.

### Market Emergencies and Regulatory Relief

During extreme market stress—liquidity crises, cyberattacks, or major operational failures—regulators and clearinghouses may invoke emergency rules allowing FoP settlement to keep critical securities transactions moving. The priority is to avoid cascading defaults and maintain market confidence. The cash leg is handled in a secondary pass once normal operations resume.

## The Mechanics of Cash Settlement After FoP

Once securities settle in FoP, the cash leg must close the position. The typical sequence is:

1. **T+0 or T+1**: Securities leg settles free of payment. Seller's account is debited securities; buyer's account is credited securities.
2. **T+0 to T+3 (or longer)**: Cash leg settles. Buyer pays the agreed amount (or the revised amount, if a corporate action altered it) to the seller.
3. **Final status**: Both legs complete. The trade is fully settled.

During the gap, neither party has a perfect claim. The receiver of securities may be unable to sell them (if restricted or pending confirmation) and must hold them at market risk. The receiver of cash obligations may have already booked the trade as revenue and must manage the credit exposure if the payer defaults.

## The Central Risk: Counterparty Default During the Gap

The defining hazard of **free of payment settlement** is [settlement-risk-vs-counterparty-risk](/settlement-risk-vs-counterparty-risk/). While both legs are still pending, each side is exposed to the other's solvency.

If the buyer receives securities but then fails before paying cash, the seller has handed over an asset in exchange for an unsecured claim on an insolvent counterparty. The seller may recover only a fraction of the cash owed, and only after an insolvency proceeding.

If the seller receives payment instructions but the cash never arrives, the buyer sits with securities that may decline in value or become restricted. The buyer has funded the seller's operations for days or weeks without compensation.

To manage this risk, counterparties often require collateral or letter-of-credit guarantees during the FoP window, or they may use a trade bank or [custodian](/custodian/) as an intermediary to backstop both legs. Many institutional investors simply refuse to settle FoP unless it is a [corporate-action-settlement-complications](/corporate-action-settlement-complications/) mandated by the issuer or a regulatory emergency.

## FoP and the Move Toward Shorter Settlement Cycles

As markets have moved toward T+1 and [T+0 settlement cycles](/settlement-risk-vs-counterparty-risk/), the window for FoP gaps has compressed. T+0 settlement (settlement same day) eliminates FoP entirely for standard trades, because both legs must clear before the close of the same business day.

However, even in T+1 environments, FoP remains necessary for:
- Corporate actions, where the legal or regulatory timeline does not align with the settlement cycle.
- International trades involving [cross-border](/currency-risk/) or [multi-currency](/currency-volatility/) settlements, where different time zones and payment systems cause unavoidable delays.
- Reconstruction of failed trades, where only partial settlement can be reversed and the two legs must be unwound in separate steps.

## Regulatory Treatment and Disclosure

Regulators distinguish between FoP settlement that is planned (routine corporate action settlement) and FoP that is unplanned (emergency or failure-driven). Planned FoP is disclosed in [prospectuses](/fund-prospectus/) and corporate action notices; investors receive advance warning and can plan their cash positions accordingly.

Unplanned FoP, or FoP windows that extend longer than expected, must be reported to compliance and risk officers. Under [Dodd-Frank](/dodd-frank-act/) and equivalent global rules, certain firms must monitor and limit their FoP settlement exposure to reduce systemic [settlement-risk-vs-counterparty-risk](/settlement-risk-vs-counterparty-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Settlement risk vs counterparty risk](/settlement-risk-vs-counterparty-risk/) — How timing of settlement creates distinct credit exposures
- [Corporate action settlement complications](/corporate-action-settlement-complications/) — Stock splits and dividends that disrupt normal settlement flow
- [Gross vs net settlement systems](/gross-vs-net-settlement-systems/) — RTGS vs deferred netting and their impact on FoP frequency
- Clearing — The infrastructure that processes FoP transactions
- [Custody and safekeeping](/custodian/) — How third parties manage securities during FoP gaps
- [Repurchase agreement](/repurchase-agreement/) — Another context where FoP mechanics are intentionally used

### Wider context

- [Counterparty risk](/counterparty-risk/) — Credit risk from any bilateral obligation
- [Basis risk](/basis-risk/) — Timing mismatch between related securities or cash flows
- [Liquidity risk](/liquidity-risk/) — The inability to move assets or settle quickly
- [Interest rate risk](/interest-rate-risk/) — How delays in settlement can cost borrowers and lenders

</div>

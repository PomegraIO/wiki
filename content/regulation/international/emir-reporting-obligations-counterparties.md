---
title: "EMIR Reporting Obligations for Counterparties"
description: "Which entities must report OTC derivatives under EMIR, what data fields are required, and how the two-sided reporting model prevents duplicates."
keywords:
  - emir reporting obligations
  - otc derivatives reporting
  - emir counterparty reporting
  - trade reporting
  - emir derivatives
  - regulatory reporting
---

*Counterparty reporting under **EMIR** requires most entities trading OTC derivatives to file trade details to a trade repository within one business day of execution.* The regulation applies asymmetrically—financial firms have stricter obligations than non-financial companies—yet relies on a two-sided reporting model designed so both sides report the same trade, preventing the buy and sell sides from cancelling each other in aggregate.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">EMIR Reporting — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One half of each OTC trade must report; both halves typically do, creating a dual-reporting safety net.</div>

|   |   |
|---|---|
| **Full name** | European Market Infrastructure Regulation |
| **Who must report** | EU counterparties; non-EU firms trading with EU entities |
| **Reporting timeline** | One business day from execution |
| **Who files** | Both counterparties normally; waiver possible for uncleared swaps |
| **Key fields** | Product type, notional, maturity, settlement date, counterparty ID, pricing terms |
| **Venue** | Authorized trade repositories |

</aside>

## The Two-Sided Reporting Model

EMIR's core architecture treats each counterparty as an independent reporter. When Bank A and Bank B execute a swap, Bank A files a report and Bank B files the same report independently. This redundancy serves a regulatory purpose: a trade repository receives two records, allowing supervisors to cross-check data quality and catch omissions or deliberate misreporting by either party.

The downside is operational: both banks invest in reporting infrastructure, both incur compliance costs, and both must reconcile their versions of the trade afterward. That reconciliation is a contractual obligation between counterparties, separate from the regulatory report itself.

## Who Must Report

**Financial counterparties** (investment firms, credit institutions, insurance companies, pension funds) face mandatory reporting with no exemptions. **Non-financial counterparties** (corporates using derivatives to hedge genuine business exposure) enjoy a threshold: they report only if their OTC derivatives positions, measured in [notional](/forward-contract/) across all counterparties, exceed €8 billion in aggregate at quarter-end. Once a company exceeds the threshold, it stays a reporter until notional falls below €500 million—a hysteresis designed to prevent frequent in-and-out status changes.

The EMIR framework also applies to **non-EU counterparties** that trade with EU entities; those non-EU firms must report, or their EU counterparties report on their behalf (often with delegated authority clauses embedded in the trade agreement).

## Mandatory Fields and Data Standards

Trade repositories publish a detailed reporting template covering:

- **Identification**: unique swap identifier (USID, now migrating to ISINs and instrument identifiers)
- **Counterparty detail**: Legal Entity Identifier (LEI) for both sides
- **Product and terms**: asset class, instrument type, underlying (if any), strike, notional amount
- **Pricing**: fixed rate, floating index, spread, fee
- **Dates**: execution, settlement, maturity, next coupon payment
- **Modifications**: any amendment to a previously reported trade
- **Collateral**: initial and variation margin posted

Central counterparties (CCPs) that clear swaps are also registered repositories, so cleared trades flow directly into a CCP's repository. For uncleared trades between bilateral counterparties, both parties must have access to an authorized trade repository.

## Timing and Responsibility

Reporting must occur no later than the end of the first business day following execution. A corporate hedging with its bank executes a trade at 3 p.m. on Tuesday; the report is due by end of business Wednesday. Delays trigger sanctions.

**Responsibility** splits by execution venue: trades on regulated exchanges or systematic internalizers may be reported by the venue itself on behalf of parties. Trades executed OTC (phone, electronic communication) are the responsibility of the counterparties. Many firms delegate the actual reporting to third-party service bureaus or to their custodian or settlement agent, but legal liability remains with the counterparty.

## Waivers and Exemptions

Non-financial counterparties below the €8 billion threshold are exempt. Small pension funds (less than €500 million in assets) are exempted from reporting. The EU also permits **waiver arrangements** for certain uncleared derivatives: if two counterparties agree that only one of them will report (provided the other confirms it), reporting can be single-sided. This waiver must be formalized in writing and submitted to the trade repository. In practice, waivers are rare; most trades are dual-reported.

## Settlement and Data Corrections

Once a trade settles (cash or physical delivery), it remains in the trade repository's historical record. If a trade is novated (transferred to a new counterparty), a novation event is reported. If a trade is amended (notional increased, maturity extended), an amendment report is filed, linked to the original trade's identifier.

Errors in initial reports must be corrected through amendment reports within five business days for most fields, longer for others. Failure to correct material errors draws supervisory action.

## Regulatory Oversight and Cross-Border Coordination

The [Securities and Exchange Commission](/securities-and-exchange-commission/) (SEC) in the United States runs a parallel system for US swaps. ESMA (the EU's market authority) oversees EU trade repositories and sets standards jointly with the [Federal Reserve](/federal-reserve/). Non-EU counterparties often must report to both ESMA and the SEC, depending on which markets and counterparties they trade with—a jurisdictional burden that has prompted some firms to reduce OTC [derivatives](/derivatives-hedging/) exposure in favor of listed [futures contracts](/futures-contract/).

## See also

<div class="wiki-seealso">

### Closely related

- [Over-the-counter market](/over-the-counter-market/) — Bilateral trading outside exchanges, the venue EMIR regulates
- [Counterparty risk](/counterparty-risk/) — The credit exposure between parties that EMIR transparency aims to reduce
- [Central counterparty](/central-bank/) — CCPs clear and net trades, reducing bilateral counterparty load
- [Securitization](/securitization/) — Financial engineering EMIR applies to when swaps are embedded in structured products
- [Credit default swap](/credit-default-swap/) — Specific OTC instrument type subject to full EMIR reporting

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — US regulatory counterpart to EMIR
- [Forward contract](/forward-contract/) — Non-standard derivatives often exempt from reporting if not exchange-traded
- [Swap](/swap/) — Generic term for the contracts EMIR targets
- [Derivative](/derivatives-hedging/) — Broader asset class

</div>

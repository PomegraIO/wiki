---
title: "Clearing Mandate"
description: "Post-2008 regulatory requirement that standardised OTC derivatives be cleared through a central counterparty rather than settled bilaterally between traders."
keywords:
  - clearing mandate
  - dodd-frank
  - emir
  - central counterparty
  - otc derivatives
  - financial regulation
image: "/svg/institutions.svg"
---

*A **clearing mandate** is a regulatory requirement that trades in standardised over-the-counter derivatives must be cleared through a central counterparty rather than settled bilaterally between the original trading partners. Introduced in the United States by the Dodd-Frank Act and in Europe by EMIR, the mandate aims to reduce systemic risk and improve transparency after the 2008 financial crisis exposed the dangers of opaque, interconnected bilateral settlement networks.*

<div class="wiki-hatnote">

For the foundational infrastructure, see Central counterparty. For the broader post-crisis rulebook, see [Dodd-Frank Act](/dodd-frank-act/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing Mandate — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions and regulatory frameworks." />

<div class="wiki-infobox-caption">A regulatory forcing function that routes standardised derivatives through centralised risk infrastructure.</div>

|   |   |
|---|---|
| **What it is** | Mandatory clearing of eligible OTC derivatives through a registered CCP |
| **Introduced** | 2010 (US [Dodd-Frank](/dodd-frank-act/)); 2012 (EU EMIR) |
| **Covers** | Interest rate swaps, credit default swaps, foreign exchange forwards, equity derivatives (jurisdiction-dependent) |
| **Exceptions** | Physically settled FX forwards, small pension funds, end-users hedging commercial risk |
| **Operating entity** | Clearinghouses (e.g., CME Clearing, LCH, Eurex Clearing) |
| **Key mechanism** | Novation — original bilateral contract replaced by two contracts with the CCP |

</aside>

## Why the crisis made clearing mandatory

Before 2008, the over-the-counter derivatives market operated almost entirely on bilateral settlement. Two financial institutions struck a swap or option, confirmed the trade, posted collateral if contractually required, and managed the counterparty risk between them. The system was efficient for the largest dealers but opaque to regulators and fragile when stressed.

When Lehman Brothers collapsed in September 2008, the full scale of the interconnection became clear. Thousands of bilateral positions across the system froze. Counterparties discovered they were holding massive exposures to institutions they'd never directly traded with—exposure they'd sold on to third parties in a chain of daisy-chained risks. Because no one could instantly quantify the true exposure of any major bank to any other, credit seized up. The Federal Reserve and Treasury had to rescue the system wholesale.

Central clearing addresses this by placing a single, well-capitalised clearinghouse between every counterparty pair. The CCP becomes the legal counterparty to every trade, collects initial and variation margin from all participants, and invests in robust risk management. If a clearing member fails, the CCP stands between the others and contagion. Regulators gain a single vantage point to see all systemic risk in standardised products.

## How the mandate works operationally

Once a trade in a [mandated product](/dodd-frank-act/) is executed—whether on an exchange or bilaterally—it must be submitted to a registered CCP within a set deadline (typically T+1, now moving toward T+0 in some jurisdictions). The CCP runs a process called novation: it cancels the original bilateral contract and replaces it with two contracts, one between each counterparty and the CCP itself. From that moment, the original counterparties face only the CCP for settlement and default risk.

The clearing member must post initial margin—typically a percentage of the contract's notional value—upfront. As markets move, variation margin adjusts daily, flowing from the losing party to the winning party via the CCP. The CCP's own capital and insurance fund (the "guarantee fund") protect participants against a member default.

Not all products are mandated. Interest rate swaps, credit default swaps, and certain equity and foreign exchange derivatives are typically in scope, but exemptions exist. Small pension funds, non-financial corporates using derivatives to hedge commercial risk, and certain foreign exchange forwards are often carved out. Regulators recognised that forcing a mid-sized manufacturing company to post daily variation margin on an FX hedge would be operationally onerous and economically inefficient.

## The regulatory architecture: Dodd-Frank and EMIR

The **Dodd-Frank Act** (2010, US) and **EMIR** (European Market Infrastructure Regulation, 2012, EU) impose clearing mandates with subtly different scopes and enforcement. Under Dodd-Frank, the Commodity Futures Trading Commission and Securities and Exchange Commission jointly determine which derivatives are "standardised" enough for mandatory clearing; under EMIR, the European Commission designates them.

Both regimes require clearing members to maintain capital and insurance contributions proportional to risk. Both impose [trade reporting](/dodd-frank-act/) obligations—trades must be reported to a trade repository so regulators can monitor systemic risk. Both also require use of [straight-through processing](/straight-through-processing/) where feasible, meaning trades move electronically from execution to settlement confirmation without manual re-keying or handoffs.

The regulations define "standardised" loosely. A product is typically cleared if it's liquid enough to find counterparties at transparent, observable prices, and simple enough for a CCP to manage its risk. Even then, a highly customised swap between two specific counterparties might not meet the threshold, leaving room for bilateral settlement of truly bespoke structures.

## Friction and unintended consequences

The mandate has succeeded in concentrating risk visibility. But it has also tightened capital requirements at clearing members and increased operational costs. Banks must invest heavily in collateral management, systems, and compliance infrastructure. Smaller dealers and non-bank financial institutions (hedge funds, asset managers, corporates) have sometimes been squeezed out of derivatives markets because clearing membership itself carries fixed costs and regulatory burdens.

Initial and variation margin requirements, while prudent risk management, can be pro-cyclical during stress. When markets spike, variation margin calls spike, forcing sudden cash outflows at the worst moment. Regulators have had to reconsider margin models to smooth these jolts without weakening the CCP's safety.

Cross-border clearing has also proved awkward. A trade cleared in a US CCP may be regulated by both the SEC and CFTC, as well as the bank's home regulator. An EU bank clearing through LCH in London faces rules from the FCA, ESMA, and the bank's home member state. Regulatory arbitrage and jurisdictional overlaps have created pockets of inconsistency.

## See also

<div class="wiki-seealso">

### Closely related

- Clearinghouses — the central counterparties that operate clearing mandates
- [Straight-through processing](/straight-through-processing/) — the automated workflow that clearing mandates require
- [Dodd-Frank Act](/dodd-frank-act/) — US legislation that created the first major clearing mandate
- [Trade compression](/trade-compression/) — technique to reduce notional exposures in cleared derivatives portfolios
- [Failed settlement](/failed-settlement/) — what happens when a cleared trade does not settle as expected

### Wider context

- Central counterparty — the infrastructure that absorbs counterparty risk
- [Over-the-counter market](/over-the-counter-market/) — the bilateral market that clearing mandates regulate
- [Systemic risk](/systemic-risk/) — the interconnection risk the mandate was designed to reduce
- [Counterparty risk](/counterparty-risk/) — the credit exposure the CCP assumption mitigates

</div>

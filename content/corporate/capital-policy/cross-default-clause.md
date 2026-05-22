---
title: "Cross-Default Clause"
description: "Debt covenant triggering default across multiple obligations if the borrower defaults on any single debt instrument."
keywords:
  - cross-default covenant
  - debt covenant linkage
  - default cascade
  - credit event trigger
---

*A **cross-default clause** is a covenant in a [debt](/wiki/corporate-debt-structure/) agreement that triggers default across all of a borrower's obligations if the borrower misses payment or violates terms on any single debt instrument. This links otherwise independent loans and bonds into a single default event, turning a partial mishap into a full-scale crisis.*

<aside class="wiki-infobox">

| Aspect | Definition |
|---|---|
| **Definition** | One default triggers defaults across all linked obligations |
| **Common in** | [Corporate bonds](/wiki/corporate-bond/), bank loans, trade finance |
| **Trigger Thresholds** | Often $10M+ in principal (materiality test) |
| **Lookback Period** | 30–180 days (grace period to cure) |
| **Amplification Effect** | Can turn 1% balance-sheet miss into 100% balance-sheet default |
| **[Subordination](/wiki/subordinated-bond/) Interaction** | Senior lenders often exempt junior debt from cross-default |
| **Haircut Impact** | Can increase [credit spread](/wiki/credit-spread/) 50–200 bps |

</aside>

## How cross-default structures the defaults

A typical cross-default clause states: *"If Borrower defaults on any debt obligation exceeding $10 million and fails to cure within 30 days, all other debt obligations immediately mature and become due."*

This language appears in most [bond indentures](/wiki/bond-indenture/) and syndicated loans. The clause creates a **cascade effect**: a company that misses a small trade-finance payment or breaches a covenant on one loan can instantaneously be in default on $5 billion in other debt, even if those other obligations are unrelated and the borrower had no trouble paying them.

Cross-default clauses serve lenders by preventing moral hazard. Without them, a borrower could strategically default on one cheap obligation while servicing expensive ones—forcing a lender to negotiate. With cross-default, the borrower knows that any default spreads to everything.

## The amplification mechanism

Consider a company with:
- $1 billion revolving credit facility (bank syndicate)
- $2 billion [convertible bond](/wiki/convertible-bond/)
- $500 million trade credit lines

If the company misses a $30 million interest payment on the convertible (perhaps due to temporary cash flow stress), the cross-default in that bond indenture triggers. Within 30 days, the company is in default on:
- The $1 billion bank revolver (banks accelerate, demand repayment)
- The $2 billion convertible (bondholders can put it or liquidate the collateral)
- The $500 million trade lines (suppliers stop extending credit)

Total stressed debt: $3.5 billion, even though the original miss was $30 million. This is the **cross-default amplification**. A temporary cash shortage becomes a liquidity crisis becomes insolvency.

## Where cross-default appears most

**[Sovereign debt](/wiki/sovereign-debt/):** The [Iceland Banking Crisis](/wiki/iceland-banking-crisis/) offers a stark example. Iceland's three largest banks included cross-default clauses in their international bond issuances. When Kaupthing and Landsbanki failed in October 2008, creditors invoked cross-default provisions, claiming simultaneous default on all bonds. This amplified the banking crisis into a sovereign crisis—the government's bailout costs jumped as every creditor demanded payoff at once.

**[Leveraged buyouts](/wiki/leveraged-buyout/):** A PE-backed acquisition typically stacks multiple debt tranches (bank loans, senior bonds, mezzanine debt). Cross-default language links them, so a covenant breach on the mezz triggers defaults up the capital stack. This is intentional—lenders want assurance that if stress appears anywhere, they can exit. But it also means the company can pivot into distress rapidly.

**Corporate bonds and loans:** Any seasoned corporate borrower carries multiple issuances. A [merger](/wiki/merger/), regulatory setback, or commodity-price drop affecting one obligation can cascade across all others via cross-default.

## Cross-default vs. cross-acceleration

The terms are sometimes conflated but differ:
- **Cross-default:** The borrower is in default under other contracts.
- **Cross-acceleration:** Other debts become immediately due and payable (more aggressive).

A bond indenture might specify cross-default at 30 days (giving the borrower time to cure) but cross-acceleration at 60 days (no grace, debt is due now). This asymmetry gives the borrower a brief window to fix the problem before total financial collapse.

## Materiality thresholds and exemptions

To prevent trivial breaches from cascading, most cross-default clauses include a **materiality threshold**—the default must exceed a certain amount (often $10–50 million) to trigger. This prevents a $100,000 missed payment on a small trade line from blowing up the entire capital structure.

Some indentures also exempt certain debt:
- **Trade payables** (goods purchased on net-30 terms)
- **Subordinated debt** (the [subordinated bond](/wiki/subordinated-bond/) may explicitly waive cross-default rights)
- **Debt to affiliates** (intercompany loans)

These exemptions reflect the reality that not all debt is created equal; lenders negotiate to protect themselves without creating cascading risk for the whole enterprise.

## Cross-default in [DeFi](/wiki/defi-composability/) and smart contracts

In decentralized finance, cross-default is implicit in [smart contract](/wiki/smart-contract/) design. When a borrower's [collateral](/wiki/collateral-ratio/) falls below a threshold in one protocol, that protocol's [liquidation](/wiki/liquidation/) mechanism is triggered. If the borrower has [flash loans](/wiki/flash-loan/) outstanding or [derivatives](/wiki/credit-derivative/) positions across multiple venues, the liquidation cascade can spread instantly. This is a feature and a bug: it enforces discipline but creates fragility during [market stress](/wiki/market-risk/).

## Negotiation and restructuring dynamics

In [distressed debt](/wiki/distressed-debt-fund/) scenarios, cross-default clauses become points of leverage. If a company is in default on one obligation and cannot cure, creditors with cross-default rights can demand a [debt restructuring](/wiki/debt-restructuring/) or [debt-equity swap](/wiki/debt-equity-swap/) on favorable terms. The threat of cascading defaults makes the borrower eager to settle.

Conversely, in a [debt-for-equity conversion](/wiki/debt-equity-swap/), lenders often agree to **waive** cross-default temporarily, giving the company breathing room to operationally improve. This negotiation is central to most modern restructurings—lenders accept some haircut in exchange for removal of cross-default risk and a path to recovery.

<div class="wiki-seealso">

### Closely related
- [Bond Covenants](/wiki/bond-covenants/) — Restrictions and triggers in bond indentures
- [Debt Covenant Type](/wiki/debt-covenant-type/) — Affirmative vs. negative covenants
- [Bond Indenture](/wiki/bond-indenture/) — Master agreement for bond terms
- [Credit Event Sovereign](/wiki/credit-event-sovereign/) — Default triggers at country level
- [Rating Trigger Covenant](/wiki/rating-trigger-covenant/) — Covenants tied to rating downgrades

### Wider context
- [Corporate Debt Structure](/wiki/corporate-debt-structure/) — Capital stack and seniority
- [Debt Restructuring](/wiki/debt-restructuring/) — Negotiated modification post-default
- [Debt-Equity Swap](/wiki/debt-equity-swap/) — Conversion of debt to equity
- [Iceland Banking Crisis](/wiki/iceland-banking-crisis/) — Historical example of cross-default contagion
- [Subordinated Bond](/wiki/subordinated-bond/) — Junior debt with lower recovery priority

</div>

---
title: "Net Stable Funding Ratio: How It Works"
description: "The NSFR ensures banks can survive a one-year funding crisis using stable funding sources. Learn how available and required stable funding are calculated."
keywords:
  - net stable funding ratio
  - NSFR
  - stable funding requirement
  - one-year funding horizon
  - bank structural funding
  - long-term funding resilience
---

*The **Net Stable Funding Ratio** (NSFR) is a structural liquidity rule that forces banks to fund their long-term and illiquid assets with stable, long-term funding—not short-term wholesale borrowing that can evaporate in a crisis. While the [Liquidity Coverage Ratio (LCR)](/liquidity-coverage-ratio-explained/) ensures a bank can survive 30 days of panic, the NSFR ensures it can survive a full year of stress without asset fire sales or emergency liquidity. The formula is straightforward: available stable funding divided by required stable funding must equal or exceed 100%. A bank cannot load up on risky short-term funding to boost returns; regulators force a match between the stability of funding and the illiquidity of assets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Net Stable Funding Ratio — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Banks must fund illiquid assets with stable, long-term money sources.</div>

|   |   |
|---|---|
| **Regulatory minimum** | 100% |
| **Time horizon** | One year |
| **Numerator** | Available stable funding (ASF) |
| **Denominator** | Required stable funding (RSF) |
| **Current requirement** | Full phase-in as of 2018 |
| **Key distinction** | Structural, not emergency-scenario based |
| **Consequence of failure** | Capital raise, asset sale, or funding plan |

</aside>

## The structural funding problem the NSFR solves

Before the NSFR, banks could fund long-term, illiquid assets (mortgages, corporate loans) with cheap short-term wholesale borrowing (overnight repos, commercial paper, short-term deposits). This worked during good times: interest rates stayed low and funding rolled over smoothly. But in a crisis, wholesale funding markets seize up. A bank with $100 billion in mortgages and $95 billion in overnight funding faces a mismatch: when those overnight loans mature, it cannot refinance them at any price.

The NSFR corrects this structural mismatch by requiring banks to hold a minimum proportion of their assets funded by *stable* sources—deposits, long-term bonds, or equity. It is not a scenario-based test like the LCR; it is a permanent, structural constraint that discourages the maturity mismatch that caused the 2008 crisis.

## Available Stable Funding (ASF)

Available Stable Funding counts all the bank's funding sources, with different weights depending on how likely they are to stay put during a crisis. The formula weights each funding source from 50% to 100%:

**100% stable funding (full value counts):**
- Insured deposits (up to the [FDIC](/federal-deposit-insurance-corporation/) insurance cap per customer). These rarely leave because they are protected.
- Capital raised from equity or [preferred stock](/preferred-stock/). Equity holders cannot withdraw; they are locked in.
- Long-term secured funding (bonds with maturity >1 year backed by collateral).

**90% stable funding:**
- Unsecured [corporate bonds](/corporate-bond/) with >1 year to maturity issued by the bank. These are less stable than deposits but more stable than overnight funding; regulators assume a 10% runoff.

**80% stable funding:**
- Non-maturing deposits (deposits with no stated maturity but low actual runoff, like demand accounts). These are sticky but can leak. Regulators assume 20% could leave.

**50% stable funding:**
- Uninsured deposits above insurance caps. Large corporate deposits are hot money and can flee. Regulators assume 50% leaves in stress.

**0% stable funding:**
- Overnight funding, commercial paper, and other <1-year borrowed money. This does not count as stable because it will not roll over in a crisis.

The bank sums across all categories: ASF = (100% × insured deposits) + (100% × capital) + (90% × long-term bonds) + (80% × non-maturity deposits) + (50% × uninsured deposits) + (0% × overnight funding).

## Required Stable Funding (RSF)

Required Stable Funding is the other side of the equation. It weights the bank's assets and off-balance-sheet exposures by how long it would take to convert them to cash in a stress scenario. The weights range from 5% to 100%:

**100% required funding (highest weight—most illiquid):**
- Illiquid assets with no ready market: mortgages and unsecured [corporate loans](/accounts-receivable/). These cannot be sold quickly and must be held to maturity. Regulators assume you need stable funding for the full amount.
- Loans to retail customers where defaults may rise in stress.

**85% required funding:**
- [Mortgage-backed securities](/mortgage-backed-security/) and other [securitizations](/securitization/) (less illiquid than raw mortgages but not tradeable like Treasuries).
- [Corporate bonds](/corporate-bond/) held in the bank's portfolio (less liquid than securities the bank issues).

**50% required funding:**
- Unencumbered, investment-grade [corporate bonds](/corporate-bond/) and [loans](/accounts-receivable/) to investment-grade counterparties. These can be sold in most market conditions but may require a markdown.
- Equity holdings and derivatives exposures.

**5% required funding:**
- Liquid, unencumbered Treasury holdings and [high-quality liquid assets](/liquidity-coverage-ratio-explained/). These need almost no stable funding because they are saleable anytime.

**0% required funding:**
- [Central bank](/central-bank/) reserves and other assets that convert to cash instantly.

Off-balance-sheet commitments also count. A committed credit line is assumed to be drawn down during stress; [derivative](/option/) exposures are marked-to-market with add-ons.

RSF = (100% × mortgages + retail loans) + (85% × securitizations) + (50% × corporate bonds) + (5% × Treasuries) + (0% × central bank reserves).

## The NSFR formula and the 100% threshold

The NSFR is simply:

**NSFR = Available Stable Funding / Required Stable Funding ≥ 100%**

An NSFR of 100% means available stable funding exactly covers the stable funding required to hold the asset mix. An NSFR of 110% means the bank has a 10% cushion. Most large banks target 110–120% to signal prudent funding and provide a buffer for portfolio changes.

A bank can improve its NSFR by either:
1. Shifting funding toward longer maturity and insured deposits (increase ASF).
2. Shifting assets toward more liquid instruments like Treasuries (decrease RSF).
3. Reducing illiquid lending (decrease RSF).

Most banks do a mix. They offer higher rates on longer-term deposits, issue more long-term bonds, and reduce illiquid wholesale lending.

## NSFR vs. LCR: complementary, not redundant

The LCR and NSFR protect against different crises:

| Aspect | LCR | NSFR |
|--------|-----|------|
| **Horizon** | 30 days | 1 year |
| **Assumption** | Acute panic; funding markets freeze | Chronic stress; some funding available but costly |
| **Asset types** | Cares only about liquid assets | Weights all assets by illiquidity |
| **Funding sources** | Only counts cash and HQLA | Weights all funding by stability |
| **Focus** | Immediate survival | Structural mismatch |

A bank can pass the LCR (hold enough cash to survive 30 days) but fail the NSFR if it has funded all that cash with overnight borrowing. The NSFR catches structural fragility that the LCR misses.

## Real-world impact: the shift to term funding

The NSFR became mandatory in 2018, and it has reshaped bank funding markets. Banks now issue much longer-dated bonds (5–10 years instead of 2–3 years), offer higher rates on longer-term deposits to attract stickier funding, and have reduced illiquid commercial-lending books or syndicated more loans to other lenders.

Mortgages, the classic illiquid long-duration asset, are now funded mostly with insured retail deposits or long-term securitizations. Overnight repo funding has declined relative to term funding. The result is that the average bank balance sheet is now structurally safer: funding and assets are duration-matched, and there is less embedded maturity mismatch.

## Limits and challenges

The NSFR has drawbacks. A one-year horizon may be too short for truly illiquid assets like mortgages (which are 15–30 year assets). Some banks argue the NSFR over-penalizes commercial lending and securitization, raising the cost of credit. Central-bank facilities that repo-ed out illiquid assets (common during 2020) created temporary distortions—should a bank count those as readily refinanceable?—that regulators had to address with exemptions.

There is also regulatory arbitrage. A bank can shift illiquid assets to a sister company or sell them to a hedge fund, reducing RSF without truly reducing its funding risk. Regulators watch for this and sometimes adjust the rules, but the dynamic continues.

Despite these criticisms, the NSFR has meaningfully reduced maturity mismatch in large banks since 2018. Banks no longer fund 30-year mortgages with 30-day wholesale borrowing. That structural change is the NSFR's core achievement.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidity Coverage Ratio Explained](/liquidity-coverage-ratio-explained/) — the 30-day short-term liquidity requirement
- [Stress Testing: Regulatory Requirements Explained](/stress-testing-bank-regulatory-requirements/) — tests both capital and funding resilience
- [Systemic Risk Buffer Requirement](/systemic-risk-buffer-requirement/) — extra capital for too-big-to-fail banks
- [Repurchase Agreement](/repurchase-agreement/) — short-term funding markets the NSFR restricts
- [Securitization](/securitization/) — how banks convert illiquid mortgages into NSFR-friendly securities
- [Capital Adequacy](/capital-adequacy/) — the parallel capital framework

### Wider context

- [Basel III](/capital-adequacy/) — international framework including NSFR
- [Mortgage-Backed Security](/mortgage-backed-security/) — asset type with 85% RSF weight
- [Corporate Bond](/corporate-bond/) — funding source and asset, weighted differently by stability
- Financial Crisis — the 2008 maturity mismatch problem NSFR was designed to prevent
- [Central Bank](/central-bank/) — backstop for term funding and liquidity markets

</div>

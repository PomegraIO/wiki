---
title: "Collateralized Debt Obligation (CDO)"
description: "A collateralized debt obligation is a complex securitized instrument backed by a pool of bonds or loans. CDOs are structured with tranches of different risk levels."
keywords:
  - CDO
  - collateralized debt obligation
  - securitization
  - tranched structure
  - credit exposure
image: "/svg/fixed-income.svg"
---

*A **collateralized debt obligation** — or **CDO** — is a securitized debt instrument backed by a pool of bonds, loans, or other debt obligations. CDOs are structured with tranches that prioritize cash flows and losses, with AAA-rated senior tranches bearing minimal loss risk and lower-rated subordinated tranches bearing substantial risk. CDOs became infamous during the 2008 financial crisis when highly-rated CDOs backed by subprime mortgages defaulted.*

<div class="wiki-hatnote">

For mortgage-backed securitization, see [mortgage-backed security](/mortgage-backed-security/). For loan-backed securitization, see [collateralized loan obligation](/collateralized-loan-obligation/) and [asset-backed security](/asset-backed-security/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CDO — key facts</div>

<img src="/svg/fixed-income.svg" alt="A waterfall structure showing tranches and loss allocation in a CDO" />

<div class="wiki-infobox-caption">CDOs prioritize cash flows by tranche, concentrating risk in lower-rated slices.</div>

|   |   |
|---|---|
| **What it is** | Securitized pool of debt obligations |
| **Underlying collateral** | Bonds, loans, or mortgages |
| **Structure** | Tranches (AAA to BB/B equity) |
| **Cash flows** | Coupon and principal from underlying debt |
| **Losses** | Absorbed first by equity, then by BBB, then AA, then AAA |
| **Typical yield** | AAA: 100–300 bps; BBB: 400–800 bps; equity: 8–15%+ |
| **Maturity** | 5–10 years typical |
| **Risk profile** | Varies dramatically by collateral and tranche |
| **Primary issue** | Complexity, [correlation](/diversification/), opacity |

</aside>

## The structure: waterfall and tranches

A CDO bundles hundreds of debt obligations (bonds, loans, mortgages) into a single security. The obligations generate cash flows (coupon and principal payments). Those cash flows are allocated to tranches in a waterfall structure:

1. **AAA tranche** — Receives interest and principal first; protected by all subordinate tranches
2. **AA tranche** — Receives after AAA; protected by A, BBB, and equity
3. **A tranche** — Receives after AA; protected by BBB and equity
4. **BBB tranche** — Receives after A; protected only by equity
5. **Equity tranche** — Receives what's left after all seniors are paid; absorbs first losses

This structure allows the same pool of debt to be carved into securities with vastly different risk profiles. A pool where default rates are 3% might produce a safe AAA tranche (because 20% subordination protects it) and a risky equity tranche (which absorbs the first 20% of losses).

## CDOs of asset-backed securities and the crisis

The most infamous CDOs were "CDOs of ABS" — securitizations of [mortgage-backed securities](/mortgage-backed-security/) and other asset-backed securities. This created a chain of leverage: mortgages → MBS → CDO.

When mortgage defaults spiked after 2006, the entire chain collapsed. Mortgage defaults cascaded into MBS defaults, which cascaded into CDO losses. The complexity made losses opaque — investors did not understand the exposure to underlying mortgages. Ratings agencies gave AAA ratings to securities that proved to be very risky.

The failure of CDO markets was catastrophic to the financial system. The market froze; investors refused to trade CDOs at any price. Banks holding CDOs were forced to write down assets, sparking the financial crisis.

## Correlation and systemic risk

The fundamental problem with CDOs is correlation. In a diversified pool, some bonds might default while others do not. But in a recession, correlations spike — many bonds default together.

A CDO structure assumes default correlation of 30–40%. But in severe recessions, correlations approach 80–90%. This means the subordinated tranches, designed to absorb 20–30% of losses, are overwhelmed. Losses exceed design assumptions, impair senior tranches, and destroy value.

This systemic risk cannot be diversified away. When the financial system enters crisis, correlations rise, assumptions break, and CDOs suffer.

## Ratings and complexity

Rating agencies assigned AAA ratings to many CDOs that later defaulted. The complexity of the structures, the difficulty in assessing underlying collateral, and the assumption that housing never declined combined to produce catastrophically wrong ratings.

Post-crisis, rating agencies recalibrated their models and ratings became more conservative. But the damage to credibility was permanent.

## Current market for CDOs

The CDO market rebuilt slowly post-crisis. Banks issue CDOs of corporate loans ([collateralized loan obligations](/collateralized-loan-obligation/)) and other debt. These new CDOs have tighter underwriting, better transparency, and more conservative assumptions.

However, the product remains complex and appropriate only for sophisticated investors who can conduct detailed credit analysis. Retail investors typically access CDOs indirectly through [hedge funds](/hedge-fund/) or specialist [mutual funds](/mutual-fund/).

## Comparison to straight bonds

A CDO AAA tranche is materially riskier than a AAA-rated [corporate bond](/corporate-bond/) because the CDO's rating assumes perfect diversification. In practice, correlation risk means that assumption fails in crises.

A AAA-rated [corporate bond](/corporate-bond/) carries the risk of that single company; a CDO AAA tranche carries the risk of hundreds of companies plus structural risk from correlation and loss-cascade dynamics.

## See also

<div class="wiki-seealso">

### Closely related

- [Collateralized loan obligation](/collateralized-loan-obligation/) — CDOs backed by corporate loans
- [Mortgage-backed security](/mortgage-backed-security/) — the underlying collateral type
- [Asset-backed security](/asset-backed-security/) — securitized consumer loans
- [Credit spread](/credit-spread/) — why CDO tranches yield differently
- [Default rate](/default-rate/) — determines CDO performance

### Wider context

- [Securitization](/asset-backed-security/) — the underlying process
- [Recession](/recession/) — when CDO correlations spike and losses surge
- [Risk management](/hedge-fund/) — why CDO complexity is problematic
- [Diversification](/diversification/) — assumed but not guaranteed in CDOs
- [Financial crisis](/stock-market/) — 2008 demonstrated CDO fragility

</div>

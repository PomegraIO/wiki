---
title: "Basel IV Output Floor Explained"
description: "How the Basel IV output floor caps the benefit banks get from internal models by setting a minimum 72.5% ratio relative to standardised approach risk weights."
keywords:
  - basel iv output floor
  - risk-weighted assets
  - basel accords
  - capital regulation
  - internal models approach
  - standardised approach
image: "/svg/regulation.svg"
---

*The **Basel IV output floor** is a constraint on how much a bank can reduce its capital requirements by using advanced internal models instead of simpler standardised formulas. It mandates that a bank's risk-weighted assets can be no lower than 72.5% of what the standardised approach would produce, preventing banks from cherry-picking the lowest possible capital charge.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basel IV Output Floor — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Regulatory floor limiting capital arbitrage between advanced and standardised models.</div>

|   |   |
|---|---|
| **Core mechanism** | Minimum RWA cannot fall below 72.5% of standardised approach RWA |
| **Applies to** | Banks using internal ratings-based (IRB) or advanced measurement approaches (AMA) |
| **Phase-in period** | 2022–2028 (gradual increase from 50% to 72.5%) |
| **Purpose** | Prevent capital arbitrage and ensure minimum baseline risk weighting |
| **Impact on capital** | Forces banks to hold more capital than internal models alone would require |
| **Exemptions** | Smaller banks and those not using advanced models |
| **Consistency goal** | Level playing field across banks; reduces regulatory arbitrage |

</aside>

## Why the floor exists

Banks are clever at capital optimization. Starting in the 1990s, regulators allowed large, sophisticated institutions to use their own internal statistical models to calculate [risk-weighted assets](/risk-weighted-assets/) (RWA) rather than relying on blanket regulatory buckets. A bank's modelling team could estimate the probability of default and loss given default for each customer or loan, producing a precise (and often lower) capital charge than standardised tables.

The problem: internal models became a lever for reducing capital on paper without reducing actual risk. A bank might assign a borrower a 1% default probability when conservative estimates would be 3%, or argue that a risky asset carried less correlation to losses than peers estimated. Over time, these calibrations drifted downward, especially as competition heated up and banks raced to free up capital.

By 2008 and after, regulators realized that the gap between standardised and internal model capital requirements had become destabilizing. Banks using advanced approaches reported vastly lower RWA—and therefore higher [leverage ratios](/leverage-ratio-forex/)—than those using simpler rules. The output floor was introduced in Basel III to cap this arbitrage and is strengthened in Basel IV.

## The 72.5% constraint explained

The floor works mechanistically: 

1. A bank calculates RWA using both its internal models (IRB for [credit risk](/credit-risk/), AMA for operational and market risk) and the standardised approach.
2. If the internal model RWA is less than 72.5% of the standardised RWA, the bank must *use* the higher figure.
3. The bank then applies [capital adequacy](/capital-adequacy/) ratios to whichever number is binding.

**Example**: Suppose a bank's internal models produce $500 billion in RWA for its credit portfolio. The standardised approach for the same portfolio would yield $700 billion RWA. The floor is 72.5% × $700 billion = $507.5 billion. Since $500 billion < $507.5 billion, the bank must hold capital against $507.5 billion, not $500 billion.

This constraint forces banks to recognize that their models, however sophisticated, cannot drift too far from the regulatory baseline without triggering the floor.

## The phase-in timeline

Basel IV output floor did not arrive overnight. Regulators phased it in gradually from 2022 to 2028:

| Year | Floor Level |
|------|-------------|
| 2022 | 50% |
| 2023 | 55% |
| 2024 | 60% |
| 2025 | 65% |
| 2026 | 70% |
| 2027–2028 | 72.5% (final) |

This ramp allowed banks time to restructure their internal models, recalibrate parameter estimates, and potentially increase capital. Abrupt jumps would have forced rapid capital raises or deleveraging.

## Internal models vs. standardised approach

To understand why the floor matters, know the difference:

**Standardised Approach:**
- Uses fixed risk weights set by regulators (e.g., 100% weight on most corporate loans, 50% on mortgages, 20% on sovereign debt).
- Simple, transparent, comparable across banks.
- Crude: does not reflect an individual bank's credit or operational risk profile.

**Internal Models Approach (IRB/AMA):**
- Banks estimate probability of default (PD), loss given default (LGD), and exposure at default (EAD).
- Produces granular, often lower, capital charges.
- Requires extensive historical data, validation, and regulator approval.
- Subject to model risk: a miscalibrated parameter can understate risk.

The output floor acknowledges that internal models excel at precision but can be gamed. By forcing models to stay within 72.5% of standardised RWA, regulators preserve incentives for better modelling while preventing a free fall in capital.

## Who it affects most

The floor binds hardest on banks where internal models produce the lowest RWA relative to standardised formulas. This often includes:

- **Large European banks** using advanced IRB approaches on consumer portfolios; consumer lending risk weights under internal models sometimes fall far below standardised buckets.
- **Sophisticated trading desks** using advanced market risk models, which can produce thin [value-at-risk](/value-at-risk/) estimates.
- **Operational risk modellers**, where AMA can yield tight estimates if historical loss data is sparse.

Smaller banks and those using standardised approaches only are unaffected.

## Capital allocation and business impacts

When the floor bites, banks must hold more capital than models suggest. This changes incentives:

- **Pricing**: A loan that internal models say is low-risk but the floor constrains is now more expensive to the bank in capital terms; pricing may rise.
- **Portfolio mix**: Banks may shift away from low-risk assets that carry high standardised weights but low model weights (e.g., mortgages) into assets where models and standardised rules align.
- **Capital raising**: Some banks have issued equity or debt to meet the higher requirement, especially during phase-in.
- **Regulatory capital vs. economic capital**: The gap between what regulators require and what internal risk models suggest widens, creating a "regulatory tax" on certain businesses.

## Cross-border and competitive implications

Basel IV output floor is a global standard (agreed by the Basel Committee on Banking Supervision), but implementation varies slightly by jurisdiction. The EU adopted it into CRR II/CRD VI; the US has similar constraints under the [Dodd-Frank Act](/dodd-frank-act/) framework. This harmonisation reduces the chance that banks arbitrage between jurisdictions by choosing the weakest rules.

However, smaller jurisdictions and non-Basel signatories (e.g., some emerging markets) may not fully adopt it, creating pockets where the floor is looser or absent. International banks with subsidiaries in such jurisdictions face inconsistent capital treatment.

## Model validation and governance

The output floor raises the stakes for internal model governance. A bank's internal validation team must prove its models are accurate; if models perform worse than standardised rules, regulators scrutinise assumptions. This drives investment in:

- Back-testing: comparing model-predicted losses to actual outcomes.
- Stress testing: ensuring models hold up in extreme scenarios.
- Parameter estimation: using more conservative data, longer time horizons, and robust statistical methods.

Poor validation can result in regulator-imposed model restrictions or forced migration to standardised approaches.

## See also

<div class="wiki-seealso">

### Closely related

- [Risk-Weighted Assets](/risk-weighted-assets/) — The metric constrained by the output floor.
- [Capital Adequacy](/capital-adequacy/) — Regulatory framework using RWA to set minimum capital ratios.
- [Dodd-Frank Act](/dodd-frank-act/) — US parallel rules on capital standards.
- [Stress Testing](/stress-testing/) — Model validation and risk governance.
- [Credit Risk](/credit-risk/) — A primary risk class subject to internal models.

### Wider context

- [Monetary Policy](/monetary-policy/) — Central banks implement capital rules via regulation.
- [Federal Reserve](/federal-reserve/) — US regulator enforcing comparable rules.
- [Systemic Risk](/systemic-risk/) — Capital floors protect against bank failure cascades.

</div>

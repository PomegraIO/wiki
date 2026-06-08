---
title: "How Rating Agencies Rate Structured Finance Tranches"
description: "Explains how rating agencies assess CLO, ABS, and CMBS tranches using cash-flow waterfall and loss-coverage analysis, and why AAA structured notes differ from corporate AAA bonds."
keywords:
  - structured finance tranche rating
  - how rating agencies rate tranches
  - cash flow waterfall rating
  - collateralized loan obligation rating
---

*Rating agencies assess **structured finance tranches** by modeling the cash flows from an underlying pool of assets, then determining how much loss a tranche can absorb before investors lose principal. This approach differs fundamentally from corporate-bond ratings: a AAA tranche depends on the chain of priority, the diversity of collateral, and conservative assumptions about default rates—not on the issuer's balance sheet.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Structured Finance Tranches — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Waterfall mechanics determine how losses flow through tiers of investors.</div>

|   |   |
|---|---|
| **Key drivers** | Subordination, loss coverage, collateral quality, default assumptions |
| **Why tranches differ** | Senior tranches are buffered by junior tranches absorbing losses first |
| **Rating-agency model** | Stress tests on default rate, recovery rate, and timing of cash flows |
| **Common structures** | CLOs (collateralized loan obligations), ABS (asset-backed securities), CMBS (commercial mortgage-backed securities) |
| **AAA assumption** | Can withstand stress scenario without principal loss to senior investors |

</aside>

## The Waterfall and Subordination

In a structured finance deal, assets (mortgages, loans, auto loans, or corporate debt) are pooled and tranched. The simplest structure has two tiers: senior and junior. When the pool receives interest and principal payments, or when defaults occur, money flows down a waterfall. Senior investors get paid first; junior investors absorb losses first.

A AAA-rated senior tranche, therefore, is not AAA because the underlying loans are AAA—most aren't. It is AAA because the junior tranches underneath it act as a buffer. If 5% of the pool defaults and recovers 60 cents on the dollar, the junior class takes that loss. The senior class only faces risk if defaults exceed the cushion created by the junior tranche's size.

Rating agencies quantify this cushion as "loss coverage" or "subordination." If junior tranches represent 10% of the deal size and conservative stress assumptions forecast 8% total losses, the junior class can absorb the hit. Senior investors remain protected.

## Loss Modeling: Defaults, Recovery, and Timing

Agencies build a scenario for the life of the pool. They specify:

- **Default rate**: A stressed annual probability that each borrower defaults (e.g., 3% per year for auto loans in a recession scenario).
- **Recovery rate**: What the servicer recovers after seizure or liquidation (e.g., 60% for auto loans, 70% for investment-grade corporate debt).
- **Timing**: When defaults are assumed to occur (concentrated early in the deal's life creates worst-case stress).

They then run the waterfall: month by month (or quarter by quarter), the model calculates interest and principal collections, pays servicer fees, then disburses to tranches in priority order. When defaults happen, recoveries offset losses. The model tracks whether each tranche's principal balance ever touches zero.

For a tranche to earn AAA, it must withstand the specified stress scenario without principal loss. If junior tranches are sized to absorb 8% losses and the model shows 5%, the senior class survives intact across the entire scenario.

## Differences from Corporate Ratings

This is why a AAA-rated mortgage-backed security is not comparable to a AAA-rated corporate bond. A corporate AAA reflects the issuer's balance sheet, earnings, and financial flexibility. A tranche AAA reflects a carefully modeled waterfall and subordination stack.

Consider two scenarios:

**Scenario A**: A AAA corporate bond from a stable utility. The rating assumes the corporation will generate enough cash to meet interest and principal payments even in a significant economic downturn.

**Scenario B**: A AAA senior tranche in a CMBS deal. The underlying mortgages might be held by shaky borrowers; what matters is that the waterfall—defaults, recoveries, timing, and subordination—leaves the senior tranche with an adequate cushion.

If the utility stumbles but stays solvent, bondholders may still get paid. If a CMBS pool experiences worse-than-modeled defaults, the waterfall model breaks down and the "AAA" tranche can suffer losses.

## Collateral Quality and Diversity

Agencies also assess the underlying assets. A CLO backed by high-yield corporate loans has different credit quality than one backed by investment-grade loans. They weight:

- The [credit-rating distribution](/credit-rating/) of the loans in the pool.
- Industry concentration (if 20% of borrowers are in hospitality, a recession in that sector is a shared risk).
- Loan terms (covenants, leverage ratios, interest-coverage ratios).
- Servicer capabilities and track record.

A diverse pool of seasoned borrowers carries lower default risk than a concentrated pool of start-ups. The model inputs reflect this, so the subordination required for a AAA rating may be lower (or the tranche may be larger for the same subordination).

## Sensitivity and Stress Testing

Agencies publish their rating methodology, but they also model sensitivities. They ask: What if default rates are 20% higher than assumed? What if recovery drops by 10 percentage points? What if all losses occur in year one instead of spreading across the life of the deal?

A well-rated senior tranche should still survive these perturbations. If a small increase in default rates causes the senior tranche to suffer losses, the rating is questioned.

## Post-2008 Lessons

Before the financial crisis, rating agencies were criticized for under-stressing mortgage-backed securities and CDO tranches. They underestimated both the default correlation (borrowers defaulted together when house prices fell) and the recovery rate (underwater mortgages recovered very little). Agencies have since tightened assumptions and increased diversification requirements.

Modern structured finance ratings are more conservative, but they remain dependent on the integrity of the assumptions. If reality diverges sharply—collateral quality is worse than advertised, timing of defaults is clustered, or recoveries collapse—the waterfall model fails.

## The Market-Rating Divergence

Investors sometimes distrust agency ratings and compare them to market-implied assessments. A [credit-default-swap](/credit-default-swap/) spread on a tranche reveals what the market thinks the true risk is. If the market prices a AAA tranche very cheap (implying near-zero risk), or if the CDS spread widens sharply after issuance, it signals either that the market thinks the rating is too generous or that the underlying pool has deteriorated.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Rating](/credit-rating/) — how agencies grade debt securities
- [Rating Agency Conflict of Interest: The Issuer-Pays Problem](/rating-agency-conflict-of-interest/) — structural bias in agency incentives
- [Credit-Default Swap](/credit-default-swap/) — market-based alternative to agency ratings
- [Implied Credit Rating from CDS Spreads](/implied-rating-from-cds-spread/) — backing out market-implied ratings from derivative prices

### Wider context

- [Securitization](/securitization/) — process of pooling assets and issuing tranches
- [Mortgage-Backed Security](/mortgage-backed-security/) — a major class of structured finance
- [Credit Risk](/credit-risk/) — the underlying risk being modeled
- [Interest-Coverage Ratio](/interest-coverage-ratio/) — one metric within credit assessment

</div>

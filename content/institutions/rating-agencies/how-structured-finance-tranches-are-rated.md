---
title: "How Structured Finance Tranches Are Rated"
description: "Explains the credit-enhancement waterfall and loss-model methodology rating agencies use to assign AAA to equity ratings to senior, mezzanine, and equity tranches."
keywords:
  - how structured finance tranches rated
  - structured finance tranche ratings
  - credit enhancement waterfall
  - mezzanine tranche rating
  - rating agencies structured products
image: /svg/institutions.svg
---

*Rating agencies assign different ratings to senior, mezzanine, and equity tranches of the same asset pool using a **credit-enhancement waterfall** and probabilistic loss models. The mechanism is straightforward in principle: senior tranches get priority claim on cash flows, absorbing losses last; junior tranches take losses first, cushioning seniors. But the actual rating depends on modeling how many assets will default and how much recovery they'll generate.*

## The Waterfall: Who Gets Paid First

Structured finance relies on legal and contractual rank-ordering. A mortgage-backed security, collateralized loan obligation, or any securitization divides assets into tranches stacked by seniority.

| Tranche | Claim Priority | Losses Borne | Typical Rating |
|---------|---|---|---|
| Senior | First | Last | AAA to AA |
| Mezzanine | Second | Middle | A to BBB |
| Equity (residual) | Last | First | Unrated |

When the underlying asset pool generates cash, principal and interest flow to senior tranche holders first. If a loan defaults, the loss is absorbed by equity holders immediately. Only after equity is wiped out do mezzanine tranches take losses. Senior tranches absorb losses only after all junior cushions are gone.

This ordering—the waterfall—is the core credit enhancement mechanism. A senior tranche rated AAA is not saying "no asset in the pool will default." It's saying "even if losses reach X%, this tranche doesn't lose a cent."

## Loss Modeling: The Rating Methodology

Rating agencies estimate the probability that losses will exceed the cushion protecting each tranche. The calculation hinges on three components:

**Default assumptions.** The agency models the probability that loans in the pool will default. For mortgages, this reflects economic stress scenarios, borrower credit scores, and loan-to-value ratios. For corporate loans, it reflects industry cyclicality and borrower leverage. These assumptions are often expressed as "default curves"—typically showing that default rates spike during recessions and fall during expansions.

**Loss-given-default.** If a loan defaults, how much is recovered? For mortgages, recovery depends on house-price decline and foreclosure costs. For corporate loans, it depends on collateral value and seniority. Agencies typically assume loss-given-default of 40–70% for mortgages (after legal costs and property depreciation) and 30–50% for corporate debt (recovery from collateral, if any).

**Correlation.** Losses cluster in bad times. Mortgages don't default independently; if housing prices collapse, many do simultaneously. Structured finance models assume some level of correlation among defaults in the pool. Higher correlation means more extreme tail outcomes and less diversification benefit.

Given these assumptions, the agency runs a loss distribution: a statistical model showing the probability of different cumulative loss levels. The rating is then assigned by mapping loss percentiles to rating categories.

## Rating Mapping: From Loss Percentiles to Letter Grades

The mapping from loss model to rating reflects historical default probabilities for each rating category. An AAA security has a 0.03% expected default rate over 10 years (roughly one default per 3,000 AAA-rated securities). An A has roughly 0.1% per year.

For a structured product, the agency asks: "What is the probability that losses will exceed this tranche's cushion?" If a senior tranche is sized such that a 99.9% percentile loss scenario would wipe it out, it gets an AAA rating (since only a 0.1% chance of exceeding that loss level remains).

**Example:** Suppose a mortgage pool has $100 million in loans, and the agency models:
- 5% average default rate in a severe stress scenario
- 60% loss-given-default (after recovery)
- Expected loss from defaults: $100M × 5% × 60% = $3M

The agency also considers correlation and tail risk, estimating that there's a 1-in-1,000 chance losses exceed $8M. It then sizes tranches:

| Tranche | Size | Cushion | Rating |
|---------|---|---|---|
| Senior A | $90M | Takes losses above $10M | AAA |
| Mezzanine B | $7M | Takes losses above $3M (before hitting Senior) | A |
| Equity | $3M | Takes first $3M of losses | Unrated |

Senior A has an $8M cushion ($10M total possible loss minus $2M senior size). Since modeled 99.9th percentile losses are $8M, the stress test shows senior A can absorb the worst reasonably expected scenario, earning an AAA rating.

## Credit Enhancements Beyond the Waterfall

Structurers and agencies layer additional protections:

**Overcollateralization.** Assets are pledged in excess of tranche size. A mortgage pool might be $105M in loans, but only $100M in tranches. The $5M overage absorbs losses first.

**Excess spread.** Interest income exceeds tranche coupons; the surplus is trapped in a reserve account or used to amortize principal faster, further protecting seniors.

**Triggers and caps.** If delinquency or default rates hit specified thresholds, cash flow diverts from junior to senior tranches, or the securitization stops purchasing new assets, locking in what it has.

## Rating Assumptions and Their Limits

The rating process is only as good as its assumptions. If default curves are too optimistic or loss-given-defaults are underestimated, actual losses will exceed projections, and the rating proves too high. This happened during the 2008 financial crisis: rating agencies systematically underestimated default rates and loss-given-defaults on mortgage pools, assigning AAA ratings to tranches that later suffered heavy losses.

Correlation assumptions are particularly critical and hard to calibrate. Agencies often assume a fixed correlation across all scenarios, but correlations spike to near 100% during crises (all borrowers are stressed simultaneously) and fall to near-zero during booms. Contingency for extreme tail events—sometimes called "stress testing"—helps, but cannot eliminate model risk.

## Rating Methodologies Differ by Asset Class

Different underlying assets require different models. Mortgage-backed securities stress house-price declines; collateralized loan obligations stress recession and covenant violations; structured credit products stress recovery timing and fraud. Agencies maintain separate methodologies for each asset class, and ratings for the same loss percentage can vary if the underlying asset pools have different risk profiles.

## Agency Governance and Conflicts

All three major agencies—Moody's, Standard & Poor's, and Fitch—employ teams of credit analysts and modelers. The agencies are paid by the structurers (a conflict of interest), but they also face legal liability and reputational consequences if ratings prove materially wrong. Regulatory scrutiny increased after 2008, and agencies now disclose methodologies and conduct more rigorous back-testing.

## Practical Use of Tranche Ratings

Institutional investors rely on ratings as screening tools, though rarely as sole decision criteria. An A-rated mezzanine tranche in a RMBS (residential mortgage-backed security) might be bought by insurance companies or banks with capital constraints that limit how much sub-investment-grade risk they can hold. An AAA-rated senior tranche is often held by conservative funds and satisfies regulatory capital requirements.

The rating communicates a loss-absorption capacity, not a recommendation. It's one input into due diligence alongside cash-flow analysis, collateral quality, and stress-testing at the portfolio level.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Rating](/credit-rating/) — rating methodology for corporate and government bonds
- [Mortgage Backed Security](/mortgage-backed-security/) — largest asset class for structured securitization
- [Tranche](/tranche/) — hierarchical seniority structure in asset-backed securities
- [Securitization](/securitization/) — the pooling and issuance process that creates tranches
- [Structured Product](/structured-product/) — broader category of engineered investments

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator overseeing agency disclosures
- [Counterparty Risk](/counterparty-risk/) — rating agencies themselves face default risk in their legal liabilities
- [Risk Weighted Assets](/risk-weighted-assets/) — capital requirement that uses agency ratings as input
- [Stress Testing](/stress-testing/) — validation technique for rating models

</div>

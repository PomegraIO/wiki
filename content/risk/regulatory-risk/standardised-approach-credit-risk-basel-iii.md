---
title: "Standardised Approach to Credit Risk Under Basel III"
description: "How banks assign fixed risk weights to loans using the standardised approach, and when this simpler method is required instead of internal models."
keywords:
  - standardised approach credit risk basel iii
  - credit risk weights
  - regulatory capital requirements
  - basel iii credit risk
  - risk-weighted assets
image: "/svg/risk.svg"
---

*Under **Basel III**, the standardised approach to credit risk lets regulators assign fixed risk weights to loan categories—mortgages, corporate loans, government debt—instead of requiring banks to build internal statistical models. It is simpler, more transparent, and mandatory for smaller institutions, though large banks can opt for the more complex internal ratings-based (IRB) method if they prove they can model risk accurately.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Standardised Approach — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for credit risk." />

<div class="wiki-infobox-caption">Standardised approach uses preset risk weights; simpler than internal models, but less tailored to individual banks' portfolios.</div>

|   |   |
|---|---|
| **Risk weights** | Fixed percentages set by regulators; typically 0% to 150% |
| **Applies to** | Corporate loans, mortgages, government debt, retail exposure |
| **Data required** | Credit rating of borrower (for corporate), LTV ratio (for mortgages), asset class |
| **Who uses it** | Smaller banks, newer banks, or large banks on non-major portfolios |
| **Alternative** | Internal ratings-based (IRB) approach; requires regulatory approval |
| **Capital output** | Risk-weighted assets (RWA); dictates minimum [capital-adequacy](/capital-adequacy/) ratio |
| **Regulator** | [Federal Reserve](/federal-reserve/), SEC, [OCC](/securities-and-exchange-commission/), local equivalents globally |

</aside>

## The Two Paths to Credit Risk

Basel III gives banks two methods to measure credit risk and compute the capital they must hold:

1. **Standardised Approach**: Regulator prescribes a risk weight for each loan category. A residential mortgage with 80% loan-to-value (LTV) gets 35% weight; a corporate loan to a BB-rated firm gets 100% weight. The bank multiplies each loan's balance by its assigned weight to get risk-weighted assets.

2. **Internal Ratings-Based (IRB) Approach**: The bank builds proprietary models using historical default rates, loss-given-default, and exposure-at-default. It assigns a risk weight to each borrower based on its own estimated probability of default. This is more granular but requires regulatory validation and constant monitoring.

The standardised approach is the baseline. Every bank can use it. Larger banks often graduate to IRB after proving their models work and winning supervisor approval.

## How Risk Weights Are Set

Regulators—in the United States, the [Federal Reserve](/federal-reserve/), [Office of the Comptroller of the Currency](/securities-and-exchange-commission/), and Federal Deposit Insurance Corporation—publish a standardised schedule. Risk weights vary by asset type:

- **Sovereigns (government debt)**: 0% for debt issued by the home country; 20%–150% for foreign governments, depending on credit rating.
- **Corporate loans**: 20% for highest-rated (AAA), stepping up to 150% for unrated or very weak credits.
- **Residential mortgages**: 35% for owner-occupied with strong LTV; 100% for non-owner-occupied or weak LTV.
- **Retail exposure**: 75% flat rate for small business loans and consumer credit.
- **Cash and cash equivalents**: 0%.

These weights reflect historical loss rates. A AAA-rated firm defaults rarely; a BB-rated firm defaults more often. Regulators smooth the schedule to avoid gaming and keep the math consistent across banks.

## Computing Risk-Weighted Assets (RWA)

A bank's [risk-weighted assets](/risk-weighted-assets/) is the sum of each loan balance multiplied by its risk weight:

**RWA = Σ (Loan Balance × Risk Weight)**

Example: A $1 billion corporate loan to a BBB-rated firm has a 100% risk weight.

**RWA contribution = $1 billion × 100% = $1 billion**

The bank must hold minimum capital (typically 8% of RWA) to satisfy Basel III. So for this loan, minimum required capital is $80 million.

This is the key mechanic: standardised weights lock in the relationship between loan size and capital requirement. A bank cannot claim a loan is safer than the regulator's schedule permits; conversely, it cannot be more conservative without holding extra capital.

## When Standardised Is Mandatory

Not all banks can choose. Regulators require:

- **Small banks** (under $10 billion in assets, typically) use standardised only.
- **Banks without IRB approval** must use standardised.
- **Newer banks** with limited default history cannot yet model their own credit risk and default to standardised.
- **Certain loan types** within a bank might be restricted to standardised even if the bank has IRB approval elsewhere (e.g., equity holdings, securitizations).

Large banks in developed markets often have IRB approval for major portfolios (corporate, retail mortgages) but use standardised for specialized or small exposures.

## Why Banks Prefer IRB (If They Can Use It)

Under IRB, a bank's own estimated default rate becomes the risk weight input. If a bank's historical data shows a 0.5% default rate on a loan type, it can model a lower risk weight than the standardised schedule prescribes. This yields lower RWA, lower minimum capital, and (in principle) higher profits.

But IRB requires:

- Robust historical data on defaults and losses (usually 10+ years).
- Validated statistical models for [probability of default](/default-rate/), loss-given-default, and exposure-at-default.
- Annual backtesting and supervisory approval.
- Continuous monitoring and recalibration.

Regulators audit IRB models heavily. If a bank's assumptions are too optimistic and actual defaults spike, the regulator can revoke IRB status and force the bank back to standardised, a costly and humbling reversal.

## The Trade-Off: Simplicity vs. Tailoring

The standardised approach sacrifices tailoring for simplicity. Two loans that are genuinely different in credit quality might get the same weight if they fall in the same regulatory bucket. A retail bank with an excellent underwriting track record cannot claim credit in the capital calculation; it holds the same minimum capital as a weaker rival.

Conversely, standardised approach prevents regulatory arbitrage. Banks cannot tweak models to artificially lower capital and take excessive risk. The transparent, fixed schedule also makes capital comparisons across banks easier: if Bank A and Bank B hold the same portfolio, their RWA will match.

Policymakers introduced the standardised approach (revised in 2015 in the "Fundamental Review of the Trading Book") partly in response to 2008. Many large banks' IRB models had massively underestimated risk; the standardised schedule provides a reality check.

## Linking to Capital Ratios

Once a bank computes RWA using either standardised or IRB, it calculates its [capital-adequacy](/capital-adequacy/) ratio:

**Tier 1 Capital Ratio = Tier 1 Capital / RWA**

Basel III requires this ratio to be at least 8%. A bank with RWA of $100 billion must hold at least $8 billion in Tier 1 capital.

Standardised approach thus directly shapes how much capital a bank must raise and hold. Regulators can tighten risk weights to force banks to raise capital; banks lobby to lower weights to reduce capital burden.

## Evolution and Critique

When Basel III launched (2010–2015), the standardised approach was meant as a floor. The expectation was that IRB would dominate at large banks, while standardised served as a backstop.

Since 2008, however, regulators have grown skeptical of banks' models. The 2020 revision (Basel IV, not yet fully implemented) actually strengthened the standardised approach and constrained how much lower IRB can go relative to standardised. This pushes capital requirements back up, particularly for large banks that had benefited from low IRB weights.

Some scholars argue that standardised approach, despite its simplicity, is actually safer because it strips away false precision. A loan is a loan; the regulator's judgment on its risk weight is transparent and enforced uniformly.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital Adequacy](/capital-adequacy/) — the regulatory minimum capital banks must hold
- [Risk-Weighted Assets](/risk-weighted-assets/) — the denominator in capital ratios
- [Credit Risk](/credit-risk/) — the core risk of lending
- [Credit Rating](/credit-rating/) — ratings assigned by agencies; often determine risk weights
- [Counterparty Risk](/counterparty-risk/) — credit risk owed to you by another institution

### Wider context

- [Basel III](/basel-iii/) — broader regulatory framework for banks
- [Federal Reserve](/federal-reserve/) — US central bank and key regulator
- Regulation — broader financial regulation framework
- [Default Rate](/default-rate/) — what credit risk ultimately becomes
- [Stress Testing](/stress-testing/) — complementary way banks assess capital needs

</div>

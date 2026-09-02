---
title: "Expected Loss Model"
description: "A framework for measuring credit risk by combining the probability of borrower default, the amount exposed at default, and the loss if default occurs."
keywords:
  - expected loss
  - credit risk
  - probability of default
  - loss given default
---

*The **Expected Loss Model** is a quantitative framework for measuring [credit risk](/wiki/credit-risk/). It expresses expected losses as the product of three components: the probability that a borrower will default within a given period, the exposure at the time of default, and the loss the lender incurs as a fraction of that exposure. EL = PD × EAD × LGD. This model underpins modern credit risk management and regulatory [capital](/wiki/tier-1-capital/) requirements.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|---|---|
| **Formula** | EL = Probability of Default (PD) × Exposure at Default (EAD) × Loss Given Default (LGD) |
| **Measurement period** | Usually 1 year (for IRB regulatory models) but can vary |
| **PD range** | 0% to 100%; estimated from historical default rates |
| **EAD range** | The outstanding balance at the time of default; can be less than committed balance |
| **LGD range** | 0% to 100%; depends on collateral value and recovery |
| **Capital regulation** | Basel III uses this model to calculate minimum regulatory capital |

</aside>

## The three components

**Probability of Default (PD)**: The likelihood that a borrower will fail to make a required payment within one year (or another specified time horizon). A AAA-rated firm might have a PD of 0.01% (1 in 10,000); a BB-rated firm might have a PD of 2% (1 in 50). PD is estimated from historical default rates of borrowers with similar credit profiles, industry, and economic conditions.

**Exposure at Default (EAD)**: The total value of the lender's claim on the borrower at the moment of default. For a term loan, it's the outstanding balance. For a [credit line](/wiki/credit-utilization-ratio/), it's the drawn amount plus an estimate of additional amounts the borrower will draw before defaulting (called the "credit conversion factor"). For a bond, it's the face value of the outstanding issue.

**Loss Given Default (LGD)**: The percentage of EAD that the lender loses after the borrower defaults. If a lender has a $10 million loan to a company secured by $8 million in collateral, and the collateral is sold for $7 million, the LGD is ($10M - $7M) / $10M = 30%. LGD depends on seniority (senior unsecured claims recover more than junior ones), collateral quality, and recovery costs.

## A simple example

A bank originates a $5 million term loan to a manufacturing company. The loan is backed by inventory and equipment worth $3 million. Based on industry data, the bank estimates:

- PD: 3% (1 in 33 chance of default in the next year)
- EAD: $5 million (the full outstanding balance)
- LGD: 60% (if the company defaults, the collateral will be sold for ~40% of its current value, meaning the bank loses 60% of EAD)

Expected Loss = 3% × $5M × 60% = $90,000

This means the bank should, on average, expect to lose $90,000 from this loan over the next year. If the bank has 100 such loans with identical characteristics, it should expect ~$9 million in losses (~1.8% of the $500M portfolio). The bank's [provision for credit losses](/wiki/provision-for-credit-losses/) should include this $90,000 (and similar amounts for all other loans).

## Estimating each component

**PD Estimation**: Lenders analyze historical default rates of borrowers stratified by [credit rating](/wiki/credit-rating/), industry, firm size, and macroeconomic conditions. A bank might observe that BBB-rated industrial companies default at 0.5% per year on average; BB-rated companies at 2%. The bank applies these historical rates as forward-looking estimates. Some models add forward-looking macroeconomic variables (GDP growth, unemployment, [interest rates](/wiki/interest-rate/)) to adjust PD for the current economic cycle.

**EAD Estimation**: For term loans and bonds, EAD is straightforward—the outstanding balance. For credit lines, it's trickier: a borrower with a $10 million unused line might draw $2–3 million before defaulting, so EAD is not $0 (the current drawn amount) but rather $0 + estimated drawdowns. Banks use historical borrower behavior and the size of committed credit to estimate drawdown rates.

**LGD Estimation**: Lenders analyze recoveries on defaulted loans, segmented by loan type, collateral type, and seniority. A first-lien mortgage on residential real estate might have an LGD of 5–10% (lenders recover 90–95% of EAD via foreclosure); a junior unsecured loan might have an LGD of 80–90%. LGD also depends on recovery time (longer recoveries mean more costs and time-value deterioration).

## The expected loss model vs. [provision for credit losses](/wiki/provision-for-credit-losses/)

The expected loss model calculates the *average* loss the lender expects to incur. But in any given year, actual losses might be zero (no defaults) or much higher (a recession causes 5% of borrowers to default). The [provision for credit losses](/wiki/provision-for-credit-losses/) is the accounting reserve built to cover expected losses. Using the example above, the bank would provision $90,000 against the $5M loan in its financial statements.

## Regulatory capital and Basel III

Under [Basel III](/wiki/basel-iii/), banks must hold [capital](/wiki/capital-adequacy/) proportional to the risks they take. The IRB (Internal Ratings Based) approach uses the expected loss model:

Capital Requirement = EL + (Unexpected Loss)

The unexpected loss captures tail risk—the potential for losses to exceed the expected loss in stressed conditions. A bank might expect $90,000 in losses on the $5M loan but must hold capital to cover potential losses up to, say, $400,000 (if a recession causes higher-than-expected defaults and recoveries fall).

## Limitations and criticisms

**Pro-cyclicality**: During a boom, default rates are low, PD estimates fall, and banks reduce capital holdings. When a recession hits, default rates spike, PD estimates jump, and banks are forced to raise capital—just when credit is tightest. This amplifies credit cycles.

**Model risk**: The expected loss model assumes historical relationships between PD, EAD, and LGD continue into the future. If new risks emerge (e.g., COVID-induced supply-chain failures that were rare in historical data), the model will underestimate losses.

**Interconnectedness**: The model treats each loan independently but doesn't capture systemic risk. If many borrowers are exposed to the same counterparty or market (e.g., oil price), their defaults might be correlated, creating portfolio-level risk the model misses.

**Behavioral:** Lenders and borrowers change behavior when they perceive risk. As defaults rise, borrowers might prepay to avoid perceived financial stress, reducing EAD. These dynamics are not captured in historical models.

## Advanced expected loss frameworks

Modern credit risk management uses **three-stage expected loss** models:

- **Stage 1 (performing)**: Expected losses over the next 12 months.
- **Stage 2 (under stress)**: Expected losses over the loan's lifetime if credit quality has deteriorated.
- **Stage 3 (in default)**: Estimated losses on loans already in default or likely to default soon.

[IFRS 9](/wiki/credit-loss-model/) (International Financial Reporting Standards) and CECL (Current Expected Credit Loss) in the US mandate this approach, making it a global standard.

<div class="wiki-seealso">

### Closely related
- [Probability of Default](/wiki/probability-of-default/) — The PD component
- [Loss Given Default](/wiki/loss-severity/) — The LGD component
- [Credit Risk](/wiki/credit-risk/) — The underlying risk being measured
- [Provision for Credit Losses](/wiki/provision-for-credit-losses/) — The accounting reserve built from EL estimates

### Wider context
- [Basel III](/wiki/basel-iii/) — The regulatory framework incorporating expected loss
- [Capital Adequacy](/wiki/capital-adequacy/) — The regulatory standard this model informs
- [Credit Rating](/wiki/credit-rating/) — A summary measure that incorporates PD
- [Counterparty Credit Risk](/wiki/counterparty-credit-risk/) — The expected loss concept extended to derivatives

</div>

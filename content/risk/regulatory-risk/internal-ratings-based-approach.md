---
title: "Internal Ratings-Based Approach"
description: "A Basel II/III method that allows banks to use proprietary models of default probability and loss-given-default to set their own regulatory capital requirements."
keywords:
  - irb approach
  - risk weights
  - basel iii
  - credit models
  - regulatory capital
  - model risk
image: "/svg/risk.svg"
---

*The **internal ratings-based approach** (IRB) permits large banks to develop proprietary credit models estimating probability of default (PD) and loss-given-default (LGD) for borrowers, then use these estimates to calculate regulatory risk weights and capital requirements. IRB offers efficiency gains but transfers model validation risk to banks and requires intense regulatory oversight.*

## The case for models over rules

Under the standardized approach to [risk-weighted assets](/risk-weighted-assets/), a bank faces a one-size-fits-all weight: all investment-grade corporates get 100%, all residential mortgages a flat 35%, all unrated corporates 100%. A bank that has spent years building detailed knowledge of small-business credit risk—the industry, the founders, the cash-flow volatility, the recovery value of collateral—is treated the same as a peer that buys mortgages through a mortgage broker with no deep underwriting. The standardized weights are conservative, which is prudent but costly: a bank must hold more capital than the true risk of its portfolio warrants, squeezing profitability and raising lending costs for customers.

The IRB approach flips this. A bank estimates, for each borrower or loan segment, the probability that the borrower will default within a year (PD) and the fraction of the exposure lost if default occurs (LGD). The bank also models the exposure at default (EAD) for complex instruments like revolving credit. From PD, LGD, and EAD, the regulator-approved formula yields a risk weight: a SME loan with a 2% PD and 45% LGD gets, say, a 75% weight instead of a flat 100%; a prime mortgage with a 0.5% PD and 30% LGD gets a 20% weight instead of 35%. Better-understood risks are rewarded with lower capital charges. This incentivizes the bank to invest in underwriting, collateral management, and data infrastructure—activities that genuinely reduce risk.

## How banks build IRB models

A bank's IRB framework is built on historical data. A mortgage originator compiles loan-by-loan performance: origination characteristics (LTV, credit score, loan size, rate type), performance history (prepayment, delinquency, default), and recovery data (home sale price, costs of liquidation). The bank groups loans into pools by shared characteristics (e.g., owner-occupied mortgages with 80–90% LTV and FICO 720–740) and fits a statistical model—logistic regression, random forest, neural network—to estimate the default rate for each pool. This default rate becomes the PD. Similarly, for each default, the bank calculates actual recovery given the home sale, costs, and timing. The loss rate across defaults is the LGD.

For corporates, the bank builds models by industry, geography, and leverage. A model might predict default for a USD 10 million syndicated loan to a mid-market distributor with EBITDA of USD 3 million and leverage of 2.5x based on tens of thousands of historical loan observations across similar borrowers. The bank then estimates, across defaults in the dataset, the fraction of exposure recovered (after collateral liquidation, legal costs, and delays). These estimates are embedded in the bank's credit pricing and risk management: a loan priced at LIBOR + 250 bps reflects the model's estimate of credit risk.

The regulatory IRB model uses these estimates directly. A bank's internal PD estimates (which drive pricing and risk management) are validated by regulators and then used to set risk weights. If the bank's mortgage model says prime mortgages have a 0.5% PD, the regulator approves this, and the risk weight is computed from 0.5% PD and the bank's estimated LGD (say, 25%). The formula is standardized (it appears in Basel III), but the inputs (PD, LGD) are bank-specific and hard-won.

## Regulatory approval and validation

A bank cannot simply declare its own PD and LGD estimates and reduce capital. The process is adversarial and lengthy. A large bank submits an IRB application for a given asset class (mortgages, corporates, retail, etc.) that documents the model methodology, data used, parameter estimates, backtesting results, and governance structure. Regulators (the Federal Reserve, the OCC, the ECB) spend months or years reviewing the submission. They demand:

- Backtesting: Do actual default rates match model predictions? A model that consistently predicts 0.5% default but observes 1.5% is overoptimistic and will be rejected or revised.
- Out-of-sample testing: Does the model work on data it was not trained on?
- Stress tests: How do estimates hold up under adverse scenarios (recessions, sector shocks)?
- Data quality: Are the historical data points reliable, or contaminated by changes in origination or servicing practices?

Only after approval can the bank use the model for regulatory capital. Approval is conditional: if the bank's actual defaults later deviate significantly from predictions, the regulator can revoke approval or impose additional capital add-ons. This ongoing validation is resource-intensive but necessary.

## Model risk and gaming

IRB introduces a treacherous trade-off: model risk. A bank's estimates are only as good as its data and methodology. Many banks have historical datasets spanning only one or two full economic cycles. In a boom, default rates are low, and models trained on boom and recovery data will underestimate risk in a recession. The 2008 crisis exposed this sharply: mortgage models trained on 2000–2006 data—a period of historically low defaults, rising home prices, and lax lending—predicted very low default rates and LGDs. When the housing market collapsed, actual defaults and losses were multiples of model predictions. Banks had approved IRB parameters that looked prudent ex-ante but proved catastrophically optimistic ex-post.

Banks also face incentives to game the models. If a corporate borrower is on the cusp of IRB-eligible status, a bank might be tempted to adjust the loan characteristics, collateral valuations, or recovery assumptions to get it classified in a lower-PD bucket. Regulators know this and impose tight governance: credit decisions must be made independently of capital calculations, models must be reviewed by an internal validation function (not the business unit), and any changes to models must be documented and approved by risk management and the board.

The opacity of IRB models is also a vulnerability. Unlike the standardized approach, where all banks use the same 100% weight for unrated corporates, IRB models are proprietary. Two banks lending to the same borrower might assign different risk weights, making cross-bank comparisons opaque. Regulators cannot easily tell whether a bank is truly managing risk better or just has a more lenient model. This is one reason why Basel III introduced a **leverage ratio** (total assets, unweighted) as a backstop and now imposes floors: IRB capital cannot fall more than 30% below standardized approach capital.

## The tension between accuracy and prudence

IRB proponents argue that it aligns capital with genuine risk, allowing well-managed banks to hold less capital and deploy it more productively. A bank with strong underwriting and low default rates should not be penalized with standardized-approach capital. IRB critics counter that model risk is real, that banks are optimistically biased, and that the consistency gains from standardized approaches are lost when each bank uses its own model.

The regulatory consensus post-2008 has shifted toward skepticism of IRB flexibility. Many regulators have tightened standards, imposed strict floors, and required regular recalibration of parameters. The UK PRA initially pushed back against IRB approvals in the aftermath of the crisis. The Basel Committee itself has discussed whether to reduce reliance on IRB and shift more capital calculations back to standardized approaches. Yet IRB remains embedded in Basel III; large banks still use it; and regulators grudgingly maintain it because the alternative—a one-size-fits-all standardized approach that might stifle lending to legitimate low-risk borrowers—carries its own costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Risk-Weighted Assets](/risk-weighted-assets/) — the output of IRB models applied to set the capital ratio denominator
- [Capital Adequacy](/capital-adequacy/) — the regulatory framework IRB sits within
- [Countercyclical Capital Buffer](/countercyclical-capital-buffer/) — a macroprudential overlay on IRB-derived capital
- [G-SIB Surcharge](/g-sib-surcharge/) — an additional capital requirement for systemically important banks
- [Credit Risk](/credit-risk/) — the underlying risk IRB models aim to quantify
- [Stress Testing](/stress-testing/) — the tool regulators use to validate IRB models under adverse scenarios

### Wider context

- [Basel III](/capital-adequacy/) — the international accord establishing IRB rules
- [Federal Reserve](/federal-reserve/) — regulator approving IRB applications in the US
- [Probability of Default](/credit-risk/) — a core input to IRB models
- [Loss-Given-Default](/credit-risk/) — another core input
- [Model Risk](/operational-risk/) — the broader concept of risks from flawed or gamed models

</div>

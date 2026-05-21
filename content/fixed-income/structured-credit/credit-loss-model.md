---
title: "Credit Loss Model"
description: "A quantitative framework that estimates the probability and severity of loan defaults in a structured credit pool, used to price tranches and assess credit risk."
---

*Credit loss modeling is the mathematical spine of structured credit. A securitization issuer cannot simply guess how many mortgages in a pool will default or how much will be recovered from foreclosure. Rating agencies cannot assign tranches AAA ratings without modeling. Investors cannot rationally price ABS without estimating losses. Credit loss models translate historical default data, borrower characteristics, and economic conditions into forecasts of how much collateral will actually be recovered.*

## The three components of loss

Every credit loss model breaks default and loss into three pieces:

- **Probability of default (PD)**: What is the likelihood that a borrower will default within a given period (typically annual)?
- **Loss given default (LGD)**: If the borrower defaults, what fraction of the loan balance will the lender lose after recovery efforts?
- **Exposure at default (EAD)**: How much is the borrower's outstanding balance at the time of default?

Expected loss (EL) is then: **EL = PD × LGD × EAD**.

For a mortgage pool: if the average PD is 1% (1 in 100 mortgages default annually), LGD is 40% (lender recovers 60% through foreclosure and sale), and average EAD is $300,000, then expected loss per loan is 0.01 × 0.4 × $300,000 = $1,200. Across 1,000 loans, that is $1.2 million in expected losses.

## Estimating PD: historical and empirical methods

Probability of default is typically estimated from historical data. A bank looks back 10 years and calculates: of all mortgages originated, what fraction defaulted within 12 months? Within 36 months? Within the loan's life?

But PD is not constant. It depends on:

- **Borrower credit quality**: Mortgages to borrowers with 750+ FICO scores have lower PD than mortgages to borrowers with 620 FICO.
- **Loan characteristics**: Lower LTV mortgages (higher equity cushion) have lower PD.
- **Macroeconomic conditions**: Unemployment spikes raise PD. Home prices falling raise PD (negative equity reduces borrower incentive to pay).
- **Loan age**: New mortgages have lower PD than seasoned mortgages (the risky borrowers have already defaulted).

Sophisticated models use logistic regression or machine learning to predict PD as a function of borrower and loan characteristics. A model might estimate:

`PD = 0.5% × (FICO 750 baseline) × 1.2 (unemployment at 6% vs. 4%) × 1.5 (negative equity) × 0.8 (seasoned loan)`

Resulting PD = 0.72%.

## LGD estimation: recovery rates

Loss given default depends on how much can be recovered from a defaulted loan. For mortgages:

- The lender forecloses and sells the property.
- Some properties sell for their appraised value; others sell at a discount (distressed sales, market conditions).
- Foreclosure costs (legal, property maintenance, realtor commissions) reduce proceeds.

Typical mortgage LGD is 30–60%, meaning lenders recover 40–70% of unpaid principal. In strong real-estate markets, LGD is lower (more recovery). In weak markets (negative equity, distressed sales), LGD is higher (less recovery).

Historical LGD is estimated by looking at defaulted mortgages: what was the outstanding balance, and how much did the lender recover in total? The difference is the loss.

For credit cards, LGD is higher (often 80–100%)—there is no collateral to recover, the lender writes off the balance. For auto loans, LGD is lower (20–40%)—the car is repossessed and sold.

## EAD: exposure at the time of default

EAD is the outstanding balance at default. For mortgages, EAD is the principal balance; for credit cards, it is the outstanding balance at time of default. For lines of credit, EAD includes both drawn and undrawn portions (a draw might occur at default).

EAD is important because a borrower might have $200,000 in outstanding mortgage principal but default only after prepaying $50,000. The EAD is $200,000, not $250,000.

## Putting it together: portfolio-level loss distributions

To model losses in a securitization pool, the model applies PD, LGD, and EAD to each loan (or a representative sample), then sums across the pool. But there is a key complication: defaults are correlated. When the economy weakens, many borrowers default simultaneously, not independently.

A naive model that treats defaults as independent (binomial distribution) would underestimate the probability of severe losses. If the pool has 1,000 loans and each has 1% PD, the binomial distribution says losses stay close to 10 loans defaulting. But in a severe recession, 50–100 loans might default together, a 5–10× tail risk.

Modern models account for correlation. A common approach is **asset correlation modeling**, where default probability depends on both idiosyncratic factors (borrower-specific) and systematic factors (economy-wide). If unemployment spikes (systematic), all borrowers' PDs rise together.

The result is a loss distribution with fat tails. A model predicts:

- Expected loss: 1%
- 95th percentile loss (1 in 20 chance): 3%
- 99.9th percentile loss (1 in 1,000 chance): 6%

This distribution is then used to set tranches. A senior tranche is sized so that losses at the 99.9th percentile do not breach it. A mezzanine tranche is sized for the 95th percentile. Equity absorbs everything below.

## Rating agencies' standard models

The "big three" rating agencies (Moody's, S&P, Fitch) each have proprietary credit loss models for mortgages, credit cards, auto loans, and corporate loans. These models are the baseline for assigning ratings.

Broadly, they:

1. Estimate PD by borrower segment (FICO, LTV, loan age, geography, etc.).
2. Estimate LGD by property type and market condition.
3. Combine using correlation assumptions (often 20–30% correlation).
4. Run the model across stress scenarios (unemployment rises to 8%, home prices fall 25%).
5. Calculate the loss percentile that rating targets (AAA = 0.03%, BBB = 1%).
6. Size tranches accordingly.

Post-2008, agencies increased their loss assumptions materially. Pre-crisis, many models assumed mortgage defaults of 3–5%. Post-crisis, 8–10% is more common for stressed scenarios.

## Alternative models: empirical simulation

Some investors build their own credit loss models using loan-level data (now publicly available for many securitizations). These models:

- Ingest loan characteristics (FICO, LTV, DTI, state, origination date, documentation level).
- Use historical default experience from the same time period and geography to estimate PD.
- Estimate LGD from comparable property sales and foreclosure data.
- Run Monte Carlo simulation to generate loss distributions.
- Stress the model: if unemployment hits 10%, default rates increase 5x.

An investor model might produce: "This deal has a 5% expected loss, 15% at the 95th percentile, and 25% at the 99th percentile." The investor then values tranches accordingly. A senior tranche with 30% overcollateralization might be safe under this model. A mezzanine with 5% subordination is risky.

## Model risk and the 2008 crisis

The 2008 crisis revealed model risk in stark terms. Pre-crisis models assumed:

- Mortgage defaults correlated at 15–20%.
- Home prices never fell nationally (they had not since the 1930s).
- Loan-level characteristics (FICO, LTV) were sufficient to estimate PD.

None of these held in 2008. Defaults correlated at 50%+. Home prices fell 30%+. Stated income and low-documentation mortgages had default rates far above prime-loan models predicted.

As a result:

- Rated AAA tranches took losses.
- Models that assumed independent defaults were blindsided by co-movement.
- Leverage in securitizations amplified losses (a 2% loss in collateral wiped out 50% in a mezzanine tranche).

Modern models incorporate these lessons: higher correlation assumptions, stress tests that include national home-price declines, and skepticism of loan-level characteristics that proved unreliable in crisis.

## Model uncertainty and spreads

Even the best models are uncertain. Different rating agencies' models produce different loss predictions. Investors' proprietary models differ from agency models. This uncertainty is priced into spreads.

A deal that all models agree is safe trades at tight spreads (low yield). A deal where models diverge widely or where model inputs are uncertain trades at wider spreads (higher yield). The extra spread compensates investors for model risk.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/credit-rating/">Credit Rating</a> — ratings are assigned based on credit loss models.</li>
<li><a href="/wiki/probability-of-default/">Probability of Default</a> — a key input to credit loss models.</li>
<li><a href="/wiki/loss-given-default/">Loss Given Default</a> — another key input.</li>
<li><a href="/wiki/securitization/">Securitization</a> — credit loss models are used to structure deals.</li>
<li><a href="/wiki/tranche/">Tranche</a> — tranche sizing depends on modeled losses.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/structured-finance/">Structured Finance</a> — models are the engineering foundation.</li>
<li><a href="/wiki/model-risk/">Model Risk</a> — the risk that models are wrong.</li>
<li><a href="/wiki/stress-testing/">Stress Testing</a> — how credit loss models are validated.</li>
</ul>
</div>

---
title: "Value-at-Risk"
description: "Value-at-risk (VaR) is a measure of the maximum loss a portfolio is expected to suffer over a given time horizon at a specified confidence level, widely used in risk management and financial regulation."
keywords:
  - value-at-risk
  - VaR
  - risk measure
  - tail loss
  - confidence level
image: "/svg/risk.svg"
---

*Value-at-risk (VaR) is a statistical measure estimating the maximum loss a portfolio could experience over a defined period (e.g., one day) at a specified confidence level (e.g., 95% or 99%). It answers the question: "What is the worst loss I can expect with X% confidence over Y days?" Despite its limitations, VaR is the dominant risk metric in finance.*

<div class="wiki-hatnote">

This entry covers VaR measurement and use. For the average loss in tail events beyond VaR, see [expected-shortfall](/expected-shortfall); for risks VaR misses, see [tail-risk](/tail-risk) and [model-risk](/model-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Value-at-Risk — key facts</div>

<img src="/svg/risk.svg" alt="A portfolio value graph with a downside threshold marked at 95% confidence" />

<div class="wiki-infobox-caption">VaR is the loss threshold at a given confidence level.</div>

|   |   |
|---|---|
| **What it is** | Maximum expected loss at a confidence level over a time period |
| **Example** | 1-day VaR of $1M at 99% confidence = 1% chance of losing >$1M in one day |
| **Common parameters** | 1 day, 10 days; 95% or 99% confidence |
| **Calculation methods** | Parametric (normal distribution); historical; Monte Carlo |
| **Regulatory use** | Basel capital standards require banks to calculate VaR |
| **Strengths** | Simple; intuitive; widely understood; easy to compare across portfolios |
| **Weaknesses** | Misses tail risk; underestimates during crises; assumes stable parameters |

</aside>

## Understanding VaR with an example

A portfolio manager calculates a 1-day VaR of $2 million at 99% confidence. This means:

- There is a 1% chance (roughly 2.5 trading days per year) that the portfolio loses more than $2 million in a single day.
- There is a 99% chance that the portfolio loses less than $2 million in a single day.

This is useful: the manager knows that on a typical bad day, the loss is at most $2M. On really bad days (the 1% tail), the loss could be much worse — $5M, $10M, or more. But most days are not really bad, and VaR captures the threshold for the typical bad day.

## Three methods for calculating VaR

**Parametric VaR (Variance-Covariance):**
Assume returns follow a normal distribution with a mean and standard deviation. Calculate the percentile of the distribution corresponding to the confidence level. A portfolio with daily returns averaging 0.05% and standard deviation of 1% has a 1-day 95% VaR of roughly 1.65 standard deviations below the mean = 1.65%. For a $100M portfolio, this is $1.65M.

Advantage: Fast, simple.
Disadvantage: Assumes normal distribution; underestimates risk if returns have [fat tails](/fat-tail-risk).

**Historical VaR:**
Use historical returns directly. For 1-day 99% VaR, take the worst 1% of past daily returns and use that as the VaR. If the worst 1% of days over the past 5 years (1,000 trading days) had losses of $2.5M or worse, the 1-day 99% VaR is $2.5M.

Advantage: No distributional assumptions; reflects actual market behaviour.
Disadvantage: Assumes the past is representative of the future; misses new types of shocks; sparse data for extreme tail (1% of 1,000 days is only 10 days).

**Monte Carlo VaR:**
Simulate thousands or millions of possible future scenarios using models for price movements, correlations, and volatility. For each simulation, calculate portfolio loss. Use the worst 1% (for 99% confidence) as VaR.

Advantage: Flexible; can model complex instruments and non-linear relationships.
Disadvantage: Computationally intensive; depends on model assumptions; garbage in, garbage out.

## VaR in practice: where it succeeds and fails

VaR works well for:
- **Typical market conditions.** When markets are calm and correlations are stable, VaR estimates are reasonable.
- **Comparison.** VaR allows different portfolios to be compared on a common metric.
- **Regulatory communication.** Banks report VaR to regulators; it is a standard language.
- **Risk limits.** A trading desk might have a limit of "$10M daily VaR," which operationalizes risk management.

VaR fails:

- **Tail events.** VaR does not measure the size of the 1% tail loss. A portfolio with 1-day 99% VaR of $2M could lose $2M or $20M in that 1% tail; VaR does not distinguish.
- **Crisis periods.** VaR models fitted to calm periods underestimate risk when volatility spikes or correlations jump.
- **Stress scenarios.** VaR assumes the future is like the past. A new type of shock (a new kind of black swan) is not captured.
- **Fat tails.** Normal distribution assumption means VaR underestimates the probability of extreme losses.

## The limitations are well-known

The 2008 financial crisis showed that VaR was systematically too low. Banks held what they thought were safe portfolios with calculated VaRs of 2-3%, but actual losses in September-October 2008 exceeded VaR by 5-10x. This prompted regulators to supplement VaR with [expected-shortfall](/expected-shortfall) and [stress-testing](/stress-testing).

## Beyond VaR: [Expected-Shortfall](/expected-shortfall)

Recognizing VaR's shortcomings, regulators now require banks to also calculate [expected-shortfall](/expected-shortfall) (ES), also called conditional VaR or CVaR. ES measures the *average* loss in the tail — the average loss on the worst 1% of days. This directly addresses VaR's main weakness: not measuring the size of tail losses.

## See also

<div class="wiki-seealso">

### Closely related

- [Expected-shortfall](/expected-shortfall) — average loss in the tail
- [Conditional-value-at-risk](/conditional-value-at-risk) — synonym for expected-shortfall
- [Stress-testing](/stress-testing) — assesses losses under extreme scenarios
- [Scenario-analysis](/scenario-analysis) — structured assessment of specific outcomes
- [Tail-risk](/tail-risk) — risk of extreme losses beyond VaR

### Methodological variants

- [Parametric-var](/parametric-var) — using normal distribution
- [Historical-var](/historical-var) — using historical returns
- [Monte-carlo-var](/monte-carlo-var) — simulation-based

### Broader context

- [Model-risk](/model-risk) — VaR estimates depend on model assumptions
- [Basel capital](/basel-capital) — regulations use VaR and ES
- [Risk management](/value-at-risk) — VaR is foundational to modern risk management
- [Fat-tail-risk](/fat-tail-risk) — VaR underestimates due to fat tails
- [2008 financial crisis](/credit-risk) — exposed VaR limitations

</div>

---
title: "How to Calculate Value at Risk: A Simple Example"
description: "Walk through the three main VaR methods—historical simulation, variance-covariance, and Monte Carlo—with worked numerical examples."
keywords:
  - value at risk calculation
  - how to calculate VaR
  - historical simulation VaR
  - variance covariance method
  - monte carlo VaR
  - portfolio risk measurement
---

*Computing **value at risk** answers a single question: given a portfolio and a time horizon, what is the maximum loss I am likely to suffer at a given confidence level? If you hold a $1M portfolio and calculate a one-day 95% VaR of $50k, you are saying there is a 95% probability you will not lose more than $50k in a single day. The three main approaches—historical simulation, variance-covariance, and Monte Carlo—each make different assumptions and suit different scenarios.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Value at Risk Calculation — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">VaR quantifies tail-risk loss at a given confidence level; estimates depend heavily on method choice and market regime.</div>

|   |   |
|---|---|
| **Typical VaR levels** | 95% (5% tail loss) or 99% (1% tail loss); daily or 10-day horizon |
| **Historical simulation** | Uses past returns directly; assumes history repeats; best for simple portfolios |
| **Variance-covariance** | Assumes normal distribution; fast to compute; breaks in fat-tail markets |
| **Monte Carlo** | Simulates thousands of paths; flexible; computationally expensive |
| **Key limitation** | VaR ignores loss magnitude *beyond* the threshold; a $50k loss or $500k loss both breach the VaR |

</aside>

## The Three Methods Explained

All three VaR methods take the same inputs—a portfolio, historical returns or volatility, and a confidence level—but diverge in execution. Here's a small worked example using a $100k portfolio: 60% stocks (S&P 500 index) and 40% bonds (10-year Treasury).

### Historical Simulation

This is the most intuitive method: use actual past returns and see what the worst cases looked like.

**Setup**: Gather daily returns for both the stock and bond indices over the past 252 trading days (one year). Reweight the portfolio each day using the same allocation (60/40) and calculate daily portfolio returns.

**Hypothetical data** (first 10 days of daily returns):

| Day | S&P 500 return | Bond return | Portfolio return |
|---|---|---|---|
| 1 | +1.2% | +0.1% | +0.8% |
| 2 | -0.5% | +0.3% | -0.1% |
| 3 | +0.8% | -0.2% | +0.4% |
| 4 | -2.1% | +0.5% | -1.0% |
| 5 | +0.3% | -0.1% | +0.1% |
| ... | ... | ... | ... |
| 252 | -1.8% | +0.4% | -0.9% |

Compute 252 daily portfolio returns. Rank them from worst to best.

**Calculate 95% VaR**: At 95% confidence, the worst 5% of outcomes are excluded. Rank days from worst to best. The 5th worst day (since 5% × 252 ≈ 13 days) represents the threshold. If the 13th worst return was -1.8%, your portfolio would lose $1,800 (1.8% × $100k) on that day. **95% one-day VaR = $1,800.**

This means: in 95% of trading days, you will not lose more than $1,800. In the remaining 5%, you might.

**Pros**: No distributional assumptions; uses real price movements.
**Cons**: Limited by sample size (only 252 days of data); if a rare event didn't occur in the past year, VaR won't capture it; assumes future resembles past.

### Variance-Covariance Method

This parametric approach assumes returns follow a normal distribution. It uses only volatility and correlation, making it fast to compute.

**Setup**: Calculate the standard deviation (volatility) of daily returns for stocks and bonds, plus their correlation.

Suppose over the past year:
- S&P 500 daily volatility: 1.2%
- 10-year Treasury daily volatility: 0.35%
- Correlation between them: -0.15 (bonds and stocks move opposite on average)

**Calculate portfolio volatility** using the two-asset formula:

Portfolio σ = √[(w₁ × σ₁)² + (w₂ × σ₂)² + 2 × w₁ × w₂ × σ₁ × σ₂ × ρ]

Plug in weights (w₁ = 0.6, w₂ = 0.4), volatilities, and correlation:

σ_portfolio = √[(0.6 × 0.012)² + (0.4 × 0.0035)² + 2 × 0.6 × 0.4 × 0.012 × 0.0035 × (-0.15)]
            = √[5.18 × 10⁻⁵ + 1.96 × 10⁻⁶ − 3.02 × 10⁻⁶]
            = √[5.07 × 10⁻⁵]
            = 0.712% daily volatility

**Find the z-score** for 95% confidence. Under a normal distribution, 95% of outcomes fall within 1.645 standard deviations of the mean. Daily mean return is typically near zero, so:

VaR (95%, one day) = 1.645 × 0.712% × $100k = $1,174

**95% one-day VaR = $1,174.**

**Pros**: Fast; captures diversification benefit (negative correlation reduces portfolio volatility).
**Cons**: Assumes normal distribution; real returns have fat tails (extreme moves happen more often than normal distribution predicts); overstates safety in market stress.

### Monte Carlo Simulation

This method generates thousands of random future paths for each asset, respecting observed volatilities and correlations, then calculates outcomes.

**Setup**: 
1. Assume the same volatilities and correlation as variance-covariance.
2. For each Monte Carlo trial, generate a random daily return for stocks and bonds using those parameters.
3. Combine them into a portfolio return.
4. Repeat 10,000 times (or more).

**Simplified illustration** (10 simulations for clarity; real MC uses 10,000+):

| Trial | Simulated stock return | Simulated bond return | Portfolio return |
|---|---|---|---|
| 1 | +0.8% | -0.1% | +0.5% |
| 2 | -1.5% | +0.6% | -0.6% |
| 3 | +0.2% | -0.3% | +0.06% |
| 4 | -2.3% | +0.8% | -1.2% |
| 5 | +1.1% | +0.2% | +0.7% |
| 6 | -0.9% | -0.2% | -0.6% |
| 7 | +0.3% | +0.05% | +0.2% |
| 8 | -1.7% | +0.4% | -0.9% |
| 9 | +0.6% | -0.15% | +0.4% |
| 10 | -2.8% | +0.5% | -1.6% |

Rank the 10,000 simulated outcomes. The worst 5% (500 trials) define the 95% VaR. If the 500th worst return was -1.3%, then **95% one-day VaR = $1,300.**

**Pros**: Flexible (can model non-normal distributions, options, tail dependencies); captures correlations in stress; no parametric assumptions required if calibrated to observed tails.
**Cons**: Computationally intensive; depends on the random seed and number of simulations; can produce different results across runs.

## Comparing Results and Interpreting VaR

Our three methods on the same $100k 60/40 portfolio:

| Method | 95% one-day VaR |
|---|---|
| Historical simulation | $1,800 |
| Variance-covariance | $1,174 |
| Monte Carlo | $1,300 |

The variance-covariance estimate is lowest because it assumes perfect normal distributions and misses tail risk. Historical simulation is highest because it encountered a particularly bad day in the past year. Monte Carlo sits in the middle.

**Interpretation**: A trader holding this portfolio knows that on 95 out of 100 trading days, the loss will be less than $1,300–$1,800 (depending on method). On the 5th worst day, the loss could exceed that—possibly by a lot. This is the key VaR limitation: it tells you the threshold, not the magnitude beyond it.

## Time Horizons and Scaling

So far, we've calculated one-day VaR. Risk managers often report 10-day VaR (useful for longer trading positions) or longer.

A rough scaling rule: **VaR over N days ≈ one-day VaR × √N.**

So if one-day 95% VaR is $1,300, then:
- 5-day 95% VaR ≈ $1,300 × √5 ≈ $2,905
- 10-day 95% VaR ≈ $1,300 × √10 ≈ $4,111

This assumes returns are independent (no autocorrelation); in practice, market shocks cluster, so 10-day loss during a crisis can exceed the √10 scaling. Still, the scaling is useful for rough estimates.

## Practical Applications and Limitations

**Bank regulators** require VaR reporting under [Basel III](/capital-adequacy/). Major banks compute daily VaR on their trading portfolios and set aside capital to cover potential losses.

**Risk committees** use VaR to set position limits. A hedge fund might decree: "No trader may hold a position with > $500k 95% one-day VaR."

**Backtesting**: A risk manager compares actual daily losses to forecasted VaR. If 95% VaR is $1,300 but losses exceed $1,300 more than 5% of the time, the model is miscalibrated and needs revision.

**The critical flaw**: VaR does not answer "How bad could it be?" It only answers "What is the threshold?" During the 2008 financial crisis and March 2020 COVID crash, many portfolios experienced losses 10–50x larger than their VaR estimates. VaR models were trained on calm markets and failed to predict stress tail correlations (all assets fell together).

For that reason, risk managers also use **[conditional VaR](/conditional-value-at-risk/)** (or expected shortfall), which estimates the *average* loss in the worst 5% of cases, not just the 5th percentile. A portfolio might have 95% one-day VaR of $1,300 but conditional VaR of $2,500 (meaning, on the 5% worst days, the average loss is $2,500).

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — VaR framework and interpretation
- [Conditional Value at Risk](/conditional-value-at-risk/) — Expected shortfall; average loss in tail events
- [Volatility](/historical-volatility/) — Standard deviation inputs to VaR models
- Correlation — Asset relationships affecting portfolio risk
- [Stress Testing](/stress-testing/) — Complement to VaR; tests extreme scenarios
- [Risk Weighted Assets](/risk-weighted-assets/) — Basel III capital rules based on VaR and stress tests

### Wider context

- Portfolio Risk — Diversification and concentration effects
- [Capital Adequacy](/capital-adequacy/) — Regulatory VaR requirements for banks
- [Tail Risk](/tail-risk/) — Extreme events beyond VaR thresholds
- [Loss Aversion](/loss-aversion/) — Behavioral response to perceived portfolio risk
- Backtesting — Validating VaR models against realized losses

</div>

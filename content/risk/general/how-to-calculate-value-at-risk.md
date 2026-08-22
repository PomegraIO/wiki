---
title: "How to Calculate Value at Risk (VaR)"
description: "How to calculate Value at Risk: historical simulation, variance-covariance, and Monte Carlo methods with worked examples."
keywords:
  - value at risk calculation
  - var methodology
  - historical simulation var
  - monte carlo simulation
  - variance covariance var
image: /svg/risk.svg
---

*[Value at Risk](/value-at-risk/)) (VaR) measures the maximum loss a portfolio could suffer within a given time horizon, at a specified confidence level. The three standard calculation methods — historical simulation, variance-covariance, and Monte Carlo — differ in speed, assumptions, and accuracy. Each produces the same answer to a different question, depending on which method matches your data and model.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VaR Calculation Methods — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk topics." />

<div class="wiki-infobox-caption">Three approaches, each with strengths: speed, realism, or tail sensitivity.</div>

|   |   |
|---|---|
| **Historical simulation** | Rank actual past returns; no distribution assumption; handles tail risk well |
| **Variance-covariance** | Assume normal returns; matrix algebra; fastest, smoothest |
| **Monte Carlo** | Simulate thousands of random paths; flexible; computationally intense |
| **Common confidence level** | 95% (5% loss tail) or 99% (1% loss tail) |
| **Time horizon** | 1-day, 10-day, or longer; longer horizon = larger VaR |
| **Output** | Dollar amount or percentage: "95% VaR is $2.5M loss over 10 days" |

</aside>

## The VaR definition and setup

Before calculating, fix two parameters: the confidence level and the time horizon. A portfolio manager might ask: "What is the worst loss we could see 95% of the time, over a one-day holding period?" Or: "At 99% confidence, over 10 days, what is our maximum expected loss?"

The answers are different. VaR at 95% confidence is smaller than VaR at 99% (the 99% tail is wilder). VaR over one day is smaller than VaR over 10 days (more time = more variance). The formula does not change; only the inputs change.

Formally, VaR is the inverse of the cumulative loss distribution. If you can model the probability of losses of each magnitude, the 95% confidence VaR is the loss level below which you fall 95% of the time — or above which you fall 5% of the time. The choice of 95% vs 99% is a policy call; 95% is common for internal risk management, while 99% features in some regulatory requirements.

## Method 1: Historical simulation

Historical simulation is conceptually simplest: rank the past returns of your portfolio, and read off the worst loss at your target confidence level.

### Worked example: historical simulation

Suppose a portfolio returned the following daily percentage changes over the past 100 trading days:

| Rank | Daily return | Rank | Daily return |
|------|--------------|------|--------------|
| 1 (best) | +2.3% | 51 | +0.1% |
| 2 | +1.8% | 52 | −0.2% |
| ... | ... | 75 | −1.1% |
| 25 | +0.5% | 95 | −2.8% |
| 50 | 0.0% | 96 | −3.2% |
| | | 97 | −3.5% |
| | | 98 | −4.1% |
| | | 99 | −4.6% |
| | | 100 (worst) | −5.2% |

To calculate 95% VaR (the loss you exceed 5% of the time), find the 5th percentile of losses. With 100 observations, the 5th percentile is approximately the 5th worst return. Looking at the sorted list:

- 100th worst (−5.2%) is the absolute worst.
- 5th worst is approximately −2.8%.

So 95% VaR ≈ 2.8% of the portfolio value. If your portfolio is $10 million, the 95% one-day VaR is about $280,000.

For 99% VaR (the loss you exceed 1% of the time), the 1st worst return is roughly the only observation in the extreme tail:

- 99% VaR ≈ 5.2% of portfolio value, or $520,000 on a $10 million portfolio.

### Strengths and limitations

Historical simulation has two major advantages:

1. **No distributional assumption.** It uses what actually happened, not a model. If returns are non-normal (fat tails, skew), the method captures that.
2. **Tail sensitivity.** Extreme events in history are weighted equally to normal days, preserving tail risk.

The main limitation: **you need many observations to estimate the extreme tail credibly.** With only 100 days of data, the 99% VaR is the single worst day — unstable and likely to shift sharply when new data arrives. Risk managers often use one to five years of historical data (250–1,250 trading days) to get smoother tail estimates.

A second limitation is **structural breaks.** If your portfolio manager changed strategy, or markets underwent a regime shift, old data may not predict future losses. A historical simulation trained on pre-2008 data, for instance, underestimated losses in 2008 itself.

## Method 2: Variance-covariance (parametric) VaR

The variance-covariance method assumes returns follow a normal (Gaussian) distribution. Given that assumption, you need only two inputs: the mean return and the [standard deviation](/volatility-smile/)) (volatility).

### Worked example: variance-covariance

Suppose your portfolio has:
- Mean daily return: 0.05%
- Standard deviation (volatility): 1.2% per day
- Portfolio value: $10 million

For a normal distribution, the 95% confidence level corresponds to a z-score of −1.645 (the point 1.645 standard deviations below the mean). The 99% confidence level corresponds to z = −2.326.

**95% VaR:**
Loss = Mean − (z × Volatility)
Loss = 0.05% − (−1.645 × 1.2%)
Loss = 0.05% + 1.974% = 2.024% of portfolio value
Dollar VaR = 0.02024 × $10 million = $202,400

**99% VaR:**
Loss = 0.05% − (−2.326 × 1.2%)
Loss = 0.05% + 2.791% = 2.841% of portfolio value
Dollar VaR = 0.02841 × $10 million = $284,100

### Multi-asset portfolios

For a portfolio holding multiple stocks or bonds, the variance-covariance method uses the correlation matrix):

VaR = Portfolio Value × (Zα × √(w^T × Cov × w))

where:
- Zα is the z-score for your confidence level (−1.645 for 95%, −2.326 for 99%).
- w is the weight vector (what fraction of the portfolio is in each asset).
- Cov is the covariance matrix (correlations and individual volatilities).

The square root of (w^T × Cov × w) is the portfolio volatility. Diversification — low correlations — reduces this volatility, lowering VaR.

### Strengths and limitations

Variance-covariance is **fast and elegant.** You can compute it in a spreadsheet. It also scales well to large portfolios: a matrix multiplication is cheaper than simulating 10,000 paths.

The major limitation is the **normal distribution assumption.** Real market returns have fat tails (extreme events more often than normal theory predicts) and skew. Variance-covariance VaR systematically underestimates tail losses. In March 2020, for instance, variance-covariance models predicted far smaller losses than actually occurred.

A second issue: **option [gamma](/gamma/))**. If your portfolio holds options or other nonlinear instruments, return distributions are non-normal even if underlying asset returns are normal. Variance-covariance breaks down.

## Method 3: Monte Carlo simulation

Monte Carlo simulation generates thousands of random future portfolio values, each following a specified probability model. The method is flexible and realistic but computationally demanding.

### Worked example: Monte Carlo

Suppose your $10 million portfolio consists of:
- $6 million in a stock with 15% annual volatility and 0.08% daily mean.
- $4 million in a bond with 3% annual volatility and 0.02% daily mean.
- Correlation between stock and bond: 0.2.

You specify the model (mean, volatility, correlation), then run 10,000 simulations. Each simulation:

1. Draw a random normal number for the stock return: say −1.2%.
2. Draw a random normal number for the bond return, respecting the 0.2 correlation: say +0.3%.
3. Compute portfolio value: 6M × (1 − 0.012) + 4M × (1 + 0.003) = $9,951,200.
4. Compute loss: $10M − $9,951,200 = $48,800.

Repeat 10,000 times. Sort the 10,000 losses. The 95% VaR is the loss at the 500th worst simulation (the 5th percentile); the 99% VaR is the loss at the 100th worst simulation (the 1st percentile).

| Simulation | Loss | Percentile |
|-----------|------|-----------|
| 1 (best) | −$120,000 | 100% |
| 500 | $320,000 | 95% |
| 950 | $580,000 | 50% |
| 9,900 | $1,200,000 | 5% |
| 10,000 (worst) | $1,650,000 | 1% |

So 95% VaR ≈ $320,000; 99% VaR ≈ $1,200,000.

### Strengths and limitations

Monte Carlo is **highly flexible.** You can model non-normal distributions, option payoffs, jump risks, and regime shifts. It is the preferred method for portfolios with derivatives or complex payoff structures.

The downside is **computational cost and randomness.** A large portfolio simulated with 10,000 paths takes minutes or hours. The result also includes Monte Carlo error — run the simulation twice and you get slightly different answers because the random draws differ. To reduce error, you increase the number of paths, which takes more time.

Also, Monte Carlo is only as good as the model you assume. If you assume normal returns and the true distribution is fat-tailed, 10,000 simulated paths may still miss extreme events.

## Comparing the three methods

For the same portfolio and confidence level:

| Aspect | Historical | Variance-Covariance | Monte Carlo |
|--------|-----------|-------------------|-------------|
| **Assumptions** | None (uses data) | Normal returns | Specified model |
| **Speed** | Medium (sorting) | Very fast | Slow |
| **Tail accuracy** | Good (if enough data) | Poor (underestimates) | Good (if model correct) |
| **Data requirement** | 1–5 years | Correlations + volatilities | Correlations + volatilities |
| **Option handling** | Good | Poor | Excellent |
| **Regime change risk** | High | Medium | Medium |

## Using VaR in practice

VaR is a summary statistic — useful but incomplete. A portfolio with 95% VaR of $1 million tells you that 5% of the time you lose more than $1 million, but not how much more. [Conditional Value at Risk](/value-at-risk/)) (CVaR or expected shortfall) extends VaR by computing the *expected* loss in that worst 5% tail — often 50–100% larger than VaR itself.

Regulators and boards mandate VaR reporting for [market risk](/market-risk/)) limits. Risk managers also use it to size [hedges](/derivatives-hedging/)), allocate [capital](/equity-financing/)), and stress-test portfolios. But VaR should always be paired with scenario analysis, historical backtesting, and expert judgment.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the concept and uses of VaR in portfolio management
- [Conditional Value at Risk](/value-at-risk/) — the average loss in the tail beyond VaR
- [Historical Volatility](/historical-volatility/) — the building block for variance-covariance VaR
- [Correlation](/market-risk/) — how asset pairs move together, central to multi-asset VaR
- [Monte Carlo Simulation](/sensitivity-analysis-valuation/) — the simulation technique behind one method
- [Market Risk](/market-risk/) — the broad risk category that VaR measures

### Wider context

- [Risk Management](/market-risk/) — the discipline that uses VaR for decision-making
- [Stress Testing](/stress-testing/) — complementary to VaR for extreme scenarios
- [Derivatives Hedging](/derivatives-hedging/) — sizing hedges often requires VaR
- [Capital Adequacy](/capital-adequacy/) — regulatory frameworks that reference VaR

</div>

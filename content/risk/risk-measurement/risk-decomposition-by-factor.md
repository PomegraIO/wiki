---
title: "Risk Decomposition by Factor in Multi-Factor Models"
description: "How a portfolio's total variance is attributed to individual risk factors using factor model algebra, revealing the true drivers of portfolio risk."
keywords:
  - risk decomposition by factor
  - factor exposure risk
  - multi-factor models
  - portfolio variance attribution
image: /svg/risk.svg
---

*A **risk decomposition by factor** breaks down a portfolio's total variance into contributions from each systematic risk source—[market beta](/beta/), [size factor](/factor-investing/), value exposure, momentum, interest rates—showing which risks actually drive losses. This decomposition is the bridge between a portfolio's raw [volatility](/historical-volatility/) and the deeper question of where that volatility comes from, and it is essential for understanding whether you are being compensated for the risks you actually hold.*

## The Basic Setup: Return as a Sum of Factor Exposures

Start with a linear factor model of returns. A portfolio's total return can be written as:

$$R_{\text{portfolio}} = \alpha + \beta_1 F_1 + \beta_2 F_2 + \ldots + \beta_k F_k + \epsilon$$

where:

- $F_1, F_2, \ldots, F_k$ are the returns of $k$ risk factors (market excess return, size, value, etc.).
- $\beta_1, \beta_2, \ldots, \beta_k$ are the portfolio's exposures (sensitivities) to each factor.
- $\alpha$ is the unexplained return (alpha, if any).
- $\epsilon$ is idiosyncratic noise uncorrelated with the factors.

For example, a large-cap growth portfolio might have a [market beta](/beta/) of 1.1, a size factor loading of −0.3 (tilt away from small caps), and a value factor loading of −0.5 (tilt away from value).

## Decomposing Total Variance

If we assume the factors are not perfectly correlated (a realistic assumption), we can write the portfolio's total variance as:

$$\text{Var}(R_{\text{portfolio}}) = \sum_{i=1}^{k} \beta_i^2 \text{Var}(F_i) + 2 \sum_{i < j} \beta_i \beta_j \text{Cov}(F_i, F_j) + \text{Var}(\epsilon)$$

This breaks into three pieces:

1. **Own-factor variance**: $\sum_{i=1}^{k} \beta_i^2 \text{Var}(F_i)$—the variance each factor contributes on its own.
2. **Cross-factor covariance**: $2 \sum_{i < j} \beta_i \beta_j \text{Cov}(F_i, F_j)$—how factors move together and amplify or dampen total variance.
3. **Idiosyncratic variance**: $\text{Var}(\epsilon)$—the noise that cannot be explained by the factors.

### A Concrete Example

Suppose a portfolio holds:

- Exposure to the market factor (beta = 1.2)
- Exposure to a "momentum" factor (beta = 0.4)

Assume:
- Market factor variance = 0.16 (annual volatility ≈ 40%)
- Momentum factor variance = 0.04 (annual volatility ≈ 20%)
- Correlation between market and momentum = 0.3
- Idiosyncratic variance = 0.01

Then:

$$\text{Var}(R) = (1.2)^2 (0.16) + (0.4)^2 (0.04) + 2(1.2)(0.4)(0.3)(0.16 \times 0.04)^{0.5} + 0.01$$

$$= 0.2304 + 0.0064 + 2(0.48)(0.3)(0.08) + 0.01 = 0.2304 + 0.0064 + 0.0115 + 0.01 \approx 0.2583$$

Portfolio volatility ≈ 50.8%. Breaking this down: the market contributes the bulk (about 89%), momentum adds a small piece (about 2.5%), their covariance adds about 4.4%, and idiosyncratic risk adds about 3.9%.

## Why Cross-Factor Covariance Matters

The cross-term is critical and often overlooked. Two factors might each have low volatility, but if they move together strongly in crises, they amplify portfolio risk. Conversely, if they are negatively correlated, they diversify each other.

For instance, during equity market selloffs, both [market beta](/beta/) and value factor returns often plummet (value underperforms growth). A portfolio long both amplifies losses in downturns—the covariance term is positive and large. A portfolio long market and short bond yield changes might benefit from negative covariance, since equities and bonds often move in opposite directions.

This is why understanding correlation across factors is as important as understanding individual factor volatilities.

## Practical Applications: Factor Risk Reporting

Asset managers and risk teams use factor decompositions to answer questions like:

- **What is driving our losses?** If a portfolio is down 5% and the [market beta](/beta/) is 1.2, then about 4% of the loss is from market moves; the rest comes from [idiosyncratic risk](/idiosyncratic-risk/) or other factors.
- **Are we being paid for our risks?** If the momentum factor exposure contributes 20% of variance but has earned zero excess return over 3 years, that is wasted risk.
- **How much can we reduce variance by changing exposures?** Reducing beta from 1.2 to 1.0 cuts own-market variance by 14%, but it also reduces the covariance contributions, so the total variance reduction is smaller than a naive calculation would suggest.

## Factor Correlation During Crises

A subtle but critical feature: factor correlations are not constant. During calm markets, size and momentum factors might have low correlation; during market crashes, they both collapse toward the market, raising their joint contribution to losses.

This is why a decomposition computed on 10 years of calm data can underestimate tail risk. Risk managers often stress-test by assuming correlations rise during downturns or by examining historical periods of stress separately.

## The Role of Idiosyncratic Risk

The final component, $\text{Var}(\epsilon)$, is the part of portfolio return not explained by the factors. For a [diversified](/diversification/) portfolio of many stocks, idiosyncratic risk should be small (a few percent of total variance) because it averages out. For a concentrated position (e.g., 10 stocks, or a single security with low factor correlation]), idiosyncratic risk can dominate, suggesting that stock-picking or company-specific bets drive returns more than systematic [factor exposure](/factor-investing/).

Minimizing idiosyncratic risk is a key goal of [passive index fund](/index-fund/) strategies, which aim to be pure factor bets.

## Limitations and Model Choice

The quality of the decomposition depends entirely on the choice of factors:

- Too few factors (e.g., only market beta) and you miss important risk sources; idiosyncratic variance inflates.
- Too many factors and you overfit, double-count risk, or introduce factors with weak statistical significance.
- Factors must be economically meaningful (e.g., size, value, momentum) and tradeable; they should not be statistical artifacts.

Common factor models include the [Fama-French 3-factor model](/factor-investing/) (market, size, value), the 5-factor model (adding profitability and investment), and bespoke models for fixed-income (duration, credit spread) or alternatives (illiquidity premium).

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — the systematic risk sensitivity to the market factor.
- [Factor investing](/factor-investing/) — constructing portfolios around specific risk factors.
- [Volatility](/historical-volatility/) — the overall level of price fluctuation in returns.
- Correlation — how factor returns move together, driving covariance terms.
- [Idiosyncratic risk](/idiosyncratic-risk/) — the diversifiable portion of portfolio risk.
- [Market risk](/market-risk/) — the broad systematic risk all equities share.
- [Diversification](/diversification/) — reducing idiosyncratic risk by holding multiple exposures.

### Wider context

- [Value-at-risk](/value-at-risk/) — a single-number summary of downside risk, informed by factor decomposition.
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — the theoretical foundation linking systematic risk and returns.
- [Performance fee](/performance-fee/) — compensation structures that reward factor outperformance.
- [Concentration risk](/concentration-risk/) — when a few factors or holdings dominate portfolio variance.
- [Stress testing](/stress-testing/) — examining how factor correlations change in crisis scenarios.

</div>

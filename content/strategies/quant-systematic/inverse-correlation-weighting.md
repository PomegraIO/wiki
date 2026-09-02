---
title: "Inverse Correlation Weighting"
description: "Portfolio construction method that weights assets inversely to their correlation matrix, reducing concentration and diversification benefit loss."
keywords:
  - inverse correlation weighting
  - correlation matrix
  - portfolio diversification
  - minimum variance
  - asset allocation
---

*An **inverse correlation weighting** strategy allocates capital to portfolio constituents in proportion to the inverse of their pairwise correlations with other holdings. Assets that move independently receive higher weight; highly correlated assets receive lower weight. The method aims to maximize [diversification](/wiki/diversification/) by concentrating capital where correlation drag is lowest.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Core principle** | Weight assets inversely to their average correlation with peers |
| **Correlation matrix** | N×N symmetric matrix of pairwise correlations between all portfolio assets |
| **Inverse operation** | Invert the correlation matrix; use diagonal or row-sum weights |
| **Mathematical form** | Weights proportional to row sums of the inverse correlation matrix |
| **Outcome** | Lower portfolio volatility than equal-weight; no forward-return assumptions |
| **Data requirement** | Lookback window (e.g., 252 trading days) to estimate correlations |
| **Rebalancing** | Typically quarterly or monthly; correlations drift over time |
| **Comparison** | Similar risk reduction to minimum-variance, easier to compute |

</aside>

## The intuition behind inverse correlation weighting

Consider two assets: a technology stock and a utility stock. If they are perfectly uncorrelated (correlation = 0), both contribute equally to [diversification](/wiki/diversification/). If they are highly correlated (correlation = 0.9), holding both is nearly redundant—buying more of the correlated asset does not reduce portfolio volatility as much.

Inverse correlation weighting formalizes this trade-off. An asset with low average correlation to the rest of the portfolio earns a higher weight because it provides more diversification per unit of volatility. An asset with high average correlation earns a lower weight because it is already largely represented by other holdings.

The appeal is simplicity: the method requires only a [correlation matrix](/wiki/correlation-coefficient/), not forecasts of future returns or volatility. It is a *risk-based* allocation rule, not a return-based one.

## Computing weights from the inverse correlation matrix

The mathematical mechanics are straightforward:

1. **Estimate the correlation matrix** *R* from historical returns (e.g., 252-day lookback):
   - Element *R_ij* = correlation between assets *i* and *j*

2. **Invert the matrix** to get *R*^−1

3. **Extract row sums** from *R*^−1:
   - Each row sum represents the cumulative "inverse correlation" of that asset with all others

4. **Normalize to weights**:
   - Weight for asset *i* = (row sum for *i*) / (sum of all row sums)

Example: Suppose a three-asset portfolio has inverse correlation matrix row sums of [0.4, 0.3, 0.2]. After normalization:
- Asset A: 0.4 / 0.9 ≈ 44%
- Asset B: 0.3 / 0.9 ≈ 33%
- Asset C: 0.2 / 0.9 ≈ 22%

Assets with higher row sums (lower average correlations) receive heavier allocation.

## Why inverse correlation weighting reduces volatility

The method exploits a fundamental principle: portfolio volatility depends on both individual volatilities and correlations. A portfolio of perfectly correlated assets has volatility equal to the weighted average of constituent volatilities. A portfolio of uncorrelated assets has lower volatility because diversification reduces the "effective risk."

By over-weighting uncorrelated positions, inverse correlation weighting lowers the portfolio's sensitivity to any single asset or risk factor. If asset A is uncorrelated with the rest, increasing its weight does not increase overall risk much. If asset B is highly correlated, reducing its weight removes redundant risk without sacrificing diversification.

The method is similar in spirit to [minimum-variance portfolio](/wiki/minimum-variance-portfolio/) construction but avoids the need to forecast future volatility. Minimum-variance solves a quadratic optimization problem to find the lowest-volatility portfolio; inverse correlation weighting uses a simpler rule that often delivers comparable results.

## Comparison to equal-weight and market-cap weighting

An equal-weight strategy (each asset = 1/N) ignores correlations entirely. High-correlation assets receive the same weight as uncorrelated ones, leading to unnecessary concentration in correlated pairs and higher portfolio volatility.

A [market-cap-weighted](/wiki/market-capitalization/) portfolio (weight by the asset's market value) also ignores correlations, instead assuming market weights are optimal. This assumption holds under certain conditions but breaks when correlations spike (e.g., crisis periods where most assets fall together).

Inverse correlation weighting sits between the two: it is more sophisticated than equal-weight but requires no return forecasts (unlike [mean-variance optimization](/wiki/capital-asset-pricing-model/)). Studies show it typically reduces volatility by 10–20% relative to equal-weight while avoiding the estimation error that plagues mean-variance.

## Practical implementation and rebalancing

To implement inverse correlation weighting:

1. **Choose a lookback window** (typically 252 trading days = 1 year)
2. **Estimate daily or weekly returns** for all portfolio constituents
3. **Compute the correlation matrix** from returns
4. **Invert the matrix** (computationally stable if the matrix is well-conditioned)
5. **Calculate weights** from row sums and normalize
6. **Rebalance monthly or quarterly** as correlations drift

The approach scales well: even a 100-asset portfolio requires only a 100×100 matrix inversion, which modern computers execute in milliseconds.

A key decision is the rebalancing frequency. Correlations are not stationary—they shift as market regimes change ([volatility clustering](/wiki/volatility-clustering/), crisis contagion). Quarterly rebalancing is common for institutional portfolios; monthly is more responsive but incurs higher transaction costs.

## When inverse correlation weighting shines

The method is most effective in stable, low-correlation environments. Consider a portfolio of U.S. equities, bonds, and commodities. Historically:
- U.S. equities and bonds are modestly negatively correlated (~-0.2)
- Commodities and equities are weakly positively correlated (~0.2)
- Bonds and commodities are near zero

Inverse correlation weighting would over-weight bonds and commodities relative to equal-weight, reducing overall portfolio volatility while maintaining exposure to growth (equities) and inflation protection (commodities).

In high-correlation environments (crisis periods, narrow market rallies), the benefits shrink. If all assets move together, the inverse correlation matrix offers little edge over equal-weight. The method also struggles with near-singular correlation matrices (e.g., when many assets track the same factor), which can produce unstable weights.

## Limitations and practical considerations

**Matrix inversion stability**: If the correlation matrix is nearly singular (e.g., two assets are almost perfectly correlated), the inverse becomes unstable and can produce extreme weights. Practitioners often add a small amount of regularization (shrinkage toward the identity matrix) to improve numerical stability.

**Correlation estimation error**: Historical correlations are estimates. A 252-day window may not reflect future behavior, especially if the portfolio composition or market regime changes. Extended periods of high or low correlation can skew the estimated matrix.

**Concentration risk**: The method can produce unequal weights. A single uncorrelated asset might receive 20% or more, while a highly correlated one might fall to 2%, creating concentration in a different dimension.

**Computational complexity**: Inverting a large matrix requires careful attention to numerical precision. Institutional implementers often use robust linear algebra libraries and monitor condition numbers.

## Relationship to other risk-based methods

Inverse correlation weighting is one of several [risk-based portfolio](/wiki/risk-parity-strategy/) construction approaches:

- **Inverse volatility**: Weight inversely to standard deviation; ignores correlations.
- **Risk parity**: Weight so that each asset contributes equal [risk](/wiki/risk-parity-strategy/) (variance × volatility); requires volatility and correlation estimates.
- **Minimum variance**: Optimize to minimize portfolio variance; forward-looking, depends on volatility *and* return forecasts.

Inverse correlation weighting is simpler than risk parity or minimum variance but more sophisticated than inverse volatility alone.

<div class="wiki-seealso">

### Closely related
- [Correlation coefficient](/wiki/correlation-coefficient/) — measure of joint movement between two assets
- [Diversification](/wiki/diversification/) — spreading capital across uncorrelated assets to reduce risk
- [Minimum-variance portfolio](/wiki/minimum-variance-portfolio/) — optimal risky portfolio with lowest expected volatility
- [Risk parity](/wiki/risk-parity-strategy/) — equal risk contribution across portfolio positions

### Wider context
- [Asset allocation](/wiki/asset-allocation/) — overall portfolio construction and weighting
- Portfolio volatility — standard deviation of portfolio returns
- [Volatility clustering](/wiki/volatility-clustering/) — tendency for high and low volatility to persist
- [Factor investing](/wiki/factor-investing/) — strategies targeting specific return sources or risk drivers

</div>

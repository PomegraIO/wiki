---
title: "Risk Contribution Decomposition"
description: "Method that attributes total portfolio risk to individual positions using marginal risk contributions and Euler's homogeneity theorem."
keywords:
  - risk attribution
  - marginal risk
  - portfolio risk
  - position sizing
  - euler theorem
  - risk budgeting
image: /svg/risk.svg
---

*A **risk contribution decomposition** breaks down the total risk of a portfolio into slices attributable to each holding, revealing which positions are pulling the heaviest weight on portfolio volatility or loss. Unlike historical attribution (which explains past returns), risk contribution is forward-looking and mathematical: it answers what each position contributes to tail risk, given the portfolio's current composition and correlation structure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Contribution Decomposition — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement concepts." />

<div class="wiki-infobox-caption">Maps total portfolio risk to individual positions for better oversight and rebalancing.</div>

|   |   |
|---|---|
| **What it is** | Calculation that allocates portfolio risk across holdings |
| **Key principle** | Euler's homogeneity theorem; marginal × weight = contribution |
| **Measured in** | Basis points or percentage of total portfolio variance |
| **Primary use** | Risk budgeting, position sizing, portfolio optimization |
| **Output** | Risk budget per position; identifies hidden concentration |

</aside>

## The problem: you can't see risk through positions

A portfolio manager holds 50 stocks, three bond funds, and a hedge fund. The portfolio's volatility is 12%. But which holdings are driving that 12%? Position A has a 5% allocation but may contribute 20% of total risk if it's highly correlated with other positions and volatile. Position B has a 10% weight but contributes only 3% of risk because it's defensive and uncorrelated.

Traditional performance reporting shows which positions made money or lost money—that's **return attribution**. But risk doesn't accumulate linearly with weight. A position's risk contribution depends on three things: (1) its own volatility, (2) its correlation with the rest of the portfolio, and (3) the portfolio's total risk scale. A simple weight-based risk allocation ("each position contributes risk proportional to its size") is wrong and misleading.

Risk contribution decomposition solves this by computing the **marginal risk contribution** of each position—the amount that portfolio risk changes if you adjust that position by a small amount—and then using a mathematical theorem to allocate total risk.

## Euler's homogeneity theorem

The trick comes from a classical result in mathematics. If a function is homogeneous of degree one—meaning that scaling all inputs by a factor λ scales the output by λ—then a specific property holds:

For portfolio variance, which is homogeneous of degree 1 in portfolio weights:

σ² (λ·w) = λ·σ²(w)

This implies:

Total Risk = Σ (Marginal Risk × Weight)

Or more formally:

σₚ = Σ wᵢ · (∂σₚ/∂wᵢ)

The marginal risk contribution of position i is how much portfolio volatility increases if you increase that position by one percentage point. When you multiply each position's marginal risk by its weight, the pieces sum exactly to total portfolio risk. No residual, no approximation—pure decomposition.

## The calculation

Suppose a portfolio has weights **w** and covariance matrix **Σ**. Portfolio variance is:

σₚ² = **w**ᵀ **Σ** **w**

The gradient with respect to weights is:

∇σₚ² = 2 **Σ** **w**

So the marginal contribution of position i to variance is:

MRC_i = (∂σₚ²/∂wᵢ) = 2 Σⱼ Σ_{ij} wⱼ

This is the sensitivity of portfolio variance to a change in position i. To convert to volatility (standard deviation), divide by 2σₚ. The **contribution** is then:

RC_i = wᵢ · (MRC_i / σₚ) = wᵢ · (∂σₚ/∂wᵢ)

Sum all RC_i across all positions and you get exactly σₚ. No missing pieces.

## Reading the output

Imagine a €100m portfolio:

| Position | Weight | Volatility | Correlation with portfolio | Marginal RC | Risk Contribution | % of Total Risk |
|----------|--------|-----------|---------------------------|-------------|-------------------|-----------------|
| Tech ETF | 20% | 18% | 0.95 | 3.2% | 0.64% | 26.7% |
| Bonds ETF | 40% | 5% | 0.45 | 0.60% | 0.24% | 10.0% |
| Hedge Fund | 25% | 8% | 0.70 | 1.40% | 0.35% | 14.6% |
| Cash | 15% | 0% | 0 | 0 | 0% | 0% |

Total portfolio volatility: **2.4%**

The Tech ETF, at only 20% of capital, drives 27% of risk because it's volatile and highly correlated with the overall portfolio. The Bond ETF, though it's the largest position at 40%, contributes only 10% because it's defensive. A naive 20% "risk budget" for tech would be too high; the math says 27% is accurate.

This is actionable. If a manager wants to reduce portfolio risk, they see immediately that trimming tech by 5% saves 27% × 5% ≈ 1.35% of total portfolio risk, while trimming bonds by 5% saves only ~0.5%. Or if the manager wants to maintain total risk while shifting into growth, they can calibrate by seeing what the trade-off is.

## Risk budgeting and position limits

Many institutional portfolios now operate under an explicit **risk budget**. Instead of saying "Tech can be no more than 25% of the portfolio," a modern risk framework says "Tech can contribute no more than 30% of total portfolio risk." This is more sophisticated because it accounts for correlation and volatility, not just size.

A quantitative portfolio manager might allocate a 2% risk budget to a 50-position portfolio, meaning each position has a risk cap. Using risk contribution decomposition, they can compute the maximum weight for each position given its expected volatility and the rest of the portfolio's structure. This prevents a small bet from exploding into a hidden concentration.

## Limitations and practical pitfalls

The method is only as good as the covariance matrix. In turbulent markets, correlation estimates become noisy, and the decomposition can whipsaw. A position might show a small marginal contribution in calm times, then suddenly spike during a correlation rout.

Equally, the decomposition is **ex-post**. It describes how risk is currently sliced, based on today's weights and today's estimated covariances. It doesn't predict how the slice will change if markets move, if you rebalance, or if correlations shift. A manager might learn that their hedge fund position contributes surprisingly little risk today—because it's small and hedging—but if they increase it, the correlation may strengthen and its risk contribution may explode.

For portfolios with [leverage](/leverage-ratio-forex/) or short positions, the calculation is still valid but the interpretation requires care. A short position may have a negative risk contribution (lowering total risk), but adding to it further can increase overall risk if correlations tighten.

## Integration with optimization

Modern portfolio construction uses risk contribution as a direct constraint. Instead of [mean-variance optimization](/mean-variance-optimization/) ("maximize return for a given volatility"), a manager might run **risk-parity optimization** ("equal risk contribution across all positions") or **maximum Sharpe ratio under a risk budget constraint** ("maximize returns but each position contributes at most X% of risk").

The output is a more robust, transparent portfolio. Investors can see not just how much capital is in each position, but how much risk it actually carries.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — aggregate portfolio loss metric to which risk is decomposed
- Variance — foundational measure of portfolio dispersion
- [Concentration Risk](/concentration-risk/) — risk contribution reveals hidden concentration
- Correlation — fundamental input to risk decomposition calculations
- [Asset Allocation](/asset-allocation/) — framework in which risk budgets are set
- [Factor Investing](/factor-investing/) — decomposition across systematic risk factors

### Wider context

- [Copula Risk Modeling](/copula-risk-modeling/) — alternative method capturing non-linear dependence
- [Stress Testing](/stress-testing/) — testing how risk contributions change under scenarios
- Portfolio Optimization — construction methods using risk constraints
- [Systemic Risk](/systemic-risk/) — aggregate portfolio risk in the financial system

</div>

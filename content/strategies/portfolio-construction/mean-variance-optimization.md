---
title: "Mean-Variance Optimization"
description: "Markowitz's mathematical framework for constructing portfolios that maximize expected return for a given level of volatility."
keywords:
  - portfolio construction
  - mean-variance
  - markowitz
  - asset allocation
  - volatility
  - efficient frontier
image: "/svg/strategies.svg"
---

*The **mean-variance optimization** framework, devised by Harry Markowitz in 1952, finds the portfolio weights that deliver the highest expected return for any chosen level of risk—or equivalently, the lowest volatility for any target return. It is the mathematical foundation of modern portfolio theory and remains the most widely used systematic approach to asset allocation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mean-Variance Optimization — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for portfolio construction strategy." />

<div class="wiki-infobox-caption">The method that launched a thousand allocation committees.</div>

|   |   |
|---|---|
| **Core idea** | Choose weights that maximize return per unit of [volatility](/currency-volatility/) |
| **Input data** | Expected returns, [standard deviations](/). covariances among assets |
| **Output** | Efficient portfolios along the [efficient frontier](/). uncorrelated returns |
| **Key metric** | Sharpe ratio (return minus risk-free rate, divided by volatility) |
| **Constraint** | Weights usually sum to 1; can include long-only, short, or sector bounds |
| **Computing** | Quadratic programming; closed-form solution with two risky assets |
| **Limitation** | Highly sensitive to small changes in expected-return estimates |

</aside>

## The math and the intuition

Markowitz's insight was deceptively simple: a portfolio's return is the weighted average of its asset returns, but its risk is *not* the weighted average of individual risks. Because assets move in different directions—some rising when others fall—the correlation structure matters. Diversification works precisely because you can lower portfolio [volatility](/currency-volatility/) without sacrificing return by holding negatively correlated positions.

The framework builds a covariance matrix—a table showing how each asset moves relative to every other. Then it searches for weights that minimize variance for a given return target. Flip the objective, and you maximize return for a given variance. Plot all efficient combinations together and you get the efficient frontier: a curved boundary showing the best possible tradeoff.

The mathematics requires only linear algebra. With two assets, the formula is nearly pencil-and-paper. With dozens, you need quadratic programming solvers. Most professional managers today use numerical optimizers that handle hundreds of constraints: no short selling, sector caps, ESG mandates, exposure limits. The core logic remains Markowitz's.

## Why it dominated institutional investing

For decades, mean-variance optimization *was* portfolio management. Pension funds, insurance companies, and family offices built their entire allocation process around it. The logic appealed to trustees and boards: you feed in reasonable assumptions about returns and risks, the math does the rest, and you get a defensible answer. No gut feel. No bias. Just optimal.

The framework also made risk concrete and measurable. Before Markowitz, risk was vague—something you felt. After him, risk was [volatility](/currency-volatility/): the [standard deviation](/.) of returns. That shift allowed institutions to talk about [asset allocation](/asset-allocation/) in numerical terms and to backtest historical tradeoffs.

## The estimation problem

Elegant mathematics collides with brutal reality: you must estimate future returns and covariances. Historical averages are noisy. Small errors balloon under optimization. Suppose you overestimate the return on one asset by just 1 per cent. The optimizer often assigns it 20–50 per cent of the portfolio, creating concentration that later backfires.

This curse of sensitivity is the framework's deepest flaw. The portfolio weights oscillate wildly with minor input tweaks, yet the portfolio's expected return and risk stay almost flat. The efficient frontier looks smooth, but the optimal weights are unstable. Practitioners call this the "error maximizer" problem: mean-variance optimization is so powerful that it amplifies your forecasting mistakes.

Responses have ranged from practical (input less volatile expected returns, impose weight bounds, rebalance often) to theoretical (use [Black-Litterman models](/black-litterman-model/) or [factor models](/factor-investing/) to constrain expectations, or shift to risk-based weighting). None fully solves it, but all reduce the sting.

## Related frameworks

The simplest variant is the **global minimum-variance portfolio**: the point on the efficient frontier where volatility is lowest. You don't need to forecast returns, only correlations and volatilities—easier and less error-prone. Many practitioners start here and then layer in views.

**Risk-parity portfolios** invert the problem: instead of maximizing return per unit of risk, they assign risk budgets equally across asset classes and solve for weights. A bond/stock split might be 70–30 by weight but 50–50 by volatility.

The [**Black-Litterman model**](/black-litterman-model/) begins with market-implied equilibrium returns (solved backward from current market prices) then blends in your own views. This stabilizes the optimization and often produces more robust, less extreme weights.

[**Maximum-diversification portfolios**](/maximum-diversification-portfolio/) weight assets inversely to their correlation with others, explicitly rewarding diversification without predicting returns.

## In practice

Universities, foundations, and sovereign wealth funds still use mean-variance optimization as a core tool, usually with heavy guardrails: rolling-window volatility estimates, Bayesian shrinkage of expected returns, minimum weight floors to prevent over-concentration. The [**endowment model**](/endowment-model/)—biased toward alternatives and illiquid assets—emerged partly as a response to mean-variance optimization's limitations with long time horizons and complex return distributions.

Few allocators run it unadorned anymore. Most use it as a check on judgment, or as part of a broader analytical process that includes stress tests, scenario analysis, and [value-at-risk](/value-at-risk/) modelling. The efficient frontier remains invaluable as a communication tool: a board or a client can see the return-risk tradeoff and understand why adding emerging-market equities makes sense even though it looks volatile.

The formula and the intuition endure. The practice has matured into something more nuanced and realistic.

## See also

<div class="wiki-seealso">

### Closely related

- Efficient frontier — the boundary of optimal return-risk combinations
- [Black-Litterman model](/black-litterman-model/) — stabilizing mean-variance optimization with market views
- [Maximum diversification portfolio](/maximum-diversification-portfolio/) — weighting by diversification potential rather than return forecast
- [Asset allocation](/asset-allocation/) — the strategic positioning of capital across asset classes
- [Sharpe ratio](/sharpe-ratio/) — return in excess of the risk-free rate, per unit of volatility
- [Factor investing](/factor-investing/) — systematic tilts toward return sources independent of forecasts

### Wider context

- [Endowment model](/endowment-model/) — alternative-heavy allocation for long-horizon investors
- [Volatility smile](/volatility-smile/) — departure of observed from theoretical risk distributions
- [Value-at-risk](/value-at-risk/) — worst-case loss under normal market conditions
- [Diversification](/diversification/) — the first free lunch in investing

</div>

---
title: "Least-Squares Monte Carlo"
description: "Longstaff-Schwartz regression method for valuing American and Bermudan options by estimating continuation value on simulated paths."
keywords:
  - american option pricing
  - longstaff-schwartz method
  - least squares regression
  - bermudan option
  - early exercise
image: "/svg/derivatives.svg"
---

*The **Least-Squares Monte Carlo** (LSM) method, developed by Longstaff and Schwartz, values American and Bermudan [options](/option/) by using regression to estimate the value of holding (not exercising) an option at each point in time along simulated asset paths. It combines simulation flexibility with the ability to handle early-exercise decisions.*

## The American option challenge

European [options](/option/) can only be exercised at maturity, so standard [Monte Carlo](/exotic-option-monte-carlo/) works well: simulate to the end, evaluate the payoff, average, and discount. American options can be exercised at any time, which introduces an optimal-stopping problem. At each moment, the holder must decide: exercise now and lock in the current payoff, or wait and keep the option alive?

This requires knowing the value of holding the option—the "continuation value"—at every point in time. Standard simulation doesn't naturally produce this, because you don't know future paths when making the exercise decision at an earlier time. Finite-difference grids and binomial trees can handle early exercise but become computationally expensive in higher dimensions or with complex dynamics.

The Longstaff-Schwartz method solves this by using linear regression to approximate the continuation value directly from the simulated paths.

## The algorithm

1. **Forward simulation**: Generate N paths of the underlying asset from today to maturity, respecting [volatility](/volatility-smile/) and [drift](/interest-rate/).

2. **Backward induction**: Starting at the final time step (maturity), work backwards towards today:
   - At maturity, the option's value is its payoff (max of strike difference, zero, etc.).
   - At each earlier date, for each simulated path:
     - Compute the immediate exercise payoff.
     - Use regression to estimate the expected continuation value based on the current asset price (and possibly other state variables).
     - The option value at that node is the maximum of exercise payoff and discounted continuation value.

3. **Regression specification**: The continuation value is typically modelled as a polynomial in the underlying price:

   E[V | S] ≈ β₀ + β₁ S + β₂ S² + ...

   Run least-squares regression across all N paths at each time step to fit the coefficients β. More sophisticated bases (Hermite polynomials, Laguerre polynomials) are used in practice, chosen to match the expected behaviour of option values.

4. **Final estimate**: Average the discounted payoffs across all paths. The result approximates the American option's fair value.

## Why it works

The key insight is that regression on the simulated paths gives you an unbiased estimator of the continuation value. At each decision point, you're asking: "What is the expected value of the option if we don't exercise now?" The regression answers this by fitting the future value (discounted backwards) as a function of today's observable state.

Because the regression is computed using all N paths simultaneously, you get a smooth approximation to the true continuation surface. Noise is smoothed out, and you can make robust exercise decisions even with coarse simulation grids.

The method converges to the true American option value as N increases, though the convergence is slower than for European options (roughly 1/√N in N, but with a larger constant factor).

## Bermudan options and multi-dimensional problems

Bermudan options can only be exercised on specified dates (not continuously). The algorithm naturally extends: you apply the regression and early-exercise logic only on exercise dates, not at every time step. This is actually computationally cheaper than American options and still captures the essential value of flexibility.

The method shines in high dimensions. A Bermudan swaption (option to enter an interest-rate swap) has a large state space: multiple forward rates or tenor points. A binomial or trinomial tree explodes in size; finite-difference grids become intractable. Least-squares Monte Carlo handles it gracefully—just simulate all factors jointly and use multivariate regression. Exotic baskets and multi-asset American options are similarly tractable.

## Practical considerations

**Choice of basis**: The regression basis (polynomial order, specific polynomials) affects accuracy and stability. Too few terms under-fit the continuation surface; too many over-fit and amplify noise. Practitioners often start with a cubic polynomial and test sensitivity to the basis choice.

**In-the-money paths**: Standard implementations use only in-the-money paths in the regression, since out-of-the-money paths have near-zero continuation value and add noise. This biased sample is corrected for in the final average.

**State variables**: For exotic options, you may include additional state variables in the regression: time to maturity, volatility level, or correlated factor returns. This enriches the approximation of the continuation surface.

**Computational cost**: Least-squares requires solving a least-squares problem at every time step and every path. For millions of paths and hundreds of time steps, this is non-trivial. Modern implementations use efficient solvers and GPU acceleration. A typical run might take seconds to minutes on a single machine.

## Biases and convergence

The method underestimates American option values slightly. This is because the regression approximation is optimistic about future continuation values—you're fitting regression coefficients using paths that have already revealed themselves, introducing a look-ahead bias. In practice, the bias is small (typically <1% of the option price) for well-chosen bases and sufficiently large N.

Some implementations run a dual algorithm (upper and lower bounds) to bracket the true value and assess bias.

## Extensions and alternatives

**Variance reduction**: Antithetic variates and control variates (using European option baselines) reduce sampling error and allow fewer paths.

**Quasi-Monte Carlo**: Replace pseudo-random numbers with low-discrepancy sequences (Sobol, Halton) to improve path coverage and reduce variance.

**Stochastic volatility and jumps**: The algorithm extends naturally to models where [volatility](/volatility-smile/) is random or where asset returns include jumps. Just simulate the full model and use appropriate state variables in the regression.

**Dividend and event modeling**: Discrete dividends, coupons, and other scheduled cash flows are easily incorporated by adjusting payoff functions along the path.

## Comparison to other methods

Versus binomial trees: Least-squares Monte Carlo scales better to multiple dimensions and non-standard dynamics; trees are faster for single-factor early-exercise.

Versus finite-difference PDE: Both are grid-free in the sense that discretisation happens in time and (implicitly via regression) state; PDE grids require careful placement in multi-dimensional problems.

Versus analytical approximations: LSM is more flexible and accurate for exotic structures; closed-form bounds (like Ju's quadratic approximation) are faster but less general.

## See also

<div class="wiki-seealso">

### Closely related

- [Exotic Option Monte Carlo Simulation](/exotic-option-monte-carlo/) — foundational simulation technique underlying LSM
- [Option](/option/) — call and put contracts with and without early exercise
- [Call Option](/call-option/) — plain-vanilla case
- [Strike Price](/strike-price/) — critical parameter in exercise decisions

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — theoretical foundation for European option pricing
- [Implied Volatility](/implied-volatility/) — key input to valuation and calibration
- [Volatility Smile](/volatility-smile/) — empirical pattern affecting option values
- [Interest Rate](/interest-rate/) — discount rate in American option valuation

</div>

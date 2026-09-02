---
title: "Delta-Normal VaR"
description: "Linear approximation method for value-at-risk assuming normal distribution of returns"
keywords:
  - var methodology
  - value at risk
  - delta-normal approximation
  - parametric var
  - risk measurement
---

*The **delta-normal VaR** method is a parametric approach to estimating portfolio value-at-risk that assumes returns follow a normal distribution and uses linear approximation (delta) to model how portfolio value changes with market movements. It's the simplest and fastest VaR calculation, but trades accuracy for computational speed.*

<aside class="wiki-infobox">

| Attribute | Value |
|---|---|
| **Also known as** | Parametric VaR, delta VaR, variance-covariance method |
| **Calculation time** | Milliseconds (matrix algebra only) |
| **Key assumption** | Returns are normally distributed |
| **Accuracy assumption** | Linear price response (convexity negligible) |
| **Best for** | Bonds, currencies, simple linear portfolios |
| **Not suitable for** | Options-heavy portfolios, fat-tail regimes |
| **Primary limitation** | Underestimates tail risk in real markets |

</aside>

## Why the delta-normal method starts with normality

The delta-normal method builds on a foundational assumption: that daily (or periodic) returns across assets follow a normal (Gaussian) distribution. Under this assumption, a portfolio's value is itself normally distributed, so you can describe its entire risk using just two parameters: the mean return and the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation). This is why the method is sometimes called the variance-covariance approach — you compute the variance (or volatility) of each position and the covariances between them, then combine them into a single tail-loss estimate.

The math is elegant. If a portfolio has expected return μ and volatility σ, then a 1-day VaR at the 95% confidence level is approximately μ − 1.645 × σ (where 1.645 is the 95th percentile of the standard normal distribution). For a $10 million portfolio with 2% daily volatility, the 95% VaR is roughly $10M × 1.645 × 0.02 = $329,000. A 99% VaR uses 2.326 instead of 1.645, yielding $465,000. That one-liner captures the entire method.

## Where "delta" enters: linear approximation for derivatives

For portfolios containing only stocks and bonds — assets with linear payoff functions — the normal-distribution assumption is the only approximation. But when you add [options](/wiki/option/), the portfolio's value no longer moves linearly with the underlying market. A call option has [gamma](/wiki/gamma-option-greeks/) (convexity), meaning its delta (price sensitivity) changes as the underlying moves. The delta-normal method ignores gamma and treats the option as if it were a linear position with a fixed delta. This is why it's called delta-normal: it uses the option's delta (first-order price sensitivity) and ignores the second-order (gamma) and higher-order effects.

In practice, this means delta-normal VaR works well for interest-rate swaps, [currency forwards](/wiki/currency-future/), and long stock portfolios, but systematically underestimates losses in short-option positions or during market crashes when gamma becomes extreme.

## The three-step calculation

**Step 1: Build the covariance matrix.** Collect daily returns for all assets in the portfolio over a lookback window (usually 252 trading days for a year). Compute the correlation and volatility of each asset and pair-wise [correlations](/wiki/correlation-coefficient/). This gives you a covariance matrix Σ.

**Step 2: Compute portfolio volatility.** If your portfolio weights are w (a vector of position sizes), then portfolio variance is w^T × Σ × w, and volatility is the square root. This step is where the method's speed comes from — it's pure linear algebra, no simulation needed.

**Step 3: Apply the confidence level.** Multiply portfolio volatility by the appropriate quantile from the normal distribution (1.645 for 95%, 2.326 for 99%) and by the portfolio value. This gives the VaR in dollars or basis points.

## Why practitioners still use it, despite its flaws

Delta-normal VaR dominated risk management from the 1990s through the 2010s. Three reasons persist:

*Speed and transparency.* The calculation runs in microseconds and every number is auditable. You can trace a $1 million VaR estimate back to specific asset volatilities and correlations. [Historical simulation](/wiki/historical-var/) and Monte Carlo require thousands or millions of scenario recalculations. In 1995, when JPMorgan published RiskMetrics, computational power was scarce.

*Regulatory acceptance.* Basel III and derivative-trading regulations long treated delta-normal VaR as a baseline approach. Banks filing [stress-test](/wiki/stress-testing/) results often use it as a benchmark to which they compare more complex methods.

*Adequate for calm markets.* In quiet periods when correlations are stable and no tail events are imminent, delta-normal's normality assumption is roughly harmless. It fails catastrophically only during crises — exactly when you most need an accurate risk estimate.

## When delta-normal VaR breaks down

The method's critical weakness emerged during the [2008 financial crisis](/wiki/lehman-brothers-collapse/) and replayed in the 2020 COVID crash: normal distributions have no fat tails, but real market returns do. A 25-sigma (once-in-a-million-years, in normal terms) move happened on March 16, 2020, across dozens of assets simultaneously. Delta-normal VaR flagged no warning beforehand because the method is backward-looking. If the last 252 days showed calm, the covariance matrix reflects calm, and VaR estimates are complacent.

For portfolios heavy in short options (selling downside protection), delta-normal is worse than useless. A sold put position has very high gamma-at-the-money: if the market rallies 5%, you lose gamma convexity and delta-normal forecasts your loss as near zero (delta ≈ zero at the money). If the market crashes, your delta swings hard negative and losses blow through delta-normal's estimate. The method cannot capture this gamma punch.

## Delta-normal versus historical and Monte Carlo

Three major parametric and simulation VaR methods compete:

[**Historical simulation**](/wiki/historical-var/) abandons the normal assumption entirely. It replays the last 252 days of market moves against your current portfolio. If the worst historical day caused a $500k loss, your 99% VaR is $500k. No matrix algebra, no distributional assumptions — just empirical data. But it requires *unique* stress scenarios to have occurred in your lookback window. A new tail risk (crypto crash, pandemics) has no historical precedent.

[**Monte Carlo VaR**](/wiki/monte-carlo-var/) generates thousands of random paths of future returns, each obeying a specified distribution (usually multivariate normal with fitted parameters). This is computationally expensive but flexible: you can incorporate non-normal tail behavior, regime shifts, and jumps. Most models still assume multivariate normality, though, which is only marginally better than delta-normal unless you calibrate the tails explicitly.

Delta-normal wins on speed and regulatory clarity. Historical simulation wins on simplicity and tail-fidelity. Monte Carlo wins on flexibility but loses on transparency and computation.

## Regulatory use today

Agencies distinguish between the **standard approach** (prescribed risk weights, no VaR required) and the **internal models approach** (banks compute their own VaR using approved methods). Under Basel III, delta-normal VaR is permitted but increasingly discouraged in favor of [expected shortfall](/wiki/expected-shortfall/) (conditional value-at-risk), which captures tail severity better. The U.S. [Federal Reserve](/wiki/federal-reserve/) now requires certain derivatives dealers to report VaR using at least 99% confidence and 10-day holding periods. Delta-normal at 95% and 1-day horizon is treated as a bare minimum, not a standard.

<div class="wiki-seealso">

### Closely related
- [Value at Risk](/wiki/value-at-risk/) — The general framework for measuring tail loss
- [Variance Covariance](/wiki/capital-asset-pricing-model/) — Underpinning covariance calculation
- [Volatility](/wiki/historical-volatility/) — Input to every parametric VaR calculation
- [Expected Shortfall](/wiki/expected-shortfall/) — Regulatory alternative that measures loss severity beyond VaR

### Wider context
- Risk measurement — Portfolio risk quantification
- [Capital adequacy](/wiki/capital-adequacy/) — Regulatory capital requirements for risk
- [Stress testing](/wiki/stress-testing/) — Scenario-based risk assessment complementing VaR
- [Correlation coefficient](/wiki/correlation-coefficient/) — Covariance between asset pairs

</div>

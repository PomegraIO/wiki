---
title: "Heston Stochastic Volatility Model"
description: "A pricing framework where volatility itself evolves randomly, allowing the model to capture the volatility smile observed in real option markets."
keywords:
  - Heston model
  - stochastic volatility
  - option pricing
  - volatility smile
  - mean reversion
image: "/svg/derivatives.svg"
---

*The [Black-Scholes model](/black-scholes-model/) assumes that volatility stays constant over time. In real markets, it doesn't. Traders observe that [options](/option/) at different [strike prices](/strike-price/) command different implied volatilities—a pattern called the volatility smile. The **Heston model**, published in 1993, solved this by treating volatility itself as a stochastic (random) variable that evolves according to its own mean-reverting process. The payoff is a pricing framework that fits observed market smiles and generates [option Greeks](/delta/) that match trader intuition better than constant-volatility models.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Heston Stochastic Volatility Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and complex instruments." />

<div class="wiki-infobox-caption">Volatility follows a mean-reverting random walk; the model captures volatility smile without closed-form constant-volatility assumptions.</div>

|   |   |
|---|---|
| **What it is** | Two-factor [option](/option/) pricing model where asset price and variance both follow stochastic differential equations |
| **Key feature** | Volatility exhibits mean reversion and its own randomness, independent of asset price movements |
| **Output** | Option prices and Greeks that match empirical volatility patterns; calibrates to market-observed smiles |
| **Alternative to** | [Black-Scholes model](/black-scholes-model/) (constant volatility) and [jump-diffusion models](/option/) (discrete jumps) |
| **Computational method** | Closed-form characteristic-function solution; often solved numerically via FFT or Monte Carlo |
| **Advantage** | Naturally captures [volatility smile](/volatility-smile/); [theta](/time-decay-theta/) and Greeks more realistic |

</aside>

## The volatility smile problem

Under Black-Scholes, an [equity option](/option/) is priced as a function of five inputs: stock price, [strike price](/strike-price/), time to expiry, the risk-free rate, and volatility. If volatility were truly constant, all options on the same underlying with the same maturity would display the same implied volatility across all strikes.

Empirically, this fails. In equity markets, out-of-the-money [put options](/put-option/) and [call options](/call-option/) far from the current spot price trade at higher implied volatilities than at-the-money options. When graphed (implied volatility on the y-axis, strike on the x), the curve dips in the middle and rises at the wings—a smile.

This smile emerged sharply after the 1987 market crash, when traders realized that extreme moves were more frequent and more severe than Gaussian assumptions allowed. A constant-volatility model could not reconcile these prices.

## The Heston framework: two coupled stochastic processes

Steven Heston's solution was to model volatility as a separate state variable driven by its own random process:

- The stock price (or forward) follows a standard diffusion with volatility \(v_t\): \(dS = \mu S dt + \sqrt{v_t} S dW_1\)
- The variance \(v_t\) itself follows a mean-reverting square-root (Cox-Ingersoll-Ross) process: \(dv = \kappa(\theta - v_t) dt + \sigma_v \sqrt{v_t} dW_2\)

The two Wiener processes \(W_1\) and \(W_2\) are correlated by a constant \(\rho\), capturing the empirical "leverage effect": bad news (falling stock price) often coincides with a spike in volatility.

The parameters are:

- \(\kappa\): speed of mean reversion of variance (how fast volatility pulls back to its long-run level)
- \(\theta\): long-run average variance
- \(\sigma_v\): volatility of volatility (how much the variance itself jitters)
- \(\rho\): correlation between stock price and variance shocks

## Why the square-root process matters

Volatility cannot be negative, so Heston chose a square-root (CIR) process for variance. This ensures \(v_t\) remains non-negative for all positive parameter values. The square-root term \(\sqrt{v_t}\) also means that as variance approaches zero, the random drift diminishes—the process "bounces" back toward its mean.

This structure produces mean reversion: if volatility spikes, the process pulls it back toward \(\theta\) at a rate governed by \(\kappa\). Traders observe this in practice: volatility bursts typically don't persist indefinitely.

## Capturing the smile

The genius of the model is that \(\rho\) generates the smile. A negative correlation means that when the stock falls, volatility rises—making out-of-the-money puts more expensive (lower strikes, higher vol) and at-the-money calls cheaper relative to out-of-the-money calls. This tilts the smile and skew in ways that match real equity option markets.

A calibration of the Heston model to observed prices yields parameters \(\kappa, \theta, \sigma_v, \rho\) that make the model's prices consistent with traded option prices across the entire strike surface and term structure.

## Valuation: closed form and numerical methods

Heston derived a closed-form solution using characteristic functions—a Fourier-based representation of the [option](/option/) price. This is not a simple formula like Black-Scholes, but it is faster to compute than Monte Carlo and more stable numerically.

The characteristic function approach expresses the option price as an inverse Fourier integral, typically evaluated via FFT or adaptive quadrature. For practitioners, this means Heston prices can be computed to high precision in milliseconds on modern hardware.

Alternatively, Monte Carlo simulates the two coupled stochastic processes forward in time, averaging payoffs over many paths. Monte Carlo is slower but easily handles American options, barriers, and exotic payoffs that the characteristic-function method struggles with.

## Strengths and limitations

**Strengths:**
- Explains the volatility smile and skew elegantly
- Greeks ([delta](/delta/), [gamma](/gamma/), [vega](/vega/)) emerge naturally and match market behavior
- Mean reversion of volatility is empirically grounded
- Calibration is well-established; software is widely available

**Limitations:**
- Correlation parameter \(\rho\) is fixed; real leverage effects may vary with time and moneyness
- Assumes no jumps; large market shocks (earnings surprises, political events) are not modeled
- Calibration can be unstable if the option surface is sparse or noisy
- Heston model parameters don't remain stable across market regimes

## Extensions and alternatives

The [SABR model](/sabr-model/) simplifies Heston for interest-rate options by assuming a different form of volatility diffusion. Jump-diffusion extensions add discontinuous price jumps on top of stochastic volatility, improving fit during crises.

Rough volatility models—a newer direction—treat volatility as a fractal process with memory, fitting shorter-dated option prices even better. But these are harder to calibrate and price.

## Practical use in trading and risk

Trading desks use Heston daily. Quants calibrate it to the morning's volatility surface, then use the model to price bespoke exotics, hedge [Greeks](/delta/), and identify arbitrage opportunities. Risk managers incorporate Heston-based scenarios into [value-at-risk](/value-at-risk/) frameworks to stress-test [delta](/delta/), [gamma](/gamma/), and [vega](/vega/) exposures.

The model is sophisticated enough to pass the sniff test—it explains real phenomena—yet simple enough that parameters can be pinned from observable data and prices computed in real time.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes Model](/black-scholes-model/) — constant-volatility predecessor that Heston extends
- [Volatility Smile](/volatility-smile/) — empirical phenomenon the Heston model explains
- [Implied Volatility](/implied-volatility/) — the volatility extracted from option prices; Heston reconciles cross-strike variation
- [Delta](/delta/) — option Greeks emerge naturally in Heston framework
- [Vega](/vega/) — sensitivity to volatility shifts; Heston hedges captured via [options](/option/)
- [SABR Model](/sabr-model/) — alternative stochastic volatility framework for rates

### Wider context

- [Option](/option/) — the instrument Heston prices
- [Call Option](/call-option/) and [Put Option](/put-option/) — specific payoff types fitted to market
- [Strike Price](/strike-price/) — the moneyness coordinate along which the smile is observed
- [Value at Risk](/value-at-risk/) — uses Heston for scenario and [Greeks](/delta/) based risk models
- [Gamma](/gamma/) and [Theta](/time-decay-theta/) — second-order Greeks also output by Heston

</div>

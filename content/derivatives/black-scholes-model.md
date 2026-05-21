---
title: "Black-Scholes Model"
description: "The Black-Scholes model is the foundational formula for pricing European options, using stock price, strike, time, volatility, and interest rates to calculate fair value."
keywords:
  - black-scholes
  - option pricing
  - valuation model
  - derivatives pricing
  - european option
image: "/svg/derivatives.svg"
---

*The **Black-Scholes model** is a closed-form mathematical formula that prices [European option](/european-option)s on non-dividend-paying stocks. Published in 1973 by Fischer Black, Myron Scholes, and Robert Merton, it revolutionized derivatives markets by providing an instant, analytically tractable method to compute option values. The model takes five inputs—[stock](/stock) price, [strike price](/strike-price), time to [expiration](/expiration-date), [volatility](/historical-volatility), and interest rates—and outputs the fair value of [call](/call-option) and [put option](/put-option)s, plus the [options Greeks](/options-greeks).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Black-Scholes Model — key facts</div>

<img src="/svg/derivatives.svg" alt="Mathematical formula on financial charts" />

<div class="wiki-infobox-caption">Black-Scholes pricing: the foundation of modern options trading.</div>

|   |   |
|---|---|
| **Applies to** | European options on non-dividend stocks |
| **Outputs** | Option price and Greeks (delta, gamma, theta, vega, rho) |
| **Inputs** | Stock price, strike, time, volatility, rates |
| **Computation** | Closed-form (instant calculation) |
| **Accuracy** | Exact for Europeans; approximation for Americans |
| **Volatility input** | Uses implied or historical volatility |
| **Key assumptions** | Log-normal distribution, no arbitrage, frictionless |
| **Nobel Prize** | 1997 (Scholes and Merton; Black deceased) |
| **Modern usage** | Baseline; adjusted for dividends, American features, exotics |
| **Limitations** | Assumes constant volatility, zero dividends, no transaction costs |

</aside>

## The formula and intuition

The Black-Scholes call price formula is:

C = S₀ × N(d₁) − K × e^(−rT) × N(d₂)

Where:
- S₀ is the current stock price
- K is the [strike price](/strike-price)
- r is the risk-free interest rate
- T is time to [expiration](/expiration-date)
- σ is [volatility](/historical-volatility)
- N(d) is the cumulative normal distribution function
- d₁ and d₂ are derived from these inputs

The intuition: the call is worth the [present value](/compound-interest) of the expected payoff if the stock finishes above the strike, minus the [present value](/compound-interest) of the strike price. The normal distributions weight the payoffs by their probabilities under a log-normal stock price model.

For puts, the formula is:

P = K × e^(−rT) × N(−d₂) − S₀ × N(−d₁)

## Assumptions underlying Black-Scholes

1. **Log-normal distribution:** Stock prices follow a log-normal distribution.
2. **Constant volatility:** [Volatility](/historical-volatility) is constant over the option's life (unrealistic but tractable).
3. **No dividends:** The stock pays no [dividend](/dividend)s. (Extensions add dividend yield.)
4. **Frictionless markets:** No transaction costs, taxes, or borrowing constraints.
5. **Continuous trading:** You can buy/sell at any time (not gaps).
6. **No arbitrage:** Markets are efficient; prices preclude riskless profit.

These assumptions are violated in real markets, but the model's simplicity and accuracy in many scenarios made it the industry standard.

## Greeks from Black-Scholes

The Black-Scholes formula yields closed-form Greeks:

- **Delta:** N(d₁) for calls; N(d₁) − 1 for puts
- **Gamma:** φ(d₁) / (S₀ × σ × √T), where φ is the standard normal density
- **Theta:** Daily decay formula (negative for long options)
- **Vega:** S₀ × φ(d₁) × √T for both calls and puts
- **Rho:** K × T × e^(−rT) × N(d₂) for calls; −K × T × e^(−rT) × N(−d₂) for puts

These formulas let traders compute hedging ratios instantly.

## Extensions and variants

**For dividends:** The Black-Scholes formula is adjusted by replacing the stock price with S₀ × e^(−q×T), where q is the dividend yield. This shifts the call price down and the put price up.

**For American options:** Black-Scholes does not account for early exercise. The [binomial-option-pricing](/binomial-option-pricing) model or numerical methods are needed for [american-option](/american-option)s.

**For exotics:** [Exotic option](/binary-option)s with path-dependent payoffs (e.g., [asian-option](/asian-option)s, [barrier-option](/barrier-option)s) require [Monte-carlo-options-pricing](/monte-carlo-options-pricing) or other numerical methods.

## Implied volatility

The Black-Scholes formula is also used in reverse: given a market option price, solve for the [volatility](/historical-volatility) that makes the formula equal the market price. This is the **[implied volatility](/implied-volatility)**. The market's implied volatility is a key input for traders pricing and hedging other options.

## Historical impact

Before Black-Scholes, options pricing was ad-hoc and subjective. After publication, the model became the lingua franca of options markets. It enabled:

1. **Quantitative pricing** of options across exchanges.
2. **Hedging** using precise Greeks.
3. **Volatility arbitrage** by comparing implied and realized [volatility](/historical-volatility).
4. **Derivatives explosion** (swaps, exotics, structured products).

The 1997 Nobel Prize in Economics recognized its importance.

## Limitations and real-world adjustments

**Volatility smile/skew:** Markets do not trade all strikes at the same [implied volatility](/implied-volatility). The Black-Scholes model assumes constant volatility, but market data shows it varies by [strike price](/strike-price) and [expiration](/expiration-date). Traders adjust prices and Greeks manually or use alternative models.

**Jump risk:** Real stocks can gap (jump) overnight (earnings, news). Black-Scholes assumes continuous paths. Extended models account for jumps.

**Stochastic volatility:** Volatility itself changes over time. Models like Heston's stochastic volatility model improve on Black-Scholes.

**Dividends and early exercise:** American options can be exercised early; Black-Scholes does not handle this.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the instrument being priced
- [Call option](/call-option/) — one primary output
- [Put option](/put-option/) — other primary output
- [Implied volatility](/implied-volatility/) — volatility input and market observation
- [Historical volatility](/historical-volatility/) — alternative volatility input

### Extensions and alternatives

- [Binomial option pricing](/binomial-option-pricing/) — for American options
- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — for exotic options
- [Volatility smile](/volatility-smile/) — empirical deviation from Black-Scholes
- [Heston model](/volatility-smile/) — stochastic volatility extension

### Greeks and risk

- [Options Greeks](/options-greeks/) — delta, gamma, theta, vega, rho
- [Delta](/delta/) — primary risk measure
- [Vega](/vega/) — volatility risk

### Deeper context

- [European option](/european-option/) — main application
- [Derivatives pricing](/black-scholes-model/) — fundamental principle
- Financial modeling — core quantitative tool

</div>

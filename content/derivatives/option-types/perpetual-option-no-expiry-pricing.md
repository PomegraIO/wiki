---
title: "How Perpetual Options Are Priced Without an Expiry Date"
description: "Perpetual option pricing uses optimal stopping theory to derive a closed-form value where time decay is replaced by dividend yield and interest rate factors."
keywords:
  - perpetual option no expiry
  - perpetual American option pricing
  - optimal stopping option
  - time value option
  - dividend-yield option pricing
  - black-scholes perpetual
---

*A **perpetual option** is an American option with no expiration date, meaning the holder can exercise it at any future time without limit. Its value does not approach zero as time advances—instead, pricing relies on a balance between [interest rates](/interest-rate/), [dividend yields](/dividend-yield/), and the distance of the [strike price](/strike-price/) from the current asset price.*

Standard [options](/option/) expire on a specified date. The closer an option approaches expiration, the more its [time value](/time-value/) decays toward zero—eventually only [intrinsic value](/intrinsic-value/) remains. A perpetual option has no expiration, which appears to create a paradox: if time never runs out, should not its value be infinite?

The resolution lies in recognizing that perpetual options are priced using **optimal stopping**—a mathematical framework that determines the boundary at which the holder should exercise. The value is finite because holding the option indefinitely has an opportunity cost: foregone interest income on the strike price and foregone dividends if the underlying asset pays them. These economic drains eventually make early exercise optimal, establishing an equilibrium price.

## The Optimal Stopping Framework

An American call option on a dividend-yielding stock can be exercised at any point. The holder must decide: should I exercise now and collect the intrinsic value, or wait for a possible future gain?

If the stock pays a continuous dividend yield **q**, then holding the stock and receiving its yield is attractive compared to holding the option (which does not receive dividends). Similarly, holding cash (the strike price) and earning the [risk-free rate](/federal-funds-rate/) **r** is valuable. The **optimal exercise boundary** for a perpetual call is the stock price **S\*** at which the marginal gain from waiting exactly equals the marginal cost of waiting.

At the optimal boundary **S\***, the perpetual call value **C(S\*)** satisfies:

$$C(S^*) = S^* - K$$

That is, the option value equals intrinsic value at the exercise boundary. And the value in the continuation region (before reaching S\*) is determined by solving the differential equation that balances dividend flow, interest rates, and [volatility](/historical-volatility/):

$$\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + (r - q)S \frac{\partial C}{\partial S} - rC = 0$$

where **σ** is the asset's volatility.

## Closed-Form Perpetual Call Solution

For a perpetual American call on a dividend-paying stock, the exercise boundary is:

$$S^* = \frac{\beta_1}{\beta_1 - 1} K$$

where **β₁** is the larger root of the quadratic:

$$\frac{1}{2}\sigma^2 \beta(\beta - 1) + (r - q)\beta - r = 0$$

Solving yields:

$$\beta_1 = \frac{1}{2} - \frac{r - q}{\sigma^2} + \sqrt{\left(\frac{r - q}{\sigma^2} - \frac{1}{2}\right)^2 + \frac{2r}{\sigma^2}}$$

The perpetual call value for **S < S\*** is:

$$C(S) = \left(\frac{S}{S^*}\right)^{\beta_1} (S^* - K)$$

This formula reveals the key insight: as **S** grows toward **S\***, the option value rises smoothly; beyond **S\***, the option is exercised immediately and the value is just intrinsic value.

## Why Time Value Never Decays to Zero

In a standard European option, time value decays monotonically and vanishes at expiration. Why not here?

The answer is that a perpetual option offers **perpetual optionality**—the flexibility to wait indefinitely for a better outcome. This flexibility has intrinsic economic value that does not erode over time. The balance between:
- **Interest cost**: holding the strike price in cash for another day forgoes **r × K × dt**,
- **Dividend cost**: not owning the stock forgoes **q × S × dt**,
- **Volatility benefit**: the chance that the stock will rise further,

creates a steady state. The option holder is willing to pay a constant premium above intrinsic value to retain this flexibility, and this premium does not decay as the option gets older because there is no expiration clock.

## Perpetual Put Valuation

A perpetual American put follows similar logic but with reversed roles. If the stock declines to a low boundary **S\***, the put holder exercises and receives **K − S\***.

The optimal exercise boundary for a perpetual put is:

$$S^* = \frac{\beta_2}{\beta_2 - 1} K$$

where **β₂** is the *smaller* root of the same quadratic (and is negative). The perpetual put value for **S > S\*** is:

$$P(S) = \left(\frac{S}{S^*}\right)^{\beta_2} (K - S^*)$$

When **q = 0** (no dividends) and **r > 0**, the put holder's incentive to wait weakens as interest rates rise—the opportunity cost of holding the strike price increases, making early exercise more attractive. Conversely, high dividends increase the incentive to defer put exercise (and hold the stock) rather than cash in the put immediately.

## Assumptions and Practical Limits

The closed-form solution assumes:
- **Log-normal stock price dynamics** (constant volatility under geometric Brownian motion).
- **No transaction costs** or discontinuous jumps in the asset price.
- **Continuous dividend yield** (not discrete payments).
- **Perfect divisibility** of the stock.

In reality, perpetual options are rare in markets. Most traded options have fixed expirations because:
- Counterparties prefer known payoff timelines.
- Perpetual options create unresolved contingent claims on a company's balance sheet.
- Issuers (e.g., a company short the option) face indefinite liability.

However, perpetual options do appear in theoretical work, corporate finance (e.g., investment timing decisions), and in **real options valuation**, where a company has the perpetual right to invest in a project.

## Comparison to Standard Options

| Feature | Standard Option | Perpetual Option |
|---------|-----------------|------------------|
| **Expiration date** | Fixed, e.g., 3 months | None |
| **Time decay (Theta)** | Accelerates near expiry | Constant (non-zero) |
| **Valuation method** | Black-Scholes, binomial | Optimal stopping, PDE |
| **Exercise boundary** | Not fixed (dynamic) | Fixed, determined by roots |
| **Practical use** | Widespread | Rare (theoretical, real options) |

## Applications in Corporate Finance and Valuation

Perpetual options underpin **real options analysis**—the idea that managers can time large capital expenditures. A firm with the perpetual right to build a factory (but no obligation) owns a perpetual American call on the factory's operating cash flows with the strike price equal to the construction cost. The formula above determines whether it is better to invest today or wait.

Similarly, a firm holding a mineral concession indefinitely can model abandonment or expansion as perpetual put and call decisions, weighting the option value against the [cost of capital](/cost-of-equity/).

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational instrument with fixed expiry; perpetual options extend this
- [American Option](/option/) — perpetual options are a limiting case of American options
- [Optimal Stopping](/option/) — mathematical framework underlying perpetual option pricing
- [Strike Price](/strike-price/) — the exercise boundary depends critically on strike and spot
- [Dividend Yield](/dividend-yield/) — affects the cost of waiting and the optimal exercise boundary
- [Time Value](/time-value/) — perpetual options retain non-zero time value indefinitely
- [Black-Scholes Model](/black-scholes-model/) — extended to perpetual options via differential equations
- [Interest Rate](/interest-rate/) — determines the opportunity cost of deferral

### Wider context

- [Option Premium](/option-premium/) — perpetual options command a premium above intrinsic value
- [Real Options Valuation](/business-development-company/) — real options invest timing decisions using perpetual option logic
- [Volatility Smile](/volatility-smile/) — empirical pricing patterns that may affect practical perpetual option use
- [Derivatives Hedging](/derivatives-hedging/) — broader context for option strategies

</div>

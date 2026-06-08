---
title: "Black-Scholes Delta Calculation Explained With an Example"
description: "How to calculate delta using the Black-Scholes formula with a worked example, showing the precise inputs and step-by-step computation."
keywords:
  - black scholes delta calculation
  - delta formula option pricing
  - option greek delta
  - how to calculate delta
  - call option delta
---

*The **delta** in the [Black-Scholes model](/black-scholes-model/) measures how much an option's price moves for a one-dollar move in the underlying stock. It is calculated from five inputs—stock price, strike price, time to expiration, interest rate, and volatility—using the cumulative standard normal distribution. This article walks through the formula and a concrete numeric example.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Black-Scholes Delta — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A precise, model-derived sensitivity metric showing how many dollars an option gains for each dollar the stock moves.</div>

|   |   |
|---|---|
| **Symbol** | Δ (delta) |
| **Range (call)** | 0 to 1; 1 means fully leveraged move with stock |
| **Range (put)** | -1 to 0; -1 means inverse move with stock |
| **What it means** | Approximate change in option price per $1 stock move |
| **Formula step** | Calculate d1, then take N(d1) for calls or N(d1) − 1 for puts |
| **Inputs required** | Stock price, strike, time, rate, volatility |
| **Practical use** | [Hedging](/derivatives-hedging/), [gamma](/gamma/) calculation, [covered calls](/covered-call/) |

</aside>

## The Black-Scholes delta formula

The Black-Scholes model expresses the **delta** of a call option as:

**Δ_call = N(d₁)**

where **N(d₁)** is the cumulative standard normal distribution function evaluated at d₁. The formula for d₁ is:

**d₁ = [ln(S / K) + (r + σ² / 2) × T] / (σ × √T)**

Breaking down each component:

- **S** = current stock price
- **K** = strike price (the price at which you have the right to buy)
- **r** = risk-free interest rate (annualized, as a decimal)
- **σ** = volatility of the stock's returns (annualized, as a decimal)
- **T** = time to expiration (in years)
- **ln()** = natural logarithm
- **N()** = cumulative standard normal distribution (a table lookup or function)

For a put option, delta is:

**Δ_put = N(d₁) − 1**

This is always negative, reflecting that put values move opposite to stock prices.

## A worked example: call option delta

Suppose you are analyzing a call option with the following parameters:

- Stock price (S) = $100
- Strike price (K) = $105
- Time to expiration (T) = 0.25 years (3 months)
- Risk-free rate (r) = 0.05 (5% annual)
- Volatility (σ) = 0.20 (20% annual, or annualized historical volatility)

**Step 1: Calculate d₁**

First, compute the numerator:

ln(S / K) = ln(100 / 105) = ln(0.9524) ≈ −0.0488

(r + σ² / 2) × T = (0.05 + 0.04 / 2) × 0.25 = (0.05 + 0.02) × 0.25 = 0.07 × 0.25 = 0.0175

Sum of numerator components:
−0.0488 + 0.0175 = −0.0313

Now compute the denominator:

σ × √T = 0.20 × √0.25 = 0.20 × 0.5 = 0.10

Therefore:

d₁ = −0.0313 / 0.10 = −0.313

**Step 2: Look up N(d₁)**

N(d₁) is the cumulative probability that a standard normal random variable is less than or equal to −0.313. Using a standard normal table or spreadsheet function (NORM.S.DIST in Excel, for example):

N(−0.313) ≈ 0.377

**Step 3: The delta**

Δ_call = N(d₁) ≈ 0.377

This means that for every $1 the stock price rises, the call option price is expected to rise by approximately $0.38. Conversely, if the stock falls $1, the call should fall roughly $0.38.

## Interpretation and practical use

A delta of 0.377 indicates that the option is **out of the money** (the stock is below the strike) and has a moderate probability of finishing in the money at expiration. The delta is not 0.5, which would indicate the strike is at-the-money, because we are starting $5 below the strike with only three months to expiration.

As the stock price rises and the option moves deeper in the money, delta approaches 1. As the stock falls and the option moves further out of the money, delta approaches 0. At expiration, delta is either exactly 0 (if the option is out of the money) or exactly 1 (if it is in the money)—a consequence of the binary payoff at maturity.

Traders and risk managers use delta for several purposes:

- **[Hedging](/derivatives-hedging/)**: If you own 100 shares of stock and want to hedge against downside, you might sell call options with a delta of 0.4 on each share. Selling 100 calls with delta 0.4 is equivalent to short-hedging 40 shares' worth of upside.
- **[Gamma](/gamma/) calculation**: Delta changes as the stock moves; the rate of that change is gamma. Traders who are long gamma profit from volatility; those short gamma lose.
- **Probability estimation**: Delta can be loosely interpreted as the [risk-neutral probability](/intrinsic-value/) that the option finishes in the money, though this interpretation is not exact when rates and volatility vary.

## Why volatility matters

Notice that the example assumed 20% annualized volatility. If volatility were instead 40%, d₁ would be larger (less negative), and delta would be higher—perhaps 0.45 instead of 0.38. Higher volatility increases the probability that an out-of-the-money call finishes in the money, raising its delta. Conversely, lower volatility (say, 10%) would lower delta.

This is why options traders closely track [implied volatility](/implied-volatility/), the market's forecast of future volatility backed out of option prices. High implied volatility inflates delta for out-of-the-money options, making them more responsive to stock moves.

## Time decay and delta

As time to expiration shrinks, delta becomes more extreme. An at-the-money option with 30 days to go has a delta closer to 0.5 than a 90-day at-the-money option does. Far out-of-the-money options lose delta as expiration approaches, since there is less time for the stock to reach the strike. This interplay between time and delta is captured by theta, the rate at which option value decays with time.

## A put option example

For completeness, consider the same parameters applied to a put option:

Δ_put = N(d₁) − 1 = 0.377 − 1 = −0.623

The negative delta means that if the stock rises $1, the put option falls roughly $0.62. This aligns with economic intuition: put values are highest when stock prices are low. A put that is out of the money (stock above strike) has a delta closer to 0; a put that is in the money (stock below strike) has a delta closer to −1.

## Limitations of Black-Scholes delta

The Black-Scholes delta is exact only if the stock's returns are lognormally distributed, volatility is constant, and there are no dividends. In reality:

- Stocks exhibit [skew and smiles](/volatility-smile/) in their return distributions; delta from Black-Scholes is an approximation.
- Volatility is not constant; it changes day to day, leading to [gamma](/gamma/) exposure.
- Dividend-paying stocks require a modification to the formula (subtracting the present value of expected dividends from the stock price).
- Transaction costs and bid-ask spreads (especially for illiquid options) mean that the theoretical delta does not perfectly describe real trading dynamics.

For these reasons, practitioners often recalibrate delta estimates with [realized volatility](/historical-volatility/) or use more advanced models. Nevertheless, Black-Scholes delta remains the industry standard benchmark for quick option valuation and [hedging](/derivatives-hedging/) decisions.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes Model](/black-scholes-model/) — the full pricing framework
- [Gamma](/gamma/) — the second derivative of price with respect to stock price
- [Vega](/vega/) — sensitivity to volatility changes
- [Theta](/theta/) — time decay of option value
- [Implied Volatility](/implied-volatility/) — market's forecast volatility embedded in option prices
- [Strike Price](/strike-price/) — the target price in the option contract

### Wider context

- [Option](/option/) — the underlying financial instrument
- [Call Option](/call-option/) — the bullish option type
- [Put Option](/put-option/) — the bearish option type
- [Derivatives Hedging](/derivatives-hedging/) — practical use of delta in risk management
- [Covered Call](/covered-call/) — strategy combining stock and call delta
- [Risk-Neutral Probability](/intrinsic-value/) — theoretical interpretation of delta

</div>

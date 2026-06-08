---
title: "Dual Delta"
description: "The derivative of option price with respect to the strike price, equal to the risk-neutral probability of exercise and a key measure of strike-space sensitivity."
keywords:
  - dual delta
  - strike sensitivity
  - option greeks
  - risk-neutral probability
  - derivative pricing
image: "/svg/derivatives.svg"
---

*Dual delta measures how much an option's price changes when the strike price shifts by a small amount. Mathematically, it is the first derivative of the option premium with respect to the strike price, and it equals the risk-neutral probability that the option will expire in the money—a profound connection between differential calculus and probability theory.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dual Delta — strike-space sensitivity</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and pricing mechanics." />

<div class="wiki-infobox-caption">The probability of exercise, measured as a derivative in strike price.</div>

|   |   |
|---|---|
| **What it is** | ∂C/∂K, the change in option value per unit change in strike |
| **Equals** | −N(d2) for a call; N(−d2) for a put (risk-neutral probability) |
| **Units** | Option price per unit of strike currency |
| **Also called** | Strike delta, strike sensitivity |
| **Key use** | Hedging strike risk; understanding moneyness distribution |
| **Sign** | Negative for calls; positive for puts |

</aside>

## The bridge from calculus to probability

Dual delta is among the most elegant concepts in derivative pricing. Unlike ordinary [delta](/delta/), which captures sensitivity to the underlying spot price, dual delta measures sensitivity along a different axis: the strike price itself. When you vary the strike of an option holding spot fixed, you move the option along the range of potential exercise prices.

The stunning theoretical result is that dual delta does not merely quantify price sensitivity in a mechanical sense—it *is* the risk-neutral probability of exercise. Specifically, for a European call option under the [Black-Scholes model](/black-scholes-model/), dual delta equals −N(d2), where N(d2) is the cumulative normal distribution evaluated at the log-moneyness parameter. For a put, it equals N(−d2). This identity means that if you want to know the risk-neutral odds that an option will finish in the money, you need only compute (the negative of) dual delta.

## Computing dual delta

For a European call option under [Black-Scholes](/black-scholes-model/), the closed-form relationship is:

∂C/∂K = −e^{−rT} · N(d2)

where r is the risk-free rate, T is time to expiration, and d2 encodes the log-moneyness standardized by volatility. For a put, the formula carries opposite sign. In practice, traders and risk managers compute dual delta numerically: they value the option at strike K, then at strike K + ΔK, and divide the change in premium by ΔK.

The sensitivity is always expressed in units of option price per unit of strike price. If an option premium is quoted in dollars and the strike is also in dollars, dual delta will be a unitless probability-like number between −1 and 0 for calls (and 0 to 1 for puts), echoing its probability interpretation.

## Why dual delta matters in practice

Dual delta surfaces primarily in two contexts: theoretical understanding and hedging against strike-price risk in exotic or path-dependent derivatives.

**Probability interpretation**: When structuring a trade or sizing a position, knowing that dual delta *is* the risk-neutral probability of exercise offers immediate intuition. A call option with a dual delta of −0.30 has a 30% risk-neutral chance of expiring in the money. This connection helps portfolio managers benchmark the reasonableness of prices and understand the tails of the market's probability distribution for the underlying.

**Hedging strike exposure**: In the over-the-counter market, where strikes are often customized, traders sometimes face risk arising from strike adjustments or from path-dependent products where notional strike levels shift. Dual delta quantifies the exposure: if you have a large position in a derivative sensitive to its effective strike, you can hedge by taking an offsetting position with dual-delta exposure, much as you would use ordinary delta to hedge spot exposure.

## The sign convention and interpretation

For calls, dual delta is negative: raising the strike makes the option less valuable (further out of the money), so ∂C/∂K < 0. Conversely, for puts, raising the strike makes the option more valuable (further in the money), so ∂P/∂K > 0. This sign convention aligns with intuition: you always pay a price for moving against the optionality.

At-the-money options typically have dual delta near −0.40 for calls (roughly 40% probability of finish-ITM in the risk-neutral measure). Deep in-the-money calls have dual delta approaching 0 (nearly certain exercise; further strike rises have little effect). Out-of-the-money calls have dual delta approaching −1 in magnitude (tiny probability of exercise; each basis point of strike relief dramatically increases value). Puts display the mirrored pattern.

## Dual delta in portfolio and risk systems

Large institutional derivatives desks track dual delta as part of their comprehensive greek book. Where [delta](/delta/) tells you the spot-price risk of the position, [gamma](/gamma/) tells you how delta itself changes, and [vega](/vega/) quantifies volatility exposure, dual delta is part of the full sensitivity tensor. In systems that price portfolios across many spot and strike combinations, dual delta feeds into stress tests and scenario analysis.

For exchange-traded [options](/option/), strike levels are discrete: you cannot infinitesimally adjust the strike. There, dual delta is more of a theoretical tool. But in bespoke over-the-counter derivatives, where strike is a tunable parameter, dual delta becomes operationally relevant—particularly in structured notes, barrier products, or volatility derivatives where the exercise barrier or effective strike must be hedged.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the foundational greek measuring spot-price sensitivity
- [Gamma](/gamma/) — convexity in the spot price direction, the second derivative of option value
- [Dual Gamma](/dual-gamma/) — the second derivative with respect to strike, measuring strike-space curvature
- [Phi](/phi-greek/) — sensitivity to foreign risk-free rates in FX options
- [Dollar Delta](/dollar-delta/) — delta scaled by spot to express notional directional exposure
- [Black-Scholes Model](/black-scholes-model/) — the foundational framework for european option pricing
- Risk-Neutral Valuation — the theoretical basis linking greeks to probability measures

### Wider context

- [Option](/option/) — the fundamental derivative contract
- [Option Premium](/option-premium/) — the price of the option itself
- [Intrinsic Value](/intrinsic-value/) — the payoff if exercised immediately
- [Volatility Smile](/volatility-smile/) — the market observation that implied volatility varies by strike

</div>
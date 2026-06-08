---
title: "Dual Gamma"
description: "The second derivative of option price with respect to the strike price, measuring curvature and convexity in the strike dimension."
keywords:
  - dual gamma
  - strike curvature
  - option greeks
  - second derivative
  - derivatives pricing
image: "/svg/derivatives.svg"
---

*Dual gamma measures how [dual delta](/dual-delta/) itself changes as the strike price shifts. It is the second derivative of the option premium with respect to the strike, capturing the curvature or convexity of the option's value surface along the strike axis—a finer-grained sensitivity than dual delta alone can reveal.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dual Gamma — strike-space curvature</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and pricing mechanics." />

<div class="wiki-infobox-caption">The rate of change of strike sensitivity itself, embedded in risk-neutral probability density.</div>

|   |   |
|---|---|
| **What it is** | ∂²C/∂K², the second derivative of option value with respect to strike |
| **Equals** | e^{−rT} · n(d2) / (σ√T · S) for Black-Scholes calls (and puts) |
| **Units** | Option price per unit of strike squared |
| **Also called** | Strike gamma, strike curvature |
| **Sign** | Positive for both calls and puts |
| **Key use** | Measuring probability density; hedging strike curvature risk |

</aside>

## From first to second derivative

Just as [gamma](/gamma/) is the second derivative of option value with respect to the underlying spot price—measuring how delta changes when spot ticks—dual gamma is the second derivative with respect to strike. Where [gamma](/gamma/) tells you "how fast is my delta accelerating?", dual gamma asks "how fast is my [dual delta](/dual-delta/) accelerating?" as you move along the strike dimension.

Mathematically, dual gamma is always non-negative for both calls and puts. This makes intuitive sense: the option's payoff function at maturity is convex (kinked but never concave in strike space), so its premium curve must also display curvature everywhere. When you shift the strike upward, [dual delta](/dual-delta/) becomes less negative for a call (less pressure pushing price down), so the derivative of [dual delta](/dual-delta/) is positive.

## The probability density connection

Under the [Black-Scholes model](/black-scholes-model/), the closed-form expression for dual gamma is:

∂²C/∂K² = e^{−rT} · n(d2) / (σ√T · S)

where n(d2) is the standard normal probability density function (not cumulative), σ is volatility, T is time to maturity, and S is the spot price. The appearance of the density function n(d2) rather than the cumulative N(d2) is profound: dual gamma is essentially the risk-neutral probability *density* at the strike price. Where [dual delta](/dual-delta/) gives you the probability of exercise (the cumulative), dual gamma gives you the concentration of probability near that strike level.

Intuitively, dual gamma is largest when d2 is near zero—that is, when the strike is near the [forward price](/forward-contract/) of the underlying adjusted for volatility. There, the risk-neutral distribution is most concentrated. Far out of the money or deep in the money, where d2 is extreme, dual gamma decays toward zero: the probability density is thin in those regions, so small strike shifts have negligible effect on the option's value.

## Why dual gamma appears in practice

Dual gamma is a second-order effect, so it often takes a backseat to [delta](/delta/) and [gamma](/gamma/) in vanilla option risk management. However, it becomes important in several scenarios.

**Exotic and path-dependent products**: Instruments whose payoff depends on multiple strikes—barrier options with adjustable barriers, cliquets that reference a series of strikes, or structured notes with embedded strike-reset features—carry strike risk. Hedging that risk requires understanding how the option value curves in strike space, which is precisely what dual gamma captures.

**Volatility surface calibration**: When [market makers](/market-maker-trading/) fit models to observed option prices across many strikes, they implicitly fit the dual gamma surface. The shape of that surface encodes information about market expectations for the tail distribution. A spike in dual gamma at far-out-of-the-money strikes might indicate hedging demand or tail risk perception.

**Risk management across strikes**: A portfolio of options spanning many different strikes needs a measure of how the portfolio value changes when the entire strike grid shifts (e.g., due to a corporate action, an index rebalance, or currency adjustment). Dual gamma aggregates to give the portfolio-level curvature along the strike dimension, just as [gamma](/gamma/) does for spot.

## The relationship to dual delta and dual vega

The three "dual" greeks form a coherent system in strike space:

- [Dual delta](/dual-delta/) (∂C/∂K) tells you the marginal change in option value per unit of strike shift.
- Dual gamma (∂²C/∂K²) tells you how fast that marginal change accelerates.
- Dual vega would measure sensitivity to changes in the volatility parameter associated with that strike—a more advanced concept, blending strike and volatility dimensions.

For practical portfolio hedging, traders often combine ordinary [gamma](/gamma/) and dual gamma to manage both spot and strike curvature simultaneously. A position might be [gamma](/gamma/)-neutral (flat in spot convexity) but still carry dual gamma exposure if the strikes used in hedges are misaligned with the portfolio's own strike distribution.

## Computing and monitoring dual gamma

Numerical computation is straightforward: value the option at strikes K − ΔK, K, and K + ΔK, then apply the finite-difference formula for the second derivative:

∂²C/∂K² ≈ [C(K+ΔK) − 2C(K) + C(K−ΔK)] / (ΔK)²

The choice of ΔK matters for numerical stability, as is always the case with finite differences. In a production system, most risk engines compute all the greeks analytically or semi-analytically from the pricing model, reserving numerical differentiation for model validation or debugging.

Dual gamma is typically monitored in percentage terms: what fraction of the option's remaining time value is stored in strike curvature? A high dual gamma relative to the option's vega suggests that strike shifts pose material risk relative to volatility shifts. Conversely, a low dual gamma indicates that the option's value is relatively linear in strike, so [dual delta](/dual-delta/) is a stable measure of strike risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — convexity in spot price space, the foundational measure of delta acceleration
- [Dual Delta](/dual-delta/) — the first derivative with respect to strike; the risk-neutral probability of exercise
- [Phi](/phi-greek/) — sensitivity to the foreign risk-free rate in FX options
- [Dollar Delta](/dollar-delta/) — delta scaled by notional exposure for absolute directional risk
- [Vega](/vega/) — sensitivity to changes in implied volatility
- [Black-Scholes Model](/black-scholes-model/) — the framework linking dual gamma to probability density

### Wider context

- [Option](/option/) — the fundamental derivative contract
- [Option Premium](/option-premium/) — the price that dual gamma helps measure
- [Volatility Smile](/volatility-smile/) — how implied volatility varies across strikes, interacting with dual gamma
- Option Greek — the broader family of price sensitivities

</div>
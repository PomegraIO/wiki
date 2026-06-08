---
title: "Zomma"
description: "The third-order derivative measuring how gamma changes as implied volatility changes, revealing convexity in both price and volatility dimensions."
keywords:
  - third-order greek
  - gamma volatility sensitivity
  - option greeks
  - derivatives risk
image: "/svg/derivatives.svg"
---

*Zomma is a third-order Greek that measures how an option's [gamma](/gamma/) (delta sensitivity) responds to changes in implied volatility. It is a hybrid measure of convexity, connecting price-space dynamics ([gamma](/gamma/)) with volatility-space dynamics ([vega](/vega/)), and reveals how stable an option's hedge ratios are under volatility regimes shifts.*

## The third-order frontier

Traders who work with delta, [gamma](/gamma/), and [vega](/vega/) live in a two-dimensional risk landscape: how the option reacts to price moves (delta and gamma) and how it reacts to volatility moves (vega). Zomma opens a third dimension: how do the price sensitivities themselves change when volatility changes?

A concrete example: a short gamma position (negative gamma) becomes more costly when volatility rises, because the option buyer is willing to pay more for the convexity. But the magnitude of gamma exposure also shifts. Zomma quantifies that shift. If you are short gamma and volatility spikes, your gamma exposure might increase (positive zomma) or decrease (negative zomma) depending on the option's strike, expiry, and the shape of the volatility surface.

Formally, zomma is the third partial derivative of option price: the derivative of gamma with respect to implied volatility. It is rarely mentioned in casual trading, but it becomes unavoidable for traders managing large or dynamic portfolios where gamma and vega exposures interact.

## When zomma matters in practice

Consider a long call spread: long a call at strike K, short a call at strike K+10. The position has limited upside but collects some time decay. Its gamma is nearly zero near the short call strike because one leg's positive gamma is offset by the other's negative gamma. But as volatility rises, the two legs' gamma profiles shift at different rates — the long call gains more gamma sensitivity to vol than the short call loses. Zomma captures this divergence and determines whether the spread's effective gamma exposure increases or shrinks.

During volatility spikes, zomma becomes visceral. A trader holding a seemingly gamma-neutral book might discover that the book's gamma exposure has drifted because zomma was non-zero across the positions. This forces unplanned rebalancing and can leave the trader whipsawed if volatility is rising quickly.

Portfolio managers using [volatility smile](/volatility-smile/) models must account for zomma because smiles shift dynamically. When skew steepens (as it often does in equity markets after downturns), out-of-the-money puts experience larger gamma changes than at-the-money options, and zomma is the mechanism driving that separation.

## Computing zomma

In the Black–Scholes framework, zomma has a closed analytical form, but it is rarely cited because it is the product of several terms and depends on the Black–Scholes parameters: spot, strike, rate, time, and volatility. Practitioners compute zomma numerically by shocking volatility (say, +1%) and recalculating gamma, then dividing the change in gamma by the volatility shock. Most risk systems compute it automatically as part of daily Greeks updates.

Zomma is typically small compared to gamma or vega on an absolute basis, but its impact compounds over time. A portfolio with positive zomma benefits when volatility is expected to rise and gamma exposure is wanted; negative zomma becomes costly in those scenarios.

## Zomma across the volatility surface

Not all options have the same zomma. At-the-money options tend to have the highest zomma magnitude in absolute terms, while deep out-of-the-money options can have zomma that changes sign across volatility levels. The volatility smile introduces surface-specific zomma effects that pure Black–Scholes models cannot capture.

In stochastic volatility models, zomma is more complex because gamma itself depends on the path of volatility, not just the current level. Some options exhibit time-varying zomma that is highest near expiry, while others show relatively stable zomma far from expiry. These nuances matter for hedging strategies that must hold firm over long periods.

## Zomma in tail-risk management

When market stress unfolds, volatility does not move in isolation; at the same time, the price convexity of out-of-the-money options intensifies. Zomma is a leading indicator of this co-movement. A portfolio heavy in long out-of-the-money puts has positive zomma: as volatility rises (signalling stress), gamma exposure surges, making the put position more sensitive to further price moves.

Conversely, a short volatility position with negative zomma is especially dangerous in a crisis. As volatility explodes, gamma exposure worsens, forcing the trader to sell into falling prices — a vicious feedback loop. Risk managers who ignore zomma may be blindsided by how quickly a seemingly manageable position becomes unhedgeable.

## Practical implications for rebalancing

A trader who rebalances delta-gamma risk manually (rather than continuously) must understand zomma to anticipate how rebalancing needs will evolve. If you expect volatility to rise and your book has negative zomma, you know that gamma exposure will increase, demanding more frequent delta rebalancing. If zomma is positive, you can afford slightly fewer rebalancing cycles.

In algorithmic trading systems, zomma is often hard-coded as a secondary stress parameter. A trader might set an acceptable gamma range given current volatility and an expected volatility move, then monitor zomma to see if that range is likely to be breached.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — first derivative with respect to price; zomma measures its volatility sensitivity
- [Vega](/vega/) — volatility sensitivity; zomma bridges gamma and vega
- [Volga](/volga/) — second derivative of price with respect to volatility; zomma links gamma to volga
- Greeks — the full family of option risk measures
- [Implied volatility](/implied-volatility/) — the input that zomma measures gamma's sensitivity to
- [Black–Scholes model](/black-scholes-model/) — framework for computing zomma analytically

### Wider context

- [Option](/option/) — zomma applies to all option contracts
- Derivatives — third-order Greeks are essential for sophisticated risk management
- [Volatility smile](/volatility-smile/) — introduces zomma patterns across strikes
- Stochastic volatility — models that capture dynamic zomma effects
- [Value-at-risk](/value-at-risk/) — zomma contributes to tail-risk stress tests

</div>

---
title: "DDelta"
description: "The second partial derivative of option value with respect to changes in volatility; measures sensitivity to volatility changes after accounting for vega."
keywords:
  - option greeks
  - volatility sensitivity
  - second derivative
  - hedging parameter
---

*The **DDelta** (sometimes written as dDelta or ∂²C/∂σ²) is the second partial derivative of an [option](/wiki/option/) price with respect to [volatility](/wiki/implied-volatility/). It measures how the [delta](/wiki/delta-option-greeks/) of an option changes as implied volatility shifts. In other words, it captures the convexity of the delta-to-volatility relationship—whether delta becomes more or less sensitive at the edges of the [volatility](/wiki/implied-volatility/) range.*

<aside class="wiki-infobox">

| Property | Meaning |
|---|---|
| **Definition** | ∂²C / (∂σ ∂σ) or ∂V / ∂σ² |
| **Units** | Option price per 1% vol change squared |
| **Sign for calls** | Positive (convex) |
| **Sign for puts** | Negative (concave) |
| **Practical use** | Volatility hedging refinement |
| **Related greeks** | [Vega](/wiki/vega-option-greeks/), [Gamma](/wiki/gamma-option-greeks/) |

</aside>

## Understanding second-order volatility sensitivity

Option traders typically monitor [vega](/wiki/vega-option-greeks/) to gauge exposure to volatility moves. A [call option](/wiki/call-option/) with vega of 0.15 will gain $0.15 for every 1% rise in implied volatility (all else equal). But this relationship is not linear. As volatility climbs, the sensitivity of the option price to further volatility moves changes—the option's vega itself changes. DDelta quantifies this higher-order effect.

Consider a long straddle (long call + long put) on a stock. The trader buys [volatility](/wiki/implied-volatility/) exposure, expecting a large move. Both the call and put are [at-the-money](/wiki/at-the-money/). When realized volatility spikes, implied volatility typically rises alongside it, boosting the straddle's value. But the relationship is non-linear: the first 10 percentage-point jump in vol has a bigger impact than the second 10-point jump. DDelta quantifies this diminishing sensitivity.

## The relationship to vega and gamma convexity

[Vega](/wiki/vega-option-greeks/) is ∂C/∂σ. If we take the derivative of vega with respect to volatility, we get DDelta. This is analogous to the relationship between [delta](/wiki/delta-option-greeks/) and [gamma](/wiki/gamma-option-greeks/): gamma is the second derivative of price with respect to the underlying [stock](/wiki/stock/) price, and it tells you how delta changes.

For a standard long [call](/wiki/call-option/), both gamma and DDelta are positive. This means:
- As the stock rises, delta increases toward 1.0 (gamma > 0)
- As volatility rises, vega decreases (DDelta < 0 for calls in some parameterizations; conventions vary)

Most textbooks use a sign convention where DDelta is negative for [calls](/wiki/call-option/) and positive for [puts](/wiki/put-option/), reflecting that higher volatility increases the value of [out-of-the-money](/wiki/out-of-the-money/) options (where vega is high) but decreases the marginal vega of [in-the-money](/wiki/in-the-money/) options.

## Practical hedging applications

In practice, DDelta is a second-order correction to vega hedging. A portfolio manager holding a large position in long-dated [volatility](/wiki/implied-volatility/) derivatives (straddles, strangles, variance swaps) cares about how the hedge ratio changes when volatility itself moves. A high DDelta exposure means the portfolio's vega sensitivity will shift sharply if volatility spikes—a risk that a pure vega-neutral hedge does not capture.

Systematic traders, particularly those running [high-frequency trading](/wiki/high-frequency-trading/) strategies or [volatility](/wiki/volatility-swap/) arbitrage, compute DDelta to refine their [risk models](/wiki/value-at-risk/). They use DDelta alongside [vega](/wiki/vega-option-greeks/), [gamma](/wiki/gamma-option-greeks/), and [theta](/wiki/theta-option-greeks/) to forecast P&L across volatility regimes.

## Sensitivity across moneyness and expiration

DDelta is largest for [at-the-money](/wiki/at-the-money/) options with moderate time to [expiration](/wiki/option-expiration/). Out-of-the-money options have high vega (vol moves matter a lot), but the vega itself is stable relative to small vol changes—so DDelta is small. Deep [in-the-money](/wiki/in-the-money/) options have low vega, and it falls further with additional vol—higher DDelta in magnitude.

Short-dated options are more sensitive to vega changes because they are closer to expiration and [implied volatility](/wiki/implied-volatility/) changes feed directly into [theta](/wiki/theta-option-greeks/) decay.

## Limitations and why practitioners rarely isolate it

Most risk systems report vega, gamma, and theta. DDelta is a higher-order Greek that few traders quote in daily conversations. It is implicit in vega's behavior but rarely hedged separately. Instead, traders use [variance swaps](/wiki/variance-swap/) and [volatility](/wiki/volatility-swap/) swaps to gain pure volatility exposure, sidestepping the non-linear sensitivity altogether.

In [Black-Scholes](/wiki/black-scholes-model/) models, DDelta has a closed form, but it is rarely used because practitioners find gamma hedging (on the underlying stock) and vega hedging (with options or variance swaps) sufficient for most portfolios. DDelta becomes material only when the portfolio is extremely large or extremely sensitive to vol-of-vol (second-order volatility of volatility movements).

<div class="wiki-seealso">

### Closely related
- [Vega (option greeks)](/wiki/vega-option-greeks/) — First derivative with respect to volatility
- [Gamma (option greeks)](/wiki/gamma-option-greeks/) — Second derivative with respect to price
- [Theta (option greeks)](/wiki/theta-option-greeks/) — Time decay sensitivity
- [Delta (option greeks)](/wiki/delta-option-greeks/) — Primary price sensitivity

### Wider context
- [Black-Scholes model](/wiki/black-scholes-model/) — Closed-form option pricing
- [Implied volatility](/wiki/implied-volatility/) — The input that vega and DDelta measure
- [Variance swap](/wiki/variance-swap/) — Pure volatility exposure without non-linearity
- [Options greeks](/wiki/options-greeks/) — Complete greek family

</div>

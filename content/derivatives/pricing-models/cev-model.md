---
title: "Constant Elasticity of Variance Model"
description: "A local-volatility option pricing model where volatility changes inversely with stock price, generating leverage effects and volatility skew."
keywords:
  - constant elasticity of variance
  - cev model
  - local volatility
  - leverage effect
  - option pricing
image: /svg/derivatives.svg
---

*The **constant elasticity of variance (CEV) model** is an option pricing framework where volatility is not constant but depends on the stock price level. As the stock falls, volatility rises—a relationship rooted in financial leverage: when a company's equity shrinks relative to its fixed debt, equity becomes riskier and more volatile. The CEV model captures this leverage effect through a single elasticity parameter, generating a [volatility smile](/volatility-smile/) without introducing jumps or stochastic volatility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Constant Elasticity of Variance Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for quantitative derivatives pricing." />

<div class="wiki-infobox-caption">Local volatility determined by the stock price level; the simplest model capturing the leverage effect.</div>

|   |   |
|---|---|
| **What it is** | A deterministic-volatility option pricing model where σ = σ₀ × S^(β−1) |
| **Also called** | CEV model; special cases include Black-Scholes (β=1) and square-root (β=0.5) |
| **Key advantage** | Produces realistic [volatility skew](/volatility-smile/) with a single elasticity parameter |
| **Parameters** | Initial volatility σ₀, elasticity β (0 ≤ β ≤ 1) |
| **β = 1** | Black-Scholes constant volatility |
| **β < 1** | Inverse leverage: lower stock price → higher volatility (typical equity) |
| **Limitation** | No closed-form pricing; numerical schemes required for most strikes |

</aside>

## The leverage effect: why volatility moves with the stock price

The CEV model rests on a simple observation: a company's equity is the residual claim on assets after debt is paid. When the stock price falls, the equity cushion shrinks relative to the fixed debt obligation. The same movements in asset value now produce larger percentage swings in equity value. A 10% loss in asset value might cause a 20% loss in equity—higher leverage, higher volatility.

This is not a market sentiment story; it is pure accounting. A firm with assets worth $100m and debt worth $80m has equity worth $20m. If assets fall to $90m, equity falls to $10m—a 50% move from a 10% asset move. The lower the equity value, the higher the beta, and the higher the required [return](/return-on-equity/). Volatility follows.

The Black-Scholes model treats volatility as constant—unrealistic for equities. The CEV model lets volatility scale with price, capturing this mechanical effect.

## The CEV volatility function

The CEV model specifies that the local volatility follows:

σ(S) = σ₀ × S^(β−1)

where *S* is the stock price, σ₀ is a reference volatility (typically the initial price volatility), and *β* is the elasticity parameter.

When β = 1, volatility is constant (the Black-Scholes case). When β < 1 (the empirically relevant regime for equities), volatility increases as the stock price *decreases*. This inverse relationship generates the characteristic downward-sloping [volatility skew](/volatility-smile/) observed in equity [options](/option/): out-of-the-money [puts](/put-option/) are more expensive than out-of-the-money [calls](/call-option/) because the deeper the put goes into the money, the higher the local volatility on the path to that strike.

A typical estimate for equities is β ≈ 0.5 to 0.7. For example, with β = 0.5, if the stock is at $100 and volatility is 20%, then at a stock price of $50, volatility would be approximately 20% × (100/50)^0.5 ≈ 28%.

## Generating the observed volatility skew

The Black-Scholes model produces a flat implied volatility surface—all [options](/option/) at all strikes have the same implied volatility, regardless of moneyness. Empirically, this is false. [Put options](/put-option/) trade at higher implied volatility than [calls](/call-option/), particularly when out of the money. This skew is a persistent feature of equity [option](/option/) markets.

The CEV model produces a skew naturally. Suppose a stock at $100 has volatility of 20% under CEV with β = 0.7. As the stock price path falls toward a strike at $80, the local volatility on the path rises. This higher realized volatility increases the probability of landing deep in the money at the put's maturity. As a result, the put's price rises more steeply as the strike falls, and its implied volatility rises.

Conversely, [call options](/call-option/) become less valuable at lower strikes because the local volatility rises, but the call's upside is capped. The ratio of put price to call price widens as strikes fall, creating the skew.

## Why β < 1 makes financial sense

When β > 1, volatility *increases* with the stock price—a counterintuitive relationship. Under this regime, the more valuable the firm becomes, the riskier its equity. This occurs only in exotic cases, such as distressed debt or options on illiquid assets. For normal, solvent equities, β < 1.

The lower bound is β = 0. This extreme case, sometimes called the "square-root" CEV model (when combined with specific parameterizations), produces a volatility term structure that prevents the stock price from crossing zero—it becomes absorbing. This is unrealistic for most equities but has niche applications in credit-risk modeling.

## Pricing CEV options: numerical methods required

Unlike Black-Scholes, the CEV model admits no closed-form formula for [option](/option/) prices. Instead, practitioners use numerical schemes:

- **Finite-difference methods** solve the pricing PDE directly on a grid.
- **Trinomial lattices** discretize the stock-price path and build backward recursively.
- **Monte Carlo simulation** samples stock-price paths under the CEV dynamics.

Each method has trade-offs. Finite-difference schemes (especially Crank-Nicolson) are fast and accurate for European [options](/option/) but require careful handling of the boundary at stock price = 0 when β is small. Trinomial lattices converge reliably but can be memory-intensive for long maturities. Monte Carlo is flexible and handles path-dependent [options](/option/) well but can be slow for high-precision pricing.

For American [options](/option/), which allow early exercise, lattice methods and finite-difference schemes with free-boundary conditions are most practical.

## The CEV model in practice

The CEV model is widely used in equity [option](/option/) desks and risk management systems, particularly for single-stock [options](/option/) where the leverage effect is pronounced. It is simpler than stochastic volatility models like Heston and often fits the skew more parsimoniously.

However, the CEV model has limitations. It produces a smile (U-shaped implied volatility) for low β, whereas real equity [options](/option/) more often show a pronounced skew (downward-sloping). In periods of high uncertainty, the skew can steepen or flatten, changes the CEV model cannot capture without re-calibration. For longer-dated [options](/option/), term-structure effects (the skew evolving over time) become important; CEV is a static framework.

Some firms blend the CEV model with stochastic volatility or jump-diffusion extensions to handle these cases, though this adds complexity.

## CEV versus Heston and alternatives

The Heston model treats volatility as a separate stochastic process, allowing it to evolve independently of the stock price. This flexibility makes Heston more adaptable to changing market regimes. However, Heston requires fitting more parameters and typically has no closed-form prices for American [options](/option/).

The [Constant Elasticity of Variance Model](/cev-model/) is simpler and faster—a single elasticity β captures the leverage effect without introducing a second random driver. For vanilla equity [options](/option/), especially in regimes where leverage dominates the skew, CEV often works as well as Heston and is cheaper to compute.

Jump-diffusion models (Merton) add discrete jumps on top of diffusion, useful for capturing market events. For normal equity [options](/option/), CEV is often a cleaner choice.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes Model](/black-scholes-model/) — the constant-volatility benchmark (β=1 case)
- [Volatility Smile](/volatility-smile/) — the empirical smile and skew that CEV generates
- [Option](/option/) — the derivative contract priced under CEV
- [Variance Gamma Model](/variance-gamma-model/) — an alternative pure-jump model for skew
- [Trinomial Option Pricing](/trinomial-option-pricing/) — a lattice method for numerical CEV pricing
- [Finite Difference Methods for Options](/finite-difference-methods-options/) — another numerical approach

### Wider context

- Stochastic Volatility — a more general framework with independent volatility dynamics
- [Leverage Ratio](/leverage-ratio-forex/) — the financial leverage concept underlying the CEV model
- Risk Management — how CEV skew feeds into hedge ratios and Greeks

</div>

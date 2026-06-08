---
title: "Displaced Diffusion Model"
description: "A simple shift of the lognormal Black model that accommodates negative interest rates without switching to a full normal model."
keywords:
  - displaced diffusion
  - negative interest rates
  - black model
  - swaption pricing
  - shifted lognormal
  - interest rate model
image: /svg/derivatives.svg
---

*The **Displaced Diffusion Model** is a pragmatic fix to the [LIBOR Market Model](/lmm-libor-market-model/) and Black's framework when [interest rates](/interest-rate/) go negative. It shifts the lognormal diffusion upward by a fixed displacement, allowing negative values while preserving the mathematical convenience of lognormal volatility.*

## The problem: lognormality breaks down at negative rates

Under the classic [LIBOR Market Model](/lmm-libor-market-model/), forward LIBOR rates follow a lognormal distribution. That is, the logarithm of the rate is normally distributed. Lognormality forbids negative values: if a rate is lognormal, it cannot be negative because you cannot take the logarithm of a negative number in real arithmetic.

From 2008 onward, central banks in Switzerland, the eurozone, and Japan pushed policy rates below zero. Market participants began quoting negative [LIBOR](/interest-rate/) rates—a shock to anyone trained on the old assumption that rates are always positive. The Black framework and the LIBOR Market Model, as originally formulated, could not accommodate these negative quotes without switching to a completely different distribution.

Switching to a normal (Gaussian) distribution solves the negative-rate problem but costs something: normal distributions do not have a closed-form Black formula for caps and swaptions. A trader loses the closed-form cap-pricing formula that made the LIBOR Market Model transparent.

## A simple shift: displaced diffusion as the middle ground

Displaced diffusion is a surgical patch. Instead of allowing the forward rate *f* to be lognormal, you allow *f* + *d* to be lognormal, where *d* is a fixed shift (displacement). The displaced rate follows:

d(*f* + *d*) = *μ* d*t* + *σ* d*W*

Or equivalently:

d*f* = *μ* d*t* + *σ* d*W*

The forward rate *f* is still driven by the same lognormal process, but shifted. If the displacement *d* is positive, then *f* can go as low as −*d* (where the shifted value *f* + *d* is zero). If the current rate is −0.3% and you set *d* = 1%, then *f* + *d* = 0.7%, and *f* stays above −1% in practice.

The displacement parameter is calibrated to market data. A negative-rate regime requires a larger displacement; a positive-rate regime can use a small displacement (or zero, recovering pure lognormality).

## Preservation of Black's formula

Here is the elegant part: under displaced diffusion, the cap pricing formula barely changes. A caplet with strike *K* on a forward rate *f* has payoff max(*f* − *K*, 0). Under displaced diffusion, the caplet formula uses Black's formula with:

- **Moneyness adjusted**: (*f* + *d*) / (*K* + *d*) replaces *f* / *K*
- **Volatility scaled**: *σ* × (*f* + *d*) / *f* replaces *σ*

The adjustment is simple algebra, and traders can compute cap prices in milliseconds. No simulation, no loss of the closed-form convenience that made lognormality popular.

## When displaced diffusion applies (and when it doesn't)

Displaced diffusion is standard for pricing caps, floors, and swaptions when rates are negative. A trader will quote a swaption volatility at 1.2%, calibrate a displacement to match the current curve (typically 0.5% to 2%), and price any swaption or Bermuda swaption using that framework.

It works best for derivatives that are "not too far out of the money." If you are pricing a 5% cap when the current forward rate is −0.5%, the effective strike is (5 + 1) = 6 and the forward is 0.5, a ratio of 12:1—a far-out-of-the-money call. Displaced diffusion still works, but the result is extremely sensitive to the displacement assumption.

For exotic derivatives with path-dependent payoffs, displaced diffusion is the input volatility model, but a full simulation (Monte Carlo or trees) is required to compute the derivative price.

## Calibration: choosing the displacement

In practice, the displacement *d* is determined one of two ways.

First, use historical data. If you observe the range of forward LIBOR rates over the past 10 years and they've touched −0.5%, you might set *d* = 0.6% to ensure the lognormal shifted process cannot be driven that low by noise alone. This is a safety margin approach.

Second, calibrate to swaption implied volatilities. If the market quotes a swaption vol and the ATM forward is negative, you solve for the displacement that makes the model's option price match the market price. Then apply that displacement to all subsequent caps and swaptions consistently.

The first approach is simpler but ad-hoc. The second is more rigorous but requires live market data and frequent recalibration.

## Why not always use normal distributions?

The normal model (where rates diffuse additively, not multiplicatively) avoids the displacement question entirely: negative rates are native to normal geometry. Yet normal models are less popular, in part because they require numerical integration for cap prices. Black's formula does not apply; traders must integrate a normal density, adding latency to a trading system.

Displaced diffusion splits the difference: it keeps most of the computational simplicity of lognormality while permitting negative rates. For most fixed-income trading desks, that trade-off is acceptable.

## Limitations and trade-offs

Displaced diffusion is a patch, not a fundamental model. It constrains the volatility smile in ways that may not match reality. A trader using displaced diffusion with fixed *d* will find that the implied volatility smile looks different from the market's implied smile across different strikes. For pricing exotic derivatives that are sensitive to skew and smile, a more sophisticated model (like SABR stochastic volatility) might be needed.

Also, displaced diffusion is less elegant than pure lognormality or pure normality. It is a hybrid born of necessity, not theory. That makes it harder to teach and to extend.

## Practical use in a negative-rate world

Since 2015, when rates in major markets turned negative and stayed there, displaced diffusion has become standard. A quantitative analyst at a bank building a cap-pricing system will almost certainly implement displaced diffusion as the baseline framework, with SABR or other stochastic-volatility models as overlays for exotic sensitivity.

The displacement parameter is a tuning knob that captures the "how negative can rates realistically go?" question without resorting to full Monte Carlo. For daily risk management of thousands of positions, that computational efficiency matters.

## Relation to other frameworks

The [LIBOR Market Model](/lmm-libor-market-model/) is displaced diffusion's spiritual parent. LIBOR Market Model prices caps and swaptions using lognormal forward rates; displaced diffusion is the same idea with a shift to handle negative rates.

The [Hull-White Model](/hull-white-model/) is Gaussian natively (rates can go negative), but requires more complex calibration and is usually applied to short rates, not forward LIBOR.

The [Cox-Ingersoll-Ross Model](/cir-model/) stays non-negative by design through a square-root structure, avoiding the issue entirely—at the cost of computational complexity and affine-structure constraints.

SABR and other stochastic-volatility models add a second source of randomness to handle the volatility smile more flexibly than any single-volatility displaced diffusion can.

## See also

<div class="wiki-seealso">

### Closely related

- [LIBOR Market Model](/lmm-libor-market-model/) — parent framework; lognormal forward rates for caps and swaptions
- [Hull-White Model](/hull-white-model/) — Gaussian short-rate alternative that handles negative rates natively
- [Cox-Ingersoll-Ross Model](/cir-model/) — square-root structure preventing negative rates by design
- [Black-Scholes Model](/black-scholes-model/) — underlying option formula adapted by displaced diffusion
- [Implied Volatility](/implied-volatility/) — market volatility used for calibration
- [Volatility Smile](/volatility-smile/) — deviation from constant vol that displaced diffusion may miss

### Wider context

- [Interest Rate](/interest-rate/) — underlying economic variable
- Interest-Rate Derivatives — caps, floors, swaptions
- [Option Premium](/option-premium/) — value pricing
- Derivatives — broader asset class
- [Yield Curve](/yield-curve/) — term structure context

</div>

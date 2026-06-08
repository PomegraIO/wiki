---
title: "Cox-Ingersoll-Ross Model"
description: "A square-root short-rate model with mean reversion that enforces non-negative interest rates through its diffusion process."
keywords:
  - cox ingersoll ross
  - cir model
  - square root process
  - short rate model
  - mean reversion
  - non-negative rates
  - bond pricing
image: /svg/derivatives.svg
---

*The **Cox-Ingersoll-Ross (CIR) Model** is a one-factor [interest-rate model](/interest-rate/) where the short rate evolves with mean reversion and a square-root diffusion term that naturally prevents rates from going negative. It trades mathematical elegance for computational complexity, and remains a standard reference in fixed-income theory.*

## Keeping rates non-negative by design

The central innovation of the CIR model is structural. Instead of allowing the short rate to wander freely (as in the [Hull-White Model](/hull-white-model/)) or adopting a lognormal form (as in LIBOR frameworks), CIR uses a square-root process:

d*r* = *a*(*b* − *r*) d*t* + *σ* √*r* d*W*

The term √*r* is the key. When the short rate *r* is near zero, the volatility (the √*r* coefficient) shrinks toward zero, dampening the random shock. Rates cannot drift below zero because the mathematics forbids it: if *r* were to go negative, √*r* would be undefined in real numbers. The square root acts as a barrier, gently repelling rates upward when they approach zero.

This is theoretically elegant. The model respects economic intuition: borrowing costs cannot be negative in a literal sense (you can't pay someone to take your loan, at least not in the real world). The CIR model builds this constraint into the physics, not as an ad-hoc rule.

## Mean reversion toward a long-run equilibrium

The drift term *a*(*b* − *r*) embodies mean reversion. The parameter *a* controls how fast rates pull back toward their long-run mean *b*. If the current rate is 1% and the long-run rate is 3%, then the drift is positive, pulling the rate upward. If rates spike to 8%, the drift becomes negative, dragging them back down.

This reversion is economically sensible. Central bank policy has long-run anchors (e.g., a 2% inflation target), and [market interest rates](/interest-rate/) oscillate around those anchors. A rate model without mean reversion would imply that rates drift forever higher or lower, an absurd proposition over decades.

Both the CIR and [Hull-White models](/hull-white-model/) include mean reversion. The difference is CIR's square-root volatility structure, which ties volatility to the level of rates, and CIR's non-negativity constraint.

## Bond pricing and affine models

A profound mathematical fact: in the CIR model, zero-coupon bond prices have an affine (exponential-linear) form. That is, the log price is a linear function of the current short rate and time-to-maturity. This closure property is rare and precious.

Affine structure means that many derivatives have semi-closed-form solutions or can be priced using Fourier methods without brute-force simulation. Bond prices, bond-option prices, and certain swaption prices can be computed via formulas or numerical integration over a characteristic function. This makes CIR tractable for risk managers who need Greek calculations every few seconds.

## Calibration challenges: data is messier than the theory

The CIR model has only three parameters: the mean-reversion speed *a*, the long-run rate *b*, and volatility *σ*. For pricing vanilla derivatives, that sparsity is appealing. But when you fit the model to historical [yield curves](/yield-curve/), you discover that a single *σ* cannot explain the variation across different maturities.

The observed volatility of short rates differs from the observed volatility of long rates. CIR's constant *σ* cannot capture this term-structure dependence of volatility. Extensions like the two-factor CIR model or hybrid models (CIR + a long-rate factor) add flexibility at the cost of losing the affine structure that made CIR attractive.

Modern practitioners often use [displaced diffusion](/displaced-diffusion-model/) variants or stochastic-volatility overlays (like SABR) to bend the volatility surface into shape, sacrificing some of CIR's mathematical purity.

## Negative rates force a reckoning

From 2008 onward, when [LIBOR](/interest-rate/) rates went negative in parts of Europe and Asia, the CIR model's defining feature—non-negativity—became a constraint, not a feature. If the market was quoting a negative three-month LIBOR, a trader using CIR had to ask: should I adjust the model, or am I mis-pricing the market?

Some practitioners shifted to normal models or explicitly allowed negative rates by shifting the CIR process upward (creating a [displaced diffusion](/displaced-diffusion-model/) variant). Others argued that CIR's non-negativity was a feature, not a bug: negative rates are a policy quirk, not a natural economic state, and hedging books should not be distorted by abnormal central-bank interventions.

That debate reflects a deeper tension: CIR is ideologically pure, but empirically constrained. Reality is messier than theory.

## Computational trade-offs: affine structure vs. complexity

Bond prices in CIR have a closed form, as do some swaption prices. For these vanilla cases, CIR is fast. But for path-dependent payoffs (range accruals, Bermuda swaptions, leveraged floaters), even affine structure doesn't produce a formula. A trader must resort to simulation or a trinomial tree.

Trees for CIR are more subtle than trees for [Hull-White](/hull-white-model/). The square-root volatility means that state-space discretization must be careful: a naive tree might violate non-negativity if step sizes are too large. Practitioners use alternative discretization schemes (e.g., QE scheme) to preserve the square-root property on a lattice.

For an overnight risk-management system pricing 10,000 bonds and 5,000 derivatives across multiple scenarios, the model choice is crucial. Hull-White's Gaussian structure is simpler to implement. CIR's affine structure is more compact for some calculations but requires specialized solvers.

## Relation to other frameworks

The [Hull-White Model](/hull-white-model/) is CIR's main competitor: both are one-factor short-rate models with mean reversion. Hull-White is Gaussian (rates can go negative but usually don't), has exact fit to the yield curve via time-dependent drift, and is computationally straightforward. CIR is non-negative by construction, affine, but more complex to calibrate and implement.

The [LIBOR Market Model](/lmm-libor-market-model/) is an alternative philosophy: instead of modeling a single short rate, it models forward LIBOR rates directly, making caps and swaptions transparent. LIBOR Market Model is higher-dimensional and requires simulation for many payoffs.

[Displaced diffusion](/displaced-diffusion-model/) is a practical patch that lets traders use CIR-like models even when rates are negative.

## Enduring legacy: theory and practice

Despite its computational demands, CIR remains a standard reference in academic fixed-income research and in the curricula of quantitative finance programs. Its theoretical elegance—the affine structure, the non-negativity, the closed-form bond prices—makes it a teaching vehicle for understanding how interest-rate models work.

In practice, most trading desks have migrated to simpler models (Hull-White, or LIBOR Market Model for caps) or more flexible frameworks that handle negative rates without strain. But CIR's influence lives on in textbooks and in the thinking of risk managers who learned that volatility should shrink with rates.

## See also

<div class="wiki-seealso">

### Closely related

- [Hull-White Model](/hull-white-model/) — simpler Gaussian alternative; easier to calibrate, less theoretically constrained
- [LIBOR Market Model](/lmm-libor-market-model/) — forward-rate framework; higher dimensionality, more direct cap/floor calibration
- [Displaced Diffusion Model](/displaced-diffusion-model/) — shifted process allowing negative rates while preserving square-root structure
- Interest-Rate Derivatives — bonds, caps, floors, swaptions
- [Yield Curve](/yield-curve/) — term structure the model must reconcile with
- [Mean Reversion](/interest-rate/) — economic concept embedded in all three models

### Wider context

- [Interest Rate](/interest-rate/) — underlying economic variable
- [Bond](/bond/) — primary asset
- Bond Option — common derivative class
- [Interest-Rate Risk](/interest-rate-risk/) — hedging goal
- Affine Structure — mathematical technique in quantitative finance

</div>

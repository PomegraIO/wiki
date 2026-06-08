---
title: "Hull-White Model"
description: "A one-factor short-rate model with mean reversion that fits the initial yield curve for pricing interest-rate derivatives."
keywords:
  - hull white model
  - short rate model
  - mean reversion
  - interest rate derivatives
  - yield curve fitting
  - bond option pricing
  - swaption valuation
image: /svg/derivatives.svg
---

*The **Hull-White Model** is a one-factor [interest-rate model](/interest-rate/) that captures mean reversion in short rates while fitting the current [yield curve](/yield-curve/) exactly. It prices caps, floors, bond options, and swaptions with closed-form solutions, making it a workhorse for derivative traders and risk managers.*

## The core dynamics: a single rate that pulls toward a target

The Hull-White model describes the short rate's evolution with two ingredients: a drift (mean reversion) and a random shock. The short rate doesn't wander freely; instead, it is pulled toward a time-dependent equilibrium level. If market rates are currently 2%, but the model's long-term normal rate is 3%, then the short rate drifts upward, with random noise superimposed.

Formally, the instantaneous short rate *r(t)* follows:

d*r* = (*θ*(*t*) − *a* × *r*) d*t* + *σ* d*W*

Here *a* is the mean-reversion speed, *σ* is volatility, and d*W* is a Brownian increment. The term *θ*(*t*) is a time-dependent drift that shifts each day to match today's [yield curve](/yield-curve/). That calibration step is crucial: no matter what historical short rates have done, the model adjusts its drift so that when you value a zero-coupon bond, you recover the market price exactly.

## Why one factor is enough (and when it isn't)

The Hull-White model has one source of randomness—the single Brownian increment d*W*. That simplicity is its strength. All bond prices move together (though by different amounts), all interest-rate derivatives can be priced in closed form (or with efficient trees), and the model runs in milliseconds on a trading desk.

For vanilla caps, floors, and swaptions, one factor often suffices. A trader's income depends mostly on the level of short rates, not on subtle curvature of the yield curve. But if a desk is hedging a Bermuda swaption (an option that can be exercised on many dates), or a range accrual note (a structure that accrues coupons only when rates stay in a band), one factor can miss second-order risks. More sophisticated shops use two-factor models or full LIBOR frameworks.

## Closed-form solutions for vanilla derivatives

Bond options in the Hull-White model have explicit formulas. A European call option on a zero-coupon bond reduces to a shifted [Black-Scholes](/black-scholes-model/) calculation. Swaptions—options on interest-rate swaps—also yield closed form. This is rare in interest-rate derivatives; most exotic payoffs require simulation.

The payoff of a swaption is the maximum of zero and the swap value. Under Hull-White, that maximum distributes normally (roughly), and the formula becomes a sum of bond-option formulas. Traders call this result a "closed-form swaption price," and it was a major selling point when the model was published in 1990.

## Fitting the yield curve daily

The yield curve changes every day. New bonds mature, credit spreads widen or tighten, and central banks adjust policy. The Hull-White model's time-dependent drift *θ*(*t*) re-calibrates daily. On each date, the model solves for the drift function that makes the model's bond prices match the market's zero-coupon curve exactly.

This discipline is both a strength and a weakness. Strength: the model never misprices a bond, and it remains consistent with the current curve. Weakness: all of the model's flexibility is used up in fitting *θ*(*t*), leaving only the volatility *σ* and mean-reversion speed *a* to be set by historical data or market [implied volatility](/implied-volatility/). If implied vol changes or the correlation between rates and vega shifts, the model can't adapt without retraining.

## The short-rate assumption: theoretical purity, practical friction

The Hull-White model is built on a theoretical short rate—the instantaneous rate for an infinitesimal loan. In reality, no lender will quote you a rate for an overnight loan that matures in a nanosecond. The short rate is inferred from longer bonds using [yield curve](/yield-curve/) interpolation.

This abstraction rarely causes problems because the model's hedge ratios and Greeks are computed relative to observable bond prices, not the short rate itself. A trader calculates "how much the bond-option value changes if the zero-coupon curve shifts up 1 basis point," and that is what [interest-rate risk](/interest-rate-risk/) managers care about.

## Negative rates: a design limitation exposed

The Hull-White model is Gaussian: rates can go negative. In 2008 and beyond, as central banks drove policy rates to zero and below, markets actually quoted negative [LIBOR](/interest-rate/) rates in Switzerland, the eurozone, and Japan. The model could accommodate this, at least in principle.

But the Gaussian assumption breaks down at very negative rates. A trader quoting a three-year swaption when the current zero-rate is −0.5% can't assume rates are normally distributed around −0.5%. The [LIBOR Market Model](/lmm-libor-market-model/) suffered from the same constraint, spurring adoption of [displaced diffusion](/displaced-diffusion-model/) or normal models like SABR.

## Relation to other frameworks

The [LIBOR Market Model](/lmm-libor-market-model/) and the Hull-White model are complementary. LIBOR Market Model directly simulates the forward rates traders see quoted, making cap and floor prices transparent. Hull-White models the short rate and is cheaper to compute, but its connection to market caps and floors is less direct—you have to calibrate to swaption implied vols or back out cap vols from the model.

The [CIR Model](/cir-model/) uses a square-root diffusion so rates stay non-negative by design. It is theoretically elegant but requires numerical approximation for many payoffs. Hull-White is less pure mathematically but vastly more practical.

Displaced diffusion and other extensions patch Hull-White to handle negative rates without abandoning Gaussian structure. For most modern books, these patches are standard.

## Practical use: risk management and pricing

Many banks price everyday interest-rate derivatives using Hull-White trees. An interest-rate derivative desk builds a recombining tree of short-rate values, rolls forward in time, and computes option payoffs at maturity, then steps backward to the present. This backward recursion gives the option value and all the Greeks—delta, gamma, vega, theta.

For intraday rebalancing, the computational speed of a tree or closed-form solution beats Monte Carlo simulation. For overnight risk monitoring across thousands of positions, Hull-White is often the industry standard.

## See also

<div class="wiki-seealso">

### Closely related

- [LIBOR Market Model](/lmm-libor-market-model/) — forward-rate alternative; more transparent for caps and swaptions, higher dimensionality
- [Cox-Ingersoll-Ross Model](/cir-model/) — square-root short rate that enforces non-negativity; theoretically sound, less calibration-flexible
- [Displaced Diffusion Model](/displaced-diffusion-model/) — simple shift to Hull-White allowing negative rates
- Interest-Rate Derivatives — caps, floors, swaptions, Bermudan options
- [Yield Curve](/yield-curve/) — term structure input that the model fits daily
- [Black-Scholes Model](/black-scholes-model/) — option-valuation foundation underlying bond-option solutions
- [Implied Volatility](/implied-volatility/) — market volatility used for model calibration

### Wider context

- [Interest Rate](/interest-rate/) — underlying economic driver
- [Bond](/bond/) — primary asset class
- [Interest-Rate Risk](/interest-rate-risk/) — hedging motivation
- [Option Premium](/option-premium/) — value component of derivatives
- Derivatives — broader asset class context

</div>

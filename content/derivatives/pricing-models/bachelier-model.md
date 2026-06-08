---
title: "Bachelier Model"
description: "The normal-distribution option pricing formula, ideal for near-zero or negative interest rates and forwards."
keywords:
  - normal distribution
  - option pricing
  - negative rates
  - Bachelier model
  - interest-rate derivatives
image: "/svg/derivatives.svg"
---

*The **Bachelier model** is an option pricing framework based on the assumption that the underlying asset price follows a normal (Gaussian) distribution rather than a lognormal one. Developed by Louis Bachelier in 1900—a century before it became fashionable—the model prices options in absolute price units and is now the standard for interest-rate derivatives in negative-rate environments and for highly volatile commodities where prices can swing dramatically in absolute terms.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bachelier Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">Option pricing based on normally distributed price changes, not logarithmic returns.</div>

|   |   |
|---|---|
| **What it is** | An option pricing model where the underlying asset follows a normal distribution |
| **Key insight** | Price changes are additive (dollars, not percentage returns); no lower bound of zero |
| **Distribution** | Normal (bell curve), not lognormal |
| **Main use** | Interest-rate [option](/option/) pricing in negative-rate environments; commodity [futures-contract](/futures-contract/) |
| **Also called** | Arithmetic Brownian motion model |
| **Closed-form price** | Similar to [Black-Scholes-model](/black-scholes-model/), but σ is applied to absolute price, not logarithmic return |
| **Advantage** | Handles negative forwards, better fit for rates near zero |

</aside>

## The normal assumption: price changes, not returns

The fundamental difference between Bachelier and [Black-Scholes-model](/black-scholes-model/) is how they model the underlying:

**Black-Scholes:** Assumes the stock price S follows a geometric Brownian motion:
dS = μS dt + σS dW

Here, the drift and volatility are proportional to the current price S. A 10% move is the same whether the stock trades at $100 or $1. This ensures the price never goes negative (lognormal distribution is bounded below by zero).

**Bachelier:** Assumes the forward price F follows an arithmetic Brownian motion:
dF = σ dW

The drift is zero (under the risk-neutral measure), and the volatility σ is constant in absolute terms. A $5 move has the same probability whether the forward is at $100 or $1. The resulting distribution is normal, and it is entirely possible (though unlikely if volatility is small relative to the forward price) for prices to go negative.

This seemingly small change has enormous consequences for pricing [call-option](/call-option/) and [put-option](/put-option/) when interest rates or forwards are near zero—or below it.

## When Bachelier outperforms Black-Scholes: negative rates

For decades, Bachelier remained a historical curiosity. Equity traders had no use for it; [Black-Scholes-model](/black-scholes-model/) with its lognormal assumption worked beautifully for stocks that were never negative.

But after central banks pushed short-term interest rates into negative territory (especially in Japan, the eurozone, and Switzerland), the picture changed. When a [interest-rate](/interest-rate/) forward can trade at -0.5%, the lognormal assumption becomes absurd: Black-Scholes assumes the forward price is always positive, so it cannot price a contract with a negative strike or underlying.

Bachelier handles this naturally. A normal distribution is symmetric around its mean and extends to both positive and negative values. If the forward is at 0.2% with a [volatility](/volatility-smile/) of 40 basis points, the model cheerfully assigns probability to negative outcomes.

This is why, since 2010, Bachelier has become the **de facto standard** for interest-rate cap, floor, and swaption pricing in negative-rate economies.

## The closed-form price for options

The Bachelier price for a [call-option](/call-option/) struck at K on a forward price F maturing at time T is:

C = e^(−rT) [σ√T N'(d) + (F−K) N(d)]

where:

d = (F−K) / (σ√T)
N() is the cumulative normal distribution
N'() is the probability density function (the normal bell curve)
σ is volatility in absolute terms (e.g., basis points per year)
r is the [interest-rate](/interest-rate/)

The [put-option](/put-option/) price follows by put-call parity.

Compared to Black-Scholes, the formula is simpler in one sense (no logarithm) and more transparent: the first term σ√T N'(d) is the option's time value, and (F−K) N(d) is a probability-weighted intrinsic value.

## Volatility quoting: basis points vs. percentages

A crucial practical distinction: in Bachelier models, [volatility](/volatility-smile/) is quoted in absolute terms—basis points (or dollars per contract, depending on context). In Black-Scholes, it is a percentage.

For an interest-rate swaption with a forward swap rate of 3% and a Bachelier volatility of 100 basis points per year, that volatility is literally 100 bps, or 0.01 in decimal terms. A 2-standard-deviation move over one year would span 3% ± 2(100 bps) = 1% to 5%.

By contrast, in Black-Scholes for a stock at $100 with 20% volatility, the volatility of 0.20 represents 20% of the stock price, so a 2-sigma move spans $100 × (1 ± 2 × 0.20) = $60 to $140.

This quoting convention matters for practitioners: if you see a swaption quoted at "120 vols" in a Bachelier-based system, you are looking at 120 basis points per year, not 120%. The convention is locked into trading desks, risk systems, and broker quotes worldwide.

## When prices can go negative: a feature or a bug?

The ability for prices to go negative is sometimes criticized. A real commodity like crude oil cannot have a negative price (though in March 2020, WTI futures briefly traded negative due to storage constraints, which surprised many). Nor can a stock.

But for interest rates and spreads, negativity is acceptable and sometimes observed. When a [interest-rate](/interest-rate/) forward is already negative, the normal distribution is simply more honest about the risk than a lognormal one that forbids it.

Traders manage this by ensuring volatility is small relative to the level of the forward. If your forward rate is 2% with volatility of 20 bps, the probability of a negative rate is negligible. But if the forward is 10 bps with volatility of 50 bps, that probability is meaningful, and Bachelier correctly prices it into the option value.

## Comparing Bachelier and Black-Scholes: when to use each

For equities and stock indices: **Black-Scholes.** Stocks do not go negative, and the lognormal distribution is a natural model for returns that compound over time.

For interest rates at normal levels (>1%): **Black-Scholes-based models** (like [Black-76-model](/black-76-model/)) remain acceptable, though Bachelier is increasingly standard.

For interest rates near zero or negative: **Bachelier.** It is the only natural model.

For commodity futures with large swings: **Bachelier can be appropriate.** Oil, natural gas, and agricultural futures can move wildly in absolute terms. The normal model sometimes fits the empirical distribution better than lognormal.

For options on spreads (e.g., credit spreads, [yield-curve](/yield-curve/) slopes): **Bachelier.** Spreads can go negative; the normal model is more natural.

## Volatility smile in Bachelier markets

Like all pricing models, Bachelier has limitations. Real interest-rate markets exhibit a [volatility smile](/volatility-smile/): at-the-money options trade at lower implied volatility than far out-of-the-money options. A pure Bachelier model with constant volatility cannot capture this.

In practice, traders use **local-volatility Bachelier** or **stochastic-volatility Bachelier** extensions (the most popular being SABR with normal-model calibration). These allow volatility to vary with the level and dynamics of the forward, capturing the smile whilst preserving the nice properties of the normal distribution.

## Historical note: a century ahead of its time

Bachelier published his option pricing formula in 1900, more than 70 years before Black-Scholes. His model was mathematically rigorous and economically sound. Yet it fell into obscurity for much of the 20th century because:

1. Interest rates were almost always positive (and usually positive by a significant margin), so the lognormal assumption's prohibition on negative prices mattered little.

2. Black-Scholes (1973) arrived during the equity options boom and became the standard for stock options, whose positive-price assumption made geometric Brownian motion natural.

3. Bachelier's paper was in French and addressed a problem (Treasury bond options) that was not yet liquid.

The 2008 financial crisis and subsequent zero-/negative-rate regimes vindicated Bachelier's approach. Today, every major derivatives desk maintains Bachelier pricing libraries, and regulators mandate Bachelier-based calculations for certain interest-rate exposures.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes-model](/black-scholes-model/) — The lognormal option pricing framework; standard for equities
- [Black-76-model](/black-76-model/) — Black-Scholes adapted to futures; often replaced by Bachelier in negative-rate regimes
- [Interest-rate](/interest-rate/) — The variable that Bachelier models handle best, especially near zero or negative levels
- [Implied volatility](/implied-volatility/) — The volatility input to Bachelier; for interest rates, quoted in basis points
- [Option](/option/) — The derivative that Bachelier prices
- [Call-option](/call-option/) and [put-option](/put-option/) — The option types priced by Bachelier's formula
- [Volatility-smile](/volatility-smile/) — The empirical pattern that pure Bachelier (with constant volatility) cannot capture

### Wider context

- [Futures-contract](/futures-contract/) — Often priced in Bachelier when markets are in negative-rate regimes
- [Strike-price](/strike-price/) — The fixed price in a Bachelier option
- [Yield-curve](/yield-curve/) — The schedule of forward rates priced using Bachelier
- [Central-bank](/central-bank/) policy — Negative rate policies drove Bachelier adoption in real markets
- [Volatility](/volatility-smile/) — The empirical distribution of price changes that Bachelier models assume to be normal

</div>

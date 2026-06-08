---
title: "Interpolated Yield"
description: "A synthetic benchmark yield for odd maturities, constructed by interpolating between two on-the-run Treasury yields."
keywords:
  - interpolated yield
  - treasury yield curve
  - bond benchmarking
  - yield interpolation
  - on-the-run treasuries
image: /svg/fixed-income.svg
---

*An **interpolated yield** is a benchmark rate derived by estimating the yield at a maturity that falls between two actively traded (on-the-run) Treasury instruments. Fixed-income traders and analysts use interpolation to establish reference rates for valuations, risk management, and cash flow analysis when direct market quotations are unavailable.*

<div class="wiki-hatnote">

For the technical method of deriving zero-coupon rates from coupon bonds, see [Bootstrapping the Yield Curve](/bootstrapping-yield-curve/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interpolated Yield — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">A synthetic rate filling gaps between liquid Treasury quotations.</div>

|   |   |
|---|---|
| **What it is** | A yield estimated for a maturity between two observed on-the-run rates |
| **Primary use** | Benchmarking and discounting cash flows at odd maturities |
| **Data needed** | Two adjacent Treasury yields and maturities; assumes smooth curve shape |
| **Method** | Typically linear interpolation; sometimes log-linear for longer curves |
| **Liquidity context** | Bridges gap where off-the-run bonds trade infrequently or not at all |

</aside>

## Why Treasury benchmarks have gaps

The U.S. Treasury does not issue bonds at every possible maturity. At any moment, the on-the-run (most recently auctioned and most liquid) issues are typically 2, 3, 5, 7, 10, and 30-year bonds. A corporate bond maturing in 4 years, a mortgage payment arriving in 6.5 years, or a pension liability due in 13 years falls between these standard maturities.

Rather than wait for an exact-maturity Treasury to trade, market participants estimate a fair benchmark for the odd maturity by interpolating between the two neighbouring on-the-run yields. This keeps pricing and risk models current without inventing a rate out of thin air.

## The mechanics of linear interpolation

The simplest and most common approach is **linear (straight-line) interpolation**. Suppose a 5-year Treasury yields 3.2% and a 7-year Treasury yields 3.5%. To find the benchmark for a 6-year maturity:

The time difference is 2 years (from 5 to 7). The yield difference is 0.3% (from 3.2% to 3.5%). The target date is 1 year past the 5-year point.

```
Interpolated 6-year yield = 3.2% + (1 / 2) × (3.5% − 3.2%)
                          = 3.2% + 0.5 × 0.3%
                          = 3.2% + 0.15%
                          = 3.35%
```

Linear interpolation assumes the yield curve changes at a constant rate between the two points. It is transparent, fast, and matches market convention across many fixed-income pricing systems.

## When (and why) log-linear interpolation matters

For longer-dated instruments, the yield curve's shape can be slightly convex or concave in ways that linear interpolation misses. **Log-linear interpolation** assumes the discount factor changes linearly rather than the yield itself—a subtle adjustment that can matter for 20+ year maturities.

The difference rarely exceeds a basis point for curves that are reasonably smooth. Most traders and systems stick with linear interpolation for simplicity, especially for maturities under 10 years. Central banks and academic work often favour log-linear for greater precision.

## Pitfalls and limitations

Interpolation only works reliably when the yield curve is relatively smooth and stable. In sharp market dislocations—flights to safety, sharp repricing of long-dated inflation expectations, or structural changes in Treasury supply—the curve can twist in ways that make bracketing assumptions invalid. An interpolated 6-year yield might temporarily mismatch the actual 6-year [spot rate](/spot-rate/) implied by market prices.

Moreover, interpolation is a one-time snapshot. As time passes and new Treasuries are auctioned, the set of on-the-run issues shifts, and interpolated benchmarks must be recalculated. A careful analyst revisits interpolations at least daily to capture curve moves.

## Interpolation versus bootstrapping

Interpolation and [bootstrapping](/bootstrapping-yield-curve/) are related but distinct. Interpolation simply connects two yield observations; it does not derive zero-coupon [spot rates](/spot-rate/). Bootstrapping, by contrast, uses a no-arbitrage framework to strip coupon bonds into their component cash flows and solve for the true discount curve. 

For practical risk management, traders often use interpolated yields directly as a quick benchmark. For precise valuation—especially of exotic or long-dated instruments—bootstrapping is preferred because it accounts for the full structure of bond coupons and removes ambiguity from the curve shape.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot Rate](/spot-rate/) — the zero-coupon yield at a specific maturity, used for precise discounting
- [Bootstrapping the Yield Curve](/bootstrapping-yield-curve/) — deriving zero-coupon rates from coupon bond prices
- [Forward Rate](/forward-rate/) — the implied future short rate between two spot rates
- [Yield Curve](/yield-curve/) — the full map of yields across maturities
- [Coupon Payment](/coupon-payment/) — the periodic cash payment on a coupon bond
- [Treasury Bond](/treasury-bond/) — direct U.S. government obligations underlying the benchmark curve

### Wider context

- [Bond](/bond/) — the fundamental debt instrument
- [Interest Rate](/interest-rate/) — the core economic variable driving yields
- [Discount Rate](/discount-rate/) — the rate used to value future cash flows
- [Duration](/duration/) — a bond's sensitivity to yield moves
- [Market Capitalization](/market-capitalization/) — why Treasury market size matters for liquidity

</div>

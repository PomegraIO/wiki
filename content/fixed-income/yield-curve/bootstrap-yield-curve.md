---
title: "Bootstrapping the Yield Curve"
description: "The sequential method for extracting zero-coupon spot rates from observable coupon bond prices."
keywords:
  - yield curve construction
  - spot rates
  - zero-coupon rates
  - bond pricing
  - fixed income valuation
  - coupon stripping
image: "/svg/fixed-income.svg"
---

*Bootstrapping is the sequential extraction of zero-coupon spot rates from the prices of coupon-bearing bonds. It works backward from the shortest-maturity instruments, using observed bond prices to solve for the discount rates that price longer-maturity bonds, and is the foundation of modern curve construction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bootstrapping — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">The mechanical heart of yield curve assembly: pricing bonds to uncover the true discount rates embedded in them.</div>

|   |   |
|---|---|
| **What it is** | Sequential solution for [spot rates](/yield-curve/) from market bond prices |
| **Also called** | Spot curve construction, discount curve fitting |
| **Output** | Zero-coupon [discount factors](/discount-rate/) for each maturity |
| **Why it matters** | Provides the true cost of money at each point in time |
| **Required inputs** | Observed prices of bonds across maturities |
| **Assumption** | Market prices are arbitrage-free |
| **Limitation** | Works only for maturities where liquid bonds exist |

</aside>

## Why spot rates matter more than [coupon rates](/coupon-rate/)

A [bond](/bond/) trading at par carries a [coupon rate](/coupon-rate/) that equals its [yield to maturity](/yield-to-maturity/). But the coupon rate is an average; it masks the true discount rate for cash flows at each future moment. A 5-year bond paying coupons annually doesn't give you a single 5-year rate—it gives you five overlapping maturities (1 year, 2 years, 3 years, 4 years, 5 years), each with its own discount rate.

Bootstrapping untangles this. Instead of using the coupon yield as a blanket rate, you extract the *spot rate*—the yield of a zero-coupon bond—for each maturity. Spot rates are the true building blocks of bond pricing. Any coupon bond is simply a portfolio of zero-coupon bonds, so if you know all the spot rates, you can price any bond.

## The algorithm: shortest maturity first

Bootstrap begins at the short end. The shortest instrument is often a [Treasury bill](/treasury-bill/) or overnight [SOFR](/sofr/), which is already effectively zero-coupon. Its price directly implies the 1-year spot rate.

Next, take the first coupon-bearing bond—say a 2-year Treasury paying a 3% coupon. You already know the 1-year spot rate from step one. The bond price must equal the present value of its cash flows, discounted at the appropriate spot rates:

Bond Price = (Coupon / (1 + r₁)) + (Coupon + Principal) / (1 + r₂)²

Since you know r₁ (the 1-year spot) and the bond price (observable in the market), you can solve algebraically for r₂, the 2-year spot rate.

Repeat this for the 3-year bond using known 1-year and 2-year rates, and solve for the 3-year rate. Continue up the curve. Each new spot rate is solved using the ones already extracted. The method is mechanical, deterministic, and requires no assumptions about rate behaviour.

## Real-world complications

Pure bootstrapping assumes a liquid bond at every maturity. Markets are not so obliging. The U.S. Treasury issues actively only at 3-month, 6-month, 2-year, 3-year, 5-year, 7-year, 10-year, 20-year, and 30-year points. There are gaps.

For missing maturities, practitioners interpolate. The most common approach is cubic spline interpolation on the discount factors, which preserves smoothness and avoids spurious humps or dips. Other methods include linear interpolation in the logarithm of discount factors, or fitting a functional form (Nelson-Siegel, Svensson) to the entire curve and extracting spot rates analytically.

A second complication: what counts as a "bond price"? In government markets, the bid-ask spread can be tight for on-the-run securities but wide for off-the-run bonds. Active traders use on-the-run bonds; academics and central banks often hand-pick the most liquid instruments. The choice affects the curve slightly.

Third, corporate bonds carry credit risk, so their prices reflect both the risk-free curve and a [credit spread](/credit-spread/). To bootstrap a corporate curve, you must subtract the spread first—but the spread itself is not observable until you have the curve. This circularity is addressed by fitting a spread function jointly with the curve.

## Where bootstrapping appears in practice

[Central banks](/central-bank/) publish daily zero-coupon curves built via bootstrap. The Federal Reserve publishes a Treasury curve; the ECB publishes euro curves for multiple credit ratings. Market participants use these curves to [price derivatives](/discounted-cash-flow-valuation/), manage [duration](/duration/) risk, and forecast [monetary policy](/monetary-policy/) shifts.

In derivatives markets, the bootstrap curve is the starting point for [discounting](/discount-rate/) cash flows. A [swap](/interest-rate/) dealer will bootstrap a curve from swap rates (or from SOFR futures and short-term [LIBOR](/libor/) instruments, depending on the currency and date) to value positions.

The bootstrap method is also the foundation for constructing [OIS curves](/ois-curve/) and other specialized curves. Each instrument type (Treasury, swap, repo) has its own curve because each carries different financing costs and counterparty risk.

## Spot rates versus forwards: the relationship

Once you have spot rates, you can extract *forward rates*—the implied cost of borrowing between two future dates. A 1-year spot rate of 3% and a 2-year spot rate of 4% imply a specific rate for borrowing from year 1 to year 2, even if that market doesn't exist. This consistency is the force behind bootstrap: it prevents arbitrage.

Practitioners often work with forward rates for intuition (they capture rate expectations) but build curves using spot rates for consistency. Bootstrapping ensures both are mathematically aligned.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield curve](/yield-curve/) — the full term structure of interest rates, what bootstrapping constructs
- [Spot rate](/discount-rate/) — the zero-coupon rate, the output of bootstrapping
- [Bond pricing](/bond/) — the mathematical foundation underlying the bootstrap algorithm
- [Duration](/duration/) — how bootstrap curves are used to manage interest rate risk
- [OIS curve](/ois-curve/) — a specialized bootstrap curve for overnight rates
- [Discounted cash flow](/discounted-cash-flow-valuation/) — practical use of the bootstrap curve in valuation

### Wider context

- [Yield to maturity](/yield-to-maturity/) — the coupon yield, which bootstrapping disaggregates
- [Forward guidance](/forward-guidance/) — how central banks signal future rate paths that curves embed
- [Federal Reserve](/federal-reserve/) — issuer of the most actively bootstrapped curve (U.S. Treasuries)
- [Interest rate](/interest-rate/) — the quantity being extracted at each maturity
- [Monetary policy](/monetary-policy/) — the force shifting the entire curve over time

</div>

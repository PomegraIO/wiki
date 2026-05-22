---
title: "Par Yield Curve"
description: "Curve showing the coupon rates of bonds trading at par value by maturity, directly revealing market yield expectations without adjustment."
keywords:
  - par yield
  - bond coupon rates
  - yield-to-maturity
  - bond pricing
  - par bond construction
---

*A **par yield curve** plots the coupon rate that a bond must offer to trade at par value (face price) across different maturities. Unlike other yield curve constructions, it does not require interpolation or smoothing; it shows the market's direct pricing of credit-risk-free borrowing by maturity.*

<div class="wiki-hatnote">For other yield curve shapes, see [Yield Curve](/wiki/yield-curve/) and [Zero Coupon Bond](/wiki/zero-coupon-bond/).</div>

<aside class="wiki-infobox">

| Property | Meaning |
|----------|---------|
| Definition | Coupon rate at which bond trades at 100% of face |
| Y-axis value | Annualized coupon percentage |
| X-axis | Maturity (1Y, 2Y, 5Y, 10Y, 30Y) |
| Relationship to spot | Par yield = annualized spot rate; related but distinct |
| Interpretation | Market's required return to par |
| Smoothing | Minimal; each point is observable |
| Frequency | Typically updated daily for government bonds |

</aside>

## What par yield means

A bond that offers a 3% coupon and trades at exactly $100 (par) is yielding 3% to maturity—the coupon rate equals the [yield-to-maturity](/wiki/yield-to-maturity/). If the market demands a 4% yield for that maturity and credit quality, a 3% coupon bond will trade below par (around $97 or $98, depending on the exact calculation).

A **par bond** is one whose coupon *exactly matches* the market's required yield. The par yield curve shows what coupon rates the market demands for bonds to be at par across the maturity spectrum. At maturity 2Y, the par yield might be 2.1%; at 10Y, it might be 3.2%. These represent the break-even coupon rates.

## Constructing a par yield curve

Unlike a [zero coupon bond](/wiki/zero-coupon-bond/) curve, which requires stripping complex securities or inferring rates from market prices, a par yield curve can be constructed directly from observed bond prices in the market—particularly government bonds, which trade actively and frequently.

**Simple method**:
1. For each maturity (1Y, 2Y, 5Y, 10Y, etc.), find the most actively traded government bond (the "on-the-run" issue).
2. Calculate its [yield-to-maturity](/wiki/yield-to-maturity/). If it trades near par, this yield *is* the par yield. If it trades away from par (premium or discount), interpolate or adjust to find the coupon that would make it par at the observed yield.
3. Plot these points to form the curve.

**More rigorous method**:
Use a bootstrapping algorithm. Start with the 1Y yield. Use it to infer the 2Y spot rate, then calculate what 2Y coupon yields 2.0% yield-to-maturity at par. Repeat for each maturity, building the par curve from short end to long end.

## Par yield vs. spot yield vs. forward yield

The **spot yield curve** (or zero-coupon curve) shows yields for single lump-sum payments at each maturity. A par yield of 3% at 5Y means a bond paying 3% annually trades at par; the 5Y spot yield might be 2.95% because spot rates don't embed interim coupons.

The **forward yield** is the rate implied for borrowing in a future period (e.g., the 4Y-5Y forward rate—the rate for year 5 as seen from year 4). Par and spot curves can be reconciled mathematically; forward rates bridge them.

For most traders and analysts, the par yield curve is the most intuitive: it directly answers the question "What coupon does a safe bond need to offer at 10 years?" without requiring calculation.

## Practical use in bond trading

Bond traders use the par yield curve as a benchmark for pricing and relative value:

- **New issuance pricing**: When a government or corporation issues a new bond, the par curve sets the floor coupon. If the 5Y par yield is 2.8%, a new 5Y bond with a 2.5% coupon will be repriced or rejected.
- **Identifying richness/cheapness**: If an existing 5Y bond offers a 3.0% coupon and the par yield is 2.8%, the bond is "cheap"—it offers above-market coupon and is likely trading below par (or at a premium if older and bought at lower rates). A trader might buy it for income.
- **Cross-currency arbitrage**: Par curves for US Treasuries, Gilts (UK), Bunds (Germany), and OATs (France) can be compared; large yield differences might signal arbitrage opportunities or currency risk.

## The transition from par curve to zero coupon curve

Modern derivatives pricing relies on **zero coupon (spot) rates**, not par coupons. A par curve is a market-observable input; it must be converted to a zero coupon curve for option pricing, [duration](/wiki/duration/) calculation, and [CVA](/wiki/cvar-tail-risk/) models.

The conversion is mathematical: the present value of a par bond must equal $100, so:

$$\text{Par Coupon} \times \sum_{t=1}^{T} \text{DF}(t) + 100 \times \text{DF}(T) = 100$$

Where DF(t) is the discount factor for year t. Solving for the DF terms across all maturities yields the zero coupon curve.

## Par curve characteristics under different regimes

In **normal yield curve**: Par yield rises with maturity (upward-sloping curve). This reflects a risk premium for long-duration borrowing.

In **inverted yield curve**: Par yield falls with maturity (5Y par yield > 10Y par yield). Markets expect lower rates in the future.

In **flat yield curve**: Par yields are similar across maturities (e.g., 2Y and 10Y both at 2.5%). Often a transitional state before a shift.

In **low-interest-rate environment** (e.g., post-2008 or 2020): Par yields near zero or negative for shorter maturities. This is why central banks set policy rates *at* zero—par yields cannot be negative unless the issuer has credit risk or the bond trades at a premium.

## Par yield curves beyond government bonds

While the par yield concept is most visible in sovereign debt (Treasuries, Gilts, Bunds), it also applies to [corporate bonds](/wiki/corporate-bond/). A high-grade corporation's par yield curve will sit above the government curve, reflecting the credit spread. A junk-rated firm's curve sits much higher, reflecting default risk.

The gap between the government par curve and a corporate par curve is the **credit spread**. Traders watching spread widening or tightening are effectively watching the corporate par curve move relative to the risk-free curve.

<div class="wiki-seealso">

### Closely related
- [Yield Curve](/wiki/yield-curve/) — concept overview
- [Yield-to-Maturity](/wiki/yield-to-maturity/) — par yield calculation method
- [Zero Coupon Bond](/wiki/zero-coupon-bond/) — derived concept
- [Duration](/wiki/duration/) — related sensitivity measure
- [Credit Spread](/wiki/credit-spread/) — corporate par yield gap

### Wider context
- [Bond Basics](/wiki/bond-basics/) — bond fundamentals
- [Bond Price Formula](/wiki/bond-price-formula/) — pricing mechanics
- [Discount Rate](/wiki/discount-rate/) — cost of money
- [Spot Yield Curve Dynamics](/wiki/spot-yield-curve-dynamics/) — market-wide movements

</div>

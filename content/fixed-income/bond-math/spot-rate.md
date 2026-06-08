---
title: "Spot Rate"
description: "The yield on a zero-coupon instrument for a specific maturity, used to discount individual cash flows."
keywords:
  - spot rate
  - zero-coupon yield
  - discount rate
  - yield curve
  - cash flow discounting
image: /svg/fixed-income.svg
---

*A **spot rate** is the yield an investor earns today on a zero-coupon bond held to maturity—that is, an instrument with no interim payments that pays a single lump sum at a fixed future date. Spot rates form the foundation of the [yield curve](/yield-curve/) and are essential for valuing any fixed-income cash flow because they represent the true, no-coupon cost of borrowing money for a specific time period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spot Rate — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">The pure, zero-coupon rate for a given maturity; the building block of bond valuation.</div>

|   |   |
|---|---|
| **What it is** | The yield on a theoretical zero-coupon bond for a specified maturity |
| **Also called** | Zero-coupon yield, spot yield, zero rate |
| **Primary use** | Discounting individual cash flows; constructing the yield curve |
| **Key relationship** | Spot rates for all maturities define the complete discount function |
| **Derivation** | Extracted from coupon bond prices via [bootstrapping](/bootstrapping-yield-curve/) |
| **Time-varying** | Spot rates change daily as bond prices and expectations shift |

</aside>

## Why spot rates matter in bond math

A standard [bond](/bond/) pays coupons semi-annually or annually, then returns principal at maturity. Its price is the sum of discounted cash flows. But what discount rate should apply to the year-two coupon, versus the year-five coupon? The answer is not a single, uniform rate—different maturities carry different risk and liquidity premia, so each cash flow should be discounted at the rate appropriate to its maturity.

**Spot rates solve this problem.** A 2-year spot rate of 2.5% tells you exactly what yield you can lock in today on a 2-year zero-coupon instrument. A 5-year spot rate of 3.1% tells you what a 5-year zero would offer. By using the correct spot rate for each cash flow, you price a bond accurately.

## Zero-coupon bonds and implicit spot rates

Directly observable zero-coupon bonds (such as [Treasury STRIPS](/treasury-bill/), or certain corporate zero bonds) trade at explicit prices, and their [yield-to-maturity](/yield-to-maturity/) *is* the spot rate. A STRIP maturing in 3 years, purchased at 85 cents per dollar of face value, has a spot rate you can calculate directly—it is the discount rate that makes 100 = 85 × (1 + r)^3.

Most zero-coupon instruments are not actively traded. Instead, analysts derive spot rates from coupon bond prices using [bootstrapping](/bootstrapping-yield-curve/)—a mathematical process that backs out the implied zero-coupon yield at each maturity from the prices of coupon-bearing bonds.

## The spot curve and the yield curve

A collection of spot rates, one for each maturity from 1 year to 30 years, forms the **spot curve** (or sometimes **zero-coupon curve**). This is the theoretical foundation of the [yield curve](/yield-curve/) that traders and risk managers reference daily.

The spot curve is not directly quoted in financial media or terminals the way [bond](/bond/) prices are. Instead, it is calculated and refined by traders and risk systems as an intermediate step in pricing and hedging. A bond trader's computer automatically bootstraps the spot curve from observed Treasury prices each morning, then uses those spots to value corporate bonds, mortgages, derivatives, and other securities.

## The mathematics of discounting with spot rates

If you hold a cash flow of $100 due in 3 years, and the 3-year spot rate is 2.8%, the present value is:

```
PV = 100 / (1 + 0.028)^3 = 100 / 1.0857 ≈ $92.11
```

For a coupon bond with a $50 coupon due in 2 years, another $50 coupon in 4 years, and $1,050 principal in 6 years, you discount each cash flow separately:

```
Price = 50 / (1 + r₂)² + 50 / (1 + r₄)⁴ + 1,050 / (1 + r₆)⁶
```

where r₂, r₄, and r₆ are the appropriate spot rates. This approach—discounting each cash flow at its own maturity's rate—is called **spot curve discounting** and is the standard in professional fixed-income analysis.

## Spot rates versus par yields

A bond's [yield-to-maturity](/yield-to-maturity/) (or **par yield**) is a single internal rate of return that summarizes all its cash flows. This is useful for quick comparison but masks the underlying term structure of rates. Two bonds with the same [yield-to-maturity](/yield-to-maturity/) can have very different prices and risks if the spot curve is non-flat.

Spot rates, by contrast, directly reflect what the market is willing to pay for zero-coupon cash at each maturity. When the [yield curve](/yield-curve/) is upward-sloping, spot rates rise with maturity; spot rates fall when the curve inverts. This makes spots more economically meaningful than an aggregate [yield-to-maturity](/yield-to-maturity/) number.

## Practical use in portfolio management

Portfolio managers and risk committees use spot curves to:

- **Value individual bonds** by summing discounted cash flows, capturing the true [duration](/duration/) and interest-rate sensitivity.
- **Measure immunization**: matching the present value (and [duration](/duration/)) of liabilities to assets, using precise spot discounting.
- **Assess relative value**: comparing a new bond issue against the benchmark spot curve to judge whether it is cheap or expensive.
- **Monitor [interest-rate risk](/interest-rate-risk/)**: by repricing portfolios daily using the updated spot curve.

Changes in spot rates at different maturities drive portfolio returns. A steepening curve—where longer spots rise more than shorter ones—benefits bonds held long and may hurt intermediate positions.

## See also

<div class="wiki-seealso">

### Closely related

- [Bootstrapping the Yield Curve](/bootstrapping-yield-curve/) — extracting spot rates from coupon bond prices
- [Forward Rate](/forward-rate/) — the implied future rate between two spot rates
- [Interpolated Yield](/interpolated-yield/) — estimating a rate at an odd maturity
- [Yield Curve](/yield-curve/) — the complete map of yields across maturities
- [Yield-to-Maturity](/yield-to-maturity/) — a bond's single internal rate of return
- [Discount Rate](/discount-rate/) — the general principle of reducing future value to present
- [Duration](/duration/) — a bond's interest-rate sensitivity

### Wider context

- [Bond](/bond/) — the fundamental instrument whose cash flows are discounted
- [Treasury Bond](/treasury-bond/) — the benchmark for spot curve construction
- [Interest Rate](/interest-rate/) — the economic variable underlying all spot rates
- [Time Value](/time-value/) — why future money is worth less today
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — applying spot rates to broader valuation problems

</div>

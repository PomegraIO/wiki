---
title: "Yield to Call: How to Calculate It for Corporate Bonds"
description: "Yield to call is the annualized return if a bond is redeemed at its first call date; calculation is identical to yield to maturity but uses call price and call date."
keywords:
  - yield to call calculation
  - how to calculate yield to call
  - corporate bond yield to call
  - callable bonds
  - bond valuation
image: "/svg/fixed-income.svg"
---

*A **yield to call** (YTC) calculation tells you the total annualized return you will earn if a [callable bond](/callable-bond/) is redeemed on its first call date at the call price—a crucial metric because called bonds often deliver lower returns than their stated [coupon rate](/coupon-rate/) suggests.*

When you buy a [corporate bond](/corporate-bond/) that the issuer can redeem early, you face an asymmetry: if rates fall and the bond's price rises, the issuer will likely call (redeem) the bond to avoid paying high coupons. You capture the price gain only up to the call price, not the full upside. Yield to call measures the reality of that scenario: your return *if* the bond is called on its first possible date.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield to Call — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">The annualized return if a bond is redeemed at the call price on the first call date.</div>

|   |   |
|---|---|
| **Formula** | Same as [yield to maturity](/yield-to-maturity/), but substitute call price for par and call date for maturity date |
| **Key inputs** | Current price, coupon rate, call price, years to first call date, coupon frequency |
| **Calculation method** | Iterative/trial-and-error or financial calculator; no closed-form formula |
| **When to use YTC** | When a bond is trading above the call price and likely to be called |
| **Comparison** | YTC is typically *lower* than YTM for bonds trading above par |
| **Outcome range** | Can be lower than coupon rate (if bond premium is large relative to call date) |

</aside>

## The callable bond dilemma

A [callable bond](/callable-bond/) is debt that the issuer can redeem before maturity, typically after a call-protection period. Most corporate bonds are callable. The issuer buys the option to refinance at lower rates; the bondholder bears the cost.

Suppose you buy a 30-year corporate bond with a 5% coupon for $1,050 (a $50 premium over par). You dream of 5% annual income. But the bond is callable in 5 years at $1,000. If rates fall, the issuer will almost certainly call the bond at year 5, forcing you to collect par ($1,000) plus the remaining coupons—not the full premium-adjusted return.

[Yield to maturity](/yield-to-maturity/) (YTM) assumes the issuer holds the bond to the stated maturity date. It ignores the call risk. Yield to call assumes the issuer *will* call the bond on the first call date and calculates your actual return under that scenario.

## The yield-to-call formula

The yield to call uses the identical mathematical form as yield to maturity:

```
Price = [C / (1 + y)¹] + [C / (1 + y)²] + ... + [C / (1 + y)ⁿ] + [Call Price / (1 + y)ⁿ]
```

Where:
- **Price** = the current market price you paid for the bond
- **C** = the semi-annual (or annual) coupon payment
- **y** = the yield to call you are solving for (expressed as a decimal per period)
- **n** = the number of periods until the first call date
- **Call Price** = the redemption price (usually $1,000 or slightly above)

The key difference from YTM: you use the *call price* (not par) and the *call date* (not maturity date) as your endpoint.

## Step-by-step example

Suppose:
- You buy a bond for **$1,050**
- Coupon rate is **5%** (so semi-annual coupon = $25 per $1,000 face value)
- Call price is **$1,000**
- Years to first call date: **5 years** (10 semi-annual periods)
- Coupons pay semi-annually

You want to find YTC. Set up the equation:

```
1,050 = 25/(1 + y)¹ + 25/(1 + y)² + ... + 25/(1 + y)¹⁰ + 1,000/(1 + y)¹⁰
```

There is no algebraic solution. You solve iteratively by guessing and refining.

**First guess:** Try y = 2% per half-year (4% annualized):
- PV of coupons = $25 × 8.983 (annuity factor at 2%) = $224.58
- PV of call price = $1,000 / (1.02)¹⁰ = $820.75
- Total ≈ $1,045.33 (too low; we need a lower y to get a higher present value)

**Second guess:** Try y = 1.9% per half-year (3.8% annualized):
- PV of coupons ≈ $228.51
- PV of call price ≈ $825.08
- Total ≈ $1,053.59 (too high; we need a slightly higher y)

**Third guess:** Try y = 1.93% per half-year (3.86% annualized):
- PV of coupons ≈ $226.82
- PV of call price ≈ $822.80
- Total ≈ $1,049.62 (very close)

The yield to call is approximately **3.86% annualized**, or **1.93% per half-year**.

In practice, use a financial calculator or spreadsheet. Input the values, solve for rate, and read the result. Most calculators have a "YTC" or "yield" function that automates the iteration.

## Yield to call vs. yield to maturity

For the same bond, calculate both YTM and YTC:

| Metric | Value |
|--------|-------|
| Current price | $1,050 |
| Coupon | 5% |
| Par / Call price | $1,000 |
| Years to call | 5 |
| Years to maturity | 30 |
| **YTC** | 3.86% |
| **YTM** | 4.73% |

The YTC is lower. This is typical for bonds trading *above* par (at a premium). The bondholder loses the benefit of holding the premium all the way to maturity; the issuer redeems at par.

If instead the bond trades *below* par (at a discount), YTC and YTM can be ranked either way depending on which is closer to par. The general rule: if the bond is trading above the call price, YTC < YTM.

## When to use yield to call

Use YTC when:
- The bond is trading **above the call price**. A bond at par or a discount will likely not be called, so YTM is the relevant metric.
- You believe the **bond is likely to be called** based on rate outlook or issuer incentives. If the issuer can refinance at materially lower rates, they will call.
- You are comparing **two callable bonds** with different call features. YTC allows apples-to-apples comparison of actual expected returns.

Many professional bond investors use YTC as their primary metric for callable bonds because it reflects the true economically likely outcome, not an optimistic assumption about holding to maturity.

## The call-adjusted comparison

Imagine two similar corporate bonds:

**Bond A:** 5% coupon, callable in 5 years at $1,000, trading at $1,050, YTC = 3.86%

**Bond B:** 4.8% coupon, non-callable, trading at $1,010, YTM = 4.70%

Bond A's coupon is higher, but Bond B's YTM is higher *and* Bond B has no call risk. An investor expecting rates to stay flat would likely prefer Bond B, despite the lower coupon, because the YTC of Bond A is significantly below par.

## Risks and limitations

YTC assumes the bond *will* be called on the first call date. If rates rise instead, the issuer will not call, and you will hold to maturity or sell at a loss. YTC does not capture this scenario; it assumes a fixed outcome.

YTC also ignores credit risk (the bond may default) and reinvestment risk (you must reinvest coupons at uncertain future rates). Like YTM, it is useful only as a comparison tool, not a guarantee of return.

A bond with YTC of 3.86% is not a 3.86% guaranteed return; it is a 3.86% return *if* coupons are reinvested at 3.86%, rates don't move, and the issuer calls on schedule.

## Practical calculation tools

Most financial calculators and spreadsheets have yield-to-call functions:
- **Excel:** Use Goal Seek or the IRR function, adjusting the formula for call price and date.
- **HP 12C or TI-BA II Plus:** Enter cash flows, call price, and call date; press "solve for rate."
- **Bloomberg terminal:** Yield to call is a standard field (YTC) in bond pricing screens.
- **Online tools:** Many bond pricing websites auto-calculate YTC alongside YTM.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable bond](/callable-bond/) — overview of call mechanics and investor implications
- [Yield to maturity](/yield-to-maturity/) — calculation and meaning for non-callable bonds
- [Corporate bond](/corporate-bond/) — characteristics and typical features
- [Coupon rate](/coupon-rate/) — definition and role in bond returns
- [Call risk](/call-risk/) — the risk of early redemption and lost upside

### Wider context

- Bond valuation — general framework for pricing debt instruments
- [Duration](/duration/) — how bond prices respond to rate changes
- Bond pricing — mechanics of market prices for fixed-income securities
- [Reinvestment risk](/reinvestment-risk/) — the assumption underlying yield calculations
- [Credit spread](/credit-spread/) — extra yield demanded for credit risk

</div>

---
title: "Yield to Maturity: Semiannual vs Annual Compounding"
description: "Understand why yield to maturity differs with semiannual vs annual discounting, and how to convert between the two compounding conventions."
keywords:
  - yield to maturity
  - semiannual compounding
  - annual compounding
  - bond valuation
  - discount rate
  - coupon payment
---

*The **yield to maturity** (YTM) of a bond depends on whether you discount its cash flows semiannually or annually. Most U.S. corporate and Treasury bonds pay coupons twice yearly and are quoted with semiannual YTM; switching to annual compounding produces a different number. Understanding the difference matters for accurate valuation and comparing bonds across markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">YTM Compounding — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The same bond yields a different number depending on the compounding frequency baked into the calculation.</div>

|   |   |
|---|---|
| **Semiannual YTM (BEY)** | Standard for U.S. bonds; coupons discounted twice per year |
| **Annual YTM** | Coupons discounted once per year; yields a lower number for the same cash flows |
| **Relationship** | Annual YTM < Semiannual YTM (for positive yields) |
| **Conversion factor** | Annual = (1 + BEY/2)² − 1 |
| **Market convention** | U.S. corporates, Treasuries, agencies use semiannual |
| **Practical impact** | Mismatched compounding can misprice bonds by 10–50 basis points |

</aside>

## The compounding frequency problem

A typical U.S. [corporate bond](/corporate-bond/) pays [coupon payments](/coupon-payment/) twice a year: $25 on June 15 and $25 on December 15 (for a bond with a 5% annual coupon on $1,000 par). When you calculate the [yield to maturity](/yield-to-maturity/) of that bond, you must specify: are you discounting those semiannual payments at a semiannual rate, or are you treating them as if they were discounted at an annual rate?

The answer changes the YTM number significantly. A bond might have a semiannual YTM of 5.00% (the industry standard quote), but an equivalent annual YTM of 4.88%. The bond's cash flows haven't changed — only the mathematical convention for discounting them.

## Why semiannual is the U.S. default

U.S. corporate bonds, [Treasury bonds](/treasury-bond/), and most agency securities pay coupons semiannually. To match reality, the market quotes YTM on a "bond equivalent yield" (BEY) basis: the yield is stated as a semiannual rate, then doubled to an annual figure. So a semiannual YTM of 2.5% is quoted as 5.0% BEY.

This convention is simply history and habit. The semiannual convention makes the math align with the actual cash flow dates — coupons arrive every six months, so the discount periods are six months.

By contrast, government bonds in some other markets (e.g., the U.K. Gilts, Euro bonds) may use annual or even quarterly compounding, depending on their coupon schedule and regulatory convention.

## The mathematical relationship

If a bond's **semiannual YTM** (BEY) is *y*_s_, then the equivalent **annual YTM** is:

*y*_a = (1 + *y*_s / 2)² − 1

For example, if semiannual YTM is 5.00%:

*y*_a = (1 + 0.05 / 2)² − 1 = (1.025)² − 1 = 1.050625 − 1 = 5.0625%

Wait — that's *higher* than 5.00%. Why?

The answer is compounding frequency. A semiannual rate of 2.5% applied twice per year compounds to 5.0625% annualized. If you state that 5.0625% as an annual yield, you are implicitly ignoring the compounding effect when you discount at that rate once per year.

To flip it: if a bond has an **annual YTM** of *y*_a, the semiannual rate is:

*y*_s = 2 × [√(1 + *y*_a) − 1]

Using our example, if annual YTM is 5.0625%:

*y*_s = 2 × [√1.050625 − 1] = 2 × [1.025 − 1] = 2 × 0.025 = 5.00% (BEY)

## A worked example

Suppose you are evaluating a $1,000 par bond with a 4% annual coupon (semiannual payments of $20), maturing in 2 years, trading at $980.

**Semiannual calculation:**
You set up the present value equation with six cash flows (one every six months):

PV = $20 / (1 + y/2)¹ + $20 / (1 + y/2)² + $20 / (1 + y/2)³ + $20 / (1 + y/2)⁴ + $20 / (1 + y/2)⁵ + $1,020 / (1 + y/2)⁶ = $980

Solving numerically (trial and error, or a financial calculator), you get y/2 ≈ 2.05%, so **y ≈ 4.10% (BEY)**.

**Annual calculation:**
You could also treat the cash flows as arriving annually by summing the two semiannual coupons into $40 annual payments (this is a simplification; technically you'd discount at midyear):

PV = $40 / (1 + *y*_a)¹ + $40 / (1 + *y*_a)² + $1,040 / (1 + *y*_a)² ≠ $980

In practice, the true annual YTM using the compounding formula is:

*y*_a = (1 + 0.041 / 2)² − 1 ≈ 4.1421%

The annual YTM is about 14 basis points higher than the semiannual quoted yield, due to the extra compounding period.

## When this matters in practice

**Bond pricing and trading:** If you mistakenly use an annual YTM of 5.00% to value a bond that the market quotes at 5.00% semiannual YTM (≈ 5.0625% annual), you will misprice the bond by about 50 basis points or more, depending on duration. You might think the bond is cheaper than it really is.

**Comparing bonds across markets:** A [Treasury bond](/treasury-bond/) quoted at 2.50% BEY is *not* directly comparable to a German Bund quoted at 2.50% annual, because they use different compounding conventions. Always convert to the same basis before comparing.

**Mortgage-backed securities and floating-rate bonds:** Some securities use monthly or quarterly discounting. Ignoring the convention can introduce large valuation errors.

**Reinvestment assumptions:** The semiannual convention also implicitly assumes that coupons received are reinvested at the semiannual rate for the next half-year. Annual compounding assumes reinvestment at the annual rate. These are different assumptions about future returns.

## Converting between the two

To move from **semiannual to annual**, use:

*y*_a = (1 + *y*_s / 2)² − 1

To move from **annual to semiannual**, use:

*y*_s = 2 × [√(1 + *y*_a) − 1]

Both formulas are exact and assume that the cash flows and price are otherwise identical.

## The impact of [duration](/duration/) and [interest rate risk](/interest-rate-risk/)

A bond's price sensitivity (duration) is also affected by the compounding convention. Semiannual discounting produces slightly different modified duration than annual. For most practical purposes, the difference is small (1–2%), but for bond trading, options pricing, and hedging, precision matters. Always ensure your [interest rate](/interest-rate/) sensitivities are calculated with the same compounding convention you use for valuation.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield to Maturity](/yield-to-maturity/) — the foundational concept
- [Coupon Payment](/coupon-payment/) — the cash flows being discounted
- [Coupon Rate](/coupon-rate/) — stated annual rate vs actual yield
- [Duration](/duration/) — how compounding affects price sensitivity
- [Discount Rate](/discount-rate/) — the mathematical mechanism

### Wider context

- [Bond](/bond/) — the instrument being valued
- [Corporate Bond](/corporate-bond/) — typical semiannual coupon schedule
- [Treasury Bond](/treasury-bond/) — standard U.S. market convention
- [Interest Rate Risk](/interest-rate-risk/) — what YTM changes mean
- [Fixed Rate Mortgage (Personal)](/fixed-rate-mortgage-personal/) — alternative compounding rules

</div>

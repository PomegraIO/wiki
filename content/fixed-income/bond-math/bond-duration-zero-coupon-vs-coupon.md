---
title: "Duration of a Zero-Coupon Bond vs a Coupon Bond"
description: "Why a zero-coupon bond's duration always equals its maturity, while coupon-paying bonds have shorter duration."
keywords:
  - zero coupon bond duration
  - bond duration calculation
  - duration vs maturity
  - coupon bond duration
  - modified duration interest rate
  - Macaulay duration
image: /svg/fixed-income.svg
---

*The **duration of a zero-coupon bond** is always exactly equal to its maturity, while a [coupon bond](/bond/) with the same maturity has shorter duration. This difference exists because **duration** measures the average time you wait to recover your money, weighted by cash flows. A zero-coupon bond pays nothing until the end, so you wait the full maturity. A coupon bond pays you cash along the way, shortening your weighted average wait. Duration is why a 10-year zero-coupon bond is more sensitive to [interest rate](/interest-rate/) moves than a 10-year coupon bond.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration Basics — Zero-Coupon vs Coupon</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Coupon payments compress duration by moving a portion of cash recovery forward in time.</div>

|   |   |
|---|---|
| **Zero-coupon Macaulay duration** | Always equals maturity (N years) |
| **Coupon bond Macaulay duration** | Less than maturity (N - δ years, where δ > 0) |
| **10-year zero-coupon duration** | 10 years exactly |
| **10-year 5% coupon bond duration** | ~8.1 years (typical; varies with yield) |
| **Modified duration use** | Approximates percentage price change per 1% yield move |
| **Duration sensitivity** | Higher duration = larger price swings on rate changes |

</aside>

## What Duration Measures

Duration is **the effective maturity of a bond**, weighted by when you get paid. It answers the question: "On average, how long until I recover my investment?"

For a simple example:

- **10-year zero-coupon bond**: You invest $100 and get paid nothing for 10 years, then receive $100 × (1 + yield). You wait the full 10 years. Duration = 10.
- **10-year coupon bond paying 5% annually**: You invest $100 and receive $5 per year for 10 years, plus $100 at the end. Some money comes back early (the coupons), so your average wait is less than 10 years. Duration ≈ 8.1 years (for typical yields).

This is not academic nitpicking. Duration directly measures [interest rate risk](/interest-rate-risk/). A bond with 8-year duration will fall roughly 8% in price if yields rise 1 percentage point. A bond with 10-year duration falls 10% under the same shock. The zero-coupon bond's longer duration means larger price swings.

## Macaulay Duration: The Intuitive Calculation

Macaulay duration is the weighted-average time until you receive cash flows. Here is the formula:

**Duration = Σ (t × PV(CF_t)) / Bond Price**

Where:
- t = years until cash flow
- PV(CF_t) = present value of cash flow at time t
- Sum all weighted flows, then divide by the bond price

### Zero-Coupon Bond Example

A $100 face value, 10-year zero-coupon bond yielding 5%:

- Bond price: $100 / (1.05)^10 = $61.39
- Only cash flow: $100 at year 10
- Duration = (10 × $100) / $61.39 = 16.29 / 1.00 = 10 years

The duration is exactly the maturity. This always holds for zero-coupon bonds.

### Coupon Bond Example

A $100 face value, 10-year coupon bond paying 5% annually, yielding 5%:

- Bond price: $100 (since coupon = yield; par value)
- Cash flows: $5 at each year 1–10, plus $100 at year 10

| Year | Cash Flow | PV @ 5% | Weight (Years × PV) |
|------|-----------|---------|---------------------|
| 1 | $5 | $4.76 | $4.76 |
| 2 | $5 | $4.54 | $9.07 |
| 3 | $5 | $4.33 | $12.99 |
| 4 | $5 | $4.13 | $16.52 |
| 5 | $5 | $3.94 | $19.71 |
| 6 | $5 | $3.76 | $22.55 |
| 7 | $5 | $3.58 | $25.05 |
| 8 | $5 | $3.42 | $27.36 |
| 9 | $5 | $3.26 | $29.33 |
| 10 | $105 | $64.79 | $647.93 |
| **Total** | | **$100** | **$815.27** |

Duration = $815.27 / $100 = 8.15 years

The coupon bond's duration (8.15 years) is shorter than its maturity (10 years) because coupons compress the time-weighting. You recover money earlier via coupons, reducing your average wait.

## Why Zero-Coupon Duration Always Equals Maturity

The mathematical reason is simple: A zero-coupon bond has only one cash flow, at maturity. If that single flow is at time N, the weighted average time is N. There is no earlier cash to compress it.

For a coupon bond, earlier cash flows (the coupons) carry positive weight in the duration calculation, pulling down the average.

## Modified Duration and Price Sensitivity

Traders use **modified duration** to estimate how much a bond's price changes when yields move:

**Modified Duration = Macaulay Duration / (1 + Yield)**

For the coupon bond above:

**Modified Duration = 8.15 / 1.05 = 7.76 years**

A rule of thumb: A bond's price falls roughly **Modified Duration %** for every 1 percentage point rise in yield.

If yields rise 1 point (from 5% to 6%):
- **Zero-coupon bond** (10-year, modified duration ≈ 9.52): Falls about 9.5%
- **Coupon bond** (10-year, modified duration ≈ 7.76): Falls about 7.8%

The zero-coupon bond's steeper duration makes it more volatile. This matters for investors trying to lock in returns or hedge [interest rate risk](/interest-rate-risk/).

## Duration Changes as Yields Move

Here is a subtlety often overlooked: duration is not fixed. As [yields](/yield-curve/) change, duration changes.

Consider the 10-year zero-coupon bond again. If yields rise from 5% to 6%, the bond's modified duration drops slightly (fewer years of growth at lower present value). But the Macaulay duration stays exactly 10 years because the maturity and single cash flow do not change. For zero-coupon bonds, Macaulay duration is truly constant.

For coupon bonds, both Macaulay and modified duration shift with yields. As yields rise, duration *shortens* (the present value of far-future coupons shrinks, pulling the weight closer to nearer payments). As yields fall, duration *lengthens*.

## Practical Implications for Bond Investors

**Interest rate exposure**: If you expect yields to fall (prices to rise), longer-duration bonds offer more upside. A zero-coupon bond's longer duration than a comparable coupon bond makes it the superior play in a falling-rate environment—but also the riskier play if rates rise.

**Reinvestment risk**: Zero-coupon bonds avoid [reinvestment risk](/reinvestment-risk/) (the risk that falling yields will force you to reinvest coupons at lower rates). But they concentrate all your cash recovery at one point in time. Coupon bonds spread cash flows, offering more flexibility and less timing risk.

**Callable bonds**: [Callable bonds](/callable-bond/) (where the issuer can redeem early) have duration that shortens dramatically if yields fall (because early call becomes likely). Zero-coupon bonds cannot be called, so their duration remains stable.

**Hedging**: Portfolio managers use duration to hedge interest rate exposure. A portfolio can be matched to a liability by matching durations; zero-coupon bonds simplify this because their duration is transparent and equals their maturity.

## Duration, Convexity, and Larger Moves

Duration is a linear approximation: it works well for small yield moves (0.5–2 points). For larger moves, **convexity** (the curvature of the price-yield relationship) becomes important.

Zero-coupon bonds and coupon bonds have different convexity profiles, but that is beyond the scope of duration itself. The key insight: duration is shorter for coupon bonds, and that difference drives meaningful volatility differences between them.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — Comprehensive explanation of effective maturity measures
- [Bond](/bond/) — Structure, pricing, and mechanics of fixed-income securities
- [Yield-to-Maturity](/yield-to-maturity/) — Key metric in bond valuation
- [Interest Rate Risk](/interest-rate-risk/) — How duration translates to price sensitivity
- [Coupon Payment](/coupon-payment/) — Role of periodic interest in duration

### Wider context

- [Callable Bond](/callable-bond/) — Bonds where issuer control affects duration
- [Reinvestment Risk](/reinvestment-risk/) — Risk of falling rates on reinvested coupons
- [Fixed-Income Strategy](/bond-etf/) — Portfolio construction with duration targets
- [Yield Curve](/yield-curve/) — Term structure and duration across the market
- [Discount Rate](/discount-rate/) — Underlying concept in present-value calculations

</div>

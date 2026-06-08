---
title: "Bond Duration vs Maturity: What Is the Difference?"
description: "Bond duration vs maturity difference: maturity is the repayment date; duration is the weighted-average time to receive cash flows, which determines price sensitivity to interest-rate changes."
keywords:
  - bond duration vs maturity difference
  - duration
  - maturity
  - interest rate sensitivity
  - bond price risk
image: "/svg/fixed-income.svg"
---

*A bond's **maturity** is when the issuer repays principal; its **duration** is the weighted average time until all cash flows are received, and duration is what determines how much the bond's price moves when interest rates change.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration vs Maturity — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Two distinct time measures with different implications for bond risk.</div>

|   |   |
|---|---|
| **Maturity** | Calendar date when issuer repays the loan principal |
| **Duration** | Weighted-average years until you receive all cash flows (coupons + principal) |
| **Price sensitivity** | Determined by duration, not maturity |
| **Example** | A 10-year bond with 5% coupon has maturity = 10 years but duration ≈ 7.8 years |
| **Effect of coupons** | Higher coupons reduce duration because you receive cash sooner |
| **Duration formula** | Macaulay duration weights each cash-flow timing by present value |
| **Practical use** | A 1% interest rate move changes price by roughly 1× duration (in percentage terms) |

</aside>

## Maturity: The Legal Repayment Date

Maturity is straightforward. A bond that matures in 10 years means the issuer owes you the face amount (usually $1,000) at the end of year 10. If you buy a 30-year Treasury bond, the U.S. government will pay you back in 30 years. Maturity appears in every bond's prospectus and term sheet. It is the non-negotiable deadline.

Yet maturity alone tells you almost nothing about how much the bond's price will fluctuate if interest rates rise or fall. A 30-year zero-coupon bond and a 30-year bond with a 10% [coupon-rate](/coupon-rate/) have the same maturity but will behave very differently in response to rate shocks. This is where duration enters.

## Duration: The Weighted-Average Time to Cash Flows

**Duration** is a measure of how long, on average, you must wait to receive your cash back. If a bond pays [coupon-payments](/coupon-payment/) annually and returns principal at maturity, duration accounts for both. Every coupon you collect early—before maturity—shortens your average waiting time.

The most common version is **Macaulay duration**, calculated as a weighted average of the time to each cash flow, where the weights are the present values of those cash flows. Here's a simple example:

Suppose you buy a 3-year bond with a 5% coupon and 5% yield. You receive:
- Year 1: $50 coupon
- Year 2: $50 coupon
- Year 3: $1,050 (final coupon + principal)

The present value of each cash flow, at the 5% yield, determines its weight. The Year 1 coupon ($50 discounted) is worth less than the Year 3 payment. Duration is the sum of (years × weight). For this bond, duration works out to approximately 2.72 years, even though maturity is 3 years.

The presence of the coupon pulls the average waiting time downward. A zero-coupon bond, by contrast, has duration equal to its maturity because you receive no interim cash—all your money arrives at maturity.

## Why Duration Matters More Than Maturity for Price Risk

The critical insight: **a bond's price sensitivity to interest-rate changes is driven by duration, not maturity.**

When interest rates rise, bond prices fall because new bonds offer higher yields. A bond with a long maturity but high coupons (and thus short duration) loses less value than a bond with the same maturity but lower coupons (and longer duration). This is because you are receiving more cash from the high-coupon bond before maturity, reducing your effective exposure to rate changes.

A useful approximation: if interest rates rise by 1 percentage point, a bond's price falls by roughly the duration percentage. A bond with duration of 7 years will lose about 7% in value if yields rise 1%. A bond with duration of 3 years will lose about 3%.

More formally, this relationship is captured by [modified-duration](/duration/) (which adjusts Macaulay duration for the yield level) and is the basis for bond portfolio [hedging](/derivatives-hedging/) strategies.

## Duration and Bond Types

Different bond types naturally have different durations relative to their maturity:

| Bond Type | Duration Relative to Maturity | Why |
|---|---|---|
| High-coupon bond | Shorter | Early cash returns reduce average waiting time |
| Low-coupon bond | Longer | Few interim payments extend waiting time |
| Zero-coupon bond | Equal to maturity | No interim cash; all return delayed to maturity |
| Floating-rate bond | Very short | Coupon resets to market rates; price risk minimal |
| [Callable-bond](/callable-bond/) | Shorter than par | Negative convexity; if rates fall, call limits upside |

A [callable-bond](/callable-bond/) is a key example. Even if it matures in 20 years, the issuer can redeem it early if interest rates fall. Duration is often just 5–7 years because investors expect early redemption, not the full 20-year wait.

## Practical Implications

Fixed-income managers build portfolios by targeting duration, not maturity. A manager seeking "moderate interest-rate risk" might target a duration of 4–6 years. This could be achieved through a mix of shorter-maturity bonds with low coupons and longer-maturity bonds with high coupons. The maturity ladder is secondary.

Investors also use duration to compare bonds across different coupon rates and structures. Two bonds may look similar by maturity but carry very different price risk if their duration differs. Duration also underpins the [yield-curve](/yield-curve/) and [interest-rate-risk](/interest-rate-risk/) management.

When central banks announce rate moves, fixed-income markets react based on duration expectations. A bond fund with a duration of 8 years will suffer larger losses in a rising-rate scenario than one with a duration of 4 years, regardless of maturity composition. Portfolio rebalancing, [hedge](/derivatives-hedging/) strategies, and risk limits are all set on duration, not maturity.

## Modified Duration and Convexity

In practice, portfolio managers use **modified duration**, which adjusts Macaulay duration downward slightly to reflect the yield level. Modified duration is the direct estimate of price change per 1% move in yield.

There is also **convexity**, a second-order effect. As rates move significantly, the straight-line duration approximation breaks down. Convexity captures how much better (or worse) bonds perform when rates move more than 1–2%. High-coupon bonds have positive convexity; callable bonds have negative convexity.

For large rate moves or precise portfolio hedging, both duration and convexity matter. For a rule of thumb, duration suffices.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — in-depth treatment of the concept and its formula
- [Coupon rate](/coupon-rate/) — the bond's stated interest payment, which affects duration
- [Coupon payment](/coupon-payment/) — the periodic cash flow that shortens duration vs. maturity
- [Callable bond](/callable-bond/) — matures later but has shorter duration due to call option
- [Yield to maturity](/yield-to-maturity/) — the discount rate used in duration calculations
- [Interest rate risk](/interest-rate-risk/) — how duration translates to portfolio loss in rising rates
- [Modified duration](/duration/) — the market-standard version used for price-change estimates

### Wider context

- [Bond](/bond/) — fundamental fixed-income security
- [Yield curve](/yield-curve/) — how yields vary by maturity and duration
- [Fixed-rate mortgage (personal)](/fixed-rate-mortgage-personal/) — consumer debt with interest-rate risk shaped by duration
- [Treasury bond](/treasury-bond/) — government bonds with no credit risk, duration only
- [Interest rate swap](/interest-rate-swap/) — derivative used to manage portfolio duration

</div>

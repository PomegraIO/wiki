---
title: "Duration for Corporate Bonds Explained"
description: "Duration measures a bond's price sensitivity to interest rate changes. A 5-year duration bond loses approximately 5% in value for every 1% rise in yield. Calculated as weighted-average time to cash flows."
keywords:
  - duration for corporate bonds explained
  - bond duration calculation
  - modified duration interest rate sensitivity
  - macaulay duration
image: /svg/fixed-income.svg
---

*The **duration for corporate bonds** is a measure of how sensitive a bond's price is to changes in interest rates. A bond with a 5-year duration will lose roughly 5% of its value if yields rise by 1%, and gain 5% if yields fall by 1%. Duration is the fundamental tool for comparing interest rate risk across bonds with different maturities, coupons, and prices.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration — Key Facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Duration converts yield risk into a single, comparable number: years of price sensitivity.</div>

|   |   |
|---|---|
| **Macaulay duration** | Weighted-average time until you receive cash flows (in years) |
| **Modified duration** | Macaulay duration adjusted for yield; used for price sensitivity |
| **Relationship to rate moves** | Price ≈ –Modified Duration × Yield Change (in percentage points) |
| **Example** | 5-year duration, 1% rate rise → ~5% price decline |
| **Typical ranges** | 2–10 years for investment-grade corporates |

</aside>

## What Duration Measures

Duration answers a single question: if yields change by 1%, how much will the bond's price change? It is an elasticity—a sensitivity metric. A bond with a 5-year duration has a price elasticity of approximately –5 (negative because prices move inversely to yields). A 10-year duration bond has roughly twice the rate sensitivity.

This makes duration extraordinarily useful. Two corporate bonds might have different maturities, coupons, and prices. Without a common metric, it is hard to compare their interest rate risk. Duration normalizes that risk into a single number that can be compared across any bond in any market.

Duration exists in two forms: Macaulay duration and modified duration. Macaulay duration is the weighted-average time (in years) until you receive all the bond's cash flows. Modified duration is Macaulay duration adjusted by the bond's yield, and it is the number used to calculate price sensitivity to yield changes.

## Calculating Macaulay Duration: A Worked Example

Macaulay duration is calculated as the sum of each cash flow's present value multiplied by the time to that cash flow, divided by the bond's total price.

**Bond details:**
- Par value: $1,000
- Coupon: 5% ($50 annually)
- Maturity: 3 years
- Current yield: 5% (so the bond trades at par, $1,000)

**Cash flows and present values:**

| Year | Cash Flow | PV at 5% | Weight (PV / Price) | Time × Weight |
|------|-----------|----------|---------------------|----------------|
| 1    | $50       | $47.62   | 0.04762             | 0.04762        |
| 2    | $50       | $45.35   | 0.04535             | 0.09070        |
| 3    | $1,050    | $907.03  | 0.90703             | 2.72109        |
| **Total** | | $1,000 | 1.00000 | **2.86 years** |

**Macaulay duration = 2.86 years.**

This means the average time until you receive your money back (principal and interest combined) is 2.86 years. The final payment dominates because it contains the $1,000 principal, which is the largest single cash flow.

## Converting to Modified Duration

Modified duration is used to calculate price sensitivity to yield changes. It is derived from Macaulay duration:

**Modified Duration = Macaulay Duration / (1 + Yield)**

In the example above:
- Macaulay duration: 2.86 years
- Yield: 0.05 (5%)
- Modified Duration = 2.86 / 1.05 = 2.72 years

This modified duration of 2.72 means: for every 1% (100 basis point) change in yield, the bond's price changes by approximately 2.72% in the opposite direction.

## Price Sensitivity in Action

Using the modified duration, you can estimate price changes from yield moves.

**Formula:** Approximate Price Change = –Modified Duration × Yield Change (in percentage points)

From the example, suppose yields rise from 5% to 6% (a 1% increase):
- Approximate price change = –2.72 × 1% = –2.72%
- New estimated price ≈ $1,000 × (1 – 0.0272) = $972.80

If you calculate the exact new price using the discounted cash flow formula at 6% yield, you get $972.76—the duration estimate is very close.

Conversely, if yields fall from 5% to 4%:
- Approximate price change = –2.72 × (–1%) = +2.72%
- New estimated price ≈ $1,000 × 1.0272 = $1,027.20

The exact price at 4% yield is $1,027.35, again confirming that duration gives a reliable approximation for small yield moves (up to roughly 2%).

## What Affects Duration: The Three Drivers

Three factors determine a bond's duration:

**1. Maturity** — Longer-maturity bonds have higher duration. A 30-year bond has much higher rate sensitivity than a 2-year bond. More of the cash flow is far in the future, so discount rate changes compress its present value more.

**2. Coupon rate** — Lower-coupon bonds have higher duration. A zero-coupon bond (no coupons, only a final payment at maturity) has a duration equal to its maturity because all the value is in the distant payment. A bond with high coupons has lower duration because investors receive and reinvest cash flows throughout the bond's life.

**3. Yield level** — Bonds trading at lower yields have higher modified duration. This is because the denominator in the modified duration formula shrinks. A bond yielding 2% has higher modified duration than an otherwise identical bond yielding 5%. Counterintuitively, this means bonds are more rate-sensitive when rates are low—a dynamic that amplifies losses in rising-rate environments.

## Duration for Corporate Bonds vs. Treasuries

Corporate bonds and Treasuries of the same maturity and coupon have nearly identical Macaulay duration. The credit spread does not affect the duration calculation—only maturity, coupon, and yield matter. However, corporate bonds are riskier in rising-rate environments because of credit spread risk. A 1% rise in Treasury yields often causes corporate spreads to widen (investors demand more credit premium), compounding the price loss from the higher discount rate. The true total "duration risk" of a corporate bond includes both rate duration and spread duration.

## Negative Convexity in Callable Bonds

Most corporate bonds are callable—the issuer can redeem them at par before maturity. When yields fall, the price of a callable bond rises less than a non-callable bond, because the call feature caps the upside. From a duration perspective, a callable bond appears to have lower duration than expected, especially when trading at a premium (above par). This is called negative convexity.

In practice, the dealer or platform will often quote "effective duration" for a callable bond—duration adjusted for the likelihood that the bond will be called. This is a more accurate measure of rate sensitivity than Macaulay or modified duration alone.

## Using Duration to Compare Bonds

Duration is the most efficient way to compare interest rate risk across corporate bonds. Two investment-grade corporates might differ in maturity and coupon but have similar duration, meaning they will respond similarly to rate moves. A portfolio manager targeting a specific level of rate sensitivity can balance shorter-maturity, higher-coupon bonds with longer-maturity, lower-coupon bonds to hit a target duration.

For example, a portfolio manager who wants 5 years of rate sensitivity might buy a mix of 3-year bonds (lower coupon, duration ~2.8) and 7-year bonds (higher coupon, duration ~6.2) in proportions that average to 5-year duration.

## Duration and Portfolio Risk

Duration is particularly valuable for portfolio-level risk management. The average duration of a bond portfolio tells you how much the entire portfolio's value will change if yields move by 1%. A portfolio with 5-year average duration will lose approximately 5% of its value if yields rise by 1%. This makes it easy for managers and investors to understand and control interest rate risk.

## See also

<div class="wiki-seealso">

### Closely related

- [How Corporate Bond Prices Move With Interest Rates](/how-corporate-bond-prices-move-with-interest-rates/) — How duration drives the price-yield relationship in practice
- [Yield to Worst on Corporate Bonds](/corporate-bond-yield-to-worst/) — Why duration is applied to the appropriate yield in callable bonds
- [Corporate Bond Secondary Market](/corporate-bond-secondary-market/) — How bond quotes and valuations appear in trading
- [Convexity](/convexity/) — The second-order effect that makes duration estimates more or less accurate
- [Interest Rate Risk](/interest-rate-risk/) — The general framework for bond rate sensitivity

### Wider context

- [Corporate Bond](/corporate-bond/) — Full overview of corporate bond structure and risks
- [Bond](/bond/) — General bond pricing and terminology
- [Yield to Maturity](/yield-to-maturity/) — The yield used in duration calculations
- [Treasury Bond](/treasury-bond/) — Government bonds with similar duration mechanics
- [Volatility Smile](/volatility-smile/) — Related to option-adjusted spread and effective duration calculations

</div>

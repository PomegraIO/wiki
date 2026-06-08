---
title: "How TIPS Interest Payments Are Calculated"
description: "How the inflation-adjusted principal affects coupon payments on Treasury Inflation-Protected Securities, with calculation examples."
keywords:
  - tips interest payments
  - tips coupon calculation
  - how tips work
  - inflation adjusted principal
  - tips accrued inflation
---

*On a **Treasury Inflation-Protected Security (TIPS)**, the principal grows with inflation, and the coupon payment is calculated on that adjusted principal each period. If inflation erodes the dollar, the bond's par value rises, ensuring the holder keeps pace with real purchasing power. Understanding how the coupon is calculated month by month is essential to predicting actual cash flows.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TIPS Interest Payments — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">TIPS coupons are paid on inflation-adjusted principal, making real return the true fixed component of the bond.</div>

|   |   |
|---|---|
| **Coupon type** | Fixed percentage (e.g., 2.5%) on adjusted principal |
| **Principal adjustment** | Tied to Consumer Price Index, lagged by 3 months |
| **Coupon frequency** | Semi-annual (every 6 months) |
| **Inflation index** | Non-seasonally adjusted CPI-U (all urban consumers) |
| **Accrual period** | Applies inflation for the month of coupon date + two months prior |
| **Minimum redemption** | Par value if deflation brings principal below issuance price |
| **Holding to maturity** | Investor receives the greater of original par or inflation-adjusted par |

</aside>

## The mechanics of inflation adjustment

Unlike a traditional [bond](/bond/), where par is fixed at $1,000 and the coupon pays a percentage of that fixed amount, TIPS par value fluctuates with inflation. The Treasury publishes an "index ratio" each month, calculated by dividing the current CPI level by the base CPI at issuance.

A TIPS issued with an index ratio of 1.000 at a par of $1,000 will have a par of $1,050 if the cumulative inflation since issuance is 5%. The coupon—stated at issuance as a fixed percentage—is then applied to that adjusted $1,050 principal.

The adjustment lags by three months. If you are receiving a coupon payment on June 15, the Treasury uses CPI data through March 15 to calculate the principal adjustment. This three-month lag exists because the CPI for a given month is not finalized until weeks after month-end, and the Treasury needs time to process and publish updated par values.

## Worked example

Imagine a 10-year TIPS issued on June 15, 2024, with a par of $1,000 and a coupon rate of 2.0%.

**At issuance (June 15, 2024):**
- Par value: $1,000
- Index ratio: 1.000 (baseline)
- First coupon payment (December 15, 2024): calculated on original $1,000 par

**By December 15, 2024 (first coupon):**
Suppose cumulative inflation since issuance is 0.75% (measured through September 2024, three months prior). The index ratio is now 1.0075.
- Adjusted par: $1,000 × 1.0075 = $1,007.50
- Coupon payment: $1,007.50 × 0.02 × 0.5 (half-year) = $10.08

**By June 15, 2025 (second coupon):**
Suppose cumulative inflation through March 2025 reaches 1.50%. The index ratio is 1.0150.
- Adjusted par: $1,000 × 1.0150 = $1,015.00
- Coupon payment: $1,015.00 × 0.02 × 0.5 = $10.15

Notice the coupon increased from $10.08 to $10.15, even though the coupon rate (2.0%) is fixed. The rise reflects the growing inflation-adjusted principal.

## Real yield vs. nominal yield

The coupon rate on TIPS is the "real yield"—the return you receive above inflation. Because the principal itself grows with inflation, the bond automatically protects the holder's purchasing power.

A traditional [corporate bond](/corporate-bond/) or [treasury bond](/treasury-bond/) might offer a 4% nominal yield. If inflation runs at 3%, the real yield is roughly 1% (in simplified terms). A TIPS coupon rate of 2.0% is a 2.0% real yield—you receive that return whether inflation is 0% or 5%.

This distinction matters for long-term savers. Over a 20-year horizon, cumulative inflation can be severe. A TIPS ensures you receive the coupon on the inflation-adjusted principal, making your purchasing power stable. A conventional bond's fixed dollar coupons become worthless if inflation accelerates.

## Accrual between coupon dates

If you buy TIPS between coupon dates, you pay [accrued interest](/accrued-interest/) just as with any bond. But TIPS accrued interest is calculated on the inflation-adjusted principal, not the original par.

If the bond's adjusted par is $1,015 and the coupon rate is 2.0% semi-annually, the daily accrual is $1,015 × 0.02 / 365 = $0.0556 per day. The buyer receives a credit for that accrual when the next coupon is paid; the seller receives the accrual cash for the days held.

## Deflation protection

If deflation occurs—prices fall and cumulative CPI declines—the TIPS principal is protected at par. If a TIPS is issued at $1,000 and deflation causes the index ratio to drop to 0.97, the par value is not reduced to $970. Instead, it remains at $1,000 (the floor).

However, if you hold to maturity, you receive par or inflation-adjusted par, whichever is greater. If deflation has reduced the adjusted par below $1,000, you still receive $1,000. This is the investor's deflation floor; the Treasury bears the risk of having to redeem above par in a deflation scenario.

The practical impact: in a deflationary environment, TIPS coupon payments may decline (if principal falls), but your principal is protected. You cannot lose to deflation if you hold the bond to maturity; you receive at minimum par.

## Secondary market and inflation accrual

Buying TIPS in the secondary market (bond trading markets) requires careful attention to inflation accrual. If you purchase a TIPS with an adjusted par of $1,025 and the coupon rate is 2.5%, the price you see on the screen is typically quoted as a percentage of the *current* adjusted par, not the original par.

A TIPS trading at 101.5 with an adjusted par of $1,025 costs you $1,015.375 plus accrued inflation interest. This can be confusing; prices, yields, and effective returns all hinge on the current inflation-adjusted principal, which changes monthly. Traders and fund managers use specialized tools to track and reconcile these moving targets.

## Tax implications

TIPS holders owe federal income tax on two sources: the coupon payments received in cash and the accrued inflation adjustment, whether or not inflation has been realized in cash. A TIPS that accrues $50 in inflation adjustment over a tax year is taxable on that $50, even if you have not sold the bond and taken a gain.

This creates a "phantom income" problem. You receive the coupon in cash but owe tax on inflation accrual you have not collected in cash. It is why TIPS are often held in [tax-deferred accounts](/roth-ira/) like IRAs and pension funds, where the tax liability is deferred until withdrawal.

In a taxable account, the effective after-tax return on TIPS is lower than the stated coupon, because you are paying tax on accrued (not realized) gains. Investors in high tax brackets are particularly sensitive to this; low-income investors and institutions with tax-exempt status are indifferent.

## Practical impact on portfolio returns

Because TIPS coupons rise with inflation, the distribution you receive in a rising-inflation environment increases. If you are living off bond income, TIPS provide a hedge: your income rises when you need it most (as prices rise). Traditional bonds pay fixed coupons; your income is constant even as your costs rise.

Conversely, if you are reinvesting coupons, the higher nominal income in inflationary periods enables you to reinvest at higher yields, compounding your real returns.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury bond](/treasury-bond/) — conventional US government fixed-income securities and their pricing
- [Consumer price index](/consumer-price-index/) — measure of inflation used to adjust TIPS principal
- [Bond](/bond/) — fundamentals of fixed-income securities and coupon mechanics
- [Current yield](/current-yield/) — relationship between bond price and income yield

### Wider context

- [Inflation risk](/inflation-risk/) — erosion of purchasing power and hedges like TIPS
- [Real interest rate](/real-interest-rate/) — inflation-adjusted return and its relationship to nominal rates
- [Yield curve](/yield-curve/) — structure of bond yields across maturities, including TIPS
- [Accrual accounting](/accrual-accounting/) — matching of income to periods in which it is earned

</div>

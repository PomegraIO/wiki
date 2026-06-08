---
title: "Bond Equivalent Yield vs Effective Annual Yield"
description: "Understand bond equivalent yield vs effective annual yield: BEY annualizes semiannual coupons, EAY accounts for compounding. Learn when each applies and how to convert."
keywords:
  - bond equivalent yield
  - effective annual yield
  - bond yield calculation
  - annual percentage rate bonds
  - semiannual compounding
  - yield comparison
---

*A **bond equivalent yield** annualizes the semiannual coupon payment without accounting for compounding, while an **effective annual yield** reflects the true year-over-year return including the impact of how often coupons are reinvested. BEY is the market standard for quoting Treasury and corporate bonds; EAY is the true economic return.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Yields — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two conventions for the same bond reflect different compounding assumptions.</div>

|   |   |
|---|---|
| **BEY formula** | Coupon rate × 2, or (Annual coupon ÷ Price) × 2 |
| **EAY formula** | (1 + BEY/2)² − 1 |
| **Market default** | U.S. Treasuries, corporates quoted in BEY |
| **When it matters** | Comparing bonds with different coupon frequencies or building multi-period portfolios |
| **Practical relationship** | EAY is always slightly higher than BEY (compounding gain) |

</aside>

## Why Bonds Use Two Yield Conventions

U.S. Treasury and corporate bonds pay coupons semiannually—twice per year. In the 1970s, the market standardized on **bond equivalent yield** because it provided a simple doubling of the semiannual yield, making quotes easy to compare across dealers without calculators. Modern screens do the math instantly, but the convention persists because market participants expect it.

The problem: doubling the semiannual yield ignores compounding. If you receive $25 of interest every six months and reinvest it at the prevailing rate, that reinvested amount earns its own return in the second half of the year. The true economic return—what you would earn if you held the bond for a full year and reinvested coupons—is slightly higher. That is **effective annual yield**.

Both are correct; they simply answer different questions. BEY is what dealers quote you at the desk. EAY is what you actually earn.

## How Bond Equivalent Yield Is Calculated

The bond equivalent yield is the simplest of the two. For a bond paying a fixed coupon twice yearly:

**BEY = (Semiannual yield) × 2**

In practice, dealers calculate the semiannual yield by solving for the discount rate that equates the bond's current price to the present value of all remaining cash flows, then double it.

**Example:** A Treasury bond trading at 102 with a 4% annual coupon (2% per half-year) has a semiannual yield of, say, 1.8%. The BEY quoted by the dealer is 1.8% × 2 = 3.6%.

This is also called the **annual percentage rate (APR)** convention in bond markets. It does no compounding within the year—it simply scales the six-month rate to twelve months by multiplication.

## How Effective Annual Yield Is Calculated

The effective annual yield accounts for the fact that each semiannual coupon, once received, can be reinvested for the remainder of the year.

**EAY = (1 + BEY/2)² − 1**

In other words: take half the BEY (the semiannual rate), add 1, square it (to reflect two half-yearly compounding periods), then subtract 1 to express it as a decimal yield.

**Example:** If BEY is 3.6%, then:
- Semiannual rate = 3.6% ÷ 2 = 1.8%
- EAY = (1.018)² − 1 = 1.03624 − 1 = 0.03624 = 3.624%

The difference—0.024 percentage points in this case—is small but compounds across a portfolio and over many years.

## When Each Convention Is Used

**Bond Equivalent Yield** is the universal market standard. Traders, brokers, and exchanges quote bonds in BEY. If you check a Treasury auction result, a municipal bond dealer's screen, or a corporate bond spread sheet, you are seeing BEY. It is the lingua franca of fixed-income markets because it is simple to compare: higher BEY means higher yield, all else equal.

**Effective Annual Yield** is used in two contexts:

1. **Investor decision-making:** If you want to know the true economic return of holding a bond, especially to compare it to an equity return or a savings account, EAY is more accurate.

2. **Securities with different coupon frequencies:** Suppose you are comparing a bond that pays coupons quarterly to one that pays semiannually. Converting both to EAY puts them on equal footing, accounting for the compounding effect of differing payment schedules.

For a single semiannual bond, the practical difference is negligible. For a laddered portfolio where you reinvest coupons over decades, the gap compounds noticeably.

## Converting Between BEY and EAY

To go **from BEY to EAY**, use the formula above:

EAY = (1 + BEY/2)² − 1

To go **from EAY to BEY**, reverse the operation:

BEY = 2 × [(1 + EAY)^(1/2) − 1]

This matters when comparing a bond yield (usually in BEY) to a money market fund yield or an annualized savings rate, which are often quoted in EAY. Converting ensures you are comparing apples to apples.

## The Reinvestment Assumption

The gap between BEY and EAY depends entirely on reinvestment. EAY assumes that coupons received at the halfway point can be reinvested at the same rate (the semiannual rate) for the second half of the year. In reality, rates change. If rates fall, reinvestment rates are lower, and actual returns fall short of EAY. If rates rise, investors may do better.

This is why [yield-to-maturity](/yield-to-maturity/) calculations always come with a reinvestment assumption—they are forecasts, not promises. The coupon is fixed; the reinvestment return is not.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield-to-maturity](/yield-to-maturity/) — the total return assuming coupons are reinvested at the YTM rate
- [Current-yield](/current-yield/) — the simple annual coupon divided by price, ignoring capital gain or loss
- [Coupon-rate](/coupon-rate/) — the fixed coupon payment printed on the bond, distinct from calculated yield
- [Bond](/bond/) — core structure of coupon payments and maturity
- [Interest-rate-risk](/interest-rate-risk/) — how bond prices move when rates change, affecting realized returns

### Wider context

- [Treasury-bill](/treasury-bill/) — short-term U.S. government bonds quoted differently, in discount yield
- [Corporate-bond](/corporate-bond/) — longer-term corporate debt, also quoted in BEY
- [Repurchase-agreement](/repurchase-agreement/) — short-term lending where yield conventions matter for pricing
- [Compound-interest](/compound-interest/) — the underlying math of how money grows over time

</div>

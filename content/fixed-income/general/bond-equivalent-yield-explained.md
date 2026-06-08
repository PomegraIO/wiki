---
title: "Bond Equivalent Yield Explained"
description: "Bond equivalent yield annualizes the discount instrument return to a semi-annual basis for apples-to-apples comparisons with coupon bonds."
keywords:
  - bond equivalent yield explained
  - money market yield
  - treasury bill yield conversion
  - semi-annual compounding
  - yield comparison
image: /svg/fixed-income.svg
---

*A **bond equivalent yield** takes the return on a short-term discount instrument—such as a [Treasury bill](/treasury-bill/) or commercial paper—and converts it to an annualised rate on a semi-annual compounding basis. This conversion lets an investor compare apples-to-apples a 91-day T-bill (sold at a discount, no coupon) with a coupon-bearing [bond](/bond/) that pays interest twice a year.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Equivalent Yield — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Standardizes short-term discount returns to bond-market conventions.</div>

|   |   |
|---|---|
| **What it is** | A yield measure that annualizes a discount instrument's return using semi-annual compounding, the standard for coupon bonds in the US. |
| **Why it exists** | T-bills and money market instruments are quoted on a discount basis (simple annual interest). Bond equivalent yield makes them directly comparable to coupon bond yields, which are quoted on a semi-annual compounding basis. |
| **Formula** | BEY = (Face Value − Price) / Price × (365 / Days to Maturity) × 2. The "2" factor converts to semi-annual compounding. |
| **Key convention** | Uses a 365-day year (not 360, which is standard for some money market yields). |
| **Common use** | Treasury bill, commercial paper, and money market fund yields; required by SEC rules for transparency. |

</aside>

## The problem: incomparable yield conventions

In the fixed-income markets, two types of instruments have different quoting conventions:

**Discount instruments (T-bills, commercial paper):** Sold at a discount to face value. The buyer pays less today and receives face value at maturity. Return is the difference between purchase price and face value. These are quoted using a simple annual yield—often on a 360-day year basis (the "bank discount yield").

**Coupon bonds:** Sold at or near par, with periodic interest payments. Yields are quoted on a semi-annual compounding basis—standard in the US Treasury and corporate bond markets.

Comparing a 90-day Treasury bill yielding 4.5% (bank discount basis) with a 10-year bond yielding 4.2% (semi-annual compounding) looks like the T-bill is better. But the two yield numbers are calculated differently, so the comparison is misleading. The T-bill yield is a simple 360-day yield; the bond yield accounts for compounding and uses a 365-day year. A true apples-to-apples comparison requires converting one to the other's basis.

## How bond equivalent yield works

The **bond equivalent yield** (BEY) standardises discount-instrument yields to the bond market's semi-annual compounding convention.

Given:
- Purchase price: P
- Face value: F
- Days to maturity: d
- Year basis: 365 days

The money market (bank discount) yield is:
**Bank Discount Yield = (F − P) / F × (360 / d)**

To convert to bond equivalent yield:

**BEY = (F − P) / P × (365 / d) × 2**

The factor of 2 converts from a simple annualized rate to a semi-annual compounding basis. This matches how coupon bond yields are reported.

## Worked example

A Treasury bill is purchased for $99,000 and matures in 91 days at face value of $100,000.

**Bank discount yield:**
(100,000 − 99,000) / 100,000 × (360 / 91) = 0.01 × 3.956 = 3.956% (or ~3.96%)

**Bond equivalent yield:**
(100,000 − 99,000) / 99,000 × (365 / 91) × 2
= 0.01010 × 4.011 × 2
= 0.0809 or **8.09%**

The BEY is roughly double the bank discount yield because:
1. The denominator is the purchase price (99,000), not face value (100,000), slightly raising the rate.
2. The 365-day year vs. 360-day year adds ~1.4%.
3. The factor of 2 accounts for semi-annual compounding.

Now the T-bill's 8.09% BEY can be compared directly with a coupon bond's semi-annual yield. If a bond is quoted at 7.80%, the T-bill is slightly more attractive on a yield basis.

## Why semi-annual compounding?

US Treasury and corporate bonds pay [coupon payments](/coupon-payment/) twice per year. The yield-to-maturity quoted in bond markets reflects this semi-annual frequency. A bond quoted at 4.00% yield means:
- 2.00% paid every six months.
- (1.02)^2 − 1 = 4.04% effective annual return.

Short-term instruments like T-bills don't have multiple payment periods, so the bond market's semi-annual convention is imposed artificially—but consistently. This makes all fixed-income securities comparable on a single yield basis.

## Bond equivalent yield vs. other yield measures

Several yield measures exist for short-term instruments. Understanding the differences prevents errors:

| Yield Type | Basis | Formula | Use |
|---|---|---|---|
| **Bank Discount Yield** | 360-day year; simple interest | (F − P) / F × (360 / d) | Quoted in T-bill markets; simplest |
| **Money Market Yield** | 365-day year; simple interest; P in denominator | (F − P) / P × (365 / d) | Treasury markets; closer to realized return |
| **Bond Equivalent Yield** | 365-day year; semi-annual compounding | (F − P) / P × (365 / d) × 2 | Direct comparison with coupon bonds |
| **Effective Annual Yield** | Accounts for all compounding | (F / P)^(365/d) − 1 | True annualized return |

For a 91-day T-bill bought at $99,000 (face $100,000):
- Bank discount yield: 3.96%
- Money market yield: 4.06%
- Bond equivalent yield: 8.09% (this is the 2× factor)
- Effective annual yield: 8.04%

(The effective annual yield is close to BEY because a 91-day investment doesn't compound much.)

Investors and traders need to know which basis they are working with. Many T-bill quotes are given in bank discount yield, but regulators require disclosure in BEY.

## Semi-annual compounding in detail

The semi-annual adjustment is not arbitrary. In the bond market, a 4.00% yield means:
- Six months: earn 2.00%
- Next six months: earn 2.00% on the compounded base

Total return = (1 + 0.02) × (1 + 0.02) − 1 = 1.0404 − 1 = 4.04% (effective annual)

For a short-term instrument using BEY, we mimic this by multiplying the annualized simple rate by 2:

**BEY = Simple Annual Rate × 2**

where the simple annual rate is (F − P) / P × (365 / d).

This factor-of-2 adjustment assumes that the investor could reinvest the mid-year return at the same rate. In practice, reinvestment rates vary, so BEY is an approximation. But it standardises comparisons across the market.

## Practical application

**For investors evaluating short-term holdings:** A money market fund or T-bill portfolio yielding 3.50% in bank discount terms is actually 3.59% in money market yield and 7.18% in bond equivalent yield. If comparing to a short-duration bond fund quoted at 3.70% (semi-annual), the bond fund offers marginally more; if the short-term yield is quoted as 7.50% BEY, they are nearly identical.

**For bond traders:** Converting T-bill yields to BEY is essential when constructing hedges or comparing the relative value of bills vs. short-dated coupon bonds. A futures contract on a [Treasury bill](/treasury-bill/) may be quoted in one basis; a short-dated [Treasury bond](/treasury-bond/) in another. The trader must reconcile them.

**For SEC disclosure:** Money market funds and other short-term investment vehicles are required to disclose yields on a bond equivalent basis so that retail investors can compare them to bond-fund yields transparently.

## Limitations and caveats

- **Assumes reinvestment:** The factor-of-2 adjustment assumes you reinvest the first six months' earnings at the same rate. In reality, rates may move.
- **Applies only to short instruments:** BEY is most relevant for items maturing within a year. For longer-dated instruments, there are multiple coupon periods, and the semi-annual compounding is more accurate (not an approximation).
- **Ignores credit risk differences:** Comparing a Treasury bill's BEY to a corporate paper's BEY ignores [credit risk](/credit-risk/). The corporate paper is riskier and *should* yield more.
- **Not the same as effective annual yield:** BEY is an annualized rate assuming semi-annual compounding, but it does not account for the exact timing or frequency of all cash flows. For precise comparisons over long periods, use effective annual yield or [yield-to-maturity](/yield-to-maturity/).

## See also

<div class="wiki-seealso">

### Closely related

- Discount Instrument — short-term security sold below face value; basis for bond equivalent yield
- [Treasury Bill](/treasury-bill/) — US government short-term debt; standard example for BEY
- [Coupon Payment](/coupon-payment/) — periodic interest on bonds; semi-annual frequency drives BEY convention
- [Yield-to-Maturity](/yield-to-maturity/) — the total return on a coupon bond held to maturity
- [Current Yield](/current-yield/) — annual coupon divided by price; differs from YTM
- [Credit Risk](/credit-risk/) — riskier instruments (e.g., commercial paper) should yield more than Treasury equivalents

### Wider context

- [Money Market Fund](/money-market-fund/) — invests in short-term instruments; yields quoted in BEY for comparability
- [Bond](/bond/) — interest-bearing debt; yields quoted on semi-annual compounding basis
- [Federal Funds Rate](/federal-funds-rate/) — overnight borrowing rate; affects short-term yields
- [Interest Rate Risk](/interest-rate-risk/) — price sensitivity of bonds to rate changes
- Fixed Income — asset class encompassing bonds and money market instruments

</div>

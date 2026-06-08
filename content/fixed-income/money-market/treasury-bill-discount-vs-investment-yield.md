---
title: "Treasury Bill Discount Yield vs Investment Yield"
description: "Treasury bill discount yield vs investment yield difference: why T-bills quote two yields and how to convert between them."
keywords:
  - treasury bill discount yield
  - investment yield
  - bond equivalent yield
  - bank discount yield
  - treasury yield conversion
image: /svg/fixed-income.svg
---

*A **treasury bill discount yield vs investment yield** confusion stems from the fact that T-bills are quoted in two different ways in the market: the **bank-discount yield** (used by dealers and the [Federal Reserve](/federal-reserve/)) and the **investment yield** or bond-equivalent yield (the actual return an investor realizes). The two figures differ because they use different day-count conventions and compound differently, and knowing how to convert between them is essential for comparing money-market investments.*

## Why Two Yield Figures Exist

[Treasury bills](/treasury-bill-discount-vs-investment-yield/) are sold at a discount to [par value](/par-value/)—if you buy a $100 bill maturing in 90 days, you might pay $98.50. The $1.50 difference is your interest income.

The problem arises because there are two natural ways to express that return:

1. **Bank-discount yield:** Annualizes the discount as a percentage of par value, using a 360-day year.
2. **Investment yield (bond-equivalent yield):** Annualizes the actual dollar gain as a percentage of the purchase price, using a 365-day year.

The Federal Reserve and T-bill dealers have historically quoted bank-discount yield because it simplifies calculations in the primary market. But investors who buy T-bills in [secondary markets](/secondary-market/) or hold them to maturity care about investment yield—the true annual return on their money.

## Bank-Discount Yield Formula

The bank-discount yield is calculated as:

$$\text{BDY} = \left( \frac{\text{Discount}}{\text{Par Value}} \right) \times \left( \frac{360}{d} \right) \times 100\%$$

Where:
- **Discount** = Par value minus purchase price
- **Par Value** = $100 (or any denomination)
- **d** = days to maturity

**Example:** A 90-day T-bill with par value of $100 sells for $98.50.
- Discount = $100 − $98.50 = $1.50
- BDY = ($1.50 ÷ $100) × (360 ÷ 90) × 100% = 1.5% × 4 = **6.0%**

## Investment Yield (Bond-Equivalent Yield) Formula

The investment yield is:

$$\text{IY} = \left( \frac{\text{Discount}}{\text{Purchase Price}} \right) \times \left( \frac{365}{d} \right) \times 100\%$$

Where:
- **Discount** = Par value minus purchase price
- **Purchase Price** = what you actually paid
- **d** = days to maturity

**Same example:** 90-day T-bill, par $100, purchase price $98.50.
- Discount = $1.50
- IY = ($1.50 ÷ $98.50) × (365 ÷ 90) × 100% = 1.523% × 4.056 ≈ **6.18%**

Notice the investment yield is *higher* than the bank-discount yield. This reflects two differences:
1. **Day-count:** 365 vs 360 days inflates the annualization factor.
2. **Base:** Dividing by purchase price ($98.50) rather than par ($100) increases the percentage return.

## Why These Conventions Matter

When a dealer quotes a T-bill at "6.00%," they typically mean bank-discount yield. If you want to compare that T-bill to a [money-market fund](/money-market-fund/) that quotes its yield as investment yield, or to a certificate of deposit that compounds on a 365-day basis, you must convert both to the same basis.

The conversion allows apples-to-apples [yield](/yield-curve/) comparison across different money-market instruments—[commercial paper](/), [banker's acceptances](/), and repurchase agreements all use different quoting conventions.

## Conversion Between the Two Yields

To convert bank-discount yield to investment yield:

$$\text{IY} = \text{BDY} \times \frac{365}{360 - (\text{BDY} \times d)}$$

Where **d** is days to maturity.

**Using the 6.00% BDY example (90 days):**
- IY = 6.00% × 365 ÷ (360 − (6.00% × 90))
- IY = 6.00% × 365 ÷ (360 − 5.4)
- IY = 6.00% × 365 ÷ 354.6
- IY ≈ **6.18%**

This matches our direct calculation above.

To go the other direction (investment yield to bank-discount yield):

$$\text{BDY} = \frac{\text{IY} \times 360}{365 + (\text{IY} \times d)}$$

For the 6.18% IY (90 days):
- BDY = 6.18% × 360 ÷ (365 + (6.18% × 90))
- BDY = 6.18% × 360 ÷ (365 + 5.56)
- BDY = 6.18% × 360 ÷ 370.56
- BDY ≈ **6.00%**

## Which Yield Do You Use?

**For comparing T-bills to each other:** Use bank-discount yield. Dealers and the Federal Reserve quote this, and it is the standard in [primary-market](/primary-market/) auctions.

**For comparing T-bills to other investments:** Convert to investment yield (bond-equivalent yield). If you are evaluating whether a 90-day T-bill or a [money-market fund](/money-market-fund/) offers a better return, both must be on a 365-day, purchase-price basis.

**For actual returns:** Investment yield is closer to what you will actually earn, because it uses your actual purchase price as the denominator and the calendar year (365 days) for annualization.

## The [Fed Funds Rate](/federal-funds-rate/) Connection

The [Federal Reserve](/federal-reserve/) also manages short-term [interest rates](/interest-rate/) through [open-market operations](/), which often involve T-bills and repurchase agreements. The Fed typically quotes its target [fed funds rate](/federal-funds-rate/) and [treasury bill](/treasury-bill-discount-vs-investment-yield/) auction results in bank-discount terms, which is why understanding both conventions is important for interpreting central-bank communication.

## Practical Takeaway

Money-market investors should always ask: "Is that yield on a bank-discount or investment basis?" The difference is small for very short maturities (a few days) but can exceed 20 basis points for T-bills maturing in 180+ days. When yields are thinly quoted and competition for returns is fierce, that gap can meaningfully affect the choice between instruments.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill-discount-vs-investment-yield/) — core money-market instrument
- [Money-Market Fund](/money-market-fund/) — holder of T-bills and similar instruments
- [Bond Equivalent Yield](/treasury-bill-discount-vs-investment-yield/) — standard basis for yield comparison
- [Yield Curve](/yield-curve/) — relationship between maturity and yield
- [Overnight Repo Rate vs Fed Funds Rate](/overnight-repo-rate-vs-fed-funds-rate/) — related short-term [interest rates](/interest-rate/)

### Wider context

- [Federal Reserve](/federal-reserve/) — conducts T-bill auctions and manages short-term rates
- [Primary Market](/primary-market/) — where T-bills are auctioned
- [Secondary Market](/secondary-market/) — where T-bills trade between investors
- [Compound Interest](/compound-interest/) — underpins yield calculations

</div>

---
title: "Day-Count Conventions"
description: "How Actual/360, Actual/365, and 30/360 rules alter accrued interest and yield calculations for bonds."
keywords:
  - day-count convention
  - actual/360
  - actual/365
  - 30/360
  - accrued interest
  - bond yield
  - interest accrual
image: "/svg/fixed-income.svg"
---

*A **day-count convention** is the rule governing how many days elapse in an interest period for the purpose of calculating [accrued interest](/accrued-interest/) and [yield-to-maturity](/yield-to-maturity/). Three main conventions—Actual/360, Actual/365, and 30/360—are used globally, and choosing between them can shift a bond's quoted return and the amount owed at settlement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Day-Count Conventions — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income concepts." />

<div class="wiki-infobox-caption">A small technical detail with measurable impact on accrued interest and yield.</div>

|   |   |
|---|---|
| **Actual/360** | Count actual calendar days; divide by 360 (most US corporate/government bonds) |
| **Actual/365** | Count actual calendar days; divide by 365 (UK, Eurobonds, many index funds) |
| **30/360** | Assume each month has 30 days, each year has 360 (some corporate and municipal bonds) |
| **Effect on yield** | Small but measurable; investors must match the convention to the bond |
| **Settlement implication** | Determines the [full price](/full-price-vs-clean-price/) owed to the seller |
| **Why it exists** | Historical: 360-day years simplified hand calculation before computers |
| **Bond prospectus** | Always states the convention used |

</aside>

## The core logic

The accrued interest on any [bond](/bond/) is calculated as:

Accrued Interest = Coupon Payment × (Days Elapsed / Days in Period)

This tells you what fraction of the coupon has been earned since the last payment date. But "days elapsed" and "days in period" depend on the convention chosen. Over a year or two, the differences seem trivial. Over a long coupon period, or across a portfolio of thousands of bonds, the cumulative effect is material.

## Actual/360

The Actual/360 convention (also called "Money Market Basis" in some contexts) counts the true number of calendar days that have elapsed, then divides by 360. It is the global standard for US corporate bonds, US government bonds, and most floating-rate instruments.

Example: A bond paying a 4% semi-annual coupon ($20 per $1,000 face value, or $10 per half-year). The coupon period runs from March 1 to August 31. Today is May 15. Using Actual/360:

- Days from March 1 to May 15 = 75 actual days
- Days from March 1 to August 31 = 184 actual days (March has 31, April has 30, May has 31, June has 30, July has 31, August has 31)
- Accrued Interest = $10 × (75 / 184) = $4.08

Why 360? Historically, bankers used a 360-day year for simplicity in hand calculation—it divides evenly by 2, 3, 4, 6, 12, and other common factors. Computers have made this obsolete, but the convention persisted because it was the standard when electronic trading began.

## Actual/365

The Actual/365 convention counts actual calendar days and divides by 365. It is standard in the UK gilt market, most Eurobond markets, and is the basis for many index calculations and floating-rate benchmarks.

Using the same bond as above:

- Days from March 1 to May 15 = 75 actual days
- Days from March 1 to August 31 = 184 actual days
- Accrued Interest = $10 × (75 / 184) = $4.08

Wait—the result is identical in this case. That's because we divided by the actual coupon period (184 days), not by a standardised figure. The difference emerges when the bond specifies a one-year coupon period and you must divide by either 360 or 365.

Example: Semi-annual coupon, six months from now. Using Actual/365:
- Days elapsed = 90 (three months)
- Days in period = 182.5 (one year / 2 = 182.5 days, on average)
- Accrued Interest = $10 × (90 / 182.5) = $4.93

Using Actual/360:
- Days in period = 180 (one year / 2 = 180 days under the 360 convention)
- Accrued Interest = $10 × (90 / 180) = $5.00

The Actual/360 version gives a slightly higher accrued interest—$5.00 instead of $4.93—because the denominator is smaller. Over thousands of trades, this compounds.

## 30/360

The 30/360 convention (also called "Bond Basis") assumes each month has exactly 30 days and each year has exactly 360 days. It is common in the US corporate bond and municipal bond markets, particularly among older or more traditional issuers.

To calculate days under 30/360:
1. Treat each month as having 30 days.
2. Treat the year as having 360 days.
3. Apply special rules: if a start or end date falls on the 31st of a month, treat it as the 30th. If the start date is February 28 (or 29 in a leap year), keep it; if the end date is February 28/29, treat it as the 30th of February.

Example: From March 1 to August 31, under 30/360:
- March 1 to March 30 = 29 days (not 30, because the start is the 1st)
- April 1 to April 30 = 30 days
- May 1 to May 30 = 30 days
- June 1 to June 30 = 30 days
- July 1 to July 30 = 30 days
- August 1 to August 30 = 30 days
- Total = 29 + 30 + 30 + 30 + 30 + 30 = 184 days

And from March 1 to August 31:
- Use 184 days (treating August 31 as August 30)

30/360 is tidier to calculate by hand but less precise—it ignores the actual number of days in February, for instance. Its main advantage is consistency: the same coupon period always has the same number of days, making comparison and disclosure easier.

## Impact on yield and pricing

A bond's [yield-to-maturity](/yield-to-maturity/) and [current yield](/current-yield/) are calculated using accrued interest. If two otherwise identical bonds use different day-count conventions, their quoted yields will differ slightly. A bond using Actual/360 will show a marginally higher yield than one using Actual/365, because the accrued interest (and hence the [full price](/full-price-vs-clean-price/) paid at settlement) is slightly higher, depressing the yield.

This is why bond traders and investors must always check the convention stated in the [bond prospectus](/fund-prospectus/) or the bond's offering documentation. A seemingly attractive yield might simply reflect a choice of convention rather than genuine outperformance.

## Global variation

- **US corporate and government bonds:** Actual/360
- **UK gilts:** Actual/365 (fixed coupon); Actual/Actual in some cases
- **Eurozone bonds:** Actual/Actual (ISDA), which adapts depending on the coupon period and whether it is a leap year
- **Japanese bonds:** Actual/365
- **Municipal bonds (US):** Often 30/360
- **Floating-rate notes:** Typically Actual/360 or Actual/365

The Actual/Actual convention, common in longer-dated Eurobonds, is a hybrid: it counts actual days in each coupon period and divides by the actual number of days in that period, accounting for leap years.

## Practical implication

When you trade a bond or evaluate its return, the settlement amount you owe (the [full price](/full-price-vs-clean-price/)) depends on the day-count convention. A mispriced accrual can be spotted by manually recalculating accrued interest using the bond's stated convention; if your calculation doesn't match the dealer's invoice, an error—or fraud—may be present.

For [total return analysis](/total-return-analysis/) and [horizon return](/horizon-return/) calculations over a holding period, the convention governs how reinvestment income is compounded. Over a multi-year investment, the choice between Actual/360 and Actual/365 can shift the final return by a few basis points—small, but measurable across institutional portfolios.

## See also

<div class="wiki-seealso">

### Closely related

- [Full Price vs. Clean Price](/full-price-vs-clean-price/) — the settlement amount includes accrued interest calculated using this convention
- [Accrued Interest](/accrued-interest/) — the earned coupon owed to the seller
- [Coupon Payment](/coupon-payment/) — the periodic interest payment on a bond
- [Yield-to-Maturity](/yield-to-maturity/) — calculated using the convention's accrued interest
- [Current Yield](/current-yield/) — annual coupon divided by clean price
- [Horizon Return](/horizon-return/) — total return over a holding period, accounting for reinvestment

### Wider context

- [Bond](/bond/) — the foundational debt instrument
- [Total Return Analysis](/total-return-analysis/) — comprehensive return projection
- [Interest Rate](/interest-rate/) — the economic basis for coupon calculations
- Floating-Rate Notes — another instrument governed by day-count conventions

</div>

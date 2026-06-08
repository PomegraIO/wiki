---
title: "Discount Yield"
description: "The annualized return on Treasury bills quoted as a percentage of face value, not the purchase price."
keywords:
  - discount yield
  - treasury bill yield
  - t-bill
  - bond yield convention
  - short-term debt
image: "/svg/fixed-income.svg"
---

*The **discount yield** is the annualized percentage return on a [Treasury bill](/treasury-bill/), calculated as a fraction of the bill's face value rather than its purchase price. It is the market convention for quoting short-term U.S. government debt and differs from the [bond equivalent yield](/yield-to-maturity/), making comparisons between bills and longer bonds non-obvious.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Discount Yield — at a glance</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark representing fixed-income instruments." />

<div class="wiki-infobox-caption">Treasury bill yields quoted as a discount from face value, annualized.</div>

|   |   |
|---|---|
| **What it is** | Annualized return expressed as a percentage of face value, not purchase price |
| **Also called** | Bank discount, discount rate, T-bill discount |
| **Used for** | Treasury bills (13-week, 26-week, 52-week maturities) |
| **Formula** | (Face Value − Purchase Price) ÷ Face Value × 360 ÷ Days to Maturity |
| **Units** | Percentage per annum |
| **Quirk** | Uses 360-day year (not 365), penalizes T-bills vs. bonds |
| **Comparison** | Bond equivalent yield (BEY) adjusts discount yield for apples-to-apples comparison |

</aside>

## Why not just use the bond yield?

When you buy a [Treasury bond](/treasury-bond/), you see a [coupon rate](/coupon-payment/). When you buy a 13-week [Treasury bill](/treasury-bill/), you see a discount yield. Same instrument family, different quoting convention. This quirk has historical roots in banking practice and persists because the bill market is liquid, professional, and inertial.

A [Treasury bill](/treasury-bill/) is a pure discount instrument: you buy it at a discount to par, hold it to maturity in weeks or months, and receive face value. There's no coupon. If a 26-week bill with $10,000 face value is quoted at a 4.5% discount yield, you can work backward to find the price and your actual return. But the convention makes cross-instrument comparison awkward.

## The formula

**Discount Yield = (Face Value − Purchase Price) ÷ Face Value × (360 ÷ Days to Maturity)**

Suppose a $1,000,000 face-value 13-week (91-day) bill is quoted at a 4.50% discount yield. What is the purchase price?

Rearranging:
- (1,000,000 − Price) ÷ 1,000,000 = 4.50% × (91 ÷ 360)
- (1,000,000 − Price) ÷ 1,000,000 = 0.0450 × 0.2528 = 0.01138
- 1,000,000 − Price = 11,375
- **Purchase Price = $988,625**

You pay $988,625 today, receive $1,000,000 in 91 days. That spread of $11,375 is your profit.

## The 360-day quirk

Notice the formula uses 360 days, not 365. This is a historical banking convention—a remnant of the days when institutions used 30-day months for ease of calculation. The consequence is subtle but material: the discount yield *understates* the true annualized return relative to a 365-day convention or [bond equivalent yield](/yield-to-maturity/). A 4.50% discount yield on a 91-day bill corresponds to roughly a 4.56% bond equivalent yield (BEY).

For a portfolio manager or arbitrageur comparing a [Treasury bill](/treasury-bill/) to a [Treasury bond](/treasury-bond/) or a commercial paper instrument, this difference is crucial. You must convert to a common basis to compare returns fairly.

## Bond equivalent yield (BEY)

The [bond equivalent yield](/yield-to-maturity/) adjusts the discount yield to a 365-day basis and quotes return against purchase price (not face value), matching the way bonds are quoted:

**BEY = Discount Yield × (365 ÷ 360) ÷ (1 − Discount Yield × Days ÷ 360)**

For our 4.50% discount yield on a 91-day bill:
- BEY ≈ 4.56%

That 6 basis point bump is small but measurable. Over billions in daily bill issuance, it compounds into real money.

## Why the market uses it

The [Treasury bill](/treasury-bill/) market is deep, liquid, and fast. Dealers and investors need to quote prices in seconds. The discount yield convention, despite its oddities, is ingrained in the infrastructure: Bloomberg, Reuters, the Federal Reserve itself. Changing it would require coordination across thousands of market participants and decades of retooling. Instead, the convention persists, and traders learn to translate on the fly.

The [Treasury bill](/treasury-bill/) market is also wholesale and professional. Hedge funds, banks, and money-market funds all know the conversion. Retail investors rarely buy bills directly; they buy [money-market funds](/mutual-fund/) or [Treasury ETFs](/etf/), which handle the yield conversion behind the scenes.

## Bills vs. bonds: the comparison problem

Suppose you're allocating between a 6-month [Treasury bill](/treasury-bill/) at a 4.5% discount yield and a 10-year [Treasury bond](/treasury-bond/) at a 4.2% [coupon](/coupon-payment/). Which is the better deal?

You cannot simply compare 4.5% to 4.2%. The bill's 4.5% is discount yield; the bond's 4.2% is coupon, and its [yield-to-maturity](/yield-to-maturity/) depends on price. You must convert the bill to [BEY](/yield-to-maturity/) (roughly 4.56%) and look up the bond's [yield-to-maturity](/yield-to-maturity/). Only then can you see which offers more return for its [duration](/duration/) and [credit risk](/credit-risk/).

This is one reason [Treasury bills](/treasury-bill/) are often discussed separately from the broader bond market. The quoting mismatch creates friction in mental models and formal comparisons.

## The real numbers

In practice, the [Federal Reserve](/federal-reserve/) publishes both discount yield and [BEY](/yield-to-maturity/) for outstanding bills. Money-market analytics platforms automatically convert. But if you're reading an old article or a market commentary, you need to know: "4.5% T-bill" means discount yield, and you should convert it before comparing to bonds.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill/) — the short-term debt instrument quoted in discount yield
- [Yield-to-Maturity](/yield-to-maturity/) — the standard bond yield measure for apples-to-apples comparison
- [Bond Equivalent Yield](/yield-to-maturity/) — the adjusted discount yield for comparability
- [Coupon Payment](/coupon-payment/) — the mechanism by which bonds differ from pure-discount instruments
- [Discount Rate](/discount-rate/) — a related but different concept (the rate used in [present value](/discounted-cash-flow-valuation/) calculations)
- [Federal Funds Rate](/federal-reserve/) — the day-to-day [interest rate](/interest-rate/) that T-bills track

### Wider context

- [Bond](/bond/) — the broader asset class
- [Treasury Bond](/treasury-bond/) — the longer-maturity government debt
- [Interest Rate](/interest-rate/) — the economic determinant of all yields
- [Money Market](/mutual-fund/) — the short-term debt ecosystem
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the conceptual framework underlying all yield calculations

</div>

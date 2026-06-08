---
title: "Converting Bank Discount Yield to Investment Yield"
description: "Step-by-step formula to convert T-bill and banker's acceptance quotes from bank discount yield to bond-equivalent (investment) yield basis for fair comparison."
keywords:
  - convert bank discount yield to investment yield
  - bank discount yield formula
  - t-bill yield conversion
  - bond equivalent yield calculation
  - money market yield comparison
  - banker's acceptance yield
image: /svg/fixed-income.svg
---

*When comparing **T-bills**, banker's acceptances, and other money-market instruments quoted on a **bank discount yield** basis, you must convert them to **bond-equivalent (investment) yield** to compare them fairly with [coupon-bearing bonds](/bond/) and other fixed-income securities. The conversion is a two-step formula that adjusts for day-count conventions and the fact that discount securities earn returns via principal discount, not periodic coupons.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bank Discount to Investment Yield — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">Two different quoting conventions; one formula to reconcile them.</div>

|   |   |
|---|---|
| **What it is** | Restating a discount instrument's return using bond-equivalent yield basis |
| **Why it matters** | T-bills quoted at 4.00% bank discount actually yield ~4.06% on bond-equivalent basis |
| **Used for** | [Treasury bills](/treasury-bill/), [banker's acceptances](/alternative-trading-system/), commercial paper quoted on discount basis |
| **Day-count basis** | Discount yield: actual/360; Investment yield: actual/365 |
| **Formula step 1** | Calculate dollar discount: Face Value × (Discount Rate ÷ 365) × Days to Maturity |
| **Formula step 2** | Divide discount by purchase price; annualize by 365 days |

</aside>

## Why Two Quoting Methods Exist

[Treasury bills](/treasury-bill/) and banker's acceptances are quoted in dealer markets using a **bank discount yield** convention, which differs from the [yield-to-maturity](/yield-to-maturity/) (or **bond-equivalent yield**) used for [corporate bonds](/corporate-bond/), [municipal bonds](/municipal-bond/), and most other fixed-income securities. This historical convention persists because money-market instruments are short-term, deeply discounted, and traded among professionals who are accustomed to the shorthand.

Under bank discount yield, a security is quoted as a percentage of its face value, assuming a 360-day year. A T-bill with a face value of $10,000, quoted at 4.00% discount yield for 91 days, means the buyer pays less than face value by an amount calculated using the 360-day year. In contrast, bond-equivalent yield annualizes the actual holding-period return and uses a 365-day year, making it comparable to [coupon-bearing bonds](/bond/) and other securities.

For a buyer comparing a T-bill at 4.00% bank discount with a six-month [bond fund](/bond-etf/) yielding 4.15%, the T-bill discount basis masks the fact that the true return is higher than the quoted 4.00% suggests—creating the risk of mispricing.

## The Two-Step Conversion Formula

The conversion from bank discount yield to bond-equivalent yield has two steps:

**Step 1: Calculate the dollar discount (the gain the buyer makes at maturity)**

Dollar Discount = Face Value × (Bank Discount Yield ÷ 360) × Days to Maturity

Example: A $1,000,000 face-value T-bill quoted at 4.00% bank discount for 91 days.

Dollar Discount = $1,000,000 × (0.04 ÷ 360) × 91
Dollar Discount = $1,000,000 × 0.000111111 × 91
Dollar Discount = $10,111.11

The buyer pays $1,000,000 − $10,111.11 = $989,888.89 and receives $1,000,000 at maturity.

**Step 2: Annualize using the actual holding-period return and 365-day year**

Bond-Equivalent Yield = (Dollar Discount ÷ Purchase Price) × (365 ÷ Days to Maturity)

Using the example above:

Bond-Equivalent Yield = ($10,111.11 ÷ $989,888.89) × (365 ÷ 91)
Bond-Equivalent Yield = 0.010207 × 4.0110
Bond-Equivalent Yield = 0.04091, or 4.091%

The T-bill quoted at 4.00% bank discount actually yields 4.09% on a bond-equivalent basis.

## Why the Difference Matters

The wedge between bank discount yield and bond-equivalent yield widens as the discount yield and days to maturity increase. For very short instruments (30 days or fewer), the difference is negligible—less than 2 basis points. For longer money-market instruments (180 days, such as six-month T-bills), the spread can exceed 20 basis points.

A six-month T-bill quoted at 4.00% bank discount converts to approximately 4.08% bond-equivalent yield. A borrower shopping for short-term [secured funding](/repurchase-agreement/) must convert all quotes to a single basis to avoid accidentally accepting an unfavorable rate.

The difference arises from two sources:
1. **Day-count convention**: The bank discount method uses 360 days; bond-equivalent uses 365 days. A T-bill earning a 4% return over 91 days looks smaller when annualized over 365 days (with 365 in the denominator) than over 360 days.
2. **Return base**: Bank discount is expressed as a percentage of face value; bond-equivalent return is a percentage of the purchase price (the amount actually invested). Since the purchase price is slightly less than face value, the return on that smaller amount is slightly higher on a percentage basis.

## Practical Application: Comparing Instruments

Suppose a [CFO](/accounts-payable/) is deciding between:
- A 182-day T-bill quoted at 4.20% bank discount yield
- A commercial paper issued by a strong-credit firm, quoted at 4.35% yield (already on a bond-equivalent basis)

To compare fairly, convert the T-bill:

Dollar Discount = $1,000,000 × (0.042 ÷ 360) × 182
Dollar Discount = $21,283.33

Bond-Equivalent Yield = ($21,283.33 ÷ $978,716.67) × (365 ÷ 182)
Bond-Equivalent Yield ≈ 0.04299, or 4.30%

Now the comparison is apples-to-apples: the T-bill at 4.30% bond-equivalent yield is 5 basis points lower than the commercial paper at 4.35%. The decision can factor in [credit risk](/credit-risk/), [liquidity](/liquidity-risk/), and other considerations without quote-convention confusion.

## The Inverse: Bond-Equivalent to Bank Discount

Occasionally, traders need the reverse conversion—to quote a bond-equivalent yield as a bank discount yield. The formula is inverted:

Bank Discount Yield = (Dollar Discount ÷ Face Value) × (360 ÷ Days to Maturity)

Where Dollar Discount = (Bond-Equivalent Yield × Purchase Price × Days to Maturity) ÷ 365

This is less common in practice, since the convention is to work upward from bank discount to bond-equivalent. But it is useful for issuers or dealer desks that need to quote in both languages.

## Historical Context and Standards

The bank discount convention has roots in 19th-century banker practice, when interest on very short-term loans was simply deducted from the principal at origination—a practice called "discounting." The formula stuck in money markets because of network effects and dealer standardization. 

In the modern era, regulators and clearing systems (such as the [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/)) codify these conventions in rule books. The Financial Industry Regulatory Authority publishes standard conversion tables and calculators; most bond-market platforms and [custodians](/custodian/) automate the conversion so traders do not calculate by hand.

## Variations: Other Yield Conventions

Some securities use other conventions:
- **Simple interest yield**: Used for some commercial paper and [banker's acceptances](/alternative-trading-system/); similar to bond-equivalent but may use different day-count.
- **Street convention**: For certain money-market instruments, dealers quote on an "add-on" basis, where the yield is simply the interest divided by the principal for the holding period.

Always verify the quoting convention in a term sheet or dealer quote before committing capital.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill/) — primary instrument quoted on bank discount basis
- [Yield-to-Maturity](/yield-to-maturity/) — bond-equivalent yield and how to annualize returns
- [Coupon Rate](/coupon-rate/) — distinguishing yield from stated coupon
- [Money-Market Fund](/money-market-fund/) — vehicles that hold T-bills and other discount instruments
- [Banker's Acceptance](/alternative-trading-system/) — trade-finance instrument also quoted on discount basis

### Wider context

- [Repurchase Agreement](/repurchase-agreement/) — short-term secured borrowing using T-bills as collateral
- [Credit Risk](/credit-risk/) — comparing T-bills (nearly risk-free) with commercial paper
- [Custodian](/custodian/) — clearing and settlement systems for money-market trades
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulatory body overseeing money-market rules

</div>

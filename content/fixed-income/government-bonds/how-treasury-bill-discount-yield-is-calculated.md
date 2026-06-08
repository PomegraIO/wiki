---
title: "How Treasury Bill Discount Yield Is Calculated"
description: "Learn the bank discount yield formula for Treasury bills: how the discount, maturity, and annual basis produce the quoted yield."
keywords:
  - how treasury bill discount yield is calculated
  - bank discount yield formula
  - treasury bill bond equivalent yield
  - t-bill discount calculation
image: "/svg/fixed-income.svg"
---

*The **bank discount yield** is how Treasury bills are quoted in markets. It takes the dollar discount between the purchase price and par value, annualizes it, and divides by par—yielding a figure that looks lower than the true economic return (bond-equivalent yield) because it uses par as the denominator and assumes a 360-day year.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Treasury Bill Discount Yield — the formula and logic</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Bank discount yield understates the real return; bond-equivalent yield is more economically accurate.</div>

|   |   |
|---|---|
| **Bank discount yield formula** | (Discount / Par Value) × (360 / Days to Maturity) |
| **Discount** | Par value minus purchase price (e.g., $10,000 − $9,950 = $50) |
| **Par value** | Face value of the T-bill, always $10,000 for standard quotes |
| **360-day year** | Market convention (not 365); understates the annualized return |
| **Example: 91-day T-bill** | Discount $50, par $10,000; (50/10000) × (360/91) = 1.98% |
| **Bond-equivalent yield** | Annualizes using actual investment return and 365 days; always higher |
| **Why the difference** | Bank yield uses par as base; bond equivalent uses purchase price as base |

</aside>

## The basic formula: discount annualized

A Treasury bill is a zero-coupon instrument. You buy it at a discount to par, hold it to maturity, and collect the full face value. The yield is the return embedded in that discount.

The **bank discount yield** formula is:

**Bank Discount Yield = (Discount / Par Value) × (360 / Days to Maturity)**

Let's walk through a concrete example:

**91-day T-bill:**
- Par value: $10,000
- Purchase price: $9,950
- Discount: $50
- Days to maturity: 91

Bank Discount Yield = ($50 / $10,000) × (360 / 91)
= 0.005 × 3.956
= 0.01978 or **1.98%**

This is the yield you'll see quoted on Treasury bill market screens. It's the "headline" number.

## Why it uses par, not price

The seemingly odd choice to divide the discount by par (not by the price you paid) is convention—it keeps all T-bills on the same denominator, making them easy to compare. If the formula used the purchase price instead, every quote would differ based on the exact price, adding noise.

But economically, this understates your return. You invested $9,950 and earned $50. Your true percentage return is $50 / $9,950 = 0.503%, annualized over the 91-day holding period. Using par ($10,000) as the base artificially shrinks the percentage: $50 / $10,000 = 0.50%, which looks smaller.

## The 360-day convention: another quirk

The formula uses 360 days per year (a market legacy from before computers). Real annual returns use 365 days. This compounds the understatement: multiplying a 91-day return by 360/91 (a factor of 3.956) is smaller than multiplying by 365/91 (a factor of 4.011).

Over a 91-day T-bill, this difference seems minor, but it's real. The market quotes bank discount yields anyway for standardization across tenors and traders.

## Converting to bond-equivalent yield

To get the true economic return—the **bond-equivalent yield** (BEY)—you need to undo both quirks. The formula is:

**Bond-Equivalent Yield = (Discount / Purchase Price) × (365 / Days to Maturity)**

Using the same 91-day example:
- Discount: $50
- Purchase price: $9,950
- Days to maturity: 91

Bond-Equivalent Yield = ($50 / $9,950) × (365 / 91)
= 0.00503 × 4.011
= 0.0202 or **2.02%**

Notice: 2.02% (BEY) is higher than 1.98% (bank discount yield), even though we're looking at the same bond. The BEY is more economically accurate because it reflects your actual cash investment ($9,950) and uses a calendar year (365 days).

## Why traders still use bank discount yield

Despite the quirks, bank discount yield remains the market standard for T-bill quotes. It's embedded in Bloomberg, Reuters, the Federal Reserve's quotes, and broker screens. Switching to BEY would require retraining millions of market participants and rebuilding systems.

Also, the difference between the two is usually small (less than 0.05% on typical bills), and traders often eyeball both numbers side by side. For most purposes, knowing the bank discount yield is good enough to gauge your return—you just have to remember it's slightly overstating the par-to-price spread and understating the time value.

## Step-by-step worked example: 182-day T-bill

Let's work through a 182-day (six-month) example to solidify the logic:

**Given:**
- Par value: $10,000
- Bank discount yield quoted: 2.50%

First, solve for the discount:
- Discount = Bank Discount Yield × Par × (Days / 360)
- Discount = 0.025 × $10,000 × (182 / 360)
- Discount = $250 × 0.5056
- Discount ≈ $126.40

Purchase price: $10,000 − $126.40 = $9,873.60

Now calculate bond-equivalent yield:
- BEY = ($126.40 / $9,873.60) × (365 / 182)
- BEY = 0.01279 × 2.0055
- BEY ≈ 2.57%

Again, the BEY (2.57%) exceeds the bank discount yield (2.50%) by a modest amount.

## Why this matters for portfolio management

If you're comparing a T-bill against a bond that quotes in bond-equivalent terms, you must convert the T-bill to BEY first. Otherwise, you'd be comparing apples to oranges—one understated, one not.

Similarly, if you're building a yield curve or comparing returns across Treasury maturities, mixing bank discount yields (T-bills) with coupon-bearing Treasury yields (notes and bonds) requires normalizing them. Many portfolio managers and risk systems do this automatically, but the underlying math relies on the bank discount formula.

## The modern shift toward 365-day quoting

Some market participants and systems have begun quoting T-bills using 365-day annualization, especially for financial reporting and derivatives pricing. However, the official "street" convention remains 360 days, and Federal Reserve publications still use bank discount yield.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury-Bill](/treasury-bill/) — fundamentals of short-term government debt
- [Yield-to-Maturity](/yield-to-maturity/) — how longer-term bonds are quoted (different formula, same concept)
- Zero-Coupon — T-bills are the classic zero-coupon instrument
- [Discount-Rate](/discount-rate/) — the principle behind pricing any future cash flow
- [Current-Yield](/current-yield/) — comparison to coupon-bearing bond yields

### Wider context

- [Treasury-Note](/treasury-note/) — intermediate Treasuries with coupon payments
- [Treasury-Bond](/treasury-bond/) — long-term Treasuries with coupon payments
- [Primary-Market](/primary-market/) — where T-bills are auctioned initially
- [Secondary-Market](/secondary-market/) — where T-bills trade after issuance

</div>

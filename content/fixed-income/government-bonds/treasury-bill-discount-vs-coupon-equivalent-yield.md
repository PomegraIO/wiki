---
title: "Treasury Bill Discount Yield vs Coupon-Equivalent Yield"
description: "Why T-bill quoted discount yields understate true returns. How to convert to coupon-equivalent yield for fair comparison with other bonds."
keywords:
  - treasury bill discount yield
  - coupon equivalent yield
  - tbill effective annual yield
  - treasury bill return calculation
  - bond equivalent yield
---

*The quoted **discount yield** on a [Treasury bill](/treasury-bill-discount-vs-coupon-equivalent-yield/) is lower than its actual annualized return because it uses a 360-day year, ignores [compounding](/compound-interest/), and calculates return as a fraction of face value rather than investment outlay. Converting to a **coupon-equivalent yield** reveals the true apples-to-apples comparison with other short-term fixed-income instruments.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">T-Bill Yields Explained — two measurement methods</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income securities." />

<div class="wiki-infobox-caption">Why the discount yield quoted by dealers understates what investors actually earn.</div>

|   |   |
|---|---|
| **Discount yield** | Annual return as % of face value; uses 360-day year. Often quoted by dealers. |
| **Coupon-equivalent yield** | True annualized return on your actual cash investment; uses 365-day year. |
| **The gap** | Coupon-equivalent is typically 0.3 % to 1.5 % higher, depending on maturity. |
| **Why it matters** | For [cash-flow](/cash-flow-statement/) planning and comparing T-bills to other short-term bonds. |
| **Time horizon** | Most relevant for [Treasury bills](/treasury-bill-discount-vs-coupon-equivalent-yield/) (1 day to 52 weeks); longer-dated [Treasury bonds](/treasury-bond/) use simple coupon yields. |

</aside>

## The origin of discount yield

[Treasury bills](/treasury-bill-discount-vs-coupon-equivalent-yield/) are sold at a discount to [par value](/par-value/). If you buy a $10,000 face value T-bill maturing in 90 days and pay $9,750, you earn $250 at maturity. Dealers quote this return using a formula:

**Discount Yield = (Discount / Face Value) × (360 / Days to Maturity)**

In the example: Discount Yield = ($250 / $10,000) × (360 / 90) = 10%.

This method, called the **bank discount basis**, has been the market standard since the 1920s. It is efficient for quick mental math, but it has three quirks that understate true economic return.

## Three reasons discount yield understates actual return

**1. Use of 360-day year instead of 365**

The formula divides by 360, not 365. This convention traces back to manual calculation when 360 was convenient (12 months × 30 days). It inflates the quoted yield by about 1.4 % (365 ÷ 360 = 1.014).

**2. Return is calculated on face value, not actual cash invested**

You invest $9,750 today and receive $10,000 tomorrow. Your true [return](/return-on-assets/) is $250 ÷ $9,750, not $250 ÷ $10,000. Dividing by face value alone understates your yield, especially for longer-dated bills.

**3. No mention of compounding**

The discount yield is a simple, non-compounded rate. If you roll a 90-day bill over four times per year, your [compound interest](/compound-interest/) is not captured in the quoted number.

## The coupon-equivalent yield conversion

To convert discount yield to a true apples-to-apples return, use the **coupon-equivalent yield** (also called bond-equivalent yield or effective annual yield):

**Coupon-Equivalent Yield = (Discount / Purchase Price) × (365 / Days to Maturity)**

Returning to the example: 
- Purchase price = $9,750
- Discount = $250
- Days to maturity = 90

Coupon-Equivalent Yield = ($250 / $9,750) × (365 / 90) = 10.59%

Compare this to the quoted discount yield of 10%. The coupon-equivalent yield is 59 basis points higher, a material difference for a cash manager deciding between a T-bill and a [money-market fund](/money-market-fund/) or a short-term [corporate bond](/corporate-bond/).

## Worked example: 180-day bill

Suppose a 180-day T-bill is quoted at a discount yield of 5.2%.

**Step 1: Calculate the dollar discount.**
- Discount = Face Value × Discount Yield × (Days / 360)
- Discount = $10,000 × 0.052 × (180 / 360) = $260

**Step 2: Calculate purchase price.**
- Purchase Price = $10,000 − $260 = $9,740

**Step 3: Calculate coupon-equivalent yield.**
- Coupon-Equivalent = ($260 / $9,740) × (365 / 180)
- Coupon-Equivalent = 0.0267 × 2.028 = 5.41%

The investor earns 5.41%, not 5.2%.

## When the gap matters most

For very short-dated bills (e.g., overnight or one-week), the gap is small—often under 10 basis points—because the proportion of the year is tiny. For a full-year bill (52 weeks), the gap can exceed 100 basis points.

| Days | Discount Yield | Coupon-Equivalent | Gap (bps) |
|---|---|---|---|
| 7 | 5.0% | 5.04% | 4 |
| 30 | 5.0% | 5.07% | 7 |
| 90 | 5.0% | 5.13% | 13 |
| 180 | 5.0% | 5.26% | 26 |
| 365 | 5.0% | 5.57% | 57 |

## Practical use: comparing investment options

A treasurer evaluating where to park $10 million for 180 days might compare:

- A T-bill quoted at 5.2% discount yield → 5.41% coupon-equivalent
- A [Treasury bond](/treasury-bond/) quoted as 5.35% [coupon rate](/coupon-rate/)
- A [high-yield bond](/high-yield-bond/) quoted at 6.8% coupon rate

Using coupon-equivalent, the T-bill appears more competitive versus nominal coupon rates on other securities, and [risk-adjusted](/risk-weighted-assets/) comparison becomes clearer.

## Modern context: dealer conventions persist

Electronic platforms (Bloomberg, MarketAxess) still quote T-bills using discount yield because it is the convention accepted by the Federal Reserve and [FINRA](/finra/). Understanding the conversion is essential for anyone trading bills, doing [cash-flow](/cash-flow-statement/) forecasts, or comparing short-term financing costs across instruments.

Some money managers and central banks have advocated for quoting bills on a coupon-equivalent basis to reduce confusion, but the market has not shifted. The discount yield remains the lingua franca.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill-discount-vs-coupon-equivalent-yield/) — short-term government debt
- [Coupon Payment](/coupon-payment/) — periodic interest on bonds
- [Coupon Rate](/coupon-rate/) — stated annual interest rate
- [Par Value](/par-value/) — face value of a bond at maturity
- [Current Yield](/current-yield/) — annual income as a percent of price
- [Yield to Maturity](/yield-to-maturity/) — total return if held to maturity
- [Compound Interest](/compound-interest/) — growth of returns over time

### Wider context

- [Bond](/bond/) — fixed-income instruments
- [Treasury Bond](/treasury-bond/) — longer-dated government debt
- [Money Market Fund](/money-market-fund/) — short-term cash instruments
- [Interest Rate](/interest-rate/) — the price of borrowing

</div>

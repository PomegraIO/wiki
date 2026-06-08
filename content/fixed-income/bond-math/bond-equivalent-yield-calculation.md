---
title: "Bond Equivalent Yield Calculation"
description: "Learn how to calculate bond equivalent yield from discount or money-market yields, with step-by-step formula and worked examples."
keywords:
  - bond equivalent yield
  - how to calculate bond equivalent yield
  - discount yield conversion
  - money market yield
  - bond annualization
  - semi-annual compounding
image: "/svg/fixed-income.svg"
---

*A **bond equivalent yield** (BEY) converts a discount yield or money-market return into a semi-annual compounded annual rate, the standard format for quoting fixed-income securities. The calculation adjusts for the fact that bond prices and yields use a 180-day year rather than 365 days, making comparison across Treasury bills, commercial paper, and longer-term bonds straightforward.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Equivalent Yield — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The bridge between money-market and traditional bond yield conventions.</div>

|   |   |
|---|---|
| **Core formula** | BEY = (2 × Discount Yield) × (365 / Days to Maturity) |
| **Why 2?** | Accounts for semi-annual compounding on bonds |
| **Why 365?** | Bonds use a 365-day year; bills use 360 |
| **When to use** | Converting Treasury bill or commercial paper yields to standard bond terms |
| **Related metrics** | [Current yield](/current-yield/), [Yield to maturity](/yield-to-maturity/), [Coupon rate](/coupon-rate/) |

</aside>

## The three yield conventions and why they diverge

The U.S. fixed-income market uses three overlapping yield conventions, each optimized for a different instrument class. Short-term money-market securities—[Treasury bills](/treasury-bill/), [commercial paper](/commercial-paper/), and [repurchase agreements](/repurchase-agreement/)—quote in discount yield (also called **bank discount yield**). Corporate and government bonds quote in semi-annual bond equivalent yield. Money-market funds sometimes report a 7-day yield to help investors compare short-duration holdings.

The issue is simple: the methods compound differently and use different day counts. A Treasury bill maturing in 180 days might quote at a 4.50% discount yield. A corporate bond with the same risk and maturity might show 4.65% yield to maturity. These are not errors—they are the same economics reported in different dialects. To compare apples to apples, you convert all quotes to a common language, and bond equivalent yield is the lingua franca for U.S. fixed income.

## The discount yield formula and its mechanics

**Discount yield** (or bank discount yield) applies only to instruments priced at a discount to par, with no coupon:

> Discount Yield = (Par − Price) / Par × (360 / Days to Maturity)

A Treasury bill with a par value of $10,000, trading at $9,800, and 180 days to maturity would have:

Discount Yield = ($10,000 − $9,800) / $10,000 × (360 / 180) = 0.02 × 2 = 4.00%

Note the 360-day year—this is a money-market convention. The formula also annualizes based only on the discount, not on the actual amount invested; this makes discount yields appear lower than the [actual return](/return-on-invested-capital/) to an investor who buys the bill at $9,800.

## Converting discount yield to bond equivalent yield

To convert discount yield to bond equivalent yield, the formula is:

**BEY = (2 × Discount Yield) × (365 / 360)**

Using the Treasury bill example above:

BEY = (2 × 0.04) × (365 / 360) = 0.08 × 1.01389 = 8.11%

The factor of 2 appears because bond yields assume semi-annual compounding (hence two periods per year). The ratio 365 / 360 adjusts for the day-count mismatch. The result, 8.11%, is what you would see quoted on a bond trading screen for a comparable instrument.

This seems like a strange jump from 4.00% to 8.11%—and it is, until you understand the definitions. The discount yield was calculated on par ($10,000), while the actual cash you put up was $9,800. The bill investor earns $200 on $9,800, a true return of ($200 / $9,800) = 2.04% for 180 days, or about 4.08% annualized. The BEY of 8.11% assumes reinvestment of that 4.08% rate for the second half of the year at the same semi-annual rate, which gives (1.0408)² − 1 ≈ 0.0833 or 8.33%—close to 8.11% when the mechanics are traced through carefully.

## Money-market yield to bond equivalent yield

Some instruments, especially money-market funds, quote in **money-market yield** (MMY), also called **simple interest yield**:

MMY = (Par − Price) / Price × (360 / Days to Maturity)

The key difference is the denominator: money-market yield divides by the actual price (the cash invested), not par. For the same $9,800 bill:

MMY = ($10,000 − $9,800) / $9,800 × (360 / 180) = 0.020408 × 2 = 4.082%

To convert money-market yield to bond equivalent yield:

**BEY = (2 × MMY) × (365 / 360)**

BEY = (2 × 0.04082) × (365 / 360) = 0.08164 × 1.01389 = 8.27%

The slight difference from the previous example reflects the distinction between discount yield and money-market yield. Money-market yield is closer to the actual rate of return on the cash invested, so the BEY it produces is also more aligned with that cash-on-cash economics.

## Why the adjustment matters in practice

The conversion factors—2 for semi-annual compounding, and 365 / 360 for day-count convention—seem like arcane details. In practice, they matter for portfolio managers who need to compare short-term Treasury bills against intermediate-term bonds or floating-rate notes to decide where to allocate capital.

Consider a fund manager holding a mix of 90-day bills and 2-year [Treasury notes](/treasury-note/). The bills might quote at 4.00% discount yield, while the notes quote at 4.45% yield to maturity. Without converting both to a common basis, you cannot judge whether the extra 45 basis points (or less, once adjusted) is worth the longer duration risk. Converting the bill to BEY shows that the true annualized rate is closer to 4.08% or 4.09%, and the comparison becomes clearer: you would earn roughly 36 basis points more per year on the notes, in exchange for carrying the price risk of an extra 1.9 years of duration.

## Practical worked example with different maturities

Suppose you encounter three short-term instruments:
- Treasury bill (91 days): discount yield 3.85%
- Commercial paper (182 days): discount yield 4.10%
- Floating-rate note (180 days): money-market yield 4.05%

Convert each to BEY:

**Bill:** BEY = (2 × 0.0385) × (365 / 360) = 0.077 × 1.01389 = 0.0781 or **7.81%**

**Paper:** BEY = (2 × 0.041) × (365 / 360) = 0.082 × 1.01389 = 0.0831 or **8.31%**

**FRN:** BEY = (2 × 0.0405) × (365 / 360) = 0.081 × 1.01389 = 0.0821 or **8.21%**

Now all three are on a semi-annual bond-equivalent basis. The commercial paper offers the highest yield, followed by the floating-rate note, then the bill. This ranking would be misleading if you compared them in their original conventions (the bill at 3.85% would look artificially cheap).

## When you don't need to convert

If you are comparing two instruments that both quote in the same convention—for example, two Treasury bills quoted in discount yield, or two corporate bonds quoted in semi-annual yield to maturity—you do not need to convert. The relative comparison is unchanged by a uniform scaling. Conversion becomes essential only when you are mixing instruments from different markets or conventions, or when you need to judge an absolute return target against a policy benchmark expressed in yield-to-maturity terms.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield to maturity](/yield-to-maturity/) — the dominant bond yield metric, incorporating all coupons and the discount or premium
- [Treasury bill](/treasury-bill/) — the simplest discount-yield instrument, essential for understanding the conversion
- [Coupon rate](/coupon-rate/) — the stated annual rate on bonds, which differs from yield
- [Current yield](/current-yield/) — a simpler metric that divides annual coupon by current price
- [Duration](/duration/) — how interest-rate risk scales with maturity, often paired with yield analysis
- [Basis](/basis/) — the spread between related fixed-income instruments, expressed in yield points
- [Bid-ask spread](/bid-ask-spread/) — why the buy and sell quotes differ, relevant to transaction costs on bills and bonds

### Wider context

- [Bond](/bond/) — the foundational fixed-income instrument
- [Fixed-rate mortgage](/fixed-rate-mortgage-personal/) — another context where semi-annual compounding appears
- [Interest rate](/interest-rate/) — the fundamental driver of all yield calculations
- [Compound interest](/compound-interest/) — the mathematical engine behind the 2× factor and semi-annual convention
- [Secondary market](/secondary-market/) — where most bill and bond trading happens and yields are quoted

</div>

---
title: "Money Market Yield"
description: "A 360-day annual rate used to express short-term debt returns on a standardized, comparable basis."
keywords:
  - money market yield
  - mmy
  - bond equivalent yield
  - 360-day convention
  - treasury bill
  - commercial paper
image: /svg/fixed-income.svg
---

*The **money market yield** (or **discount yield**) expresses the return on short-term money market instruments—treasury bills, commercial paper, bankers' acceptances—as an add-on annual rate based on a 360-day year. It converts the raw purchase discount into a standardized format that traders and investors can compare across instruments and maturities.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Money Market Yield — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income products and bonds." />

<div class="wiki-infobox-caption">A standardized annual rate for short-term instruments using a 360-day convention.</div>

|   |   |
|---|---|
| **What it is** | Annual percentage return on money market instruments, expressed on a 360-day add-on basis |
| **Also called** | Discount yield, bank discount yield, treasury bill rate |
| **Convention** | 360 days in the annualization period |
| **Formula** | MMY = (Discount / Face Value) × (360 / Days to Maturity) |
| **Instruments** | [Treasury bills](/treasury-bill/), [commercial paper](/stock-market/), bankers' acceptances, CDs |
| **Advantage** | Quick, uniform comparison across short-term debt |
| **Drawback** | Understates true return; doesn't reflect compounding |

</aside>

## Why the money market needs a standard

Short-term debt instruments trade at a discount to face value—you pay less today, collect full face value at maturity. A [treasury bill](/treasury-bill/) might sell at 98.5 per 100 of face, a piece of [commercial paper](/stock-market/) at 97.2. Comparing these instruments requires a common yardstick.

The **money market yield** emerged to fill that gap. Because money market instruments mature in days or weeks, traders needed a quick, standardized way to quote returns that would allow them to compare a 30-day T-bill to a 90-day certificate of deposit without constantly recalculating. The 360-day convention—rooted in banking history, when calculation by hand made round numbers valuable—became the market standard.

## The mechanics: from discount to annual rate

The formula is straightforward:

**Money Market Yield = (Discount / Face Value) × (360 / Days to Maturity)**

Suppose you buy a treasury bill with a 180-day maturity for 99 (per 100 of face value). The discount is 1 point, or 1% of the 100 face value. Scaling to a 360-day year:

**MMY = (1 / 100) × (360 / 180) = 0.01 × 2 = 2%**

The annualized money market yield is 2%. If you held this position for a full 360 days (reinvesting at the same rate), you'd earn that 2%.

In practice, the formula is sometimes written with the actual dollar amounts. If a 91-day bill costs 98.75 and matures at 100, the discount is 1.25; multiply by (360/91) to annualize, then divide by the purchase price (not face) to express yield.

## Why 360 days?

Historical convention. Medieval and Renaissance bankers used 360-day years for simplicity—divisible evenly by 12 months, 4 quarters, and many other calendar units. When automated calculation arrived, the 360-day convention stuck in money markets rather than shift to the calendar year. It persists today, even though [interest-rate](/interest-rate/) futures, bonds, and many OTC instruments now use actual day-count conventions (Actual/360, Actual/365, 30/360).

For practitioners, this matters: a money market yield of 2% is not equivalent to a 2% annual rate in calendar time if the instrument doesn't mature exactly at year-end. The discrepancy widens with longer-dated instruments, though most money market paper trades within 180 days.

## Money market yield versus bond equivalent yield

Practitioners sometimes distinguish between **money market yield** (360-day) and **bond equivalent yield** (365-day), also called the **CD equivalent yield**. The conversion is proportional:

**Bond Equivalent Yield = MMY × (365 / 360)**

If the money market yield is 2%, the bond equivalent yield is 2.028%. This adjustment allows fair comparison between money market instruments and longer-term bonds that use a 365-day convention.

Treasury bill auction results, published by the Federal Reserve and the U.S. Treasury, are routinely quoted in money market yield format. Financial data terminals (Bloomberg, Reuters) toggle between the two conventions automatically, but understanding which rate you're reading matters when pricing short-term portfolio positions.

## The limitation: what MMY obscures

Money market yield ignores [compounding](/compound-interest/). If you earn 2% MMY and reinvest the proceeds at the same rate, you don't actually earn 2% over the calendar year unless the instrument's maturity aligns perfectly with 360 days. For very short instruments (7-day repos, overnight paper), compounding's effect is negligible; for 180-day instruments, it becomes meaningful.

Similarly, money market yield assumes you hold the instrument to maturity. If you sell early in the secondary market, your actual return depends on price at exit, not the rate at which you purchased. In volatile [interest-rate](/interest-rate/) environments, this distinction is critical for portfolio performance.

## When you'll see it

Money market yields appear in:

- **Treasury bill auctions and secondary trades** — quoted and settled in money market yield
- **Commercial paper issuance** — short-term corporate debt priced in this convention
- **Bankers' acceptances** — import/export financing instruments quoted in MMY
- **Money market mutual funds** — daily yields often reported in this format
- **Repurchase agreements** — short-term collateral loans quoted in annualized discount yield

For investors building a short-term cash allocation, comparing a 3-month Treasury to 2-month commercial paper requires converting both to a shared annual basis—money market yield does that mechanical work.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill/) — the canonical money market instrument, priced and traded in money market yield
- [Discount Rate](/discount-rate/) — the broader concept of pricing instruments below face value
- [Bond Equivalent Yield](/fixed-income/bond-math/nominal-spread/) — the 365-day convention for bonds and CDs
- [Current Yield](/current-yield/) — annual income as a percentage of price, applied to longer-dated instruments
- [Yield-to-Maturity](/fixed-income/bond-math/yield-spread-measures/) — the true internal rate of return, accounting for reinvestment

### Wider context

- [Interest Rate](/interest-rate/) — the foundation of all discount and yield calculations
- [Central Bank](/central-bank/) — the Federal Reserve sets short-term rates that influence MMY across the market
- [Federal Reserve](/federal-reserve/) — publishes Treasury auction results in money market yield format
- [Monetary Policy](/monetary-policy/) — short-term rates are the first transmission mechanism of monetary transmission
- [Credit Risk](/credit-risk/) — commercial paper carries credit risk that Treasury does not, affecting its money market yield

</div>

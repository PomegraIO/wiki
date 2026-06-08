---
title: "Accrued Interest on a Bond: How It Is Calculated"
description: "Accrued interest is the interest owed by a bond seller to the buyer for the time between the last coupon payment and the sale date, calculated using a day-count convention."
keywords:
  - accrued interest bond calculation
  - how is accrued interest calculated
  - bond accrued interest formula
  - bond trading between coupon dates
image: /svg/fixed-income.svg
---

*When a bond is sold between [coupon payment](/coupon-payment/) dates, the buyer must compensate the seller for the interest that has accumulated since the last payment. **Accrued interest** is calculated using a day-count formula—typically counting actual days (or a 30/360 standard) and the coupon rate—ensuring the seller is not penalized for holding the bond partway through a coupon period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Accrued Interest on Bonds — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">A fairness mechanism: the buyer reimburses the seller for earned-but-unpaid interest.</div>

|   |   |
|---|---|
| **Definition** | Interest earned on a bond since the last coupon date but not yet paid |
| **Who pays** | Buyer pays accrued interest to the seller |
| **When calculated** | On any sale between coupon payment dates |
| **Day-count convention** | Actual/Actual, 30/360, Actual/360, or 30E/360 (varies by bond type) |
| **Formula** | (Coupon rate × Days since last coupon / Days in coupon period) × Par value |
| **Market convention** | Most US corporate and Treasury bonds quote "clean price" (excluding accrued interest) |
| **Settlement** | Accrued interest is added at settlement; total paid is "dirty price" |

</aside>

## Why Accrued Interest Exists

Imagine a bond with a 4% annual coupon, paying $40 per year in two semi-annual installments of $20 each on March 31 and September 30. The coupon dates are fixed; all bondholders on record on those dates receive the full $20 payment.

If an investor sells the bond on August 15—after the March 31 coupon but before the September 30 coupon—the seller has earned interest for 137 days (April 1 through August 15) but will not receive the next coupon payment (which goes to the new owner). Without a mechanism to compensate the seller, the buyer would pocket a windfall: they buy on August 15 and receive the full September 30 coupon ($20) without having held the bond since March 31.

Accrued interest solves this unfairness. The buyer pays the seller the interest earned from March 31 to August 15, then both parties are made whole when the September 30 coupon is paid entirely to the buyer (new owner of record).

## The Day-Count Convention

Bonds use different day-count conventions depending on their type. The convention specifies how many days are in the accrual period (numerator) and how many days are in the full coupon period (denominator).

**Actual/Actual (most US corporate and Treasury bonds):**
- Count the actual calendar days in the accrual period.
- Count the actual calendar days in the full coupon period.
- Example: March 31 to August 15 = 137 days. March 31 to September 30 = 184 days.

**30/360 (some corporate bonds and municipal bonds):**
- Assume every month has 30 days and every year has 360 days.
- Simplifies calculation but slightly distorts reality.
- Example: March 31 to August 15 = (4 months × 30 days) + 15 days = 135 days. March 31 to September 30 = 6 months × 30 days = 180 days.

**Actual/360 and 30E/360** exist for certain instruments but are less common in the US market.

Most investors do not memorize these; they rely on brokers, custodians, and pricing services to compute accrued interest correctly.

## The Step-by-Step Calculation

**Given:**
- Bond: $1,000 par, 4% annual coupon (semi-annual payments of 2%)
- Last coupon date: March 31
- Sale date: August 15
- Day-count convention: Actual/Actual

**Step 1:** Count days from last coupon date to sale date.
- April: 30 days
- May: 31 days
- June: 30 days
- July: 31 days
- August 1–15: 15 days
- Total: 30 + 31 + 30 + 31 + 15 = 137 days

**Step 2:** Count days from last coupon date to next coupon date (full period).
- March 31 to September 30 = 184 days (same six-month period)

**Step 3:** Calculate accrued interest.
- Semi-annual coupon payment: 4% ÷ 2 = 2% of par
- Dollar amount of coupon: 0.02 × $1,000 = $20
- Accrued interest: $20 × (137 ÷ 184) = $20 × 0.7446 = $14.89

**Step 4:** Transaction price.
- Assume the bond is trading at a "clean price" of $980 (below par due to higher market yields).
- "Dirty price" (what the buyer actually pays) = clean price + accrued interest
- Dirty price = $980 + $14.89 = $994.89
- The buyer pays $994.89; the seller receives $994.89 total.

The $14.89 accrued interest goes entirely to the seller as compensation for holding the bond. On September 30, the buyer (new owner of record) receives the full $20 coupon.

## Clean Price vs. Dirty Price

The bond market quotes and displays **clean price**—the price excluding accrued interest. This convention makes bond prices easier to compare and track over time. If accrued interest were included in every quote, the price would appear to jump up on coupon dates and reset to a lower number immediately after; traders would be confused.

**Clean price:** What you see in a Bloomberg terminal, a broker's system, or financial news. This is what is used in bond indices and fund NAV calculations.

**Dirty price** (or "invoice price"): The amount the buyer actually wires at settlement. Dirty price = clean price + accrued interest. This is what appears on the settlement statement.

For example:
- Clean price: $980.00
- Accrued interest: $14.89
- Dirty price: $994.89
- The buyer's settlement payment: $994.89 per $1,000 bond

## A Worked Example With Different Day Counts

**Bond:** $1,000 par, 5% annual coupon (2.5% semi-annual, $25 per payment)
**Last coupon:** January 15
**Sale date:** March 20
**Coupon period:** January 15 to July 15 (both convention pairs below use the same coupon period, 181 days)

**Using Actual/Actual:**
- Days from January 15 to March 20:
  - January 15–31: 16 days
  - February 1–28: 28 days
  - March 1–20: 20 days
  - Total: 64 days
- Accrued interest: $25 × (64 ÷ 181) = $25 × 0.3536 = $8.84

**Using 30/360:**
- Days from January 15 to March 20:
  - January 15–31: 15 days (30 − 15)
  - February: 30 days
  - March 1–20: 20 days
  - Total: 65 days
- Accrued interest: $25 × (65 ÷ 180) = $25 × 0.3611 = $9.03

The difference is small ($0.19) but accumulates across millions in bond trading volume.

## Corporate vs. Treasury vs. Municipal Bonds

**US Treasury bonds** use Actual/Actual; accrued interest accrues continuously.

**US corporate bonds** typically use 30/360; the simplified day count is an industry standard.

**Municipal bonds** vary but often use 30/360.

**International bonds** (Eurobonds, etc.) use their own conventions. A trader buying non-US bonds must know the local convention.

## When Accrued Interest Matters Most

Accrued interest is a small percentage of the bond price in normal circumstances (usually 0.5–2% of par), but it matters for:

1. **Tax accounting:** The IRS distinguishes between accrued interest (taxable as ordinary income) and capital gains/losses on the bond price itself. Investors filing [Schedule D](/schedule-d/) must correctly identify which portion of the sale price is accrued interest.

2. **Fund accounting:** A [bond fund](/bond-etf/) must track accrued interest on every holding to correctly calculate its [net asset value](/net-asset-value/) (NAV). Funds often show "accrued interest receivable" as a separate line item on financial statements.

3. **Large transactions:** Institutional traders moving millions of dollars in bonds can have thousands of dollars in accrued interest. A single basis point error in day counting can cost money.

4. **Illiquid bonds:** In thinly traded bonds or defaulted bonds, where quotes are stale or absent, accrued interest can be a point of negotiation between buyer and seller.

## Accrued Interest and Zero-Coupon Bonds

[Zero-coupon bonds](/zero-coupon-bond/) pay no periodic coupons; they are sold at a discount and redeemed at par at maturity. They still accrue interest (the market value appreciates over time), but there is no "accrued interest" payment mechanism between buyer and seller because there are no coupon dates. A zero-coupon bond transaction is simply buyer paying market price; accrued interest is baked into the pricing formula.

## See also

<div class="wiki-seealso">

### Closely related

- [Why Bond Prices and Yields Move in Opposite Directions](/bond-price-yield-inverse-relationship/) — how accrued interest fits into bond pricing and settlement
- [Coupon Payment](/coupon-payment/) — the scheduled interest payments a bond makes
- [Bond](/bond/) — the foundational fixed-income instrument
- [Yield-to-Maturity](/yield-to-maturity/) — accrued interest affects the calculation of yield when buying between coupon dates
- [Duration](/duration/) — how a bond's price sensitivity depends on maturity and coupon
- [Schedule D](/schedule-d/) — where investors report accrued interest and gains/losses for taxes

### Wider context

- [Fixed-Rate Mortgage](/fixed-rate-mortgage-personal/) — mortgage interest accrues similarly between payment dates
- [Compound Interest](/compound-interest/) — the broader concept of interest accumulation
- Settlement — the mechanics of completing a securities transaction

</div>

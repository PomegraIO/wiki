---
title: "How Accrued Interest Works at Corporate Bond Settlement"
description: "Understand how accrued interest is calculated at bond settlement using day-count conventions, and why invoice price differs from purchase price."
keywords:
  - accrued interest bond settlement
  - how accrued interest is calculated at bond settlement
  - day-count convention bonds
  - bond invoice price
  - corporate bond settlement mechanics
---

*When you buy a **corporate bond** between coupon dates, you must pay the seller for the interest that has accrued since the last coupon payment. This accrued interest is calculated using a specific day-count method — the exact formula varies by market convention — and added to the clean price you see quoted to arrive at the settlement invoice.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Accrued Interest at Settlement — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Buyers reimburse sellers for the coupon earned between payment dates.</div>

|   |   |
|---|---|
| **Clean price** | Price quoted; excludes accrued interest |
| **Dirty (invoice) price** | Clean price + accrued interest |
| **Day-count method** | Determines accrued interest; varies by market |
| **Common convention** | Actual/360 (corporate), Actual/365 (government) |
| **Settlement date** | T+1 to T+2, depending on market |
| **Why it matters** | Accrued interest can add 0.5–2% to your cash outlay |

</aside>

## Why bonds include accrued interest

A [corporate bond](/corporate-bond/) typically pays [coupon](/coupon-payment/) twice per year — say, 15 March and 15 September. If you buy the bond on 1 July, it has been 107 days since the last coupon. The seller held the bond through those 107 days and earned the interest for that period, even though the next coupon check won't arrive until 15 September. Rather than wait for the next coupon and then make a separate payment, the buyer simply reimburses the seller at settlement for the interest already earned.

This is both practical and fair: the seller gets paid for the time they held the bond, and the buyer doesn't overpay at the next coupon date. But the calculation is not as simple as interest ÷ 2. It depends on which day-count convention governs the bond.

## The day-count convention and accrued interest formula

The **accrued interest** is computed as:

**Accrued Interest = (Days Elapsed ÷ Days in Period) × (Annual Coupon Payment)**

The numerator — days elapsed — is almost always the actual number of calendar days from the last coupon date to the settlement date (inclusive or exclusive, depending on convention). The denominator varies:

- **Actual/360**: Days are counted exactly; the year is assumed to be 360 days. Common in corporate bonds and most [bond](/bond/) markets.
- **Actual/365**: Days are counted exactly; the year is assumed to be 365 days. Typical for government bonds.
- **30/360**: Each month is assumed to have 30 days; the year is 360. Used in some corporate and agency markets.

Most corporate bonds trade on **Actual/360**. If a bond pays $50 twice per year (a $100 annual coupon on a $1,000 bond), and 107 days have elapsed out of 181 days in the coupon period, the accrued interest is:

> (107 ÷ 181) × $50 = 0.5912 × $50 = $29.56

The buyer must add this $29.56 to the clean price (the quoted market price) to arrive at the **dirty price** or **invoice price** paid at settlement.

## Clean price vs. invoice price

Bond traders and market data providers quote the **clean price** — the price stripped of accrued interest. This convention lets prices move smoothly over time without a sawtooth drop every coupon date. A bond trading at 101.50 (101.5% of par) is the clean price.

But you do not pay 101.50. You pay the **dirty price** (or **invoice price**):

**Dirty Price = Clean Price + Accrued Interest**

If the clean price is 101.50 and accrued interest is 1.48, the dirty price is 103.98. On a $1,000 bond, that is $1,039.80. The accrued interest portion ($14.80) is typically taxable income to the seller and tax-deductible by the buyer in the settlement year, though tax treatment varies by jurisdiction and bond type.

## How settlement date affects the calculation

The accrued interest is calculated as of the **settlement date**, not the trade date. In most bond markets, settlement occurs T+1 (one business day after the trade). Some corporate bonds settle T+2. If you buy a bond on Friday for settlement on Monday, the accrued interest is calculated through Monday, not Friday. The seller receives the accrued interest as of the day the bond legally transfers to you.

This distinction matters when a coupon date falls between trade and settlement. If you trade on 14 September and settle on 15 September, and the coupon pays on 15 September, the accrued interest resets to zero at settlement — you do not pay accrued interest, and the seller captures the full coupon on the 15th.

## Negative accrued interest (rare)

In unusual cases, typically shortly after a coupon payment, accrued interest can be negative (expressed as a credit to the buyer). This happens when a bond is trading "ex-coupon" — meaning the buyer is not entitled to the next coupon; the seller is. The dirty price is then lower than the clean price. This is common for [bond](/bond/) trading just after a coupon date or for bonds in default, but rare in normal markets.

## The mechanics in practice

When you receive a settlement confirmation from a broker, it will show:

- **Clean price** (the negotiated rate)
- **Accrued interest** (calculated by the clearinghouse or custodian)
- **Invoice/dirty price** (clean + accrued)
- **Settlement amount** (invoice price × par amount)
- **Day count and convention** (usually in small print)

If the day-count calculation seems high, check the convention listed on the bond's term sheet or prospectus. A corporate bond using Actual/360 will accrue interest faster (360-day year is shorter) than one using Actual/365, all else equal.

Professional traders use settlement systems and market data terminals (Bloomberg, TRACE feeds) that compute accrued interest automatically. Retail buyers can calculate it by hand using the coupon schedule and the applicable day-count method, or ask their broker for the detail.

## See also

<div class="wiki-seealso">

### Closely related

- [Coupon Payment](/coupon-payment/) — the periodic interest payment made to bond holders
- [Bond](/bond/) — the fundamental debt security; settlement mechanics apply across all types
- [Corporate Bond](/corporate-bond/) — company debt; Actual/360 day-count is standard
- [Bid-Ask Spread](/bid-ask-spread/) — accrued interest can be part of the true cost of a trade
- [Basis](/basis/) — the cost basis of a bond includes accrued interest at purchase

### Wider context

- [Interest Rate](/interest-rate/) — the coupon is set as a rate on the bond's par value
- [Secondary Market](/secondary-market/) — bonds trade between investors; accrued interest compensates for inter-coupon ownership
- Settlement — the mechanics of transferring ownership and payment
- [Yield to Maturity](/yield-to-maturity/) — accrued interest affects the true cost and yield of a bond purchase

</div>

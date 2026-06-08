---
title: "How Bond Prices Are Calculated Between Coupon Dates"
description: "Bond prices between coupon payment dates are calculated by adding accrued interest to the clean price, producing the full dirty price paid at settlement."
keywords:
  - bond price between coupon dates
  - accrued interest bonds
  - clean price dirty price
  - bond settlement calculation
  - accrued coupon bonds
  - ex-coupon date
  - dirty price formula
image: "/svg/fixed-income.svg"
---

*When you buy a **bond** between coupon dates, the seller is entitled to the portion of the next coupon earned up to the settlement date. The full amount you pay is the clean price (what you see quoted) plus accrued interest—together called the dirty price. This mechanism ensures the seller is fairly compensated for the time value of money between coupon payments.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Pricing Between Coupons — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">You pay clean price plus accrued interest; the seller keeps the accrued portion of the next coupon.</div>

|   |   |
|---|---|
| **Clean price** | Quoted market price excluding accrued interest |
| **Accrued interest** | The coupon earned by the seller from last coupon date to settlement |
| **Dirty price** | Clean price + accrued interest = amount paid at settlement |
| **Calculation basis** | Depends on day-count convention (Actual/360, 30/360, Actual/Actual) |
| **Timing** | Resets to zero on ex-coupon date; rises linearly until next coupon |
| **Key formula** | Accrued Interest = (Annual Coupon ÷ Coupon Frequency) × (Days Held ÷ Days in Period) |

</aside>

## Why Accrued Interest Exists

Bond [coupon payments](/coupon-payment/) are typically made twice yearly. If you sell a bond on, say, the 45th day after a coupon payment, you have earned 45 days' worth of the next coupon—but that coupon won't be paid for another 135 days. Without accrued interest, the buyer would receive the full next coupon while the seller, who held the bond for 45 days of its accrual period, gets nothing. The dirty price mechanism corrects this.

The buyer settles the trade by paying the seller:
- The clean price (the market value of the bond going forward)
- Plus accrued interest (compensation for the seller's holding period)

The buyer then receives the full coupon at the coupon date, recouping the accrued interest and starting the next accrual period fresh.

## Clean Price vs. Dirty Price

**Clean price** is the quotation you see in a market data feed or bond trading platform. It is the bond's value stripped of accrued interest, expressed as a percentage of par. A bond quoted at 102.50 means 102.50% of $1,000 par, or $1,025.

**Dirty price** is what you actually pay at settlement. It is calculated as:

Dirty Price = Clean Price + Accrued Interest

If the clean price is $1,025 and accrued interest is $20, you pay $1,045 at settlement. The seller receives $1,045 in total compensation; $1,025 for the bond going forward, and $20 for the time they held it.

## Calculating Accrued Interest

The formula depends on the **day-count convention** used for the bond. The most common conventions are:

**Actual/360**: Days actually elapsed divided by 360 (used widely for corporate and government bonds).

**30/360**: Assumes 30 days per month and 360 days per year; simplifies calculation but is less precise (used often in U.S. municipal and corporate bonds).

**Actual/Actual (ISDA)**: Days actually elapsed divided by actual days in the coupon period; most precise and used for government bonds in many jurisdictions.

The general formula is:

**Accrued Interest = (Annual Coupon ÷ Coupon Frequency) × (Days Held ÷ Days in Period)**

### Worked Example: Actual/360 Convention

Suppose you buy a corporate bond with:
- $1,000 par value
- 4% annual coupon (paid semiannually, $20 per coupon)
- Last coupon paid on March 15
- Settlement date: May 20 (66 days after March 15)
- Next coupon date: September 15 (184 days from March 15)

Days held (actual count): 66
Days in coupon period (actual): 184
Annual coupon: $40

Accrued Interest = ($40 ÷ 2) × (66 ÷ 184)
Accrued Interest = $20 × 0.3587 = $7.17

If the clean price is $1,010, the dirty price is $1,010 + $7.17 = $1,017.17.

### Worked Example: 30/360 Convention

Using the same bond but a 30/360 day count:

Days from March 15 to May 20 under 30/360:
- March 15 to March 31: 15 days (March 31 minus March 15)
- April: 30 days
- May 1 to May 20: 20 days
- Total: 65 days

Days in coupon period under 30/360: 184 days (March 15 to September 15, both under 30/360)

Accrued Interest = $20 × (65 ÷ 184) = $20 × 0.3533 = $7.07

The difference from the Actual/360 calculation is small but present. Different conventions matter most for very short accrual periods or unusual maturity dates.

## Accrued Interest Resets at the Coupon Date

On the coupon date (March 15 in the example above), the accrued interest is zero. The buyer receives the full $20 coupon, and a new accrual period begins. By the next coupon date, accrued interest has risen from $0 to the full $20 coupon, assuming daily increments.

This pattern is why bond prices appear to "jump up" around coupon dates if you only look at clean prices. In fact, what's happening is that accrued interest drops sharply (to zero) when the coupon is paid, but the dirty price remains smooth.

## Ex-Coupon Dates and the Clean Price

Some markets define an **ex-coupon date**, typically a few days before the coupon payment date. If you buy a bond on or after the ex-coupon date, you are not entitled to the next coupon—the seller receives it instead. The clean price typically rises noticeably around ex-coupon, because the new buyer will not receive the imminent coupon and thus should not pay accrued interest.

In most U.S. bond markets, the ex-coupon concept is less formal; instead, settlement date relative to coupon date determines whether you receive the coupon.

## Accrued Interest and Bond Valuation Models

When pricing a bond using a present-value formula, analysts discount the full cash flows (coupons and principal) and then subtract accrued interest to arrive at the clean price. The model calculates:

PV of all future cash flows = (Dirty Price)

Then:
Clean Price = Dirty Price − Accrued Interest

Conversely, if you have the clean price from a market quotation and want the dirty price (what you pay at settlement), you add accrued interest back.

## Practical Implications for Buyers and Sellers

**For buyers**, understanding accrued interest prevents overpaying. A bond quoted at 101 clean does not cost $1,010; if accrued interest is $15, you pay $1,025. This is critical for budgeting the total cash outlay.

**For sellers**, the accrued interest is compensation for holding the bond; it is separate from the sale proceeds and is treated as income (or a return of principal, depending on tax treatment). In many jurisdictions, accrued interest is taxed as ordinary income to the seller, not as a capital gain.

**For portfolio accountants**, the distinction between clean and dirty price matters for mark-to-market valuations. Portfolios are typically valued using dirty prices (what they would actually fetch in a trade), but data feeds and market quotes are usually clean prices.

## Day-Count Conventions Across Markets

Different bond markets use different conventions:
- **U.S. Treasuries**: Actual/Actual (ISDA)
- **U.S. Corporate and Municipal bonds**: 30/360
- **U.S. Agency bonds**: Varies; some use Actual/360
- **Eurobonds**: Actual/Actual or Actual/360
- **Government bonds (most other countries)**: Often Actual/Actual or Actual/360

When trading internationally or comparing bonds, always verify the day-count convention. The difference in accrued interest can be material over a long holding period or for high-coupon bonds.

## See also

<div class="wiki-seealso">

### Closely related

- [Coupon Payment](/coupon-payment/) — How coupon schedules and amounts are defined
- [Yield to Maturity vs Current Yield](/yield-to-maturity-vs-current-yield/) — How yield measures respond to clean vs. dirty prices
- Bond Settlement — The mechanics of trade execution and delivery
- [Reinvestment Risk in Bonds](/reinvestment-risk-bonds/) — How accrued interest ties into overall bond returns
- [Duration Gap](/duration-gap/) — Sensitivity of bond prices to accrued interest changes

### Wider context

- [Bond](/bond/) — Core bond terminology and structure
- [Interest Rate Risk](/interest-rate-risk/) — How bond prices respond to rate moves
- [Basis](/basis/) — Cost basis and accrued interest in tax accounting
- [Yield Curve](/yield-curve/) — Market pricing across the maturity spectrum

</div>

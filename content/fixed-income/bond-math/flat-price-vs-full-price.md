---
title: "Flat Price vs Full Price in Bond Markets"
description: "Bonds are quoted at flat (clean) price but settle at full (dirty) price; accrued interest bridges the gap at any settlement date."
keywords:
  - flat price vs full price bond
  - accrued interest bond settlement
  - clean price dirty price
  - bond market convention
  - fixed income settlement
image: "/svg/fixed-income.svg"
---

*Bond traders quote a **flat price** (also called **clean price**)—the price without accrued interest—but the bond settles at the **full price** (also called **dirty price** or invoice price), which includes accrued interest from the last coupon date to settlement. This split exists because bonds pay coupons on fixed dates; between coupon payments, the bondholder who purchased mid-interval must compensate the seller for the interest that has accrued on their watch. The difference is always accrued interest, calculated on a day-count convention and proportional to the time elapsed in the coupon period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Flat vs Full Price — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The buyer pays accrued interest to the seller at settlement; coupon dates reset the accrual counter.</div>

|   |   |
|---|---|
| **Flat (clean) price** | What bond dealers quote; excludes accrued interest |
| **Full (dirty) price** | What the buyer actually pays; includes accrued interest |
| **Formula** | Full price = Flat price + Accrued interest |
| **Accrued interest** | (Days since last coupon / Days in coupon period) × Coupon payment |
| **Day count basis** | Varies: Actual/360, 30/360, Actual/Actual (depends on bond type) |

</aside>

## Why the two prices exist

Suppose a corporate [bond](/bond/) pays a $40 coupon on March 15 and September 15 of each year. You purchase the bond on June 15, three months after the last coupon date. The seller held the bond from March 15 to June 15 and earned interest during those three months. When you buy the bond, you are buying a contract to receive the next coupon on September 15—the full $40. But you only held the bond for three months of the six-month period.

It would be unfair for the seller to receive zero interest and for you to receive the entire coupon. So the market convention is: you pay the seller the flat price (what dealers quote), plus the accrued interest from March 15 to June 15. On September 15, when the $40 coupon arrives, you keep it all—compensation for holding the bond for the remaining three months.

This mechanism ensures that no one is unjustly enriched or impoverished by the timing of the purchase.

## Calculating accrued interest

Accrued interest is proportional to the time elapsed since the last coupon payment:

**Accrued Interest = (Days since last coupon / Days in coupon period) × Annual coupon payment per period**

Example: The bond above pays 4% coupon semiannually on a $1,000 face value. Each semiannual coupon is $20. The last coupon was March 15; today is June 15 (exactly 92 days later in a June 15 to March 15 count). The coupon period from March 15 to September 15 is 184 days (by Actual/Actual day-count convention for corporate bonds).

Accrued interest = (92 / 184) × $20 = $10.

If the flat price is $1,005, the full price you pay at settlement is $1,005 + $10 = $1,015.

## Day-count conventions: the wrinkle

Different bond markets use different day-count conventions. The numerator (days elapsed) and denominator (total days in the period) are calculated differently depending on the bond type:

- **Actual/Actual (ISDA)**: Count actual days elapsed and actual days in the coupon period. Standard for U.S. Treasuries.
- **Actual/360**: Count actual days elapsed; denominator is always 360. Common for corporate bonds and other bonds.
- **30/360**: Assume 30 days per month and 360 days per year; count that way regardless of reality. Used for some municipal and corporate bonds.

The choice affects accrued interest by 1–3% in practice, which is material when exact settlement amounts are critical.

## When accrued interest resets

On each coupon payment date, accrued interest resets to zero. If you own the bond and collect the coupon, you effectively reset your accrual counter for the next period.

- **Coupon date**: Accrued interest = 0 (the coupon just paid)
- **One day after coupon**: Accrued interest = 1 day's worth
- **Half-period after coupon**: Accrued interest ≈ half the coupon amount

This is why bond prices, quoted flat, often show a sawtooth pattern on a chart: they dip on coupon dates (accrued interest drops to zero) and then drift upward between coupons as accrued interest accumulates.

## Flat price vs. full price in practice

**Trading screens and indices**: Dealers and indices quote flat prices. If you see "99.50" on Bloomberg or a bond fund's holdings sheet, that is the flat price.

**Settlement**: The actual cash that changes hands at settlement is the flat price plus accrued interest. The buyer's wire, the seller's receipt, and the post-trade reports all show the full price.

**Bond funds and mark-to-market**: Bond funds report "NAV" (net asset value) based on full prices of the bonds they hold, not flat prices. But when a fund publishes its portfolio, the prices listed are often flat (for easy comparison to market quotes).

**Accounting and financial reporting**: [Accounts payable](/accounts-payable/) and [accounts receivable](/accounts-receivable/) for bonds typically split the flat price and accrued interest into separate line items, to maintain clean matching with coupon payment flows.

## Example: a $10 million bond purchase

You buy $10 million face value of a corporate [bond](/bond/). The flat price is $102.50 (per $100 face value). The bond pays 3.5% coupon semiannually; the last coupon was 45 days ago. The coupon period is 182 days.

Each semiannual coupon = (3.5% / 2) × $10,000,000 = $175,000

Accrued interest = (45 / 182) × $175,000 = $43,407

Flat price amount = $102.50 × 10,000,000 / 100 = $10,250,000
Full price (settlement amount) = $10,250,000 + $43,407 = $10,293,407

The seller receives $10,293,407 in cash; the buyer becomes the owner of a bond position that will receive the next coupon in 137 days.

## The relationship to clean vs. dirty price in other markets

In equity markets, there is no analogous split: you pay one price, period. In commodity markets, forward prices and spot prices differ, but not in the way bonds split into flat and full prices.

Bonds are unique among liquid markets in splitting the quoted price (flat) from the settlement price (full), a practice that traces to the convention that coupons are paid on fixed dates regardless of ownership changes. The transparency of this split—publishing both prices clearly—helps investors understand their true economic exposure.

## See also

<div class="wiki-seealso">

### Closely related

- [Bond](/bond/) — coupon mechanics and principal repayment
- [Coupon-Payment](/coupon-payment/) — scheduled cash flows; the source of accrued interest
- [Accrued-Interest](/accrued-interest/) — detailed treatment of how accrual works and why
- [Yield-to-Maturity](/yield-to-maturity/) — calculated using full price at settlement
- [Bond-Basis-Points-Value](/bond-basis-points-value/) — basis point value is computed from flat prices but applied to full cash flows

### Wider context

- [Par-Yield-vs-Spot-Rate](/par-yield-vs-spot-rate/) — yield curve quotes are based on flat prices
- [Bond-Convexity-Adjustment](/bond-convexity-adjustment/) — price sensitivity applies to flat prices
- [Treasury-Bond](/treasury-bond/) — uses Actual/Actual day-count; default for rates discussion
- [Corporate-Bond](/corporate-bond/) — often uses Actual/360 day-count convention
- [Secondary-Market](/secondary-market/) — where flat and full prices are both standard

</div>

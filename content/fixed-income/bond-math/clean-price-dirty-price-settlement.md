---
title: "Clean Price vs Dirty Price at Settlement"
description: "Clean price vs dirty price at bond settlement: why investors pay accrued interest on top of the quoted price."
keywords:
  - clean price dirty price at bond settlement
  - bond accrued interest
  - settlement price bonds
  - quoted price vs invoice price
  - bond pricing convention
image: /svg/fixed-income.svg
---

*A **clean price** is the quoted price of a bond; the **dirty price** (or invoice price) is what a buyer actually pays at settlement, including accrued interest since the last coupon date. The difference ensures the seller is compensated for the time they held the bond between coupons.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clean vs Dirty Price — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The clean price omits accrued interest; the dirty price includes it.</div>

|   |   |
|---|---|
| **Clean price** | Quoted market price; excludes accrued interest |
| **Dirty price** | Settlement amount; equals clean price + accrued interest |
| **Who benefits** | Seller compensated for holding between coupons |
| **Why it matters** | Buyer must budget for full cash outlay, not headline price |
| **Calculation** | Dirty = Clean + (coupon × days elapsed / days in period) |
| **When paid** | Dirty price exchanged at settlement; clean price is the market quote |

</aside>

## Why Two Prices?

Bond markets quote the clean price to create a stable, comparable benchmark. If the quoted price moved around each day simply because time passed between coupons, pricing would become chaotic. Imagine a bond quoted at $1,000 one day drops to $990 the next—not because credit risk or rates changed, but because the next coupon is three days closer. That would make it nearly impossible to spot real value changes.

By stripping out accrued interest and quoting clean, the market isolates the true economic value of the bond from the mechanical accumulation of interest owed. The clean price reflects what the bond is fundamentally worth; the accrued interest is a separate, easily calculated add-on.

## The Settlement Mechanics

When you buy a bond, the settlement happens days later (typically T+2 in the US: trade date plus two business days). By settlement, more days have passed since the last coupon payment. The seller has "earned" interest for every day they held the bond. The buyer must reimburse them for that accrued interest, even though the coupon will be paid in the future to the new owner.

This keeps the seller whole: they sold the bond mid-coupon period, so they recover the interest they accrued.

At settlement, you pay: **Dirty Price = Clean Price + Accrued Interest**

The actual cash transfer is the dirty price. The clean price is what you see on Bloomberg or your broker's terminal—it's the market's shorthand.

## How Accrued Interest Is Calculated

Accrued interest is straightforward arithmetic:

**Accrued Interest = Coupon Payment × (Days Elapsed / Days in Coupon Period)**

Suppose a bond pays $50 semi-annually (5% coupon on $1,000 par). The last coupon was paid 45 days ago, and the next one is in 135 days (total 180-day period). Accrued interest = $50 × (45 / 180) = $12.50.

If the clean price is $995, the dirty price is $995 + $12.50 = $1,007.50.

The buyer pays $1,007.50 at settlement. Three months later, the issuer pays the next coupon ($50) to the buyer—the new owner gets the full amount, not a split.

## Dirty Price and Yield Calculations

When you calculate [yield-to-maturity](/yield-to-maturity/) or compare bond returns, you use the dirty price (the actual cash outlay), not the clean price. A bond quoted at a very low clean price might have a healthy yield if accrued interest is large; ignoring it would distort your return estimate.

Similarly, when a bond is trading between coupon dates, the dirty price can be above or below par even when the clean price appears below par. The accrued interest cushion matters for total return analysis.

## Market Convention Varies

US Treasury bonds, most corporate bonds, and municipal bonds follow this clean/dirty convention. However, some markets quote differently. Emerging-market or illiquid bonds may trade "flat" (including accrued interest in the quoted price from the outset), or quote accrued interest as a separate line item. Always check the trading convention for the specific bond or market.

## Why It Matters at Settlement

The clean/dirty split becomes real the moment you settle a trade. Your broker's system shows the clean price on the screen, but the settlement instruction includes accrued interest. If you're not paying attention, you might be surprised by the total cash due. Understanding the split prevents settlement mishaps and helps you budget the full cost of a bond purchase.

For institutional traders, accrued interest also affects repo markets and collateral accounting. A bond financed via repurchase agreement involves returning the bond plus accrued interest, which is a distinct line item in the financing cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Coupon Payment](/coupon-payment/) — scheduled interest payments to bond holders
- [Coupon Rate](/coupon-rate/) — the annual interest rate of a bond
- [Yield to Maturity](/yield-to-maturity/) — the total return on a bond held to redemption
- [Bond](/bond/) — the core fixed-income security
- [Par Value](/par-value/) — the face amount of a bond
- [Corporate Bond](/corporate-bond/) — bonds issued by companies

### Wider context

- Bond Math — pricing, duration, and cash flow concepts
- Fixed Income — the broader asset class
- [Repurchase Agreement](/repurchase-agreement/) — short-term financing secured by bonds

</div>

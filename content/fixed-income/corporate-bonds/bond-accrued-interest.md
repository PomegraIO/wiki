---
title: "Bond Accrued Interest"
description: "The portion of the next coupon payment owed to the seller of a bond when it's sold between coupon dates, calculated pro rata for the holding period."
---

*When you buy a bond between coupon dates, you pay the seller not just the bond's price but also accrued interest—the fraction of the upcoming coupon they've "earned" by holding the bond. This mechanism keeps the coupon payment whole for the current holder and compensates the previous holder for their time.*

<div class="wiki-hatnote">
For the coupon mechanism, see <a href="/wiki/coupon-payment/">Coupon payment</a>. For the overall bond, see <a href="/wiki/corporate-bond/">Corporate bond</a>.
</div>

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Accrued Interest — key facts</div>
  <table>
    <tr><th>When it applies</th><td>Bond sale between coupon dates</td></tr>
    <tr><th>Calculation</th><td>Coupon × (days held / days in period)</td></tr>
    <tr><th>Who pays</th><td>Buyer pays seller at settlement</td></tr>
  </table>
</aside>

## Why accrued interest exists

Imagine a bond pays $50 [coupon](/wiki/coupon-payment/) twice a year. The coupon dates are June 15 and December 15. You hold the bond from June 16 to November 30 and then sell it. You've owned the bond for 168 days of the 184-day coupon period, but the next $50 payment (on December 15) goes to the new owner—even though you've "earned" most of it.

Accrued interest solves this. You calculate how much of the $50 coupon you've earned pro rata: $50 × (168/184) ≈ $45.65. At settlement, the buyer pays you the bond's [market price](/wiki/fair-value/) plus $45.65 in accrued interest. On December 15, the new owner collects the full $50 coupon from the issuer. Everyone is made whole.

## How it's calculated

The standard convention for corporate bonds is **actual/360** in the U.S.: count the actual number of days you held the bond, divide by 360 (the standard bond year). For example:

- Previous coupon date: June 15
- Sale date: November 30
- Coupon payment date: December 15
- Days held in this period: June 16 to November 30 = 168 days
- Semi-annual coupon: $25
- Accrued interest: $25 × (168/180) ≈ $23.33

Note: The 180 days is the actual count of days in the June–December coupon period, not 360/2.

Different markets use different day-count conventions. Treasury bonds use **actual/actual** (count days precisely, divide by the actual number of days in the year). Municipal bonds often use **30/360** (assume each month is 30 days). These conventions matter for large trades, so traders always specify.

## Accrued interest in bond pricing

Quoted bond prices in the market are "clean prices"—excluding accrued interest. So if you see a bond quoted at 102 (meaning 102% of [par value](/wiki/par-value-bond/)), that's the clean price. The "dirty price" (or full price) is the clean price plus accrued interest. You pay the dirty price at settlement.

This distinction matters for comparing yields. Two bonds with different coupon dates will have different amounts of accrued interest, so a simple price comparison is misleading. Traders always standardize to clean prices or [yield to maturity](/wiki/yield-to-maturity/) for fair comparison.

## Accrued interest and taxes

In the U.S., accrued interest you receive on a bond sale is taxed as ordinary income, not capital gain. If you bought a bond and sold it two months later, receiving $45 in accrued interest, that $45 is taxable income at your ordinary rate, even if the bond's value (clean price) fell. The gain or loss on the bond itself (capital gain/loss) is taxed separately. This tax treatment encourages longer holding periods and can catch retail investors off guard if they're not careful.

## At issuance and at maturity

New bonds are usually issued on a coupon date, so the first buyer doesn't pay accrued interest. But if a bond is issued mid-coupon period (say, a new issue settles on August 1 but the next coupon is September 1), the issuer may pay an "odd first coupon" to keep payments on schedule.

At [maturity](/wiki/bond-maturity-corporate/), the bondholder receives the final [par value](/wiki/par-value-bond/) plus accrued interest through the maturity date. If you hold the bond to the exact maturity date and no coupons remain, you collect the par plus any accrued interest in the final period.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/coupon-payment/">Coupon payment</a> — the periodic interest you receive.</li>
  <li><a href="/wiki/par-value-bond/">Par value</a> — the principal amount on which coupon is calculated.</li>
  <li><a href="/wiki/yield-to-maturity/">Yield to maturity</a> — accounts for coupon and accrued interest in return calculation.</li>
  <li><a href="/wiki/bond-maturity-corporate/">Bond maturity</a> — when the final coupon and par are paid.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/corporate-bond/">Corporate bond</a> — the security on which accrued interest applies.</li>
  <li><a href="/wiki/current-yield/">Current yield</a> — annual coupon divided by clean price.</li>
  <li><a href="/wiki/bond-indenture/">Bond indenture</a> — specifies coupon dates and accrual method.</li>
</ul>
</div>

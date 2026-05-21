---
title: "Bond-Equivalent Yield"
description: "A standardized yield measure that converts Treasury bill returns to a semi-annual compounding basis, making them comparable to bond yields."
---

*Treasury bills are quoted on a discount basis rather than as yields. To make [Treasury bill](/wiki/treasury-bill/) returns comparable to [Treasury bond](/wiki/treasury-bond/) yields, traders calculate the bond-equivalent yield (BEY)—the annualized yield assuming semi-annual coupon compounding, the standard for longer-term bonds.*

## Why the adjustment is necessary

[Treasury bills](/wiki/treasury-bill/) mature in one year or less and do not pay coupons. They are sold at a discount: you might buy a 6-month bill for $98,000 and receive $100,000 at maturity. The discount represents the yield. However, bills are quoted as a "discount yield" (the return divided by the par value, annualized), not the investor's actual return.

A [Treasury note](/wiki/treasury-note/) or bond, by contrast, is quoted as a yield-to-maturity assuming semi-annual compounding. To compare a bill's return to a note's yield, you must convert the bill's discount yield to a bond-equivalent basis.

## The conversion formula

The bond-equivalent yield can be approximated by:

BEY ≈ (Discount Yield) × (365 / days to maturity)

Or more precisely:

BEY = [2 × (Par - Price) / Price] × (365 / days to maturity)

Example: A 6-month bill priced at $98,000 with par value $100,000 has a discount of $2,000. The discount yield is roughly ($2,000 / $100,000) × (365 / 182) = 4.01%. The BEY, accounting for semi-annual compounding, would be slightly higher.

## Practical usage

Traders use bond-equivalent yield to quickly compare bills and notes. If the 6-month bill BEY is 4.5% and the 2-year note yield is 4.6%, the trader can see that the note is only slightly richer in yield despite its longer maturity. This makes the [yield curve](/wiki/yield-curve/) more intuitive.

Financial platforms and bond traders routinely report bills in both discount yield and BEY format. Bloomberg terminals, for example, show both figures side-by-side.

## Annualization and compounding

The bond-equivalent yield is annualized and assumes semi-annual compounding. This is a convention tied to the coupon-paying bond world: most U.S. Treasuries and corporate bonds pay coupons twice per year. By standardizing all yields to semi-annual compounding, traders can compare instruments with different payment frequencies.

An investor comparing a 3-month bill BEY of 4% to a 2-year note yield of 4.2% should not conclude they are being paid for duration risk. The true return comparison requires accounting for the reinvestment of short-term proceeds (a 3-month investor would reinvest four times per year, compounding more frequently than a semi-annual frequency).

## Precision and market convention

The exact formula for BEY varies slightly depending on day-count conventions (actual/360, actual/365, etc.) used for bills versus bonds. The U.S. Treasury market uses actual/360 for bills and actual/actual for bonds, creating a small discrepancy. In practice, traders are aware of these conventions and adjust their comparisons accordingly.

For very short maturities (less than 90 days), the BEY conversion becomes more important because the discount yield can understate the annualized return.

## Investment implications

Investors should understand BEY when deciding between bills and bonds. A high 6-month bill BEY might lure you into short-term commitments, but if you plan to hold for years, reinvestment risk is significant. The BEY figure alone doesn't show the full picture of your total return.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/treasury-bill/">Treasury Bill</a> — short-term Treasuries with discount-basis pricing.</li>
<li><a href="/wiki/yield-to-maturity/">Yield to Maturity</a> — the standard yield measure for bonds.</li>
<li><a href="/wiki/current-yield/">Current Yield</a> — another yield measure based on coupon income.</li>
<li><a href="/wiki/reinvestment-risk/">Reinvestment Risk</a> — affects comparisons between bills and longer bonds.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/treasury-note/">Treasury Note</a> — medium-term bonds quoted in traditional yield terms.</li>
<li><a href="/wiki/yield-curve/">Yield Curve</a> — comparison of yields across maturities using BEY for consistency.</li>
<li><a href="/wiki/fixed-income/">Fixed Income</a> — the asset class where yield standardization matters.</li>
</ul>
</div>

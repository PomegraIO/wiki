---
title: "Full Price vs. Clean Price"
description: "Why bonds trade on clean price but settle at the dirty price that includes accrued interest owed to the seller."
keywords:
  - bond pricing
  - accrued interest
  - dirty price
  - settlement price
  - bond trading mechanics
  - coupon accrual
image: "/svg/fixed-income.svg"
---

*A **bond's clean price** is what you see quoted on the market—the actual bond value stripped of accrued interest. The **full price** (or **dirty price**) includes accrued interest owed to the seller since the last coupon date. At settlement, you pay the full price; the gap between the two reflects how much of the next coupon the previous owner has earned.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Full Price vs. Clean Price — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income concepts." />

<div class="wiki-infobox-caption">Two ways of stating the same bond transaction: one shows pure value, one includes earned interest.</div>

|   |   |
|---|---|
| **Clean price** | What you see quoted; excludes accrued interest |
| **Full price** | Clean price + accrued interest; what you actually pay |
| **Also called** | Full price = dirty price, invoice price |
| **Accrued interest** | The coupon earned by the seller since the last payment date |
| **Why it matters** | Ensures the seller is fairly compensated for interest earned before sale |
| **Standard quote** | Almost all bond markets quote the clean price |
| **Settlement payment** | Buyer remits the full price; seller nets accrued interest |

</aside>

## The mechanics of the coupon gap

When you buy a [bond](/bond/) between [coupon payment](/coupon-payment/) dates, you are not stepping into a clean situation. The seller has owned the bond since the last coupon date and is entitled to a portion of the next coupon payment. Rather than wait for the issuer to pay and then redistribute that interest to the seller, the market simplified the problem: the buyer pays the seller directly for the accrued interest as part of the settlement.

This is where clean and full prices diverge. Imagine a bond with a 5% annual coupon, paid semi-annually. The coupon date passed three months ago; the next payment is three months away. The seller has earned exactly half of the upcoming coupon. If the bond's clean price (what traders quote) is $100, the full price—what you actually remit—includes the accrued interest:

Full Price = Clean Price + Accrued Interest

In this case, with half a coupon earned:
Full Price = $100 + ($2.50) = $102.50

The buyer pays $102.50. At settlement, $100 belongs to the bond itself (the quoted price), and $2.50 goes directly to the seller for the interest already earned.

## Why bond markets quote clean prices

Traders and dealers post clean prices, not full prices, because clean prices are stable and comparable. Full prices wobble every day as accrued interest grows. If bonds were quoted on a full-price basis, the same bond would appear to move upward by a tiny fraction every single day (the accrued interest accumulating), even if its true value hadn't changed at all. This makes price tracking and yield comparison chaotic.

By stripping out the accrued interest, the clean price gives a clear signal about actual value. All else equal, if a bond's clean price ticks up, it is genuinely worth more; if it ticks down, it is worth less. Accrued interest adds nothing to this clarity—it is purely mechanical. Quoting the clean price is therefore a market-wide convention: it tells traders the bond's true economic value independent of the calendar.

## Accrued interest and the day-count convention

The amount of accrued interest depends on how many days have passed and how many days are in the full coupon period. But "how many days" is not as obvious as it sounds. Do you count weekends and holidays? Does a 30-year month have 30 or 31 days for interest purposes? This is where [day-count conventions](/day-count-conventions/) come in.

The most common conventions are Actual/360 (used for most corporate and government bonds in the US), Actual/365 (UK and Eurobonds), and 30/360 (some corporate bonds and municipal bonds). Whichever convention the bond specifies, accrued interest is calculated as:

Accrued Interest = Coupon × (Days Elapsed / Days in Period)

A bond using Actual/360 counts the actual number of calendar days elapsed and divides by 360. A bond using Actual/365 uses 365. The choice has small but real effects on the dollar amount owed to the seller.

## Full price on the ex-dividend date

One exception to this pattern appears on the [ex-dividend](/dividend/) date in some markets. In the UK gilt market, the seller on the ex-dividend date forfeits the next coupon payment entirely to the buyer. On the ex-date, accrued interest drops to zero, and the full and clean prices converge. For one day, the buyer gets a "free" coupon. The following business day, accrued interest begins accumulating again toward the next buyer.

Most US bond markets do not observe an ex-date in the same way; accrued interest is calculated continuously based on actual settlement, not the trade date. This keeps the process more uniform.

## Settlement mechanics and the invoice

When you buy a bond through a broker, the confirmation shows both the clean price (the quoted price you negotiate) and the full price (the amount you must wire or the amount credited to your account). The accrued interest is explicitly broken out on the trade ticket so both parties can verify the calculation.

At [settlement](/), which typically occurs one or two business days after the trade, the buyer's cash account is debited by the full price, and the seller's is credited by it. The [custodian](/custodian/) or the [broker](/broker/) handles the routing; from the buyer's perspective, the wire includes everything.

## Reinvestment and the full price

From an investment-return perspective, the full price you pay affects the yield you realise. If you overpay on accrued interest (perhaps due to a mispriced deal or a calculation error), your true return falls; if you underpay, your return rises. The full price is therefore the correct starting point for any [yield-to-maturity](/yield-to-maturity/) or [total return analysis](/total-return-analysis/), because it represents the true economic outlay.

For example, if two traders are comparing the same bond and one quotes a clean price of $101 while another quotes $100, the difference might be a clean one basis point of actual value—or it might be a mispricing. Checking the full price (clean + accrued) reveals which is true, and whether the accrual is correctly calculated under the bond's stated [day-count convention](/day-count-conventions/).

## See also

<div class="wiki-seealso">

### Closely related

- [Coupon Payment](/coupon-payment/) — the interest owed to the bondholder on each payment date
- [Day-Count Conventions](/day-count-conventions/) — rules for calculating accrued interest and yield
- [Yield-to-Maturity](/yield-to-maturity/) — the discount rate that makes full price equal to the present value of all future cash flows
- [Bond](/bond/) — the foundational debt instrument
- [Total Return Analysis](/total-return-analysis/) — projecting the full investment outcome over a holding period
- [Horizon Return](/horizon-return/) — total return over a specific time horizon

### Wider context

- [Fixed-Rate Mortgage (Personal)](/fixed-rate-mortgage-personal/) — another instrument where accrued interest affects settlement
- [Interest Rate](/interest-rate/) — the economic force behind coupon and accrual
- Bond Valuation — broader approach to pricing bonds
- Settlement — the mechanics of transferring ownership and payment

</div>

---
title: "Accrued Interest"
description: "Interest accumulated on a bond between coupon payment dates and whose responsibility is accrued interest."
keywords:
  - accrued interest bonds
  - coupon payments
  - dirty price
  - bond settlement
---

*[**Accrued interest**](/wiki/accrued-interest-bonds/) is the interest earned on a [bond](/wiki/bond/) from the last [coupon payment](/wiki/coupon-payment/) date to the settlement date, owed to the seller when a bond trades between coupon dates. A bond paying 5% annually ($50 per $1,000 par) accrues $5 per month; if sold 8 months after a coupon date, the buyer must compensate the seller for $40 of accrued but unpaid interest. This adjustment separates the **dirty price** (the full cost to the buyer) from the **clean price** (the quoted market price), affecting bond trading mechanics and [yield](/wiki/yield-to-maturity/) calculations.*

<aside class="wiki-infobox">

| Term | Definition |
|------|-----------|
| **Clean price** | Quoted market price, excluding accrued interest |
| **Dirty price** | Clean price + accrued interest (actual cash cost) |
| **Accrued interest** | Interest from last coupon date to settlement |
| **Coupon period** | Days between two coupon dates |
| **Accrual fraction** | (Days elapsed) ÷ (Days in coupon period) |
| **Day-count convention** | 30/360, Actual/360, Actual/Actual, etc. |

</aside>

## Why accrued interest exists: fairness in mid-coupon transfers

Imagine a bond with a $1,000 par, 5% annual coupon, and semi-annual payments on January 1 and July 1. An investor holding the bond from January 1 to June 15 (6.5 months) has earned interest for 6.5 months (~$27.08 on a $1,000 bond), but the next coupon payment ($25) is not until July 1. If the bondholder sells on June 15, they surrender the entire July 1 coupon payment of $25 to the buyer, even though only 2 weeks of that coupon was earned by the new holder. Accrued interest solves this: the buyer pays the seller the $27.08 accrued interest in addition to the quoted ("clean") bond price, and the buyer receives the full $25 coupon on July 1, offsetting the accrual paid up front.

## Clean price versus dirty price: the quoted convention

Bonds are quoted on a **clean price** basis—the price excluding accrued interest. A bond quoted at 102 means $1,020 per $1,000 par *before* accrued interest. The **dirty price** is the cash amount the buyer actually pays: dirty price = clean price + accrued interest. At settlement, if 150 days have elapsed in a 180-day coupon period (semi-annual bond), the accrual fraction is 150/180 = 0.833. If the coupon is $25, accrued interest is $25 × 0.833 = $20.83. A bond quoted at 102 has a dirty price of $1,020 + $20.83 = $1,040.83. This distinction is important for accounting: the bond buyer records the purchase cost as $1,040.83 (capitalized as an asset), but only $20.83 is interest expense (flows through the income statement immediately); the remaining $1,020 is the cost basis.

## Day-count conventions: how accrual is calculated

Bonds use standardized **day-count conventions** to compute accrued interest, because the exact number of days between coupon dates affects the fraction:
- **Actual/Actual (ISDA)**: Count actual calendar days in the coupon period and actual days since last coupon. Most common for government bonds and high-grade corporates.
- **30/360**: Assume each month has 30 days, each year has 360 days. Common for U.S. corporate and agency bonds. Simplifies calculation by hand.
- **Actual/360**: Count actual days since last coupon, assume year = 360 days. Used for money-market instruments (commercial paper, bankers' acceptances, Treasury bills).
- **Actual/Actual (ICMA)**: Count actual days in both periods. Used for euro-zone and international bonds.

For example, if a 30/360 bond last paid a coupon on January 15 and it is now February 20, the accrual is (30 - 15 + 20) / 360 = 35/360 days elapsed in a theoretical 180-day period (half year), so accrual = coupon × 35/360. Different conventions produce slightly different accruals (rounding differences), but they are typically <1 basis point.

## The spread-to-treasury and [yield curve](/wiki/yield-curve/) implications

When a bond trades between coupons, both the [bid and ask](/wiki/bid-ask-spread/) include accrued interest. A trader might see:
- Bid: 101.50 clean, ask: 101.55 clean
- With 100 days elapsed in a 182-day semi-annual coupon period
- Accrued interest: $25 × (100/182) = $13.74

The actual bids and asks are:
- Bid dirty: 101.50 + 1.374 = 102.874
- Ask dirty: 101.55 + 1.374 = 102.924

The spread is 0.05 points clean (or 0.05% of par, or 5 basis points), which is standard for corporate bonds. The accrued interest is identical on bid and ask (same accrual date), so it does not affect the spread; it is just an add-on to both sides.

## Corporate actions and accrued interest complications

When a bond is called, tendered, or converted, the issuer pays the call/tender price *plus* accrued interest to the bondholder. If a convertible bond is called on March 15 and the last coupon was January 15, the accrued interest is ~$27 on a $1,000 par / 5% bond. The call price might be 102, so the bondholder receives $1,020 + $27 = $1,047, even though the call price is technically "102." This is standard practice; accrued interest is always paid at corporate actions.

## Treasury bonds and accrued-interest mechanics in the [settlement](/wiki/settlement-t2/) system

U.S. Treasuries follow **T+1 settlement** (trade date + 1 business day), and accrued interest accrues daily using Actual/Actual (ISDA) day counting. Treasury dealers quote bond prices in 1/32nds of par (e.g., 102–16 means 102 and 16/32, or 102.50). When a Treasury bond trades, the buyer sends clean price + accrued interest to the seller; the Federal Reserve's settlement system (FEDWIRE) automatically computes accrued interest from the last coupon date using ISDA rules. There are no separate accrued-interest instructions; it is an implicit component of the settlement price. This is why Treasury yields are quoted "clean yield" (yield on clean price) even though the buyer's actual out-of-pocket is dirty price.

## Negative accrued interest: when buyers owe sellers

In rare cases, **negative accrued interest** occurs. If a bond is sold *after* the coupon has been paid but a few days before the record date (the date when coupon payments are determined), the technical accrual can be slightly negative or zero. This happens only in exotic, illiquid situations and is a settlement technicality. More commonly, bonds trading on the "ex-coupon date" (after which the seller gets the next coupon) have zero accrued interest from the perspective of the buyer, but the seller still receives the full coupon—a benefit to sellers, sometimes capitalized in pricing.

## Accrued interest and [tax-loss harvesting](/wiki/tax-loss-harvesting/)

When an investor sells a bond at a loss for tax purposes, they must account for accrued interest. The [**adjusted cost basis**](/wiki/cost-basis/) is the original purchase price minus any amortization of premium or accumulation of discount, *plus* accrued interest at the sale date. If an investor bought a bond at 105 (premium of 5), has held it for 4 years and amortized the premium to 103.5, and accrued interest at sale is $15, the cost basis for loss recognition is 103.5 + 0.15 = 103.65. The realized loss is the difference between the sale proceeds (clean price + accrued interest) and the cost basis. Failure to account for accrued interest correctly leads to tax-reporting errors.

## Auction mechanics and accrued interest at bond issuance

When a new bond is issued, the issuer often uses a "regular" auction where bids are due at, say, 10 a.m. ET and settlement occurs 1 or 2 days later. At settlement, accrued interest has accumulated; if settlement is Friday and the first coupon is not until the following month, the issuer pays the first coupon on the scheduled date. Bidders at issuance pay the clean price but no accrued interest (there is none, as the bond just issued), so the invoice price equals the clean price. This is a feature of primary issuance; in secondary trading, accrued interest is always added.

## Floating-rate bonds and accrued interest on the coupon reset

For [floating-rate bonds](/wiki/floating-rate-bond/), the coupon is reset on each coupon date based on a reference rate (SOFR, SONIA, EURIBOR); accrued interest still accumulates between resets as usual. If a floating-rate bond with 5-day resets is sold mid-reset, accrued interest is pro-rata to the days since the last reset. The next coupon (determined by the new reference rate) is paid in full to the new buyer, and accrued interest compensates the seller for the partial period.

## Accrued interest in returns calculations and yield measurements

[**Total return**](/wiki/total-return-index/) on a bond includes both price change and accrued interest received. If an investor buys a bond at 100 and holds it for exactly one coupon period (e.g., 6 months), the investor receives one coupon ($25) and the bond price remains at 100. The total return is 2.5% (one coupon payment of $25 on $1,000), even though the clean price did not change. Accrued interest is central to this: the investor's cash inflows are the coupon and the sale proceeds (clean price + accrued interest at sale). Ignoring accrued interest in return calculations understates bond returns significantly.

<div class="wiki-seealso">

### Closely related
- [Coupon Payment](/wiki/coupon-payment/) — The regular interest payments bonds provide
- [Bond Price Formula](/wiki/bond-price-formula/) — Mathematical relationship between price and interest
- [Yield to Maturity](/wiki/yield-to-maturity/) — Return metric that incorporates accrued interest
- [Accrued Interest Bonds](/wiki/accrued-interest-bonds/) — Broader entry on interest mechanics

### Wider context
- [Bond Basics](/wiki/bond-basics/) — Core bond concepts
- [Settlement Procedures](/wiki/settlement-procedures/) — How accrued interest is handled at trade settlement
- [Fixed-Income Fund](/wiki/fixed-income-fund/) — Funds managing accrued interest on large portfolios
- [Cost Basis](/wiki/cost-basis/) — Importance of accrued interest for tax calculation
- [Tax-Loss Harvesting](/wiki/tax-loss-harvesting/) — Strategy using accrued interest in accounting

</div>

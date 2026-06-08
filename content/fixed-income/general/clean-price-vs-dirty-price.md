---
title: "Clean Price vs. Dirty Price"
description: "Why bond prices quoted in markets exclude accrued interest, while settlement prices include it."
keywords:
  - bond pricing
  - accrued interest
  - settlement price
  - quoted price
  - fixed-income math
image: "/svg/fixed-income.svg"
---

*A **clean price** is the quoted price of a bond stripped of accrued interest; a **dirty price** (full price) includes it. Every bond sale settles at the dirty price, but markets quote the clean price to keep the traded number stable between coupon dates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clean Price vs. Dirty Price — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for bonds and debt instruments." />

<div class="wiki-infobox-caption">One price is quoted, the other is paid.</div>

|   |   |
|---|---|
| **Clean price** | Quoted price; excludes accrued interest |
| **Dirty price** | Settlement price; includes accrued interest |
| **Formula** | Dirty = Clean + [Accrued Interest](/accrual-accounting/) |
| **When it matters** | Every bond transaction between [coupon](/coupon-payment/) dates |
| **Who sets the standard** | Convention varies by market (Treasuries, corporates, municipals) |
| **Impact on buyers** | Buyer pays more than the quoted price |

</aside>

## Why the split exists

The clean/dirty price distinction is a market convention born from practicality. When a [bond](/bond/) pays a [coupon](/coupon-payment/) semi-annually—say on 15 March and 15 September—the issuer accumulates a liability to that coupon holder every single day between payment dates. If you buy the bond on, say, 1 August (less than two months before the next coupon), you've bought the right to receive the full coupon in six weeks. But you haven't *earned* that coupon yet; the seller held the bond for eight months of the coupon period and is entitled to the interest that accrued while they owned it.

If bond prices were quoted dirty—including accrued interest—the quoted price would ping upward every day as the coupon date approached, then drop sharply on the coupon payment date (when accrued interest resets to zero). Traders would see wild swings in a seemingly unchanged bond's price, making year-to-year or bond-to-bond comparison a nightmare. The clean price convention sidesteps this. It shows the "true" price signal—the bond's actual market value stripped of the mechanical accrual effect.

## The arithmetic

Clean and dirty prices are linked by one simple formula:

**Dirty Price = Clean Price + Accrued Interest**

Accrued interest is calculated as:

**Accrued Interest = [Coupon Rate](/coupon-rate/) × Par Value × (Days Since Last Coupon / Days in Coupon Period)**

Suppose a corporate bond with a 4% annual coupon (paid semi-annually, $40 per $1,000 par) last paid on 1 June. Today is 1 September (92 days later). The coupon period is 184 days. Accrued interest is:

4% × $1,000 × (92 / 184) = $20

If the bond's clean price is $990, you pay a dirty price of $990 + $20 = $1,010 at settlement. The seller receives $1,010 but retains the $20, which they'll pocket when you collect the full $40 coupon on the next coupon date. You'll then own the bond for the remaining 92 days and will retain that $20 when *you* sell.

## Market conventions differ

Not all markets use the clean/dirty split equally. US Treasury and corporate bonds quote clean; accrued interest is reckoned at settlement and is often shown separately in trade confirmations. Government bond markets in the UK, Europe, and Japan typically quote dirty (or "full") prices directly—there is no separate accrued interest line. Municipal bonds and some emerging-market debt also have their own conventions. A trader moving between markets must know which convention applies; a price that looks cheap in one market might simply reflect a different quoting standard.

## The investor's reality

From a buyer's perspective, the dirty price is what matters. That's the cheque you write (or, more commonly, the cash that settles electronically). The clean price is the marketing number—the one that appears on your broker's screen and in financial news. A bond quoted at 98 (clean) might cost you 98.25 (dirty) if accrued interest is $0.25. Over a portfolio of 50 bonds, accrued interest can amount to several thousand pounds or dollars, and most traders and portfolio managers keep a mental map of where they sit in the coupon cycle to anticipate settlement costs.

Between coupon dates, the clean price and the dirty price diverge; after a coupon is paid, they converge (accrued interest drops to zero). A bond is often described as trading "cum-coupon" (buyer gets the next coupon) or "ex-coupon" (seller gets it)—a distinction that also affects what the buyer must pay. These mechanics mean that purchasing a bond two days before a coupon payment saves the buyer the accrued interest of two days but costs the opportunity to collect the coupon itself, a trade-off that [market price discovery](/price-discovery/) incorporates.

## Why it matters for valuation

When you [value a bond](/bond/) using a [discounted cash flow](/discounted-cash-flow-valuation/) model, you're usually discounting all future coupons and the principal at maturity. That intrinsic valuation is conceptually aligned with the dirty price—it reflects what you actually pay. However, bond analysts and traders often work with clean prices and add accrued interest as a separate line, keeping the valuation cleaner and easier to audit. Understanding which price you're looking at is essential; a newcomer who mistakes a clean price for a dirty price will wildly miscalculate their true cost of entry.

## See also

<div class="wiki-seealso">

### Closely related

- [Coupon Payment](/coupon-payment/) — the interest paid periodically on a bond
- [Bond](/bond/) — the fundamental fixed-income instrument
- [Accrual Accounting](/accrual-accounting/) — the principle underlying accrued interest
- [Settlement](/coupon-payment/) — the actual exchange of cash and securities
- [Par Value](/par-value/) — the face value on which coupon rates are based
- [Yield-to-Maturity](/yield-to-maturity/) — return calculation that uses dirty price

### Wider context

- [Coupon Rate](/coupon-rate/) — the interest rate promised to the bondholder
- [Corporate Bond](/corporate-bond/) — the most common setting for clean/dirty pricing
- [Treasury Bond](/treasury-bond/) — where US bond-pricing conventions originate
- [Price Discovery](/price-discovery/) — how market prices converge on fair value

</div>

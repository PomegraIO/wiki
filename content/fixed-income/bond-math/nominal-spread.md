---
title: "Nominal Spread"
description: "The yield difference between a corporate bond and a Treasury of the same maturity, expressed in basis points."
keywords:
  - nominal spread
  - static spread
  - yield spread
  - corporate bond
  - credit spread
  - treasury benchmark
image: /svg/fixed-income.svg
---

*The **nominal spread** is the raw percentage-point difference between a [corporate bond](/corporate-bond/)'s [yield-to-maturity](/yield-spread-measures/) and a Treasury bond or note of matching maturity. It is the simplest spread measure, calculated by subtraction: corporate yield minus Treasury yield. Though easy to compute, it ignores the shape of the [yield curve](/yield-curve/) and the bond's duration structure, making it a starting point for credit analysis rather than a complete picture of [credit risk](/credit-risk/) compensation.*

<div class="wiki-hatnote">

For the broader framework of spread measures, including Z-spread and option-adjusted spread, see [Yield Spread Measures](/yield-spread-measures/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Nominal Spread — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income products and bonds." />

<div class="wiki-infobox-caption">The yield gap between corporate and Treasury; quick to calculate, imperfect for curve effects.</div>

|   |   |
|---|---|
| **What it is** | Corporate bond YTM minus Treasury YTM of the same maturity, in basis points |
| **Also called** | Static spread, simple spread, direct spread |
| **Formula** | Nominal Spread = Corp Yield − Tsy Yield |
| **Calculation** | Instantaneous; requires two yield quotes |
| **Typical range** | Investment-grade: 50–200 bp; high-yield: 200–1000+ bp |
| **Main advantage** | Transparent, intuitive, universally understood |
| **Main drawback** | Ignores curve shape; two bonds may have identical nominal spread but different true credit risk |

</aside>

## The simplest comparison

On any given trading day, a [corporate bond](/corporate-bond/) and a Treasury of the same maturity have quoted yields. A 10-year Ford bond trades at 5.2% yield; the 10-year Treasury trades at 4.1%. The **nominal spread** is 110 basis points (5.2% − 4.1% = 1.1% = 110 bp).

That spread compensates the bondholder for [credit risk](/credit-risk/) (Ford might default; the U.S. Treasury will not, in its own currency), [liquidity risk](/liquidity-risk/) (Treasuries trade in far deeper markets), and other factors that make corporate debt riskier than government debt.

The nominal spread is the lingua franca of bond trading floors. A trader might say, "I'll buy that Ford bond if it widens to 130 bp," meaning she wants the corporate-Treasury yield gap to grow wider (and the corporate bond price to fall), raising her compensation for the risk.

## Why it's called "nominal"

The term is slightly confusing. "Nominal" here does not mean "in name only" or "insignificant." Rather, it refers to the fact that the spread is quoted at face value—at one, single maturity point—without adjusting for how the Treasury curve's shape affects the calculation. It is the nominal (straightforward, not adjusted) difference between two yields.

By contrast, the [Z-spread](/z-spread/) is an adjusted spread: it applies the constant spread across the entire Treasury spot curve, not just the one matching maturity. Most industry participants understand "nominal" versus "Z-spread" as: nominal = one point, Z-spread = full curve.

## Nominal spread in context: credit tiers

Nominal spreads vary dramatically by [credit quality](/credit-rating/):

- **Investment-Grade Corporate:** 50–150 bp in typical markets (wider in stress, tighter in complacency)
- **High-Yield (Junk) Bonds:** 200–600 bp, often spiking to 1000+ bp during distress
- **Emerging Market Sovereigns:** 100–500 bp, depending on country, fiscal health, and currency risk
- **Financial Sector Bonds:** Often trade 20–50 bp tighter than comparable industrials (implicit government backstop)

A widening nominal spread signals deteriorating credit outlook; a tightening spread signals confidence. If Ford's nominal spread widens from 110 bp to 150 bp in a month, the market is demanding more compensation, usually because of deteriorating fundamentals (lower earnings, higher debt, product recalls) or a broad risk-off market mood.

## When nominal spread misleads

**The curve-shape problem:** Suppose the 5-year Treasury yields 3.5% and a strong credit's 5-year bond yields 4.2%. Nominal spread: 70 bp. Meanwhile, the 10-year Treasury yields 4.1% and a weaker credit's 10-year bond yields 5.0%. Nominal spread: 90 bp. Does the weaker credit offer more credit value?

Not necessarily. The Treasury curve is steep (60 bp steeper at the 10-year). The weaker credit's extra 20 bp of nominal spread (90 bp vs. 70 bp) may partly reflect the curve shape, not extra credit risk. If you use the [Z-spread](/z-spread/), you might find both bonds offer the same true credit premium—the weaker credit's apparent premium comes from a duration difference, not higher [credit risk](/credit-risk/).

**The duration mismatch problem:** A 5-year bond and a 10-year bond with identical nominal spreads are not equivalent. The 10-year bond has far more [interest-rate](/interest-rate/) risk (duration). If rates spike 100 bp, the 10-year bond loses twice as much in price as the 5-year bond, even though they have the same nominal spread. A trader comparing the two would need to adjust for this.

**The embedded-option problem:** A callable bond with a 150 bp nominal spread may actually deliver far less economic upside than a straight bond at 150 bp, because the issuer can redeem the bond if rates fall. The bondholder loses the upside; the spread understates this cost. This is why [option-adjusted spread (OAS)](/yield-spread-measures/) was invented.

## When nominal spread is exactly right

Nominal spread shines for quick, relative-value decisions within tight universes:

- **All investment-grade industrials, same sector:** "These three auto-parts suppliers all have 10-year debt maturing in 2034. Nominal spreads are 95, 110, and 125 bp respectively. Which is best value?" The nominal spread gives an instant ranking, assuming the curve hasn't twisted since yesterday.

- **Same issuer, different coupons:** "I own the Ford 4% 2034 at 115 bp. Ford issued new 5% 2034 debt at 120 bp. Should I trade up?" The 5 bp nominal spread difference tells you the market value of the extra coupon.

- **Trend analysis:** Plotting Ford's nominal spread over time shows how the market's credit opinion has evolved. Widening usually signals deterioration; tightening signals improvement.

- **Auction pricing:** When a new [corporate bond](/corporate-bond/) is priced to the public, the underwriter quotes it as a nominal spread to a Treasury benchmark ("priced at +105 to Treasuries"). The investor immediately knows the spread relative to risk-free.

## The shortcut versus the full calculation

A portfolio manager running $10 billion of corporate bonds doesn't have time to re-compute Z-spreads on 500 holdings every 15 minutes. But she can glance at nominal spread changes: if XYZ Bank's nominal spread moves from 95 bp to 115 bp, something changed—either the bond's absolute yield rose while Treasury yield fell, or vice versa. That's a red flag meriting investigation.

Professional traders and risk managers use nominal spread as a screening and quick-judgment tool, then dig into [Z-spread](/z-spread/) and OAS when a trade or position requires deeper analysis. A trading system might alert on nominal spread moves; the trader then evaluates whether the move reflects credit deterioration (actionable) or curve twist (may fade).

## Historical perspective

The nominal spread has been the market standard for decades, long before computers could rapidly calculate Z-spreads and OAS. It remains embedded in:

- **Bond indices:** Credit indices are often quoted in terms of nominal spread, as a shorthand for risk
- **Regulatory guidance:** [SEC](/securities-and-exchange-commission/) disclosures and [Federal Reserve](/federal-reserve/) stress tests sometimes reference spreads in nominal terms
- **Dealer screens:** Bloomberg, Refinitiv, MarketAxess all display nominal spread as the lead metric for each corporate bond

As computing power improved, Z-spread and OAS were added as refinements. But nominal spread persisted because it is transparent and requires no model. A trader can verify the number instantly: look up the corporate bond's yield, look up the Treasury yield, subtract.

## See also

<div class="wiki-seealso">

### Closely related

- [Z-Spread](/z-spread/) — the nominal spread improved to account for curve shape
- [Yield Spread Measures](/yield-spread-measures/) — the full menu of spread calculations
- [Yield-to-Maturity](/yield-spread-measures/) — the yield metric both corporate and Treasury use
- [Credit Risk](/credit-risk/) — the primary driver of nominal spread width
- [Callable Bond](/callable-bond/) — complicates simple spread analysis; requires OAS

### Wider context

- [Corporate Bond](/corporate-bond/) — the instrument most often compared via nominal spread
- [Treasury Bond](/treasury-bond/) — the risk-free benchmark used to measure spread
- [Yield Curve](/yield-curve/) — curve shape drives differences between nominal and Z-spread
- [Interest Rate](/interest-rate/) — the foundation of all yield measurements
- [Bond](/bond/) — the general fixed-income instrument
- [Liquidity Risk](/liquidity-risk/) — bundled into spreads but distinct from credit risk

</div>

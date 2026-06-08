---
title: "Treasury Constant Maturity Rate Explained"
description: "Treasury Constant Maturity Rate: how the Fed interpolates CMT yields from on-the-run bonds and uses them in mortgage and loan pricing."
keywords:
  - treasury constant maturity rate
  - cmt rate
  - treasury interpolation
  - fed constant maturity
  - mortgage rate indexing
image: /svg/fixed-income.svg
---

*A **Treasury Constant Maturity rate** (or CMT) is an interpolated yield that the Federal Reserve calculates daily to represent what it would cost to borrow at a fixed rate for a specific maturity—typically 1, 3, 5, 10, 20, or 30 years—using the current prices of Treasury bonds. Lenders use these rates as the baseline index for mortgage and loan rates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Treasury Constant Maturity Rate — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">The CMT bridges the gap between actual Treasury auctions and the interest rates banks reference every day.</div>

|   |   |
|---|---|
| **What it is** | Daily interpolated yield on a hypothetical Treasury bond of a specific maturity |
| **Published by** | Federal Reserve (daily, via H.15 release) |
| **Common maturities** | 1, 3, 5, 10, 20, 30 years |
| **Used in** | ARM mortgages, student loans, adjustable-rate bonds, business loans |
| **Basis** | On-the-run Treasury yields, interpolated between actual auction dates |
| **Updates** | Trading days when markets are open; not weekends or holidays |

</aside>

## Why the Fed doesn't just use Treasury auction rates

When the U.S. Department of the Treasury auctions bonds, it does so on a fixed schedule—typically quarterly for the 20-year and 30-year, and monthly or more frequently for shorter maturities. This means that between auction dates, there is no official "new" Treasury yield for those periods. A mortgage lender originating a 5-year ARM on a Tuesday may need a 5-year Treasury reference rate, but the Treasury may not have auctioned a new 5-year bond in weeks.

The solution is interpolation. The Federal Reserve publishes CMT rates daily by taking the yield curves derived from actual Treasury trades on the secondary market and calculating what the yield would be at points where no official auction exists. This is not a guess—it is a mathematical fit to observed prices of Treasury securities that have recently traded.

## How CMT rates are calculated

The Fed uses a method called **polynomial spline fitting** to interpolate between on-the-run Treasury yields. On-the-run securities are the most recent, actively traded bonds of a given maturity; older issues (off-the-run) are less liquid and less representative.

Each trading day, the Fed records the closing bid and ask prices of on-the-run Treasury securities across multiple maturities. It then fits a smooth curve through these points, constraining the fit to ensure that the interpolated rates are economically sensible. The result is a continuous yield curve, from which the Fed can extract the hypothetical yield at any maturity—including the standard CMT maturities like 5 years or 10 years.

For example, if at 3 p.m. on a given day the 4-year on-the-run Treasury yields 2.50% and the 6-year on-the-run yields 2.65%, the interpolated 5-year CMT might be 2.58%. The next day, if market rates shift, the 5-year CMT will shift too, even though no new 5-year bond was auctioned.

## Where CMT appears in contracts

The CMT rate is embedded in three broad categories of financial instruments:

**Adjustable-rate mortgages (ARMs).** An ARM might reset every year to the 1-year CMT plus a 2.5% margin. When the CMT moves up, the borrower's rate follows.

**Student loans.** Federal student loans tied to variable rates often reference the CMT. Stafford loans and PLUS loans previously used the 6-month and 1-year CMT as their index, though legislation has shifted some to SOFR in recent years.

**Business and commercial loans.** Construction loans, credit facilities, and asset-based lending agreements frequently tie rate resets to the 1-year, 5-year, or 10-year CMT.

**Structured securities and bonds.** Some callable bonds and floating-rate notes use CMT as their base rate.

The appeal of CMT to lenders is that it is published by a government agency, updated daily, and deeply rooted in the most liquid market on earth—U.S. Treasuries. Borrowers can verify the rate independently and have no reason to distrust the calculation.

## CMT, par rates, and yield curves

It is important to distinguish the CMT from the spot yield curve and par yield curve used by traders. The CMT is a **par rate**—it represents the coupon yield at which a Treasury of that maturity would trade at par (face value) on that day. This is not the same as the spot rate, which reflects the pure zero-coupon yield.

For the purposes of loan and mortgage contracts, the par rate (CMT) is the economically relevant one: it tells you directly what interest rate a borrower would face if they locked in a Treasury-backed loan for that term. A trader building a full discount curve needs the spot rates, but a mortgage applicant only needs to know the CMT, because that is what their rate will be pegged to.

## Stability and volatility

The CMT rates move daily, sometimes sharply. During periods of economic stress, flight-to-safety flows push Treasury prices up and yields down, lowering the CMT. During inflationary episodes or when the Federal Reserve is tightening, Treasury yields rise and CMT rates rise.

For borrowers with ARMs indexed to CMT, this volatility can mean loan payments that climb significantly during rising-rate environments. Lenders structure ARMs with rate caps (per adjustment and lifetime) to cap the borrower's worst-case payment, but the CMT is the starting point.

For fixed-rate mortgages, the CMT is not directly relevant at origination—the lender prices off the 10-year or 30-year Treasury yield, not the CMT. But CMT rates do influence the shape of the Treasury curve and thus indirectly affect all mortgage pricing.

## Publication and where to find CMT rates

The Federal Reserve publishes CMT rates daily in its **H.15 release** (Selected Interest Rates), typically released at 4:15 p.m. ET after trading closes. The rates are available free on the Fed's website and are also published by Bloomberg, financial news sites, and mortgage platforms.

Historical CMT data stretches back decades and is useful for valuing seasoned mortgage pools or understanding how loan rates have moved relative to their index.

## See also

<div class="wiki-seealso">

### Closely related

- [Treasury Bill](/treasury-bill/) — The shortest-maturity government borrowing instrument; CMT matures directly from Treasury yield curves
- [Coupon Rate](/coupon-rate/) — The stated interest rate on a bond; CMT is a par-rate equivalent for a hypothetical Treasury
- [Yield Curve](/yield-curve/) — The shape of Treasury rates across maturities; CMT rates are interpolated points on this curve
- [Federal Reserve](/federal-reserve/) — The central bank that publishes CMT rates daily
- [Interest Rate Risk](/interest-rate-risk/) — How CMT fluctuations affect ARM borrowers and floating-rate bond holders
- Adjustable-rate mortgages (ARMs) — Loans that typically reset to CMT plus a margin

### Wider context

- [Bond](/bond/) — Fixed-income instrument; CMT is derived from Treasury bonds
- [Mortgage-Backed Security](/mortgage-backed-security/) — Pools of mortgages often indexed to CMT or other Treasury rates
- [Primary Market](/primary-market/) — Treasury auctions; CMT fills the gap between auction dates
- [Fixed-Rate Mortgage (Personal)](/fixed-rate-mortgage-personal/) — Contrast with ARMs indexed to CMT

</div>

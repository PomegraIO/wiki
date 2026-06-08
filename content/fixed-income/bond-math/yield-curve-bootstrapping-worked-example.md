---
title: "Bootstrapping the Spot Rate Curve: A Worked Example"
description: "Step-by-step guide to deriving zero-coupon spot rates from par-priced coupon bonds through bootstrapping spot rate curve calculations."
keywords:
  - bootstrapping spot rate curve
  - zero-coupon bonds
  - spot rates
  - bond pricing math
  - yield curve construction
image: /svg/fixed-income.svg
---

*Bootstrapping the spot rate curve is the foundational arithmetic of fixed-income pricing. By working backward from a sequence of par-priced coupon bonds, traders and analysts extract the zero-coupon **spot rates**—the discount rates that price each maturity individually. This method reveals the true shape of the yield curve and enables accurate [bond valuation](/bond/) and [interest rate risk](/interest-rate-risk/) assessment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bootstrapping Spot Rates — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">Extract zero-coupon rates by solving backward from bonds you can observe.</div>

|   |   |
|---|---|
| **Input data** | Par-priced coupon bonds at consecutive maturities |
| **Output** | Zero-coupon [spot rates](/spot-rate/) for each maturity |
| **Key equation** | Bond price = sum of discounted cash flows |
| **Assumption** | No arbitrage between spot rates |
| **Use case** | [Duration](/duration/) calculations, [valuation](/fair-value/), risk modeling |

</aside>

## Why bootstrapping matters

In real markets, Treasury bonds and corporate bonds always pay coupons—they don't come as pure zero-coupon instruments. Yet traders and risk managers need zero-coupon **spot rates** to properly discount future cash flows and compare bonds of different maturities.

Bootstrapping solves this problem. It uses the price of a coupon bond—observable in the market—to back out the implied zero-coupon rate for that maturity. By starting with the shortest-maturity bond and working forward, you build an entire spot curve.

This curve is essential because [yield-to-maturity](/yield-to-maturity/) (YTM) blurs maturities together: a bond's YTM is a single rate that discounts all its cash flows equally. But the 2-year rate and the 10-year rate should never be the same. Bootstrapping separates them.

## A worked example: three bonds

Suppose you have three par-priced Treasury bonds. "Par-priced" means the bond's market price equals its face value (100). These bonds pay annual coupons.

| Maturity | Coupon Rate | Price | Face Value |
|----------|-------------|-------|------------|
| 1 year   | 2.0%        | 100   | 100        |
| 2 years  | 3.0%        | 100   | 100        |
| 3 years  | 4.0%        | 100   | 100        |

Your goal: find the spot rates *s*₁, *s*₂, and *s*₃ for each maturity.

### Step 1: Extract the 1-year spot rate

The 1-year bond pays one cash flow: face value plus final coupon.

- Cash flow in 1 year: \$100 + (0.02 × \$100) = \$102

The bond price is:

**100 = 102 / (1 + s₁)**

Solving for *s*₁:

**(1 + s₁) = 102 / 100 = 1.02**

**s₁ = 0.02 = 2.0%**

The 1-year spot rate is 2%. This makes sense: if the bond pays 2% coupon and trades at par, the zero-coupon rate must also be 2%.

### Step 2: Extract the 2-year spot rate

The 2-year bond pays two cash flows:

- Year 1: \$3 (coupon)
- Year 2: \$100 + \$3 = \$103 (final coupon plus principal)

The bond price equation is:

**100 = 3 / (1 + s₁) + 103 / (1 + s₂)²**

You already know *s*₁ = 0.02. Substituting:

**100 = 3 / 1.02 + 103 / (1 + s₂)²**

**100 = 2.94 + 103 / (1 + s₂)²**

**97.06 = 103 / (1 + s₂)²**

**(1 + s₂)² = 103 / 97.06 = 1.0612**

**(1 + s₂) = √1.0612 = 1.0301**

**s₂ = 0.0301 = 3.01%**

The 2-year spot rate is approximately 3.01%. Notice it's higher than the 1-year rate—the curve is upward sloping.

### Step 3: Extract the 3-year spot rate

The 3-year bond pays three cash flows:

- Year 1: \$4
- Year 2: \$4
- Year 3: \$100 + \$4 = \$104

The price equation is:

**100 = 4 / (1 + s₁) + 4 / (1 + s₂)² + 104 / (1 + s₃)³**

Substitute known values:

**100 = 4 / 1.02 + 4 / (1.0301)² + 104 / (1 + s₃)³**

**100 = 3.92 + 3.77 + 104 / (1 + s₃)³**

**100 = 7.69 + 104 / (1 + s₃)³**

**92.31 = 104 / (1 + s₃)³**

**(1 + s₃)³ = 104 / 92.31 = 1.1263**

**(1 + s₃) = ∛1.1263 = 1.0405**

**s₃ = 0.0405 = 4.05%**

The 3-year spot rate is approximately 4.05%.

## Your bootstrapped curve

| Maturity | Spot Rate |
|----------|-----------|
| 1 year   | 2.00%     |
| 2 years  | 3.01%     |
| 3 years  | 4.05%     |

This upward-sloping curve tells you the market is pricing higher yields for longer-dated cash flows—a normal environment. You can now use these rates to value any other bond, strip its [duration](/duration/), or calculate [interest rate risk](/interest-rate-risk/).

## Why the order matters

Bootstrapping must proceed from shortest to longest maturity. The 1-year bond has only one cash flow, so solving for *s*₁ is trivial. The 2-year bond has two cash flows, but you've already pinned down *s*₁, leaving only *s*₂ as an unknown. The 3-year bond has three cash flows, but you've already solved for *s*₁ and *s*₂, leaving only *s*₃.

If you tried to solve for the 3-year rate before the 2-year rate, you'd have two unknowns in one equation—impossible. The sequential structure of bootstrapping is not arbitrary; it's the only way forward.

## Practical notes

In real markets, you rarely have exactly par-priced bonds at convenient annual intervals. Practitioners interpolate between observed bond prices and use more sophisticated techniques—like spline methods—to smooth the curve. [SOFR](/sofr/) and [LIBOR](/libor/) swap curves are bootstrapped from futures and swap contracts, not just bonds.

Bootstrapping also assumes no arbitrage—that the spot rates you extract are consistent with market prices and that no two bonds offer free profit. In efficient markets, this holds; in stressed conditions, it may not.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot rate](/spot-rate/) — the zero-coupon discount rate for a given maturity
- [Yield-to-maturity](/yield-to-maturity/) — the blended rate that prices a coupon bond
- [Duration](/duration/) — sensitivity of bond price to yield shifts, calculated using spot rates
- [Bond pricing](/bond/) — how spot rates discount all cash flows
- [Interest rate risk](/interest-rate-risk/) — why extracting accurate spot rates matters for risk
- [Contango](/contango/) — forward rates relative to spot rates; visible in bootstrapped curves

### Wider context

- [Treasury bond](/treasury-bond/) — the instruments typically used for bootstrapping
- [Swap](/swap/) — interest rate swaps used to extend spot curves beyond liquid bond maturities
- Fixed-income markets — where bootstrapping is a daily reality
- [Yield curve](/yield-curve/) — the visual result of bootstrapping spot rates

</div>

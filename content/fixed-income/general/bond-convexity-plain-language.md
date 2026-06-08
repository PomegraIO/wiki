---
title: "Bond Convexity in Plain Language"
description: "Understand bond convexity as the curvature in the price-yield relationship, and why it matters more in volatile rate environments."
keywords:
  - bond convexity explained simply
  - bond convexity plain language
  - duration vs convexity
  - positive negative convexity bonds
  - bond price sensitivity yield
image: "/svg/fixed-income.svg"
---

*Bond convexity is the curvature in how a bond's price changes as yields move. Because the price-yield relationship is not a straight line but a curve, the linear [duration](/bond-duration-explained/) formula understates gains when rates fall and overstates losses when rates rise. Bonds with **positive convexity** outperform the duration model in both directions; [callable bonds](/callable-bond-mechanics/) have **negative convexity**, meaning they underperform during sharp rate declines because the call option caps price appreciation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Duration is a straight-line approximation; convexity measures the curve that duration misses.</div>

|   |   |
|---|---|
| **Positive convexity** | Standard bonds; outperform duration estimate in both directions |
| **Negative convexity** | [Callable bonds](/callable-bond-mechanics/); underperform when rates fall sharply |
| **Duration only** | Accurate for tiny rate moves (~0.5%); breaks down for larger moves |
| **Convexity adjustment** | Added to duration formula: Price change ≈ −duration × Δy + 0.5 × convexity × (Δy)² |
| **High convexity** | Long maturity, low coupon, low yield; increases value in volatile markets |
| **Low convexity** | Callable bonds, short maturity, high coupon |
| **Why it matters** | Can add or subtract 1–3% of return over a single large rate move |

</aside>

## The Curve vs. the Line: Why Duration Alone Fails

Imagine plotting a bond's price against yields. If you drew a straight line using [duration](/bond-duration-explained/), you'd get the linear approximation. But the actual relationship is curved—it bends upward (convex) for most bonds, meaning the actual price sits above the line.

**Practical example:**

- Bond: 5-year maturity, 4% coupon, currently yielding 4% (trading at par, $100).
- [Modified duration](/bond-duration-explained/): 4.5 years.

**If yields fall 2% (to 2%):**
- Duration-only estimate: Price rises by 4.5 × 2 = 9%, to $109.
- Actual price: ~$109.50 (the curve bends upward).
- Gain from convexity: ~$0.50, or 0.5%.

**If yields rise 2% (to 6%):**
- Duration-only estimate: Price falls by 4.5 × 2 = 9%, to $91.
- Actual price: ~$91.50 (the curve still bends upward).
- Gain from convexity: ~$0.50, or 0.5%.

In both cases, the bond outperforms the linear forecast. This is **positive convexity**, and it's the norm for plain-vanilla bonds. The reason: as prices fall, the bond yields more (mathematically), pulling some price back up. As prices rise, the bond yields less, but the benefit of lower yield is already captured in higher price. The asymmetry creates the curve.

## Measuring Convexity

Convexity is measured as the second derivative of the price-yield relationship—essentially, "how much does the slope change as yields change?" A number around 60–100 is typical for investment-grade bonds. Higher numbers (100+) indicate greater curvature; zero means perfectly linear (no curve at all).

The full price-change formula is:

**Price change (%) ≈ −modified duration × Δy + 0.5 × convexity × (Δy)²**

For small moves (Δy < 0.5%), the convexity term is negligible. But as rate moves grow, convexity becomes material. In a 3% rate move, the convexity adjustment can swing 4.5% ((Δy)² term = 9), significantly changing the outcome.

## Positive Convexity: The Investor's Friend

Most investors instinctively prefer positive convexity because it works in their favor. When rates fall sharply, they reap larger gains than duration predicts. When rates rise sharply, losses are smaller than duration predicts. It's a "heads I win, tails I win less" outcome.

**Bonds with highest positive convexity:**
- Long maturity (20+ years)
- Low coupon (deep discount bonds, zero-coupon bonds especially)
- Low starting yield (the price has more room to move)

A 30-year zero-coupon bond, for instance, might have convexity of 500+ because its price swings wildly; a 2-year bond with a 5% coupon might have convexity under 20. In volatile markets, investors bid up prices of high-convexity bonds to lock in this embedded asymmetry.

## Negative Convexity: The Callable Bond Problem

[Callable bonds](/callable-bond-mechanics/) exhibit **negative convexity**—the price curve bends *downward*. The call option acts as an option on the issuer's side, capping the investor's upside while preserving downside.

**Callable bond example:**

- Bond: 10-year maturity, 5% coupon, currently yielding 4% (trading above par at $105), callable at 103 in 5 years.
- Modified duration: 6 years (shorter than the non-callable equivalent, ~7.5 years, because of call risk).

**If yields fall 3% (to 1%):**
- Non-callable bond would price to ~$130.
- Callable bond prices to only ~$103 because the issuer calls the bond and locks investors out of further gains.
- Loss from negative convexity: ~$27, or massive underperformance.

**If yields rise 3% (to 7%):**
- Non-callable bond prices to ~$70.
- Callable bond prices to ~$75 (the call becomes worthless, so it behaves like a non-callable bond).
- Loss is roughly symmetrical to non-callable bonds; no protection.

This asymmetry—capped gains, unprotected losses—is why investors demand higher coupons to hold callable bonds. In falling-rate environments, callable-bond investors experience the disappointing scenario: reinvested principal at much lower rates, with limited price appreciation to offset the decline.

## Convexity Across Bond Markets

**Treasury bonds** (non-callable) display standard positive convexity, with magnitudes depending on maturity and duration.

**Corporate bonds** are typically callable and exhibit slight negative convexity, though it's often hidden because quoted yields assume a held-to-maturity scenario.

**Mortgage-backed securities** ([MBS](/mortgage-backed-security/)) are a extreme case of negative convexity. As rates fall, homeowners refinance, shortening the bond's expected life (prepayment risk). As rates rise, prepayments slow, lengthening the bond. This creates severe negative convexity: "you lose on gains, lose on duration extension, and lose again on refinancing delays." MBS investors are compensated with higher yields, but convexity is a persistent drag.

**Zero-coupon bonds** have extreme positive convexity. Because all cash return arrives at maturity, the relationship between price and yield is deeply curved, creating the highest asymmetry in your favor.

## Why Volatility Amplifies Convexity Value

In stable, slowly-moving rate environments, convexity contributes little—most moves are < 1%, where duration dominates. But in volatile environments (say, 2008, 2022, or during Fed policy reversals), 2–3% rate moves are common. In those regimes:

- High-convexity bonds (long Treasuries, zeros, high-quality corporates) outperform.
- Negative-convexity bonds ([callables](/callable-bond-mechanics/), MBS) underperform.

A portfolio manager anticipating volatility might extend duration by adding long-maturity, low-coupon bonds specifically for their convexity, not just for yield. This is especially true in periods of Fed policy uncertainty, when the yield curve is steep and rate moves are large.

## The Trade-off: Yield vs. Convexity

Bonds with high positive convexity usually offer lower coupons because investors are willing to accept lower current yield for the embedded asymmetry. A 30-year zero-coupon bond is a pure bet on convexity—it pays no coupon but has enormous price upside if rates fall. A 5-year high-coupon bond offers little convexity but steady income.

Choosing between them depends on your rate outlook and risk tolerance. Expecting stable or rising rates? The high-coupon bond's yield matters more. Expecting rate volatility or eventual declines? High-convexity bonds are insurance—you pay in coupons, but you collect in outsized gains.

## See also

<div class="wiki-seealso">

### Closely related

- [Bond Duration Explained](/bond-duration-explained/) — Duration is the linear part; convexity is the curve
- [Callable Bond Mechanics](/callable-bond-mechanics/) — Negative convexity in callable bonds
- [Bond Ladder Strategy Explained](/bond-ladder-strategy-explained/) — How diversified maturities affect portfolio convexity
- [Mortgage-Backed Security](/mortgage-backed-security/) — Extreme negative convexity due to prepayment risk
- [Interest-Rate Risk](/interest-rate-risk/) — Convexity is a refinement of rate sensitivity
- [Yield-to-Maturity](/yield-to-maturity/) — Computing the yield in convexity models

### Wider context

- [Treasury Bond](/treasury-bond/) — Strong positive convexity as a safe-haven feature
- [Corporate Bond](/corporate-bond/) — Callable corporates reduce convexity vs. Treasuries
- [Market Risk](/market-risk/) — Convexity shapes portfolio risk in volatile regimes
- [Volatility Smile](/volatility-smile/) — Related concept in options pricing
- [Bond](/bond/) — Foundational bond mechanics

</div>

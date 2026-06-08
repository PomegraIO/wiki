---
title: "Government Bond Duration and Interest Rate Risk"
description: "Understand modified duration as a measure of price sensitivity for government bonds, with examples of how interest rate moves affect bonds of different maturities."
keywords:
  - government bond duration interest rate risk
  - modified duration bond price sensitivity
  - interest rate risk treasury bonds
  - bond duration calculation examples
image: "/svg/fixed-income.svg"
---

*Bond **duration** measures how sensitive a government bond's price is to changes in interest rates. **Modified duration**—the most useful version for investors—tells you the percentage price change for each 1% move in yield. A 2-year Treasury might have a duration of 1.9 years; a 10-year note, around 8.5 years. Rate rises hurt long-duration bonds much more than short ones.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Government Bond Duration and Interest Rate Risk</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Duration quantifies how much a bond's price swings when yields change.</div>

|   |   |
|---|---|
| **Modified duration** | Percentage price change per 1% change in yield |
| **Macaulay duration** | Weighted average time (in years) until you receive cash flows |
| **2-year Treasury** | Modified duration ≈ 1.9; a 1% rate rise ≈ −1.9% price drop |
| **10-year Treasury** | Modified duration ≈ 8.5; a 1% rate rise ≈ −8.5% price drop |
| **30-year Treasury** | Modified duration ≈ 18–22; a 1% rate rise ≈ −18% to −22% price drop |
| **Coupon effect** | Higher coupons = lower duration (faster cash return reduces rate sensitivity) |
| **Yield effect** | Higher yields = lower duration (bigger denominator in the calculation) |
| **Key formula** | Modified Duration = Macaulay Duration / (1 + Yield) |

</aside>

## What duration measures: the time-value summary

**Macaulay duration** is the weighted average time (in years) until you receive all your cash flows from a bond—coupons and principal repayment. A bond that pays $100 annually for two years and then $1,100 at maturity has most of its cash near the end, so its duration is close to, but slightly less than, two years. A 10-year bond stretches that average much further into the future.

**Modified duration** takes that concept and converts it into a price-sensitivity metric. It answers: "If yields rise 1%, what percentage does my bond's price fall?"

The relationship is direct and negative: higher duration means bigger price swings when rates move.

## How to think about it visually

Imagine two government bonds:

1. **A 2-year Treasury** yielding 4.0% with a modified duration of 1.9.
2. **A 10-year Treasury** yielding 4.5% with a modified duration of 8.5.

Suppose the Federal Reserve signals tighter policy and yields jump 1.0% across the board (all rates rise from their current levels by exactly 1 percentage point).

- **2-year bond:** Price falls ≈ 1.9% (a relatively modest loss).
- **10-year bond:** Price falls ≈ 8.5% (a much steeper loss).

If you own $100,000 face value of the 2-year, you lose roughly $1,900. If you own $100,000 face value of the 10-year, you lose roughly $8,500. The long-duration bond is far more vulnerable to rate moves.

## Why longer bonds have higher duration

Two factors explain this. First, a longer-maturity bond pays most of its cash flow far in the future. When rates rise, that distant cash becomes worth less in today's dollars—a bigger hit than a short-dated bond.

Second, you're locked into an old, lower coupon for longer. If you own a 10-year Treasury yielding 4%, and new 10-year Treasuries suddenly yield 5%, you can't "reinvest" your old coupon into a higher rate for another 9.5 years (you're stuck with 4%). With a 2-year bond in the same scenario, you get back your principal in two years and can reinvest at 5% for the remaining eight years. That earlier exit reduces rate sensitivity.

## A concrete example: the 2-year versus 10-year

Let's compare two real scenarios using realistic numbers.

**Scenario A: A 2-year Treasury**
- Par: $10,000
- Coupon: 4.0% annual (paid semi-annually, $200 each)
- Maturity: 2 years
- Current yield to maturity: 4.0%
- Current price: $10,000 (trading at par)
- Modified duration: 1.94 years

**Scenario B: A 10-year Treasury**
- Par: $10,000
- Coupon: 4.5% annual (paid semi-annually, $225 each)
- Maturity: 10 years
- Current yield to maturity: 4.5%
- Current price: $10,000 (trading at par)
- Modified duration: 8.53 years

Now, rates rise 1.0% instantly across all maturities.

**2-year bond after rate rise:**
- New yield: 5.0%
- New price ≈ $10,000 × (1 − 0.0194) = $9,806
- Loss: $194, or 1.94%

**10-year bond after rate rise:**
- New yield: 5.5%
- New price ≈ $10,000 × (1 − 0.0853) = $9,147
- Loss: $853, or 8.53%

The 10-year loss is more than four times larger in percentage terms, despite the same 1% rate move. This is the power—and peril—of duration.

## The inverse relationship: yields fall, bonds rally harder with longer duration

Duration is a two-way street. If yields *fall* 1%, the same calculation applies with a plus sign:

**If the 2-year yield drops 1%:**
- New price ≈ $10,000 × (1 + 0.0194) = $10,194
- Gain: $194, or 1.94%

**If the 10-year yield drops 1%:**
- New price ≈ $10,000 × (1 + 0.0853) = $10,853
- Gain: $853, or 8.53%

Long-duration bonds magnify gains when rates fall. This is why investors "reach for duration" in periods of falling rates or recession fears. But it cuts both ways: in a rising-rate environment, duration is your enemy.

## Duration varies across the curve

The modified duration of government bonds depends on three things:

1. **Maturity:** Longer maturities have higher durations, but not linearly. A 30-year Treasury doesn't have 15 times the duration of a 2-year; it might have 10–12 times. This is because the yield denominator in the modified duration formula is larger for longer bonds.

2. **Coupon rate:** Higher coupons mean lower duration. A 30-year Treasury yielding 5% has lower duration than a 30-year Treasury yielding 3% because you're collecting cash faster. Zero-coupon bonds (like very short-maturity T-bills) have durations close to their maturity (since all cash comes at the end).

3. **Yield level:** Higher yields reduce duration. A bond yielding 6% has lower duration than the same bond yielding 3%. This is purely a mathematical effect: the denominator in the modified duration formula grows with yield.

## Using duration to manage interest rate risk

Portfolio managers use duration to control rate sensitivity. If a manager expects rates to fall, she might increase her portfolio's average duration (buy longer bonds) to amplify the expected gains. If she expects rates to rise, she might shorten duration (shift to shorter bonds, bond funds, or floating-rate notes) to limit losses.

Duration also helps answer "what-if" questions: "If the Fed raises rates 0.5%, what's my bond portfolio's expected loss?" Multiply your portfolio's weighted average duration by 0.5%.

## The limits of duration: convexity

Duration is a *linear* approximation. It works well for small rate moves (±0.5%) but breaks down for large moves. A bond's price-yield relationship is actually curved (convex), not straight, so a 2% rate drop produces a larger gain than a 2% rate rise produces a loss, even with the same duration.

This is **convexity**, and it's particularly important for long-duration bonds. But for most daily use, duration alone is enough to gauge rate risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate-Risk](/interest-rate-risk/) — the broader concept of how rates affect bond prices
- [Yield-Curve](/yield-curve/) — why yields differ across maturities
- [Treasury-Note](/treasury-note/) — intermediate-term government bonds where duration shines
- [Treasury-Bond](/treasury-bond/) — long-term bonds with high duration and high rate sensitivity
- [Bond](/bond/) — fundamentals of how bonds are priced
- [Coupon-Rate](/coupon-rate/) — how coupon affects duration and price

### Wider context

- [Federal-Reserve](/federal-reserve/) — how Fed policy moves affect rates and durations
- [Inflation-Risk](/inflation-risk/) — why real yields matter despite duration risk
- [Market-Risk](/market-risk/) — interest rate risk as a component of portfolio risk
- [Yield-to-Maturity](/yield-to-maturity/) — the yield used in duration calculations

</div>

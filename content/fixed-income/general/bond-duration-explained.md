---
title: "Bond Duration Explained: What It Measures and Why It Matters"
description: "Understand what bond duration measures, how to interpret the number, and why longer-duration bonds carry greater interest-rate risk."
keywords:
  - bond duration explained
  - what does bond duration measure
  - macaulay duration
  - modified duration
  - interest rate risk bonds
image: "/svg/fixed-income.svg"
---

*Bond duration is a measure of how sensitive a bond's price is to changes in interest rates. Specifically, **duration** quantifies the weighted average time it takes to recover your initial investment through coupon payments and principal repayment—and it predicts how much the bond's price will fall if rates rise (or rise if rates fall). A 5-year duration means a 1% rise in rates will typically lower the bond's price by roughly 5%.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Duration is both a time measure and a price-sensitivity gauge; the two are intimately linked.</div>

|   |   |
|---|---|
| **Macaulay duration** | Weighted average time (in years) to recover principal and coupons |
| **Modified duration** | Price sensitivity to interest-rate changes; Macaulay ÷ (1 + yield) |
| **Price sensitivity rule** | Price change ≈ −modified duration × yield change (%) |
| **Higher duration** | Greater [interest-rate risk](/interest-rate-risk/) and higher price swings |
| **Shorter bonds** | Lower duration, lower interest-rate risk |
| **Zero-coupon bonds** | Duration equals time to maturity (no interim coupons to speed recovery) |
| **[Callable bonds](/callable-bond-mechanics/)** | Effective duration shorter than stated maturity due to call risk |

</aside>

## Why Duration Matters More Than Maturity Alone

Maturity tells you when the final payment arrives, but duration tells you when you'll truly break even. A 30-year bond paying 1% coupons recovers your money far more slowly than a 30-year bond paying 8% coupons. The high-coupon bond returns cash in the early years, lowering your effective holding period; the low-coupon bond leaves you waiting, so its duration exceeds its maturity.

This matters because interest-rate risk depends on duration, not maturity. A 10-year bond with a 4-year duration (high coupon) is safer than a 7-year bond with a 6-year duration (low coupon) in a rising-rate environment. A portfolio manager hedging against rate volatility cares far more about duration than about how many years until final maturity.

## Macaulay Duration: The Time Dimension

Macaulay duration is the weighted average of the times at which you receive each cash flow (coupon or principal). Imagine a 3-year bond paying $50 annually plus $1,000 at maturity:

| Year | Cash flow | Weight (% of PV) | Weighted years |
|------|-----------|-----------------|-----------------|
| 1 | $50 | 5% | 0.05 |
| 2 | $50 | 4.8% | 0.10 |
| 3 | $1,050 | 90.2% | 2.71 |
| | | **Total** | **2.86 years** |

Macaulay duration = 2.86 years. Even though the bond matures in 3 years, you recover your money on average after 2.86 years, because most of the principal arrives in year 3 but coupons trickle in earlier. If the coupon were higher (say, $100/year), the earlier cash flows would weigh more, and Macaulay duration would fall.

## Modified Duration: The Price-Sensitivity Measure

Modified duration converts Macaulay duration into a price-sensitivity coefficient. It answers the question: "How much will the bond's price change if yields shift?"

**Modified duration = Macaulay duration ÷ (1 + yield-to-maturity)**

If a bond has a Macaulay duration of 5 years and a yield of 4%, modified duration ≈ 5 ÷ 1.04 ≈ 4.81.

The price-sensitivity formula is:

**Approximate price change (%) = −modified duration × yield change (%)**

If modified duration is 4.81 and yields rise 1%, the bond's price falls by roughly 4.81%. If yields fall 1%, the price rises by roughly 4.81%. For larger yield moves or bonds with [high convexity](/bond-convexity-plain-language/), this approximation drifts—but it's a reliable first-pass tool.

## Duration Across Bond Types

**Government bonds and investment-grade corporates** typically have durations ranging from 2 to 8 years, depending on maturity and coupon. A 10-year Treasury with a 3.5% yield might have a modified duration of 7.5 years, making it moderately sensitive to rate moves.

**Short-duration bonds**—floating-rate notes, high-coupon bonds, bonds maturing soon—carry durations under 2 years. They hedge against rising rates because their prices barely move when yields shift.

**Long-duration bonds**—30-year zero-coupon bonds, deeply discounted long-term corporates—can have durations exceeding 20 years, making them extremely sensitive to rate changes. These bond types are [high-convexity](/bond-convexity-plain-language/) instruments and can deliver outsized gains when rates fall sharply.

## Duration and Reinvestment Risk

Duration also hints at reinvestment risk. A bond with a 5-year duration returns principal and interim coupons over roughly 5 years. If rates fall while you hold it, the coupons you receive must be reinvested at lower rates. If rates rise, reinvestment at higher rates is possible. This interplay—price falling when rates rise, but future coupons reinvested at higher rates—partially offsets the price loss over time. Duration does not directly measure this trade-off, but it highlights why a diversified [bond ladder](/bond-ladder-strategy-explained/) can smooth both price and reinvestment outcomes.

## The Limits of Duration

Duration is most accurate for small, immediate shifts in yield. For a 2% change or larger, or for bonds with [call provisions](/callable-bond-mechanics/), convexity becomes important. Duration also assumes a parallel shift in the yield curve; in reality, long and short rates can move by different amounts, and duration doesn't capture that complexity.

Despite these limits, duration remains the single most important metric for understanding interest-rate sensitivity. Bond traders, portfolio managers, and individual investors all rely on it to anticipate portfolio movements and construct appropriate risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Bond Convexity in Plain Language](/bond-convexity-plain-language/) — How curvature in the price-yield relationship goes beyond duration
- [Callable Bond Mechanics](/callable-bond-mechanics/) — Why call provisions shorten effective duration
- [Interest-Rate Risk](/interest-rate-risk/) — The core risk that duration measures
- [Yield-to-Maturity](/yield-to-maturity/) — The discount rate used in duration calculations
- [Bond Ladder Strategy Explained](/bond-ladder-strategy-explained/) — How staggered maturities reduce reinvestment and interest-rate risk
- [Bond](/bond/) — Foundational structure and terminology

### Wider context

- [Corporate Bond](/corporate-bond/) — Duration varies widely across credit qualities
- [Treasury Bond](/treasury-bond/) — Government bonds as a duration reference
- [High-Yield Bond](/high-yield-bond/) — Shorter effective duration due to call risk
- [Fixed-Rate Mortgage (Personal)](/fixed-rate-mortgage-personal/) — Mortgages as negative-duration assets
- [Market Risk](/market-risk/) — How interest-rate risk fits into portfolio risk

</div>

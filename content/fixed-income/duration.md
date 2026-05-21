---
title: "Duration"
description: "Duration is a measure of a bond's sensitivity to interest-rate changes. It measures the weighted average time until cash flows are received."
keywords:
  - duration
  - macaulay duration
  - modified duration
  - interest rate risk
  - bond sensitivity
image: "/svg/fixed-income.svg"
---

*The **duration** of a bond measures how sensitive its price is to changes in interest rates. More formally, duration is the weighted average time until the bondholder receives all cash flows (coupons and principal). A bond with a 5-year duration loses approximately 5% in value when interest rates rise 1%; it gains approximately 5% when rates fall 1%.*

<div class="wiki-hatnote">

For the curvature in the price-yield relationship, see [convexity](/convexity/). For the interest-rate risk itself, see [bond duration risk](/bond-duration-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration — key facts</div>

<img src="/svg/fixed-income.svg" alt="A graph showing bond price sensitivity to yield changes" />

<div class="wiki-infobox-caption">Duration measures how much a bond's price changes when yields move.</div>

|   |   |
|---|---|
| **What it is** | Sensitivity to interest-rate changes |
| **Measurement** | Years; weighted average time to cash flow |
| **Modified duration** | Adjusts Macaulay duration for the yield level |
| **Effective duration** | Accounts for option-adjusted spreads for complex bonds |
| **Price rule** | Price change ≈ -duration × yield change |
| **Zero-coupon bond** | Duration = maturity |
| **Coupon bond** | Duration < maturity (due to interim coupons) |
| **Higher coupon** | Lower duration (cash returned sooner) |
| **Portfolio duration** | Weighted average of holdings' durations |

</aside>

## Macaulay duration and the weighted average concept

**Macaulay duration** is the weighted average time until you receive all cash flows. For a 10-year bond paying semi-annual coupons, Macaulay duration might be 7 years — meaning on average, you receive your cash flows in 7 years (not 10).

The weighting reflects the timing of cash flows. Early coupons (received soon) have low weight; the principal repayment (received at year 10) has high weight.

For a [zero-coupon bond](/zero-coupon-bond/), duration equals maturity (all cash flow received at maturity). For a high-coupon bond, duration is much shorter than maturity (many coupons returned early).

## Modified duration and price sensitivity

**Modified duration** converts Macaulay duration into a price sensitivity measure. It answers the question: "If yields rise 1%, how much does the bond price fall?"

The formula is: **Price change (%) ≈ -modified duration × yield change**

Example: A bond with modified duration of 5 will:
- Lose 5% in value if yields rise 1%
- Gain 5% in value if yields fall 1%
- Lose 10% in value if yields rise 2%

This makes duration the primary measure for understanding interest-rate risk in bond portfolios.

## Duration vs. maturity

Duration and maturity are different:

- **Maturity** = the date the bond matures
- **Duration** = the weighted average time to cash flows

A 10-year bond with a 4% [coupon](/coupon-rate/) has duration of approximately 8.5 years. A 10-year bond with an 8% [coupon](/coupon-rate/) has duration of approximately 7 years (shorter, because coupons are received earlier).

This matters for interest-rate risk. A 10-year 8% coupon bond is less sensitive to rate changes than a 10-year 4% coupon bond, despite having the same maturity.

## Duration of portfolios

For a portfolio of bonds, the portfolio duration is the weighted average of the bond durations. A $100M portfolio with 50% in 5-year duration bonds and 50% in 10-year duration bonds has portfolio duration of 7.5 years.

This is useful for liability matching. An insurance company with liabilities due in 10 years can buy bonds with 10-year duration, ensuring that portfolio returns match the liability timeframe.

## Negative duration

Some securities have negative duration — their prices rise when yields rise. [Inverse-floating-rate bonds](/bond-duration-risk/) are an example. These are rare and used primarily for hedging.

## Duration and convexity

Duration measures the linear relationship between price and yield. But the relationship is curved — bonds have **positive [convexity](/convexity/)**, meaning they gain more in price when rates fall than they lose when rates rise (by the same amount).

For large rate moves, [convexity](/convexity/) becomes important. For small moves, duration dominates.

## Effective duration for complex bonds

For [callable bonds](/callable-bond/) and other complex securities, **effective duration** accounts for the option-adjusted characteristics. A [callable bond](/callable-bond/) has shorter effective duration than a straight bond because the call option limits upside when rates fall.

## Portfolio management use

Bond managers use duration actively:

- **Rising-rate environment** — Reduce portfolio duration (buy shorter-duration bonds) to minimize losses
- **Falling-rate environment** — Increase portfolio duration (buy longer-duration bonds) to maximize gains
- **Liability matching** — Match portfolio duration to liability duration to immunize the portfolio

## Key rate duration

For a portfolio manager, "key rate duration" measures sensitivity to specific parts of the [yield curve](/yield-curve/). A portfolio might have 5-year key rate duration of +2 and 10-year key rate duration of -1, reflecting different sensitivities across the curve.

## See also

<div class="wiki-seealso">

### Closely related

- [Convexity](/convexity/) — curvature in the price-yield relationship
- [Bond duration risk](/bond-duration-risk/) — the interest-rate risk duration measures
- [Callable bond](/callable-bond/) — complex duration due to call option
- [Yield to maturity](/yield-to-maturity/) — affects duration calculations
- [Interest rate](/interest-rate/) — what duration measures sensitivity to

### Wider context

- [Bond](/bond/) — debt securities in general
- [Central bank](/central-bank/) — monetary policy affects rates and duration risk
- [Portfolio management](/hedge-fund/) — duration is core to bond portfolio management
- [Yield curve](/yield-curve/) — duration varies across the curve
- [Diversification](/diversification/) — duration is one form of portfolio risk

</div>

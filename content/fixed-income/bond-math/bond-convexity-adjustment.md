---
title: "Convexity Adjustment: Improving Duration-Based Price Estimates"
description: "Convexity adjustment refines bond price estimates by correcting for the curvature that duration alone misses in large yield movements."
keywords:
  - convexity adjustment bond price
  - duration and convexity
  - bond price sensitivity
  - yield curve curvature
  - fixed income valuation
image: "/svg/fixed-income.svg"
---

*A **convexity adjustment** corrects the error that creeps into duration-only bond price forecasts when yields move sharply. Since duration assumes a linear relationship between yield and price, it undercounts gains when yields fall and overcounts losses when yields rise. Adding a convexity correction term—a simple quadratic adjustment—restores accuracy for large moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity Adjustment — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Convexity adjustments matter most for large yield changes or long-dated bonds.</div>

|   |   |
|---|---|
| **What it corrects** | The curvature missed by linear duration estimates |
| **Formula term** | ½ × Convexity × (ΔY)² |
| **When it matters** | Yield moves > 50 basis points |
| **Direction** | Always adds back gains; asymmetric in practice |
| **Related metric** | [Duration](/duration/) measures linear price sensitivity |

</aside>

## Why duration alone falls short

A bond's [duration](/duration/) measures its effective time-to-maturity weighted by cash flows. At any yield level, duration gives you the percentage price change per 1% (100 basis point) yield move. For small moves—say 5 or 10 basis points—this linear approximation works beautifully. But for large moves (100+ basis points), the true price curve bends.

This happens because bond prices follow a convex relationship to yield. When yields fall 200 basis points, a bond's price rises more than duration alone predicts. When yields rise 200 basis points, the price falls less than duration predicts. That asymmetry is pure geometry: the slope of the price-yield line steepens as yields fall (you get paid more for the time value of each coupon) and flattens as yields rise (each coupon is less valuable in real terms).

Duration captures the slope at one point. Convexity captures the rate at which that slope changes—the curvature. Together, they let you estimate the price change for any size move.

## The convexity adjustment formula

The price change formula breaks into two parts:

**ΔPrice = −Duration × ΔY + ½ × Convexity × (ΔY)²**

The first term is what you already know: duration times the yield change (in decimal form). The second term is the convexity adjustment. It is always positive—whether yields go up or down—because (ΔY)² is always positive. That positive term reflects the fact that bond prices curve favorably either direction.

For example, if a bond has a duration of 5 years and a convexity of 30, and yields fall by 200 basis points (0.02 in decimal):
- Duration effect: −5 × (−0.02) = +0.10 or +10%
- Convexity adjustment: ½ × 30 × (0.02)² = 0.006 or +0.6%
- Total price change: +10.6%

Without the convexity term, you'd have forecast only +10%. The 0.6% extra comes from the bond's favorably curved response.

## Computing convexity

Convexity is calculated as the second derivative of bond price with respect to yield, normalized by price. For a standard coupon bond, you can compute it directly from the cash flow schedule:

**Convexity = Σ [ t(t+1) × CF_t / (1 + y)^(t+2) ] / Price**

where CF_t is the cash flow in period t, y is the yield per period, and t runs from 0 to maturity. The numerator weights each cash flow by the product of its time period and the next time period—a heavier emphasis on distant cash flows—and discounts it all back.

Alternatively, many practitioners use duration convexity approximations. For a bullet bond (single maturity), higher convexity comes from:
- **Longer maturity**: longer bonds are more convex
- **Lower coupon**: zero-coupon bonds have very high convexity relative to high-coupon bonds at the same maturity, because all the cash arrives at the end
- **Lower yield**: out-of-the-money bonds curve more sharply than in-the-money ones

## When the adjustment matters in practice

For yield moves under 50 basis points, the convexity adjustment is trivial—usually less than 0.1% of price. Most daily trading doesn't justify the calculation.

But trading desks routinely account for convexity when:
- **Macro volatility erupts**: the Fed signals a 100+ basis point shift in rates, and portfolio managers hedge with convexity-aware models
- **Steepening or flattening trades**: betting on yield curve reshaping often involves large moves in particular tenors
- **Long-duration portfolios**: pension funds and insurers hold 10–30 year bonds; a 50 basis point move causes 5–15% price swings where convexity adds meaningful precision

Central banks and large institutional traders also use convexity to price bonds over multi-month horizons and to understand tail risk. For a 10-year bond with a coupon of 4%, the convexity is typically in the range of 80–120, meaning a 200 basis point shock picks up an extra 0.6–1.2% of upside—a real effect worth modeling.

## Convexity and callable bonds

The convexity adjustment breaks down for [callable bonds](/bond/) and other bonds with embedded options. When yields fall and prices would normally soar, the issuer may redeem the bond to refinance at lower rates. That call option limits upside—the bond's price flattens instead of curving up. The bond displays **negative convexity**: price gains slow as yields fall further, and price losses accelerate as yields rise.

For callable bonds, valuation requires option-adjusted spread (OAS) models and scenario analysis rather than a simple convexity number. The asymmetry is real but driven by the issuer's option, not the mathematics of the bond alone.

## Key insight: the asymmetry is mild for plain bonds

For bullet bonds without embedded options, convexity always works in the bondholder's favor. A 200 basis point move in either direction delivers a convexity bonus. The adjustment is typically 0.3–1.5% of price for realistic moves, depending on duration and coupon. It matters for risk management and relative-value decisions, but it is not a trading signal by itself—it is a correction that helps you forecast bond prices accurately when big moves occur.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — linear measure of a bond's price sensitivity to yield changes
- [Bond](/bond/) — foundational term; covers coupon, yield, maturity, and plain-vanilla mechanics
- [Yield-to-Maturity](/yield-to-maturity/) — the discount rate that equates a bond's cash flows to its market price
- [Interest-Rate-Risk](/interest-rate-risk/) — how price volatility rises with duration and decreases with convexity
- [DV01](/dv01/) — the dollar value of one basis point; related to duration and used in hedging

### Wider context

- [Par-Yield-vs-Spot-Rate](/par-yield-vs-spot-rate/) — how par yields and spot rates relate to bond pricing
- [Bond-Basis-Points-Value](/bond-basis-points-value/) — pricing at the basis-point level
- [Flat-Price-vs-Full-Price](/flat-price-vs-full-price/) — settlement price mechanics
- [Credit-Risk](/credit-risk/) — credit spread changes interact with duration and convexity
- [Discounted-Cash-Flow-Valuation](/discounted-cash-flow-valuation/) — the foundational bond pricing framework

</div>

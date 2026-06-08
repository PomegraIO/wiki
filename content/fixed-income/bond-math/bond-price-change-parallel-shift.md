---
title: "Bond Price Change from a Parallel Yield Curve Shift"
description: "How to estimate bond price changes when all yields shift by the same amount, using duration and convexity to calculate price and percentage impact."
keywords:
  - bond price change parallel shift
  - yield curve shift duration
  - bond duration calculator
  - convexity bond pricing
  - interest rate sensitivity bond
image: /svg/fixed-income.svg
---

*When the entire [yield curve](/yield-curve/) shifts up or down by the same amount—a **parallel shift**—every bond's price moves inversely to yields. Using [duration](/duration/) and convexity, you can quickly estimate the dollar and percentage price change without repricing every cash flow.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Parallel Yield Curve Shift — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Duration and convexity together estimate price changes from parallel yield shifts with high accuracy for small moves.</div>

|   |   |
|---|---|
| **Parallel shift** | All yields move by the same basis points (e.g., all rates +50 bps) |
| **Duration rule** | Price ≈ −Duration × ∆Yield × Price (linear approximation) |
| **Convexity adjustment** | Price ≈ ½ × Convexity × (∆Yield)² × Price (captures curvature) |
| **Combined formula** | ∆Price% ≈ −Duration × ∆Yield + ½ × Convexity × (∆Yield)² |
| **Duration units** | Measured in years; modified duration = duration ÷ (1 + yield) |
| **Convexity** | Positive for standard bonds; larger for lower-coupon, longer-maturity bonds |
| **Accuracy range** | Within 1–2% for ±100 bps shifts; less accurate for >200 bps moves |

</aside>

## Duration: The Linear Price Approximation

The [duration](/duration/) of a bond measures its effective maturity—how long it takes, on a weighted basis, for the bondholder to recover their investment. More importantly, duration tells you how much the bond's price will change for a small change in yield.

**Modified duration** (often just "duration" in practice) is defined as:

$$\text{Modified Duration} = \frac{\text{Macaulay Duration}}{1 + \text{YTM}}$$

And it directly gives you the price sensitivity:

$$\Delta \text{Price}\% \approx -\text{Duration} \times \Delta \text{Yield}$$

### A Simple Example

Suppose you own a 10-year, 4% coupon bond trading at par ($1,000), with a modified duration of 8.5 years. The yield-to-maturity is 4%.

If yields rise by **50 basis points** (0.5%), the price falls by:

$$\Delta \text{Price}\% \approx -8.5 \times 0.005 = -0.0425 = -4.25\%$$

So the bond price drops to roughly $1,000 × (1 − 0.0425) = $957.50.

If yields *fall* by 50 basis points, the price rises by 4.25% to $1,042.50.

This linear approximation works well for small yield changes (±50 to 100 basis points). For larger moves, it breaks down because bond pricing is **convex**, not linear.

## Why the Linear Model Breaks Down: Convexity

A bond's price-yield relationship is curved, not straight. When yields fall, prices rise by slightly *more* than the duration rule predicts. When yields rise, prices fall by slightly *less* than duration predicts. This curvature is **convexity**.

Convexity arises because each unit decrease in yield compounds the price gain—the reinvested coupons also benefit from lower yields. Each unit increase in yield compounds the price loss. The effect is small for small moves but becomes material (1–2%) for shifts larger than 100 basis points.

Convexity is always positive for standard, non-callable bonds (every bond benefits from falling yields and only partly suffers from rising yields). It's larger for:

- **Lower-coupon bonds** (more cash concentrated at maturity, farther in the future)
- **Longer-maturity bonds** (greater time horizon for the nonlinear effect to compound)
- **Lower-yielding bonds** (the denominator in the modified duration formula is smaller, amplifying the duration term and the associated convexity)

## The Full Formula: Duration + Convexity

To estimate a bond's price change accounting for convexity:

$$\Delta \text{Price}\% \approx -\text{Duration} \times \Delta \text{Yield} + \frac{1}{2} \times \text{Convexity} \times (\Delta \text{Yield})^2$$

The first term is duration (linear, negative). The second is the convexity adjustment (quadratic, always positive).

### A Larger Shift Example

Using the same bond (duration 8.5, convexity ~75):

**If yields rise by 150 basis points:**

$$\Delta \text{Price}\% \approx -8.5 \times 0.015 + \frac{1}{2} \times 75 \times (0.015)^2$$
$$= -0.1275 + 0.0084 = -0.1191 = -11.91\%$$

Duration alone would predict a 12.75% loss. Convexity reduces it to 11.91%—a 0.84 percentage point gain from the bond's built-in convexity protection.

**If yields fall by 150 basis points:**

$$\Delta \text{Price}\% \approx -8.5 \times (-0.015) + \frac{1}{2} \times 75 \times (-0.015)^2$$
$$= 0.1275 + 0.0084 = 0.1359 = 13.59\%$$

The bond gains more than the 12.75% duration rule predicts—the extra 0.84% comes from convexity.

## Why Parallel Shifts Matter

In reality, yield curves don't always shift in parallel. The 2-year yield might rise 75 bps while the 10-year rises 50 bps (a flattening). Long-dated bonds would be less affected than the parallel shift model predicts.

But parallel shifts do occur, especially:

- During large monetary policy moves (central bank rate hikes or cuts)
- During broad flight-to-quality episodes (all rates rise together)
- Over short horizons in calm markets

When they do happen, the duration-plus-convexity formula is accurate and fast—no need to reprice every cash flow.

## Practical Use in Portfolio Management

Bond traders and portfolio managers use this formula for:

1. **Hedge sizing.** How many Treasury futures should I buy to hedge my corporate bond exposure if rates rise 75 bps? Use duration to calculate the notional exposure.
2. **Risk estimation.** What's my portfolio's interest rate risk? Duration × portfolio value × expected yield move.
3. **Scenario analysis.** "If the Fed raises 100 bps, my bond portfolio loses roughly…" (use duration + convexity for a fast answer).
4. **Convexity trading.** Long convexity is valuable; some investors pay a price premium for higher-convexity bonds in volatile markets.

## Limitations and When to Reprice

The duration-convexity approximation is accurate within ±1–2% for yield moves up to 100–150 basis points. Beyond that:

- **Large moves** (>200 bps) should be repriced fully.
- **Option-embedded bonds** (callable bonds, mortgage-backed securities) have negative convexity and behave differently than the formula predicts; they require full repricing.
- **Credit spread changes** happen alongside yield curve shifts. A falling yield curve might trigger credit tightening (spreads widen), partially offsetting the price gain from lower yields. Duration captures only the interest-rate component.

For most standard bonds in normal market conditions, duration and convexity are the workhorses of bond risk and return estimation.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the foundation of bond price sensitivity measurement
- [Yield-to-Maturity](/yield-to-maturity/) — the yield used to calculate price sensitivity
- [Yield Curve](/yield-curve/) — the set of yields across maturities; parallel shifts are one scenario
- [Bond](/bond/) — the foundational instrument; cash flows and pricing
- [Interest Rate Risk](/interest-rate-risk/) — the broader risk of rising or falling yields
- [Coupon Payment](/coupon-payment/) — the cash flows that determine duration and convexity

### Wider context

- [Bond Price Change from a Parallel Yield Curve Shift](/bond-price-change-parallel-shift/) — the specific focus of this article
- [Fixed Income](/bond/) — bonds as an asset class
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the underlying principle of bond pricing
- [Basis Risk](/basis-risk/) — how bond values and yields can diverge from expectations
- [Credit Risk](/credit-risk/) — the risk that issuer default changes bond value

</div>

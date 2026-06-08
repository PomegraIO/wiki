---
title: "Convexity Adjustment for Large Yield Changes"
description: "Why linear duration approximation fails for large yield moves, and how convexity corrects bond price forecasts."
keywords:
  - convexity adjustment yield
  - convexity bond formula
  - duration convexity
  - bond price estimation
  - yield curve risk
  - negative convexity
---

*A bond's price moves inversely to yields, but not in a straight line. When yields drop sharply, [duration](/duration/) alone systematically underestimates the price gain; when yields spike, it overstates the loss. **Convexity adjustment for large yield changes** quantifies this curvature and corrects the forecast.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity Adjustment — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Duration is the tangent line to the bond price curve; convexity accounts for the curve itself.</div>

|   |   |
|---|---|
| **Duration effect** | Price change ≈ −Duration × Yield change (first-order, linear) |
| **Convexity effect** | Adds curvature correction: ½ × Convexity × (Yield change)² |
| **Full formula** | ΔPrice% = −Duration × ΔYield + ½ × Convexity × (ΔYield)² |
| **Sign of convexity** | Positive convexity = bondholders gain when rates move; negative = they lose on big moves |
| **Practical threshold** | Convexity matters most when yield moves exceed ±100 basis points |

</aside>

## Why duration alone fails at large yield movements

The relationship between a bond's price and its [yield-to-maturity](/yield-to-maturity/) is mathematically curved, not linear. Duration captures the *slope* of this curve at the current yield level—a useful approximation for small shifts. But as yield changes grow, the linear approximation diverges from reality.

Consider a 10-year, 5% coupon bond trading at par (100), with a duration of roughly 8 years. If yields fall by 1% (100 basis points), duration predicts a price gain of 8%. The actual price gain will be *larger*—say, 8.25%—because the price-yield curve is convex (bends upward). Conversely, a 1% rise in yields predicts an 8% loss, but the actual loss will be *smaller*—perhaps 7.75%—again due to convexity.

This asymmetry is not coincidence. Bond prices exhibit *positive convexity*: gains from favorable yield moves exceed losses from equally-sized unfavorable moves. (Some instruments, like [mortgage-backed securities](/mortgage-backed-security/), exhibit negative convexity, where the asymmetry runs the other way.)

## The convexity adjustment formula

The full price change from a yield move combines two terms:

**ΔPrice% = −Duration × ΔYield + ½ × Convexity × (ΔYield)²**

The first term is the familiar duration effect. The second term is the **convexity adjustment**: it quantifies the curvature contribution and *always* has the same sign as convexity.

Convexity is a measure of the bond's price sensitivity curve. For a standard bond, it is calculated as the weighted average of the maturity squared of all cashflows, scaled by the bond's current price and yield. The exact formula is technical, but the intuition is simple: longer-duration bonds exhibit greater convexity because their cashflows are spread further into the future, amplifying the curvature effect.

## A worked example: 10-year bond with 1% yield drop

**Bond details:**
- 10-year maturity, 5% annual coupon
- Current price: 100 (par), current yield: 5%
- Duration: 7.9 years
- Convexity: 68 (a typical value for a plain vanilla bond)

**Scenario: Yields fall from 5% to 4% (−100 bps)**

**Duration effect alone:**
- ΔPrice% = −7.9 × (−0.01) = +0.079 or +7.9%

**Convexity adjustment:**
- ½ × 68 × (−0.01)² = ½ × 68 × 0.0001 = 0.0034 or +0.34%

**Total price change:**
- +7.9% + 0.34% = +8.24%

In this case, duration underestimated the gain by 34 basis points of return. For a large portfolio, this omission compounds into material tracking error.

## The same bond: 1% yield increase

**Scenario: Yields rise from 5% to 6% (+100 bps)**

**Duration effect alone:**
- ΔPrice% = −7.9 × (+0.01) = −0.079 or −7.9%

**Convexity adjustment:**
- ½ × 68 × (+0.01)² = ½ × 68 × 0.0001 = 0.0034 or +0.34%

**Total price change:**
- −7.9% + 0.34% = −7.56%

Duration overstated the loss by 34 basis points because convexity *offsets* the downside move. This is the beneficial aspect of positive convexity: you lose less than duration predicts when yields rise, and gain more when they fall.

## When convexity matters most

For small yield moves (±25 basis points), the convexity term is negligible. A 25 bps move squared (0.0025²) is 0.0000063, so convexity's contribution shrinks to less than 1% of the duration effect. But as moves grow:

- **±50 bps**: Convexity contribution ≈ 8–12% of duration effect
- **±100 bps**: Convexity contribution ≈ 30–40% of duration effect
- **±200 bps**: Convexity contribution ≈ 100%+ of duration effect

Portfolio managers and traders routinely ignore convexity for routine forecasts, but when yield curve reshaping is expected—say, a sudden shift in [monetary policy](/monetary-policy/) or a major [credit event](/credit-event-sovereign/)—omitting convexity introduces material risk.

## Negative convexity and the mortgage trap

Not all bonds exhibit positive convexity. [Mortgage-backed securities](/mortgage-backed-security/) and callable bonds have embedded [call options](/call-option/): when yields fall sharply, borrowers refinance (exercising the embedded call), capping the bondholder's upside. Meanwhile, when yields rise, borrowers hold the loan, extending duration. This creates *negative convexity*.

In mathematical terms, the borrower's option subtracts from the bond's raw convexity. For a mortgage-backed security, the convexity term becomes negative, so the formula becomes:

**ΔPrice% = −Duration × ΔYield − ½ × |Convexity| × (ΔYield)²**

Negative convexity is a hidden cost: you gain less than duration predicts when yields fall, and lose more when they rise. This asymmetry is why callable bonds and mortgages trade at [credit spreads](/credit-spread/) that compensate for the option's value.

## Measuring convexity in practice

Convexity is not observable; it must be calculated from the bond's cashflow structure. Most financial calculators and bond-pricing platforms report it alongside duration. Some define convexity in "years squared" (a precise mathematical definition); others normalize it as a decimal percentage (convexity ÷ 100, to make the adjustment term unit-consistent with duration).

When comparing bonds, *pay attention to the convexity definition*. A bond listed with convexity of 68 (years squared) and another with 0.68 (normalized decimal) are the same security; the adjustment term must be scaled accordingly.

## Strategic implications

Investors who anticipate large [interest-rate](/interest-rate/) moves should favor securities with positive convexity. In a scenario where rates are expected to fall significantly, a longer-duration bond with high convexity will outperform one with low convexity, capturing both the duration gain and the convexity bonus.

Conversely, in a period of high yield-curve uncertainty—where large moves are possible but direction unknown—positive convexity acts as insurance, reducing downside while preserving upside.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the linear approximation convexity refines
- [Yield-to-maturity](/yield-to-maturity/) — the yield metric convexity adjusts for
- [Interest-rate risk](/interest-rate-risk/) — the broader risk convexity addresses
- [Bond price](/bond/) — the market price convexity predicts
- [Call option](/call-option/) — the embedded option creating negative convexity
- [Credit spread](/credit-spread/) — the compensation for negative convexity in callable securities

### Wider context

- [Treasury bond](/treasury-bond/) — the baseline low-convexity instrument
- [Mortgage-backed security](/mortgage-backed-security/) — the classic negative-convexity case
- [Bond ETF](/bond-etf/) — how convexity affects portfolio performance
- [Yield curve](/yield-curve/) — the environment where convexity adjustments matter

</div>
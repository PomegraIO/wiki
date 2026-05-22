---
title: "Modified Duration"
description: "Measure of a bond's sensitivity to interest rate changes, expressed as the percentage price change for a 1% yield shift."
keywords:
  - duration
  - interest rate risk
  - bond sensitivity
  - yield elasticity
---

*The **modified duration** of a [bond](/wiki/bond/) is the percentage change in its price for every 1 percentage point change in [yield](/wiki/yield-to-maturity/), accounting for the convexity of the bond price-yield relationship.*

Bond prices and yields are inversely related: when interest rates rise, bond prices fall, and vice versa. The question is by how much. A 10-year Treasury might drop 5% if yields jump from 3% to 4%, while a 30-year bond might drop 10%. Modified duration quantifies that sensitivity, making it a crucial tool for bond portfolio management and risk assessment.

<aside class="wiki-infobox">

| Measure | Definition | Use |
|---------|-----------|-----|
| **Macaulay duration** | Weighted-average time to receive cash flows | Theoretical measure; not practical |
| **Modified duration** | Macaulay duration / (1 + yield); % price change per 1% yield shift | Primary risk measure for bonds |
| **Effective duration** | Empirical measure from actual price moves | Used for bonds with embedded options |
| **Key rate duration** | Sensitivity to specific yield curve points | Used for curve positioning |

</aside>

## Macaulay duration and the leap to modified

**Macaulay duration** is the weighted-average time until a bondholder receives all cash flows (coupons and principal). A 5-year bond with annual coupons has a Macaulay duration of roughly 4.5 years (less than 5 because you receive coupons before maturity). For a zero-coupon bond, Macaulay duration equals maturity.

Macaulay duration is intuitive but not directly actionable for pricing. **Modified duration** translates it into a price sensitivity measure. The formula is:

Modified Duration = Macaulay Duration / (1 + Yield)

For a bond with Macaulay duration of 5 years and a yield of 4%, modified duration is 5 / 1.04 = 4.81 years. This means the bond price changes by approximately 4.81% for every 1% move in yield.

## The interpretation: 1% yield shift

A bond with a modified duration of 5 will lose 5% in value if yields rise by 1%. Conversely, it will gain 5% if yields fall by 1%. For a $1 million position, a 1% yield move translates to a $50,000 move.

This linear approximation works well for small moves (±0.5%). For larger moves, you must account for [convexity](/wiki/convexity/) — the curvature of the bond price-yield relationship. A bond with positive convexity gains more than the linear estimate when yields fall, and loses less when yields rise.

## Duration and bond characteristics

**Longer maturity = longer duration.** A 30-year bond has much longer duration than a 2-year bond, so it is more sensitive to rate moves.

**Higher coupon = shorter duration.** A 6% coupon bond has shorter duration than a 2% coupon bond of the same maturity, because you receive more cash early (reducing weighted-average time to cash flow). Conversely, zero-coupon bonds have very long duration relative to their maturity.

**Higher yield = shorter duration.** If yields are high (say, 8%), the denominator in the modified duration formula is larger, so the duration is smaller. This creates a negative feedback: when yields spike up in a crisis, duration falls, dampening some of the price sensitivity. When yields are low (say, 1%), duration is very long, making bonds super-sensitive to any rate rise.

## Effective duration and embedded options

Some bonds have embedded options: a **callable bond** can be prepaid by the issuer; a **putable bond** can be redeemed early by the investor. These options distort the relationship between yield and price.

For a callable bond, if rates fall sharply, the issuer will likely call it, capping your upside. The price does not rally as much as it would for a non-callable bond, so effective duration is shorter. **Effective duration** measures actual price sensitivity, accounting for the behavior of these embedded options. You calculate it by modeling the bond's price under various yield scenarios and measuring the slope.

For a putable bond, you can force the issuer to redeem at a fixed price if yields rise, which effectively caps your downside. Effective duration is shorter on the downside.

## Portfolio duration and rate moves

Portfolio managers use duration to estimate portfolio [interest-rate risk](/wiki/interest-rate-risk/). If your bond portfolio has an average modified duration of 6 years and yields rise by 1%, the portfolio will fall roughly 6% in value. This is a key risk metric, often reported alongside [beta](/wiki/beta/) in equity portfolios.

When yields are expected to rise, managers shorten duration by shifting to shorter-maturity bonds or floating-rate notes. When yields are expected to fall, managers lengthen duration to capture gains.

## Duration and bond prices: the math

The bond price formula is:

Price = Σ [Coupon / (1 + y)^t] + [Par / (1 + y)^n]

Where y is the yield, t is the period number, and n is the total number of periods. As y increases (yields rise), the denominators grow, and price falls. The slope of this curve at any yield level is the negative of modified duration.

The second derivative (curvature) is positive for typical bonds, which is [positive convexity](/wiki/positive-convexity/). This means:
- Price falls less than duration predicts when yields rise (because you are moving down the convex curve).
- Price gains more than duration predicts when yields fall.

## Negative convexity: the mortgage problem

Mortgage-backed securities (MBS) have negative convexity. When yields fall and homeowners refinance, the MBS holder's cash flow accelerates, capping the price gain. When yields rise, refinancing slows, extending the duration and worsening the loss. This is called [extension risk](/wiki/extension-risk/). The effective duration of an MBS is uncertain and changes with rates, making them riskier than their stated duration suggests.

## Currency and [credit](/wiki/credit-risk/) duration

Duration is sometimes extended to other risks. **Credit duration** measures sensitivity to credit-spread changes: if the credit spread on a corporate bond widens by 1%, the price falls by X%. **Currency duration** (or [forex](/wiki/forex-spread/) duration) measures sensitivity to currency moves for foreign bonds held by a domestic investor.

## Practical use in portfolio construction

Investors often target a specific portfolio duration to match their liability stream. A pension fund with obligations due in 10 years might hold bonds with an average duration of 10, so that a decline in asset values is offset (approximately) by a decline in liability values. This is [immunization](/wiki/interest-rate-risk/).

Active managers adjust duration tactically: shorten when they expect rates to rise, lengthen when they expect rates to fall. Over many cycles, tactical duration moves add value, though the track record is mixed.

<div class="wiki-seealso">

### Closely related
- [Duration](/wiki/duration/) — General concept of bond sensitivity
- [Macaulay duration](/wiki/macaulay-duration/) — Weighted-average time to cash flows
- [Effective duration](/wiki/effective-duration/) — Empirical duration accounting for embedded options
- [Convexity](/wiki/convexity/) — The curvature of the bond price-yield relationship
- [Yield to maturity](/wiki/yield-to-maturity/) — The discount rate used in duration calculations

### Wider context
- [Bond](/wiki/bond/) — The security underlying duration analysis
- [Interest rate risk](/wiki/interest-rate-risk/) — The risk that modified duration quantifies
- [Bond-duration-risk](/wiki/bond-duration-risk/) — Portfolio-level implications of duration exposure
- [Immunization](/wiki/interest-rate-risk/) — Matching duration to liabilities
- [Extension risk](/wiki/extension-risk/) — Duration uncertainty in MBS

</div>

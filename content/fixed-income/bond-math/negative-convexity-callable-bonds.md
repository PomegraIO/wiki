---
title: "Negative Convexity in Callable Bonds Explained"
description: "Callable bonds exhibit negative convexity because an embedded call option caps price appreciation when yields fall, creating asymmetric price-yield behavior."
keywords:
  - negative convexity callable bonds explained
  - callable bond price-yield curve
  - embedded call option
  - bond convexity
  - interest rate risk
image: /svg/fixed-income.svg
---

*A **callable bond** with negative convexity loses the price appreciation you would normally enjoy when yields fall, because the issuer can redeem (call) the bond at a fixed price. The embedded [call option](/call-option/) acts as a ceiling on upside: as yields drop toward the call price, the bond's price curve bends inward, producing the counterintuitive result that duration increases and downside risk grows even as the bond rallies.*

## The embedded call option and the payoff cap

When a bond is callable, the issuer has the right—but not the obligation—to repay the principal plus accrued interest before maturity, usually after an initial call protection period. From the investor's perspective, this is equivalent to being long the bond and short a [call option](/call-option/) on the bond's price.

A standard (non-callable) bond's price rises as yields fall, without limit. If yields drop from 5% to 2%, a 20-year bond's price might rise 25–30%. But a callable bond's upside is capped near the call price (often 100–105% of par). If yields fall sharply, the issuer exercises the call, the bondholder receives the fixed call price, and any unrealized gain beyond that point evaporates. The investor wanted more upside but gets locked out.

Conversely, when yields rise, both the callable and non-callable bond fall in price together—there is no floor from the call. So the bond loses on the downside but gains less (or not at all) on the upside. This asymmetry is the essence of negative convexity.

## Convexity defined and visualized

Convexity measures how much the bond's price-yield curve bends. A standard bond exhibits positive convexity: the curve is slightly convex (bending upward), so price gains from falling yields exceed price losses from rising yields of the same magnitude. A callable bond exhibits negative convexity: the curve bends downward (concave) near the call price, so price losses from rising yields exceed price gains from falling yields.

Imagine two bonds—one non-callable, one callable—with identical coupons and maturity. Plot their price against yield:

- **Non-callable:** A smooth, upward-bending curve. As yield drops 100 basis points, price rises 8%. As yield rises 100 bps, price falls 7.5%. The asymmetry favors the bondholder.
- **Callable:** The same curve up to a certain yield level (where the option is out-of-the-money), then the curve flattens as it approaches the call price. As yields drop 100 bps from that inflection point, price rises only 2–3%. The curve bends inward.

The difference is most pronounced for high-coupon bonds when yields are low—precisely when the call is most likely to be exercised.

## Why the duration increases as yields fall

Duration measures the bond's sensitivity to yield changes. For non-callable bonds, duration is stable or declines slightly as yields fall. For callable bonds, duration *increases* as yields approach the call trigger.

This counterintuitive behavior stems from the option dynamics. As yields fall and the bond price approaches the call price, the issuer's incentive to call grows stronger. Investors begin to model a smaller "effective maturity" because they expect an earlier redemption. But as the call approaches, the relationship between yield changes and price changes becomes less sensitive—the price curve flattens—so the bond acts more like a shorter-duration instrument *and* less responsive to further yield declines.

In practice, a callable corporate bond trading near its call price might have a reported [duration](/duration/) of 3–4 years but behave like a 6-month instrument when yields move. This creates [execution risk](/execution-risk/) for portfolio managers hedging duration.

## Negative convexity in different rate environments

The severity of negative convexity depends on how far yields are from the call trigger:

| Yield scenario | Call status | Convexity effect | Investor implication |
|---|---|---|---|
| High yields (5–6%) | Out-of-the-money | Minimal; bond acts nearly non-callable | Small negative convexity drag |
| Moderate yields (3–4%) | Approaching | Significant; curve flattens near call price | Large cap on gains if yields fall further |
| Low yields (1–2%) | In-the-money or deep ITM | Maximal; bond price stuck near call price | Price trapped; no upside; all downside risk |

In a rising-rate environment, callable bonds look almost identical to non-callable bonds—both fall together. But when rates fall sharply, the callable bond's gains slow while the non-callable bond continues to rally. A 200-basis-point yield drop might lift a non-callable bond 15%, while a callable bond rises only 4–6%.

## Call price level and spread impact

The higher the call price, the greater the negative convexity, because the cap on upside is higher. A bond callable at 105 offers more breathing room than one callable at 100, but the cap still exists. A bond callable at 99 (a "make-whole call," sometimes seen in recent corporate debt) has almost no negative convexity because the call price floats with interest rates—the investor retains full upside.

[Credit spread](/credit-spread/) also matters. A callable bond issued by a weak credit with a wide spread may never be called because refinancing costs stay high. Negative convexity is dormant. But a callable bond issued by a strong credit trading tight (narrow spread) is always at risk of being called if rates fall.

## Compensation for negative convexity

Issuers compensate investors for negative convexity by offering a higher [coupon](/coupon-payment/) or a wider [credit spread](/credit-spread/) than a non-callable bond with the same credit quality and maturity would trade at. This [option-adjusted spread](/credit-spread/) (OAS) reflects the value of the embedded call.

For a callable corporate bond with a 5% coupon, an investor might receive 200 basis points of extra yield relative to a Treasury [yield curve](/yield-curve/) compared to 100 basis points for a non-callable corporate bond of the same credit. The extra 100 bps is the implicit option value.

The challenge is that this compensation is not always adequate. During a sharp rate decline—say, a 300-basis-point drop in a recession—a callable bond still underperforms a non-callable bond by 5–10 percentage points, erasing much or all of the "option value" premium the investor was paid.

## Measuring and hedging negative convexity

Practitioners use "effective duration" and "partial effective duration" to model callable bonds:

- **Effective duration:** Accounts for the possibility of early call. A callable bond's effective duration is lower than its stated maturity duration because the call shortens the expected life.
- **Partial effective duration:** Measures how duration changes as yields fall—a key risk metric for callable bonds. A high partial duration signals that the bond's sensitivity to rate declines is much lower than its sensitivity to rate increases, creating asymmetric risk.

To hedge negative convexity, investors often sell interest-rate [swaptions](/swap/) or [call options](/call-option/) to offset the short call position embedded in the bond itself. This is expensive and reduces yield, so most investors simply demand the higher coupon and accept the convexity risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable bond](/callable-bond/) — bond with an embedded call option exercisable by the issuer
- [Call option](/call-option/) — right to buy an asset at a fixed price; issuer "calls" the bond
- [Duration](/duration/) — bond price sensitivity to yield changes; shifts with callable bond dynamics
- [Interest rate risk](/interest-rate-risk/) — source of price variability in fixed-income portfolios
- [Convexity](/duration/) — curvature of the price-yield relationship; negative for callable bonds
- [Embedded option](/callable-bond/) — issuer's right baked into the bond contract

### Wider context

- [Yield curve](/yield-curve/) — interest rate structure that determines when callable bonds are at-the-money
- [Credit spread](/credit-spread/) — extra yield compensating for credit risk and embedded options
- [Option-adjusted spread](/credit-spread/) — spread accounting for option value in callable bonds
- [Corporate bond](/corporate-bond/) — most callable bonds are corporate; treasuries and munis rarely have calls
- [Bond](/bond/) — foundational debt security; callable bonds are a variant with issuer optionality

</div>

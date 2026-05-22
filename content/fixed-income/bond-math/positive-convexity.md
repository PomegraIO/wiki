---
title: "Positive Convexity"
description: "Property of bonds where the price-yield relationship accelerates gains when yields fall, exaggerating the price sensitivity benefit."
keywords:
  - convexity
  - bond price dynamics
  - duration
  - yield sensitivity
  - fixed income
---

*A [bond](/wiki/bond/) exhibits **positive convexity** when its [price](/wiki/bond-price-formula/) increases more rapidly for a given fall in [yield](/wiki/current-yield/) than it decreases for an equivalent rise in [yield](/wiki/current-yield/). This is the typical behavior of standard bonds. The intuition: as [yields](/wiki/current-yield/) fall, [duration](/wiki/duration/) lengthens (creating larger gains), and when [yields](/wiki/current-yield/) rise, [duration](/wiki/duration/) shortens (limiting losses).*

<aside class="wiki-infobox">

| Attribute | Detail |
|---|---|
| **Mathematical Property** | Positive second derivative of price with respect to yield |
| **Benefit to Investor** | Gains are amplified on yield declines; losses are dampened on yield rises |
| **Typical Bond Type** | Standard [option-free bonds](/wiki/bond/); bonds without [call features](/wiki/callable-bond/) |
| **Quantification** | Measured as "convexity" statistic (usually 50–200 for corporate bonds) |
| **vs Negative Convexity** | [Callable bonds](/wiki/callable-bond/) and [mortgage-backed securities](/wiki/mortgage-backed-security/) have negative convexity |
| **Trade-off** | Positive convexity bonds often yield less than equivalently-rated [callable bonds](/wiki/callable-bond/) |

</aside>

## The math of positive convexity

[Bond](/wiki/bond/) prices move inversely to [yields](/wiki/current-yield/). A 100-basis-point (1%) drop in [yield](/wiki/current-yield/) raises a [bond](/wiki/bond/) price by more than a 1% rise in [yield](/wiki/current-yield/) lowers it. The precise magnitude of these moves depends on both [duration](/wiki/duration/) and **convexity**.

Mathematically, the price change is:
- **Approximation 1** (linear): ΔPrice ≈ –Duration × ΔYield
- **Approximation 2** (convexity-adjusted): ΔPrice ≈ –Duration × ΔYield + 0.5 × Convexity × (ΔYield)²

The second term is always positive (whether yield rises or falls). If convexity is 100 and yield changes by 1%, the convexity contribution is +0.5%. This means:
- Yield down 1%: Price up ≈ Duration + 0.5% convexity benefit = larger gain.
- Yield up 1%: Price down ≈ Duration, offset by 0.5% convexity cushion = smaller loss.

This asymmetry — *larger gains on declines, smaller losses on rises* — is the definition of positive convexity.

## Why standard bonds have positive convexity

A [bond](/wiki/bond/) with positive convexity has **no embedded options**. The issuer cannot force redemption, and the bondholder cannot force early prepayment. Each promised [cash flow](/wiki/coupon-payment/) will be paid in full.

When [yields](/wiki/current-yield/) fall, the bondholder benefits twice:
1. Existing [coupons](/wiki/coupon-payment/) are worth more (discounted at lower rates).
2. The entire [cash flow stream](/wiki/bond-yield-curve-risk/) extends further into the future (because [duration](/wiki/duration/) lengthens), amplifying the rate-decline benefit.

When [yields](/wiki/current-yield/) rise, the bondholder loses, but the second effect reverses: [duration](/wiki/duration/) shortens (the [cash flow](/wiki/coupon-payment/) stream seems less distant), so the loss is contained.

This is a **free option** for the bondholder: you get the good asymmetry without paying for it (beyond the general [bond](/wiki/bond/) [yield](/wiki/current-yield/)).

## Positive convexity quantified

A [bond](/wiki/bond/) with [duration](/wiki/duration/) of 5 years and convexity of 75 faces:
- **Yield down 1%**: Price change ≈ –5 × (–0.01) + 0.5 × 75 × (0.01)² = 5% + 0.375% = 5.375%
- **Yield up 1%**: Price change ≈ –5 × (0.01) + 0.5 × 75 × (0.01)² = –5% + 0.375% = –4.625%

The asymmetry is visible: a 1% yield move gains 5.375% but loses only 4.625%.

Convexity values for typical bonds range from 50 to 200+. [Longer-duration](/wiki/duration/) [bonds](/wiki/bond/) have higher convexity; [shorter-duration](/wiki/duration/) [bonds](/wiki/bond/) have lower convexity. A [30-year Treasury](/wiki/treasury-bond/) might have convexity of 600+, while a [2-year Note](/wiki/treasury-note/) might have convexity of 3.

## Positive convexity vs negative convexity

**Positive convexity** is the standard case and favors bondholders. **Negative convexity** (or "negative gamma") occurs when the [bond](/wiki/bond/) contains embedded options.

### Callable bonds and negative convexity

A [callable bond](/wiki/callable-bond/) gives the issuer the right to redeem the [bond](/wiki/bond/) before maturity, usually when [interest rates](/wiki/interest-rate/) have fallen (making refinancing attractive for the issuer).

When [yields](/wiki/current-yield/) fall sharply:
- A standard [bond](/wiki/bond/) gains substantially.
- A [callable bond](/wiki/callable-bond/) gains less, because the issuer is likely to call it (redeeming it at par, capping the bondholder's upside).

This is negative convexity: the upside is capped. The bondholder paid for this disadvantage via a higher [yield](/wiki/current-yield/) at issuance, but the benefit is real: when [yields](/wiki/current-yield/) fall, the [callable bond](/wiki/callable-bond/) underperforms a standard [bond](/wiki/bond/).

### Mortgage-backed securities and negative convexity

[Mortgage-backed securities](/wiki/mortgage-backed-security/) carry an implicit [call option](/wiki/call-option/): homeowners can refinance (prepay) when [interest rates](/wiki/interest-rate/) fall. As [yields](/wiki/current-yield/) decline, [prepayments](/wiki/prepayment-risk/) accelerate, shortening the effective [duration](/wiki/duration/) and limiting the bondholder's price appreciation.

## The convexity premium

Investors who want positive convexity must "pay" for it by accepting lower [yields](/wiki/current-yield/). A [callable bond](/wiki/callable-bond/) with negative convexity typically yields 50–200 basis points more than a comparable [non-callable bond](/wiki/bond/) to compensate investors for the missing upside.

The trade-off:
- Buy a [non-callable bond](/wiki/bond/) at 3.5% [yield](/wiki/current-yield/): You get positive convexity.
- Buy a [callable bond](/wiki/callable-bond/) at 4.2% [yield](/wiki/current-yield/): Higher current [income](/wiki/income-statement/), but negative convexity limits upside if [rates](/wiki/interest-rate/) fall.

Which is better depends on your [yield](/wiki/current-yield/) forecast. If you expect [yields](/wiki/current-yield/) to fall, the [non-callable bond](/wiki/bond/) is better. If you expect [yields](/wiki/current-yield/) to stay flat or rise, the extra current [yield](/wiki/current-yield/) from the [callable bond](/wiki/callable-bond/) is attractive.

## Convexity and [portfolio](/wiki/asset-allocation/) management

Investors managing [bond portfolios](/wiki/fixed-income-fund-strategy/) use convexity as a portfolio lever:

- **Bullish on [rates](/wiki/interest-rate/) falling**: Overweight [longer-duration](/wiki/duration/), [non-callable bonds](/wiki/bond/) to maximize positive convexity benefit.
- **Neutral or bearish on [rates](/wiki/interest-rate/)**: Overweight [shorter-duration](/wiki/duration/) or [callable bonds](/wiki/callable-bond/) to reduce convexity drag.

High-convexity [positions](/wiki/position-limit-regulations/) are especially valuable in low-[volatility](/wiki/volatility-rules/) environments, where [yields](/wiki/current-yield/) are unlikely to move dramatically in either direction. In high-[volatility](/wiki/volatility-rules/) environments, the convexity asymmetry pays off more often.

## Practical hedging with convexity

A [bond](/wiki/bond/) manager who expects [interest rates](/wiki/interest-rate/) to become more [volatile](/wiki/volatility-rules/) might buy [longer-duration](/wiki/duration/), high-convexity [bonds](/wiki/bond/) as a [hedge](/wiki/hedging-with-futures/). The positive convexity acts like a free [option](/wiki/call-option/) that benefits from [volatility](/wiki/volatility-rules/) regardless of direction.

Conversely, a manager who expects stable [rates](/wiki/interest-rate/) might accept negative convexity ([callable bonds](/wiki/callable-bond/)) to capture the higher [yield](/wiki/current-yield/) without fear that the missing upside will be realized.

## Cross-links and further reading

<div class="wiki-seealso">

### Closely related
- [Convexity](/wiki/convexity/) — general mathematical property; positive convexity is the favorable case
- [Negative Convexity](/wiki/negative-convexity/) — opposite condition in callable and prepayable bonds
- [Duration](/wiki/duration/) — linear price sensitivity; convexity captures non-linearity
- [Bond Price Formula](/wiki/bond-price-formula/) — mathematical foundation for convexity effects

### Wider context
- [Callable Bond](/wiki/callable-bond/) — embedded option reduces convexity
- [Mortgage-Backed Security](/wiki/mortgage-backed-security/) — prepayment option creates negative convexity
- [Fixed Income Fund Strategy](/wiki/fixed-income-fund-strategy/) — portfolio management of convexity exposure
- [Interest Rate Option](/wiki/interest-rate-option/) — derivatives that isolate convexity

</div>

---
title: "Yield Spread Measures"
description: "Methods for quantifying the excess yield on a corporate bond relative to its benchmark, accounting for embedded options and curve shape."
keywords:
  - yield spread
  - nominal spread
  - z-spread
  - oas
  - option-adjusted spread
  - bond valuation
image: /svg/fixed-income.svg
---

*A **yield spread** measures the additional return an investor earns by holding a [corporate bond](/corporate-bond/) instead of a risk-free Treasury of the same maturity. Yet different spread measures isolate different sources of that excess—the [nominal spread](/nominal-spread/) captures raw yield difference, the [Z-spread](/z-spread/) accounts for curve shape, and the option-adjusted spread (OAS) removes the value of embedded options. All three are in use; which one matters depends on whether you're comparing bonds, assessing [credit risk](/credit-risk/), or pricing callable debt.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield Spread Measures — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income products and bonds." />

<div class="wiki-infobox-caption">Three ways to slice bond excess yield; each reveals different risks and pricing dynamics.</div>

|   |   |
|---|---|
| **What they measure** | Excess return on a corporate or risky bond versus a Treasury benchmark |
| **Three main types** | [Nominal spread](/nominal-spread/), [Z-spread](/z-spread/), option-adjusted spread |
| **Key insight** | Shape of yield curve affects spread calculation; callable bonds require special treatment |
| **Usage** | Credit analysis, relative-value trading, portfolio construction |
| **Who uses them** | Bond traders, credit analysts, portfolio managers, risk officers |
| **Risk captured** | [Credit risk](/credit-risk/), [liquidity risk](/liquidity-risk/), event risk, [call risk](/call-risk/) |

</aside>

## Why spreads matter

Two [bonds](/bond/) with the same maturity and credit quality may trade at different yields. A 10-year corporate bond might offer 4.5% yield; a 10-year Treasury offers 3.8%. The 70 basis-point difference—the spread—compensates the investor for [credit risk](/credit-risk/), lower [liquidity](/liquidity-risk/), and any embedded features (like a call option that lets the issuer redeem early).

But the "70 basis points" is deceptively simple. It doesn't tell you:
- Whether that spread is wide or tight compared to history, or other issuers
- How much of it reflects credit risk versus illiquidity
- How a callable bond's embedded option affects the comparison
- Whether the yield curve's shape distorts the comparison

Three spread measures have emerged to answer these questions.

## Nominal spread: the quick comparison

The [nominal spread](/nominal-spread/)—sometimes called the **static spread**—is the simplest: subtract the Treasury's [yield-to-maturity](/yield-spread-measures/) from the corporate bond's YTM, same maturity, same point in time.

**Nominal Spread = Corporate Bond Yield − Treasury Yield**

If the corporate bond yields 4.5% and the Treasury yields 3.8%, the nominal spread is 70 basis points.

**Virtue:** Dead simple, transparent, intuitive.

**Vice:** Ignores the shape of the yield curve. If the Treasury curve is steep (short rates far below long rates), the nominal spread overstates the compensation for pure [credit risk](/credit-risk/). The corporate bond is probably being compared to a Treasury of the exact same 10-year maturity, but in reality, the issuer might be borrowing from a range of points along the curve, not just at the 10-year tenor. The nominal spread makes no adjustment for this mismatch.

## Z-spread: accounting for curve shape

The [Z-spread](/z-spread/) (or **zero-volatility spread**) fixes the nominal spread's curve blindness. Instead of comparing at a single maturity, the Z-spread is the constant spread you add to every [spot rate](/spot-exchange-rate/) on the Treasury curve so that the corporate bond's discounted cash flows equal its market price.

Imagine the Treasury spot curve: 2 years at 3%, 5 years at 3.5%, 10 years at 4%. To value the corporate bond, you discount each coupon and principal payment using these spot rates, then add a constant Z-spread (say, 80 basis points) to each one. The Z-spread that makes the sum equal the bond's actual price is **the** Z-spread.

**Virtue:** Economically cleaner; uses the entire yield curve, not just one point. If the curve is steep, the Z-spread will differ from the nominal spread, signalling that some of the yield difference comes from curve shape, not credit risk alone.

**Vice:** Requires a full spot curve and a discounted cash flow model. Less intuitive for traders eyeballing prices. Also, it assumes yields will not change and the [volatility](/volatility-smile/) of future rates is zero—the "zero-vol" assumption. In a fast-moving market, this static assumption can mislead.

## Option-adjusted spread (OAS): for bonds with embedded options

The real trickiness emerges with [callable bonds](/callable-bond/). When a bond is callable, the issuer can redeem it if rates fall—capping the bondholder's upside. A naive comparison understates the value of that call option to the issuer and overstates the yield the investor truly gets if rates fall.

The **option-adjusted spread** accounts for the value of embedded options. It's the constant spread added to the spot curve (like Z-spread) but adjusted for the probability-weighted value of the issuer's call (or the bondholder's embedded put).

**Virtue:** Correctly compares bonds with and without embedded options. A callable bond's OAS will be higher than its Z-spread because some of the yield compensates for the call option the bondholder grants to the issuer.

**Vice:** Requires an interest-rate model to price the embedded option—models can differ, so two analysts may calculate different OAS on the same bond. Also computationally heavier than nominal or Z-spread.

## Applying the three measures

Imagine a corporate bond desk comparing two bonds:
- **Bond A:** 5-year corporate, trading at 4% yield; 5-year Treasury at 3.3%. Nominal spread = 70 bp.
- **Bond B:** Same issuer, 10-year corporate, trading at 4.8% yield; 10-year Treasury at 3.8%. Nominal spread = 100 bp.

The nominal spread suggests Bond B offers 30 bp more compensation. But the Treasury curve is steep (70 bp across the 5-to-10 year segment). The Z-spread might reveal that both bonds have nearly identical true credit spread—the 100 bp nominal spread on Bond B includes 70 bp of curve shape, not extra credit risk.

Now add a third bond:
- **Bond C:** 10-year corporate, callable after 5 years, trading at 5.2% yield. Nominal spread = 140 bp.

Bond C's extra 40 bp looks like extra credit risk, but much of it is compensation for the call option. The OAS, factoring in the call option's value, might be only 110 bp—closer to Bond B's true risk premium.

## Trade-offs in practice

**Corporate credit analysts** favour the Z-spread or OAS because they want to isolate credit risk from curve effects and option effects.

**Relative-value traders** often start with nominal spread—it's fast and captures simple yield differences—then dig deeper with Z-spread if the trade seems off.

**Risk managers** pricing portfolios tend toward OAS, especially if the portfolio includes callable bonds or any position sensitive to [interest-rate](/interest-rate/) changes and [volatility](/volatility-smile/).

Most financial terminals (Bloomberg, Refinitiv, others) compute all three in real time. The key is knowing which spread answers your question: Are bonds cheap or dear relative to peers? Which spread is widest in history? How much of the yield difference is credit risk versus curve shape? Is the call option overpriced?

## See also

<div class="wiki-seealso">

### Closely related

- [Nominal Spread](/nominal-spread/) — the raw yield difference between bond and Treasury benchmark
- [Z-Spread](/z-spread/) — spread adjusted for the shape of the entire Treasury curve
- [Callable Bond](/callable-bond/) — bonds with embedded call options; the principal reason OAS exists
- [Call Risk](/call-risk/) — the bondholder's risk that the issuer redeems early
- [Credit Risk](/credit-risk/) — the spread's core compensation source
- [Yield-to-Maturity](/yield-spread-measures/) — the metric both corporate and Treasury yields use

### Wider context

- [Yield Curve](/yield-curve/) — the shape that Z-spread and OAS account for
- [Interest Rate](/interest-rate/) — the baseline for all yield calculations
- [Bond](/bond/) — the instrument being valued
- [Corporate Bond](/corporate-bond/) — where these spreads live and are actively traded
- [Liquidity Risk](/liquidity-risk/) — often bundled into spread but distinct from credit risk

</div>

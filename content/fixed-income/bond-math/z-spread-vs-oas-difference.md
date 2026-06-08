---
title: "Z-Spread vs OAS: What the Difference Reveals"
description: "Z-spread vs OAS difference: OAS strips embedded option value from Z-spread, isolating true credit and liquidity risk in callable and putable bonds."
keywords:
  - z-spread vs oas difference
  - option-adjusted spread
  - z-spread bond
  - callable bond valuation
  - bond credit spread
---

*A bond's **Z-spread vs OAS difference** reveals whether its promised yield premium comes from real credit risk or from an embedded option that could reduce your return. The OAS strips out option value—what a callable bond's issuer might exercise—leaving only the spread attributable to credit quality and liquidity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Z-Spread vs OAS Difference — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two ways to measure the yield premium embedded in a bond's price.</div>

|   |   |
|---|---|
| **Z-spread (zero-volatility spread)** | Constant spread added to each point on the Treasury yield curve that reconciles to market price; ignores embedded options |
| **OAS (option-adjusted spread)** | Z-spread minus the estimated value of embedded options; isolates credit and liquidity risk alone |
| **When they diverge most** | [Callable bonds](/callable-bond/) with deep in-the-money call options; [convertible bonds](/convertible-bond/) |
| **For plain vanilla bonds** | Z-spread and OAS are identical (no embedded options to strip) |
| **Use case: credit analysis** | OAS tells you the "true" credit spread; Z-spread can overstate it if a call is valuable |

</aside>

## Why Two Spreads Exist

The Z-spread and OAS both measure how much yield premium a bond offers over risk-free Treasuries. They differ because some bonds carry *embedded options*—rights that alter the bond's future payoffs.

A [callable bond](/callable-bond/) gives the issuer the right to redeem early, usually when rates fall and refinancing becomes attractive. A [putable bond](/put-option/) lets the bondholder force early redemption if conditions deteriorate. A [convertible bond](/convertible-bond/) contains a hidden equity option. These options have value—they change the bond's expected return and risk profile.

The Z-spread captures the total yield premium needed to match market price, including option value. But if you're a credit analyst trying to gauge whether the issuer's credit quality justifies the yield, you need to know the spread *after* stripping out the option's impact. That's the OAS. The difference between the two tells you how much value the option holds.

## How Z-Spread Is Calculated

The Z-spread (or zero-volatility spread) is the constant spread added to every point on the [Treasury yield curve](/treasury-bond/) such that the bond's discounted cash flows equal its current market price.

In practice:
1. You start with the Treasury curve (1-year, 2-year, 5-year rates, etc.).
2. You add a fixed spread to *every* rate on that curve.
3. You discount the bond's cash flows at these adjusted rates.
4. You adjust the spread until the present value of those flows equals the bond's market price.

The Z-spread treats all cash flows—whether they're promised coupons or include an early redemption—as certain. It makes no distinction between a bond the issuer will hold to maturity and one it will call away.

## The Option-Adjusted Spread: Stripping Out Option Value

The OAS starts with the same goal—find the credit premium—but accounts for the fact that embedded options may *not* deliver all promised cash flows.

To calculate OAS:
1. Use a model of interest rate dynamics (e.g., a binomial tree of future rate paths).
2. For each path, simulate when the bondholder or issuer will exercise the embedded option (e.g., the issuer calls the bond when rates fall far enough to justify refinancing).
3. Adjust each path's cash flows to reflect exercise decisions.
4. Calculate the spread that makes the expected value of *those* state-dependent cash flows equal the market price.

The difference between Z-spread and OAS *is* the value of the option, expressed as a spread:

**OAS = Z-spread − Option-adjusted value**

## When the Difference Matters Most

For a plain vanilla bond with no embedded options, Z-spread and OAS are identical. Both measure the pure credit and liquidity premium.

For a callable bond, the two diverge sharply when the call is *in-the-money*. Suppose a bond is trading at par, yielding 4%, while risk-free Treasuries yield 2%. The Z-spread might be 200 basis points. But if the issuer's call option is worth 50 basis points (because rates have fallen and refinancing is profitable), the OAS is only 150 basis points. The true credit spread—what you're compensated for lending to the issuer rather than the government—is 150 bps, not 200.

Conversely, a putable bond where the put is valuable will see Z-spread *below* OAS, because the put protects you and reduces the required credit compensation.

For a convertible bond, the embedded equity call is often substantial. A convertible trading at 110% of par might have a Z-spread of 150 bps but an OAS of 200 bps or higher, because the equity option is worth more than 50 bps—the bondholder is paying implicitly for the upside.

## A Worked Example

Imagine a 5-year corporate bond paying 4% annually, trading at $102. Comparable Treasuries yield 2% overall. A quick calculation shows a Z-spread of roughly 180 basis points (4% − 2% ≈ 180 bps when accounting for the price premium).

Now suppose the bond is callable at par in 2 years. Interest rates have fallen, so the call is worth about 40 basis points—the issuer will likely exercise it if rates stay low. A proper OAS model, simulating many paths of future rates and the issuer's optimal call decisions, estimates the OAS at 140 basis points.

The 40 basis point gap means:
- **180 bps Z-spread** = credit risk + liquidity risk + option value.
- **140 bps OAS** = credit risk + liquidity risk alone.
- The option costs you 40 bps in expected return because your upside is capped.

A naive credit analyst using Z-spread might conclude the issuer's credit premium is generous. The OAS reveals the true picture: 140 bps is the real compensation for lending risk.

## Practical Use in Bond Trading and Analysis

Bond traders use OAS to compare credit value across bonds with different maturity and coupon structures, and different embedded options. Two bonds with the same issuer but different options might have the same OAS even if their Z-spreads differ, signaling they offer comparable credit compensation.

Credit analysts prefer OAS because it isolates credit and liquidity factors from option factors. A rising OAS for an issuer's bonds signals deteriorating credit quality; a narrowing OAS reflects improving creditworthiness or falling [credit-risk](/credit-risk/) premiums.

Conversely, changes in Z-spread can reflect option value shifting—rates falling and making a call more valuable—even though the issuer's credit quality hasn't changed.

Portfolio managers building [bond portfolios](/bond/) watch both. A wide gap between Z-spread and OAS signals a bond with valuable embedded options that might behave unpredictably if rate regimes shift. A narrow gap suggests a straightforward credit trade.

## The Limits of Both Measures

Neither Z-spread nor OAS is perfect. Both depend on:
- **Model assumptions** about interest rate volatility (critical for pricing options).
- **The yield curve shape** you choose as a starting point.
- **Illiquidity assumptions**—a less liquid bond's true credit spread may be hard to isolate from liquidity premiums.

In practice, the Z-spread vs OAS difference is useful as a *signal* of option value, but not as a precise measurement. Traders often compute both and use the gap as a relative indicator—if OAS narrows significantly while Z-spread widens, something has changed about option value, and it's worth investigating whether that reflects a real change in interest rate expectations or in the issuer's refinancing incentives.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable bond](/callable-bond/) — bonds where the issuer retains the right to redeem early
- [Option-adjusted spread](/bond/) — the foundational concept for understanding option-adjusted returns
- [Credit spread](/credit-spread/) — the premium yield over risk-free rates that varies with credit quality
- [Put option](/put-option/) — how bondholder protection options work
- [Convertible bond](/convertible-bond/) — bonds with embedded equity upside

### Wider context

- [Bond](/bond/) — core instrument structure and uses
- [Treasury bond](/treasury-bond/) — the baseline for yield curve construction
- [Interest rate risk](/interest-rate-risk/) — why embedded options matter for rate sensitivity
- [Yield to maturity](/bond/) — the simpler, option-unaware return measure

</div>

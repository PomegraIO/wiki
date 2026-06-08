---
title: "Par Yield vs Spot Rate: What Each Tells You About the Yield Curve"
description: "Par yield is the coupon rate that prices a bond at par; spot rate is the zero-coupon discount rate. Each derives from market prices but answer different valuation questions."
keywords:
  - par yield vs spot rate
  - yield curve construction
  - zero coupon rates
  - bond pricing methods
  - fixed income mathematics
image: "/svg/fixed-income.svg"
---

*The **par yield** and **spot rate** are two ways of expressing the same market prices, but they answer different questions. The par yield is the coupon rate that would make a bond trade at 100 (par) given the current rate structure; the spot rate is the zero-coupon discount rate for a single maturity. Traders and risk managers switch between them depending on whether they are pricing vanilla coupon bonds or solving for the term structure of rates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Par Yield vs Spot Rate — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two lenses on the same market; neither is "correct," but each suits different uses.</div>

|   |   |
|---|---|
| **Par yield** | The coupon rate on a hypothetical bond priced at par (100) |
| **Spot rate** | The discount rate for a single, lump-sum cash flow at maturity |
| **Where derived** | Both from actual bond prices in the market |
| **Common use** | Par yields for quotation; spot rates for valuation and risk |
| **Relationship** | Both rise/fall with the same underlying market forces |

</aside>

## The core difference: one rate for each cash flow vs. one rate per coupon bond

A **spot rate** is the yield on a zero-coupon bond—an instrument that makes no interim payments and returns principal at maturity. If the two-year spot rate is 3%, you pay $94.26 today for $100 received in two years (rounding). That 3% is the pure discount rate for a two-year cash flow, uncontaminated by any interim coupons.

A **par yield** is the coupon percentage on a coupon-paying bond that would price it at exactly 100 (par). If the two-year par yield is 3%, a bond paying 3% annually and maturing in two years is worth exactly 100. The same market that generated the spot rates also generates the par yields, but par yields bundle together all the single-period discount factors into a single coupon rate.

In short: a spot rate answers "what is the discount rate for a single cash flow at time T?"; a par yield answers "what coupon rate makes a bond worth par?".

## Deriving spot rates from market bond prices

Suppose the market offers these prices for zero-coupon bonds (or strips):

| Maturity | Price | Yield |
|----------|-------|-------|
| 1 year   | $97.09 | 3.0% |
| 2 year   | $94.26 | 3.0% |
| 3 year   | $91.51 | 3.0% |

If all three spot rates happen to be 3% (a flat curve), then:
- s₁ = 3.0%
- s₂ = 3.0%
- s₃ = 3.0%

That is the spot rate curve. In reality, spot rates are rarely flat; they usually slope upward (yields rise with maturity during normal times) or invert (short-term yields exceed long-term, a recessionary signal).

## Deriving par yields from spot rates

Once you have the spot curve, the par yield for any maturity follows directly from the [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) principle. For a bond with maturity of N years and annual coupon rate c, the price is:

**Price = c/(1+s₁) + c/(1+s₂) + ... + (c+100)/(1+sₙ)**

If you set Price = 100 and solve for c, you get the par yield for that maturity.

Example: if the spot rates are s₁ = 2%, s₂ = 3%, s₃ = 4%, then the par yield for three years is the coupon c such that:

**100 = c/1.02 + c/1.03 + (c+100)/1.04**

Rearranging: c × [1/1.02 + 1/1.03 + 1/1.04] + 100/1.04 = 100

Solving: c ≈ 3.03%

So the three-year par yield is about 3.03%. A three-year bond paying a 3.03% coupon trades at 100 given this spot curve.

## Why both exist: quotation vs. valuation

**Bond traders quote coupon bonds by yield-to-maturity (YTM)**, not par yield, because YTM is what the market prices show—it is a single internal rate of return. But par yields matter for understanding the shape of the yield curve without the confounding effect of different coupon rates. All par yields have the same coupon (100 cents of interest per 100 of principal), so comparing par yields directly shows you the true term structure.

**Risk managers and quantitative analysts prefer spot rates** because they are the pure discount rates. When you hedge a portfolio or price derivatives, you discount each future cash flow by its own spot rate. That is theoretically cleaner and operationally essential for bonds with embedded options or for multi-currency strategies where you need the discount curve in each currency.

## A practical comparison

Consider two real 3-year bonds:
- Bond A: 2% coupon, priced at 97.50 (YTM ≈ 2.8%)
- Bond B: 4% coupon, priced at 102.00 (YTM ≈ 3.8%)

Both are 3-year bonds, but they have different YTMs because their coupons differ. Neither YTM is the "market yield for three years"—they are just the internal rates of return for those specific bonds.

The **3-year par yield** (say, 3.5% in this market) represents the coupon rate for a hypothetical bond that trades at par. It is the canonical yield for that maturity, independent of which specific bond you bought.

The **3-year spot rate** (say, 3.6% in this market) is the discount rate for a single $100 payment in three years. It is slightly higher than the par yield because the par yield blends together the lower rates for years 1 and 2 with the higher rate for year 3.

## The relationship between par yield and spot rates

The spot rate curve and the par yield curve are two representations of the same market. If spot rates are rising with maturity (an upward sloping curve), par yields will also be rising, but typically at a slightly different pace. The par yield is a weighted average of the spot rates up to that maturity, weighted by the discount factors of the coupon payments.

In a rising rate environment, the par yield lies *below* the longest spot rate (because earlier coupons are discounted at lower rates). In a falling rate environment, the par yield lies *above* the shortest spot rate. Both curves convey the same information, but they present it differently.

## Where you see each in practice

- **Par yields**: official yield curve data from central banks and bond indices; trader quotations for benchmarks like the U.S. Treasury curve
- **Spot rates**: fixed-income analytics, option-adjusted spread (OAS) models, bond futures hedging, derivatives valuation

A portfolio manager might say, "The par yield curve is now positively sloped," while a quant says, "The spot curve is inverted at the 5–10 year junction." Both are drawing on the same underlying prices, just reformulated for their respective tasks.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield-to-Maturity](/yield-to-maturity/) — the single discount rate implied by a coupon bond's price
- [Bond](/bond/) — coupon structure and par value basics
- [Discounted-Cash-Flow-Valuation](/discounted-cash-flow-valuation/) — the framework that connects all three: YTM, par yields, and spot rates
- [Yield-Curve](/yield-curve/) — term structure of interest rates, typically shown as par yields or spot rates
- [Bond-Convexity-Adjustment](/bond-convexity-adjustment/) — how convexity relates to understanding bond price curves

### Wider context

- [Duration](/duration/) — effective maturity; changes with the spot curve
- [Interest-Rate-Risk](/interest-rate-risk/) — spot rate shocks drive bond price changes
- [Bond-Basis-Points-Value](/bond-basis-points-value/) — pricing precision using basis-point sensitivity
- [Credit-Risk](/credit-risk/) — credit spread adjustments over spot curves
- [Forward-Contract](/forward-contract/) — forward rates are implied from spot curves

</div>

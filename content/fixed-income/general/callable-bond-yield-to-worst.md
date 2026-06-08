---
title: "Yield to Worst on a Callable Bond"
description: "Yield to worst on a callable bond accounts for call risk. Learn why it's the most conservative yield metric and how to calculate it across multiple call dates."
keywords:
  - yield to worst callable bond
  - call risk
  - yield-to-call
  - bond callable
  - fixed income risk
image: /svg/fixed-income.svg
---

*The **yield-to-worst (YTW)** is the lowest possible return you could earn on a [callable-bond](/callable-bond/), accounting for the worst-case scenario: the issuer calls the bond when rates fall and the call makes sense for them. YTW is calculated across every possible call date and maturity, and the metric reveals the return if the absolute least favorable outcome occurs. It is more realistic than [yield-to-maturity](/yield-to-maturity/) when the bond is at risk of early redemption, but less rosy than a simple [yield-to-call](/yield-to-call/) assumes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield to Worst — Key Facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">The lowest credible return across all call and maturity paths.</div>

|   |   |
|---|---|
| **What it measures** | Minimum yield if the issuer exercises the worst outcome for you |
| **When to use it** | Any bond with embedded optionality (callable, puttable, convertible) |
| **Calculation** | Test all call dates and maturity; pick the path yielding the lowest return |
| **Why it matters** | YTM assumes no call; YTW is the realistic floor for callable bonds |
| **Call protection** | A bond with no call risk for 3 years may have YTW ≈ YTM for short horizons |
| **Rising rate environment** | YTW often ≈ YTM when call risk is low (issuer will not call) |
| **Falling rate environment** | YTW << YTM as call risk spikes (issuer will call) |

</aside>

## Why Yield-to-Maturity Isn't Enough for Callable Bonds

When you buy a bond, the [yield-to-maturity](/yield-to-maturity/) tells you the internal rate of return (IRR) if you hold until maturity and collect all coupons and principal. But a [callable-bond](/callable-bond/) includes an embedded option: the issuer can redeem the bond early, typically at par (100% of face value) plus accrued interest.

If you buy a corporate bond yielding 5% and the company can call it in 3 years at par, you face a dilemma. If rates fall to 3%, the company will almost certainly call—they can refinance at a lower cost and you lose your high-coupon stream. You are left with par redemption instead of holding a premium bond for 10 years. Your actual return drops sharply from the promised [yield-to-maturity](/yield-to-maturity/).

This is [call-risk](/callable-bond/): the risk that the bond is redeemed early when rates fall, stranding you at par instead of enjoying the capital appreciation you might have captured. Yield-to-worst quantifies this risk in a single number.

## How Yield-to-Worst Is Calculated

The process involves testing three scenarios: hold to maturity, call at each possible call date, and select whichever path yields the *lowest* return.

**Example: A 10-year corporate bond**
- Current price: $105 (premium)  
- Coupon: 5% ($50/year)  
- Par: $100  
- Maturity: 10 years  
- First call date: 3 years at par ($100)  
- Second call date: 5 years at par ($100)  

For each path, you calculate the IRR:

**Path 1: Hold to maturity (10 years)**
- Buy at $105, collect 10 × $50 coupon, get $100 at maturity  
- IRR (yield-to-maturity) = 4.58%  

**Path 2: Called at 3 years**
- Buy at $105, collect 3 × $50 coupon, get $100 at call  
- IRR (yield-to-call at year 3) = 1.22%  

**Path 3: Called at 5 years**
- Buy at $105, collect 5 × $50 coupon, get $100 at call  
- IRR (yield-to-call at year 5) = 2.84%  

**Yield-to-worst = minimum of {4.58%, 1.22%, 2.84%} = 1.22%**

The 3-year call yields the worst outcome because you lose the most premium the fastest. YTW of 1.22% is the realistic worst case and therefore the metric a risk-averse investor should focus on.

## Call-Adjusted Yield: The Risk-Aware Metric

Yield-to-worst is superior to [yield-to-maturity](/yield-to-maturity/) for callable bonds because it acknowledges reality: if rates fall, the bond gets called. A bond yielding 5% YTM but 1.2% YTW is a very different investment than the label "5% bond" suggests.

However, YTW is still conservative in one respect: it assumes the *absolute worst* call date (the one that hurts you most), not the *most likely* call date. In a stable or rising-rate environment, call risk may be low, and YTW overstates the pain. A typical investor might expect the bond to be called in 5 years or not at all, not necessarily in 3 years.

To bridge this, some practitioners use **yield-to-call on the most likely call date** (e.g., the date when the issuer's refinancing incentive is highest) as a middle estimate between YTM (too optimistic) and YTW (too pessimistic).

## Callable Bonds vs Call Risk: When YTW Matters Most

The relevance of YTW depends on the environment and the bond's characteristics.

**High call risk (falling rates, premium bond):**  
YTW can be 1–3% *lower* than YTM. A 5% coupon bond trading at $110 might have YTM = 4.2% but YTW = 1.8% if it will be called at par within 3 years. The gap is severe, and YTW is the only honest yield metric.

**Low call risk (rising rates, discount bond):**  
YTW ≈ YTM. If rates are high and the bond trades below par, the issuer has no incentive to call. The bond will likely run to maturity, so YTW and YTM converge. A 6% bond trading at $90 with 2% interest rates may have YTW ≈ YTM because call is unlikely.

**Call protection (non-callable for N years):**  
A bond with 5 years of call protection (no call for the first 5 years) will have YTW ≈ YTM over a 5-year horizon, because call cannot occur. After year 5, call risk re-enters.

## Quantifying the Yield Hit

Consider a $100 bond with the following:

| Metric | Value |
|--------|-------|
| Coupon | 6% |
| Current price | $108 |
| Maturity | 15 years |
| First call date | 3 years at $100 |
| Yield-to-Maturity | 5.35% |
| Yield-to-Call (3-year) | 0.84% |
| Yield-to-Worst | 0.84% |

The investor paid a $8 premium for the bond. If called in 3 years at par, they lose that entire premium in 3 years, resulting in a 0.84% return. The YTW reveals that this bond's actual downside is severe—you are paying up for a coupon you may not keep.

## Yield-to-Worst in Portfolio and Bond Selection

When evaluating [corporate-bond](/corporate-bond/) [alternatives](/alternative-trading-system/) or [municipal-bond](/municipal-bond/) issues, always scan the YTW as your conservative baseline return. If YTW < cost of equity, the bond is not worth holding except for diversification or [credit-risk](/credit-risk/) mitigation.

For bond funds, YTW aggregated across the portfolio gives a more honest estimate of downside return than a simple [yield-to-maturity](/yield-to-maturity/)-weighted average. A [bond-etf](/bond-etf/) full of callable corporates may advertise a 4.5% YTM but deliver 2.8% YTW in a falling-rate scenario—a major gap.

## The Options Perspective

From an options standpoint, the bondholder is short a call: the issuer owns the right to buy back the bond at par. As rates fall, that call option becomes valuable and likely to be exercised. YTW reflects this embedded short call risk, whereas YTM ignores it entirely. This is why [duration](/duration/) (interest-rate sensitivity) must also be adjusted for callable bonds—the duration of a 15-year callable bond might be only 5 years if call risk is high.

## See also

<div class="wiki-seealso">

### Closely related

- [Callable Bond](/callable-bond/) — Definition and mechanics of bonds with call provisions
- [Yield to Maturity](/yield-to-maturity/) — The standard yield metric; does not account for call risk
- [Yield to Call](/yield-to-call/) — Yield if the bond is called on a specific date; a component of YTW
- [Call Risk](/call-risk/) — The risk that the issuer redeems the bond when rates fall
- [Duration](/duration/) — Effective interest-rate sensitivity of a callable bond differs from standard duration

### Wider context

- [Corporate Bond](/corporate-bond/) — Corporate bonds are often callable; municipal bonds less so
- [Credit Risk](/credit-risk/) — The default risk underlying any bond valuation
- [Municipal Bond](/municipal-bond/) — Some munis are callable; YTW applies here too
- [Bond ETF](/bond-etf/) — Portfolio YTW is a key metric for evaluating bond fund risk

</div>
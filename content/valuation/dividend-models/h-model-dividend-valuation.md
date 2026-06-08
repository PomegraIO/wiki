---
title: "H-Model"
description: "A dividend discount valuation formula that accommodates linear decline from initial high growth to stable perpetual growth."
keywords:
  - dividend valuation
  - linear growth decline
  - two-stage model
  - share valuation
  - H-model formula
image: "/svg/valuation.svg"
---

*The **H-Model** is a variation of the [dividend discount model](/dividend-yield/) that values equities when expected dividend growth starts high and declines in a straight line toward a stable long-term rate. Rather than jumping abruptly from one growth phase to another, it smooths the transition.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">H-Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation methods." />

<div class="wiki-infobox-caption">A practical approximation for firms in transition between high and stable growth.</div>

|   |   |
|---|---|
| **What it is** | A [dividend discount model](/dividend-discount-model/) variant handling linearly declining growth |
| **Key formula** | V = D₀ × [(1+gₗ)/(r−gₗ) + H × (gₛ−gₗ)/(r−gₗ)] |
| **H parameter** | Half the length of the high-growth period (years) |
| **Advantages** | Cleaner than two-stage models; captures realistic growth transitions |
| **Limitation** | Still assumes linear decline—actual growth paths rarely follow exactly |
| **When to use it** | Mature firms with declining but still-above-normal dividend growth |

</aside>

## Why one steady growth rate isn't enough

The basic [dividend discount model](/dividend-discount-model/) assumes perpetual growth at a single constant rate. That works for truly mature utilities where dividends grow at GDP rates forever. But for many real firms—especially those past their rapid-growth phase—dividends accelerate initially, then gradually slow toward the long-term norm. A single discount rate misses that arc.

A crude approach would be a two-stage model: grow fast for 5 years, then switch to a slow rate forever. This creates a discontinuity. The H-Model smooths it by assuming growth declines *linearly* from an initial rate gₛ (short-term, high) down to gₗ (long-term, stable) over a defined period.

## The formula and its logic

The H-Model value is:

**V = D₀ × [(1+gₗ)/(r−gₗ) + H × (gₛ−gₗ)/(r−gₗ)]**

Where:
- D₀ = most recent dividend per share
- r = required return (discount rate)
- gₛ = initial short-term growth rate
- gₗ = terminal long-term growth rate
- H = half-life of the high-growth period (in years)

The first term, (1+gₗ)/(r−gₗ), is the perpetuity value growing at the stable rate. The second term, H × (gₛ−gₗ)/(r−gₗ), adds the extra value from the higher growth in the initial phase. The H parameter captures how long that advantage persists; larger H means a longer transition, so more extra value.

## Where it came from

The H-Model was popularized by Harley Fuller and Chi-Cheng Hsia in the 1980s as a practical shortcut. The math assumes dividends follow a linear declining growth trajectory—not a precise reality, but a useful approximation that avoids the manual calculation of year-by-year forecasts over a high-growth phase. It became a favourite of equity analysts precisely because it's fast to estimate and less prone to error than explicitly modeling dozens of years of transition.

## Using H properly

The value of H is critical. If gₛ is expected to decline to gₗ over 10 years, then H = 5 (half of 10). The parameter reflects the analyst's belief about *how quickly* the firm matures. A tech company might have H = 3; a utility with a gentler deceleration might have H = 7.

This is where judgment enters. No formula can tell you whether a firm's high growth will fade in 5 years or 15. Market conditions, competitive dynamics, and reinvestment discipline all matter. A practitioner should test a range of H values to see how sensitive the valuation is—a sign that the estimate depends heavily on hard-to-predict timing.

## When does it break down?

The linear assumption is clean but rarely exact. Some firms' dividends accelerate before decelerating. Others plateau and then shift abruptly. If the actual growth path is convex (starts slow, peaks, then falls) or concave (drops steeply early), the H-Model will misestimate. It also assumes constant [required return](/interest-rate/) r over the transition, which ignores any change in risk as the firm matures.

For highly cyclical or distressed firms, or those whose business model is fundamentally shifting, the H-Model may mislead. It works best for established companies where the transition is neither violent nor unpredictable—think a profitable software firm gradually moving from 20% dividend growth to 5%, or a bank settling into a new competitive equilibrium.

## Comparison to alternatives

A [two-stage dividend discount model](/dividend-discount-model/) explicitly forecasts cash flows for years 1 to N, then assumes stable growth thereafter. It gives more detail but is slower to calculate. A [three-stage model](/dividend-discount-model/) or explicit [discounted cash flow](/discounted-cash-flow-valuation/) adds a third phase, useful for firms with a distinct turnaround or decline period.

The H-Model sits in the middle: faster than explicit multistage forecasting, more realistic than a single perpetual growth rate. For many practitioners, it's the sweet spot—enough sophistication without over-precision.

## Practical use

Equity analysts often use the H-Model as a quick sanity check. If a stock trades at a price that implies a required return r below the [risk-free rate](/interest-rate/), something is wrong. Conversely, if the implied r is extremely high, perhaps the market is pricing in dividend risk the analyst hasn't accounted for.

The H-Model works best paired with [sensitivity analysis](/sensitivity-analysis-valuation/). Vary gₛ, gₗ, r, and H across reasonable ranges and see what valuation range emerges. If a small shift in H doubles the value, the estimate is fragile. If valuations cluster in a tight band despite parameter variation, the analysis is more robust.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the foundational approach that values stocks as the present value of all future dividends
- [Stochastic Dividend Discount Model](/stochastic-dividend-discount-model/) — incorporates random growth shocks rather than deterministic patterns
- [Dividend Yield Plus Growth Model](/dividend-yield-plus-growth-model/) — a simpler two-parameter estimate of required return
- [Implied Cost of Equity (DDM-Derived)](/implied-cost-of-equity-ddm/) — backing out the market-implied discount rate from observed price
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the broader framework of which dividend models are a subset
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing how valuations shift with parameter changes
- [Dividend Yield](/dividend-yield/) — the cash yield on the stock price

### Wider context

- [Cost of Equity](/cost-of-equity/) — the required return used as the discount rate
- Valuation — the general practice of estimating intrinsic value
- [Dividend](/dividend/) — the cash payment itself
- [Stock](/stock/) — the equity security being valued
- [Business Cycle](/business-cycle/) — long-term growth trends anchor stable-rate assumptions

</div>

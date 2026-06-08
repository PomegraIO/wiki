---
title: "H-Model vs Two-Stage DDM: When Each Applies"
description: "Compare H-model smooth decay versus two-stage DDM phase transitions for dividend discount modeling; guidance on growth-profile fit."
keywords:
  - h-model vs two-stage dividend discount model
  - h-model dividend growth
  - two-stage dividend discount model
  - dividend discount model comparison
image: /svg/valuation.svg
---

*The **H-model vs two-stage dividend discount model comparison** is a choice between two distinct assumptions about how dividend growth changes over time. The H-model assumes a smooth, linear decline from high growth to stable growth; the two-stage DDM assumes an abrupt phase transition from extraordinary growth to maturity. Each fits different real-world patterns, and choosing wrong can significantly overvalue or undervalue a stock.*

## The Dividend Discount Model Foundation

Both models rest on the same principle: a company's intrinsic value is the present value of all its future dividends. The [dividend discount model](/dividend-discount-model/) requires three inputs: the current dividend, the growth rate going forward, and the required return (discount rate). A stable, mature company can be valued with constant-growth assumptions; a high-growth company cannot.

The challenge is modeling the transition from high growth to stability. Most companies do not grow at 15% forever; they eventually slow to 3% or 4% as they mature. The question is how fast that deceleration occurs and by what path.

## The H-Model: Linear Decay

The **H-model** assumes that growth declines linearly from an initial high rate to a terminal stable rate over a finite period. The name comes from H, which represents half the length of the high-growth period.

In mathematical terms, if a company begins with dividend growth of *g*₁ (say, 12%) and eventually settles to terminal growth of *g*₂ (say, 3%), the H-model assumes that the growth rate decays in a straight line from *g*₁ to *g*₂ over a period of 2H years. The value formula is:

**V = D₀ × [(1 + g₂) / (r - g₂)] + D₀ × H × (g₁ - g₂) / (r - g₂)**

In plain terms: the first term is the present value of perpetual stable-growth dividends; the second term is the extra value from the high-growth years, which decays linearly.

### When the H-Model Fits

The H-model works well for companies in steady transition from growth to maturity:

- **Mature growth stocks** entering a gradual slowdown (such as a large retailer expanding but facing eventual market saturation)
- **Infrastructure or utilities** historically growing faster than GDP but slowing to GDP growth
- **Real estate investment trusts** experiencing above-average growth but heading toward long-run stable yields
- **Established tech companies** that have moved past hypergrowth but remain above-market growers

The model's strength is its simplicity. You specify only the current growth rate, the target rate, and the decay period. The linear assumption is intuitive and avoids the false precision of multi-stage models.

## The Two-Stage DDM: Abrupt Transition

The **two-stage dividend discount model** divides a company's future into two distinct phases: an explicit high-growth period (typically 5–10 years) during which dividends grow at a constant rate *g*₁, followed by a stable-growth period in perpetuity at rate *g*₂.

During the first stage, the investor forecasts dividends year by year. In the second stage, they use the [Gordon growth model](/dividend-discount-model/) formula (also called the constant-growth DDM) to value all dividends from year *n*+1 onward as a terminal value, then discount that back to today.

The formula simplifies to:

**V = Σ [D₀ × (1 + g₁)ᵗ / (1 + r)ᵗ] (for t = 1 to n) + [Terminal Value / (1 + r)ⁿ]**

Where Terminal Value = D_n × (1 + g₂) / (r - g₂)

### When Two-Stage Fits

The two-stage model is preferred when the company faces a clear, identifiable inflection point:

- **IPOs and young growth companies** with a defined window of rapid expansion before slowing (e.g., a fintech firm expected to dominate market share over 7 years, then grow with the market)
- **Cyclical businesses** exiting a trough or entering a known recovery window (e.g., an automaker restructuring for 5 years, then returning to industry growth)
- **Turnarounds** where management has a specific plan to restore profitability and increase dividends over a discrete period
- **Acquisitions** where synergies are expected to fade after a known integration window
- **Regulated utilities** awaiting rate relief or infrastructure buildout with a defined end date

The two-stage model is valuable when you can credibly forecast the explicit high-growth period. If you say "this company will grow dividends at 10% for exactly 7 years, then 4% forever," the two-stage DDM directly reflects that narrative.

## Key Differences

| Dimension | H-Model | Two-Stage DDM |
|-----------|---------|---------------|
| **Growth path** | Linear decay over 2H years | Constant growth for n years, then step to stable |
| **Transition assumption** | Smooth, gradual slowdown | Abrupt shift at the boundary |
| **Inputs** | High growth, stable growth, half-life (H) | High-growth rate, stable rate, explicit period (n) |
| **Best for** | Mature companies in slow transition | Young/cyclical with clear inflection point |
| **Sensitivity** | Modest; small errors in H matter less | High; errors in *n* or the growth rates amplify |

## Practical Comparison: An Example

Consider a mid-cap software company currently paying a $2 dividend, with a cost of equity of 10%.

**Scenario A: Gradual Deceleration**
- Current growth: 12% annually
- Terminal growth: 4% annually
- H-model with H = 5 (i.e., 10-year decay period)

Using the H-model formula: V ≈ $2 × [(1.04 / 0.06) + 5 × (0.08 / 0.06)] ≈ $78

**Scenario B: Abrupt Shift**
- Years 1–5: grow at 12% per year
- Year 6 onward: grow at 4% per year
- Two-stage DDM with explicit 5-year high-growth phase

Calculating year-by-year dividends and terminal value: V ≈ $75

The values are close, but the interpretation is different. The H-model analyst is saying, "This company will slowly decelerate over 10 years." The two-stage analyst is saying, "This company will grow rapidly for 5 years, then mature overnight."

## Sensitivity and Risk

The two-stage DDM is more sensitive to forecast error. If you overestimate the length of the high-growth phase by just 2 years, the terminal value—which dominates the total value—can shift dramatically. An overly optimistic view of the high-growth period inflates the stock price.

The H-model is more forgiving because the linear decay is built in. If you misestimate H by a year or two, the impact is smaller because the model already assumes growth is decelerating every single year.

## Which to Choose

Choose the **H-model** if:
- The company is already mature and you believe growth will gradually decelerate
- You lack concrete milestones or catalysts for a discrete transition
- You want a model that is less sensitive to forecast error
- You are valuing a large, diversified, established business

Choose the **two-stage DDM** if:
- The company has a clear, time-bound growth catalyst (e.g., new product launch, market entry, restructuring)
- You can credibly forecast the explicit high-growth period from management guidance, contracts, or market dynamics
- You are valuing a startup, turnaround, or newly public company
- You have visibility into when and how the growth regime will shift

## Avoiding Common Mistakes

**H-model pitfall**: Setting H too short (say, 3 years) for a large, slowly transitioning company. This overstates the rate of deceleration and understates the value.

**Two-stage pitfall**: Setting the high-growth period too long. A 10-year explicit forecast implies extreme confidence; for most companies, anything beyond 7 years is speculative.

**Both models**: Forgetting to test sensitivity. Change *g*₁, *g*₂, *H*, or *n* by ±1 and see how much the value moves. If small changes produce huge value swings, your model is fragile.

## Terminal Value Dominance

Both models are heavily weighted toward terminal value—the value of dividends from year *n* or after year 2*H*. This is the model's greatest weakness. A small shift in terminal growth rate (*g*₂) or the cost of equity can change the total valuation by 20% or 30%. Neither model solves this problem; both require disciplined assumptions about mature-phase growth (usually in the range of GDP growth + a small premium).

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend discount model](/dividend-discount-model/) — the foundation for both models
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the broader valuation framework that includes DDM
- [Gordon growth model](/dividend-discount-model/) — the constant-growth formula embedded in both models' terminal phases
- [Cost of equity](/cost-of-equity/) — the discount rate input that drives both valuations
- [Dividend yield](/dividend-yield/) — the current return, which feeds into the terminal value

### Wider context

- [Relative valuation](/relative-valuation/) — alternative approaches using multiples instead of forecasts
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — how to stress-test model assumptions
- [Dividend](/dividend/) — the underlying source of value in DDM

</div>

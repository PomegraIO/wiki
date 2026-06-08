---
title: "Continuing Value Ratio"
description: "The percentage of total enterprise value attributable to terminal value, and what it reveals about forecast risk and analyst confidence."
keywords:
  - continuing value ratio
  - terminal value
  - dcf valuation
  - forecast risk
  - valuation proportions
  - explicit forecast period
image: "/svg/valuation.svg"
---

*In any [discounted cash flow valuation](/discounted-cash-flow-valuation/), the total enterprise value is the sum of present values from the explicit forecast period plus the present value of the terminal value. The **continuing value ratio** is the terminal value's share of that total—often expressed as a percentage. A high ratio signals that your valuation leans heavily on far-future assumptions; a lower ratio suggests confidence in near-term cash flows.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Continuing Value Ratio — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation concepts." />

<div class="wiki-infobox-caption">A diagnostic of forecast depth versus perpetuity risk.</div>

|   |   |
|---|---|
| **What it is** | Terminal value ÷ total enterprise value, expressed as % |
| **Typical range** | 60–80% for mature firms; 40–60% for growth firms |
| **Red flag** | Ratio above 85% suggests over-reliance on terminal assumptions |
| **Yellow flag** | Ratio below 40% suggests explicit forecast is too long or terminal growth too pessimistic |
| **Implication** | Higher ratio = more valuation risk concentrated in perpetuity assumptions |

</aside>

## Why the ratio matters

A continuing value ratio of 70% means that 70 cents of every dollar of fair value comes from the terminal perpetuity. If your terminal assumptions are even slightly wrong—a 0.5% error in perpetual growth rate or a 50-basis-point error in the terminal discount rate—you have materially mispriced the firm. A ratio of 50% means the forecast period is more meaningful; misses in the terminal value have less leverage over the final answer.

This is not to say that high ratios are bad. For a mature utility or consumer staple with a stable, predictable business, terminal value representing 75% of value is entirely appropriate. The business will exist and generate steady cash flows indefinitely. But for a growth company or an early-stage venture, a continuing value ratio above 75% should trigger scrutiny: are you extending the explicit period long enough? Is your terminal growth rate realistic?

## Computing the ratio

The calculation is straightforward:

Continuing value ratio = Present value of terminal value ÷ Total enterprise value

Or equivalently:

Continuing value ratio = Terminal value ratio × (discount factor from terminal year to present)

If your terminal value in Year 10 is $1B, discounted to present at a WACC of 8%, and total enterprise value is $1.5B, the ratio is roughly 67%. The ratio embeds both the size of the terminal perpetuity and how far in the future it lies; cash flows 10 years out are worth less today than cash flows in Year 3.

## Benchmarking against peers and sectors

**Utilities and consumer staples**: Continuing value ratios of 75–85% are normal and healthy. These are cash-generative, mature businesses with predictable decay into perpetuity. An analyst expecting a 45% ratio for a utility is probably being too optimistic about near-term growth or underestimating perpetual cash flow.

**Financial services**: Banks and insurance firms often show continuing value ratios of 70–80%. Their business model is to generate steady spreads and earnings in perpetuity, so the terminal assumption is foundational.

**Technology and growth**: Software companies, e-commerce platforms, and biotech firms often have continuing value ratios of 50–65%. These businesses are still in expansion phases; the explicit forecast captures meaningful share gains and margin improvement. A ratio above 75% suggests the model is leaning too hard on late-life assumptions and not capturing near-term optionality.

**Cyclical and commodity**: Mining, energy, automotive, and other cycle-exposed sectors often see ratios of 55–75%, depending on where they are in the business cycle and how far you extend the explicit period.

## Rising red flags

A continuing value ratio above 85% is a signal to pause and reconsider:

- **Is your explicit forecast period too short?** If you are using only 3 years when 7–10 is standard for the industry, extend it and push material assumptions into the detailed forecast rather than assuming perpetuity.
- **Is your terminal growth rate plausible?** A perpetual growth rate of 3% is standard. If you are using 4–5% perpetually for a firm in a low-growth developed market, you are claiming above-GDP growth forever—a big assumption that usually cannot hold.
- **Are you underestimating capex or working capital needs?** A thin explicit-period forecast understates reinvestment needs and inflates free cash flow, making the terminal perpetuity appear more valuable by contrast. Recheck capex and change-in-NWC assumptions.
- **Is terminal margin or return on capital realistic?** If the terminal year assumes ROIC far above or below cost of capital, the perpetuity assumption is doing hidden work. State the assumption plainly and test its reasonableness against peers.

## Low ratios: the opposite problem

A continuing value ratio below 40% raises different concerns:

- **Are you being too pessimistic about the long-term business?** If you assume the firm deteriorates into a near-zero-margin commodity operation by Year 12, you may be undervaluing it. Many mature firms sustain mid-single-digit margins in perpetuity; that is not pessimism, it is realism.
- **Is your explicit period unrealistically long?** If you are detailing to Year 15 and your ratio is only 35%, you are probably over-projecting growth, margin improvement, or both. Few businesses sustain 8–10% revenue growth for 15 years straight.
- **Have you implicitly assumed the company fails?** A ratio below 30% often reflects a model where the firm is expected to shrink into insignificance. Clarify: is that intentional (the firm faces secular decline) or an artifact of too-long forecast windows and reversion to low or zero terminal margins?

## Using the ratio in sensitivity and scenario analysis

The continuing value ratio is a useful diagnostic during sensitivity testing. Build a simple table:

| Explicit Forecast | Terminal Growth | Cost of Equity | CV Ratio |
|---|---|---|---|
| 5 years | 2.5% | 8.0% | 72% |
| 5 years | 3.0% | 8.0% | 75% |
| 7 years | 2.5% | 8.0% | 65% |
| 7 years | 3.0% | 8.0% | 68% |

This matrix shows how the ratio changes as you shift the key levers. If extending the forecast period by 2 years drops the ratio by 7 percentage points, you know that the ratio is moderately sensitive to forecast length. If pushing terminal growth from 2.5% to 3.0% raises the ratio by only 2 points, that variable is less influential. Investors and boards can then assess which assumptions they trust most.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the framework that produces the ratio
- [Terminal Value](/terminal-value/) — the numerator of the ratio
- [Explicit Forecast Period](/explicit-forecast-period/) — the denominator's complement
- [Convergence Assumption in DCF](/convergence-assumption-dcf/) — the perpetuity assumption in the terminal calculation
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing how the ratio shifts across scenarios

### Wider context

- [Weighted Average Cost of Capital](/weighted-average-cost-of-capital/) — the discount rate baked into both forecast and terminal value
- [Free Cash Flow](/free-cash-flow/) — the cash metric being projected and perpetualized
- [Going Concern](/going-concern/) — the perpetual-operations assumption underlying terminal value
- [Acquisition](/acquisition/) — deal valuations often benchmark continuing value ratios against acquirer expectations

</div>

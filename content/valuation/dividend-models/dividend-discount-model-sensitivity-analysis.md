---
title: "Sensitivity Analysis in Dividend Discount Models"
description: "Build sensitivity tables for dividend discount models to see how changes in growth rate and discount rate affect valuation and identify key value drivers."
keywords:
  - dividend discount model sensitivity analysis
  - ddm sensitivity table
  - valuation sensitivity
  - growth rate assumptions
  - discount rate impact
  - financial modeling
image: "/svg/valuation.svg"
---

*A **dividend discount model sensitivity analysis** shows how a stock's fair value swings when you adjust the growth rate or required return assumptions—a critical reality check because DDM outputs are extraordinarily sensitive to small input changes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sensitivity Analysis in DDM — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Sensitivity tables reveal which assumptions drive the bulk of value.</div>

|   |   |
|---|---|
| **What it is** | A table varying two or more DDM inputs to show resulting valuations |
| **Primary inputs tested** | [Discount rate](/cost-of-equity/) and growth rate |
| **Typical range** | ±0.5–2.0% around base assumptions |
| **Why it matters** | Exposes assumption risk and investor judgment calls |
| **Red flag** | Value swings >50% within realistic input bounds |

</aside>

## Why Small Changes Produce Large Valuation Swings

The dividend discount model's core formula—dividing expected cash flow by (discount rate minus growth rate)—makes valuations hyperresponsive to the denominator. A stock with a $1 annual dividend growing at 5% and a required return of 10% trades at $20. If the discount rate rises just one percentage point to 11%, that same stock drops to $16.67. The 100-basis-point shift obliterates nearly 17% of value.

This sensitivity is *not* a bug—it reflects real economic truth. Higher interest rates truly do reduce the present value of distant cash flows. But it means your DDM output is only as good as your assumption inputs, which are inherently uncertain. A sensitivity table lets you map that uncertainty visually and decide whether the model's answer is robust or dependent on heroic guesses.

## Building a Standard Sensitivity Table

The canonical sensitivity table puts discount rate along one axis and growth rate along the other, with intrinsic value in each cell. Let's use a practical example: a company paying $2.50 in annual dividends.

**Base assumptions:**
- Discount rate: 9%
- Growth rate: 3%
- Current dividend: $2.50
- Formula: Value = Next Year's Dividend / (r − g) = ($2.50 × 1.03) / (0.09 − 0.03) = $42.83

Now vary both inputs:

|   | **Growth 1%** | **Growth 2%** | **Growth 3%** | **Growth 4%** | **Growth 5%** |
|---|---|---|---|---|---|
| **Discount 7%** | $47.50 | $51.25 | $55.42 | $60.42 | $66.67 |
| **Discount 8%** | $40.00 | $42.86 | $46.43 | $51.07 | $57.14 |
| **Discount 9%** | $34.29 | $36.67 | $39.63 | $43.75 | $50.00 |
| **Discount 10%** | $29.63 | $31.25 | $33.65 | $37.14 | $41.67 |
| **Discount 11%** | $25.63 | $26.92 | $28.75 | $31.43 | $35.00 |

Each cell reflects the fair value under that combination. The base case (9% discount, 3% growth) sits at $39.63. But notice: at 7% discount and 5% growth, value nearly doubles to $66.67. Flip to 11% discount and 1% growth, and you're down to $25.63.

## Interpreting Sensitivity Ranges

The width of the range in your table tells you whether the valuation is robust. If all reasonable combinations cluster tightly—say within a $38–$44 band—you can have confidence in the central estimate. If they sprawl across $20–$65, the model is telegraphing that the answer hinges on judgment calls you cannot defend with hard data.

Benchmark the range against comparable company valuations or the current market price. If your sensitivity table produces a $50 fair-value midpoint but the stock trades at $35 and your comparable-companies analysis suggests $38, that's signal to revisit your assumptions. Perhaps your growth estimate is too optimistic, or your discount rate is too low. Misalignment isn't failure—it's a prompt to reality-check your inputs.

## Key Assumptions Worth Stress-Testing

**Discount rate** fluctuates with interest rates and perceived risk. A 50-basis-point change—from 9% to 9.5%, say—is not extreme. When the Federal Reserve signals rate moves or a company's credit profile shifts, this assumption deserves re-examination.

**Perpetual growth rate** is the most dangerous assumption because it extends forever. Assuming 5% growth indefinitely for a company in a 2% nominal GDP-growth world is heroic. Most analysts anchor it to long-term GDP or industry growth, or they use a two-stage model: high growth for 5–10 years, then a terminal rate tied to macro conditions. A sensitivity table forces you to be explicit about this choice.

**Next year's dividend** (the numerator) is less sensitive in percentage terms, but changes here ripple through. If you forecast a dividend cut or surge because of a capital allocation shift, that edge case belongs in the table as an alternate row or scenario.

## Common Mistakes in Building Sensitivity Tables

**Ranges too narrow**: Testing ±0.25% around your assumptions glosses over real uncertainty. Use ranges that span credible debate—typically ±1% for discount rate, ±0.5–1.5% for growth rate, depending on the business.

**Mechanical without narrative**: A table without interpretation is just numbers. Always identify which cells are realistic given current conditions, which are bull cases, and which are bear cases. Label them: "Recession scenario" (high discount, low growth), "Goldilocks case" (your base), "Secular-growth scenario" (low discount, high growth).

**Ignoring the negative territory**: In the formula (r − g), if g approaches r, value shoots to infinity and the model breaks. A sensitivity table should never push g above r; if your range does, narrow it or flag the limitation in your analysis.

## Extending to a Two-Stage Model

Single-stage DDMs assume stable growth forever. Real analysts often use two-stage models: high growth for 5–10 years, then stable perpetual growth. Sensitivity analysis becomes more complex but even more valuable.

In two-stage DDM, you vary not just the terminal growth rate and discount rate, but also the explicit-forecast period and the near-term growth rate. A table might test whether lengthening the high-growth window from 5 to 7 years swamps the terminal-value estimate. It often does—another reality check on assumption risk.

## When Sensitivity Analysis Points to Trouble

A sensitivity table that produces wildly divergent outcomes under small input perturbations is telling you the DDM is the wrong tool. Some stocks—deep-cyclicals, distressed firms, those with erratic dividends—resist stable perpetual-growth assumptions. Acknowledge that limit. Consider switching to [discounted cash flow valuation](/discounted-cash-flow-valuation/) or [relative valuation](/relative-valuation/) frameworks instead.

The goal of sensitivity analysis is not to arrive at a pinpoint value. It's to understand which assumptions matter most, to recognize the range of defensible answers, and to make conscious trade-offs between optimism and conservatism. A well-built table answers not "what is this stock worth?" but "under what conditions would these valuations hold?"

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the foundational perpetual-growth valuation formula
- [Cost of Equity](/cost-of-equity/) — how to estimate the discount rate for a DDM
- [Dividend Discount Model for Cyclical Companies](/dividend-discount-model-cyclical-companies/) — adapting DDM when dividends surge and collapse
- [Excess Return Dividend Model](/excess-return-dividend-model/) — an alternative decomposition linking dividends to returns on retained earnings
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — a broader multi-stage framework when dividends don't reflect true economic capacity

### Wider context

- Financial Modeling — the mechanics of assumption-setting and scenario analysis
- Valuation — frameworks across intrinsic value, comparable companies, and market-based approaches
- [Stock](/stock/) — equity ownership and the claims on dividends

</div>

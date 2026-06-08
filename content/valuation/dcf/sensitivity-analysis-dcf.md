---
title: "DCF Sensitivity Analysis"
description: "Mapping how terminal growth and WACC assumptions jointly drive the output valuation, revealing which inputs most influence the final price."
keywords:
  - sensitivity analysis
  - dcf assumptions
  - valuation range
  - terminal growth
  - discount rate risk
image: "/svg/valuation.svg"
---

*A DCF model produces a single number—but that number rests on guesses. **Sensitivity analysis** shows how much that output shifts if your assumptions change. It's the honest accounting of how much your valuation depends on hope versus fundamental math.*

## Why sensitivity analysis matters

Every DCF is built on assumptions: the [discount rate](/discount-rate/), terminal growth, [reinvestment rates](/cash-conversion-cycle/), far-future [profit margins](/operating-margin/). Change any one of them, and the output changes. Often by billions of dollars.

A naive analyst might build a single "base case" and declare it the value. A thoughtful analyst builds a base case, then asks: What if I'm wrong? If I'm wrong by 0.5%, does that destroy the investment thesis? Or does the thesis hold even across a wide range of plausible outcomes?

Sensitivity analysis answers that question. It's also a tool for spotting fragile assumptions: if a 1% change in WACC swings your valuation by 30%, you're overly dependent on nailing that single input, and your margin of safety is thin.

## The two-way table: WACC and terminal growth

The classic sensitivity output is a two-dimensional table. One axis is WACC (say, 6% to 11%); the other is terminal growth rate (say, 1% to 4%). Each cell shows the resulting equity value.

Here's a stylized example for a $5B revenue firm:

|        | 1% Growth | 2% Growth | 3% Growth | 4% Growth |
|--------|-----------|-----------|-----------|-----------|
| **6% WACC** | $52B      | $58B      | $67B      | $79B      |
| **7% WACC** | $45B      | $50B      | $57B      | $66B      |
| **8% WACC** | $40B      | $43B      | $48B      | $56B      |
| **9% WACC** | $35B      | $38B      | $42B      | $48B      |
| **10% WACC** | $31B    | $33B      | $36B      | $41B      |

This table tells a story. At 8% WACC and 3% growth, value is $48B. But if you're wrong and WACC is actually 7%, value jumps to $57B. If growth is 4% instead, it's $56B. If both assumptions are off in your favor, you get $66B.

But here's the kicker: if WACC is 10% (higher risk than you thought), or if long-term growth is only 1%, the valuation collapses to $31B. **The range is $31B to $79B** for the same company. Which assumption gets right determines whether you buy, hold, or sell.

## Why these two inputs?

WACC and terminal growth are the heavyweights of DCF because they drive the terminal value—often 60–80% of total value. In a standard DCF, terminal value is:

**TV = Year 5 FCF × (1 + g) / (WACC − g)**

Notice the denominator: WACC minus growth. As growth creeps toward WACC, the denominator shrinks and the fraction explodes. A 3% growth at 8% WACC gives a denominator of 5%. A 3.5% growth at 8% WACC gives 4.5%. That 0.5% shift widens the terminal value multiple by 11%.

Similarly, a 0.5% shift in WACC from 8.0% to 7.5% widens the denominator from 5% to 4.5%, also an 11% increase in value. The sensitivity is *symmetric* in WACC and growth—a dangerous symmetry, because WACC is often more controllable (you can research competitor costs and [debt](/corporate-bond/) spreads) while growth is speculative.

## Building a sensitivity table

The mechanics are simple:

1. Define your base-case assumptions: WACC = 8%, terminal growth = 3%, forecast [free cash flow](/free-cash-flow/) = $2B in year 5.
2. Choose a range: WACC from 6% to 10% (±2%), growth from 1% to 5% (±2%).
3. For each WACC–growth pair, plug into the DCF formula and calculate resulting equity value.
4. Plot the results in a table, highlighting your base case.

Most software (Excel, financial modeling platforms) makes this a one-line lookup or data-table function. The art is choosing the ranges. Too narrow, and you're not stress-testing. Too wide, and you include implausible scenarios (a 5% perpetual growth rate for most mature companies is fantasy; a 6% WACC assumes no [equity risk](/market-risk/) premium).

## One-way sensitivity: isolating single inputs

A one-way sensitivity holds everything constant except one variable and plots the result as a line graph.

For instance, hold WACC at 8% and growth at 3%, then vary the [profit margin](/operating-margin/) assumption from 4% to 8%. You'll see a line sloping upward: higher margins mean higher cash flows and higher value. If the line is steep, margin assumptions matter a lot. If it's flat, you're less exposed to that input.

One-way sensitivity is useful for identifying your true risks. Many analysts assume cost inflation, tax changes, or capital expenditure surprises are decisive, only to run a sensitivity and discover that 99% of the value swing comes from terminal growth assumptions, not operation detail.

## Multi-factor sensitivity: scenarios

A richer approach is scenario analysis: define a "base case," a "bull case," and a "bear case," each internally consistent.

- **Base case:** 8% WACC, 3% terminal growth, 5% margin. Value = $48B.
- **Bull case:** 7% WACC (lower risk perceived), 4% growth (competitive strength holds), 6% margin (scale advantages). Value = $66B.
- **Bear case:** 9% WACC (higher risk), 2% growth (commoditizing market), 4% margin (price pressure). Value = $38B.

This three-point range ($38B to $66B) reflects a realistic band of outcomes tied to strategic narratives, not just mathematical extremes.

## Using sensitivity to set a price target

A disciplined investor combines sensitivity analysis with a margin of safety.

Suppose sensitivity shows a range of $35B to $65B. You're not equally confident in all outcomes. You might assign:

- 50% probability to base case = $48B.
- 25% probability to bull case = $66B.
- 25% probability to bear case = $38B.

**Probability-weighted value = 0.5×$48B + 0.25×$66B + 0.25×$38B = $51B.**

If the stock is trading at $40B, it's cheap. If it's at $55B, it's fair. If it's at $65B, it's expensive—the market is pricing in the bull case with high confidence, leaving no margin for error.

## Pitfalls: garbage in, garbage out

Sensitivity analysis doesn't cure bad assumptions—it exposes them.

If your base case WACC is 5% (unrealistically low [cost of equity](/cost-of-equity/)), a sensitivity table will show absurdly high valuations even in the "bear case." Garbage assumptions produce garbage ranges. Before running sensitivity, sanity-check your inputs against peers, historical data, and [risk-free rates](/treasury-bill/).

Also, sensitivity analysis can encourage false precision. A table suggesting value is "between $40B and $60B" might imply confidence you don't have. The true answer is: I don't know. This range shows what factors matter most, and how wide the uncertainty is.

Finally, don't assume the axes are independent. If [interest rates](/interest-rate/) rise, WACC rises *and* growth often falls (corporations cut capex). Sensitivity tables treat them separately, which understates tail risk in a rising-rate environment.

## Communicating sensitivity results

A clean sensitivity table beats pages of prose. One table and one sentence—"Base case value is $48B; plausible range is $38B–$66B; key driver is terminal growth assumption"—conveys more than paragraphs of caveats.

For presentations, highlight the base case cell. Color-code the table: green for upside, red for downside, yellow for the central band. Let the visual reveal which regions are most likely and which are outliers.

And always state your assumptions clearly: "Assumes WACC of 8%, calibrated to current [Treasury](/treasury-bond/) rates plus 3.5% equity [risk premium](/market-risk/); terminal growth of 3%, consistent with long-run GDP growth; margin expansion from 5% to 6% over 5 years based on operational initiatives."

## See also

<div class="wiki-seealso">

### Closely related

- Discounted Cash Flow Valuation — the model for which sensitivity is performed
- Terminal Value — the output most sensitive to growth and WACC assumptions
- [WACC](/cost-of-equity/) — the discount-rate input most often stress-tested
- [Return on Invested Capital in DCF](/return-on-invested-capital-dcf/) — another high-impact input worth one-way sensitivity
- [Excess Return DCF Model](/excess-return-dcf/) — alternative DCF format with similar sensitivity structure

### Wider context

- Margin of Safety — the investment discipline enabled by sensitivity analysis
- [Cost of Equity](/cost-of-equity/) — the equity component of WACC
- Valuation — the broader discipline of which sensitivity is a tool
- [Scenario Analysis](/scenario-analysis/) — the strategic companion to financial sensitivity

</div>

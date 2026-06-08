---
title: "Gordon Growth Model Limitations and When It Breaks Down"
description: "The Gordon Growth Model fails when growth rate approaches discount rate, terminal values turn negative, or dividend cuts occur. Learn its blind spots."
keywords:
  - gordon growth model limitations
  - dividend discount model breakdown
  - terminal value valuation issues
  - constant growth assumption
  - dividend valuation problems
---

*The **Gordon Growth Model** assumes a constant dividend growth rate forever—a convenient fiction that produces elegant valuations. But it breaks down sharply when growth approaches the discount rate, when dividend cuts occur, or when the company is in a mature, uncertain state. The model's inputs are so sensitive to small changes that small errors in estimating the terminal growth rate produce massive valuation swings.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gordon Growth Model — Where it fails</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Elegant in theory; fragile and unreliable at the margins.</div>

|   |   |
|---|---|
| **Formula** | P = D₁ / (r − g), where g = growth rate, r = discount rate |
| **Fatal assumption** | Constant g in perpetuity; often wrong |
| **Worst case** | When g ≥ r, value is undefined or infinite |
| **Sensitivity** | 1% change in g or r often swings value by 20–50% |
| **Best fit** | Stable, mature companies with steady dividends |
| **Worst fit** | High-growth, cyclical, or non-dividend-paying firms |
| **Real use** | Terminal value component of multi-stage DCF; rarely standalone |

</aside>

## The model and its math

The **Gordon Growth Model** (also called the Perpetuity Growth Model) values a stock as:

**P = D₁ / (r − g)**

where D₁ is the next year's expected dividend, r is the required return (discount rate), and g is the constant growth rate, assumed to hold forever. Rearranging: the value per share is the next dividend divided by the spread between required return and growth.

The elegance is seductive. It requires only three inputs: a single dividend estimate, a cost-of-equity estimate, and a terminal growth assumption. It has been taught in every business school for decades.

But that elegance is also the model's fatal flaw: it oversimplifies a world of companies and returns into a single perpetual constant. Almost every input is fragile.

## The growth-rate paradox

The most glaring problem: **when g approaches r, the model breaks**. 

If you estimate that a company will grow at 4% forever and your cost of equity is 5%, the denominator (5% − 4% = 1%) is tiny. The P/D₁ ratio becomes 100×. A stock paying a $1 dividend is worth $100. A trivial 0.5% change in either input—growth down to 3.5% or cost of equity up to 5.5%—cuts the valuation in half.

If growth ever exceeds the discount rate (g > r), the formula yields negative value, which is nonsensical—a stock cannot be worth less than zero. Some analysts interpret this as "the stock is worth infinity," a reductio ad absurdum suggesting the model has failed.

In practice, this problem arises when:

- **Terminal growth set too high**: An analyst assumes a mature company will grow at 3.5% forever, but the cost of equity is only 4%. The spread is so thin that valuation is unreliable.
- **Cost of equity underestimated**: A researcher assumes a required return of 6%, but the stock is actually riskier (required return 7%). The gap narrows, and the valuation inflates retroactively.
- **High-growth companies**: A company growing 15% annually is being valued under a "terminal phase" where growth slows to 5%. But if the transition is abrupt (e.g., end of Year 5), the Gordon model is misapplied unless layered into a multi-stage [discounted cash flow](/discounted-cash-flow-valuation/) model.

## The assumption of constant growth

The model's second pillar—**constant growth forever**—is empirically absurd. No company grows at a constant rate indefinitely. Mature utilities might grow close to GDP growth (2–3%); tech companies in their prime grow at 15–25%; startups grow at 100%+. All eventually slow.

Examples of when this assumption fails badly:

- **Dividend cuts**: A company faced with a recession might cut its dividend by 30%. The Gordon model, which assumes unbroken growth, does not accommodate this. It assumes the cut is permanent (new lower base with g growth from there), or it ignores the cut entirely. Valuation is wrong either way.
- **Cyclical industries**: A cyclical company (construction, automotive) does not have a steady growth rate. It cycles through booms and busts. Plugging an average long-term growth rate into the Gordon model masks the volatility and timing risk.
- **Dividend policy changes**: A company might shift from dividends to share buybacks, changing the D₁ input entirely. A company might slash dividends to fund capex. The model assumes the policy is stable forever.

## Sensitivity and estimation risk

Even small errors in the three inputs produce vast valuation swings. Consider a mature stock:

- Estimate: D₁ = $2, r = 8%, g = 3%
- Value = $2 / (0.08 − 0.03) = $40 per share

Now, suppose you revise g upward by just 0.5% (from 3% to 3.5%):

- Value = $2 / (0.08 − 0.035) = $44.44 per share

That's an 11% increase in value from a 0.5 percentage-point change in growth. Worse:

- If g = 4%, value = $2 / 0.04 = $50 (a 25% jump)
- If g = 4.5%, value = $2 / 0.035 = $57.14 (a 43% jump)

This sensitivity is not a feature; it is a weakness. In practice, estimating a company's long-term growth rate is notoriously hard. Analyst forecasts for growth rates differ widely, especially for mature companies. The Gordon model amplifies those disagreements into implausible valuation ranges.

## When discount rate is uncertain

The same problem afflicts the cost of equity (r). Using the [Capital Asset Pricing Model](/capital-asset-pricing-model/), r = risk-free rate + β × (market risk premium). Each of these is estimated, and small changes compound:

- **Risk-free rate**: Often taken as the 10-year Treasury yield, which fluctuates. A 50 bps rise cuts valuations across the board.
- **Beta**: Estimated from historical returns; noisy and regime-dependent.
- **Market risk premium**: Assumed to be 5–7%; this is contentious and time-varying.

An analyst estimating r as 7% versus 8% is a small difference in a spreadsheet but a large difference in valuation. The Gordon model is unforgiving.

## Inapplicability to non-dividend-paying stocks

The Gordon model explicitly values *dividends*. If a company does not pay dividends, D₁ = 0, and the model yields value of zero—clearly wrong for a profitable, growing company like Amazon or Tesla that reinvests all earnings.

Some analysts adapt the model by substituting free cash flow or distributable earnings for D₁. But this moves away from the model's core logic and introduces fresh estimation headaches. A [discounted cash flow](/discounted-cash-flow-valuation/) model is more transparent in this case.

## Better uses: terminal value in multi-stage DCF

The Gordon Growth Model's most reliable use is **not as a standalone valuation tool** but as a component in a multi-stage [discounted cash flow](/discounted-cash-flow-valuation/) model. 

A typical three-stage DCF forecasts cash flows explicitly for Years 1–5 (high growth), applies a slower growth rate for Years 6–10 (transition), then uses the Gordon model to value the business from Year 11 onward (terminal value). This limits the model's exposure: you are not relying on a single perpetual rate for a vast future, but rather anchoring a forecast explicitly to a transition period.

Even here, the model is fragile. The terminal value (Year 11+) often represents 60–80% of total DCF value for a mature company, so errors in the terminal growth assumption still have enormous impact. Many practitioners now use alternative terminal assumptions (e.g., a fixed revenue multiple, an [exit multiple](/relative-valuation/)) to cross-check the result.

## Red flags in practice

Use the Gordon model with extreme caution—or avoid it—when you see:

- **Growth rate within 2 percentage points of cost of equity**: Valuations become hypersensitive. A small forecast error produces wild swings.
- **Declining or volatile dividends**: The assumption of constant growth is visibly false.
- **Rapidly changing industry**: Tech, biotech, and other innovating sectors have uncertain long-term growth rates. Applying a fixed perpetual rate is arbitrary.
- **Cyclical business**: Utilities and consumer staples with smooth, predictable dividends are better candidates.
- **Non-dividend payer**: The model requires adaptation, reducing its utility.

## Better alternatives

- **Multi-stage DCF**: Models growth in phases, with explicit forecasts and a more defensible terminal value.
- **Relative valuation**: Compare the stock to peers using [price-to-earnings](/price-to-earnings-ratio/) or [price-to-book](/price-to-book-ratio/) multiples, avoiding the perpetuity assumption.
- **[Residual income model](/return-on-equity/)**: Values the company as book value plus the present value of future excess returns; more flexible on payout policy.
- **[Sum-of-the-parts](/relative-valuation/)**: For conglomerates, value divisions separately; avoids a single growth rate for heterogeneous businesses.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — The broader family of models valuing stocks via dividends
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Multi-stage models that use the Gordon model as a terminal-value component
- [Cost of Equity](/cost-of-equity/) — How to estimate the discount rate r
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — Framework for estimating required return
- [Dividend Yield](/dividend-yield/) — The current yield on dividends; relevant for Gordon model calibration

### Wider context

- [Relative Valuation](/relative-valuation/) — Price-to-earnings and other multiples as alternatives to DCF
- [Fair Value](/fair-value/) — Determining what an asset should be worth
- [Valuation Risk](/market-risk/) — How estimation errors affect investment decisions
- [Stock](/stock/) — The security being valued

</div>

---
title: "Net Operating Loss Carryforwards in DCF Valuation"
description: "How to value net operating loss carryforwards in DCF models, including tax-shield benefits, Section 382 limits, and expiry schedules."
keywords:
  - net operating loss carryforward
  - nol tax shield
  - dcf valuation
  - section 382 limitations
  - tax-loss carry forward valuation
---

*The value of a company's **net operating loss carryforward** (NOL)—the right to offset future profits against past losses—depends entirely on whether the company will earn enough future taxable income to use it. Building that probability into a DCF model requires three layers: forecasting taxable income, capping usage by tax law, and discounting for timing risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Net Operating Loss Carryforward — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">A past loss becomes a future tax shield only if profits materialise.</div>

|   |   |
|---|---|
| **What it is** | Right to reduce future taxable income by prior-year losses |
| **Primary value source** | [Tax shield](/deferred-tax-asset/) on projected future profits |
| **Biggest risk** | [Section 382 limitation](/corporate-income-tax/) shrinks annual usage after ownership change |
| **Time limit** | Federal: 20 years (indefinite if post-2017 loss); state rules vary |
| **Discount factor** | Higher if profits are uncertain or far out |
| **Common scenario** | Unprofitable company acquired; buyer values the NOL |

</aside>

## What an NOL Is, and Why It Has Value

A net operating loss is a negative [net income](/income-statement/) in a tax year: revenue minus deductible expenses comes out below zero. In most jurisdictions, companies cannot claim a cash refund for that loss. Instead, they carry it forward (or backward) and use it to reduce taxable income in profitable years.

The value is straightforward: if a company carried a $50 million NOL and faces a 25% marginal tax rate, it saves $12.5 million in taxes the first time it applies the loss to offset $50 million of future profits. But that value is not automatic. The company must generate sufficient taxable income to use it. A perpetually unprofitable firm has a worthless NOL. A startup with a large loss today might use it in a few years or never. The DCF modeller must therefore forecast when and whether the loss will be deployed.

## Building NOL Usage into Free Cash Flow Projections

In a conventional DCF, [free cash flow](/free-cash-flow/) is discounted back to present value. The presence of an NOL modifies the tax calculation in each future year.

Start with the standard formula:

> **Taxable income = Revenue − Operating Expenses − Depreciation − Other deductions**  
> **Taxes = Taxable income × Tax rate**

When an NOL exists, the formula becomes:

> **Taxable income (after NOL) = max(0, Taxable income − Remaining NOL balance)**  
> **Taxes = Taxable income (after NOL) × Tax rate**  
> **Remaining NOL balance = max(0, Remaining NOL balance − Taxable income)**

In each projection year, you:
1. Calculate pre-loss taxable income.
2. Subtract available NOL, but not below zero.
3. Pay tax only on the net amount.
4. Reduce the NOL balance by the amount used.
5. Carry forward any unused portion.

This logic naturally captures the tax benefit as income rises. Early years may generate small or zero taxable income; the NOL remains dormant. Later, when profits ramp, the NOL is deployed, reducing taxes owed and boosting [free cash flow](/free-cash-flow/).

## Section 382: The Ownership-Change Ceiling

The largest trap is **Section 382** of the US tax code (most countries have an equivalent). When ownership of a loss-making company changes substantially—typically more than 50 percentage points in a three-year window—the annual NOL usage is capped.

The cap is: **Annual NOL deduction = Fair market value at ownership change × Long-term tax-exempt bond rate**

If a company worth $100 million at the time of acquisition has the ownership change occur, and the tax-exempt bond rate is 3%, the ceiling is $3 million per year. An NOL of $200 million cannot be used to offset more than $3 million of taxable income per year; the company would need ~67 years to exhaust it. In practice, expiry (usually 20 years) arrives first, and much of the loss is never used.

Section 382 applies automatically and is non-negotiable. It exists to prevent tax-loss trafficking: buying a loss-making shell specifically to shelter an unrelated profitable business's income. In a DCF, you must:

1. Identify whether an ownership change has occurred (or will occur as part of the acquisition you are valuing).
2. Calculate the Section 382 limit.
3. Apply the lower of (a) taxable income and (b) Section 382 limit in each year.
4. Reduce the expected tax benefit significantly if the limit is small relative to the NOL balance.

A $100 million NOL behind a $3 million-per-year cap and a 20-year expiry window is much less valuable—only $60 million (20 years × $3 million) can ever be used, even if profits are high. The remaining $40 million expires worthless.

## Probability Weighting and Timing Uncertainty

Not all NOLs are deployed with certainty. If a company's earnings forecast is uncertain, the tax shield is too.

Two practical approaches:

**Scenario 1: Conservative forecasting.** Include NOL usage only in projection years where you have high conviction the company will be profitable. If the forecast becomes negative in year 7, stop crediting NOL usage at year 6. This naturally penalises uncertain cases.

**Scenario 2: Probability-weighted approach.** Estimate the probability that cumulative taxable income will reach each successive year of the NOL balance. If there is a 90% chance of generating $20 million of taxable income in years 1–5, and an 70% chance in years 1–10, then weight the year-10 portion at 70%. This is more precise but requires fine-grained earnings conviction.

The earlier the NOL is expected to be used, the more valuable it is. A $50 million NOL used in year 2 is worth far more than the same loss used in year 18, because the tax savings arrive sooner and face less [discount-rate](/discount-rate/) erosion.

## State and International Complications

Many US states impose their own NOL rules, separate from federal law. Some cap carryforward periods shorter than 20 years; others have tighter Section 382 rules. A company filing in multiple states may face fragmented NOL utilization—federal and state losses expire on different schedules, and a federal NOL may be usable while state losses are exhausted.

Outside the US, tax-loss carryforward rules vary dramatically. Some countries limit the percentage of annual profit that can be offset (e.g., 60% in the European Union). Others require tracing NOLs to specific business units. In cross-border M&A, the target's NOLs may be worthless to the parent if they cannot be consolidated for tax purposes.

Always check the jurisdiction's specific rules and whether any ownership change triggers additional limitations.

## Expiry Dates and the Real Deadline

Federal NOLs generated in tax years **before 2018** can be carried forward for 20 years. Those from 2018 onward can be carried forward indefinitely but face a limitation on annual use (up to 80% of taxable income per year, under the Tax Cuts and Jobs Act). This is another constraint to model.

Forgetting expiry is a common DCF error. A company with a $100 million NOL and a flat 20-year forecast may appear to have a $25 million tax benefit (at 25% tax rate), but if the NOL expires in year 15 and profitable years are back-loaded, much of it is wasted. Always list expiry dates in a separate table and check that cumulative projected income reaches the NOL balance before expiry.

## Adjusting Terminal Value for Unused NOL

If your projection period extends 10 years but the NOL has a 20-year horizon, some loss remains at the end. The question is whether to credit it in terminal value.

Most practitioners ignore it: they assume the company's steady-state profitability, reflected in the terminal-value multiple or perpetuity calculation, implicitly prices any remaining NOL at zero (because they are valuing a mature, profitable firm that has likely exhausted the NOL or faces declining profitability). This is conservative and acceptable.

If you wish to credit residual NOL in terminal value, calculate how much remains unused and discount it forward at your tax rate and WACC. This only adds material value if the terminal period is still within the NOL expiry window and cumulative income is forecast to be high. In most mature-company DCFs, this adjustment is immaterial.

## Practical Checklist for DCF Modelling

1. **Identify the NOL balance and expiry date** — confirm jurisdiction and any special rules.
2. **Check for Section 382 (or local equivalent) — calculate the annual usage cap.** If an ownership change is imminent, engage tax counsel to compute the limit.
3. **Project taxable income year-by-year**, including all applicable adjustments (depreciation, amortization, extraordinary items).
4. **Apply NOL usage in order:** subtract available loss from each year's taxable income (subject to Section 382 cap); carry unused balance forward.
5. **Verify cumulative usage does not exceed NOL balance or expiry window.**
6. **Discount the tax benefit** at your company's [cost of equity](/cost-of-equity/) or WACC, same as cash flows.
7. **Document assumptions** — expiry date, probability of usage, Section 382 limit, state-specific rules.
8. **Stress-test:** model scenarios where profitability is weaker or delayed, showing how the tax benefit erodes.

An NOL is real economic value, but only if the numbers work out. In a DCF, that scrutiny is non-negotiable.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — foundational DCF mechanics and discount-rate selection
- [Tax shield](/deferred-tax-asset/) — how future tax benefits are valued
- [Cost of equity](/cost-of-equity/) — discount rate for equity cash flows, used to present-value NOL benefit
- [Corporate income tax](/corporate-income-tax/) — the statutory tax rate that determines the NOL's dollar benefit
- [DCF valuation for cyclical businesses](/dcf-for-cyclical-businesses/) — normalising income when forecasting is uncertain

### Wider context

- [Acquisition](/acquisition/) — NOLs are often a driver of deal value
- [Earnings per share](/earnings-per-share/) — tax benefit flows through to EPS
- [Revenue recognition](/revenue-recognition/) — determining taxable vs. book income
- [Sensitivity analysis in valuation](/sensitivity-analysis-valuation/) — testing NOL assumptions' impact on value

</div>

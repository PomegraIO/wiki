---
title: "Free Cash Flow to Equity Valuation"
description: "A valuation method that values equity by discounting the free cash flows available to equity holders after debt payments at the cost of equity."
keywords:
  - free cash flow to equity
  - FCFE
  - levered valuation
  - equity valuation
  - cost of equity
image: "/svg/valuation.svg"
---

*A **free cash flow to equity (FCFE)** valuation values a company's equity by discounting the cash available to equity holders—after the company has paid interest and principal to debt holders—at the [cost of equity](/cost-of-equity/). It is the levered cousin of [free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/), and it is more restrictive but sometimes more direct when debt levels are complex or shifting.*

## What FCFE is

FCFE is the cash flow that remains after a company has paid all operating expenses, taxes, capex, and changes in working capital, and has serviced all debt holders. It is the cash truly available for shareholders to withdraw or reinvest.

The calculation begins with operating free cash flow (EBIT times 1 minus tax rate, plus depreciation and amortization, minus capex, minus working capital changes). From that, you subtract interest and principal payments to debt holders and add back any new debt issued. The result is free cash flow to equity: what equity holders can claim.

Valuation is then the present value of FCFE streams, discounted at the cost of equity.

## FCFE vs. FCFF: the structural choice

[Free cash flow to firm (FCFF) valuation](/free-cash-flow-to-firm-valuation/) is the standard approach. You value the entire enterprise by discounting cash available to all capital providers—debt and equity—at the weighted average cost of capital. You then subtract net debt to get equity value.

FCFE is the alternative. You value equity directly by discounting cash available only to equity holders at the cost of equity, skipping the weighted-average step. Conceptually, they should yield the same result if assumptions are consistent.

**When FCFE is cleaner:** When a company has complex, changing debt schedules—private equity backed firm with a detailed debt paydown plan, or a company in refinancing. FCFE lets you model debt flows explicitly.

**When FCFE is messier:** When debt is stable or projected to change at an unknown pace. Varying debt levels mean the cost of equity varies (higher leverage increases equity risk), making the discount rate itself dynamic and harder to estimate.

## Building FCFE forecasts

Start with a projection of operating free cash flow: NOPAT (earnings before interest and taxes after tax adjustments) plus depreciation minus capex minus changes in working capital.

From NOPAT in year one, subtract the after-tax cost of debt (interest paid times 1 minus the tax rate). Then adjust for debt activity: add new borrowing, subtract principal repayment. The result is free cash flow to equity for year one.

Repeat for each year of the forecast period. In the terminal year, assume debt-to-value or debt-to-EBITDA stabilizes, so debt grows at the same rate as the business and FCFE grows at a stable perpetual rate.

## The leverage problem

A company's [cost of equity](/cost-of-equity/) depends on its leverage. Debt is cheap (because debt holders have priority); equity is expensive (because equity holders are residual). A company with no debt has lower cost of equity than an identical company with high debt.

In FCFE valuation, if you are forecasting changing debt levels, your cost of equity changes in parallel. In year one, with low debt, cost of equity might be 10%. In year five, if leverage has increased, cost of equity might be 11%. Should you use the current cost of equity, the average, or year-specific costs?

This is cumbersome. Most practitioners default to FCFF (value the firm at a constant weighted-average cost of capital, then subtract net debt) as the cleaner approach. FCFE shines only when debt levels are deterministic and explicit.

## FCFE for non-dividend payers

Unlike [dividend discount models](/dividend-discount-model/), which are worthless for non-paying companies, FCFE valuation works perfectly for any company regardless of dividend policy. A company that generates FCFE of 100 million but reinvests it all is valued based on that 100 million, not on the zero dividends paid.

This is the key advantage over dividend-based models. It says: the company's value depends on cash generated, not on management's decision to distribute it. If you trust the cash flow forecast, FCFE is a powerful tool.

## The practical challenge: debt paydown

For a leveraged company with explicit debt paydown, FCFE is the natural choice. You project revenues, margins, capex, and then specify how much debt the company will pay down each year. Subtract that debt paydown (net of any new borrowing), and the residual is FCFE.

But this requires a strong view on debt policy. If you forecast debt paydown too aggressively, you undervalue equity (too much cash goes to debt holders). If you forecast it too conservatively, you overvalue equity. The assumption is often more art than science.

## Terminal value in FCFE

At the end of the explicit forecast period, assume FCFE grows at a perpetual rate (typically 2–4% for a mature company). Use the [Gordon growth formula](/gordon-growth-model/): year-N plus one FCFE divided by (cost of equity minus perpetual growth rate). Discount this terminal value back to today and add to the sum of discounted explicit-period cash flows.

The cost of equity in the terminal year should reflect the assumed terminal leverage. If you assume zero debt at terminal, use the unlevered cost of equity plus an adjustment for terminal leverage. This often requires back-of-envelope iteration.

## Strengths and weaknesses

**Strength.** Direct valuation of equity; no need to separately value debt then subtract.

**Strength.** Works for any capital structure, including no debt.

**Strength.** Honors explicit debt schedules if they exist.

**Weakness.** Requires forecasting or assuming debt payoff, which is uncertain.

**Weakness.** Discount rate (cost of equity) changes if leverage changes, adding complexity.

**Weakness.** Less stable than FCFF for companies with volatile or discretionary debt policies.

## See also

<div class="wiki-seealso">

### Closely related

- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/) — the unlevered alternative
- [Cost of equity](/cost-of-equity/) — the discount rate
- [Capital asset pricing model](/capital-asset-pricing-model/) — estimating cost of equity
- [Dividend discount model](/dividend-discount-model/) — an earlier approach to valuing equity

### DCF framework

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — parent class
- [Two-stage DCF](/two-stage-dcf/) — time structure
- [Terminal value](/terminal-value/) — the endpoint calculation
- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — used in FCFF, not FCFE

### Comparison

- [Multiples valuation](/multiples-valuation/) — market-based approach
- [Comparable company analysis](/comparable-company-analysis/) — peer benchmarking

</div>

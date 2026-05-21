---
title: "Free Cash Flow to Firm Valuation"
description: "A valuation method that values the entire enterprise by discounting free cash flow available to all capital providers—both debt and equity—at the weighted average cost of capital."
keywords:
  - free cash flow to firm
  - FCFF
  - enterprise value
  - unlevered valuation
  - WACC
image: "/svg/valuation.svg"
---

*A **free cash flow to firm (FCFF)** valuation is the canonical [discounted cash flow](/discounted-cash-flow-valuation) model. It values the entire enterprise—all the cash available to all investors, debt and equity holders alike—by discounting at the [weighted average cost of capital](/weighted-average-cost-of-capital). From enterprise value, you subtract net debt to arrive at equity value. It is the most widely used approach in professional valuation work.*

## What FCFF captures

FCFF is the cash the business generates after paying all operating expenses and taxes but before servicing debt or equity. In formula terms: EBIT times (1 minus tax rate), plus depreciation and amortization (non-cash charges that reduce taxable income), minus capex (cash spent on assets), minus increases in working capital (cash tied up in receivables, inventory, payables).

The result is the cash the business throws off before any division between debt and equity providers. It answers the question: how much cash is available to distribute to everyone who has a claim on the company—both bondholders and shareholders?

Valuation is the sum of all future FCFF streams, each discounted at the weighted average cost of capital, plus a terminal value, discounted back to today. The result is enterprise value. Subtract net debt (total debt minus cash), and you have equity value.

## Why FCFF is the standard

**Conceptually clean.** The method separates the valuation of the operating business (FCFF, discounted at WACC) from the financing decision (net debt). You can value the business independent of how it is financed, then layer in the actual capital structure.

**Stable through capital structure changes.** If a company refinances heavily, debt levels spike, but FCFF is unchanged. The valuation of the business is unchanged; you just restructure who owns how much. By contrast, [FCFE](/free-cash-flow-to-equity-valuation) valuation, which directly values equity, becomes messy when debt policies shift dramatically.

**Works for all structures.** Startups with no debt, utilities with high leverage, private equity-backed businesses with explicit debt paydowns—FCFF handles all without requiring you to recalibrate discount rates.

**Widely understood.** Investment banks, private equity, and corporate development teams all use FCFF. It is the lingua franca of M&A and equity research.

## The core calculation

Start with NOPAT: net operating profit after tax, or EBIT times (1 minus tax rate). This is the profit available to all investors after accounting for the tax shield on operating earnings.

Add depreciation and amortization back in—they reduce taxable income but are not cash outflows. Subtract capex (cash spent on property, plant, equipment, and intangibles). Subtract the increase in net working capital—cash tied up in receivables, inventory, and payables nets off cash received from operations.

The result is free cash flow to the firm. Repeat this calculation for each year of your forecast period, discounting each year's FCFF at the WACC, then add a terminal value.

## FCFF calculation variants

**Starting from EBIT.** EBIT times (1 minus tax rate) plus depreciation and amortization minus capex minus change in NWC. This is the most direct route.

**Starting from net income.** Net income is after interest expense, so you must add back interest times (1 minus tax rate) and then subtract the after-tax cost of debt from the final value. More cumbersome but sometimes necessary.

**Starting from operating cash flow.** If you have cash flow statements, operating cash flow is close to FCFF. Just subtract capex and add back interest net of tax. Conversely, capex is already deducted in many cash flow formats, so reconcile carefully.

The starting point matters less than consistency and transparency about which adjustments you are making and why.

## Terminal value in FCFF

At year N plus one (where N is your explicit forecast period), assume FCFF grows at a stable perpetual rate—typically 2–4% for a developed-economy company. Using the Gordon growth formula, terminal value equals year-N plus one FCFF divided by (WACC minus perpetual growth rate).

This terminal value is crucial: in most FCFF models, 60–80% of enterprise value comes from perpetuity. Small changes in the perpetual growth assumption or WACC swing valuation enormously. This is why sensitivity analysis is critical.

## Why FCFF beats FCFE for most applications

FCFF is stable through capital structure changes because you are valuing the business, not the equity. If management decides to lever up or down, the FCFF valuation does not move. Only the equity value does.

FCFE is messier because debt levels and the cost of equity are entangled. As leverage rises, cost of equity rises, pushing down equity value. But FCFE itself changes because debt flows shift. Forecasting FCFE under changing leverage is like chasing a moving target.

That said, FCFE is occasionally cleaner for highly leveraged or extremely simple capital structures where debt policy is deterministic and already known.

## Building the forecast

A typical FCFF forecast spans 5–10 years:

- **Years 1–3:** Explicit, detailed forecasts. You know the industry, the company's position, near-term investments.
- **Years 4–7:** Still explicit but with more confidence intervals. You assume some normalization of margins and capex as a percentage of revenue.
- **Year 8+:** Mature state, assumed stable. Capex normalizes to maintenance levels, ROIC stabilizes, reinvestment declines.

For each year, you project revenues (growth from market share or pricing), operating margins (determined by competitive position, cost structure, scale), capex (as percentage of revenue, or based on asset replacement needs), and working capital changes.

The result is a cash flow cascade that is testable and transparent.

## Strengths and weaknesses

**Strength.** Separates business value from financing structure, providing clarity.

**Strength.** Stable under capital structure changes.

**Strength.** Works for any company, regardless of capital structure or dividend policy.

**Weakness.** Requires estimating WACC, which is itself complex and requires [cost of equity](/cost-of-equity) and [cost of debt](/cost-of-debt) estimates.

**Weakness.** Terminal value is enormous and sensitive to tiny changes in perpetuity assumptions.

**Weakness.** Requires detailed forecasts of margins, capex, and working capital, not always available early in analysis.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — the parent method
- [Two-stage DCF](/two-stage-dcf) — simplest time structure
- [Three-stage DCF](/three-stage-dcf) — with explicit transition
- [Free cash flow to equity valuation](/free-cash-flow-to-equity-valuation) — the levered alternative

### Key inputs

- [Weighted average cost of capital](/weighted-average-cost-of-capital) — the discount rate
- [Cost of equity](/cost-of-equity) — WACC component
- [Cost of debt](/cost-of-debt) — WACC component
- [Terminal value](/terminal-value) — the endpoint calculation
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the terminal assumption

### Reality checks

- [Multiples valuation](/multiples-valuation) — market-based alternative
- [Comparable company analysis](/comparable-company-analysis) — peer benchmarking
- [Sensitivity analysis](/sensitivity-analysis-valuation) — which assumptions drive value
- [Football field valuation](/football-field-valuation) — ranges of outcomes

</div>

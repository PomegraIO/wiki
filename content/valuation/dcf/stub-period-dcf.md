---
title: "Stub Period Adjustment"
description: "Handling a partial first forecast period when the valuation date falls between fiscal year-ends in DCF models."
keywords:
  - stub period
  - dcf adjustments
  - partial period
  - fiscal year mismatch
  - cash flow timing
image: /svg/valuation.svg
---

*A **stub period** is the partial first forecast interval when a valuation date falls partway through a fiscal year, requiring separate timing treatment to avoid compounding forecast and discounting errors.*

## The timing mismatch problem

Every DCF model needs a starting date. Ideally, that date aligns with a fiscal year-end: the analyst values a company on 31 December, has full-year financials in hand, and begins forecasting from 1 January the next day. But corporate valuations rarely cooperate with the calendar. A private equity firm may appraise a target on 15 June; an analyst upgrades a stock on a Tuesday in March; a [merger](/merger/) negotiation happens mid-August.

When the valuation date falls inside a fiscal year, the first forecast period becomes irregular. If a company's year ends 31 December and you value it on 30 June, the first forecast period is only seven months (1 July to 31 December). This is the **stub period**—neither a full year nor negligible.

Ignoring the stub creates two errors. First, you forecast full-year growth and cash flows but only discount them for part of a year, overstating present value. Second, you may accidentally double-count financial information: actual cash flows from the early months of the fiscal year get included in both historical financials and the forecast, distorting the opening position of the forecast.

## Building a stub-period forecast

The standard approach builds the stub forecast separately, then transitions cleanly into full-period forecasting.

**Method 1: Pro-rata scaling.** If the company's latest full-year [operating profit](/ebitda/) was £100 million and run-rate is unchanged, the stub period (7 months in the June example) would forecast £100m × 7/12 = £58.33 million. This assumes even cash generation across months—reasonable for mature, seasonal businesses, fragile for volatile firms.

**Method 2: Using actual-plus-forecast.** If six months of actual results are available (1 January to 30 June), use those figures directly and forecast only the remaining six months. This is more precise because half the period is known, not estimated. Year-to-date [revenue](/revenue-recognition/) of £52 million plus a forecast of £55 million for July–December gives £107 million for the full year, a more grounded baseline than pure pro-rata.

**Method 3: Forecast the full year, then apportion.** Build a forecast for the full fiscal year (1 January to 31 December) as usual, then allocate to the stub and the remainder. If the forecast is £120 million for the full year and the stub is 7 months, one assumes £70 million lands in the stub and £50 million in the remaining 5 months—though this is coarser and assumes even distribution.

Most practitioners favour Method 2 when recent actuals are available, because it wastes neither information nor forecast effort.

## Discounting the stub

Once the stub cash flow is forecast, the timing of its discount depends on the convention chosen.

Under the **end-of-stub convention**, the stub cash flow is discounted to the end of the stub period (31 December in the example), then the entire result—including subsequent full years—is discounted back to the valuation date (30 June). A 7-month stub discounts back 7/12 of a year; a full year 1 discounts back a further full year.

Under the **mid-stub convention**, the stub cash flow is assumed to arrive at the midpoint of the stub (mid-September in the 7-month example) and discounted accordingly. This parallels the [mid-year convention](/mid-year-convention/) but applies only to the irregular period.

In practice, the difference is small. A £50 million stub flow at a 10% discount rate discounts to:
- **End-of-stub**: £50m ÷ (1.10^(7/12)) = £47.34 million
- **Mid-stub**: £50m ÷ (1.10^(7/24)) = £47.68 million (roughly 0.7% higher)

Most commercial models use the end-of-stub method for simplicity, reserving the mid-stub approach for more detailed valuations. The choice should be documented and consistent.

## Reconciling the stub to historical financials

A critical step is reconciling the opening position. If the company reported £120 million in [operating profit](/ebitda/) for the year ended 31 December, and you're valuing on 30 June of the next calendar year, you need to know:

- What was the actual [operating profit](/ebitda/) from 1 January to 30 June? (six months)
- What is the run-rate for July–December? (the forecast part)

If actual January–June profit was £55 million and you forecast £60 million for July–December, the full-year run-rate is £115 million, not the prior year's £120 million. Failing to make this reconciliation—simply forecasting another £120 million year—implies that the first half of the year didn't happen, a nonsensical error.

The stub period forces discipline into this reconciliation. Because it is partial and explicit, careless analysts cannot accidentally hide double-counts or inconsistencies.

## The transition to steady-state assumptions

After the stub period closes on the fiscal year-end, the model reverts to standard full-period forecasting. If the company is expected to grow at 5% annually in Year 1 (fiscal year starting 1 January), that 5% is now applied to a full 12-month period, not the remaining months of the prior year.

Similarly, if the model incorporates a [fade rate](/fade-rate-dcf/)—gradually decaying growth toward long-run steady state—the stub period often uses a simplified assumption (e.g., hold the prior year's margin) and then shift to the full trajectory. This avoids overcomplicating the stub and preserves clarity about when the forecast regime changes.

## Practical prevalence

In investment banking and large institutional valuations, stub-period adjustments are standard. They are less common in smaller analyses, retail investor models, or quick back-of-envelope valuations. Many commercial DCF templates include a stub-period toggle, making the mechanics transparent. Some finance software (SAP, Oracle Hyperion, Bloomberg terminals) calculate stubs automatically; manual spreadsheet models must handle them explicitly.

The stub adjustment is particularly important in real estate, [REIT](/real-estate-investment-trust/) valuation, and [leveraged buyout](/leveraged-buyout/) models, where timing alignment between valuation date and forecast horizon can swing fair value estimates by several percentage points.

## See also

<div class="wiki-seealso">

### Closely related

- [Mid-Year Convention](/mid-year-convention/) — timing adjustments for full-period cash flows
- [Fade Rate in DCF Forecasting](/fade-rate-dcf/) — managing forecast assumptions post-stub
- [Reinvestment Rate](/reinvestment-rate-dcf/) — capital assumptions from year one onward
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the full DCF framework
- [Terminal Value](/discounted-cash-flow-valuation/) — perpetuity at the end of the explicit forecast
- [Discount Rate](/discount-rate/) — the rate applied to all periods, including the stub

### Wider context

- [Cost of Equity](/cost-of-equity/) — setting the discount rate
- [Free Cash Flow](/free-cash-flow/) — the metric being forecast
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing stub assumptions

</div>

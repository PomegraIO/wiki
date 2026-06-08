---
title: "Reinvestment Rate"
description: "The fraction of operating cash flow or earnings that a company reinvests into the business to sustain or achieve its forecast growth rate."
keywords:
  - reinvestment rate
  - dcf growth
  - capital expenditure
  - working capital
  - sustainable growth
image: /svg/valuation.svg
---

*The **reinvestment rate** is the proportion of [free cash flow](/free-cash-flow/) or [earnings](/earnings-per-share/) that a company reinvests into capital expenditure, working capital, and debt reduction to fund forecast growth, linking the growth assumption to its required capital.*

## The growth equation

A foundational insight in corporate finance is that growth does not appear from thin air. A company cannot increase its revenue or profits without deploying additional capital—whether in factories, inventory, technology, working capital, or in reducing debt. The reinvestment rate quantifies this relationship.

The basic growth equation is:

**Sustainable Growth Rate = ROIC × Reinvestment Rate**

Where [ROIC](/return-on-invested-capital/) is the return on invested capital (operating profit after tax, divided by the capital deployed). If a company has a 12% ROIC and reinvests 50% of its [free cash flow](/free-cash-flow/), it can grow at 12% × 50% = 6% per year without raising new [equity](/common-stock/) or [debt](/corporate-bond/). If it reinvests 75%, it can grow at 9%.

This discipline constrains the DCF forecast. Many analysts forecast high growth (say, 15% revenue growth) without thinking through the capital required. The reinvestment rate makes this visible: a 15% growth rate with a 12% ROIC requires an 125% reinvestment rate—reinvesting £1.25 for every £1 of earnings. That is only possible if the company raises external capital or dips into cash reserves; organic, self-funded growth is impossible at that pace with that return. Alternatively, the ROIC assumption is too low, or the growth forecast is too high. The equation forces consistency.

## What counts as reinvestment

Reinvestment includes three components:

1. **Capital expenditure (CapEx)**: Spending on property, plant, equipment, and intangible assets (patents, software, R&D capitalized on the balance sheet). Calculating it as CapEx minus depreciation gives the *net* incremental capital required.

2. **Change in net working capital**: An increase in [receivables](/accounts-receivable/), inventory, and other current assets (cash tied up in operations) counts as reinvestment. A company growing 20% typically needs more cash sitting in [accounts receivable](/accounts-receivable/) and [inventory](/inventory-turnover/). Conversely, a reduction in working capital (collecting faster, paying suppliers slower) releases cash and reduces reinvestment needs.

3. **Debt repayment or equity issuance**: In steady state, a company maintains a constant [debt-to-equity](/debt-to-equity-ratio/) ratio. If it grows faster, both assets and financing must grow. If [debt](/corporate-bond/) remains flat while equity and assets expand, the company is implicitly delevering—an unsustainable or conscious restructuring, not normal growth. The reinvestment rate assumption should reflect the capital structure policy (e.g., if the company maintains a 40% debt ratio, 60% of growth must be equity-financed, 40% debt-financed).

## Linking reinvestment to cash flow forecasts

In a [discounted cash flow](/discounted-cash-flow-valuation/) model, reinvestment is the bridge from operating profit to [free cash flow](/free-cash-flow/):

**Free Cash Flow = EBIT(1 – Tax Rate) – CapEx + Depreciation – Change in Net Working Capital**

Alternatively, if starting from net income:

**Free Cash Flow = Net Income + Depreciation – CapEx – Change in Net Working Capital + Interest Expense × (1 – Tax Rate)**

The reinvestment rate is implicit in the CapEx and working capital items. If CapEx is forecast to be 5% of revenue and working capital to grow at 2% of revenue growth, the reinvestment rate is determined by those line items, not stated separately.

However, when building a forecast, many analysts work backwards: they assume a reinvestment rate based on the target growth and expected ROIC, then solve for CapEx or working capital as a consistency check.

## Declining reinvestment as a firm matures

Young, high-growth companies typically have high reinvestment rates. A software startup might retain and reinvest 80% of operating cash flow to fund expansion; a 50-year-old utility might reinvest only 30% and distribute the rest as [dividends](/dividend/).

As a firm matures and growth slows—often modeled via a [fade rate](/fade-rate-dcf/)—the reinvestment rate should decline. A company growing at 4% with an 8% ROIC needs only a 50% reinvestment rate (4% ÷ 8%). If growth fades to 2%, reinvestment can drop to 25% (2% ÷ 8%), freeing up cash for [dividends](/dividend/), share buybacks, or debt reduction.

Many DCF models hold the reinvestment rate constant across the explicit forecast period, then step it down to a lower "terminal" rate as growth converges to the long-run equilibrium. This is a simplification; in reality, reinvestment should decline in tandem with the [fade rate](/fade-rate-dcf/).

## Common errors and calibration challenges

**Ignoring working capital changes** is widespread, especially in quick models. A company with 30 days of receivables and 45 days of inventory whose revenue grows 20% needs to fund the incremental working capital—often equivalent to 3–6 months of CapEx. Omitting this overstates [free cash flow](/free-cash-flow/).

**Using historical CapEx as a guide** without considering the business model. A retail chain opening stores requires high ongoing CapEx as a % of revenue. A software company with mostly maintenance CapEx has low ongoing CapEx needs. The forecast must reflect the *forward* capital intensity, not the past.

**Confusing depreciation with growth capital.** Some analysts subtract depreciation from the reinvestment rate, treating it as a "source" of cash. This is incorrect. Depreciation is a non-cash expense; CapEx is real cash outflow. The two are linked only if CapEx is forecast to equal depreciation (the "replacement" scenario, where the company neither grows nor shrinks its asset base). In a growing company, CapEx exceeds depreciation; the difference is incremental capital for growth.

**Circular logic between ROIC and reinvestment.** If a company's ROIC is forecast to decline (as the [fade rate](/fade-rate-dcf/) erodes returns), but reinvestment is held constant, the growth rate should also decline. Some models hold both ROIC and growth constant while changing reinvestment, which is internally inconsistent.

## Sector patterns

**Software, platforms**: Low reinvestment rates (20–40%) after the early growth phase. Marginal revenue requires little incremental capital; network effects and scale produce outsize returns.

**Industrials, capital goods**: High reinvestment rates (60–80%) to sustain or grow. Asset-heavy balance sheets and ongoing CapEx requirements mean cash generation is more constrained.

**Retail, hospitality**: Very high reinvestment rates (80%+ in growth phases) due to real estate and inventory. Mature chains typically reinvest 40–60%.

**Utilities, infrastructure**: Moderate to high (50–70%), driven by regulated return requirements and the need to maintain aging infrastructure. Highly predictable.

**Financials**: Variable; [banks](/jpmorgan-chase/) need high [capital adequacy](/capital-adequacy/) ratios and thus retain significant earnings; insurers with strong underwriting and float management can pay out more.

## Sensitivity and validation

The reinvestment rate is a high-leverage assumption. A 10% change in the reinvestment rate can shift the fair value of a growing company by 15–25%. Testing it via [sensitivity analysis](/sensitivity-analysis-valuation/)—varying it across a plausible range—is essential. For mature or declining businesses, the sensitivity is lower; for high-growth companies, it is critical.

A useful sanity check: compare the forecast reinvestment rate to historical norms and to peer companies. If a company historically reinvested 50% to grow at 5%, but the forecast assumes 65% reinvestment to grow at 6%, ask why. Is the ROIC expected to improve? Is the business becoming more efficient? Or is the forecast overly optimistic on growth without corresponding scrutiny of capital requirements?

## See also

<div class="wiki-seealso">

### Closely related

- [Free Cash Flow](/free-cash-flow/) — the cash available after reinvestment
- [Return on Invested Capital](/return-on-invested-capital/) — the paired metric determining growth
- [Fade Rate in DCF Forecasting](/fade-rate-dcf/) — managing declining growth and reinvestment together
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the model embedding reinvestment
- [Capital Expenditure](/discounted-cash-flow-valuation/) — the primary reinvestment line item
- [Working Capital](/cash-conversion-cycle/) — the secondary reinvestment component

### Wider context

- [Dividend Payout Ratio](/dividend-payout-ratio/) — the inverse of reinvestment (distribution policy)
- [Cost of Equity](/cost-of-equity/) — the rate discounting the freed cash
- [Sustainable Growth](/business-cycle/) — the long-run growth achievable without external financing

</div>

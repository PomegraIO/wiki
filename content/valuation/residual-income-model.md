---
title: "Residual Income Model"
description: "A valuation method that values equity by discounting the earnings in excess of the cost of equity, plus the book value of equity."
keywords:
  - residual income model
  - abnormal earnings
  - excess earnings
  - RIM
  - equity valuation
image: "https://picsum.photos/seed/residual-income-model/900/600"
---

*The **residual income model (RIM)** values equity by asking: what is the book value of the company's equity, plus the present value of the excess earnings it will generate beyond its cost of equity? It is a theoretically elegant alternative to [dividend discount models](/dividend-discount-model) and [free cash flow valuation](/free-cash-flow-to-equity-valuation) that emphasizes the spread between return on equity and cost of equity.*

## The intuition

Book value of equity is what the company's equity is worth if it earns exactly its cost of equity. If a company has 100 million in book equity and a cost of equity of 10%, the market should value it at 100 million if earnings are 10 million annually (10% return).

But if the company actually earns 15 million (15% return), the extra 5 million is "residual income"—earnings above the cost of equity. This excess creates value. The present value of all future residual income, plus book value, is intrinsic equity value.

## The formula

Equity value = Book value + PV of expected residual income

Residual income in any year = Net income minus (Cost of equity × Beginning book value)

Or equivalently: (ROE minus Cost of equity) × Beginning book value

A company earning a 15% ROE with a 10% cost of equity generates 5 percentage points of residual income.

## Why RIM is elegant

**Connects to accounting.** Uses book value and earnings, which are directly observable or forecast from financial statements.

**Economic intuition.** Immediately shows whether the company is creating value: if ROE exceeds cost of equity, it creates value; if not, it destroys it.

**Works for unprofitable companies.** If a company earns zero today but is expected to be profitable in the future, RIM can still value it (unlike dividend discount models).

**Parsimonious.** Fewer parameters than DCF. No need to separately forecast capex and working capital; ROE summarizes the economics.

## RIM vs. free cash flow models

Free cash flow models and RIM should yield the same intrinsic value if assumptions are consistent. But RIM is more transparent about the return being earned:

- A company that invests heavily in capex (lowering free cash flow) but earns high returns shows up in RIM as high ROE. The value is correct.
- A company that returns all cash as dividends (high free cash flow) but reinvests at low returns shows up in RIM as declining ROE. The value reflects this destruction.

## Building an RIM valuation

**Step 1: Start with book value.** Take the equity value from the most recent balance sheet.

**Step 2: Forecast net income.** Project earnings per share or net income, based on forecasted revenue, margins, and capital structure.

**Step 3: Forecast book value growth.** Book value grows by retained earnings (earnings minus dividends). Forecast the dividend payout ratio.

**Step 4: Calculate ROE.** ROE = Net income / Average book equity. This will typically decline over time as the company matures.

**Step 5: Calculate residual income.** For each year, residual income = (ROE minus Cost of equity) × Beginning book value.

**Step 6: Discount residual income.** Discount each year's residual income at the cost of equity.

**Step 7: Terminal residual income.** In the terminal period, assume ROE converges to cost of equity (zero residual income), or assume a modest perpetual residual income if the company has durable competitive advantages.

**Step 8: Sum.** Equity value = Current book value + PV of forecasted residual income + PV of terminal residual income.

## Example

A company has 50 million in book equity and a 10% cost of equity.

Year 1: Projected net income 8 million. ROE = 16%. Residual income = (16% - 10%) × 50 = 3 million.
Year 2: Projected net income 9 million (as book equity grows). Book equity grows to 55 million. Residual income = (16.4% - 10%) × 55 = 3.5 million.
Year 3-5: ROE gradually declines to 12%. Residual income continues, declining each year.
Terminal: ROE converges to 10% (cost of equity). Residual income = 0.

PV of residual income over 5 years (discounted at 10%) might be 15 million.
Equity value = 50 + 15 = 65 million.

## Advantages

**Explicit return focus.** RIM makes the return-on-equity assumption crystal clear. If you forecast 12% ROE on a 10% cost of equity, you are explicitly saying the company will beat the cost of capital forever—a strong claim.

**Stability over time.** RIM valuations are often more stable than DCF across different accounting periods. Changes in capex policy don't affect the fundamental RIM value as much.

**Book value anchor.** The starting point (book value) is objective. Even if the RIM component is zero, the company is worth at least book value.

## Disadvantages

**Terminal value assumption.** Like DCF, the bulk of value lies in terminal residual income, which is hard to estimate.

**ROE forecasting.** Accurately forecasting ROE for 5+ years is difficult. ROE depends on many factors: sales growth, margins, asset turnover, capital structure.

**Accounting distortions.** Book value can be distorted by accounting choices. A company that expensed R&D has lower book value than one that capitalized it, even if they have the same economic value.

**Less suitable for young companies.** A high-growth company with negative earnings today might have low or negative book value. RIM works but is less intuitive than DCF.

## Terminal value in RIM

The terminal assumption is critical. A few approaches:

1. **ROE converges to cost of equity.** Assume the company earns at cost of equity perpetually. Terminal residual income = 0. This is conservative.

2. **ROE converges to industry average.** Assume the company's ROE converges to the long-run industry average. Calculate perpetual residual income from that.

3. **Perpetual excess return.** If the company has durable competitive advantages, assume it maintains 2–4% ROE above cost of equity perpetually. This is aggressive and requires strong justification.

## See also

<div class="wiki-seealso">

### Closely related

- [Abnormal earnings growth model](/abnormal-earnings-growth-model) — a variant of RIM
- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — equivalent to RIM if assumptions are consistent
- [Free cash flow to equity valuation](/free-cash-flow-to-equity-valuation) — the cash-flow counterpart
- [Return on equity](/return-on-equity) — the key metric in RIM
- [Cost of equity](/cost-of-equity) — the hurdle rate

### Components

- Book value — the starting point
- Net income — the earnings metric
- [Retained earnings](/retained-earnings) — drives book value growth

### Related concepts

- Economic profit — closely related to residual income
- EVA / Economic value added — the operating version

### Testing and sensitivity

- [Sensitivity analysis](/sensitivity-analysis-valuation) — ROE and cost-of-equity sensitivity
- [Football field valuation](/football-field-valuation) — combining with other methods

</div>

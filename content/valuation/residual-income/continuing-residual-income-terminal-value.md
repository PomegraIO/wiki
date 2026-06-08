---
title: "Continuing Residual Income and Terminal Value"
description: "How to estimate continuing residual income and terminal value beyond the explicit forecast period in a residual income valuation model."
keywords:
  - continuing residual income terminal value
  - terminal value residual income model
  - perpetuity growth residual income
  - RI model forecast period
image: /svg/valuation.svg
---

*The residual income model projects excess returns (earnings above the cost of equity) for a finite forecast period—often 5 to 10 years—then must estimate the value of residual income that continues beyond. This "continuing" or "terminal" value can represent 40–70% of intrinsic value, making the assumption critical. Two main frameworks dominate: assume residual income fades to zero, or assume it persists at a constant growth rate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Continuing Residual Income & Terminal Value — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The forecast ends, but the value question doesn't. Terminal assumptions often drive valuation outcomes.</div>

|   |   |
|---|---|
| **Forecast period** | Typically 5–10 explicit years, after which terminal value takes over |
| **Fade-to-zero assumption** | Residual income decays to zero; terminal value = 0 |
| **Perpetuity-growth assumption** | Residual income continues at constant growth rate (e.g., 2–3% GDP growth) |
| **Terminal value formula** | TV = RI_final × (1 + g) / (r − g), where r = cost of equity, g = growth rate |
| **Sensitivity** | Terminal value often accounts for 40–70% of total intrinsic value |

</aside>

## Why terminal value matters in RI models

Unlike [discounted cash flow](#) valuation, which projects free cash flows to perpetuity, the residual income model typically forecasts only a discrete "explicit" period. During this period, you estimate year-by-year earnings, cost of equity charges, and the resulting residual income. Once that period ends, you face a choice: assume excess returns vanish, or assume they continue in some form.

The reason this matters is simple arithmetic. If a company is forecast to earn strong residual income for 10 years, but then the excess returns disappear, intrinsic value will be lower than if those excess returns persist (even at a declining rate). The terminal value assumption can swing a valuation by 30–50%, so getting it conceptually right is essential.

## The fade-to-zero assumption

The most conservative terminal value approach assumes that competitive pressures, market maturation, or industry disruption cause residual income to decline to zero. This is the implicit assumption when you don't explicitly calculate a terminal value—you simply stop projecting RI beyond year 10 (or 5, or whenever).

**Economic logic**: Most firms in competitive markets eventually converge to earning just their cost of equity (RI = 0) because:
- Excess profits attract competitors.
- Barriers to entry erode.
- Technological change or regulation shifts the landscape.

This assumption suits mature, low-growth industries (utilities, consumer staples, banking) where competitive returns eventually prevail.

**Formula**: Terminal Value = 0 (or equivalently, no continuation value is added).

**Total intrinsic value** = Book Value₀ + PV(explicit-period RIs) + 0

## The perpetuity-growth assumption

A more nuanced view acknowledges that some firms possess durable competitive advantages—brand strength, network effects, proprietary technology, scale economies—that allow them to earn excess returns indefinitely. For these firms, assuming RI drops to zero understates value.

The perpetuity-growth approach assumes residual income continues in perpetuity at a constant growth rate, typically aligned with long-term nominal GDP growth (2–3% in developed economies). The logic: a firm that grows at the economy's long-run rate faces the same competitive pressures as the economy itself, but its durable advantages let it maintain a stable spread above the cost of equity.

**Formula**:

Terminal Value = RI_final × (1 + g) / (r − g)

where:
- RI_final = residual income in the final explicit year
- g = perpetual growth rate
- r = cost of equity

This is identical to the [Gordon growth model](#) for dividends or free cash flow, applied to residual income.

**Example**: A software firm with a loyal customer base and switching costs earns RI of $50M in year 10. Cost of equity is 8%. Assume perpetual growth at 2.5% (slightly above GDP, reflecting sticky market position).

Terminal Value = $50M × (1.025) / (0.08 − 0.025) = $51.25M / 0.055 = **$931M**

This terminal value is then discounted back to present value and added to the book value and explicit-period RIs.

## Choosing between fade-to-zero and perpetuity-growth

The choice depends on competitive positioning and industry structure:

**Fade-to-zero fits**:
- Cyclical industries (auto, retail, chemicals) where excess returns are cyclical
- Mature, slow-growing sectors with limited barriers to entry
- Firms without clear competitive advantages
- Conservative valuation when competitive intensity is high

**Perpetuity-growth fits**:
- Firms with strong brands, patents, or network effects
- High-growth technology or healthcare companies with durable moats
- Dominant market positions unlikely to be disrupted in the forecast period
- Industries with structural growth (healthcare, software-as-a-service)

Many analysts use a hybrid: a fade-to-low assumption in which residual income doesn't drop to zero but gradually converges to a small positive level (e.g., 10–20% of the explicit-period RI) by year 15, then continues at that level in perpetuity.

## Sensitivity to terminal value assumptions

Because terminal value often comprises 40–70% of intrinsic value, small changes in the growth rate or cost of equity can dramatically shift the valuation:

| Growth rate | Terminal RI | Cost of equity | Terminal value |
|---|---|---|---|
| 0% | $50M | 8% | $625M |
| 2% | $50M | 8% | $1,050M |
| 3% | $50M | 8% | $1,700M |

A 1-percentage-point increase in the assumed perpetual growth rate (from 2% to 3%) raises terminal value by 62%. This is why analysts spend time stress-testing and defending their terminal assumptions in valuation reports.

## Estimating the growth rate in terminal value

If you're using the perpetuity-growth formula, what growth rate should you choose?

**GDP growth**: The most common benchmark. If a firm grows faster than the economy in perpetuity, it will eventually become larger than the economy—impossible. Most analysts cap perpetual growth at 2.5–3.5%, depending on real GDP growth and inflation expectations.

**Industry growth**: Some analysts use industry-specific long-run growth forecasts (e.g., 4–5% for healthcare, 1–2% for utilities). This can be justified if the firm is expected to maintain or gain market share at exactly the industry rate.

**Risk adjustment**: A firm with higher uncertainty (smaller scale, newer industry) might warrant a lower terminal growth rate, even if the underlying industry is growing faster. The growth rate should reflect sustainable, competitive equilibrium, not peak-case assumptions.

## When terminal value goes negative

If the cost of equity (r) is less than or equal to the perpetual growth rate (g), the formula breaks down. This signals that your assumptions are inconsistent: either the cost of equity is too low, or the growth rate is too optimistic. Re-examine both inputs before proceeding.

Also avoid high perpetual growth rates (above 4–5%) unless the firm has truly exceptional competitive advantages. The temptation to use a high terminal growth rate to justify a high current valuation is a common source of optimistic bias.

## Integration with book value

Remember that the full RI model is:

**Intrinsic Value = Book Value₀ + PV(explicit RIs) + PV(Terminal Value)**

The terminal value doesn't exist in isolation; it's the continuation of the residual income stream. If you've used [book value adjustments](/book-value-adjustments-residual-income/) to restate the balance sheet, the explicit and terminal RIs build on that adjusted base.

## See also

<div class="wiki-seealso">

### Closely related

- [Residual Income Model with Negative Book Value](/residual-income-model-negative-book-value/) — How terminal value assumptions change when the starting book value is weak
- [Multi-Stage Residual Income Model Explained](/residual-income-model-multi-stage/) — Explicit forecasts of different growth phases before terminal value kicks in
- [Book Value Adjustments for Residual Income Valuation](/book-value-adjustments-residual-income/) — The foundation on which continuing RIs are built

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Uses similar terminal value logic with perpetuity-growth and free cash flow
- [Gordon Growth Model](/dividend-discount-model/) — The perpetuity formula applied to dividends
- [Cost of Equity](/cost-of-equity/) — The denominator in the terminal value perpetuity formula
- Competitive Advantage — The economic basis for expecting residual income to persist

</div>

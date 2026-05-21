---
title: "Gordon Growth Model"
description: "The simplest discounted cash flow formula, which values a stock or firm assuming constant perpetual growth in cash flows or dividends."
keywords:
  - Gordon growth model
  - perpetuity growth
  - stable growth
  - dividend valuation
  - terminal value
image: "/svg/valuation.svg"
---

*The **Gordon growth model** is the most elegant and dangerous formula in equity valuation. It states that an asset worth paying for a perpetual stream of cash flows growing at a constant rate is equal to next year's cash flow divided by the required rate of return minus the growth rate. It is used daily by practitioners, often without adequate skepticism about its assumptions.*

## The formula

The Gordon growth model is fundamentally a restatement of the perpetuity formula. If a company or asset will generate free cash flow of D in the next period, grow at rate g forever, and investors require a return of r, then value equals D divided by (r minus g).

In practical terms: if a utility pays a dividend of 5 dollars per share next year, investors require a 10% return, and the dividend grows at 2% forever, the stock is worth 5 divided by 0.08, or 62.50 dollars per share.

This formula appears everywhere: dividend valuation, [terminal value](/terminal-value) calculations in DCFs, and real estate and infrastructure valuations. Its simplicity is its appeal. Its simplicity is also its curse.

## When the model works

**True perpetuities.** Government [bonds](/bond) with no maturity are rare but exist. They grow (or not) forever. Dividend discount models for utilities, master limited partnerships, and other cash-return-focused businesses are reasonable uses.

**Terminal values in DCF.** In the final year of a [two-stage](/two-stage-dcf) or [three-stage DCF](/three-stage-dcf), when you assume the business reaches steady state and grows at GDP rate or slightly above forever, the Gordon formula collapses years 20 through infinity into a single value.

**Infrastructure and commodities.** Some assets—toll roads, ports, mines—generate fairly predictable cash flows that grow at inflation, making the model conceptually sound, if not empirically precise.

## The critical assumptions

**Perpetual growth rate g.** This is the rate at which cash flows will grow forever. For a developed-economy utility, 2–3% is reasonable. For a developed-economy company in a mature industry, 2–3% is reasonable. For anything else, the assumption is questionable. If you assume 5% perpetual growth for a company in an industry growing at 2%, you are asserting the company will take market share forever—an unusual claim.

The model is extremely sensitive to g. If r = 10% and g = 3%, value is D over 0.07. If g rises to 4%, value is D over 0.06—a 16% increase. If g rises to 5%, value doubles. Small errors in perpetual growth rate cause enormous valuation swings.

**Required rate of return r.** This is the [cost of equity](/cost-of-equity) for an equity valuation or a blended [cost of capital](/weighted-average-cost-of-capital) for an enterprise valuation. Estimating r requires choices about risk, market returns, and company-specific factors. The more volatile the cash flows, the higher r should be.

**Stability of cash flows.** The model assumes you can forecast next year's cash flow with some precision. This is false for cyclical businesses, growth companies in transition, or any firm in disruption. Using Gordon growth on a pandemic-struck airline, a bankrupt retailer, or an emerging-growth software company is a category error.

## The perpetual growth rate ceiling

A fundamental constraint is that g must be less than r, or the denominator becomes negative or zero. But there is a deeper constraint: over the very long run, no company can grow faster than the economy as a whole. A mature business cannot take infinite market share; it hits saturation. Assuming perpetual growth above nominal GDP growth is therefore assuming ever-rising market share or industry consolidation without end.

For a developed economy, nominal GDP grows at 3–4% annually (real growth of 2–3%, plus inflation of 1–2%). No mature company can grow faster than that forever. A private-equity-backed business might grow at 10% for ten years, but the model assumes it continues at 10% in perpetuity, which is impossible.

The most common mistake in Gordon growth modeling is an unconstrained perpetual growth rate. If you model a software company at 5% perpetual growth because "the market is growing at 15%," you are making an implicit assumption that the company takes market share from every peer, forever, which is not a forecast; it is a delusion.

## Variants and extensions

**Two-stage Gordon.** Assume high growth for N years, then apply Gordon growth to the final period. This is far more realistic than one-stage Gordon for any real business.

**Declining growth.** Model perpetual growth as declining over time—say, 5% in year one, 4% in year two, down to 2% in perpetuity. This is sometimes called the H-model when the decline is linear.

**Cash flow variant.** Replace dividends with free cash flow to equity. The logic is identical; the input differs.

## Why practitioners use it despite its flaws

The Gordon growth model persists because:

1. **It forces explicit assumptions.** You cannot fudge a perpetual growth rate; it sits right there in the denominator.

2. **It works for true perpetuities.** Utilities, REIT dividends, and infrastructure cash flows are often stable enough to warrant the assumption.

3. **It scales to complex valuations.** A detailed [three-stage DCF](/three-stage-dcf) uses Gordon growth in the terminal value; it is unavoidable.

4. **It is simple.** In a world of uncertainty, simplicity is not nothing.

The correct use of Gordon growth is narrow: for stable, mature, cash-return-focused businesses with predictable growth, or as the terminal-value assumption in a more sophisticated model where the explicit forecast period is honest about declining growth.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend discount model](/dividend-discount-model) — the typical application
- [Perpetuity growth terminal value](/perpetuity-growth-terminal-value) — the canonical use in DCF
- [Terminal value](/terminal-value) — what this model is usually calculating
- [Multi-stage DDM](/multi-stage-ddm) — extending Gordon growth with an explicit period

### Criticism and alternatives

- [Two-stage DCF](/two-stage-dcf) — a more nuanced time structure
- [Three-stage DCF](/three-stage-dcf) — explicit transition period
- [Exit multiple terminal value](/exit-multiple-terminal-value) — an alternative to perpetuity
- [Scenario valuation](/scenario-valuation) — discrete cases instead of formulas

### Inputs

- [Cost of equity](/cost-of-equity) — the required return r
- [Capital asset pricing model](/capital-asset-pricing-model) — how to estimate cost of equity
- [Market risk premium](/market-risk-premium) — a key input to CAPM

</div>

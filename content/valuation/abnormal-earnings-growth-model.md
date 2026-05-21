---
title: "Abnormal Earnings Growth Model"
description: "A valuation method that values equity based on expected growth in abnormal earnings, valuing a company based on earnings growth expectations rather than absolute earnings levels."
keywords:
  - abnormal earnings growth
  - AEG
  - earnings growth
  - equity valuation
  - terminal value
image: "/svg/valuation.svg"
---

*The **abnormal earnings growth (AEG) model** is a variant of the [residual income model](/residual-income-model) that shifts focus from the level of abnormal earnings to the growth in abnormal earnings. Instead of forecasting earnings and subtracting cost of equity, you forecast how earnings growth will evolve and value the company based on its capacity to grow earnings beyond the cost of capital. It is less widely used than RIM but offers an elegant framework for thinking about growth.*

## The intuition

The residual income model values a company based on the excess earnings (above cost of equity) it generates each year. The AEG model asks: how will those excess earnings grow?

A company earning 10% ROE on 100 million in equity (10 million earnings) with a 10% cost of equity generates zero residual income. But if earnings grow to 11 million next year (11% ROE), the increase is "abnormal earnings growth." The value of that growth is what AEG captures.

## The formula

Equity value = Current earnings / Cost of equity + PV of expected abnormal earnings growth

The first term (current earnings divided by cost of equity) is the value as if earnings never grow but remain at the cost-of-capital return. This is the "normal value."

The second term is the value of growth above the cost of capital.

## Building an AEG model

**Step 1: Establish current earnings.** Most recent annual earnings per share (EPS).

**Step 2: Calculate normal value.** Normal value = EPS / Cost of equity. If EPS is 5 and cost of equity is 10%, normal value is 50 per share.

**Step 3: Forecast abnormal earnings growth.** Project how much earnings will grow in excess of the cost of equity return.

If earnings grow from 5 to 5.5 (10% growth), and cost of equity is 10%, there is no abnormal growth—growth is in line with the cost of capital.

If earnings grow to 5.75, that is 15% growth, which exceeds the 10% cost of equity. The excess 5% growth is abnormal.

**Step 4: Discount abnormal growth.** Discount the present value of abnormal earnings growth at the cost of equity.

**Step 5: Terminal value.** Assume abnormal earnings growth eventually converges to zero (growth falls to cost-of-equity level), or assume modest perpetual abnormal growth.

## AEG vs. RIM

The AEG model is mathematically equivalent to RIM but often easier to think about:

- **RIM asks:** What is the annual spread between ROE and cost of equity, and how long does it persist?
- **AEG asks:** How much will earnings exceed the cost-of-capital growth rate, and for how long?

For a company with steady ROE, RIM is simpler. For a company whose growth rate is the key uncertainty, AEG is more intuitive.

## Example

A company has EPS of 2 and a cost of equity of 10%.

Normal value = 2 / 0.10 = 20.

Over the next five years, analysts forecast earnings growth of 15% annually (above the 10% cost of capital). The abnormal growth premium is 5% per year.

Year 1: Abnormal earnings = 2 × 15% minus 2 × 10% = 0.10. (Earnings grow 15%, but a 10% return is required; the excess is abnormal.)
Year 2-5: Abnormal earnings grow as the base grows.

PV of five years of abnormal earnings at 10% cost of capital = roughly 0.40 per share.

In terminal, assume earnings grow at cost of capital (10%) forever, so abnormal earnings = 0.

Equity value = 20 + 0.40 = 20.40 per share.

If the stock trades at 22, it is slightly overvalued.

## When AEG is useful

**Growth companies.** A company whose main value driver is unexpected earnings growth can be valued easily with AEG.

**Earnings surprise analysis.** If a company beat earnings forecasts, the AEG model quickly shows how that surprise affects valuation.

**Scenario analysis.** Testing different earnings growth scenarios is straightforward.

## Challenges

**Forecasting earnings growth.** The model shifts the difficulty from forecasting ROE and book value (RIM) to forecasting earnings growth rates. Both are hard.

**Terminal assumptions.** Like RIM and DCF, the terminal value dominates, and it depends on whether you assume abnormal earnings growth persists or converges to zero.

**Accounting quality.** Earnings can be manipulated through accounting choices. A cash-flow-based model (DCF) is less vulnerable to these distortions.

## AEG as a check on DCF

An AEG model is sometimes used as a reality check on DCF. If a DCF implies 15% perpetual earnings growth and AEG based on consensus forecasts implies only 8% abnormal earnings growth, the DCF is probably too aggressive.

## See also

<div class="wiki-seealso">

### Closely related

- [Residual income model](/residual-income-model) — the parent framework
- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — equivalent if assumptions align
- Earnings growth — the metric being valued
- [Cost of equity](/cost-of-equity) — the baseline return

### Components and concepts

- [Earnings per share](/earnings-per-share) — the starting metric
- Return on equity — determines whether growth is abnormal
- Book value — foundation of equity value

### Testing and validation

- [Sensitivity analysis](/sensitivity-analysis-valuation) — growth-rate sensitivity
- [Football field valuation](/football-field-valuation) — combining methods
- [Scenario valuation](/scenario-valuation) — discrete growth scenarios

</div>

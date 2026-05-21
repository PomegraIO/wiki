---
title: "Free Cash Flow Yield Valuation"
description: "A simplified valuation approach that values a company based on the ratio of free cash flow to enterprise value, comparing to required yield or market yields."
keywords:
  - free cash flow yield
  - FCF yield
  - earnings yield
  - valuation approach
  - yield-based valuation
image: "/svg/valuation.svg"
---

*A **free cash flow yield valuation** is a shortcut approach that bypasses detailed forecasting. You calculate the current free cash flow yield (free cash flow divided by enterprise value), compare it to required or market yields, and determine if the company is cheap or expensive. A company with 5% FCF yield when you require 8% is undervalued; one with 3% yield is overvalued. It is simple, fast, and works well as a screen.*

## The logic

Free cash flow yield = Free cash flow to firm / Enterprise value

This is the inverse of EV/FCF multiple. A company with 100 million in FCF and 1 billion in EV has a 10% FCF yield, or a 10x EV/FCF multiple.

A higher yield means the company generates more cash relative to its value—a better deal. A lower yield means less cash per unit of value—a worse deal.

The question is: what yield do you require? If you require 8%, a company yielding 10% is undervalued. If it yields 6%, it is overvalued.

## Required yield

Your required yield depends on the company's risk and your opportunity cost:

**Risk-free rate.** The baseline is the risk-free rate (10-year Treasury, 4–5%). A safe company should yield above this.

**Risk premium.** Add a premium for business risk. A stable utility might yield 6–7% (risk-free plus 1–2%). A volatile tech company might require 10–12% (risk-free plus 5–7%).

**Opportunity cost.** What else could you do with your money? If you can buy a Treasury at 5% or this company at 6% FCF yield, the company is barely better.

Most investors use a blended required yield of 8–10%.

## Application

**Screen for value.** Calculate FCF yield for a list of companies. Rank by yield. Buy the highest-yielding (cheapest by this metric), assuming fundamentals are sound.

**Valuation check.** If a company yields 3% and you require 8%, it is overvalued by roughly 8/3 - 1 = 166%. In other words, the yield is 3/8 = 37.5% of your requirement.

**Bench-marking.** Compare a company's FCF yield to peers. If peers yield 6% and this company yields 4%, it is expensive relative to peers (lower cash generation per unit of value).

## Example

Company A:
- Free cash flow to firm: 100 million
- Enterprise value: 1,000 million
- FCF yield: 10%
- If you require 8%, it is undervalued. Implied value = FCF / Required yield = 100 / 0.08 = 1,250 million. At 1,000, it is 20% undervalued.

Company B:
- Free cash flow to firm: 50 million
- Enterprise value: 1,000 million
- FCF yield: 5%
- If you require 8%, it is overvalued. Implied value = 50 / 0.08 = 625 million. At 1,000, it is 60% overvalued.

## Advantages

**Simple.** No need for detailed forecasts. You use current-year FCF.

**Comparable across companies.** A yield is yield, whether it is a utility, a tech company, or a bank. Easy to compare.

**Tied to cash, not accounting earnings.** Free cash flow is harder to manipulate than reported earnings.

**Works as a screen.** For a portfolio manager with many opportunities, FCF yield quickly identifies which stocks are cheap and which are expensive.

## Disadvantages

**Assumes no growth.** The method treats FCF yield as a perpetual yield (like a bond). But companies grow. A high-growth company with low current FCF yield might create value, while a mature company with high FCF yield might destroy it.

**Ignores growth differences.** A tech company yielding 3% but growing at 20% is cheaper than a utility yielding 7% growing at 2%, but the method would suggest the opposite.

**Relies on current FCF.** If current FCF is depressed (cyclical down year), the yield is misleadingly high, and the company appears cheap.

**No accounting for leverage or capital structure.** Two companies with the same FCF yield might have very different leverage and risk.

## Refinement: FCF yield adjusted for growth

A common refinement is the **PEG-style adjustment**: compare FCF yield to expected growth.

Adjusted yield = FCF yield + Expected growth rate

Or simply: compare yield-to-growth ratio. A company yielding 5% with 10% growth is "cheaper" than a company yielding 5% with 0% growth.

This is less precise than full DCF but much simpler.

## When FCF yield is useful

**Screening a large list of stocks.** Quickly identify which are potentially cheap.

**Monitoring a portfolio.** Regular FCF yield calculations show if individual holdings are becoming cheaper or more expensive.

**Rough valuation.** You need a ballpark value in minutes, not a detailed model.

**Comparing mature, stable businesses.** For companies with similar risk profiles and growth rates (e.g., dividend-paying utilities), FCF yield is directly comparable.

## When FCF yield is misleading

**Growth companies.** A startup with negative FCF but huge growth potential is valued poorly by FCF yield.

**Cyclical businesses.** A commodity company at trough earnings has high FCF yield but poor value.

**Distressed companies.** A company on the edge of bankruptcy might have high FCF yield but zero real value.

**Structural change.** A company whose business model is disrupting and FCF will plummet looks good by current FCF yield but is actually a value trap.

## Integration with DCF

FCF yield valuation can be a starting point or reality check on DCF:

1. Calculate DCF intrinsic value.
2. Calculate implied FCF yield from that valuation (DCF value as EV, current FCF as FCF).
3. Compare implied yield to required yield. If they don't align, reconsider assumptions.

A DCF implying a 3% FCF yield when you require 8% suggests your terminal growth or discount-rate assumptions are too aggressive.

## See also

<div class="wiki-seealso">

### Closely related

- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation/) — the detailed approach
- [Enterprise value](/enterprise-value/) — the denominator
- [Free cash flow](/free-cash-flow/) — the numerator
- Yield — the metric

### Related metrics

- Earnings yield — earnings version of the same idea
- Dividend yield — cash-returned version

### Valuation integration

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — detailed method
- [Multiples valuation](/multiples-valuation/) — multiple approaches
- [Comparable company analysis](/comparable-company-analysis/) — peer comparison
- [Football field valuation](/football-field-valuation/) — combining methods

### Adjustments and refinement

- [PEG ratio](/peg-ratio/) — yield adjusted for growth
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — required yield sensitivity

</div>

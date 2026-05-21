---
title: "Capital Asset Pricing Model"
description: "A method for estimating the cost of equity by combining a risk-free rate, a market risk premium, and the company's beta—the standard approach in modern finance."
keywords:
  - CAPM
  - capital asset pricing model
  - cost of equity
  - beta
  - market risk premium
image: "https://picsum.photos/seed/capital-asset-pricing-model/900/600"
---

*The **capital asset pricing model (CAPM)** is perhaps the most important formula in modern finance: cost of equity equals the risk-free rate plus beta times the market risk premium. It is simple, testable, and ubiquitous. It is also imperfect, which is why academics and practitioners have been tinkering with it for decades.*

## The formula and what it says

Cost of equity = Risk-free rate + Beta × Market risk premium

This says: the return you should demand for holding a stock is a baseline (what you can get risk-free) plus an adjustment for the stock's riskiness (how much it wiggles relative to the market, times how much extra return the market demands for that wiggling).

If the 10-year Treasury yields 4%, the market risk premium is 6%, and a stock has a beta of 1.2, then its cost of equity is 4% + 1.2×6% = 11.2%.

The elegance is its simplicity. The problem is that each input is uncertain and debatable.

## The three inputs

**Risk-free rate.** Conventionally, the yield on a 10-year US Treasury, though some use 20-year or 30-year. The choice depends on your valuation horizon. For a perpetual valuation, a very long-term rate makes sense; for a 5-year projection, something shorter might suffice. In normal times, this is the least controversial input.

**Beta.** The slope of the regression line when you plot a stock's returns against market returns. A beta of 1 means the stock moves in line with the market. Above 1 means it is more volatile than the market. Below 1 means it is less volatile.

High-beta stocks (tech, biotech, small-cap growth) have beta of 1.5–2.0 and are risky. Low-beta stocks (utilities, consumer staples) have beta of 0.5–0.7 and are stable. But beta is backward-looking and changes over time.

**Market risk premium.** The extra annual return investors demand for holding the overall market instead of a risk-free asset. Historical data from 1926–present suggests 5–7% in the US (depending on which average you use). Current estimates are often 5–6%.

## Beta: the moving target

Beta is central to CAPM, but it is unstable. A company's beta reflects both its business risk (how volatile its earnings are) and its financial risk (its leverage). As a company matures, its business risk can decline, lowering beta. If it levers up, financial risk rises, raising beta.

Beta is usually estimated by regression over 3–5 years, but the choice of window affects the result. A 3-year regression captures recent volatility; a 5-year regression is more stable but slower to adapt to structural changes.

Sector averages help. All software companies might have average beta of 1.3; all utilities might have average beta of 0.6. Using sector beta instead of company-specific beta is sometimes more reliable than relying on a single company's regression.

For a company changing its business model or leverage, adjusting beta is necessary. Unlevering the current beta, then relevering at target capital structure, is the standard practice.

## Why the market risk premium is controversial

Is it 5%? 6%? 7%? This single input swings the valuation significantly. In the 2010s, with interest rates at zero and valuations elevated, many practitioners used 5% or lower. The academic consensus is broader: 5–7%.

Some estimate it forward-looking based on current valuations and growth expectations rather than relying purely on history. If the market trades at a 15x earnings multiple and growth is 2%, the implied market return might be 7.7% (inverse of PE plus growth). Subtract the risk-free rate, and you have a forward-looking premium.

No perfect answer exists. Using 5–6% is conservative and credible. Using 7% is at the high end but defensible.

## The assumptions CAPM embeds

CAPM assumes perfect markets, no taxes, and rational investors. None of these are true. In reality:

- Taxes and transaction costs exist, changing returns.
- Not all investors are rational (behavioral finance shows otherwise).
- Markets have frictions—some assets are hard to borrow, some investors cannot short.

So CAPM is a simplification. But it is a simplification that works pretty well for most purposes.

## CAPM's weaknesses and amendments

**The equity premium puzzle.** Historical equity returns (10% annually) seem far too high relative to what CAPM would predict given reasonable risk preferences and bond returns (2–3%). Why do investors settle for such high risk premia? CAPM does not have a great answer.

**Size and value effects.** Small stocks and value stocks have historically returned more than CAPM would predict. This led to the [Fama-French three-factor model](/fama-french-three-factor-model), which adds premiums for size and value.

**Momentum.** Stocks that have recently gone up tend to continue going up; those that have gone down tend to continue going down. CAPM does not capture this.

**Liability-matching.** For long-duration liabilities (pension funds, insurers), the relevant discount rate for assets depends on the duration of the liabilities, not just market risk. CAPM ignores this.

## Practical application in valuation

To use CAPM in a valuation:

1. Choose a risk-free rate (10-year Treasury, typically 3–5%).
2. Look up the company's beta (from Bloomberg, Yahoo Finance, etc.) or estimate it via regression.
3. Choose a market risk premium (5–6% is standard).
4. Calculate cost of equity.
5. Run sensitivity: show cost of equity at ±0.5% to ±1% on market risk premium and ±0.2 to ±0.5 on beta.

The result is your discount rate for a DCF model, a [dividend discount model](/dividend-discount-model), or any other equity valuation.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost of equity](/cost-of-equity) — what CAPM estimates
- [Beta](/beta) — a key CAPM input
- [Market risk premium](/market-risk-premium) — the other key input
- [Equity risk premium](/equity-risk-premium) — the premium for holding equities
- [Weighted average cost of capital](/weighted-average-cost-of-capital) — uses cost of equity from CAPM

### Variants and extensions

- [Fama-French three-factor model](/fama-french-three-factor-model) — adds size and value factors
- [Carhart four-factor model](/carhart-four-factor-model) — adds momentum
- [Fama-French five-factor model](/fama-french-five-factor-model) — adds profitability and investment factors
- [Build-up method cost of equity](/build-up-method-cost-of-equity) — additive alternative

### Valuation frameworks

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses CAPM-derived cost of equity
- [Dividend discount model](/dividend-discount-model) — uses cost of equity as discount rate
- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation) — uses WACC, which includes CAPM cost of equity

### Analysis

- [Sensitivity analysis](/sensitivity-analysis-valuation) — CAPM input sensitivity
- [Football field valuation](/football-field-valuation) — ranges across assumptions

</div>

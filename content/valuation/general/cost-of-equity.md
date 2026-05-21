---
title: "Cost of Equity"
description: "The minimum rate of return that equity investors demand on their investment, determined by the risk of the company and alternative investment opportunities."
keywords:
  - cost of equity
  - required return
  - CAPM
  - equity risk premium
  - discount rate
image: "/svg/valuation.svg"
---

*The **cost of equity** is the minimum return that shareholders demand for holding a company's stock, given its riskiness. It is a crucial input to every equity valuation model and a key component of the [weighted average cost of capital](/weighted-average-cost-of-capital/). Despite decades of academic work, estimating it remains more art than science.*

## What cost of equity represents

Think of cost of equity as an investor's hurdle rate. If I can buy a US Treasury bond and earn 5% with no risk, why would I buy your stock unless I expect at least 10% or 12% return? The extra return—that 5–7 percentage points above the risk-free rate—is compensation for risk.

Cost of equity has two components: a baseline (the risk-free rate) and a risk premium (extra return for bearing risk). The baseline is typically the yield on a long-term government bond. The risk premium depends on how risky the company is relative to the market.

## The capital asset pricing model

The CAPM is the most widely used method to estimate cost of equity. It states that cost of equity equals the risk-free rate plus the company's beta times the [market risk premium](/market-risk-premium/).

Risk-free rate: The yield on a 10-year US Treasury, roughly 3–5% depending on economic conditions.

Beta: A measure of how much the company's stock moves with the overall market. A beta of 1 means it moves in line with the market. A beta of 1.2 means it is 20% more volatile than the market. A beta of 0.8 means it is 20% less volatile.

Market risk premium: The extra return investors demand for holding the overall market instead of a risk-free asset. Historical data suggests 5–7%, though current estimates vary.

**Example:** Risk-free rate 4%, company beta 1.1, market risk premium 6%. Cost of equity is 4% plus (1.1 times 6%), or 10.6%.

## Estimating beta

Beta is typically estimated by running a regression of the company's stock returns against market returns over 3–5 years. If the stock returned 15% in a year when the market returned 10%, and this pattern repeats, beta is around 1.5.

Beta can be looked up from data providers (Bloomberg, Capital IQ, Yahoo Finance) but comes with caveats. Historical beta may not predict future beta. Beta changes when a company's business model shifts or its leverage changes.

A high-beta company (tech, biotech, small-cap growth) might have beta of 1.5–2.0. A low-beta company (utilities, consumer staples) might have beta of 0.5–0.8.

## Size of the market risk premium

This is the most hotly debated input. The historical arithmetic mean return of US equities is roughly 10%, and the risk-free rate has averaged 2–3%. This suggests a market risk premium of 7–8%.

But is past equal to future? In the 2010s, when valuations were high and rates were very low, many practitioners used 5–6% instead. The choice matters: a 1% difference in market risk premium swings cost of equity by 1% and valuation by 10–15%.

No consensus exists. Practitioner surveys show responses ranging from 4% to 7%. Using 5–6% is defensible and common.

## Beyond CAPM: other models

**Build-up method.** Instead of using beta, add premiums: risk-free rate plus equity risk premium plus size premium (for small companies) plus company-specific risk. This is more transparent but requires estimating each premium independently.

**Fama-French factors.** The [Fama-French three-factor model](/fama-french-three-factor-model/) adds size and value premiums to market beta. The result is often a slightly different cost of equity than CAPM alone.

**Dividend discount model implied return.** Work backward from the [Gordon growth model](/gordon-growth-model/): current dividend, next-year growth assumption, current stock price. Solve for the discount rate. This is what the market is implicitly assuming.

**Earnings yield approach.** For a mature company, use earnings divided by market cap, then add a growth expectation. If earnings yield is 5% and you expect 3% growth, cost of equity is roughly 8%. Less rigorous but sometimes useful.

## The leverage trap

Cost of equity depends on leverage. A company with no debt has lower cost of equity than an identical company with high debt. Why? Because equity holders are farther down the priority ladder when debt is present; the stock is riskier; they demand higher returns.

The relationship is not linear. A moderate amount of leverage (debt-to-value of 30%) might not materially increase cost of equity. But heavy leverage (70%+) can increase it substantially.

When you change a company's capital structure in a valuation (e.g., a private equity sponsor levering it up), you must relevel cost of equity. Unlever the current beta, then relever using the target capital structure.

## Common mistakes

**Using the wrong risk-free rate.** The risk-free rate should match the horizon of your valuation. For a perpetual DCF, use a long-term (10–30 year) government bond, not the short-term rate.

**Using an unrealistic market risk premium.** Anchoring to historical averages makes sense, but blind adherence to 7% when valuations are elevated and rates are low is lazy.

**Ignoring that beta changes with leverage.** If you are valuing a company at a different leverage than its current state, adjust beta accordingly.

**Using a cost of equity that is internally inconsistent.** If you assume 8% cost of equity but your terminal value assumes 3% perpetual growth, the math works. But does your growth assumption imply that the company will grow faster than your required return in perpetuity, which is impossible?

## Sensitivity and ranges

Because cost of equity is uncertain, running sensitivity analysis is critical. Build your valuation at 9%, 10%, 11%, and 12% cost of equity. If the range is narrow, the valuation is robust. If it is wide, you are betting heavily on a precise cost-of-equity estimate.

Most valuations are most sensitive to cost of equity in the perpetuity calculation. A 1% change in cost of equity often swings valuation by 15–30%.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital asset pricing model](/capital-asset-pricing-model/) — the standard estimation method
- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — uses cost of equity
- [Market risk premium](/market-risk-premium/) — a key CAPM input
- [Equity risk premium](/equity-risk-premium/) — the market risk premium plus company-specific premium
- [Beta](/beta/) — a key CAPM input

### Alternative estimation methods

- [Fama-French three-factor model](/fama-french-three-factor-model/) — adds size and value factors
- [Build-up method cost of equity](/build-up-method-cost-of-equity/) — additive approach

### Valuation frameworks using cost of equity

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — parent method
- [Dividend discount model](/dividend-discount-model/) — uses cost of equity as discount rate
- [Free cash flow to equity valuation](/free-cash-flow-to-equity-valuation/) — uses cost of equity directly

### Testing and sensitivity

- [Sensitivity analysis](/sensitivity-analysis-valuation/) — cost-of-equity sensitivity
- [Football field valuation](/football-field-valuation/) — ranges across assumptions

</div>

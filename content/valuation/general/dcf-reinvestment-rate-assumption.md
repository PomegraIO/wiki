---
title: "Reinvestment Rate Assumption in DCF Models"
description: "How reinvestment rate assumptions in DCF valuation link a company's growth to free cash flow, and why mismatched assumptions cause systematic valuation errors."
keywords:
  - reinvestment rate assumption
  - dcf reinvestment
  - free cash flow growth
  - terminal value growth
  - fcf to nopat
  - capex assumptions
  - cost of capital
image: "/svg/valuation.svg"
---

*The **reinvestment rate assumption** in a DCF model determines what fraction of free cash flow a company must spend on capital expenditure and working capital to sustain a given growth rate. If a firm grows at 5% but the model assumes it reinvests only 2% of cash flow, the math is broken—the model will either overvalue the company or predict unsustainable cash distributions. Consistency between growth, reinvestment, and [free cash flow](/free-cash-flow/) is the linchpin of DCF accuracy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reinvestment Rate — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Reinvestment rate links profitability to sustainable growth.</div>

|   |   |
|---|---|
| **Definition** | Share of free cash flow or NOPAT needed to fund growth |
| **Mathematical form** | Growth rate ÷ return on invested capital (ROIC) |
| **Typical range** | 20–70% for mature firms; 80%+ for high-growth |
| **Key constraint** | Reinvestment rate + payout ratio = 1.0 |
| **Terminal rate** | Often set to match long-run GDP or inflation growth |
| **Error source** | Disconnecting growth assumption from reinvestment needs |

</aside>

## The fundamental reinvestment equation

Free cash flow available to all investors (debt and equity holders) equals NOPAT (net operating profit after tax) minus the reinvestment needed to sustain growth. The relationship is:

**Growth rate = ROIC × Reinvestment rate**

where ROIC is the return on invested capital and the reinvestment rate is the fraction of NOPAT (or operating cash flow) dedicated to capital expenditure, acquisitions, and working capital increases.

This equation is not theoretical—it reflects an iron law of competitive markets. A company cannot grow at 10% per year unless it either (1) earns 10% on every dollar already invested and reinvests nothing extra, or (2) reinvests a portion of its profits back into the business. A retail chain with 15% ROIC can grow at 5% while reinvesting one-third of profits, or grow at 10% while reinvesting two-thirds. Growth and reinvestment are mathematically yoked.

## Why reinvestment assumptions trip up valuers

Most DCF errors stem from one of three mistakes:

**1. Assuming high growth with low reinvestment.** A model projects sales growth of 12% per year but assumes capex will stay flat, or that working capital won't expand. This is impossible if the company is genuinely growing and operating in the same markets with the same asset efficiency. Either growth will be lower than projected, or the model is hiding a massive improvement in ROIC—which is fine if explained, but usually is not.

**2. Assuming high ROIC without justifying why.** A model assumes the company will reinvest 40% of cash flow at a 20% return indefinitely. That is a competitive moat claim. If the company competes in a liquid, rational market with substitutes, sustainable ROIC above the cost of capital will shrink as competitors enter. The model must explain *why* this firm will durably outcompete.

**3. Mismatch between cash flow and reinvestment.** The model projects free cash flow by deducting capex, but then assumes that capex (reinvestment) will decline as a percentage of sales, implying growth will slow. But the implicit reinvestment rate in the model no longer supports the stated growth rate, creating internal inconsistency.

## Linking reinvestment to cash flow components

In practice, a DCF modeler estimates reinvestment by tracking three cash drains: capex, depreciation, and changes in net working capital.

**Reinvestment = Capex − Depreciation + Δ Net Working Capital**

Capex is the cash spent on plant, equipment, and acquisitions. Depreciation is a non-cash charge that roughly recovers historical capex (though it lags and may differ in amount). The difference, *capex minus depreciation*, is net capex: the true cash cost of maintaining and growing the asset base. Net working capital—receivables plus inventory minus payables—expands when a company grows, absorbing cash, and shrinks during contraction, releasing cash.

If a company has stable margins and steady growth, its reinvestment rate often stabilizes. A telecom with 5% revenue growth might need 3% net capex and 0.5% working capital growth, totaling 3.5% reinvestment. If NOPAT grows at 5%, then 3.5% ÷ 5% = 70% reinvestment rate. This is self-reinforcing and plausible for a mature, capital-intensive business.

Conversely, a software company with 15% growth, minimal capex, and shrinking working capital (net cash collection improving) might need only 5% reinvestment, implying a 33% reinvestment rate. The DCF can then payout 67% of free cash flow to investors—a vastly different capital structure than the telecom.

## Terminal value and the long-run reinvestment rate

The terminal value (the present value of all cash flows beyond the explicit forecast period) often hinges on reinvestment rate assumptions. A common terminal value formula is:

**Terminal FCF = NOPAT × (1 − Reinvestment Rate)**

If terminal growth is assumed to equal long-run GDP growth—say, 2–3% in developed markets—then the reinvestment rate must support that growth. If ROIC is 10%, reinvestment is 25% (2.5% growth ÷ 10% ROIC). The model then distributes 75% of terminal NOPAT as free cash flow.

Here is where carelessness destroys credibility. Modelers sometimes assume *high* terminal growth (4–5%) but *low* reinvestment (10–15%), assuming the company will somehow grow faster than GDP while needing less capital. This violates the growth equation. Either:

- Assume terminal growth matches long-run GDP growth (2–3%), allow reinvestment to decline, and validate that ROIC stays above cost of capital; or
- Assume higher terminal growth and proportionally higher reinvestment, and justify why this company will sustain above-market returns for decades.

## From NOPAT to investable FCF

A clean DCF flow works from NOPAT down:

1. Start with NOPAT (operating profit after tax)
2. Subtract reinvestment (net capex + change in NWC)
3. Arrive at unlevered free cash flow (FCF to all investors)
4. Discount at weighted average cost of capital (WACC)

Alternatively, some modelers work in terms of return on invested capital directly:

**Unlevered FCF = Invested Capital × (ROIC − WACC) / (1 + WACC)**

This formula highlights that value creation—the spread between ROIC and WACC—drives cash available to investors. If ROIC equals WACC, all operating cash flow is reinvested; no cash is left over. If ROIC exceeds WACC, the spread creates value.

Both approaches are equivalent; the choice is pedagogical. The key is internal consistency: growth, reinvestment, and ROIC must all move together.

## Sector and life-cycle variation

Reinvestment rates vary wildly by business stage and sector.

**Mature, capital-light businesses** (software, consumer staples with owned brands) often show 20–40% reinvestment rates. They grow slowly but generate cash because their competitive moats allow high ROIC with minimal new investment.

**Growing, capital-intensive businesses** (infrastructure, manufacturing, real estate) might show 50–80% reinvestment. They burn cash to build capacity that will earn returns later. A DCF of such a company must accept that near-term free cash flow will be modest, but long-term value rests on successful execution.

**Declining businesses** sometimes show negative reinvestment (capex below depreciation) as the firm harvests residual cash. The reinvestment rate formula still holds: if a business shrinks 5% per year and has ROIC of 8%, reinvestment is negative (−62% of NOPAT, meaning the firm is harvesting).

## Stress-testing reinvestment assumptions

Experienced valuers always run sensitivity analyses on reinvestment rate. A 5–10 percentage point swing in the reinvestment assumption can swing valuation by 20–40%. The test is: over the explicit forecast period, what do capex, depreciation, and working capital *actually* show in the financial statements? Do they support the assumed reinvestment rate?

A second check: does the company's *historical* reinvestment rate match the assumption going forward? If a firm has reinvested 45% of NOPAT for the past decade but the model assumes 25% in the forecast, the burden is on the modeler to explain the structural shift. Cost productivity gains? Asset sales? Reduced working capital? Without clear drivers, the assumption is a red flag.

Third, compare the model's implied ROIC growth with competitive dynamics. If ROIC is assumed to stay at 18% for ten years while the cost of capital is 9%, the model is claiming perpetual competitive advantage. That may be true (Apple, Visa), but it must be explicitly justified, not buried in reinvestment assumptions.

## See also

<div class="wiki-seealso">

### Closely related

- [Free Cash Flow](/free-cash-flow/) — the cash available after reinvestment, the numerator of DCF
- [Return on Invested Capital](/return-on-invested-capital/) — determines how much growth a given reinvestment rate supports
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the model framework where reinvestment assumptions live
- [Terminal Value](/terminal-value/) — most sensitive to reinvestment rate in long-term models
- [Cost of Capital](/cost-of-equity/) — the discount rate paired with cash flow in DCF
- Net Operating Profit After Tax — the starting point before reinvestment deduction

### Wider context

- Capital Expenditure — the cash outflow underlying reinvestment
- Working Capital Management — determines portion of reinvestment tied to operations
- [Relative Valuation](/relative-valuation/) — alternative to DCF; less sensitive to reinvestment assumptions
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — the stress test that validates reinvestment assumptions

</div>

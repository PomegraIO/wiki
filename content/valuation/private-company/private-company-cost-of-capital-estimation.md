---
title: "Estimating Cost of Capital for a Private Company"
description: "Methods to estimate cost of capital for private company valuation when no traded equity exists, using build-up and beta adjustments."
keywords:
  - cost of capital private company
  - discount rate private firm
  - build-up method unlevered beta
  - total beta private equity
  - risk adjustment private valuation
image: /svg/valuation.svg
---

*When a private company has no traded shares, appraisers cannot simply look up a market beta. Instead, they construct a cost of capital by building up from risk-free rates and comparable firms, or by using total beta to capture risks beyond what public markets measure. The method you choose shapes the valuation.**

An investor or appraiser trying to value a private company faces a core problem: the [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) formula needs a [discount rate](/discount-rate/), but there is no stock price or market data to derive it from directly. Estimating cost of capital for a private company means synthesizing a rate that reflects both the firm's business risk and its financial risk, even though it does not trade. Three main approaches dominate practice: the build-up method, the [capital-asset-pricing-model](/capital-asset-pricing-model/) (CAPM) adjusted for private company risk, and total beta. Each has strengths and blind spots.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Capital Estimation — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Private firms require custom discount-rate methods since no public market price anchors the cost of equity.</div>

|   |   |
|---|---|
| **Core formula** | Risk-free rate + Risk premiums, or CAPM adjusted for private factors |
| **Build-up layers** | RF + equity risk premium + size premium + company-specific premium |
| **Beta source** | Comparable public companies, unlevered and re-levered to target capital structure |
| **Total beta benefit** | Captures idiosyncratic risk; often 30–50% higher than market beta alone |
| **Valuation impact** | 1% change in discount rate can swing valuation 15–30% for 5–10 year hold |
| **Common pitfall** | Overstating size premiums or ignoring [leverage-ratio-forex](/leverage-ratio-forex/) on re-leveraging |

</aside>

## The Build-Up Method: Starting from Risk-Free Ground

The build-up method works like scaffolding. Start with the risk-free rate—typically the yield on a long-term U.S. Treasury bond—then add premiums for each incremental risk the private company faces.

The formula looks like this:

Cost of Equity = Risk-Free Rate + Equity Risk Premium + Size Premium + Company-Specific Premium

**Risk-free rate** is straightforward: use a 10- or 20-year Treasury yield that matches your valuation horizon. **Equity risk premium** is the historical average excess return stocks have earned over bonds—often cited as 5–7% based on long-run data. **Size premium** reflects that smaller firms are riskier than large-cap equities; it typically ranges from 1–5% depending on revenue or market-cap proxies. **Company-specific premium** accounts for risks unique to the target firm: customer concentration, key-person dependency, operational immaturity, or regulatory headwinds. This premium is the hardest to pin down and often ranges from 2–10%.

The beauty of build-up is its transparency: each layer is visible and defensible. The weakness is that the company-specific premium invites judgment calls. A typical build-up for a stable mid-market company might total 10–14%; for a early-stage tech firm, 18–25%.

## The CAPM Approach and Private Company Adjustments

[Capital-asset-pricing-model](/capital-asset-pricing-model/) says:

Cost of Equity = Risk-Free Rate + Beta × (Market Risk Premium)

For a private company, you cannot compute beta from its stock returns because it has no public stock. Instead, appraisers find a set of comparable public firms in the same industry, calculate their betas, unlever them (removing the effect of each comparable's debt), then re-lever using the private company's target capital structure.

**Unlevering** a beta strips out the amplification that debt creates. A levered beta reflects both business risk and financial risk. The formula is:

Unlevered Beta = Levered Beta ÷ (1 + (1 − Tax Rate) × Debt/Equity)

Once you have an unlevered beta from comparables, you re-lever it to match your private company's intended capital structure:

Relevered Beta = Unlevered Beta × (1 + (1 − Tax Rate) × Target Debt/Equity)

If your target company plans to borrow more than its comparables did, the new beta rises, raising the cost of equity. This correctly penalizes financial leverage.

One critical adjustment: private companies typically have no [liquidity](/liquidity-risk/) or [diversification](/diversification/) discount. Public betas are computed from liquid, frequently traded stocks. A private equity investor or minority shareholder in a private firm faces illiquidity risk—they cannot sell quickly—so many appraisers add a 2–5% illiquidity discount to the final cost of equity.

## Total Beta: Capturing Idiosyncratic Risk

Standard CAPM assumes investors hold diversified portfolios, so only systematic (market-related) risk matters. In reality, many private company investors—founders, private-equity sponsors, or family offices—hold concentrated positions. Total beta breaks this assumption.

Total beta includes both systematic risk (the market beta) and idiosyncratic risk (firm-specific volatility that diversified investors could ignore). The formula is:

Total Beta = Market Beta ÷ Correlation with Market

If a private company's returns are weakly correlated with the broader market—say, it is in a niche market or has unique technology—its idiosyncratic risk is high, and total beta can be 30–50% higher than market beta.

Example: A public company in the same space has a market beta of 1.2. Its stock returns correlate with the S&P 500 at 0.60 (a relatively low correlation, perhaps due to unique business dynamics). Its total beta would be 1.2 ÷ 0.60 = 2.0. Using 2.0 instead of 1.2 as the input to CAPM yields a noticeably higher cost of equity, reflecting the fact that a concentrated investor cannot diversify away as much risk.

Total beta is useful when the investor (or buyer) is likely to hold a large, undiversified stake, or when the firm's cash flows diverge significantly from market cycles.

## Choosing Among the Three Methods

**Build-up** works well when comparable public firms are scarce or the target company is mature but small. It is the method preferred by appraisers in industry-specific valuations (auto dealerships, medical practices, family businesses). The downside: the company-specific premium can hide judgment.

**CAPM with adjustments** is standard for companies in established sectors with clear public comparables. It forces discipline: every risk factor must map to a comparable. The re-levering step correctly accounts for the private company's own capital structure. Illiquidity discounts, while common, are controversial; not all appraisers apply them uniformly.

**Total beta** fits when the investor is concentrated and the company's risk profile is idiosyncratic—think a venture-backed software startup or a family business with proprietary processes. It is less common in mainstream valuations but valuable when it applies.

A best practice is to calculate cost of capital using two methods and compare. If build-up yields 12% and CAPM yields 11%, averaging or documenting the difference adds confidence. If the two methods diverge sharply (say, 10% vs. 16%), the discrepancy signals a missing risk factor or a comparables problem.

## Key Inputs and Sensitivity

The cost of capital is the single most powerful lever in a DCF valuation. A 1% change in the discount rate can swing a 10-year valuation by 15–30%, depending on the cash flow pattern. The inputs most worth stress-testing are:

- **Risk-free rate**: Use the tenor that matches your forecast horizon. A 30-year business plan might warrant a 20-year Treasury, not a 3-month bill.
- **Comparables and beta**: Ensure the comparables are truly comparable in product, geography, and profitability. A software company's beta is not transferable to a healthcare services firm.
- **Debt and tax rate**: Small changes to the assumed capital structure can materially shift the re-levered beta. Confirm the tax rate applies to the actual jurisdiction and time horizon.
- **Illiquidity discount**: If you apply one, document it. A 3% discount is modest; 10% is aggressive.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the framework that uses cost of capital as the discount rate
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — the foundational formula for cost of equity in public markets
- [Cost of Debt](/cost-of-debt/) — the other half of weighted-average cost of capital
- Comparable Company Analysis — how to find and use public comparables for private valuations
- [Valuation Multiple](/relative-valuation/) — an alternative approach less sensitive to discount-rate assumptions
- [Leverage Ratio](/leverage-ratio-forex/) — how debt structure feeds into cost of capital

### Wider context

- [Debt Financing](/debt-financing/) — sources and terms of private company borrowing
- [Equity Financing](/equity-financing/) — how private equity and venture investors price their capital
- [Risk Weighted Assets](/risk-weighted-assets/) — a parallel concept for banks
- [Return on Invested Capital](/return-on-invested-capital/) — benchmarking value creation against the cost of capital

</div>

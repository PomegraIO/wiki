---
title: "Weighted Average Cost of Capital"
description: "The blended cost of capital for a company, accounting for the cost of debt and cost of equity weighted by their market values. The discount rate used in most valuation models."
keywords:
  - WACC
  - weighted average cost of capital
  - cost of capital
  - discount rate
  - valuation
image: "/svg/valuation.svg"
---

*The **weighted average cost of capital (WACC)** is the average rate of return a company must earn to satisfy all of its investors—both debt holders and equity holders. It is the discount rate used in nearly every [free cash flow to firm valuation](/free-cash-flow-to-firm-valuation). Getting WACC right is critical; getting it wrong swings valuations by 20% or more.*

## What WACC is

A company finances itself with both debt and equity. Debt holders demand an interest rate; equity holders demand a return on their investment. WACC is a weighted average of these two costs, weighted by the market values of debt and equity.

If a company is 60% equity-financed and 40% debt-financed, and the cost of equity is 12% and the cost of debt is 6%, WACC is (0.60 times 0.12) plus (0.40 times 0.06), or 9.6%.

WACC is then used as the discount rate in a DCF model. Every dollar of future free cash flow is discounted at WACC back to present value. The discount rate reflects the riskiness of the cash flows and the opportunity cost of capital.

## The two components: cost of equity and cost of debt

**Cost of equity** is the return equity investors demand. It is typically estimated using the [capital asset pricing model](/capital-asset-pricing-model), which blends a risk-free rate, the [market risk premium](/market-risk-premium), and the company's [beta](/beta). For a typical company, cost of equity ranges from 8% to 15%.

**Cost of debt** is the interest rate the company pays on its borrowings. It is usually observable from bond yields or bank loan rates. But it must be adjusted for taxes: because interest is tax-deductible, the after-tax cost of debt is lower. The after-tax cost of debt is interest rate times (1 minus tax rate).

## Weighting: market values, not book values

This is a frequent mistake. Use market values of debt and equity, not book values. Market value of equity is share price times share count. Market value of debt is the current market price of bonds (or, if not observable, a yield-based estimate of fair value).

Why market values? Because you are building a present-value model. Equity investors think about the market value of their stake, not the book value. Debt investors, if they have a choice (which they do, trading bonds daily), think about market value. Book values are historical accounting artifacts.

Using book values overstates WACC if the equity has appreciated significantly (as it does in many successful companies) and understates WACC if book value exceeds market value (distressed firms, asset-heavy businesses).

## Tax effects and after-tax cost of debt

Interest paid to debt holders is tax-deductible. This creates a tax shield: the government effectively subsidizes debt. For a company paying 6% on debt with a 25% tax rate, the after-tax cost is 6% times (1 minus 0.25), or 4.5%.

This tax effect is why highly leveraged companies have lower WACC than unleveraged ones: more of the capital is financed with cheaper, tax-deductible debt. But leverage also increases financial risk, pushing up the cost of equity. The net effect depends on the level of leverage and the company's business risk.

## Estimating WACC in practice

**Step 1:** Establish the capital structure. What is the market value of debt? What is the market value of equity? Weights as D over (D plus E) and E over (D plus E).

**Step 2:** Estimate the cost of equity using the capital asset pricing model or another method. Typical range: 8–15%.

**Step 3:** Estimate the cost of debt. If the company has traded bonds, use their yield. If not, use the credit rating to estimate a reasonable rate (BBB corporates typically yield 4–6% in normal times, higher in stress).

**Step 4:** Adjust for taxes. After-tax cost of debt is cost of debt times (1 minus marginal tax rate).

**Step 5:** Calculate WACC as (E over D plus E) times cost of equity plus (D over D plus E) times after-tax cost of debt.

## The leverage paradox

Leverage is a double-edged sword. Debt is cheaper than equity (it is senior in bankruptcy, so less risky). Using debt to finance the business lowers WACC. But leverage also increases the risk to equity holders, raising the cost of equity.

For a company with zero debt and cost of equity of 10%, issuing debt at 5% and using it to buy back equity might lower WACC initially. But as leverage rises, the cost of equity rises, and at some point, the benefit reverses. There is an optimal capital structure somewhere between zero and 100% debt, though finding it is harder than the theory suggests.

This is why WACC is stable for moderately leveraged companies but rises sharply for highly leveraged ones.

## Unlevering and relevering WACC

Sometimes you need to adjust WACC for a different capital structure. An analyst might unlever the beta of a highly leveraged company, then relever it at the leverage of the target company.

**Unlevering:** Remove the effect of current debt on cost of equity, using a formula that accounts for the current debt-to-equity ratio and tax rate. The result is the cost of equity the company would have if it were unleveraged.

**Relevering:** Apply that unlevered cost of equity to a different debt-to-equity ratio to get a new levered cost of equity, and then recalculate WACC.

This is useful in M&A when you are valuing a company on a different balance sheet than its current one.

## Common mistakes

**Using book values instead of market values.** Massively distorts WACC, especially for appreciating equities.

**Using wrong tax rate.** Some analysts use the statutory rate; others use the effective rate. Be consistent and explicit.

**Ignoring leverage changes.** If you forecast debt declining substantially, WACC should change in the terminal period. Constant WACC through changing leverage is lazy.

**Conflating cost of capital with required return.** They are the same thing, but the conceptual difference matters: WACC is what the company must earn; required return is what investors demand. The company earns WACC only if it is earning its weighted average returns.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost of equity](/cost-of-equity) — the equity component
- [Cost of debt](/cost-of-debt) — the debt component
- [After-tax cost of debt](/after-tax-cost-of-debt) — the tax-adjusted version
- [Capital asset pricing model](/capital-asset-pricing-model) — estimating cost of equity
- [Equity risk premium](/equity-risk-premium) — input to CAPM

### Valuation frameworks

- [Free cash flow to firm valuation](/free-cash-flow-to-firm-valuation) — WACC's primary use
- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — parent method
- [Two-stage DCF](/two-stage-dcf) — uses WACC
- [Three-stage DCF](/three-stage-dcf) — uses WACC

### Sensitivity and structure

- [Sensitivity analysis](/sensitivity-analysis-valuation) — testing WACC sensitivity
- [Football field valuation](/football-field-valuation) — ranges including WACC variation
- [Scenario valuation](/scenario-valuation) — different structures, different WACCs

</div>

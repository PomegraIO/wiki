---
title: "Cost of Equity in the Residual Income Model"
description: "The cost of equity in the residual income model is the discount rate applied to excess profit; small changes in this rate swing intrinsic value sharply."
keywords:
  - cost of equity residual income model
  - required return on equity
  - residual income valuation
  - capm cost of equity
  - equity discount rate
  - valuation sensitivity
---

*The **cost of equity** in the [residual income model](/residual-income-model/) is the required return on shareholders' capital—the hurdle rate against which actual earnings are measured. Any excess profit above this cost constitutes residual income and adds value; conversely, if earnings fall short of the cost of equity, the firm is destroying value. Because residual income is discounted at the cost of equity, small changes in this single input can swing intrinsic value by 10–20% or more. Understanding how the cost of equity is estimated and why it matters so heavily to the final valuation is critical for anyone relying on the residual income framework.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Equity in the Residual Income Model — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">The single most sensitive input in the residual income model; small errors compound over time.</div>

|   |   |
|---|---|
| **Definition** | The minimum annual return shareholders require to justify holding equity |
| **Common method** | [Capital Asset Pricing Model (CAPM)](/capital-asset-pricing-model/) |
| **CAPM formula** | r = Rf + β(Rm − Rf) |
| **Role in RI** | Denominator of discount rate; threshold for excess profit |
| **Typical range** | 7–12% for mature firms; varies by beta and risk premium |
| **Sensitivity** | 1% change in r can shift intrinsic value by 15–25% |
| **Stability** | Should be constant or rise slowly; sudden changes signal reassessment |

</aside>

## What Cost of Equity Means in Residual Income Valuation

In the residual income model, the cost of equity (r) serves two purposes:

1. **The threshold for profit creation**: Any earnings above r × book equity constitute residual income; earnings below this level destroy value.
2. **The discount rate**: Residual income is discounted at rate r to calculate its present value, which is added to current book equity.

A company with $100 million in book equity and a 10% cost of equity needs to generate at least $10 million in net income each year to earn its cost of capital. If it earns $12 million, it has created $2 million in residual income—value accretion. If it earns $8 million, it has created negative residual income, and shareholder wealth is eroding.

This is fundamentally different from the income statement perspective, where "profit is profit." In residual income analysis, profit matters only insofar as it exceeds what capital providers could have earned in alternative investments of similar risk.

## The Capital Asset Pricing Model (CAPM) Approach

The most widely used method for estimating cost of equity is the [Capital Asset Pricing Model (CAPM)](/capital-asset-pricing-model/):

r = Rf + β(Rm − Rf)

Where:
- **Rf** = risk-free rate (typically the yield on long-term government bonds)
- **β** = beta, the stock's sensitivity to overall market movements
- **(Rm − Rf)** = market risk premium, the expected excess return of equities over risk-free securities

### Example Calculation

Suppose:
- Risk-free rate (Rf): 4.0% (long-term U.S. Treasury yield)
- Beta (β): 1.2 (the stock is 20% more volatile than the broad market)
- Market risk premium (Rm − Rf): 6.0% (historical equity premium, though it varies with market conditions)

Cost of equity = 4.0% + 1.2(6.0%) = 4.0% + 7.2% = 11.2%

This 11.2% is the minimum annual return the firm must earn on equity capital to compensate shareholders for the risk they bear. Earnings above this threshold create residual income; earnings below it destroy value.

## The Three Inputs: Sensitivity and Controversy

**Risk-Free Rate (Rf)**

The risk-free rate is typically the yield on long-term government bonds (e.g., the 10-year U.S. Treasury). It represents the rate at which capital providers could invest with zero default risk. This input is observable and changes daily with market conditions.

Sensitivity: A 1% drop in Rf (e.g., from 4.0% to 3.0%) lowers the cost of equity directly. If this occurs because economic growth is slowing, the lower cost of equity may not be offset by higher earnings, so residual income could actually increase in value despite lower discount rates.

**Beta (β)**

Beta measures the systematic risk of the stock—how much it moves relative to the broad market. A beta of 1.0 means the stock moves with the market; 1.5 means it is 50% more volatile; 0.8 means it is 20% less volatile.

Beta is estimated using historical price data (typically 3–5 years of monthly or weekly returns regressed against market returns). It is forward-looking in intention but backward-looking in calculation, creating a persistent ambiguity. A firm's business risk may have changed (e.g., higher leverage, new market exposure), but historical beta may lag this shift.

Sensitivity: A 0.2-point increase in beta (e.g., from 1.0 to 1.2) raises the cost of equity by 1.2% (if the market risk premium is 6%). For a firm with $100 million in annual earnings and $1 billion in book equity, a 1.2% rise in cost of equity swings the residual income threshold from $12 million to $13.2 million annually, reducing residual income by $1.2 million per year. Over a 10-year explicit forecast horizon, this could reduce intrinsic value by 10–15%.

**Market Risk Premium (Rm − Rf)**

The market risk premium is the extra return investors expect from holding equities versus risk-free assets. Historical U.S. equity premiums (since 1926) average around 6–7%, but forward-looking surveys and academic estimates range from 4% to 8%, depending on methodology and time period.

This is the most controversial input. It is not directly observable; it reflects collective expectations about future equity returns. Different analysts justify different premiums based on historical averages, survey methods, or theoretical models. A 1% difference in the market risk premium (e.g., 6% vs. 7%) translates directly into a 1% change in the cost of equity for a beta-1 stock.

Sensitivity: For a cyclical stock with beta 1.5, a 1% swing in the assumed market risk premium changes the cost of equity by 1.5%, a material impact on residual income valuation.

## Why Cost of Equity Dominates Residual Income Valuation

The cost of equity affects the residual income model in two ways:

1. **It is the numerator denominator**: Raising r increases the income hurdle, shrinking residual income. All else equal, higher cost of equity lowers intrinsic value.
2. **It is the discount rate**: Residual income is divided by (1 + r)^t, so higher r reduces present values. Again, higher cost of equity lowers intrinsic value.

Because of these dual roles, the cost of equity is the most sensitive input in the model. A 1% misestimate compounds over time:

Year 1 RI effect: r% × Book Equity is deducted from earnings, reducing residual income by roughly r%.

Year 2+ discount effect: The entire residual income stream is discounted at the wrong rate, creating a 1% reduction in present value per year of positive r%, or roughly (1 + discount error) × (1 + numerator error).

In practice, a 1% error in cost of equity typically swings intrinsic value by 15–25%.

## Practical Approaches to Cost of Equity Estimation

**Method 1: Pure CAPM**

Use observable inputs (Rf from Treasury yields, β from historical regression) and a market risk premium assumption (typically 5–7%). This is transparent and widely accepted.

**Method 2: Dividend Discount Model Implied Cost of Equity**

If the firm pays a stable, growing dividend, solve for the cost of equity that makes the dividend discount model consistent with current market price. This inverts the valuation process: instead of assuming r and calculating value, you assume value and solve for r, then compare to CAPM to sense-check reasonableness.

**Method 3: Build-up Approach**

Start with Rf, add a premium for business risk (the risk of the firm's operations independent of leverage), add a premium for financial risk (leverage), and add a small-company or industry-specific premium if applicable. This is useful when beta is unreliable or the firm is not publicly traded.

## Sensitivity Analysis: The Mandatory Step

Because cost of equity is so sensitive, every residual income valuation should include a sensitivity table showing how intrinsic value changes across a range of cost-of-equity assumptions. For example:

| Cost of Equity | Intrinsic Value per Share |
|---|---|
| 9.0% | $85 |
| 10.0% | $72 |
| 11.0% | $62 |
| 12.0% | $54 |

This table reveals that a 300-basis-point change in cost of equity (9% to 12%) swings intrinsic value from $85 to $54—a 37% range. It also helps the analyst identify which assumptions drive the valuation and where estimation errors are most costly. If the analyst is confident in cost of equity at 10%, the plausible valuation range is $62–$72 (assuming ±100 bps of uncertainty), and an intrinsic value estimate outside this range suggests other forecast errors.

## Reconciling Cost of Equity with Other Valuation Approaches

In a [discounted cash flow (DCF)](/residual-income-vs-dcf-which-to-use/) valuation, the cost of equity is a component of the weighted average cost of capital (WACC), which discounts free cash flows. The residual income model uses cost of equity directly to discount residual income. If the two models are applied correctly, they should yield the same intrinsic value, but this requires that cost of equity in the RI model and cost of equity (as a component of WACC in the DCF model) are consistent.

A mismatch is a red flag. If DCF implies a 10% cost of equity via WACC, but the RI model is built using a 12% cost of equity, the two estimates will diverge, and the analyst must investigate which assumption is correct.

## Common Pitfalls

**Confusing Cost of Equity with Expected Return**

A common mistake is to use the stock's historical return or analyst-consensus expected return as the cost of equity. These are forward-looking expectations, not risk-adjusted required returns. The cost of equity should reflect the risk of the stock, not the analyst's optimistic or pessimistic forecast.

**Not Updating for Changing Risk**

Beta and the risk-free rate change over time. A residual income model built in 2021 with a 1% risk-free rate is not valid for a 2024 valuation if rates have risen to 4%. The cost of equity must be recalibrated.

**Terminal Value Dominance**

In the residual income model, terminal value (the present value of perpetual residual income after the explicit forecast period) often exceeds 70% of total intrinsic value. This terminal value is highly sensitive to cost of equity. If the analyst is uncertain about long-term cost of equity, this uncertainty propagates directly into the final valuation.

## See also

<div class="wiki-seealso">

### Closely related

- [Residual income model](/residual-income-model/) — valuation framework in which cost of equity is the central discount rate
- [Capital Asset Pricing Model (CAPM)](/capital-asset-pricing-model/) — the standard method for estimating cost of equity
- [Beta](/beta/) — systematic risk measure; a key input to CAPM cost of equity estimation
- [Market risk premium](/market-risk-premium/) — the excess return expected from equity investments; drives cost of equity
- Required return on equity — another term for cost of equity; the minimum return shareholders demand

### Wider context

- Weighted average cost of capital (WACC) — broader discount rate that incorporates both debt and equity costs
- [Discounted cash flow (DCF)](/residual-income-vs-dcf-which-to-use/) — alternative valuation method that also uses cost of capital inputs
- [Intrinsic value](/intrinsic-value/) — the true economic worth of a firm; sensitive to cost of equity assumptions
- [Risk-free rate](/risk-free-rate/) — the starting point for cost of equity; typically the yield on long-term government bonds
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — the mandatory technique for understanding valuation risk when cost of equity is uncertain

</div>

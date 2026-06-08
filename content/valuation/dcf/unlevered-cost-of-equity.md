---
title: "Unlevered Cost of Equity"
description: "The cost of equity adjusted for the absence of financial leverage, used to discount asset-level cash flows independent of capital structure."
keywords:
  - unlevered cost of equity
  - asset beta
  - levered beta
  - wacc
  - dcf valuation
image: "/svg/valuation.svg"
---

*The **unlevered cost of equity** is the return required by equity investors in a firm with no [debt financing](/debt-financing/). It isolates the cost of equity from the effect of [financial leverage](/leverage-ratio-forex/), allowing analysts to value assets or compare companies with different capital structures on an apples-to-apples basis.*

## Why unlevered cost of equity matters

When a firm is financed purely by equity—no debt—the cost of equity reflects only business risk: the uncertainty inherent in the firm's operations. When the firm adds debt, equity becomes riskier (debt holders have priority in bankruptcy), so the cost of equity rises. The gap between these two costs is a pure leverage effect.

In valuation, this distinction is critical. Suppose you're comparing two otherwise identical firms: one financed entirely by equity, the other split 50-50 between debt and equity. Their [cost of equity](/cost-of-equity/) will differ, but their underlying business risk is the same. To compare them fairly, you need to strip away the leverage effect and work with unlevered cost of equity—the cost of capital that reflects only operational uncertainty.

Unlevered cost of equity is also essential when valuing a firm you plan to recapitalize. If you're buying a leveraged company and planning to reduce debt, the current [cost of equity](/cost-of-equity/) overstates the equity cost for your holding period. You need the unlevered version to forecast returns correctly.

## The relationship between levered and unlevered costs

A firm's equity cost rises with leverage because debt holders have first claim on cash flows. When times are good, equity still earns the full residual; when times are bad, equity absorbs the loss first. This asymmetry creates higher volatility for equity, hence higher required return.

The relationship is captured through **beta**, a measure of stock volatility relative to the market. A firm financed entirely by equity has an "unlevered beta" (also called asset beta) reflecting only business risk. When the firm adds debt, its equity beta rises—the stock becomes more volatile. This is levered beta.

The formula linking them is:

```
Levered β = Unlevered β × [1 + (1 − Tax Rate) × Debt/Equity]
```

Example: a firm with unlevered beta of 1.0, debt-to-equity ratio of 0.5, and 21% tax rate:

```
Levered β = 1.0 × [1 + (1 − 0.21) × 0.5]
         = 1.0 × [1 + 0.395]
         = 1.395
```

The levered beta is higher, reflecting the additional volatility from leverage. The tax rate appears because [interest](/coupon-payment/) is tax-deductible; the tax shield makes debt cheaper than it appears, moderating the leverage effect on beta.

## Moving from levered to unlevered cost of equity

If you know the levered beta and want the unlevered version, rearrange:

```
Unlevered β = Levered β / [1 + (1 − Tax Rate) × Debt/Equity]
```

Once you have unlevered beta, you can estimate unlevered cost of equity using the capital asset pricing model (CAPM):

```
Unlevered Re = Rf + Unlevered β × (Rm − Rf)
```

Where Rf is the risk-free rate and (Rm − Rf) is the market risk premium.

Real example: a firm with levered beta of 1.2, debt-to-equity of 0.4, and tax rate of 25%:

```
Unlevered β = 1.2 / [1 + (1 − 0.25) × 0.4]
            = 1.2 / [1 + 0.3]
            = 1.2 / 1.3
            = 0.923
```

If the risk-free rate is 3% and market risk premium is 6%:

```
Unlevered Re = 3% + 0.923 × 6% = 8.54%
```

## When to use unlevered cost of equity

Use unlevered cost of equity in these contexts:

**1. Valuing assets or divisions:** If you're valuing a subsidiary independently of the parent's capital structure, or assessing a standalone project, you need unlevered cost. The unlevered rate reflects the business risk of that asset alone, independent of how the overall firm is financed.

**2. Comparing firms with different leverage:** Company A has a 40% debt ratio; Company B has 10%. Their cost of equity will differ sharply even if their business risk is identical. To compare [return on equity](/return-on-equity/) or other equity metrics on a level playing field, strip out the leverage effect using unlevered cost.

**3. Scenario analysis:** If you're modeling what happens if a firm recapitalizes (reducing debt, increasing equity), the equity cost will change. Use unlevered cost as the stable input, then re-lever to match the new capital structure.

**4. Valuing distressed or highly leveraged firms:** A firm in financial distress may have a levered equity beta distorted by distress premia. Starting from an estimated unlevered beta (based on comparable firms with stable leverage) and re-levering to the distressed firm's capital structure gives a more grounded forecast.

## Common pitfalls

**Forgetting the tax adjustment:** The formula includes (1 − Tax Rate) because tax shields reduce the true cost of debt. Omitting it overstates the unlevering effect and produces incorrect results.

**Mixing market and book values:** Always use *market* values of debt and equity in the D/E ratio, not book values. A firm's balance sheet may show $100 million equity at historical cost, but if the stock trades at $200 million, that's the relevant number for leverage.

**Using the wrong comparable firm's beta:** Unlevering a peer's beta assumes similar business risk. If you compare a stable utility to a cyclical manufacturer, their betas will differ for good reasons; unlevering one and applying it to the other is misleading.

**Assuming leverage is permanent:** The formula assumes current capital structure persists. If you're modeling a leveraged buyout where debt is expected to decline rapidly, use a path of unlevered costs re-levered at each stage, not a static one.

## Unlevered cost of equity in [WACC](/wacc-calculation/)

The unlevered cost of equity is the starting point for calculating the [weighted average cost of capital](/wacc-calculation/). To build WACC for a firm with debt, you:

1. Estimate the unlevered cost of equity based on business risk alone
2. Leverage it to match the firm's target (or current) capital structure, producing levered cost of equity
3. Blend the levered cost with [cost of debt](/cost-of-debt/), adjusted for taxes

Conversely, if you know a firm's WACC and want its unlevered cost of equity, you can solve backwards by using [discounted cash flow valuation](/discounted-cash-flow-valuation/) with the firm's unlevered free cash flow—cash flows before debt service—discounted at WACC to find the enterprise value, then divide by the number of shares.

## See also

<div class="wiki-seealso">

### Closely related

- [Weighted average cost of capital](/wacc-calculation/) — the application combining unlevered cost with debt costs
- [Cost of equity](/cost-of-equity/) — the levered version, reflecting actual capital structure
- [Cost of debt](/cost-of-debt/) — the debt component of capital costs
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the primary use of both levered and unlevered costs

### Wider context

- [Beta](/beta/) — the volatility metric underlying cost of equity calculations
- [Debt financing](/debt-financing/) — how leverage affects equity cost
- [Return on equity](/return-on-equity/) — an equity metric affected by leverage
- [Debt-to-equity ratio](/debt-to-equity-ratio/) — the leverage measure linking levered and unlevered betas

</div>

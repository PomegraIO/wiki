---
title: "WACC for an Unlisted Firm"
description: "How to calculate WACC for a private company by proxying equity cost and capital structure using public comparables and beta adjustments."
keywords:
  - wacc calculation private firm
  - unlisted company cost of equity
  - de-levering re-levering beta
  - private company valuation discount rate
  - comparable company analysis unlisted
image: /svg/valuation.svg
---

*When a company has no publicly traded shares, the weighted average cost of capital must be assembled by inferring its cost of equity from public peers and adjusting for the unlisted firm's actual capital structure and risk profile.*

<div class="wiki-hatnote">

This article focuses on estimating WACC for private or unlisted firms. For listed companies, see [Cost of Equity](/cost-of-equity/). For context on debt cost, see [Cost of Debt](/cost-of-debt/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">WACC for Unlisted Firms — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Private company discount rates require beta estimation and capital structure iteration.</div>

|   |   |
|---|---|
| **Core approach** | De-lever comparable firms' betas; re-lever for target's capital structure and risk |
| **Equity cost source** | Public peer companies with similar operations and market risk |
| **Capital structure** | Use target's balance sheet or industry median leverage ratio |
| **Iteration step** | Solve iteratively if WACC feeds into valuation that changes implied debt ratios |
| **Key adjustment** | Size premium and lack-of-liquidity discount often applied to cost of equity |
| **Data requirement** | At least 3–5 comparable public firms with available beta and debt ratios |

</aside>

## Why Public Comparables Are Necessary

An unlisted firm leaves no observable equity price and thus no direct way to measure its equity risk premium or cost of equity. Instead, you source that premium from companies in the same industry—banks, retailers, pharma firms, whatever sector your target belongs to—that *do* trade publicly. The logic is simple: if two firms have similar operations and competitive positions, they should face similar business risk. The public firm's equity beta captures that risk in a form you can observe from its stock price and leverage ratio.

The challenge is that the public peer's beta reflects both the business risk of the industry *and* the financial leverage specific to that one firm. A retail company financed 30% with debt will have a higher equity beta than an identical retail company financed 10% with debt, purely because of the extra financial risk. To use the peer's insight about business risk, you must undo its leverage—"de-lever" the beta—and then reapply the target firm's own capital structure.

## De-Levering and Re-Levering Beta

The de-levering formula isolates business risk from financial risk. Given a comparable firm's equity beta (β*E*), debt-to-equity ratio (D/E), and tax rate (T):

β*U* = β*E* / [1 + (1 − T) × (D/E)]

This "unlevered beta" (β*U*) represents the risk of the business itself, stripped of leverage. If your comparable traded with zero debt, its equity beta would equal β*U*. 

Once you have the unlevered beta, re-lever it using your *target* firm's debt-to-equity ratio:

β*E* (target) = β*U* × [1 + (1 − T) × (D/E) (target)]

If your unlisted firm is projected to carry 40% debt and a 25% tax rate while the comparable had 30% debt and a 25% tax rate, the re-levering formula adjusts the beta upward to reflect that extra financial risk. The re-levered beta feeds into [CAPM](/capital-asset-pricing-model/) to give your target's cost of equity.

## Multiple Comparables and Industry Median Approach

A single comparable firm is rarely enough. Industry practices typically call for three to five public peers—preferably chosen to match your target on size, geography, product mix, and customer base. Once you de-lever each peer's beta, you commonly use the median (not mean) of the unlevered betas to smooth outliers. That median then gets re-levered using your target's capital structure.

Alternatively, if comparable companies carry very different leverage ratios, some analysts use the industry's *median* debt-to-equity ratio as the re-levering target, reasoning that it represents the capital structure a firm in that sector would naturally sustain. A young software company with no debt might use the median software-sector leverage ratio of, say, 20% to set expectations about what its equity investors would eventually tolerate.

## The Iterative Problem: WACC and Valuation Feedback

In practice, the target firm's capital structure is often not fixed in advance. Many unlisted companies are valued using a [discounted cash flow](/discounted-cash-flow-valuation/) model: future free cash flows are discounted using WACC, and the resulting enterprise value is split into debt and equity. But WACC itself depends on the debt-to-value ratio. If you assumed 40% debt in your WACC calculation but the DCF implies 50% debt, your discount rate was wrong.

The solution is iteration: start with a reasonable debt target (from peers or the firm's stated policy), calculate WACC, discount the cash flows, derive the implied debt ratio, then recalculate WACC if the ratio shifted materially. Most analysts stop after one or two iterations; the numbers converge quickly unless the firm's leverage ratio is extremely uncertain.

## Adjustments Specific to Unlisted Firms

Two common adjustments apply to unlisted companies that do not apply (or apply differently) to large public firms:

**Size Premium.** Smaller firms, especially those without large analyst coverage or liquid secondary markets, face a measurable return premium—typically 2–5 percentage points above what [CAPM](/capital-asset-pricing-model/) predicts—to compensate investors for illiquidity and concentration risk. This is added to the cost of equity after CAPM.

**Lack-of-Liquidity Discount.** When valuing an unlisted firm, the resulting equity value is often discounted 20–50% to reflect the fact that an investor cannot quickly sell shares on an exchange. This differs from adjusting the cost of equity; instead, it reduces the final valuation. Some methodologies blend this into the discount rate; others apply it separately as a post-valuation haircut.

## Choosing the Tax Rate

The tax rate *T* in the de-levering and re-levering formulas should be the firm's marginal tax rate—the rate at which an additional dollar of interest tax shield is realized. For a profitable unlisted firm, this is often the statutory corporate rate. For a loss-making firm with no current tax benefit from debt, use zero. If the target is in a low-tax jurisdiction while comparables are in high-tax jurisdictions, adjusting for the difference is crucial: a firm that saves no tax on debt interest should have a different β*E* than one that saves 35%.

## Sensitivity and Stress-Testing the WACC

Because WACC for an unlisted firm rests on borrowed estimates—unlevered betas from imperfect peers, guesses about capital structure, size premiums—it pays to run [sensitivity analysis](/sensitivity-analysis-valuation/). Increase the unlevered beta by 0.1, lower it by 0.1, and observe how the resulting valuation changes. Shift the target's leverage ratio by 10 percentage points. Test whether the choice of size premium materially affects your conclusion. If the valuation is highly sensitive to a single uncertain input, say so; do not present false confidence.

## See also

<div class="wiki-seealso">

### Closely related

- WACC — definition and components of weighted average cost of capital
- [Cost of Equity](/cost-of-equity/) — measuring equity risk premium and beta for listed firms
- [Cost of Debt](/cost-of-debt/) — after-tax cost of borrowing
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — the framework linking beta to cost of equity
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — applying WACC as the discount rate
- [Private Equity Fund](/private-equity-fund/) — how PE firms estimate hurdle rates for unlisted deals

### Wider context

- [Acquisition](/acquisition/) — integrating target firm WACC into deal analysis
- [Due Diligence](/due-diligence/) — assessing risk inputs for unlisted companies
- [Sensitivity Analysis Valuation](/sensitivity-analysis-valuation/) — stress-testing discount rate assumptions

</div>

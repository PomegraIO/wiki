---
title: "Estimating Cost of Equity for a Private Company"
description: "Explains how to estimate a discount rate for a private firm without public beta, using the build-up method and beta unlevering and relevering."
keywords:
  - cost of equity private company
  - private company discount rate estimation
  - build-up method beta
  - beta unlevering relevering
  - private company valuation discount rate
image: /svg/valuation.svg
---

*The **cost of equity for a private company** is the discount rate used to value its cash flows—but without a public market price, you cannot calculate beta the usual way. Instead, appraisers rely on the build-up method, finding comparables, and adjusting peers' betas for differences in financial leverage. The result is inherently more subjective than for public firms, yet the technique is the industry standard.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Private Company Cost of Equity — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Discount rates derived from comparable public firms and risk premiums.</div>

|   |   |
|---|---|
| **Main method** | Build-up: risk-free rate + equity risk premium + adjustments |
| **Alternative** | Find public comparables, unlever their beta, relever for target capital structure |
| **Risk-free rate** | Typically 10-year Treasury yield |
| **Equity risk premium** | Historical market return minus risk-free rate; typically 5–8% |
| **Adjustments** | Size premium; company-specific risk; illiquidity discount |
| **Range typical** | 10–20% for mature private businesses |

</aside>

## Why Public Beta Doesn't Work

For a public company, [cost of equity](/cost-of-equity-private-company/) is straightforward: regress historical stock returns against a market index to estimate [beta](/beta/), then apply the Capital Asset Pricing Model (CAPM):

Cost of Equity = Risk-Free Rate + Beta × Market Risk Premium

But a private company has no stock price, so there are no historical returns to regress. Beta must be estimated indirectly, either by finding comparable public companies and borrowing their betas, or by working backward from a build-up framework.

The core challenge is that comparable public firms rarely match the private target perfectly. A public competitor may be larger, more diversified, or more leveraged. The appraiser must adjust betas to account for these structural differences, a process that introduces judgment and uncertainty.

## The Build-Up Method

The **build-up method** constructs cost of equity as a stack of risk premiums:

Cost of Equity = Risk-Free Rate + Equity Risk Premium + Size Premium + Company-Specific Risk Premium

**Risk-free rate:** typically the yield on a 10-year U.S. Treasury bond, chosen to match the expected investment horizon. (Some practitioners use 20-year Treasuries for very long-duration businesses like utilities; short-horizon ventures might use a 2-year rate.)

**Equity risk premium:** the historical return of the stock market minus the risk-free rate. This "market risk premium" is a single number applied to all equity investments. Historical estimates range from 5% to 8% depending on the period and methodology used.

**Size premium:** small companies carry higher risk than large ones—they have less cash, fewer customers, and weaker credit access. Academic research, particularly the Fama-French studies, has quantified a size premium: small-cap stocks earn an extra 2–5% annually relative to large caps, adjusted for their beta. A private company, almost by definition smaller than its public comparables, deserves an upward adjustment.

**Company-specific risk:** unique risks not captured by size or market moves—customer concentration, key-person dependence, regulatory threat, technology obsolesce risk. This premium is subjective and typically ranges from 1% to 5%, depending on how concentrated the business model is.

A typical build-up for a private manufacturing company might look like:

| Component | Rate |
|-----------|------|
| Risk-free rate | 4.0% |
| Equity risk premium | 6.0% |
| Size premium | 2.5% |
| Company-specific premium | 1.5% |
| **Total cost of equity** | **14.0%** |

## Unlevering and Relevering: The Comparable Method

When an appraiser has identified a public comparable, the objective is to isolate its business risk (unlevered beta) and then relever it for the private company's target capital structure.

**Unlevering** removes the effect of the comparable's debt financing. A leveraged company has higher beta because debt magnifies returns—the equity holders absorb both business risk and financial risk. The unlever formula is:

Unlevered Beta = Levered Beta / [1 + (1 − Tax Rate) × (Debt / Equity)]

Example: a public software firm has levered beta of 1.2, debt-to-equity of 0.3, and tax rate of 21%.

Unlevered Beta = 1.2 / [1 + (1 − 0.21) × 0.3] = 1.2 / 1.237 ≈ 0.97

The resulting 0.97 unlevered beta reflects the business risk alone, stripped of the leverage effect.

**Relevering** then adjusts for the private company's expected capital structure. If the private target is expected to be financed with a debt-to-equity ratio of 0.5:

Relevered Beta = Unlevered Beta × [1 + (1 − Tax Rate) × (Debt / Equity)]

Relevered Beta = 0.97 × [1 + (1 − 0.21) × 0.5] = 0.97 × 1.395 ≈ 1.35

The private company's levered beta is now 1.35, reflecting its higher leverage. Plugging into CAPM:

Cost of Equity = 4% + 1.35 × 6% ≈ 12.1%

This approach assumes the private company will be financed as expected. If the deal includes unexpected leverage (due diligence finds a hidden debt facility), the relevered beta becomes out-of-date.

## Multiple Comparables and Triangulation

A robust valuation rarely relies on a single comparable. Instead, appraisers identify 3–10 peer companies—different sizes, geographies, or business models—unlever each, and average or median the unlevered betas. This averaging smooths out idiosyncratic noise in any one peer.

If the range is wide (say, unlevered betas from 0.7 to 1.3), it signals either genuine business-model differences or that the comparables are not truly comparable. The appraiser then decides: is the private company closer to the high-risk or low-risk peer profile?

## Adjustments for Size, Illiquidity, and Key Person Risk

Beyond the build-up or comparable method, practitioners often layer adjustments:

**Size discount:** empirical research (Ibbotson and Grabowski) shows smaller companies earn higher returns. A private company with $10 million revenue, compared to public comparables with $500 million+, may warrant an additional 2–5% premium.

**Illiquidity discount:** private equity is illiquid—an investor cannot sell shares tomorrow. This discount (sometimes 20–40% of the enterprise value) is technically a valuation deduction, not a cost-of-equity adjustment, but the two interact; a higher cost of equity produces a lower valuation and partially reflects illiquidity.

**Key-person risk:** if the business depends on one founder or technical expert, and that person is irreplaceable, the cost of equity rises to reflect execution risk. Conversely, a professional management team in place lowers this premium.

## Sensitivity and Defensibility

Cost-of-equity estimates for private companies should always be presented with a range, not a point. A 12% to 16% range for a mid-sized private manufacturer is more honest than "the cost of equity is exactly 14%." Courts and advisors reviewing the valuation will scrutinize the build-up inputs: is the size premium sourced from published research? Is the company-specific premium justified by documented risks?

The most defensible approaches combine the build-up method (for transparency and auditability) with the comparable unlever-relever method (for market-grounded beta). If both converge on a 13–15% range, confidence is high. If they diverge—one method yielding 10%, the other 18%—further digging is warranted.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — Foundational framework for cost of equity
- [Beta](/beta/) — Systematic risk measure; how to estimate it for comparables
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — Using cost of equity as the discount rate
- [Risk-weighted assets](/risk-weighted-assets/) — Related risk quantification for banks
- [Private equity fund](/private-equity-fund/) — Common acquirer using private company cost of equity
- [Leveraged buyout](/leveraged-buyout/) — Often involves cost of equity and debt cost optimization

### Wider context

- [Valuation](/fair-value/) — Broader appraisal framework
- [Return on equity](/return-on-equity/) — What a private company owner might expect given risk
- [Cost of debt](/cost-of-debt/) — Parallel discount rate for debt holders
- [Fair value](/fair-value/) — Conceptual standard for valuation exercises

</div>

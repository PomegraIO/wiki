---
title: "DCF Adjustments for Private Companies"
description: "DCF valuation adjustments for private company models: normalized owner compensation, size premium in discount rates, and bespoke risk metrics where market data doesn't exist."
keywords:
  - dcf valuation adjustments for private company
  - private company valuation
  - cost of equity
  - private company discount rate
  - owner compensation normalization
image: "/svg/valuation.svg"
---

*A **discounted-cash-flow** model for a private company requires three critical adjustments: normalizing founder or owner compensation, applying a size premium to reflect limited market liquidity, and deriving the discount rate without the benefit of public-market trading data.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DCF Adjustments for Private Companies — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Three layers of judgment reshape DCF for private firms.</div>

|   |   |
|---|---|
| **Problem 1: Owner pay** | Owner salary is often artificially low or high; must normalize to fair-market salary |
| **Problem 2: Liquidity gap** | No daily trading; apply 20–40% size/illiquidity discount to beta |
| **Problem 3: Leverage data** | No market cap; proxy comparable firms' capital structure or use owner's target |
| **Size premium** | Typically 3–5% added to cost of equity for small, illiquid firms |
| **Compensation normalization** | Adjust owner salary to median for the role; reallocate excess to owner profit |
| **Working capital** | More volatile for private firms; model conservatively or with stress scenarios |
| **Terminal value** | Often 60–80% of total valuation; use low growth rates (GDP or inflation) |

</aside>

## The Owner Compensation Problem

A private company founder often takes an artificially suppressed or inflated salary. The owner might pay themselves $50,000 per year while a market-rate CEO of equivalent responsibility earns $200,000. Alternatively, an owner-operator might extract excessive personal perks—country club fees, aircraft leases, consulting payments to family—that are effectively compensation, not business expenses.

In a DCF, you must normalize owner compensation. The goal is to estimate what the business would earn if a professional manager of equivalent capability ran it. You research the median salary for a CEO of a similar-sized firm in the same industry and geography. If the private company's owner is underpaid, you add the shortfall back to operating profit. If overpaid, you subtract it.

This step is critical because it isolates cash available to equity investors (after fair compensation to the operator) rather than conflating personal income with business performance. A business valued at $10 million with an owner earning $50,000 looks worse than the same business with an owner paid $200,000—yet the underlying operations may be identical.

## Deriving the Discount Rate Without Market Data

Public companies publish equity prices daily. Analysts calculate their [beta](/beta/) (price volatility vs. the market) from three years of trading history. For a private firm, there is no public trading history. You cannot directly measure beta.

Instead, you must:

1. **Find comparable public firms.** Identify 3–6 publicly traded companies in the same industry, of similar scale, with similar capital structure. Calculate their [equity-betas](/beta/).

2. **Unlever the comparable betas.** The published beta for a public firm reflects both business risk and financial leverage. You "unlever" it using the comparable's debt-to-equity ratio, isolating business risk. The formula is:

   Unlevered beta = Levered beta ÷ [1 + (1 − Tax rate) × (Debt ÷ Equity)]

3. **Re-lever for the private firm.** The private company will have its own [debt-to-equity-ratio](/debt-to-equity-ratio/), often dictated by its lenders or target capital structure. You re-lever the unlevered beta using that ratio.

4. **Add a size premium.** Private companies are smaller and far less liquid than public comparables. Research suggests a size premium of 3–5% is appropriate. This reflects both the cost of illiquidity and the higher risk of a smaller firm with fewer diversified revenue streams.

The result is the private company's cost of equity:

**Cost of Equity = Risk-free rate + (Levered beta × Market risk premium) + Size premium**

For example, if the risk-free rate is 4%, the levered beta is 1.2, the market risk premium is 6%, and the size premium is 4%, the cost of equity is 4% + 7.2% + 4% = 15.2%. This is substantially higher than a similarly levered public company might have (which would be 4% + 7.2% = 11.2%).

## Choosing Comparable Companies

The comparables step is judgmental. You might have only one or two firms in a narrow industry segment. If the private firm operates in a niche market (specialty chemicals, regional insurance), finding exact comparables is difficult. You may need to broaden the peer group or make explicit adjustments (e.g., "these comparables are 50% larger; add 1% to the size premium").

Some practitioners use multiples of comparables—[EV/EBITDA](/ebitda/) or [price-to-earnings-ratio](/price-to-earnings-ratio/)—rather than a DCF to value the private firm. This sidesteps the beta challenge but introduces reliance on market sentiment at a moment in time. A hybrid approach—DCF with a sanity check against comparable multiples—is common.

## Terminal Value and Growth Rate

In a public-company DCF, terminal value (the value at the end of the explicit forecast period, usually year 5 or 10) is often 50–70% of total valuation. For private companies, this fraction is often 60–80% because the forecast period is shorter and subject to more error.

For a private firm, using a long-term growth rate equal to nominal GDP growth (typically 2–3%) is conservative. A small business unlikely to become a regional powerhouse should not assume long-term growth above inflation plus modest real expansion. This contrasts with a high-growth tech company, where a 6–8% terminal-growth rate might be justified.

## Working Capital and Cash Conversion

Private companies often carry higher working-capital volatility. Cash collection is less predictable; inventory turnover can spike during seasonal shifts or cost pressures. In a DCF, you model working-capital as a percentage of sales and assume it varies with revenue growth.

For a mature, stable private business, you might assume working capital is 15% of sales. For a growing one with erratic cash conversion, 20–25% is safer. The amount of additional working capital tied up each year is a use of cash and reduces free cash-flow.

Additionally, private companies rarely have the luxury of negative working capital—where payables exceed receivables and inventory—that some large public firms achieve through scale. This adds conservatism to the valuation.

## Adjustments for Lack of Marketability

Beyond the size premium baked into the discount rate, some valuations apply a separate **lack-of-marketability discount (DLOM)** of 20–40% to the DCF result. This is particularly common in gift and estate tax contexts, where the discount reflects the reality that a private-company stake cannot be sold as quickly or at as high a price as a public stock.

In a financial advisory setting—when a buyer is actually negotiating a purchase—the DLOM is usually not applied separately, because the buyer's discount rate (cost of equity) already captures private-firm risk. However, in valuation for tax or litigation purposes, courts have upheld DLOM adjustments on top of the DCF.

## Leverage, Debt Capacity, and [Cost of Debt](/cost-of-debt/)

Private firms have different debt markets than public corporations. A private company may rely on bank loans, seller financing, or owner capital rather than public [corporate-bonds](/corporate-bond/). The [cost-of-debt](/cost-of-debt/) reflects this: small-firm bank loans might carry interest rates 2–4 percentage points higher than a comparable public firm's bond yield.

The [weighted-average-cost-of-capital](/weighted-average-cost-of-capital/) (WACC) used in the DCF blends the higher cost of equity and higher cost of debt, resulting in a discount rate that can be 6–10 points higher than a public peer.

## Sensitivity Analysis

Given the number of assumptions—beta, size premium, terminal growth rate, working capital, owner compensation—a private-company DCF should include aggressive [sensitivity-analysis](/sensitivity-analysis-valuation/). Show how valuation changes if the cost of equity is 1–2 points higher, if terminal growth is 1% lower, or if owner compensation is 10% different.

A good practice is to present a base case, an upside case (lower discount rate, higher growth), and a downside case (higher discount rate, lower growth). The range often spans 40–60% of the base valuation, reflecting the uncertainty inherent in private-firm modeling.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — foundational DCF methodology
- [Cost of equity](/cost-of-equity/) — the discount rate's equity component
- [Cost of debt](/cost-of-debt/) — interest rates on private-firm debt
- [Beta](/beta/) — market-based risk measure; proxied for private firms via comparables
- Capital structure — debt-to-equity mix that affects discount rates
- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — combines cost of equity and debt
- [Terminal value](/terminal-value/) — the largest component in private-firm valuations
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — critical for models with many assumptions

### Wider context

- [Relative valuation](/relative-valuation/) — using multiples as an alternative or sanity check
- [Private equity fund](/private-equity-fund/) — investors who apply these methods to acquire firms
- [Leveraged buyout](/leveraged-buyout/) — acquisition structure that shapes private-firm DCF inputs
- [Business combination (purchase accounting)](/business-combination-purchase/) — post-acquisition accounting implications
- [Going concern](/going-concern/) — assumption underlying any private-firm valuation

</div>

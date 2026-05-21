---
title: "Fama-French Five-Factor Model"
description: "An extension of the Fama-French three-factor model that adds profitability and investment factors, further refining cost of equity estimates."
keywords:
  - Fama-French five-factor
  - profitability factor
  - investment factor
  - cost of equity
  - multi-factor model
image: "https://picsum.photos/seed/fama-french-five-factor-model/900/600"
---

*The **Fama-French five-factor model** extends the [three-factor model](/fama-french-three-factor-model) by adding two new factors: profitability and investment. It says that cost of equity depends on market risk, size, value characteristics, *how profitable a company is*, and *how much it is reinvesting*. Highly profitable, low-reinvestment companies earn less than the model would predict; low-profitability, high-reinvestment companies earn more. It is the latest iteration of multi-factor models in academic finance.*

## The five factors

**Market factor.** Beta. Market risk.

**Size factor.** Small-cap premium.

**Value factor.** Value premium (cheap stocks).

**Profitability factor.** Profitable companies (high ROA, high gross profit margins) have lower expected returns than unprofitable ones after controlling for other factors.

**Investment factor.** Companies that are investing heavily in capital and R&D (high capex-to-assets) have higher expected returns than companies that are not reinvesting.

## Why profitability and investment matter

**Profitability.** Highly profitable companies have lower expected returns because they are lower-risk. If a company earns 20% on its assets, that is a lower-risk investment than one earning 5%. Investors should demand lower returns for the profitable firm.

**Investment rate.** Companies reinvesting heavily might be riskier (growth-stage risk) or might have lower profitability on new investments. Empirically, high-investment companies earn higher returns (perhaps because they are riskier or because markets systematically misprice them).

Together, these factors explain additional variation in returns that size and value alone do not capture.

## The formula

Cost of equity = Risk-free rate + (Beta × Market risk premium) + (Size loading × Size premium) + (Value loading × Value premium) + (Profitability loading × Profitability premium) + (Investment loading × Investment premium)

## Advantages

**More complete.** The five-factor model explains more of the cross-sectional variation in stock returns than the three-factor model.

**Captures fundamental performance.** Profitability is a direct measure of how well a company is doing; investing rate reflects growth ambitions. These are fundamental characteristics, not just cheap/small traits.

**Stable premiums.** Academic research shows that profitability and investment premiums are stable and significant across time periods and markets.

## Challenges

**Complex to calculate.** Estimating five factor loadings and five premiums requires more data and computation than CAPM or even Fama-French three-factor.

**Less widely available.** Bloomberg, Yahoo Finance, and most financial databases provide CAPM beta and sometimes Fama-French three-factor loadings, but five-factor loadings are less commonly available.

**Small magnitude.** While statistically significant, the economic magnitude of the profitability and investment premiums is modest (1–3% annually). In a practical valuation, they might move cost of equity by 0.5–1.5 percentage points.

**Perpetuity problem.** Like other factors, using investment and profitability premiums in a perpetual DCF is questionable. These factors might be short-term. Over 20+ years, investment rates and profitability should converge.

## When five-factor is useful

**Academic or rigorous institutional work.** If you are building a multi-year research model or a portfolio risk model, five-factor is state-of-the-art.

**Comparing very different companies.** If comparing a high-profitability tech giant to a low-profitability biotech, the profitability factor captures a real difference in risk and expected return.

**Sector analysis.** Different sectors have different average profitability and investment rates. Five-factor models can help control for these structural differences.

## When to stick with three-factor or CAPM

**Time constraints.** CAPM is faster. If you are doing a quick valuation, spending hours to refine cost of equity by 0.5% is not worth it.

**Client expectations.** Most CFOs and boards understand CAPM and Fama-French. Five-factor might be seen as over-complicating.

**Diminishing returns.** Going from CAPM to Fama-French improves cost-of-equity estimates. Going from three-factor to five-factor improves further, but the gain is smaller.

## Hybrid approach

Some practitioners use Fama-French three-factor for the main valuation, then check cost of equity using five-factor. If five-factor yields materially different results (say, 20%+ difference), investigate why and consider using the five-factor estimate.

## See also

<div class="wiki-seealso">

### Closely related

- [Fama-French three-factor model](/fama-french-three-factor-model) — the base model
- [Capital asset pricing model](/capital-asset-pricing-model) — the original framework
- [Carhart four-factor model](/carhart-four-factor-model) — alternative extension
- [Cost of equity](/cost-of-equity) — what this estimates

### Factor concepts

- Profitability — the profitability factor
- Investment — the investment factor
- [Beta](/beta) — market risk
- Size — size premium

### Valuation application

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses cost of equity
- [Weighted average cost of capital](/weighted-average-cost-of-capital) — incorporates cost of equity

### Alternatives

- [Arbitrage pricing theory](/arbitrage-pricing-theory) — alternative multi-factor framework
- [Build-up method cost of equity](/build-up-method-cost-of-equity) — additive approach

</div>

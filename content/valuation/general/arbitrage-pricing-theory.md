---
title: "Arbitrage Pricing Theory"
description: "A multi-factor model for estimating cost of equity that allows for multiple risk factors beyond market beta, providing flexibility in modeling different sources of systematic risk."
keywords:
  - arbitrage pricing theory
  - APT
  - multi-factor model
  - cost of equity
  - systematic risk
image: "/svg/valuation.svg"
---

*The **Arbitrage Pricing Theory (APT)** is a multi-factor framework for estimating cost of equity, developed by Stephen Ross as an alternative to the single-factor [CAPM](/capital-asset-pricing-model/). Rather than assuming cost of equity depends only on market beta, APT says it depends on multiple systematic risk factors: interest rate risk, inflation risk, industry risk, etc. The theory is elegant, but in practice, identifying and measuring the factors is subjective.*

## The concept

**CAPM** assumes one risk factor (market risk) explains returns.

**APT** assumes *multiple* risk factors explain returns. The cost of equity equals the risk-free rate plus the sum of factor-based risk premiums.

Cost of equity = Risk-free rate + (Factor 1 loading × Factor 1 premium) + (Factor 2 loading × Factor 2 premium) + ... + (Factor n loading × Factor n premium)

Unlike CAPM, APT does not specify *which* factors matter; it merely says multiple factors should be considered.

## Potential factors

Different factors might explain equity returns:

**Macroeconomic factors:**
- Unexpected inflation
- Unexpected changes in interest rates
- Unexpected changes in economic growth
- Unexpected changes in oil prices

**Market factors:**
- Market risk premium (equivalent to CAPM beta)
- Size premium
- Value premium

**Firm-specific factors:**
- Earnings surprises
- Analyst forecast revisions
- Momentum

## Building an APT model

1. **Identify relevant factors.** Which risks affect the company? If it is a bank, interest-rate risk is critical. If it is a consumer staple, economic-growth risk might be secondary.

2. **Estimate factor loadings.** How sensitive is the stock to each factor? Run regressions of historical returns against factor returns.

3. **Estimate factor premiums.** What is the expected excess return for each factor?

4. **Sum.** Add all factor contributions to get total cost of equity.

## Advantages of APT

**Flexibility.** You are not locked into CAPM's single beta. You can include factors that are relevant to the company.

**Theoretical soundness.** APT is built on arbitrage principles: if two portfolios have the same risk exposures, they should have the same expected return. The theory is elegant.

**Can be empirically richer.** Multi-factor models (like Fama-French) naturally fit within APT's framework.

## Challenges in practice

**How many factors?** One factor (CAPM) is too few. But 10 factors might be too many. The choice is arbitrary.

**Which factors?** APT doesn't say. You must choose. Different analysts choose differently, yielding different cost-of-equity estimates.

**Measuring factor premiums.** While CAPM's market risk premium can be estimated from historical equity returns, premiums for other factors are harder to pin down. What is the expected premium for "unexpected inflation"?

**Data limitations.** For some factors, long-term historical data is unavailable. For a new risk (e.g., climate change), there is no history.

**Overfitting.** If you fit factor loadings using historical data, you might find spurious factors that don't persist.

## APT vs. Fama-French

**Fama-French** is essentially a practical implementation of APT. It identifies specific factors (market, size, value, profitability, investment) that empirically explain returns.

**APT** is the theoretical framework; Fama-French is an applied model.

In practice, practitioners use Fama-French (or variations) rather than building a custom APT model, because Fama-French's factors are well-researched and stable.

## When APT is useful

**Specialized industries.** If your company is in a niche industry (e.g., gold mining, telecom infrastructure), standard factors might miss key risks. A custom APT model with commodity-price or regulatory factors might be more appropriate.

**Multi-national companies.** A company with major exposure to multiple countries faces currency risk, country-specific risk, etc. A multi-factor APT model can model these.

**Hedging applications.** Portfolio managers use APT-like models to understand and manage their exposures to various risk factors.

## Practical adoption

**In industry.** Most practitioners use CAPM, Fama-French three-factor, or build-up methods. Pure APT is less common.

**In academia.** APT is widely taught and used in research. It is the theoretical foundation for understanding multi-factor models.

**In practice for valuations.** When analysts use multiple factors, they are implicitly using an APT-like framework, even if they don't call it APT.

## Building a practical APT for a valuation

Rather than deriving factors from economic first principles, a practical approach is:

1. Start with Fama-French three-factor (market, size, value).
2. Add factors specific to your company (e.g., oil prices if energy-exposed, interest rates if a bank, regulatory risk if regulated).
3. Estimate or assume premiums for these additional factors.
4. Calculate cost of equity.

This is more practical than pure APT while capturing industry-specific risks.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital asset pricing model](/capital-asset-pricing-model/) — single-factor precursor
- [Fama-French three-factor model](/fama-french-three-factor-model/) — practical multi-factor model
- [Fama-French five-factor model](/fama-french-five-factor-model/) — further extension
- [Cost of equity](/cost-of-equity/) — what APT estimates

### Factor concepts

- [Beta](/beta/) — market risk factor
- [Systematic risk](/systematic-risk/) — what factors capture
- Risk premium — factor return premiums

### Practical application

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — uses cost of equity
- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — incorporates cost of equity
- [Build-up method cost of equity](/build-up-method-cost-of-equity/) — additive APT-like approach

</div>

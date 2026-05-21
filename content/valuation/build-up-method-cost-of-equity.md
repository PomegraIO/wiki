---
title: "Build-Up Method (Cost of Equity)"
description: "An additive approach to estimating cost of equity by explicitly adding risk premiums—market risk premium, size premium, company-specific premium—rather than using regression-based beta."
keywords:
  - build-up method
  - cost of equity
  - risk premium
  - additive method
  - valuation
image: "https://picsum.photos/seed/build-up-method-cost-of-equity/900/600"
---

*The **build-up method** (or "build-up approach") for estimating cost of equity is additive and transparent. Rather than using regression to estimate a single beta (as in CAPM), you explicitly identify risk premiums and add them: start with the risk-free rate, add an [equity risk premium](/equity-risk-premium), add a size premium for small companies, add a company-specific premium for unique risks. The result is a cost of equity grounded in logic rather than backward-looking regression.*

## The formula

Cost of equity = Risk-free rate + Market risk premium + Size premium + Company-specific premium

Or more generally:

Cost of equity = Risk-free rate + (Premium 1) + (Premium 2) + (Premium 3) + ...

## Components

**Risk-free rate.** The yield on a government bond. Typically a 10-year Treasury for long-term valuations. 3–5% in normal times.

**Market (equity) risk premium.** The excess return investors demand for holding equities instead of risk-free bonds. 5–7% based on historical data, or lower if forward-looking estimates are used. This is essentially CAPM's market risk premium, added directly rather than multiplied by beta.

**Size premium.** Small companies are riskier and earn higher returns. A company with market cap below 100 million might earn 2–4% extra annually. A company with market cap over 1 billion might earn 0–1% extra.

**Company-specific premium.** Risks unique to the company not captured by size or market factors:
- Key-person risk (one executive is crucial)
- Customer concentration (a few large customers)
- Product concentration (one product is 80% of revenue)
- Competitive threats
- Technology or regulatory risks

The premium might be 1–5%, depending on the risk.

## Example

A small, regional software company:

Risk-free rate: 4%
Market risk premium: 6%
Size premium (market cap 50 million): 3%
Company-specific premium (dependent on one key product): 2%
**Total cost of equity: 4% + 6% + 3% + 2% = 15%**

Compare to CAPM: if the company's beta is 1.4, cost of equity = 4% + 1.4×6% = 12.4%.

The build-up method (15%) yields a higher cost of equity, reflecting the specific risks better.

## Advantages

**Transparency.** Each risk is explicit. You can see exactly why cost of equity is 15% (market risk, size, company risk). With CAPM beta, the calculation is abstract.

**Flexibility.** You can add premiums for specific risks. A mining company might add commodity-price risk. A bank might add interest-rate risk.

**Avoids regression noise.** CAPM betas, estimated via regression, are noisy and change over time. Build-up is more stable because it is conceptual, not backward-looking.

**Better for private companies.** For private firms without traded securities, running a regression to get beta is impossible. Build-up works: estimate size (compare to public companies of similar size) and add premiums.

## Disadvantages

**Subjectivity in premiums.** What is the appropriate size premium for a 50 million-dollar company? 3% or 4%? What is the company-specific premium? 1% or 3%? Different analysts get different answers.

**Risk of double-counting.** If you add a company-specific premium for "customer concentration," are you also implicitly adding that risk in the market risk premium? Care is needed to avoid overlap.

**Lack of market discipline.** CAPM beta comes from the market (observed from stock returns). Build-up premiums are your estimates. The market doesn't constrain them.

**Less widely accepted.** Most investment banks and analysts use CAPM or Fama-French. Build-up is less standard, so presenting it requires more justification.

## Practical build-up framework

**For any company:**
- Start with risk-free rate (10-year Treasury).
- Add market risk premium (5–7%, based on historical or forward-looking data).

**For small companies (under 500 million market cap):**
- Add size premium (1–4% depending on size).

**For any company with elevated risk:**
- Add company-specific premium (0–5% depending on risks):
  - Key-person risk: +0.5–1.5%
  - Customer concentration (top 3 customers > 50% of revenue): +0.5–1.5%
  - Product concentration: +0.5–1%
  - Emerging market or high-regulatory risk: +1–3%
  - Technology or disruption risk: +0.5–2%
  - Leverage risk (highly leveraged): +0.5–2%

**For mature, stable, low-risk companies:**
- Use risk-free + market premium only, perhaps no size premium or minimal.

## Reconciling build-up with CAPM

A build-up of 15% can be reconciled with CAPM by backing out an implied beta:

15% = 4% + Beta × 6%
Beta = (15% - 4%) / 6% = 1.83

So the build-up method, applied to a company with risk-free 4% and market risk premium 6%, is equivalent to assuming beta of 1.83. Is that reasonable for the company? If the company is highly volatile, 1.83 might be right. If not, the build-up might be too high.

This cross-check is useful: if build-up and CAPM yield very different results, investigate why.

## When build-up is most useful

**Private company valuation.** No market beta available; build-up is natural.

**Early-stage or risky companies.** Company-specific premiums capture concentrated risks better than a single beta.

**Small-cap or specialized companies.** Standard beta estimates are unreliable; build-up is more defensible.

**Non-profit or valuation for internal purposes.** When transparency and logic matter more than market convention.

## When CAPM or Fama-French is better

**Large, publicly traded companies.** Market betas are reliable; standard models are accepted.

**When you need market discipline.** If you are valuing for investors, using market-based betas is more credible than subjective premiums.

**Speed and simplicity.** CAPM is faster than estimating multiple premiums.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost of equity](/cost-of-equity) — what this estimates
- [Capital asset pricing model](/capital-asset-pricing-model) — the alternative approach
- Risk premium — the components
- [Equity risk premium](/equity-risk-premium) — a key component

### Valuation application

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses cost of equity
- [Weighted average cost of capital](/weighted-average-cost-of-capital) — incorporates cost of equity

### Risk factors

- [Market risk premium](/market-risk-premium) — the primary component
- [Beta](/beta) — alternative to build-up
- [Systematic risk](/systematic-risk) — what premiums reflect

</div>

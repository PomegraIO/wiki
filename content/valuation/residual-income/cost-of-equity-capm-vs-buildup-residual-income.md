---
title: "CAPM vs Build-Up Method for Cost of Equity in Residual Income Models"
description: "CAPM and build-up method set required return differently in residual income models. Choose based on data quality, company stage, and market transparency."
keywords:
  - capm vs build-up method cost of equity
  - residual income valuation models
  - required return on equity
  - capital asset pricing model
  - build-up method valuation
image: "/svg/valuation.svg"
---

*Two distinct frameworks determine the **cost of equity** (required return) in [residual income models](/residual-income-model/): the [Capital Asset Pricing Model](/capital-asset-pricing-model/) (CAPM) and the build-up method. CAPM derives required return from market risk (beta), while build-up stacks premiums for each risk component. The choice reshapes the residual income spread—the engine of valuation—and can swing intrinsic value by 20% or more.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Equity Methods — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">How you measure required return determines which companies appear undervalued under residual income logic.</div>

|   |   |
|---|---|
| **CAPM formula** | Risk-free rate + Beta × (Market risk premium) |
| **Build-up formula** | Risk-free rate + Equity risk premium + Size premium + (Company-specific premium) |
| **CAPM strength** | Market-observable beta; simpler application |
| **Build-up strength** | Transparent component stacking; suits private/illiquid firms |
| **Impact on residual income** | Higher cost of equity lowers the spread; lower cost raises spread |
| **Data quality risk** | CAPM: beta stability; Build-up: subjective adjustment factors |
| **Typical range difference** | 1–3% between methods on same company |

</aside>

## The residual income spread: why cost of equity matters

A [residual income model](/residual-income-model/) values a stock as the sum of book value plus the present value of future "residual income"—the excess of net income over the cost of equity times opening book value. Residual income is profit above the required return. The higher the cost of equity you assume, the *lower* the residual income spread becomes, and the *lower* intrinsic value falls. Conversely, a lower cost of equity widens the spread and inflates value.

This leverage is why choosing between CAPM and build-up matters. A company with $100 million in book value and $12 million in annual net income faces a spread of $2 million using a 10% cost of equity ($100M × 10% = $10M required return), but only $1 million using an 11% cost of equity. Over a 10-year horizon at 10% discount, that $1 million difference in annual spread compounds into a 10–15% swing in total equity value. Methodology choice, not just the inputs, reshapes the conclusion.

## CAPM: market-relative risk pricing

CAPM prices risk against the market portfolio. It holds that an investor's required return depends on one factor alone: how much a stock moves relative to the broad market (beta). A beta of 1.0 means move-in-lock-step; 1.5 means 50% more volatile; 0.7 means 30% less volatile than the market. The CAPM formula is:

**Required return = Risk-free rate + Beta × (Market risk premium)**

If the risk-free rate is 3%, beta is 1.2, and the market risk premium is 6%, required return = 3% + 1.2 × 6% = 10.2%.

CAPM's beauty is objectivity: beta is observable from historical price data (typically over 2–5 years). The market risk premium, though debated, is a single, widely-accepted estimate (commonly 5–7%). For liquid, publicly-traded companies, this method is quick and defensible.

But CAPM has a critical flaw for residual income valuation: it assumes beta is stable and that market-relative volatility is the *only* risk that matters. A company trading on a small exchange with thin liquidity faces real risks—execution, sourcing, customer concentration—that do not show up as beta. A private firm has even less beta data and faces idiosyncratic risks the public markets have priced out. CAPM shoehorns those firms into an incomplete framework.

Moreover, beta estimates drift. If a company's business model shifts, or if historical price moves are not representative of forward volatility, the CAPM cost of equity can be stale or misleading. A software company pivoting from license sales to recurring subscriptions may have historical beta that overstates market-relative risk going forward.

## Build-up method: component stacking

The build-up method abandons the single beta factor and instead layers premiums for each distinct risk:

**Required return = Risk-free rate + Equity risk premium + Size premium + Company-specific premium**

Start with the risk-free rate (same as CAPM). Add an equity risk premium (the long-run excess return of stocks over bonds, typically 4–6%). Then, if the company is small, add a size premium (1–4%, reflecting the illiquidity and volatility of small-cap stocks). Finally, add a company-specific premium (0–5%) for risks unique to the firm: concentration, competitive position, management depth, product mix.

A small industrial supplier with concentrated customer base might warrant: 3% (risk-free) + 5% (equity premium) + 2% (size) + 2% (company-specific) = 12%. By contrast, a mega-cap tech platform might be 3% + 5% + 0% (no size premium) + 0.5% (minimal company-specific) = 8.5%.

The transparency is the build-up method's advantage. You can see and debate each component. If you believe a company's competitive moat is stronger than the market credits, you lower the company-specific premium. If new management is unproven, you raise it. The method adapts to information you possess.

But build-up is subjective. What is the right size premium for a $2 billion market-cap company? Is it 1%, 2%, or 3%? Consensus is weak. And the "company-specific" premium is the wildcard—it can become a catch-all bucket where analysts hide doubts or hopes. Two analysts can reasonably disagree on the company-specific premium by 2–3%, leading to very different residual income spreads.

## When CAPM is the right choice

Use CAPM when:

- The company is large and heavily traded, so beta estimates are stable and meaningful.
- Your audience (analysts, institutional investors) expects CAPM outputs; consensus estimates of [cost of equity](/cost-of-equity/) are often CAPM-based.
- You want simplicity and speed, particularly for initial screening.
- The company's risk profile is largely market-relative (e.g., a cyclical manufacturing firm whose fortunes track GDP and commodity prices).

CAPM is also the default for mergers and acquisitions, leveraged buyouts, and other deal contexts where M&A practitioners have internalized the CAPM standard. If you're valuing a target for a private equity buyer, the deal team likely expects a CAPM-derived [discount rate](/discount-rate/) (cost of equity).

## When build-up is the right choice

Use build-up when:

- The company is private, pre-revenue, or early-stage, so public-market beta is either unavailable or misleading.
- The company faces distinct idiosyncratic risks: concentration, key-person dependency, new market entry, regulatory pending clarity.
- You need to defend each risk component explicitly—useful in family offices, venture capital, or internal corporate valuation.
- Size is material; small cap stocks truly do carry documented long-run excess returns (the "size effect"), and build-up acknowledges this explicitly while CAPM often ignores it.

Build-up is also more intuitive for non-finance audiences. Saying "required return is risk-free rate plus a 5% equity premium plus a 2% company-specific risk" is more accessible than "beta of 1.3 times a 6% market premium."

## Comparing outputs and choosing between them

On a large-cap, liquid public company, the two methods will often yield similar results (within 0.5–1.5%). On small-cap or private firms, the divergence widens. A small company might generate a CAPM cost of equity of 10% (if historical beta is 1.0 and market premium is 7%), but a build-up calculation of 12% (3% risk-free + 5% equity premium + 2% size + 2% company-specific). That 2% gap compounds into real valuation differences.

A practical approach: calculate both. If they converge, you have confidence. If they diverge sharply, investigate why. Is the company's historical beta outdated or non-representative? Does the company-specific risk premium in build-up deserve to be 3% or only 1%? Sensitivity analysis—showing how residual income value changes across a range of cost-of-equity assumptions (say, 8% to 12%)—is more honest than picking one method and pretending it is gospel.

## Sector and stage variations

Early-stage venture and growth companies almost always use build-up, because CAPM beta from short trading histories is unreliable. Private equity firms apply build-up for acquisitions of family-owned or middle-market businesses. Public-company equity research teams typically default to CAPM, since consensus beta data and market-risk-premium estimates are freely available.

For a mature industrial company with 50 years of trading history, CAPM beta is robust and CAPM is the natural choice. For a biotech firm post-IPO but pre-approval of a key drug, idiosyncratic risk is enormous; build-up better captures the company-specific hazard.

## See also

<div class="wiki-seealso">

### Closely related

- [Residual Income Model](/residual-income-model/) — valuation framework where cost of equity is the critical input
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — detailed CAPM mechanics and beta estimation
- [Cost of Equity](/cost-of-equity/) — the required return on equity capital across frameworks
- [Discount Rate](/discount-rate/) — how cost of equity is applied to future cash flows
- [Beta](/beta/) — market-relative risk and its stability over time

### Wider context

- Equity Valuation — the full framework for pricing stocks
- [Private Equity Valuation](/private-equity-fund/) — how PE firms value acquisitions
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing how valuation changes across assumptions
- [Market Risk Premium](/market-risk-premium/) — the long-run excess return of equities over bonds

</div>

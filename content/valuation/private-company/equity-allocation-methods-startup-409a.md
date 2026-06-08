---
title: "Equity Allocation Methods in a 409A Valuation"
description: "How startup 409A valuations price common stock using the Current Value Method, PWERM, and Option Pricing Model — and when the IRS prefers each."
keywords:
  - equity allocation methods 409a valuation
  - 409a valuation common stock pricing
  - current value method preferred stock
  - option pricing model startup equity
  - probability-weighted expected return method
image: /svg/valuation.svg
---

*A **409A valuation** determines the fair market value of private company equity for tax purposes, and different **equity allocation methods** — the Current Value Method, Probability-Weighted Expected Return Method, and Option Pricing Model — govern how common stock is priced relative to preferred stock. The choice hinges on a startup's stage, exit likelihood, and the eyes watching: auditors and the IRS favor the method most defensible under the facts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">409A Equity Allocation — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">How startups price common stock when preferred stock also exists.</div>

|   |   |
|---|---|
| **Primary purpose** | Tax-compliant fair market value (FMV) for option strike prices, tax reporting |
| **Three main methods** | Current Value (waterfall), PWERM (probability trees), Option Pricing Model (Black-Scholes variant) |
| **Current Value Method** | Assumes immediate liquidation; common stock = residual after preferred |
| **PWERM** | Weights multiple exit scenarios; most common in early-stage startups |
| **Option Pricing** | Treats common as call option on firm value; used when exit probability is high |
| **Who enforces** | IRS (section 409A), audit firms, option plan administrators |
| **Failure cost** | Excess tax liability, plan disqualification, exercise-price penalties |

</aside>

## What 409A Valuation Exists To Do

A 409A valuation assigns a defensible fair market value (FMV) to a private company's equity. The IRS requires it to set the strike price of startup stock options: if the strike is too low, the spread at grant becomes taxable income immediately, triggering the 20% penalty under Section 409A(a)(1)(B). The valuation also feeds into employee financial statements, tax basis calculations, and audit sign-offs.

Because most startups have multiple share classes — preferred shares owned by investors and common shares owned by employees and founders — the valuation must split the total company value between them. That split is the equity allocation. A preferred shareholder's claim is senior (they get paid first in a liquidation or exit), so common shares receive only what remains. The allocation method determines how much "what remains" is worth.

## The Current Value Method: Waterfall Liquidation

The **Current Value Method** (also called the asset method or liquidation method) assumes the company liquidates immediately at its current estimated value. Each class of equity claims assets in order of seniority.

**How it works:**
1. Estimate the total fair market value of the company.
2. Allocate cash and proceeds to preferred shares first, honoring their liquidation preference.
3. Assign anything left to common shares.

**Example:** A Series A startup is valued at $50 million. Its preferred shares have a 1x non-participating liquidation preference ($30 million invested, no multiple). Under the Current Value Method:

| Class | Preference | Allocation |
|-------|-----------|-----------|
| Preferred | 1x non-participating | $30M |
| Common | Residual | $20M |

The common shareholders' total stake is $20M. If 1 million common shares are outstanding, the FMV per share is $20.

**Strengths and use cases:**
- Simple to calculate and defend.
- Appropriate when exit is imminent or company is distressed.
- Matches the cash-flow order agreed in the certificate of incorporation.

**Weaknesses:**
- Ignores upside scenarios; assumes no growth or successful exit.
- Often severely undervalues common stock in healthy, growing startups.
- Can trigger fierce objections from employees whose options appear nearly worthless.

The Current Value Method is most credible for companies near an exit or in financial trouble. For a thriving Series B startup years away from liquidity, regulators and auditors view it skeptically.

## The Probability-Weighted Expected Return Method (PWERM)

The **Probability-Weighted Expected Return Method (PWERM)** models multiple exit scenarios — successful growth, moderate return, acquisition, failure — and assigns a probability to each. The method then calculates expected value across all scenarios.

**How it works:**
1. Identify plausible future states (e.g., unicorn exit at $2B, acquisition at $300M, failure).
2. Assign a probability to each scenario.
3. For each scenario, use the Current Value Method to allocate between preferred and common.
4. Weight each scenario's common-stock value by its probability.
5. Average to get the expected FMV per common share.

**Example:** An early-stage startup is valued at $20M today. The valuation consultant models:

- **60% chance:** Series B success, company reaches $150M in 4 years → common share worth $X.
- **25% chance:** Acquisition at $80M in 3 years → common share worth $Y.
- **15% chance:** Failure or down-round → common share worth $0.

Using the Current Value Method in each scenario (adjusted for each new valuation), the consultant calculates X and Y, then blends:

Expected FMV = (0.60 × X) + (0.25 × Y) + (0.15 × $0) = **common share value**.

**Strengths and use cases:**
- Reflects realistic exit pathways; most common in early- to mid-stage startups.
- Auditors and the IRS accept it if scenarios are reasonable and probabilities credible.
- Avoids treating a healthy startup's common stock as worthless.

**Weaknesses:**
- Requires judgment; different consultants can build different trees.
- Sensitive to probability and exit-value assumptions.
- More complex to document and defend than Current Value.

PWERM is the default for startups that are solvent, showing growth, but not yet near an exit. It is the method most frequently used in practice.

## The Option Pricing Model: Common as a Call Option

The **Option Pricing Model** treats common shares as a call option on the company's value. The strike price is the value needed to pay off all preferred investors in full. Any company value above that strike belongs to common shareholders.

**How it works:**
1. Model the distribution of future company values (typically using Black-Scholes or a binomial tree).
2. Set the strike price = total amount invested in preferred shares (or the amount owed per the liquidation preference).
3. Solve for the option value of common shares.

**Example:** A company has $40M in total preferred liabilities and is modeled to be worth $100M–$500M in 5 years. The common shareholders own a call option with a $40M strike. If the company is worth $100M, common gets $60M. If $200M, common gets $160M. The option method values this call across the entire distribution of future outcomes.

**Strengths and use cases:**
- Natural fit when the company is very likely to exit at a substantial multiple.
- Produces higher common-stock valuations in high-growth, late-stage companies.
- Theoretically elegant; mirrors how venture capital returns actually accrue.

**Weaknesses:**
- Requires volatility assumptions that can be hard to justify.
- Often produces common values higher than PWERM, raising auditor pushback.
- Best suited to late-stage, low-failure-risk companies; less appropriate for seed or Series A.

The Option Pricing Model gained traction in the late 2010s as late-stage private valuations soared, but it remains controversial in audit settings.

## Regulatory Preferences and Audit Scrutiny

The IRS does not mandate a single method. Treasury Regulation Section 1.409A-1(b)(5) requires that FMV be determined using "reasonable application of a reasonable valuation method," considering all facts and circumstances. In practice, auditors and the IRS prefer:

- **Current Value Method** for near-exit companies, or for conservatism and auditability.
- **PWERM** as the "safe harbor" for most venture-backed startups; it balances realism with defensibility.
- **Option Pricing Model** only if exit probability is demonstrably very high and the method is applied consistently.

Consultants typically perform all three methods and report all three, letting the client and auditor select the most defensible. However, a valuation that assumes an implausible success rate (e.g., 95% chance of a $10B outcome) will be questioned regardless of method.

The valuation must also pass the "smell test": if common shares are valued at $1 each in a healthy $500M company, the IRS may challenge the allocation as an attempt to gift equity to employees tax-free.

## Scenarios and Practical Trade-offs

**Early-stage (seed/Series A):**  
PWERM is standard. The company has multiple possible futures, and PWERM captures that realism. Common stock valuations are typically 20–40% of the per-share preferred price.

**Mid-stage (Series B/C):**  
PWERM remains most common, but failure probability falls. Common stock begins to approach preferred price multiples. Some consultants begin modeling Option Pricing as a secondary scenario.

**Late-stage (Series D+, approaching exit):**  
Current Value (if exit is imminent) or Option Pricing Model (if exit is very likely but not certain) becomes defensible. Common stock values rise sharply relative to preferred. The gap between preferred and common narrows.

**Down-round or restructuring:**  
Current Value Method often becomes the primary method; preferred investors' liquidation preferences bite. Common stock may be worth zero or near-zero until new capital arrives.

## Building Defensibility

A 409A valuation withstands IRS audit if the consultant:

1. **Documents assumptions**: States the company's stage, market size, competitive position, and management team explicitly.
2. **Benchmarks to comparables**: Uses precedent transactions, public comps, and comparable company multiples to set the overall valuation.
3. **Justifies probabilities**: Explains why the probability of each scenario is reasonable given market conditions and company performance.
4. **Addresses preferred terms**: Correctly models each class's liquidation preference, participation rights, and conversion features.
5. **Reports all three methods**: Shows that no single method is an outlier; if one produces extreme results, it is explained or discarded.

A well-constructed PWERM model, with transparent scenarios and realistic probabilities, is the easiest to defend in audit.

## See also

<div class="wiki-seealso">

### Closely related

- [Stock](/stock/) — equity as fractional ownership of a company
- [Liquidation preference](/liquidation-preference/) — the order in which shares are paid in an exit
- [Fair value](/fair-value/) — the principle that market-determined pricing should guide valuations
- [Cost basis](/cost-basis/) — how employee stock options affect your tax basis
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the method used to set the total company valuation being allocated

### Wider context

- [Private equity fund](/private-equity-fund/) — how venture investors approach equity allocation and returns
- [Option](/option/) — the financial derivative that inspired Option Pricing Model thinking
- [Section 179 deduction](/section-179-deduction/) — another tax rule affecting asset valuation and treatment

</div>

---
title: "How to Calculate Cost of Debt in a DCF"
description: "Step-by-step guide to estimating pre-tax and after-tax cost of debt for WACC, using yield-to-maturity, credit spreads, synthetic ratings, and market data."
keywords:
  - how to calculate cost of debt dcf
  - cost of debt wacc calculation
  - pre-tax cost of debt
  - after-tax cost of debt
  - yield to maturity debt cost
  - credit spread cost of debt
image: "/svg/valuation.svg"
---

*The cost of debt is the average interest rate a company pays on its borrowings, expressed as an annual percentage. In a DCF valuation, it feeds into the [WACC](/weighted-average-cost-of-capital/) (weighted average cost of capital) to [discount future cash flows](/discounted-cash-flow-valuation/). Unlike the cost of equity, cost of debt is observable from market prices or yield data, though adjusting for taxes requires care.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost of Debt — calculation essentials</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation methods." />

<div class="wiki-infobox-caption">Market-observable interest burden, adjusted for tax deductibility of interest expense.</div>

|   |   |
|---|---|
| **Basic formula** | After-tax cost of debt = (Interest expense ÷ Total debt) × (1 − Tax rate) |
| **Preferred input** | Yield-to-maturity of long-term debt; market yield if bonds trade |
| **Fallback method** | Credit-rating spread above risk-free rate |
| **Tax adjustment** | Critical; interest is tax-deductible, lowering effective cost |
| **Key assumption** | Firm continues to generate taxable income; carry-forward rules apply to NOLs |
| **Common error** | Using historical interest rates instead of forward market yields |
| **Multiple-instrument case** | Weight each debt tranche by book or market value |

</aside>

## Core Concept: Debt Is Cheaper Than Equity (After Tax)

The cost of debt is what a firm pays annually to service its borrowings as a percentage of debt outstanding. A company with $100 million in debt paying $5 million in annual interest has a cost of debt of 5%. This is lower than the [cost of equity](/cost-of-equity/)—the return shareholders demand—for a simple reason: debt is senior to equity in bankruptcy, so lenders accept lower returns. Additionally, interest expense is tax-deductible, making the *effective* cost to the firm even lower.

A company with a 5% cost of debt and a 35% tax rate incurs an after-tax cost of debt of 3.25%: the tax shield reduces the burden by 1.75 percentage points. This tax deductibility is why the WACC formula always uses *after-tax* cost of debt. Ignoring the tax effect significantly overstates the firm's weighted cost of capital and undervalues the firm in a DCF.

## Method 1: Yield-to-Maturity of Traded Bonds

The most direct approach is to use the [yield-to-maturity](/yield-to-maturity/) (YTM) of the firm's publicly traded bonds. If a company has bonds trading in the secondary market, their YTM represents the market's current assessment of the firm's interest burden.

**Steps:**

1. Identify all outstanding bond tranches (senior notes, subordinated notes, convertible debt, etc.).
2. Obtain the current market price and coupon of each tranche from Bloomberg, your broker, or financial websites.
3. Calculate or look up the YTM for each tranche.
4. Weight each YTM by the bond's market value (not face value, unless the bonds trade at par).
5. Divide the weighted total by aggregate debt outstanding to get a blended YTM.

**Example:** A firm has $50 million of 4% senior notes (YTM 4.2%) and $30 million of 6% subordinated notes (YTM 7%). The weighted average is:
- $50M × 4.2% + $30M × 7% = $2.1M + $2.1M = $4.2M in annual interest
- $4.2M ÷ $80M = 5.25% cost of debt (pre-tax)
- After-tax (35% tax rate): 5.25% × (1 − 0.35) = 3.41%

The YTM method is preferred because it reflects live market sentiment. However, it only works if bonds trade actively. For private firms or those without traded debt, alternatives are needed.

## Method 2: Credit Spread Over Risk-Free Rate

When a firm has no traded bonds, estimate the cost of debt as the [risk-free rate](/risk-free-rate/) plus a [credit spread](/credit-spread/) that reflects the firm's default risk.

**Steps:**

1. Choose a risk-free benchmark (typically the 10-year US Treasury yield, or the long-term yield matching the firm's weighted debt maturity).
2. Assign or look up a credit spread appropriate to the firm's credit rating (or estimated rating).
3. Add them: Cost of debt = Risk-free rate + Credit spread.

**Credit spreads by rating** (illustrative; spreads vary with economic conditions):

| Rating | Spread over Treasuries |
|--------|------------------------|
| AAA | 0.5–1.0% |
| AA | 1.0–1.5% |
| A | 1.5–2.5% |
| BBB | 2.5–4.0% |
| BB | 4.0–6.0% |
| B | 6.0–10.0% |

**Example:** If the 10-year Treasury is 3% and a firm is rated BBB, you might estimate a cost of debt as 3% + 3.0% = 6%.

This method is useful but less precise than YTM, since spreads vary with market conditions and the firm's specific circumstances. Still, it is transparent and defensible in a valuation.

## Method 3: Synthetic Rating Approach

For firms without a credit rating, estimate a synthetic rating using financial ratios, then apply the corresponding spread.

**Common metrics:**

- **Debt-to-EBITDA** – Higher leverage suggests higher risk; compare to rated peers.
- **Interest coverage ratio** – EBIT ÷ Interest expense; lower coverage implies higher risk.
- **Debt-to-equity ratio** – Higher leverage increases default risk.
- **Profitability and stability** – More volatile, lower-margin firms warrant higher spreads.

Compare the firm's ratios to those of rated comparables. If the target firm has a 3.0× Debt-to-EBITDA and comparably rated peers have 2.5–3.5×, assign a similar spread.

**Example:** A private company has:
- Debt-to-EBITDA: 3.2×
- Interest coverage: 3.5×
- Debt-to-equity: 1.8×
- These metrics align with BBB–rated peers.
- Assign a BBB spread, e.g., 3.0%, plus 10-year Treasury at 3% = 6% cost of debt.

Synthetic ratings are less precise than actual ratings but are a practical middle ground.

## Handling Multiple Debt Instruments

Most firms have multiple tranches: bank loans, bonds, convertible securities, operating leases. Each may have a different effective interest rate.

**Approach:**

1. List all interest-bearing liabilities (bank loans, bonds, notes, finance leases, in-substance finance leases).
2. For each, estimate the annual interest expense and outstanding balance.
3. Calculate the blended rate: Total annual interest expense ÷ Total debt outstanding.

Note: If you include operating leases (under IFRS 16 or ASC 842), recognize that lease liabilities carry an implicit interest rate embedded in the lease payment. Some analysts extract and use this rate; others treat operating leases separately. Be consistent.

**Example:**
- Bank loan: $40M outstanding, 5.5% rate, $2.2M annual interest
- Senior bonds: $50M outstanding, 4.2% rate, $2.1M annual interest
- Subordinated debt: $20M outstanding, 7.0% rate, $1.4M annual interest
- Total debt: $110M; total interest: $5.7M
- Blended pre-tax cost of debt: 5.7% ÷ $110M = 5.18%

## Adjusting for Tax Benefits: The After-Tax Cost

The tax adjustment is critical and often missed. Interest expense reduces taxable income, creating a tax shield:

**After-tax cost of debt = Pre-tax cost × (1 − Tax rate)**

The tax rate should be the firm's marginal corporate [tax rate](/corporate-income-tax/), not its effective rate. For a US company, the federal rate is 21% (as of 2024), plus any state/local tax (typically 0–10%, varying by jurisdiction). Combined marginal rates often range from 21–30% in the United States.

**Caveat:** This formula assumes the firm generates sufficient taxable income to deduct interest. If a firm has large **NOLs** (net operating loss carryforwards) and cannot deduct interest in the near term, the effective tax benefit is deferred, and the analyst might use a lower tax rate or defer the benefit. In DCF models, if the firm is expected to be unprofitable for several years, apply the tax rate conservatively or only to years when the firm is profitable.

## Refining the Estimate: Currency and Floating Rates

If a firm has debt in multiple currencies, weight each by value and apply the appropriate risk-free rate and spread for that currency. USD debt uses the US Treasury curve; EUR debt uses the German Bund curve, etc.

If the firm has floating-rate debt (e.g., loans tied to SOFR or LIBOR), use the forward-expected rate or current rates plus an estimate of future rate changes, rather than historical coupon rates. A loan currently at SOFR + 2.5% with SOFR at 5.5% is effectively 8%, but if rates fall, the cost falls with them.

## Common Pitfalls

1. **Using the coupon rate instead of YTM.** The coupon is fixed; YTM reflects current market price and is the correct input.
2. **Forgetting the tax adjustment.** Using 5% pre-tax cost of debt in WACC instead of the after-tax 3.25% overstates the discount rate and undervalues the firm.
3. **Inconsistent debt measurement.** Including some liabilities but excluding others (e.g., forgetting finance leases) skews the blended rate.
4. **Stale or mismatched spreads.** Using spreads from a different economic cycle or company size class undermines the estimate.
5. **Confusing the interest rate with the cost of debt.** The cost of debt is the *effective* rate the firm pays on all outstanding borrowings, not the rate on the most recent issuance.

## See also

<div class="wiki-seealso">

### Closely related

- [Weighted average cost of capital](/weighted-average-cost-of-capital/) — Framework integrating cost of debt and cost of equity
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — WACC as the discount rate
- [Yield to maturity](/yield-to-maturity/) — Bond metric for estimating cost of debt
- [Credit spread](/credit-spread/) — Market reward for default risk; inputs to synthetic ratings
- [Credit rating](/credit-rating/) — Determinant of spreads and cost of debt
- [Cost of equity](/cost-of-equity/) — Complementary cost, typically higher than cost of debt
- [Interest coverage ratio](/interest-coverage-ratio/) — Metric for assessing debt sustainability
- [Capital asset pricing model](/capital-asset-pricing-model/) — Framework for estimating cost of equity

### Wider context

- [Debt-to-equity ratio](/debt-to-equity-ratio/) — Leverage metric affecting both cost of debt and cost of equity
- [Corporate bond](/corporate-bond/) — Instrument whose YTM is used in cost-of-debt estimation
- Bankruptcy — Consequence of unsustainable debt costs
- [Tax bracket](/tax-bracket-investor/) — Corporate marginal rate used in tax adjustment

</div>

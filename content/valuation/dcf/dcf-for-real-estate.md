---
title: "DCF Valuation for Real Estate"
description: "DCF valuation for real estate adapts the cash flow discount model to property. Learn how to project NOI, choose a cap rate, and estimate terminal value."
keywords:
  - dcf valuation for real estate
  - discounted cash flow real estate
  - property valuation noi
  - cap rate terminal value
  - commercial real estate dcf
  - real estate appraisal methods
image: "/svg/valuation.svg"
---

*A **DCF valuation for real estate** applies the discounted cash flow framework to property by projecting the building's net operating income over a holding period, then discounting both the annual cash flows and a terminal resale value back to today.* Unlike stocks, where cash flows are often uncertain and far in the future, rental properties generate predictable lease income—making DCF a natural fit for commercial real estate, multifamily apartments, and other income-producing assets.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DCF for Real Estate — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Property value = PV of NOI + PV of terminal resale, discounted at your required rate of return.</div>

|   |   |
|---|---|
| **Core formula** | Value = ∑(NOI / (1+r)^t) + Terminal Value / (1+r)^n |
| **Key input: NOI** | Gross rental income − operating expenses (excluding debt service) |
| **Terminal value** | Usually: exit year NOI × exit cap rate (or exit multiple) |
| **Discount rate (r)** | Your required return; often 8–15% for real estate |
| **Time horizon** | Typically 5–10 years for institutional properties |
| **Link to [cap rate](/cap-rate/)** | Exit cap rate directly determines terminal value sensitivity |

</aside>

## The DCF Framework Adapted to Property

In a standard [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/), you estimate the cash flows an asset will generate, decide on a discount rate that reflects your required return and risk, and compute the present value. Real estate is simpler than many businesses because rental income is contractual (leases) and expenses are largely fixed and visible.

The basic structure is:

1. **Project net operating income (NOI)** for years 1 through N
2. **Estimate a terminal value**—typically, the resale price in year N
3. **Choose a discount rate**—your required annual return
4. **Discount all cash flows and the terminal value to today**

The property's fair value, under this model, is the sum of those discounted amounts.

## Projecting Net Operating Income

NOI is revenue minus operating costs, excluding debt service (mortgage payments are not deducted). For a multifamily property:

- **Gross rental income**: actual or stabilized rent × occupancy rate
- **Operating expenses**: property tax, insurance, maintenance, utilities, management, capital reserves, vacancy loss
- **NOI = Gross income − Operating expenses**

A key assumption is the **growth rate**. Rental income typically rises 2–3% per year in line with inflation; operating expenses may grow at a similar rate or slightly faster. Some analysts assume a "stabilized" year of operations and project from there, rather than forecasting year-by-year.

For example, a 100-unit apartment building grossing $1.2 million annually with 5% vacancy and $400,000 in operating costs would have NOI of roughly $740,000 in year 1. If you assume 2.5% growth, year 2 NOI might be $758,350.

## Terminal Value and Exit Strategy

The terminal value is usually 60–80% of your total property value under a DCF, because most of the value sits in that final year's resale, not year-to-year cash flows.

**The most common approach is the cap rate method:**

Terminal Value = Exit Year NOI ÷ Exit Cap Rate

For example, if you forecast that in year 5 the property's NOI will be $850,000, and you expect to sell it to a buyer demanding an 8% [cap-rate](/cap-rate/) (a fair current market rate), the terminal value would be $850,000 ÷ 0.08 = $10.625 million.

Why? Because the buyer will look at year 5's NOI and apply their own required return (the cap rate) to justify paying that price. Your job is to guess what that buyer's cap rate will be—historically, cap rates have ranged from 4–5% for trophy properties in hot markets to 8–10% for secondary properties or during high-interest-rate environments.

**Alternative terminal value approaches:**

- **Exit multiple**: Sell at a fixed NOI multiple, e.g., 12× NOI
- **Appreciation assumption**: Assume property value grows at 2–3% per year (less precise)
- **Longer hold, zero residual**: Project 30+ years of income and assume no resale (rarely done)

## Choosing a Discount Rate

The discount rate (also called the **required return** or **hurdle rate**) reflects what return you need to justify the risk and capital tied up in the property. It's not the mortgage rate; it's your equity return threshold.

Real estate discount rates typically range from **7–15%**, depending on:

- **Property type and location**: Core urban office or premium retail, 6–8%; secondary market, 10–12%
- **Tenant credit quality**: Government or investment-grade tenants, lower rate; small, unstable tenants, higher
- **Interest rate environment**: Higher [interest-rate](/interest-rate/) environment → higher discount rates
- **Lease stability**: Long-term, triple-net leases (tenant pays taxes and insurance) justify lower rates
- **Your alternatives**: If you can earn 10% in [bond](/bond/) or [stock](/stock/), you need real estate to beat that

A simple shortcut: **discount rate ≈ cap rate + equity risk premium**. If the market cap rate is 7% and you demand an extra 3% for illiquidity and leverage risk, your discount rate might be 10%.

## Why Terminal Value Drives the Valuation

Because you're discounting the terminal value back many years, it's extremely sensitive to small changes in the exit cap rate.

Suppose the terminal value in year 5 is $10 million. Discounted at 10% for 5 years:

- Year 5 resale value, discounted = $10,000,000 ÷ (1.10)^5 = $6.2 million

If your exit cap rate assumption slips from 8% to 7%, the terminal value jumps to $12.1 million, and its discounted value becomes $7.5 million—a $1.3 million swing on a property you haven't even bought yet.

This is why institutional investors stress-test the terminal cap rate. They ask: what if the market cap rate is 9% when I sell, not 8%? How much does that hurt my return?

## Building a Simple Model: A Worked Example

Assume you're evaluating a 50-unit apartment building:

- **Year 1 gross rent**: $600,000 (12 units × $12,000/year)
- **Vacancy assumption**: 5%
- **Operating expenses**: $150,000 per year (25% of gross)
- **Growth**: 2.5% annually
- **Hold period**: 5 years
- **Exit cap rate**: 7%
- **Your required return (discount rate)**: 10%

| Year | Gross Income | Vacancy Loss | Operating Exp | NOI | PV Factor @ 10% | PV of NOI |
|------|--------------|--------------|---------------|-----|-----------------|-----------|
| 1    | $600k        | $30k         | $150k         | $420k | 0.909 | $382k |
| 2    | $615k        | $31k         | $154k         | $430k | 0.826 | $355k |
| 3    | $631k        | $32k         | $158k         | $441k | 0.751 | $331k |
| 4    | $647k        | $32k         | $162k         | $453k | 0.683 | $309k |
| 5    | $663k        | $33k         | $166k         | $464k | 0.621 | $288k |

**Terminal value (end of year 5)**: $464,000 ÷ 0.07 = $6.63 million  
**PV of terminal value**: $6,630,000 × 0.621 = $4.12 million  
**Total property value**: $382k + $355k + $331k + $309k + $288k + $4,120k = **$5.785 million**

## Sensitivity to Key Assumptions

Real estate DCF is vulnerable to three assumptions:

1. **Exit cap rate**: A 1% change can swing terminal value by 15–20%
2. **Long-term NOI growth**: Small changes to 2% vs. 3% growth compound significantly
3. **Discount rate**: Higher discount rates compress present value dramatically

Professional appraisers often produce a valuation range (e.g., $5.4M–$6.2M) and note which assumptions matter most. A sensitivity table showing value under different exit cap rates and discount rates is common.

## When to Use (and Not Use) Real Estate DCF

**DCF works well for:**
- Income-producing properties with stable, long-term leases
- Institutional or REIT-held assets with public comparables for cap rates
- Properties where you have reliable historical expense data
- Strategic decisions about hold vs. sell timing

**DCF is weaker for:**
- Pre-leased developments or vacant land (no current NOI; entirely dependent on terminal assumptions)
- Distressed or value-add properties where repositioning is the main value driver
- Markets where properties are priced on "multiples" or comps, not cash flow (some trophy real estate)

For those cases, a [relative-valuation](/relative-valuation/) approach—comparing to recent sales of similar properties—often complements or replaces DCF.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the underlying framework for any DCF model
- [Cap Rate](/cap-rate/) — the market yield that sets terminal values and links to required returns
- [Net Operating Income](/net-operating-income/) — the cash generation metric that drives property valuation
- [Real Estate Investment Trust](/real-estate-investment-trust/) — how REITs use DCF and cap rates in portfolio management
- [Commercial Real Estate](/commercial-real-estate/) — market context and lease structures affecting NOI stability

### Wider context

- [Relative Valuation](/relative-valuation/) — comparing properties to market comps
- [Sensitivity Analysis Valuation](/sensitivity-analysis-valuation/) — testing assumptions in your model
- [Return on Invested Capital](/return-on-invested-capital/) — framing the discount rate as your required return
- [Enterprise Value](/enterprise-value/) — the DCF principle applied to corporate assets

</div>

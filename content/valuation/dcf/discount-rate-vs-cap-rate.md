---
title: "Discount Rate vs Cap Rate in Valuation"
description: "Discount rate vs cap rate clarifies the difference between DCF discount rates and capitalization rates used in income-property valuation."
keywords:
  - discount rate
  - cap rate
  - capitalization rate
  - dcf valuation
  - real estate valuation
  - property valuation
  - income approach
---

*The **discount rate** and **cap rate** are often confused, but they measure different aspects of investment risk and return. A discount rate reflects the time value of money and risk in a discounted cash flow (DCF) valuation, while a **capitalization rate** (cap rate) is a shorthand for the relationship between a single year's income and property price, commonly used in real estate valuation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Discount Rate vs Cap Rate — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two distinct metrics serving different valuation purposes and investor decision-making.</div>

|   |   |
|---|---|
| **Discount rate** | Required return used to discount future cash flows to present value; reflects risk, time value, and opportunity cost |
| **Cap rate** | Net operating income divided by property price; a shorthand yield metric for direct comparison |
| **Time horizon** | Discount rate applies to multi-period DCF; cap rate is a single-period ratio |
| **Typical range (real estate)** | Discount rates: 7–12%; cap rates: 3–10% (varies by property class, location, risk) |
| **Formula** | Discount rate: applied in PV = CF / (1 + r)^t; cap rate: NOI / Purchase Price |
| **Stability** | Discount rate reflects investor cost of capital; cap rate reflects market-traded prices |
| **Application** | Discount rate: acquisition valuation, project ranking; cap rate: comparable property screening |

</aside>

## The Discount Rate: Time Value and Risk

A discount rate is the rate of return an investor requires to compensate for the time value of money and the risk of a given investment. It is the denominator in a present-value calculation.

For example, if you are valuing an office building and expect it to generate USD 1 million in net operating income annually for 20 years, a simple present-value formula would be:

**Value = Σ(NOI_t / (1 + r)^t)** for t = 1 to 20

where r is the discount rate.

If r = 8%, the present value of USD 1 million in year 1 is USD 925,926. In year 10, it is USD 463,193. In year 20, it is USD 214,548. The discount rate reflects the investor's view of how much return is required to justify owning that cash flow instead of, say, holding a government bond yielding 4%, or buying stock yielding 6%.

The discount rate for a property is typically built from:
- A **risk-free rate** (e.g., 10-year Treasury yield, typically 3–5%)
- A **risk premium** for illiquidity, property-specific risk, and market volatility (typically 2–7%)

Total discount rate: 5–12%, depending on property quality, location, and market conditions.

A strong apartment complex in a major market might use 6% (low risk premium); a speculative development or troubled property might use 12% (high risk premium).

## The Cap Rate: A Single-Period Shorthand

A capitalization rate (cap rate) is simply the ratio of net operating income (NOI) in the first year to the purchase price:

**Cap Rate = NOI / Purchase Price**

If an office building trades for USD 10 million and generates USD 600,000 in NOI, the cap rate is 6%.

The cap rate is a shorthand for "if I buy this property at this price and achieve this NOI, my first-year return is 6%." It is a single-period metric and does not explicitly account for growth, leverage, or risk over time.

However, the cap rate is useful because it is observable. When properties trade, their prices and incomes are public (at least in commercial real estate). A valuer can quickly compare similar properties across a market and see that office buildings are trading at 5–7% cap rates, apartments at 4–6%, and industrial warehouses at 6–8%. This reveals what the market is paying for income in different property classes.

## How They Relate (and Differ)

For a property with stable, non-growing income, the cap rate and discount rate are nearly identical. If a property generates USD 1 million annually and will do so forever, and you buy it for USD 12.5 million (an 8% cap rate), your discount rate is also 8%.

But they diverge when income is expected to grow or decline:

Suppose a property has USD 1 million in NOI today and you expect 3% annual NOI growth. You pay USD 12.5 million (8% cap rate today). 

Using a DCF with an 8% discount rate:
- Year 1: USD 1.00M / 1.08 = USD 926K
- Year 2: USD 1.03M / 1.08^2 = USD 883K
- Year 3: USD 1.061M / 1.08^3 = USD 843K
- ... and so on, converging to a present value ≈ USD 13.75 million (assuming a 20-year hold and terminal value)

The discrepancy arises because the 8% cap rate implicitly assumes no growth, while the DCF discounts a growing income stream. If the property is expected to appreciate in value or generate growing rental income, the cap rate understates the true return; the discount rate is more accurate.

Conversely, if NOI is expected to *decline* (aging building, obsolete uses), the cap rate overstates returns.

## Where Each Metric Is Used

**Discount rate dominates:**
- Acquisition valuations for specific investors (your required return matters)
- Project ranking and capital budgeting (should we buy this or that property?)
- Leveraged buyouts and structured finance (return on equity vs. return on assets)
- Any scenario with significant income growth, leverage, or time-varying risk

**Cap rate dominates:**
- Comparable-properties analysis (what did similar buildings sell for recently?)
- Appraisals and market-based valuation (external benchmarking)
- Market screening (which cap rates are attractive in this city right now?)
- Quick back-of-envelope decisions (is this deal in the ballpark?)

In practice, commercial real estate appraisers often use *both*:

1. Estimate a cap rate from recent comparable sales.
2. Adjust it up or down based on the subject property's growth, condition, and management.
3. Use the adjusted cap rate to derive a discount rate for a DCF analysis.
4. Compare the DCF-derived value to the market value implied by comparable cap rates.

If the two values diverge significantly, the appraiser investigates the mismatch: Is the cap rate for comparables unrepresentative? Are the growth assumptions unrealistic? Is the discount rate too high or too low?

## Practical Pitfall: Confusing Yield and Return

A common mistake is conflating cap rate with total return. The cap rate is the first-year income yield; total return includes price appreciation or depreciation, leverage effects, and multi-year value changes.

Example: You buy a property at an 8% cap rate expecting 3% annual NOI growth and 4% annual appreciation. Your total return is not 8%; it is closer to 8% + 4% + leverage benefits, less holding costs. The cap rate is only the starting point.

Similarly, confusing a discount rate with a current yield can lead to overvaluation. If you buy a bond trading at par with a 5% coupon, the yield to maturity is 5%. But if interest rates rise, the bond's market price falls. If you are valuing a bond portfolio and the discount rate is based on current market rates (7%), you must discount the 5% coupon stream by 7%, not 5%, to get true present value.

## Market Implications

When cap rates are low (e.g., 3–4% for trophy properties in central cities), it means the market is willing to accept low income yields, typically because price appreciation is expected or the property is viewed as very safe. During such periods, properties are expensive relative to current income.

When cap rates are high (e.g., 8–10%), it means the market requires high income yields, typically because prices are depressed, risk is high, or growth is not expected. Properties are cheap relative to current income.

Cap rates therefore serve as a market sentiment gauge. Rising cap rates often signal that investors are turning cautious (repricing risk upward); falling cap rates signal optimism or complacency.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the DCF framework in which discount rates are applied
- [Cost of Equity](/cost-of-equity/) — the required return on equity capital, a component of discount-rate estimation
- [Real Estate Investment Trust](/real-estate-investment-trust/) — securities that own income-producing properties valued using cap rates and DCF
- [Net Operating Income](/net-operating-income/) — the income metric that sits in the numerator of cap-rate calculations

### Wider context

- Valuation — broader framework for asset pricing and company/property assessment
- [Interest Rate](/interest-rate/) — determines risk-free rates and affects discount rates across all assets
- [Real Estate Cycle](/real-estate-cycle/) — context for understanding cap-rate compression and expansion
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — theoretical foundation for estimating cost of capital (discount rates)
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — technique for testing how valuation changes with different discount and cap rates

</div>

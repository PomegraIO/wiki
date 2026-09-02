---
title: "Illiquidity Discount in Private Company DCF"
description: "Explains illiquidity discount private company DCF: rationale, empirical ranges (10–40%), and application to valuation."
keywords:
  - illiquidity discount private company dcf
  - illiquidity discount valuation
  - private company valuation discount
  - lack of marketability discount
  - non-control discount valuation
image: /svg/valuation.svg
---

*An **illiquidity discount** (also called a lack-of-marketability discount or minority-discount) is a percentage reduction applied to the [discounted cash flow](/discounted-cash-flow-valuation/) value of a private company to reflect the owner's inability to sell the stake quickly at fair value. Because a private equity stake cannot be instantly converted to cash without finding a buyer and negotiating a transaction, valuators typically apply a discount of 10–40% to compensate for this illiquidity, though the precise rate depends on company maturity, industry, and the owner's expected holding period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Illiquidity Discount in DCF — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The hidden cost of owning an asset you cannot quickly sell.</div>

|   |   |
|---|---|
| **Definition** | Percentage reduction to fair value to account for selling friction and time to exit |
| **Typical range** | 10–40% for mature private companies; 30–60% for startups or minority stakes |
| **Rationale** | Buyer illiquidity increases [cost of equity](/cost-of-equity/) and extends cash realization period |
| **Key drivers** | Company size, industry, governance, buyer pool, expected holding period, exit strategy |
| **Applied to** | Discounted cash flow value AFTER calculating the intrinsic (liquid-market) value |
| **Not the same as** | [Control premium](/control-premium/) (applies to control vs. non-control); tax or regulatory discounts |
| **Regulatory use** | Estate tax, gift tax, and fairness opinion valuations in the U.S. |

</aside>

## Why Illiquidity Deserves Its Own Discount

The standard [discounted cash flow](/discounted-cash-flow-valuation/) model produces a "fair value"—the present value of all future cash flows using a [cost of equity](/cost-of-equity/) or [WACC](/weighted-average-cost-of-capital/) derived from comparable public companies or market data. This fair value assumes an investor can own the cash flows and exit whenever he wishes, perhaps by selling to another investor or through a liquid public market.

But private company ownership is not liquid. If you own 20% of a private software company, you cannot convert that stake to cash in one phone call. You must find a buyer (narrower pool than public markets), negotiate a price (often takes months), and wait for the transaction to close (another 30–90 days). During this period, the business could deteriorate, management could quit, or market conditions could shift. And you have no interim liquidity to redeploy capital if a better opportunity appears.

This illiquidity risk is real and material. An investor who must wait 3–5 years to sell an illiquid stake faces opportunity cost, reinvestment uncertainty, and concentration risk. She demands to be compensated for this illiquidity at the time of purchase—hence the discount. The discount bridges the gap between the intrinsic value (what a liquid owner would pay) and the price an illiquid owner should pay today.

## The Distinction from Other Discounts

**Illiquidity discount vs. control premium:** A [control premium](/control-premium/) or lack-of-control (minority) discount reflects the value of operational control—the ability to set strategy, hire/fire, declare dividends, or force a sale. A minority shareholder in a private company may not have control. So a 5% stake in a $10M company is worth less than 5% of the full enterprise value, *both* because it lacks control *and* because it is illiquid. The illiquidity discount is separate from (and usually larger than) the control discount.

**Illiquidity discount vs. key-person risk or small-firm discount:** Some valuators apply ad-hoc discounts for small size, concentration in one customer, dependence on a key employee, or weak governance. These are not illiquidity discounts; they are adjustments for business-specific risk that would exist even in a public company with identical cash flows and risk profile. The illiquidity discount is purely about the marketability of the ownership stake, not the riskiness of the business.

## Empirical Ranges and Benchmarks

Academic and practitioner research has produced wide-ranging estimates:

**Mature, mid-market private companies (revenue $10M–$100M):** 15–30% discount. These firms have established cash flows, diversified customer bases, and a reasonable buyer pool (other PE firms, strategic acquirers, growth equity investors). Exit in 3–5 years at a known EBITDA multiple is plausible.

**Smaller or early-revenue private companies (revenue under $10M):** 25–45% discount. Buyer pool is narrower, profitability may be uncertain, and many potential acquirers are themselves private and cash-constrained. The holding period might stretch to 7–10 years.

**Venture-backed startups pre-exit:** 40–70% discount. A Series C biotech or software startup might be worth $500M on a liquidation-value basis (DCF using market comps), but a minority shareholder with no board seat and no liquidation rights might apply a 50%+ discount because exit is 5–10 years away and highly uncertain. Preferred shares (which have liquidation preference and other protections) deserve a smaller discount than common shares.

**Restricted stock in public companies:** 20–35% discount, as empirical studies of Rule 144 restricted stock and letter stock sales have documented. A share of Apple is worth less if you cannot sell it for 6 months; the illiquidity discount reflects the real economic cost of that restriction.

These ranges overlap significantly. There is no universal formula; the discount is specific to the transaction and the buyer's circumstances.

## How Valuators Estimate the Discount: Three Approaches

**Comparable transaction approach:** Identify M&A transactions for similar companies and calculate the implied discount by comparing acquisition price to pre-transaction DCF or public market valuations. If ABC Software was valued at $50M DCF but sold for $40M, the implied discount is 20%. The challenge is finding truly comparable deals; purchase prices are often confidential, and each deal is somewhat unique.

**Cost-of-equity adjustment:** Some valuators build illiquidity into the cost of equity itself, raising the discount rate by 2–6 percentage points for illiquid companies. A liquid biotech might use a 10% cost of equity; an illiquid private biotech might use 13–14%. This raises the discount rate, lowering the present value of cash flows. Mathematically, this can be equivalent to applying a lump-sum discount to the DCF value, but it explicitly connects illiquidity to the time value of money. The concern is double-counting: if you raise the discount rate, do not also apply a separate illiquidity discount.

**Regression/empirical models:** Academic research (e.g., Mercer's "Quantifying Marketability Discounts," Damodaran's work on illiquidity in asset pricing) has estimated the illiquidity discount as a function of volatility, liquidity measures (bid–ask spread proxies), and holding period. More volatile businesses and longer holding periods get larger discounts. This approach is systematic but data-heavy and requires assumptions about the holding period and the private company's volatility.

## Applying the Discount: Mechanics and Timing

The standard sequence is:

1. Build a DCF model for the private company, projecting 5–10 years of [free cash flow](/free-cash-flow/).
2. Estimate the [terminal value](/terminal-value/) using a perpetuity growth assumption or exit multiple.
3. Discount all cash flows and terminal value at the [weighted-average cost of capital](/weighted-average-cost-of-capital/) (or cost of equity) to get enterprise value (EV).
4. Subtract net debt to get **equity value** (the liquid-owner price).
5. Apply the illiquidity discount: multiply equity value by (1 – discount rate). If discount is 20%, equity value of $100M becomes $80M.
6. Allocate this discounted value to the specific stake you are valuing (e.g., 5% stake gets 5% of the discounted EV).

**Critical point:** The illiquidity discount is applied *after* you have calculated the intrinsic equity value. You do not reduce the cash flows themselves or arbitrarily lower the discount rate to compensate for illiquidity; instead, you apply a valuation adjustment at the end. This preserves the integrity of the DCF cash-flow projections and makes the illiquidity impact transparent.

## Factors That Drive the Discount Up or Down

**Longer holding period → higher discount.** If you expect to hold the stake for 10 years before exit, the illiquidity burden is larger than if exit is in 3 years. Typical assumptions range from 3–7 years for a PE-backed buyout to 7–15 years for a family business.

**Narrower buyer pool → higher discount.** A company in a niche vertical (specialized industrial equipment, proprietary software for a regulated industry) has fewer potential acquirers than a scalable B2C SaaS company. Fewer buyers mean longer selling process and lower bids.

**Minority vs. controlling stake → higher discount for minority.** A controlling shareholder can force a sale or take the company public, reducing illiquidity. A minority shareholder cannot. A 100% stake gets little or no illiquidity discount; a 10% minority stake gets a larger one.

**Dividend policy and interim cash distributions → lower discount.** If the company pays dividends or distributions, the owner has some interim liquidity and optionality. Lower distributions mean the owner is purely waiting for exit, increasing the illiquidity burden.

**Market conditions and M&A activity → variable.** In booming M&A markets, illiquidity discounts compress (buyers are eager, prices are high). In recessions, discounts widen (buyers are scarce, exit multiples are low).

## Real-World Example

**Scenario:** A private manufacturing company, ABC Parts Co., has projected free cash flow of $5M in year 1, growing at 3% annually. Cost of equity is 10%.

**DCF (liquid):** Terminal value at year 10 using a 3% perpetuity growth and 10% discount rate yields ~$120M equity value.

**Illiquidity adjustment:** The company is mid-sized, serves a diverse industrial customer base, and has a clear path to sale or dividend recapitalization. An illiquidity discount of 20% is appropriate (holding period 4–5 years, solid buyer pool).

**Discounted equity value:** $120M × (1 − 0.20) = $96M.

If you own 25% of the company, your stake is worth $24M in the illiquid context. Had you owned public shares worth $30M, the illiquidity would cost you $6M in discount.

## Tax and Legal Implications

U.S. tax valuators (for estate tax and gift tax purposes) apply illiquidity discounts routinely. The IRS generally accepts discounts in the 15–35% range for mature closely held businesses, though aggressive valuators have claimed discounts up to 50% for very illiquid, small, or minority stakes. The Tax Court scrutinizes these claims heavily, and each case turns on facts.

Fair-value opinions in legal contexts (divorce, litigation, regulatory proceedings) also apply illiquidity discounts, though the standard of proof is higher than in tax matters.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the base model to which illiquidity is applied
- [Cost of equity](/cost-of-equity/) — the discount rate that reflects some illiquidity risk
- [Relative valuation](/relative-valuation/) — alternative approach using multiples
- [Private placement](/private-placement/) — how illiquid stakes are often sold
- [Sensitivity analysis valuation](/sensitivity-analysis-valuation/) — testing discount rate changes
- [Intrinsic value](/intrinsic-value/) — the reference value before applying discounts

### Wider context

- [Liquidity risk](/liquidity-risk/) — the underlying economic principle
- [Holding period](/holding-period/) — a key driver of illiquidity discounts
- [Bid-ask spread](/bid-ask-spread/) — the market-liquidity analog in public markets
- [Merger](/merger/) — an exit path for illiquid stakes
- [Secondary market](/secondary-market/) — where illiquid secondary shares trade
- [Counterparty risk](/counterparty-risk/) — heightened when buyer pool is small

</div>

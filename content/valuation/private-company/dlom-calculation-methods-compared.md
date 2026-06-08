---
title: "DLOM Calculation Methods Compared: Restricted Stock vs Put Option Models"
description: "How to calculate discount for lack of marketability using restricted-stock, pre-IPO, and put-option methods; each produces different valuations."
keywords:
  - discount for lack of marketability
  - dlom calculation
  - restricted stock method
  - put option model dlom
  - private company valuation
  - lack of marketability discount
image: "/svg/valuation.svg"
---

*The **discount for lack of marketability** (DLOM) adjusts a private company's fair value downward to reflect the fact that shareholders cannot easily sell their shares. A company worth $100 million if its equity were liquid might be valued at $70–$80 million in the hands of a restricted shareholder. Three quantitative methods—restricted-stock studies, pre-IPO transaction analysis, and put-option models—produce materially different DLOM percentages for the same company. Each has strengths and blind spots; practitioners typically triangulate among all three rather than relying on a single approach.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DLOM — Three Quantitative Approaches</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The three main methods often produce different results; rarely do all three align.</div>

|   |   |
|---|---|
| **Restricted-stock method** | 20–50% DLOM (median ~35%) |
| **Pre-IPO method** | 15–40% DLOM (median ~25%) |
| **Put-option model** | 10–45% DLOM (varies widely) |
| **Typical range for high-growth private** | 30–45% |
| **Typical range for mature private** | 20–35% |
| **Most common in practice** | Restricted-stock method |
| **Most theoretically rigorous** | Put-option model |

</aside>

## The Restricted-Stock Method

The oldest and most widely used DLOM technique is the **restricted-stock method**, which looks at the discount at which restricted shares of public companies trade relative to the free-trading stock of the same company. Restricted shares (also called **letter stock** or founder shares) have a contractual lockup: the holder cannot sell for a defined period—typically two years or longer—without SEC registration or an exemption.

The logic is straightforward: if Microsoft restricted shares trade at a 40% discount to liquid Microsoft shares, then illiquid minority stakes in private companies should suffer similar discounts, all else equal. Studies dating back to the 1960s (notably Morningstar and the SEC's own analyses) have documented these discounts. Early work found discounts as high as 70%, but more recent studies cluster in the 25–40% range, depending on the lockup period and the company's size and volatility.

To apply the method, an analyst:

1. Identifies public company restricted-share transactions that occurred at, or near, the valuation date.
2. Compares the purchase price of the restricted shares to the current trading price of the liquid stock.
3. Calculates the discount as a percentage: (Liquid Price − Restricted Price) / Liquid Price.
4. Adjusts for differences in lockup term, company profitability, and volatility between the public comparables and the private company being valued.

A weakness of the method is that **restricted shares in public companies are not the same as illiquid minority stakes in private companies**. Public company restricted shareholders know that, in two years, they can freely sell—they have a known exit date and can plan around it. A private company shareholder has an indefinite, uncertain liquidity prospect. Moreover, public restricted shareholders often include insiders (executives, founders) with information and control; private shareholders may be passive investors with little influence over when or how the company might exit.

## The Pre-IPO Method

The **pre-IPO method** sidesteps some of these problems by looking at real-world transactions in private company shares—rounds of venture capital financing, secondary transactions, or buybacks—that occur shortly before the company goes public. The idea is to capture the true discount that investors apply when the company is on the cusp of liquidity.

For example, if a private company's Series C round (six months before IPO) valued the company at $2 billion, and the IPO priced the stock such that the fully-diluted value was $3 billion, the implicit DLOM on the Series C shares was roughly 33%. 

This method has intuitive appeal: it is based on real transactions by investors with strong incentives to price accurately. Venture capital firms and growth equity investors are financially sophisticated and have access to detailed company information; they are not making abstract theoretical estimates.

The practical limitation is **data scarcity**. Few companies have pre-IPO transaction data available publicly, especially at a consistent quality. An analyst may find five or six comparable IPOs per year with usable data, making the sample small and potentially biased toward successful, high-growth companies. Slower-growing private firms or those in unglamorous industries may lack any IPO comparables.

Additionally, pre-IPO DLOMs conflate multiple factors: the illiquidity discount, venture capital illiquidity premiums, option value from future growth, and cyclical market conditions at the time of the IPO. Disentangling them is difficult.

## The Put-Option Model

The **put-option model** (sometimes called the Finnerty model or the income approach) treats illiquidity as an American put option on the stock. The shareholder has the right, but not the obligation, to sell the stock at a given price on or after a given date—the hypothetical liquidity event. The value of that option is the DLOM.

The model uses **Black-Scholes option pricing** (or a variant) with inputs:

- **Current stock value** (the liquid fair value of the company, divided by shares outstanding).
- **Strike price** (same as current value; the shareholder is not underwater).
- **Time to liquidity** (expected years until exit—often 5–10 years for private companies).
- **Volatility** (the annualized standard deviation of stock returns; for private companies, estimated from comparable public firms or historical data).
- **Risk-free rate** (the yield on Treasury securities).

The model calculates the value of a put option with these parameters. That option value, expressed as a percentage of the current stock price, is the DLOM.

A numerical example: Suppose a private company is worth $100 per share based on free cash flow. The analyst estimates 40% annualized volatility, a 3% risk-free rate, and a 7-year holding period. A put option with these inputs might be worth $25 per share, implying a 25% DLOM.

The put-option model is theoretically elegant and rigorous. It explicitly accounts for volatility and time to exit, two factors that intuitively matter. A shareholder of a stable, low-volatility company should be willing to accept less discount than a shareholder of a volatile company, because the option to exit (eventually) is less valuable. Time also matters: if exit is expected in 3 years, the option is worth more than if it is 15 years away, because the shareholder faces less uncertainty.

However, the model's accuracy hinges on estimating volatility and time-to-exit correctly, and both are highly uncertain for private companies. A venture-backed SaaS firm might exit in 5–7 years; a family business might be illiquid forever (or exit in 20 years). Volatility estimates derived from public comparables may not apply: a private company might be more or less volatile than the public version due to leverage, diversification, or customer concentration.

## Practical Comparison: An Example

Imagine a private software company, valued at $500 million on a [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) basis. You are valuing a 5% minority stake for gifting or estate purposes. All three methods give different DLOMs:

**Restricted-stock method:** You find that restricted software company stocks discounted 30–40% over the past five years. You apply 35%, yielding a 35% discount to the $500 million equity value. The stake is worth $500M × 5% × (1 − 0.35) = $16.25 million.

**Pre-IPO method:** You identify three software company IPOs in the past 18 months with pre-IPO data. Discounts ranged from 20% to 35%, median 25%. You apply 25%, yielding $500M × 5% × (1 − 0.25) = $18.75 million.

**Put-option model:** You estimate 50% volatility (software companies are volatile), a 6-year hold, and a 2.5% risk-free rate. The model generates a 28% DLOM, yielding $500M × 5% × (1 − 0.28) = $18.00 million.

The three methods produce a range of $16.25–$18.75 million for the same stake—a spread of about 15%. For large estates, tax planning, or acquisition negotiations, that gap matters.

## Which Method to Use?

In practice, valuers use all three, weight them by relevance, and synthesize a conclusion. 

- **Restricted-stock method** is most defensible in tax and legal contexts because it has decades of precedent and case-law support. Courts are familiar with it. However, it may understate DLOM for true private company illiquidity.

- **Pre-IPO method** is most credible when comparable transactions exist and the company is genuinely near an exit. It is less useful for mature private companies with no near-term IPO or acquisition plan.

- **Put-option model** is most rigorous and accounts explicitly for volatility and time. It is gaining ground with academic valuers and sophisticated practitioners. However, it is sensitive to volatility assumptions and courts are less accustomed to seeing it as a primary method.

A common practice is to calculate all three, note the range, and select a DLOM within that range based on the facts of the case. If the company is a late-stage venture, pre-IPO comps might be weighted 50%, put-option 30%, restricted-stock 20%. If it is a private equity add-on acquisition, restricted-stock and put-option might dominate.

## Common Pitfalls

**Forgetting control premiums and discounts.** DLOM applies to lack of marketability, not lack of control. A controlling stake in a private company should not be discounted for illiquidity as heavily as a minority stake. The controlling shareholder can force a sale, dividend, or recapitalization, creating optionality. A minority holder cannot.

**Overstating time-to-exit.** Analysts often assume 7–10 year holding periods for private companies. In reality, exit may come sooner (acquisition, secondary sale, dividend recapitalization) or never (family offices, private firms with perpetual ownership). Overestimating time-to-exit inflates the put-option DLOM artificially.

**Ignoring company-specific factors.** Restricted-stock studies use averages across many companies. A private company with a single customer, no diversification, or key-person risk may face a higher DLOM than the historical average. Conversely, a private company backed by a strong sponsor or with a clear exit path may deserve a lower discount.

**Conflating DLOM with early-stage venture discount.** A pre-seed startup is not illiquid in the same way a mature private company is. Early-stage companies often face much larger discounts to reflect execution risk, dilution from future rounds, and the high probability of failure. That is a different discount (sometimes called a [valuation](/dlom-calculation-methods-compared/) risk discount) and should not be conflated with DLOM.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — base fair value before applying DLOM
- [Black Scholes Model](/black-scholes-model/) — option pricing used in put-option models
- [Private Equity Fund](/private-equity-fund/) — typical investors and exits in private companies
- [Price to Earnings Ratio](/price-to-earnings-ratio/) — alternative valuation approach
- [Fair Value](/fair-value/) — concepts in business valuation

### Wider context

- [Estate Tax](/estate-tax/) — where DLOM is often applied for tax planning
- [Acquisition](/acquisition/) — typical exit events that trigger liquidity
- [Merger](/merger/) — another path to liquidity for illiquid shareholders
- [Return on Equity](/return-on-equity/) — profitability metrics underlying valuations

</div>

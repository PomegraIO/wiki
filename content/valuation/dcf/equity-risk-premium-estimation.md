---
title: "Equity Risk Premium Estimation"
description: "Methods for deriving the market risk premium—the expected return of stocks above the risk-free rate—that feeds into DCF discount rates."
keywords:
  - equity risk premium
  - market risk premium
  - cost of equity
  - dcf valuation
  - risk-free rate
  - capm
image: /svg/valuation.svg
---

*The **equity risk premium** is the extra return investors expect from holding stocks instead of government bonds. It is central to [DCF valuation](/discounted-cash-flow-valuation/): the higher the equity risk premium, the higher the discount rate, and the lower the valuation. Yet no one agrees on its true value.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Equity Risk Premium — the market's required extra return</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation and finance mechanics." />

<div class="wiki-infobox-caption">The spread over risk-free rates that compensates investors for bearing equity volatility and uncertainty.</div>

|   |   |
|---|---|
| **What it is** | Expected return of the equity market minus the risk-free rate |
| **Also called** | Market risk premium, equity premium, stock premium |
| **Historical average (US)** | 5–7% annually over long periods |
| **Forward-looking estimate range** | 3–6% depending on method and macro conditions |
| **Used in** | [Cost of equity](/cost-of-equity/) via CAPM, WACC |
| **Sensitivity** | A 1% change in the premium swings valuations by 10–20% |

</aside>

## Why the equity risk premium matters

In the [capital asset pricing model](/capital-asset-pricing-model/) (CAPM), the cost of equity is:

> Cost of Equity = Risk-Free Rate + β × Equity Risk Premium

If the risk-free rate is 2%, the company's beta is 1.2, and the equity risk premium is 5%, the cost of equity is 2% + 1.2 × 5% = 8%.

Change the equity risk premium to 6%, and cost of equity becomes 9.2%. That 120-basis-point swing cuts the terminal value of a mature company by 10–15% or more. Equity risk premium estimation is not a technical nicety—it shapes the core valuation.

Yet the premium is unobservable. We cannot ask the market what it expects. We must infer it from historical data, forward-looking signals, or both. And across those methods, estimates diverge.

## Historical equity risk premium

The most straightforward approach: look at actual stock returns going back to 1926 (or whenever reliable data begins), subtract the actual return on Treasury bonds, and average the spread.

Over the long US history (roughly 100 years), equities have returned about 10% annually while Treasury bonds returned 5–6%. The historical equity risk premium is thus 4–5%. But the details matter enormously:

- **Start date**: If you begin in 1982 (when inflation was crashing and bonds were rich), your premiums are inflated. Begin in 2000 (peak of the tech bubble) and they shrink.
- **End date**: A 20-year trailing average is lower than a 50-year average.
- **Survivorship bias**: US equities have been among the best-performing markets globally. A global historical average is lower.
- **Inflation adjustment**: Do you use real (inflation-adjusted) returns or nominal? Real premiums are 2–3% lower.

Academic consensus on long-run US historical equity risk premium: **4–6%**, with 5% as a rough midpoint.

## Forward-looking equity risk premium

Historical premiums may not predict future returns. If equity valuations are extremely high (high P/E ratios, low dividend yields), future returns could be lower, implying a lower forward-looking premium. If valuations are depressed, the opposite holds.

One method: the **dividend discount model**. If you assume all long-term stock returns come from dividend yield and earnings growth, you can infer the required premium:

> Expected Return = Current Dividend Yield + Expected Earnings Growth Rate

Subtract the current Treasury yield, and you have an implied equity risk premium.

For example: S&P 500 dividend yield is 1.8%, long-term earnings growth is expected at 4%, risk-free rate is 2.5%. Implied expected equity return is 1.8% + 4% = 5.8%. Equity risk premium is 5.8% − 2.5% = 3.3%.

This method is sensitive to growth assumptions and current valuation levels, making it noisier than historical averages. But it incorporates forward-looking information.

Another approach: the **implied premium from bond spreads**. If corporate bond spreads have widened (reflecting higher risk), equity risk premiums often rise in tandem. Similarly, if VIX volatility (a measure of stock-market uncertainty) spikes, investors demand higher equity premiums.

## The Damodaran approach: bottom-up and top-down

Aswath Damodaran, a prominent valuation professor, publishes estimates of equity risk premiums by country. His methodology combines:

1. **Historical equity risk premium** for the country (or the US as a proxy for developed markets).
2. **Country risk premium** (the extra spread demanded for political or currency risk).
3. **Volatility scaling** (if the country's equity market is more volatile than global stocks, adjust upward).

For the US, he typically estimates a forward-looking equity risk premium of 4.5–5.5%. For emerging markets, he adds the country risk premium separately, as discussed in [Country Risk Premium in DCF](/country-risk-premium-dcf/).

## Consensus, survey, and practitioner estimates

The Financial Analyst Federation and other professional bodies survey practitioners annually. Current consensus (as of recent years): equity risk premium for the US is 4.5–5.5%, down from 6–7% a decade ago, reflecting higher current valuations and lower inflation expectations.

Academic papers vary widely. A 2021 survey found estimates ranging from 2% to 7%, with a mean of 4–5%. The wide dispersion reflects genuine uncertainty.

Many practitioners settle on a "round number" like 5% or 6%, acknowledging that precision is illusory. The choice often depends on the analyst's macro view: if you believe markets are overvalued, use a lower premium (and lower valuations); if you believe they are undervalued, use a higher premium.

## Adjusting equity risk premium for firm size and leverage

The **CAPM beta** captures systematic risk, but the equity risk premium itself is a market-wide number. However, not all companies have beta of 1.0. Large-cap stocks (beta < 1) are less risky than the market; small-cap stocks (beta > 1) are riskier.

Some practitioners adjust the equity risk premium by company type:

- **Small-cap premium**: Add 1–2% to the base equity risk premium for small-cap companies.
- **Illiquidity premium**: Add 1–3% for private or thinly traded companies.

These adjustments are debated. CAPM would say the beta already reflects these differences; adding a separate premium double-counts risk. But empirically, small-cap and illiquid stocks have earned higher long-term returns than CAPM would predict.

## Sensitivity and best practice

Because equity risk premium is so consequential, always run a **sensitivity table**. Show how valuation changes across a range of premiums (e.g., 3%, 4%, 5%, 6%, 7%). This forces readers to understand the uncertainty.

In a formal DCF:

1. State your chosen equity risk premium explicitly (e.g., "5.0%, based on historical US average").
2. Document the source (academic consensus, your own calculation, practitioner survey).
3. Run sensitivity to premiums ±100 basis points or more.
4. If your valuation is highly sensitive to the premium (common for mature, low-growth companies), note the risk.

For a company with cash flows extending 10+ years, a 100-basis-point change in the equity risk premium can swing the terminal value by $10 billion or more.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost of equity](/cost-of-equity/) — the discount rate that embeds the equity risk premium
- [Capital asset pricing model](/capital-asset-pricing-model/) — the framework that uses equity risk premium in the cost-of-equity formula
- [Beta](/beta/) — systematic risk relative to the market, scaled by the equity risk premium
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — the valuation method that directly uses cost of equity
- Weighted average cost of capital — the blended discount rate that combines equity and debt cost, with equity risk premium as a component
- [Country risk premium](/country-risk-premium-dcf/) — a supplement to equity risk premium for emerging markets

### Wider context

- [Risk-free rate](/risk-free-rate/) — the baseline return, from which the premium is spread
- Valuation — the broader discipline
- Volatility — equity price uncertainty, correlated with equity risk premium
- [Dividend yield](/dividend-yield/) — one signal of forward-looking equity returns

</div>

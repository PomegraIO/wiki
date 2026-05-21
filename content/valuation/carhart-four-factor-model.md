---
title: "Carhart Four-Factor Model"
description: "An extension of the Fama-French three-factor model that adds momentum as a fourth factor for estimating cost of equity."
keywords:
  - Carhart four-factor
  - momentum factor
  - cost of equity
  - multi-factor model
  - valuation
image: "/svg/valuation.svg"
---

*The **Carhart four-factor model** extends the [Fama-French three-factor model](/fama-french-three-factor-model) by adding a momentum factor. It says that cost of equity depends on market risk ([beta](/beta)), size, value characteristics, and momentum—the tendency of stocks that have recently outperformed to continue outperforming. For practitioners valuing stocks with strong or weak recent performance, the addition of momentum can refine cost-of-equity estimates.*

## The four factors

**Market factor.** Beta. How the stock moves with the market. Same as CAPM and Fama-French.

**Size factor.** Small-cap premium. Small-cap stocks earn more than large-cap stocks, after adjusting for market risk.

**Value factor.** Value premium. Cheap stocks (high book-to-market, low price-to-earnings) earn more than expensive stocks, after adjusting for market risk.

**Momentum factor.** Stocks that have outperformed over the past 3–12 months tend to continue outperforming. Conversely, stocks that have underperformed tend to continue underperforming.

## The formula

Cost of equity = Risk-free rate + (Beta × Market risk premium) + (Size loading × Size premium) + (Value loading × Value premium) + (Momentum loading × Momentum premium)

The momentum premium is typically 5–10% annually, representing the excess return of high-momentum stocks over low-momentum stocks, adjusted for the other factors.

## Why momentum matters

**Empirical fact.** Stocks with strong recent performance continue to outperform, on average, for 3–12 months. This is not explained by risk alone; it appears to be a behavioral phenomenon or a market microstructure effect.

**Cost of equity implication.** A stock with strong momentum (recently outperformed) might have a lower required return than fundamentals alone would suggest, or a higher required return if you believe the momentum will reverse.

**Valuation impact.** If a stock has strong momentum and you use Carhart to estimate cost of equity, momentum reduces the required return (because momentum stocks earn less "excess" return—their price already reflects the momentum). Conversely, a stock with negative momentum has a higher required return.

## Challenges

**Momentum is transient.** Unlike value (which has persisted for decades), momentum is a short-term effect. Using it in a perpetual DCF is questionable; momentum is more relevant for short-term trading.

**Reversal risk.** Strong momentum often precedes reversal. A high-momentum stock might underperform sharply if sentiment shifts. If you use low cost of equity (due to positive momentum), you are undervaluing the reversal risk.

**Defining the momentum period.** Is it the past 3 months? 6? 12? Different periods yield different momentum signals.

**Measurement challenges.** Calculating momentum loading for a stock requires regression, and the resulting estimates are noisier than other factors.

## When Carhart is useful

**Short-to-medium term valuations.** If you are valuing a stock for a 2–5 year horizon and momentum is strong, adjusting cost of equity for momentum makes sense.

**Identifying reversals.** If a stock has strong negative momentum and a low fundamental valuation, it might be a buy (value + reversal upside).

**Portfolio construction.** Institutional investors sometimes use Carhart to manage portfolio risk, adjusting for momentum as part of multi-factor risk models.

## When Carhart is problematic

**Long-term valuation.** DCF models value perpetuity. Momentum effects over 10+ years are uncertain. Using momentum in perpetual valuation is speculative.

**Fundamental shifts.** If a company is in the midst of structural change (disruption, transformation), momentum from the old regime is misleading.

**Market extremes.** In the 2008 financial crisis or 2020 pandemic crash, momentum reversed sharply. Past momentum was a poor guide to future risk.

## Carhart in practice

Most practitioners do not use Carhart in valuation. CAPM or Fama-French three-factor is standard. Carhart is more common in:

1. **Hedge funds and active managers** using momentum trading strategies.
2. **Risk model and portfolio management** for institutional investors.
3. **Academic research** on market anomalies.

For corporate valuation and equity research, Carhart is rarely employed. If momentum is very strong (stock up 100% in a year), analysts might note the risk of reversal but would not typically adjust DCF cost of equity.

## Reconciling momentum with fundamentals

If a stock has strong momentum but weak fundamentals (low earnings growth, declining margins), what should you do?

**Option 1:** Use standard Fama-French or CAPM, ignore momentum. Value based on fundamentals alone.

**Option 2:** Use Carhart with momentum factor. Cost of equity is lower due to momentum. But acknowledge that momentum is transient and could reverse.

**Option 3:** Use scenario valuation. Base case assumes momentum continues briefly then reverses. Bull case assumes it continues longer. Bear case assumes immediate reversal.

## Momentum and value

There is often tension between value and momentum. A deeply undervalued stock might have negative momentum (it has fallen sharply). Using Carhart would assign a *higher* required return to the undervalued stock due to negative momentum, offsetting the value advantage.

This can be problematic: the most distressed, deeply-discounted stocks (greatest bargains) are assigned high required returns due to negative momentum, making them appear less attractive.

For value investors, Carhart is less useful than Fama-French alone.

## See also

<div class="wiki-seealso">

### Closely related

- [Fama-French three-factor model](/fama-french-three-factor-model) — the base model
- [Capital asset pricing model](/capital-asset-pricing-model) — the original model
- [Cost of equity](/cost-of-equity) — what this estimates
- Momentum — the fourth factor

### Valuation application

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses cost of equity
- [Weighted average cost of capital](/weighted-average-cost-of-capital) — incorporates cost of equity

### Related concepts

- [Arbitrage pricing theory](/arbitrage-pricing-theory) — multi-factor alternative
- [Fama-French five-factor model](/fama-french-five-factor-model) — further extension

### Trading and portfolio

- Technical analysis — momentum is related
- Market efficiency — momentum challenges this

</div>

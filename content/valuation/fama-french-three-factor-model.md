---
title: "Fama-French Three-Factor Model"
description: "An extension of CAPM that estimates cost of equity using market risk, company size, and value characteristics in addition to beta."
keywords:
  - Fama-French
  - three-factor model
  - cost of equity
  - size premium
  - value premium
image: "/svg/valuation.svg"
---

*The **Fama-French three-factor model** extends the [capital asset pricing model](/capital-asset-pricing-model) by adding two additional factors beyond market risk. It says that cost of equity depends not just on how a stock moves with the overall market, but also on its size (small stocks return more) and its value characteristics (cheap stocks return more). For many investors, it is a more accurate cost-of-equity estimator than basic CAPM.*

## The three factors

**Market factor (beta).** How much the stock moves with the overall market. This is the same beta from CAPM. A company with beta of 1.2 moves 20% more than the market.

**Size factor.** Small-cap stocks have historically outperformed large-cap stocks after adjusting for market risk. This is the size premium. A stock with a market cap of 100 million might earn an extra 3–5% per year relative to a large-cap stock with the same market beta.

**Value factor.** Cheap stocks (measured by book-to-market ratio, or low price-to-earnings or price-to-book) have historically outperformed expensive stocks. This is the value premium. A stock trading at 8x earnings might earn an extra 2–4% per year relative to a stock trading at 25x earnings with the same market beta and size.

## The formula

Cost of equity = Risk-free rate + (Beta × Market risk premium) + (Size factor loading × Size premium) + (Value factor loading × Value premium)

Instead of a single beta, you now have three factor loadings (how exposed the stock is to each factor) and three premiums. Estimating the factor loadings requires regression or can be approximated using simple rules (e.g., a small-cap value stock has high loadings on both size and value factors).

In practice, the size premium is 2–4% and the value premium is 2–5%, though these vary by market and time period.

## Why Fama-French works

Academic research in the 1990s showed that raw CAPM leaves money on the table. If you build a portfolio of small-cap value stocks, you will earn more than CAPM predicts, even after adjusting for risk. This suggests CAPM is missing something.

Fama and French's explanation: size and value are risk factors. Small companies are riskier (they have less capital, less market power, higher failure rates). Value stocks are riskier (they are unpopular for a reason; they may be cheap because investors fear they will get worse). Investors demand extra return for these risks.

The empirical evidence supports this. Over long periods, small stocks and value stocks do outperform, and the premiums are sizable enough to matter in valuation.

## Estimating factor loadings

For a given stock, you can look up its market cap (size is easy) and its book-to-market ratio (value characteristic). This tells you roughly how much exposure the stock has to each factor.

Alternatively, you can run a three-factor regression. Plot the stock's returns against three factors: the overall market return, a portfolio of small-cap stocks versus large-cap stocks, and a portfolio of value stocks versus growth stocks. The regression gives you the factor loadings.

Data on these factor returns is available from Ken French's data library (Dartmouth), which is the academic standard.

## Practical implications for valuation

Using Fama-French instead of CAPM often raises cost of equity slightly, especially for small-cap or value stocks. A small-cap value stock might have:

CAPM cost of equity: 4% (risk-free) + 1.2×6% (market) = 11.2%

Fama-French cost of equity: 4% + 1.2×6% + 1.0×3% (size) + 1.0×3% (value) = 17.2%

That 6 percentage point difference swings valuation substantially. Whether to use CAPM or Fama-French is therefore a material choice.

## When Fama-French is worth the complexity

**For small-cap stocks.** Small stocks are often valued using CAPM, which understates required return. Adding a size premium is more realistic.

**For value stocks.** A stock trading at 7x earnings deserves a higher cost of equity than CAPM alone would suggest.

**For academic or institutional work.** Many institutional investors (endowments, pension funds) use Fama-French. If you are selling a valuation to them, using their factor model builds credibility.

## When CAPM is sufficient

**For large-cap growth stocks.** The size and value premiums are small for mega-cap tech companies. CAPM is often sufficient.

**For simplicity.** If you are not an expert in factor models, CAPM is transparent and defensible.

**For business valuations in practice.** Most investment bankers and many practitioners use CAPM, not Fama-French. It is the market standard.

## Critiques and limitations

**The value premium has faded.** In the 2010s, value stocks underperformed significantly. This has led some to question whether the premium is real or a statistical artifact.

**The factors may not be risk factors.** Behavioral finance suggests that small and value stocks outperform because of investor bias, not because they are riskier. If so, paying for a size or value premium is unnecessary.

**Data mining concerns.** Once Fama-French published their factors, a large industry of factor researchers emerged, finding more and more factors. Eventually, enough factors can "explain" anything in the data. Which factors are real and which are noise?

**Geographic variation.** Size and value premiums vary significantly across countries. Using US-based premiums for a foreign company may be inappropriate.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital asset pricing model](/capital-asset-pricing-model) — the base model
- [Cost of equity](/cost-of-equity) — what this estimates
- [Beta](/beta) — one of three factors
- [Market risk premium](/market-risk-premium) — the market factor premium
- [Equity risk premium](/equity-risk-premium) — related premium concept

### Extensions

- [Carhart four-factor model](/carhart-four-factor-model) — adds momentum
- [Fama-French five-factor model](/fama-french-five-factor-model) — adds profitability and investment
- [Arbitrage pricing theory](/arbitrage-pricing-theory) — multifactor alternative

### Alternatives

- [Build-up method cost of equity](/build-up-method-cost-of-equity) — additive approach
- [Dividend discount model](/dividend-discount-model) — implied return approach

### Valuation application

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — uses cost of equity
- [Weighted average cost of capital](/weighted-average-cost-of-capital) — incorporates cost of equity
- [Sensitivity analysis](/sensitivity-analysis-valuation) — testing different cost-of-equity estimates

</div>

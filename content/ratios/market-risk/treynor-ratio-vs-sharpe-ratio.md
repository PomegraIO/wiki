---
title: "Treynor Ratio vs Sharpe Ratio"
description: "Compare Treynor ratio (excess return per systematic risk) and Sharpe ratio (excess return per total volatility) to understand when each applies."
keywords:
  - treynor ratio vs sharpe ratio
  - risk-adjusted return measures
  - systematic vs total risk
  - portfolio performance evaluation
  - beta denominator
  - volatility comparison
---

*The **Treynor ratio** and **Sharpe ratio** both measure excess return relative to risk, but they divide by different risk types: Treynor uses beta (systematic risk only), while Sharpe uses total volatility. The choice depends on whether your portfolio is diversified and whether you care about market-relative performance or absolute risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Two Risk-Adjusted Metrics — Key Facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">Sharpe suits standalone portfolios; Treynor suits market-benchmarked evaluation within a larger context.</div>

|   |   |
|---|---|
| **Treynor denominator** | [Beta](/beta/) (systematic risk only) |
| **Sharpe denominator** | Standard deviation (total volatility) |
| **Treynor use case** | Comparing funds or strategies that are part of a diversified portfolio |
| **Sharpe use case** | Evaluating standalone portfolios or comparing absolute risk |
| **Formula (Treynor)** | (Return − Risk-free rate) / Beta |
| **Formula (Sharpe)** | (Return − Risk-free rate) / Standard deviation |
| **Nonsensical scenario** | Sharpe on a pure [systematic-risk](/beta/) position; Treynor on a single stock |

</aside>

## The Denominator Divide

The fundamental difference is what goes in the denominator. **Treynor ratio** divides excess return by beta, capturing only the sensitivity to market movements. **Sharpe ratio** divides excess return by total volatility—standard deviation—which includes both market risk and idiosyncratic (company-specific) risk.

This matters because it changes the story. A stock with high idiosyncratic risk (e.g., a small biotech firm with volatile earnings) will have a low Sharpe ratio but could have a reasonable Treynor ratio if its beta is modest. Conversely, a bond fund moving in lockstep with interest rates will have high beta relative to stocks, making its Treynor ratio look worse than its Sharpe.

## When Beta Is the Right Denominator

Use Treynor when you're evaluating an investment or strategy that sits *inside* a larger, well-diversified portfolio. In that context, idiosyncratic risk gets diversified away. What matters is how much the position amplifies or dampens swings in the overall market. A fund manager whose stock picks correlate tightly with the S&P 500 (high beta) needs to deliver high excess returns to justify that systematic risk, even if the individual holdings are volatile. Treynor asks: "Did this manager get paid for the market risk they took?"

This is why pension funds and institutional investors often use Treynor to compare mutual fund or hedge fund managers—they assume the fund is one piece of a much larger allocation.

## When Total Volatility Is the Right Denominator

Use Sharpe when evaluating a **standalone portfolio or your entire wealth**. If you're assessing whether a fund is worth holding as your primary equity position, or comparing two competing investments with no other context, Sharpe tells you the bang for your buck in absolute terms. It asks: "Per unit of risk I actually face, how much return did I get?"

Sharpe is also the better metric if you're comparing across asset classes (stocks, bonds, real estate) because it captures total volatility regardless of the mix. Beta, by contrast, is usually defined relative to a single index (e.g., S&P 500), making cross-asset comparisons awkward.

## A Worked Example

Suppose you're comparing two equity funds:

- **Fund A**: 12% annual return, 16% standard deviation, 0.8 beta, 3% risk-free rate  
- **Fund B**: 10% annual return, 12% standard deviation, 1.1 beta, 3% risk-free rate

**Sharpe ratios:**
- Fund A: (12 − 3) / 16 = 0.56  
- Fund B: (10 − 3) / 12 = 0.58

**Treynor ratios** (assuming excess return in percent, beta unitless):
- Fund A: (12 − 3) / 0.8 = 11.25  
- Fund B: (10 − 3) / 1.1 = 6.36

Fund B wins on Sharpe (lower total volatility per return unit). Fund A wins on Treynor (lower systematic risk per return unit). If you're holding Fund B as a standalone, Sharpe suggests it's better. If you're holding it as part of a diversified portfolio and concerned about how much market exposure it brings, Treynor suggests Fund A is more efficient.

## The Negative Beta Problem

One edge case: if an investment has negative beta (moves opposite the market), Treynor can become negative or misleading even if the Sharpe ratio is positive. A market-neutral fund or put option might have strong positive returns but negative beta, flipping the Treynor calculation. In this scenario, Sharpe is far cleaner.

## Small Portfolios and Idiosyncratic Risk

If you hold only five stocks, you haven't diversified away idiosyncratic risk. Ignoring it (as Treynor does) would misrepresent your actual risk. Sharpe, capturing total volatility, gives you the honest picture. Treynor works best when you can confidently assume the holder has a diversified base.

## Regulatory and Industry Practice

[Regulators](/securities-and-exchange-commission/) and institutional frameworks tend to favor Sharpe for reported performance metrics because it's more transparent to retail and less reliant on market index assumptions. However, hedge funds and private equity funds sometimes report Treynor or modified versions to emphasize their systematic risk efficiency.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — measures a security's sensitivity to market returns
- [Volatility](/historical-volatility/) — total price fluctuation; the denominator in Sharpe
- [Sharpe Ratio](/sharpe-ratio/) — excess return per unit of total risk
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — foundation for understanding beta and systematic risk
- [Alpha](/alpha/) — excess return; the numerator in both ratios
- [Standard Deviation](/historical-volatility/) — statistical measure of price swings

### Wider context

- [Risk-Adjusted Return](/sharpe-ratio/) — broader category of performance metrics
- [Portfolio Performance Evaluation](/sharpe-ratio/) — framework for assessing fund managers
- [Idiosyncratic Risk](/idiosyncratic-risk/) — company-specific volatility not captured by beta

</div>

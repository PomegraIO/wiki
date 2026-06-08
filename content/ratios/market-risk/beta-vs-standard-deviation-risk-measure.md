---
title: "Beta vs Standard Deviation as Risk Measures"
description: "Understand when to use beta (systematic risk vs benchmark) versus standard deviation (total volatility) in portfolio evaluation."
keywords:
  - beta vs standard deviation risk measure
  - systematic risk vs total volatility
  - portfolio risk evaluation
  - benchmark-relative performance
  - diversified portfolio risk
  - concentrated position risk
image: "/svg/ratios.svg"
---

*When evaluating an investment's risk, **beta** and **standard deviation** measure fundamentally different things. Beta measures systematic risk—how much a holding moves relative to its benchmark—while standard deviation captures total volatility from all sources. Which one matters depends on whether your wealth is concentrated in that single investment or spread across many holdings.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Beta vs Standard Deviation — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two risk measures suited to different portfolio structures and questions.</div>

|   |   |
|---|---|
| **Beta** | Systematic risk; asset's sensitivity to benchmark movements |
| **Standard deviation** | Total volatility; spread of returns around the mean |
| **Best for diversified portfolios** | Beta; unsystematic risk is eliminated by diversification |
| **Best for concentrated holdings** | Standard deviation; captures all risks the owner actually faces |
| **Benchmark dependence** | Beta requires a specified benchmark; standard deviation is absolute |
| **Correlation with return** | High standard deviation doesn't guarantee high return; neither does high beta |

</aside>

## The core distinction: systematic vs total risk

**Beta** measures *systematic risk*—the portion of an investment's volatility that moves in tandem with a broad market index or other benchmark. If a stock has a beta of 1.2 relative to the S&P 500, it swings 20% more than the index moves, up or down.

**Standard deviation** is statistical; it measures how far returns typically scatter around their average. A fund with 15% standard deviation means most returns fall within about 15 percentage points of its mean annual return.

The key insight: a stock can have high beta (moves a lot relative to the market) yet low standard deviation if its idiosyncratic volatility—the noise specific to that company—is minimal. Conversely, a stock with low beta can have high standard deviation if its firm-specific shocks create noise independent of the market.

## Why diversification changes which metric matters

If you hold a single stock or a small concentrated portfolio, you face both systematic and idiosyncratic risk. Standard deviation captures everything: broad market swings plus the stock-specific surprises that could tank your position. In this case, standard deviation is more relevant to *your actual risk* because you cannot diversify away idiosyncratic shocks.

If you hold a large diversified portfolio—say, a mutual fund tracking the S&P 500 or a 200-stock equity allocation—the idiosyncratic risks of individual holdings largely cancel out. What remains is systematic risk: the correlation of your portfolio with the market itself. Here, beta becomes the more useful gauge. Your portfolio's volatility is then driven almost entirely by how much market movement you've chosen to capture.

This is the logic behind modern portfolio theory. In a well-diversified portfolio, the risk that matters is not any single holding's standard deviation but its contribution to the portfolio's overall [beta](/beta/).

## Benchmark selection and the limitation of beta

Beta is meaningless without a benchmark. A stock's beta relative to the S&P 500 differs from its beta relative to the NASDAQ or a sector index. This flexibility is both beta's strength—you can choose benchmarks matched to your investment universe—and its weakness: the choice is subjective.

Standard deviation, by contrast, is absolute. A fund's 12% standard deviation describes its variability in isolation, regardless of what index you compare it to.

For investors who deviate from a standard benchmark—perhaps a hedge fund, a concentrated equity holder, or an alternative asset—beta can be unstable or misleading. Standard deviation remains legible.

## When to use each in practice

**Use beta** when:
- You hold a diversified portfolio aligned with a clear benchmark (e.g., a 60/40 stock-bond mix).
- You want to understand how much market exposure you've taken on.
- You're evaluating a [mutual fund](/mutual-fund/) or [ETF](/etf/) against its category peers.
- You're calculating [cost of equity](/cost-of-equity/) for a company valuation.

**Use standard deviation** when:
- You hold a concentrated position and want to know the full range of outcomes.
- Your holdings don't map cleanly to a single benchmark.
- You're comparing two strategies without a shared index (e.g., emerging-market debt vs. real estate).
- You want a straightforward measure of volatility that doesn't require benchmark specification.

## Worked example

Suppose two tech stocks, TechA and TechB, both tracked against the NASDAQ:
- **TechA**: 18% standard deviation, 0.9 beta. It swings less than the index but has firm-specific surprises (earnings misses, regulatory news).
- **TechB**: 20% standard deviation, 1.2 beta. It swings hard with the market but is closely correlated to tech trends.

If you own TechA as a concentrated position, its 18% standard deviation is the risk you actually bear. If you own a NASDAQ-tracking ETF, the fund's beta matters far more because individual stock noise gets diversified away.

## Reconciling the two metrics

Standard deviation and beta are not competing measures; they decompose volatility into components:

Total variance ≈ (Beta² × Benchmark variance) + Idiosyncratic variance

A stock's standard deviation reflects both its beta-driven swings and its unique shocks. Sophisticated investors use beta to understand market exposure and standard deviation to gauge absolute volatility. Comparing the two reveals how much of a security's risk is benchmark-driven versus firm-specific.

This distinction is especially important when evaluating [fund performance](/fund-prospectus/). A fund with high standard deviation and low beta is volatile but less exposed to broad market downturns. A fund with high beta but lower standard deviation moves closely with the market, with less idiosyncratic noise.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — sensitivity of a holding to benchmark movements
- [Standard deviation](/volatility-smile/) — statistical measure of return variability
- [Sharpe ratio](/sharpe-ratio/) — risk-adjusted return metric combining excess return and volatility
- [Cost of equity](/cost-of-equity/) — discount rate incorporating beta in valuation
- [Alpha](/alpha/) — excess return beyond what beta predicts
- [Diversification](/diversification/) — reducing risk through multiple holdings
- [Volatility](/volatility-smile/) — how much returns fluctuate

### Wider context

- Modern portfolio theory — framework linking risk and return
- [Market risk](/market-risk/) — broad category of systematic risk
- [Index fund](/index-fund/) — passively tracks a benchmark
- [Mutual fund](/mutual-fund/) — pooled investment vehicle
- [ETF](/etf/) — exchange-traded fund tracking an index or strategy

</div>

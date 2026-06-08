---
title: "How to Calculate Portfolio Beta with an Example"
description: "Calculate portfolio beta by weighting individual asset betas by their portfolio proportion; includes a worked numerical example."
keywords:
  - how to calculate portfolio beta
  - portfolio beta weighted average
  - beta calculation example
  - combining asset betas
  - systematic risk portfolio
  - portfolio risk measurement
image: "/svg/ratios.svg"
---

*To find a portfolio's **beta**, multiply each holding's beta by its weight in the portfolio, then sum. A portfolio that is 60% Stock A (beta 1.1) and 40% Stock B (beta 0.8) has a portfolio beta of 0.98—a single number capturing the portfolio's overall sensitivity to market moves. This article walks through the math with concrete examples.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Portfolio Beta Calculation — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Portfolio beta is the weighted average of individual asset betas.</div>

|   |   |
|---|---|
| **Formula** | Portfolio beta = Σ (Weight × Asset beta) |
| **Requirement** | Individual asset betas and portfolio weights |
| **Benchmark** | Must be specified (S&P 500, NASDAQ, etc.) |
| **Interpretation** | Portfolio beta of 1.2 = swings 20% more than the benchmark |
| **Weights** | Must sum to 1.0 (or 100%) |
| **Rebalancing** | Weights shift as prices move; recalculate periodically |
| **Time sensitivity** | Beta changes as asset betas and weights change |

</aside>

## The basic formula

Portfolio beta is straightforward:

> **Portfolio Beta = (Weight₁ × Beta₁) + (Weight₂ × Beta₂) + … + (Weightₙ × Betaₙ)**

Each weight must be expressed as a decimal (0.6 for 60%) and must sum to 1.0 across all holdings. Each beta is the individual asset's [beta](/beta/) relative to the same benchmark (usually the S&P 500 for U.S. equities).

## Worked example: a three-stock portfolio

Suppose you own three stocks with the following market values and betas (all relative to the S&P 500):

| Stock | Position | Beta |
|-------|----------|------|
| Apple | $30,000 | 1.25 |
| Walmart | $20,000 | 0.70 |
| Tesla | $50,000 | 1.80 |

**Step 1: Calculate total portfolio value**

$30,000 + $20,000 + $50,000 = $100,000

**Step 2: Calculate weight of each stock**

- Apple: $30,000 ÷ $100,000 = 0.30 (30%)
- Walmart: $20,000 ÷ $100,000 = 0.20 (20%)
- Tesla: $50,000 ÷ $100,000 = 0.50 (50%)

(Check: 0.30 + 0.20 + 0.50 = 1.00 ✓)

**Step 3: Multiply each weight by its beta**

- Apple: 0.30 × 1.25 = 0.375
- Walmart: 0.20 × 0.70 = 0.140
- Tesla: 0.50 × 1.80 = 0.900

**Step 4: Sum the products**

Portfolio beta = 0.375 + 0.140 + 0.900 = **1.415**

**Interpretation:** This portfolio swings 41.5% more than the S&P 500. If the S&P 500 rises 10%, the portfolio is expected to rise about 14.15%. If the index falls 10%, the portfolio is expected to fall about 14.15%.

## Including cash and bonds

If your portfolio contains cash or bonds, apply the same method. Cash typically has a beta near zero (it doesn't move with the market), and [bonds](/bond/) have lower betas than equities (usually between 0 and 0.5).

**Example with bonds:**

| Asset | Position | Beta |
|-------|----------|------|
| U.S. stocks (80%) | $80,000 | 1.10 |
| U.S. bonds (15%) | $15,000 | 0.20 |
| Cash (5%) | $5,000 | 0.00 |

Weights: 0.80, 0.15, 0.05 (sum = 1.00 ✓)

Portfolio beta = (0.80 × 1.10) + (0.15 × 0.20) + (0.05 × 0.00)
= 0.88 + 0.03 + 0.00
= **0.91**

This portfolio moves 91% as much as the S&P 500—less volatile because bonds and cash cushion the equity exposure.

## Using index funds or ETFs

If your holdings are index funds or [ETFs](/etf/) rather than individual stocks, use the same method. For example, a portfolio of 60% [S&P 500 index fund](/sp-500-index/) and 40% [bond ETF](/bond-etf/) would be:

Portfolio beta = (0.60 × 1.00) + (0.40 × 0.15) = 0.60 + 0.06 = **0.66**

(An S&P 500 index fund has a beta of essentially 1.0 by definition, since it *is* the index. A typical bond fund might have beta around 0.15.)

## Dynamic rebalancing: beta drift

Portfolio beta changes over time as two things happen:

1. **Asset betas change:** A company's systematic risk can increase or decrease. A stable utility might have beta 0.9 today and 1.1 after a major acquisition.

2. **Weights drift:** As prices move, the dollar value of holdings shifts, changing their percentage of the portfolio. If Tesla doubles while Walmart flatlines, Tesla's weight rises automatically, pulling the portfolio beta higher.

**Example of drift:**

Starting portfolio (from earlier): Apple 30%, Walmart 20%, Tesla 50%, portfolio beta = 1.415.

Six months later, prices have moved:
- Apple rose 15% → now worth $34,500
- Walmart rose 5% → now worth $21,000
- Tesla rose 30% → now worth $65,000
- New total: $120,500

New weights:
- Apple: $34,500 ÷ $120,500 = 0.286 (28.6%)
- Walmart: $21,000 ÷ $120,500 = 0.174 (17.4%)
- Tesla: $65,000 ÷ $120,500 = 0.540 (54.0%)

If betas remain unchanged:
New portfolio beta = (0.286 × 1.25) + (0.174 × 0.70) + (0.540 × 1.80)
= 0.358 + 0.122 + 0.972
= **1.452**

The portfolio beta rose from 1.415 to 1.452 simply because the highest-beta holding (Tesla) grew in value. This is why investors who want a stable beta rebalance periodically—selling winners and buying losers to restore original weights.

## Comparing portfolios by beta

Portfolio beta is useful for comparing risk profiles:

| Portfolio | Composition | Beta | Meaning |
|-----------|-------------|------|---------|
| Conservative | 20% stocks, 80% bonds | 0.25 | Low market sensitivity; cushioned |
| Moderate | 60% stocks, 40% bonds | 0.70 | Moderate market sensitivity |
| Aggressive | 100% stocks | 1.10 | Moves with or slightly above the market |
| Leveraged | 150% stocks, −50% cash | 1.65 | Amplified market moves; borrowed money |

A beta of 1.0 means the portfolio moves exactly like the market. Below 1.0 is more stable. Above 1.0 is more volatile. An aggressive hedge fund might have a beta of 0.3 (low correlation to markets, due to active positions), while a simple 100% U.S. stock portfolio has a beta near 1.0.

## Assumptions and limitations

Portfolio beta assumes:

- **Historical stability:** The individual betas used are based on past data and may not predict future sensitivity.
- **Benchmark consistency:** All betas are calculated against the same benchmark.
- **Linear relationship:** Beta assumes the relationship between a stock and the market is linear. In extreme market crashes, this breaks down.
- **No leverage:** The calculation ignores borrowing. A leveraged portfolio needs an adjusted method.

For a leveraged portfolio (using [margin](/margin-call-forex/) or derivatives), multiply the unlevered beta by the leverage ratio. If you use $150,000 of stocks with $100,000 of capital (1.5× leverage), and the stock portfolio's beta is 1.0, the leveraged portfolio beta is 1.5.

## Quarterly recalculation

Professional portfolio managers recalculate beta quarterly or whenever allocations shift materially. As individual asset betas change (companies' [volatility](/volatility-smile/) and correlation with markets shifts), and as weights drift due to price moves, the portfolio beta evolves.

This is especially important for [mutual funds](/mutual-fund/) and [hedge funds](/hedge-fund/), which publish beta in their fact sheets. Investors rely on these figures to understand how much market risk they're taking on relative to the [risk-free rate](/risk-free-rate/) or their own tolerance.

## Practical use: calculating required return

Portfolio beta feeds into the [capital asset pricing model](/capital-asset-pricing-model/) (CAPM), which calculates the return an investor should demand:

> Expected return = Risk-free rate + (Beta × Market risk premium)

If risk-free rate = 3%, market risk premium = 6%, and portfolio beta = 1.2:

Expected return = 3% + (1.2 × 6%) = 3% + 7.2% = **10.2%**

The portfolio's higher beta (1.2 vs. 1.0) justifies demanding a higher return (10.2% vs. 9%). This calculation is central to [cost of equity](/cost-of-equity/) estimation and portfolio performance evaluation.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — individual asset sensitivity to a benchmark
- [Sharpe ratio](/sharpe-ratio/) — risk-adjusted return using beta and volatility
- [Sharpe ratio vs Sortino ratio](/sharpe-ratio-vs-sortino-ratio-difference/) — alternative risk-adjusted metrics
- [Alpha](/alpha/) — outperformance relative to the [CAPM](/capital-asset-pricing-model/)
- [Standard deviation](/volatility-smile/) — total volatility of portfolio returns
- [Beta vs standard deviation](/beta-vs-standard-deviation-risk-measure/) — systematic vs. total risk
- [Capital asset pricing model](/capital-asset-pricing-model/) — framework linking beta to expected return

### Wider context

- [Cost of equity](/cost-of-equity/) — discount rate for valuation
- [Asset allocation](/asset-allocation/) — portfolio construction process
- Rebalancing — maintaining target weights
- [Leverage](/leverage-ratio-forex/) — borrowing to amplify returns and risk
- [Market risk](/market-risk/) — broad category of systematic risk
- [ETF](/etf/) — exchange-traded fund for easy diversification

</div>

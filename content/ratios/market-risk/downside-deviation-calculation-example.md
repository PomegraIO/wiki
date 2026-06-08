---
title: "Downside Deviation: Calculation with an Example"
description: "Downside deviation measures volatility of returns below a threshold, commonly used in the Sortino ratio. Learn the formula and calculation step-by-step."
keywords:
  - how to calculate downside deviation
  - downside deviation formula
  - sortino ratio denominator
  - downside risk measurement
  - semi-deviation calculation
image: /svg/ratios.svg
---

***Downside deviation** is a risk measure that counts only returns below a minimum acceptable threshold—typically zero or the risk-free rate. Unlike standard [historical-volatility](/historical-volatility/), which penalizes both gains and losses equally, downside deviation ignores upside moves and focuses on the volatility of disappointing returns. It appears in the denominator of the [sharpe-ratio](/sharpe-ratio/) alternative, the Sortino ratio.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Downside Deviation — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Volatility that matters: how far below your threshold do returns actually fall?</div>

|   |   |
|---|---|
| **Formula** | Square root of average squared shortfalls below threshold |
| **Threshold** | Usually 0% or the risk-free rate (e.g., 2% annually) |
| **Denominator in** | Sortino ratio; higher values lower the ratio |
| **Data needed** | Series of periodic returns (daily, monthly, or annual) |
| **Upside** | Ignores volatility above threshold; better for loss-averse investors |
| **Downside** | Requires choosing a meaningful threshold; can hide tail risk |
| **Typical range** | Usually 3–15% for diversified portfolios (much lower than overall volatility) |

</aside>

## Why downside deviation differs from standard volatility

Standard [historical-volatility](/historical-volatility/) (standard deviation) treats a +10% month and a –10% month identically—both contribute equally to the dispersion around the mean return. But an investor cares far more about the –10% month. A portfolio that rises 15% in half its months and falls 5% in the other half has the same standard deviation as one that rises 10% in half and falls 0% in the other—yet the second portfolio is clearly preferable.

Downside deviation zeroes in on the pain. It ignores big-up months and calculates volatility only from the bad ones. This makes it a more intuitive risk measure for people who think about "How often do I lose money?" rather than "How much does my portfolio bounce around?"

## The formula

The standard formula for downside deviation using a threshold (often called the Minimum Acceptable Return, or MAR) is:

```
Downside Deviation = √[ Σ(max(0, MAR − Rᵢ))² / n ]
```

Where:
- **Rᵢ** = return in period i
- **MAR** = minimum acceptable return (often 0% or the risk-free rate)
- **max(0, MAR − Rᵢ)** = shortfall; zero if return meets or exceeds MAR, otherwise the gap
- **n** = number of periods
- **Σ** = sum across all periods

In words: For each period, if the return falls short of your threshold, square the gap. Average those squared shortfalls across all periods (including periods with no shortfall, where the gap is zero). Take the square root.

If you use a 0% MAR (no loss is acceptable), the formula becomes simple: sum the squares of negative returns, divide by the count, and take the square root.

## Worked example

Suppose an investment has the following monthly returns over one year:

| Month | Return |
|-------|--------|
| Jan | 3% |
| Feb | -1% |
| Mar | 5% |
| Apr | -3% |
| May | 2% |
| Jun | 4% |
| Jul | -2% |
| Aug | 1% |
| Sep | 6% |
| Oct | -4% |
| Nov | 2% |
| Dec | 3% |

Let's calculate downside deviation with a 0% MAR (any negative return is a shortfall).

**Step 1: Identify shortfalls**

Months with returns below 0%:
- Feb: -1% → shortfall = 1%
- Apr: -3% → shortfall = 3%
- Jul: -2% → shortfall = 2%
- Oct: -4% → shortfall = 4%

All other months have shortfalls of 0%.

**Step 2: Square the shortfalls**

- Feb: 1² = 1
- Apr: 3² = 9
- Jul: 2² = 4
- Oct: 4² = 16
- All other months: 0

**Step 3: Sum and divide by period count**

Sum of squared shortfalls = 1 + 9 + 4 + 16 = 30

Number of periods = 12

Average = 30 / 12 = 2.5

**Step 4: Take the square root**

Downside Deviation = √2.5 = 1.58%

For this portfolio with a 0% MAR, the downside deviation is 1.58%. This tells you that when the portfolio underperforms (goes negative), it does so by a magnitude averaging around 1.6 percentage points of volatility.

## Choosing your threshold

The MAR is critical. The most common choices are:

- **0%**: Treats any loss as a shortfall. Suits conservative investors or those saving for a specific goal.
- **Risk-free rate** (e.g., 2% annually, or 0.17% monthly): You care about returns above what a Treasury would give. Suits investors comparing a stock portfolio to a safe bond alternative.
- **Target return** (e.g., 5% annually): You need 5% per year to hit your retirement goal; anything below is a miss.

Using a 2% annual MAR (0.167% monthly) on the same portfolio:

Shortfalls occur whenever return < 0.167%:
- Feb: -1% → shortfall = 1.167%
- Apr: -3% → shortfall = 3.167%
- Jul: -2% → shortfall = 2.167%
- Aug: 1% → shortfall = 0.167% (1% < 0.167%? No—1% > 0.167%, so shortfall = 0)
- Oct: -4% → shortfall = 4.167%

Sum of squared shortfalls = 1.167² + 3.167² + 2.167² + 4.167² = 1.36 + 10.03 + 4.70 + 17.36 = 33.45

Average = 33.45 / 12 = 2.79

Downside Deviation = √2.79 = 1.67%

With a 2% threshold, the downside deviation is 1.67%—slightly higher, because we're now counting the 1% month as a shortfall too.

## In context: the Sortino ratio

The [sharpe-ratio](/sharpe-ratio/) divides excess return by *total* volatility. The Sortino ratio divides excess return by *downside* deviation:

```
Sortino Ratio = (Return − Risk-Free Rate) / Downside Deviation
```

If a portfolio returns 8% with a 2% risk-free rate and a downside deviation of 2%, the Sortino ratio is (8% − 2%) / 2% = 3.0. If standard deviation were 6%, the [sharpe-ratio](/sharpe-ratio/) would be (8% − 2%) / 6% = 1.0. The Sortino ratio is higher because downside deviation ignores the good days, giving more credit to a return profile with high upside and low downside.

## Limitations and complementary measures

Downside deviation ignores **tail risk**—the chance of a catastrophic loss. A portfolio that loses 50% in one month in a crash has infinite (or very large) downside deviation, but the metric doesn't distinguish that crash from steady small losses. Investors should also examine [value-at-risk](/value-at-risk/) and stress scenarios.

Also, downside deviation is backward-looking; it assumes future risk matches past shortfalls. A portfolio with a long calm history can harbor unpriced risks. And the choice of threshold is subjective—different MAR assumptions give different rankings.

Despite these caveats, downside deviation is a useful complement to [sharpe-ratio](/sharpe-ratio/) and [beta](/beta/) for investors focused on *loss volatility* rather than price bounce.

## See also

<div class="wiki-seealso">

### Closely related

- [Sharpe Ratio](/sharpe-ratio/) — Return per unit of total risk; use downside deviation for Sortino variant
- [Historical Volatility](/historical-volatility/) — Standard deviation of returns; counts up and down equally
- [Beta](/beta/) — Systematic risk relative to a market benchmark
- [Value at Risk](/value-at-risk/) — Maximum expected loss at a confidence level; complements downside deviation

### Wider context

- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — Framework for expected return and risk
- [Risk Weighted Assets](/risk-weighted-assets/) — Bank capital regulation; uses loss-focused risk concepts
- [Volatility Smile](/volatility-smile/) — Options market view of tail risk

</div>

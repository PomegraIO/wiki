---
title: "Parametric VaR"
description: "Parametric value-at-risk (parametric VaR) is a method of calculating value-at-risk by assuming returns follow a statistical distribution and using the distribution's parameters to estimate the loss threshold."
keywords:
  - parametric VaR
  - variance-covariance VaR
  - delta-normal VaR
  - normal distribution
  - analytical VaR
image: "https://picsum.photos/seed/parametric-var/900/600"
---

*Parametric value-at-risk (also called variance-covariance VaR or delta-normal VaR) is a method of estimating portfolio loss by assuming returns follow a known statistical distribution — typically the normal (Gaussian) distribution — and deriving the loss threshold from the distribution's mean and standard deviation.*

<div class="wiki-hatnote">

This entry covers parametric VaR calculation. For alternative VaR methods, see [historical-var](/historical-var) and [monte-carlo-var](/monte-carlo-var); for the general [value-at-risk](/value-at-risk) concept.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Parametric VaR — key facts</div>

<img src="https://picsum.photos/seed/parametric-var/900/600" alt="A bell curve distribution with a marked confidence interval on the left tail" />

<div class="wiki-infobox-caption">Parametric VaR uses the distribution's parameters to calculate the threshold.</div>

|   |   |
|---|---|
| **Method** | Assume distribution; calculate percentile from mean and std dev |
| **Assumption** | Returns follow a known distribution (usually normal) |
| **Calculation** | Z-score × standard deviation at the confidence level |
| **Speed** | Fastest method; only requires mean, std dev, correlation matrix |
| **Accuracy** | Good for thin-tailed distributions; poor for fat-tailed markets |
| **Common use** | Banks and trading desks for daily risk reporting |
| **Key weakness** | Underestimates risk in fat-tailed markets |

</aside>

## How parametric VaR works

**Step 1: Estimate parameters.**
From historical data (e.g., past 250 trading days), calculate:
- Mean daily return μ (typically close to zero, ~0.05%)
- Standard deviation σ (volatility; for stocks, ~1%)

**Step 2: Identify the confidence level.**
Say, 99% confidence (1% tail).

**Step 3: Find the z-score.**
For a normal distribution, the z-score at 99% confidence is 2.33. (This means 2.33 standard deviations below the mean captures the bottom 1%.)

**Step 4: Calculate VaR.**
VaR = μ - 2.33 × σ

For a daily portfolio return with μ = 0.05% and σ = 1%:
VaR = 0.05% - 2.33 × 1% ≈ -2.28% per day.

For a $100M portfolio, the 1-day 99% VaR is 2.28% × $100M = $2.28M.

## Advantages of parametric VaR

**Speed:** VaR is calculated in seconds using just three numbers: the mean, standard deviation, and the correlation matrix. No simulation or sorting needed.

**Simplicity:** The method is intuitive — it is just a z-score lookup. Practitioners understand it easily.

**Scalability:** For portfolios with thousands of positions, parametric VaR is fast to compute.

**Regulatory standard:** Many banks report parametric VaR for regulatory compliance.

## Disadvantages: The normality assumption

The critical weakness of parametric VaR is the assumption that returns are normally distributed. Real markets do not follow normal distributions; they have [fat tails](/fat-tail-risk).

**Example of failure:**
- Historical μ = 0.05%, σ = 1%.
- Parametric VaR at 99% = -2.28% per day.
- But the actual worst day in history was -9% (in a crash).

The actual worst 1% of days (worst 2-3 days per year) might average -4%, not -2.28%. This is because real distributions have fatter tails.

A normal distribution predicts a 1 in 100 million year event at -5% loss. Real markets see -5%+ losses roughly every 50 years. Parametric VaR is systematically too optimistic.

## When parametric VaR works

Parametric VaR is reasonable for:
- **Short time horizons (1-5 days).** Over very short periods, returns are closer to normal.
- **Liquid markets with stable conditions.** When correlations are stable and volatility is not extreme, parametric VaR is usable.
- **Thin-tailed instruments.** Interest rate changes or index returns are more normal than individual stock returns; parametric VaR is less bad for these.
- **Backtesting against recent history.** If you re-estimate parameters weekly or monthly, the distribution changes to match recent conditions, reducing model lag.

Parametric VaR fails in:
- **Crises.** When volatility spikes, correlations jump to 1, and the distribution fattens. Parametric VaR (fitted to calm periods) is way too low.
- **Long-tailed markets.** Derivatives, commodities, and emerging market assets have fat tails; parametric VaR is not reliable.
- **Non-linear positions.** Options are non-linear; the delta (linear approximation) is not enough. Parametric VaR underestimates option risk.

## Extensions and improvements

**Student-t distribution:** Instead of normal, assume a Student-t distribution, which has fatter tails. This improves estimates for markets with extreme events.

**Cornish-Fisher:** A method that adjusts the normal distribution for skewness and kurtosis. Still assumes returns follow a specific distribution, but adds correction for fat tails.

**Dynamic volatility:** Instead of assuming volatility is constant, estimate how it changes over time (GARCH models). This captures volatility clustering — periods of calm followed by turbulence.

**EWMA (exponentially weighted moving average):** Gives more weight to recent observations, making volatility estimates responsive to current conditions.

## Parametric VaR in context

Parametric VaR is fast and simple, which is why it is popular. But its simplicity comes at the cost of realism. The financial industry has learned (painfully) that parametric VaR alone is not enough.

Modern risk management uses parametric VaR as one input among many:
- Pair it with [historical-var](/historical-var) or [monte-carlo-var](/monte-carlo-var) for cross-checks.
- Complement it with [expected-shortfall](/expected-shortfall) to measure tail severity.
- Use [stress-testing](/stress-testing) and [scenario-analysis](/scenario-analysis) to explicitly explore extreme cases.

The key insight is that parametric VaR assumes a particular distribution. If that assumption is wrong (and in real markets, it is), the VaR estimate can be wildly off.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-risk](/value-at-risk) — the VaR concept itself
- [Historical-var](/historical-var) — alternative VaR method without distributional assumptions
- [Monte-carlo-var](/monte-carlo-var) — simulation-based VaR using more flexible distributions
- [Expected-shortfall](/expected-shortfall) — measures tail severity, not just threshold
- [Model-risk](/model-risk) — parametric VaR depends on model assumptions

### Methodological issues

- [Fat-tail-risk](/fat-tail-risk) — parametric VaR misses fat tails
- [Parameter-risk](/parameter-risk) — estimates of μ and σ are uncertain
- [Stress-testing](/stress-testing) — addresses parametric VaR limitations
- [Scenario-analysis](/scenario-analysis) — explicit extreme scenarios
- [Backtesting](/value-at-risk) — checks whether parametric VaR is accurate

</div>

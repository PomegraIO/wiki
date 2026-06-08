---
title: "Calmar Ratio and Drawdown-Based Risk Measurement"
description: "Define the Calmar ratio as annualized return divided by maximum drawdown. Understand its use in evaluating trend-following strategies and downside risk."
keywords:
  - calmar ratio drawdown risk
  - calmar ratio definition
  - maximum drawdown calculation
  - trend-following performance metric
  - downside risk measurement
image: "/svg/risk.svg"
---

*The **Calmar ratio** divides annualized return by the maximum drawdown—the largest percentage peak-to-trough decline over a period—to measure risk-adjusted performance. A strategy that gains 15% annually with a 30% worst drawdown scores a Calmar of 0.5; one that gains 12% with a 20% drawdown scores 0.6. Higher is better, and the metric is especially valued for evaluating [trend-following](/trend-following/) and [alternative trading](/alternative-trading-system/) strategies where downside control is as important as upside capture.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Calmar Ratio & Drawdown Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk topics." />

<div class="wiki-infobox-caption">A penalty-based metric: rewards returns, punishes the deepest valley an investor endured.</div>

|   |   |
|---|---|
| **Formula** | Annualized return ÷ Maximum drawdown (expressed as a decimal) |
| **Range** | 0 to infinity (higher is better; ratio of 1+ is strong) |
| **Use case** | Evaluating strategies with volatile equity curves (CTAs, trend-following) |
| **vs. Sharpe ratio** | Focuses on largest loss, not volatility; more relevant for drawdown-sensitive investors |
| **vs. Information ratio** | Benchmark-independent; does not require a benchmark |
| **Weakness** | Single-observation bias (one catastrophic loss inflates drawdown permanently) |

</aside>

## Why Drawdown Matters More Than Volatility for Some Investors

The [Sharpe ratio](/sharpe-ratio/) measures risk as standard deviation—the average scatter of returns around the mean. But for investors who care most about *not losing money in crisis periods*, the Sharpe ratio is incomplete. A strategy with smooth, flat returns could have zero Sharpe advantage, while a strategy with one catastrophic drawdown but rapid recovery could score poorly on Sharpe despite higher terminal wealth.

The **Calmar ratio** shifts focus to what many investors dread most: the largest *unrealized* loss from peak to trough. If a strategy compounds a portfolio from $1M to $1.3M (30% gain), but hits a low of $700K at its nadir, the maximum drawdown is 30% ($1M to $700K). That 30% loss is the denominator in the Calmar calculation, no matter how briefly it lasted.

This metric resonates with **trend-following** strategies, which can be whipsaw-prone. A trend-following CTA may capture long bull markets, but when trends reverse suddenly—a geopolitical shock, a policy reversal—drawdowns spike. The Calmar ratio captures exactly this: high annualized returns are only attractive if the worst-case drawdown is survivable.

## The Mechanics: A Worked Example

Suppose you are evaluating two trend-following strategies over a 5-year period.

**Strategy A: Commodity Trend**
- Annualized return: 12%
- Maximum drawdown: 18%
- **Calmar ratio = 12% / 18% = 0.67**

**Strategy B: FX Trend**
- Annualized return: 9%
- Maximum drawdown: 12%
- **Calmar ratio = 9% / 12% = 0.75**

Strategy B has a higher Calmar ratio *despite lower returns*, because it achieved those returns with a smaller maximum loss. An investor who can tolerate only a 15% drawdown would prefer Strategy B; one with a 25% tolerance might prefer A (if capacity or correlations favored it).

Now consider a third example:

**Strategy C: High-Conviction Trend**
- Annualized return: 18%
- Maximum drawdown: 50%
- **Calmar ratio = 18% / 50% = 0.36**

Strategy C's 50% drawdown (earning $1M becomes $500K at worst) is so severe that despite the 18% annual return, the Calmar ratio is below 0.5. Many risk-conscious investors would pass, viewing the downside as catastrophic even if the long-term payoff is high.

## How to Calculate Maximum Drawdown

The maximum drawdown is calculated from a return series (daily, weekly, or monthly):

1. Compute the cumulative value (or compounded return) at each date.
2. At each point, find the highest cumulative value seen *to date* (the running peak).
3. Subtract the current value from that peak and divide by the peak. This is the drawdown at that date.
4. The **maximum drawdown** is the worst (largest) of all these drawdowns.

Example with a simple monthly return series:

| **Month** | **Return** | **Cumulative Value** | **Running Peak** | **Drawdown** |
|---|---|---|---|---|
| Start | — | $1,000 | $1,000 | — |
| Jan | +5% | $1,050 | $1,050 | 0% |
| Feb | +3% | $1,082 | $1,082 | 0% |
| Mar | −7% | $1,006 | $1,082 | 7.0% |
| Apr | −5% | $955 | $1,082 | 11.8% |
| May | +8% | $1,031 | $1,082 | 4.7% |
| Jun | +6% | $1,093 | $1,093 | 0% |

Maximum drawdown = **11.8%** (in April, before recovery in May).

If the strategy returned 12% annualized over that 6-month period (prorated to 24% annually), the Calmar ratio = 24% / 11.8% ≈ 2.03—a strong score.

## Calmar vs. Other Risk-Adjusted Metrics

**Calmar vs. Sharpe Ratio**: The Sharpe ratio penalizes all volatility equally; the Calmar penalizes only the largest loss. A strategy with many small drawdowns and low volatility might have an excellent Sharpe but a poor Calmar if it experiences one severe valley. Conversely, a strategy with low overall volatility but one deep drawdown scores well on Calmar but poorly on Sharpe.

**Calmar vs. Information Ratio**: The Information ratio measures excess return per unit of tracking error (deviation from a benchmark). Calmar is benchmark-independent; it works for absolute-return strategies (hedge funds, CTAs) that do not track an index. This makes Calmar more useful for evaluating non-traditional strategies.

**Calmar vs. Sortino Ratio**: The Sortino ratio is similar in spirit to Calmar—it penalizes downside volatility—but it uses the standard deviation of *negative returns* rather than the single worst loss. Calmar is more extreme; it focuses entirely on the trough.

## Limitations of the Calmar Ratio

The metric has blind spots:

**Single-observation bias**: A strategy might be genuinely sound, but a one-time shock (a flash crash, a regulatory surprise) creates a drawdown that haunts the Calmar ratio for years. A 50% drawdown that lasts one month in year 1 will depress the Calmar for the entire 5-year or 10-year lookback, even if the strategy recovered and performed flawlessly thereafter.

**Backward-looking**: The worst drawdown in the past does not predict the worst drawdown in the future. A strategy that has never experienced a 40% loss in historical data might face one in the next cycle.

**Insensitive to recovery speed**: The Calmar ratio does not care whether a drawdown recovers in 3 months or 3 years. Two strategies with identical max drawdowns but vastly different recovery profiles score the same, even though one is psychologically and financially superior.

**Scale issues**: A very short observation period (1–2 years) may not capture a true maximum drawdown. Conversely, a very long period (20+ years) may blend multiple market regimes where the strategy's character changed.

## Practical Use in Allocating to Trend-Following Strategies

Institutional investors allocating to commodity trading advisors (CTAs) and [hedge funds](/hedge-fund/) commonly screen by Calmar ratio. A Calmar of 1.0 or higher is often considered strong; 0.5–0.8 is acceptable for aggressive managers; below 0.3 raises red flags.

But Calmar is not standalone. An allocator would also examine:

- **Downside correlation**: How did the strategy drawdown during equity market selloffs? (If correlated, it amplifies portfolio risk.)
- **Recovery trajectory**: How fast did it bounce back?
- **Frequency of drawdowns**: One 30% drawdown is different from six 5% drawdowns, both averaging 30%.
- **Underlying mechanism**: Is the Calmar ratio a result of robust trading logic, or luck in a benign market regime?

A strategy with a 0.8 Calmar ratio and low correlation to equities might be worth more (in portfolio terms) than a 1.2 Calmar strategy that tanks during equity crashes.

## Relationship to Other Drawdown Measures

**Conditional Drawdown at Risk (CDaR)**: Uses a percentile-based approach, asking "what is the average drawdown in the worst 10% of drawdown events?" More tail-focused than Calmar.

**Duration of Drawdown**: How many months did it take to recover? A 30% drawdown that recovered in 6 months feels less painful than one that lasted 2 years.

**Drawdown Probability**: What is the likelihood of a 20% drawdown in any given year? This shifts from worst-case to expected-case thinking.

The Calmar ratio remains the simplest and most widely used of these drawdown metrics, especially in the CTAs and quant-trading world.

## See also

<div class="wiki-seealso">

### Closely related

- [Maximum drawdown](/maximum-drawdown/) — the single worst loss from peak to trough
- [Sharpe ratio](/sharpe-ratio/) — the volatility-based risk-adjusted return metric
- [Sortino ratio](/sortino-ratio/) — downside volatility focus, alternative to Sharpe
- [Trend-following](/trend-following/) — the strategy class for which Calmar is most relevant
- [Value at risk](/value-at-risk/) — another tail-risk metric (percentile-based vs. observed worst)

### Wider context

- CTA — commodity trading advisors whose returns are often evaluated via Calmar
- [Hedge fund](/hedge-fund/) — alternative strategies where drawdown control is critical to investor retention
- Risk measurement — the broader framework of quantifying and comparing risks
- Equity curve — the visual representation of returns and drawdowns over time
- Performance attribution — breaking down returns into sources to understand Calmar drivers

</div>

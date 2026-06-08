---
title: "GARCH Models for Volatility Forecasting"
description: "GARCH volatility forecasting captures how past price shocks and variance feed into future volatility, improving on fixed-window averages for risk models."
keywords:
  - garch volatility forecasting
  - garch model time series
  - heteroskedasticity volatility
  - conditional volatility model
  - exponential weighted moving average
image: /svg/risk.svg
---

*A **GARCH volatility forecasting** model predicts tomorrow's price swings by feeding both yesterday's surprise (the shock) and yesterday's volatility into a formula. Instead of assuming volatility is constant, GARCH lets it evolve dynamically: big price moves cluster together, and volatility recedes gradually once calm returns. This makes GARCH far more accurate than a simple rolling average for risk measurement and [option pricing](/option/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">GARCH(1,1) — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">GARCH models capture the clustering of volatility shocks in financial returns.</div>

|   |   |
|---|---|
| **Full name** | Generalized AutoRegressive Conditional Heteroskedasticity |
| **Key idea** | Variance today depends on past shocks and past variance |
| **GARCH(1,1) formula** | σ²(t) = ω + α × ε²(t-1) + β × σ²(t-1) |
| **Components** | ω: base variance; α: shock weight; β: persistence |
| **Common constraint** | α + β < 1 (ensures stability) |
| **Beats** | Fixed rolling windows; captures volatility clustering |
| **Common lag choice** | GARCH(1,1); higher orders rarely improve fit materially |

</aside>

## Why Standard Volatility Measures Fall Short

Most risk models—[value at risk](/value-at-risk/), [option pricing](/option-premium/)—rely on volatility forecasts. A naive approach calculates the standard deviation of the past 20, 60, or 252 days of returns and treats it as fixed. This ignores a powerful empirical fact: volatility is not constant. It clusters.

When a stock crashes on bad earnings, the next day often brings another sharp move. Then, day by day, swings gradually shrink until a new shock reappears. Volatility is *conditionally* heteroskedastic—its variance depends on recent history.

A 60-day rolling average smooths over this structure, lagging real changes. It is also brittle: as the oldest observation leaves the window, volatility can jump even if nothing new has happened. GARCH fixes both problems by making volatility respond to new information in a mathematically disciplined way.

## The GARCH(1,1) Formula

The workhorse model is GARCH(1,1):

$$\sigma_t^2 = \omega + \alpha \, \varepsilon_{t-1}^2 + \beta \, \sigma_{t-1}^2$$

Here:
- **σ²(t)** is the conditional variance (volatility squared) for day *t*.
- **ε²(t-1)** is yesterday's squared return (the shock term), capturing surprise.
- **σ²(t-1)** is yesterday's variance, capturing persistence.
- **ω**, **α**, **β** are parameters fitted to historical data.

The model says: tomorrow's volatility depends on today's shock (the squared return) and today's volatility estimate. The weights α and β control how much each term matters.

## Interpreting the Parameters

**ω (omega):** The baseline variance when there are no shocks and no history. Often tiny but nonzero. It anchors the long-run average volatility.

**α (alpha):** The shock coefficient. A high α (say, 0.15) means a big price surprise today (large ε²) sharply boosts tomorrow's volatility estimate. A low α means shocks fade quickly.

**β (beta, not to be confused with [systematic risk beta](/beta-as-systematic-risk-measure/)):** The persistence parameter. High β (say, 0.80) means yesterday's volatility has heavy weight; volatility evolves slowly and clusters noticeably. Low β means volatility reverts quickly to ω.

The sum **α + β** is crucial. If α + β < 1, volatility stays mean-reverting (spikes fade over time). If α + β ≈ 1, volatility is nearly a random walk—shocks have very long memory. Most stock and currency returns have α + β in the range 0.95 to 0.99, indicating strong persistence.

## A Numerical Example

Suppose ω = 0.00005, α = 0.10, β = 0.85 (all daily). Start with today's variance σ²(1) = 0.0001 (daily volatility of ~1%).

Day 2: The return is −3% (a shock). ε²(2) = 0.0009.
σ²(2) = 0.00005 + 0.10 × 0.0009 + 0.85 × 0.0001 = 0.00005 + 0.00009 + 0.000085 = 0.000225
Daily volatility = √0.000225 ≈ 1.5%.

Day 3: Return is +0.5% (much smaller). ε²(3) = 0.000025.
σ²(3) = 0.00005 + 0.10 × 0.000025 + 0.85 × 0.000225 = 0.00005 + 0.0000025 + 0.00019125 ≈ 0.000244
Daily volatility ≈ 1.56%.

Day 4: Return is −0.2%. ε²(4) = 0.000004.
σ²(4) = 0.00005 + 0.10 × 0.000004 + 0.85 × 0.000244 ≈ 0.000262
Daily volatility ≈ 1.62%.

Notice: the shock on Day 2 pushed volatility up, but it is decaying gradually (Days 3–4) via the β term, even as new (smaller) shocks arrive. A rolling 10-day window would have been insensitive to the Day 2 shock until Day 10; GARCH responds immediately and lets volatility fade realistically.

## Advantages Over EWMA and Rolling Windows

[Exponential weighted moving average](/moving-average/) (EWMA) is simpler: σ²(t) = λ × σ²(t-1) + (1-λ) × ε²(t-1), with λ typically 0.94. EWMA has only one parameter and is easier to compute, making it popular in [risk systems](/value-at-risk/).

But GARCH is more flexible. It separately weights the shock term (α) and the persistence term (β), allowing the model to fit the data better. In practice, GARCH(1,1) usually outperforms EWMA at forecasting [volatility](/market-risk/) one or a few steps ahead, particularly during volatile periods.

A fixed rolling window (e.g., the past 60 days' standard deviation) is even cruder. It assigns equal weight to all 60 days, ignoring that recent shocks matter more. Rolling windows also "cliff" when old data leaves the window.

## Limitations and Extensions

GARCH assumes returns are conditionally normal given the variance. In reality, asset returns have fatter tails (more extreme moves) than a normal distribution predicts. Models like Student-t GARCH or GARCH with asymmetry (E-GARCH) address this, though the gains are often modest for short-term forecasts.

GARCH(1,1) is not the only specification. GARCH(2,2), with two lags of shocks and variance, can fit some return series better but risks overfitting and is harder to interpret. For most purposes, GARCH(1,1) is a sweet spot.

GARCH is univariate—it models one asset's volatility. Multivariate GARCH (D-GARCH, CCC-GARCH) models the full covariance matrix of multiple assets, critical for portfolio risk measurement, but is computationally demanding.

Parameter estimation requires maximum likelihood fitting to historical data. Results are sensitive to the sample period chosen: a period with a crash will yield higher long-run volatility estimates. Rolling-window re-estimation (updating parameters monthly or quarterly) is common in practice.

## GARCH in Practice

Risk managers use GARCH to forecast volatility for [value-at-risk](/value-at-risk/) calculations, hedging decisions, and position sizing. Option traders use it to anticipate whether implied volatility is overpriced or cheap relative to predicted realized volatility. Central banks and regulators rely on GARCH-based [stress tests](/stress-testing/).

The main takeaway: volatility is not a fixed number. It clusters, responding to shocks and fading gradually. GARCH captures this dynamic in a parsimonious framework, making it far superior to simplistic alternatives for forecasting the near-term volatility regime.

## See also

<div class="wiki-seealso">

### Closely related

- [Volatility](/market-risk/) — the time-varying quantity GARCH models
- [Historical volatility](/historical-volatility/) — backward-looking measurement vs. GARCH's forward focus
- [Value at risk](/value-at-risk/) — risk metric that often uses GARCH forecasts
- [Option pricing](/option-premium/) — requires volatility estimates; GARCH improves accuracy
- [Exponential weighted moving average](/moving-average/) — simpler alternative to GARCH

### Wider context

- [Beta as systematic risk measure](/beta-as-systematic-risk-measure/) — another tool for decomposing risk
- [Stress testing](/stress-testing/) — applying GARCH within extreme scenarios
- [Tail risk](/tail-risk/) — fatter tails not captured by standard GARCH

</div>

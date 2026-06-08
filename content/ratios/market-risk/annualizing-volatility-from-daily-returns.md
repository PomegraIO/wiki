---
title: "How to Annualize Volatility from Daily Returns"
description: "Annualize daily volatility by multiplying by the square root of 252 trading days per year. The square-root-of-time rule assumes independent returns, which markets violate in crises."
keywords:
  - annualize volatility daily returns
  - square root of time rule
  - daily standard deviation annualization
  - volatility scaling
  - 252 trading days
  - volatility calculation method
---

*To convert daily volatility into an annualized figure, multiply the daily standard deviation by the square root of 252 (the number of trading days in a year). This **square-root-of-time rule** is the standard in finance, but it assumes returns are independent—a critical assumption that breaks during market crises when losses cluster and volatility spikes unpredictably.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Annualizing Daily Volatility — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The square-root-of-252 scaling is the industry standard but rests on an assumption of random, independent daily moves.</div>

|   |   |
|---|---|
| **Formula** | Annual volatility = Daily std dev × √252 |
| **Scaling constant** | 252 trading days per year; √252 ≈ 15.87 |
| **Assumption** | Returns are independent over time |
| **Reality** | Returns cluster; volatility is autocorrelated |
| **Best practice** | Use longer periods (weekly/monthly) when possible |
| **Caution zone** | <30 days of data; scaling becomes unreliable |

</aside>

## The square-root-of-time rule

The most widely used annualization formula is:

> Annual Volatility = Daily Volatility × √252

The number 252 comes from the typical number of trading days in a U.S. market year (excluding weekends and holidays). The square root comes from the mathematics of variance: if daily returns are independent, their variances *add* over time, not linearly, but through the square-root relationship.

Here's the reasoning: if a portfolio's daily returns have a standard deviation of 1%, then the 2-day volatility is 1% × √2, the 5-day volatility is 1% × √5, and the 252-day (annual) volatility is 1% × √252 ≈ 1% × 15.87 = 15.87%.

## Worked example: computing annualized volatility

You have a stock with the following daily returns over 30 trading days:

| Metric | Value |
|---|---|
| **Daily return observations** | 30 days |
| **Mean daily return** | 0.08% |
| **Daily standard deviation** | 1.23% |
| **Annualized volatility (252-day)** | 1.23% × √252 = 1.23% × 15.87 ≈ 19.5% |

So a stock that wobbles ±1.23% on a typical day is expected to fluctuate around ±19.5% annually. That matches intuition: daily noise scales up over the course of a year.

## Why 252 and not 365?

Markets are closed weekends and holidays, so there are roughly 252 trading days per year in the U.S., compared to 365 calendar days. Using 365 would overstate volatility by including non-trading periods where prices don't move. The standard in global finance is 252 for equities.

Some markets use 250 (a round approximation) or 260 (assuming all weekdays are trading days). The choice matters slightly—√250 ≈ 15.81 vs √252 ≈ 15.87—but consistency within a firm or strategy is more important than the exact constant.

## The critical assumption: independence

The square-root-of-time rule assumes that daily returns are statistically independent—yesterday's return gives you no information about today's, and markets behave like a random walk.

This assumption is roughly true in normal markets. But it catastrophically fails during crises. In March 2020, March 2008, and October 1987, losses didn't scatter randomly across days; they clustered. Ten days of brutal declines in a row, not spread evenly. The assumption of independence breaks when [volatility](/volatility-smile/) itself becomes volatile.

During a crisis, the daily standard deviation might spike from 1.2% to 3.5% for a week, then settle back down. The square-root-of-time formula cannot predict this volatility-of-volatility. It assumes the next day's volatility equals today's, which is false.

## What happens when the assumption breaks

Under the square-root-of-time rule, if daily volatility is 1%, then 10 days of returns should have a volatility around 1% × √10 ≈ 3.16%. That works fine if daily returns scatter randomly. But if all 10 days are down 2%, the 10-day volatility is actually 20%, not 3.16%.

This is why [maximum drawdown](/maximum-drawdown/) and stress testing matter. The formula tells you "expect ±19.5% annually," but it doesn't warn you that all of it could come in a month, all of it could be downside, or all of it could be concentrated in a crash.

## When to use this rule and when to be skeptical

Use the square-root-of-time rule when:
- Computing baseline volatility expectations from normal market periods (1–2 years of daily data).
- Annualizing volatility for [portfolio comparison](/asset-allocation/) and risk management in stable regimes.
- Feeding into models like [Black-Scholes](/black-scholes-model/) that assume log-normal independent returns.

Be skeptical when:
- You're in a crisis period (volatility is spiking, correlations are changing).
- You have fewer than 30–60 days of data (the law of large numbers hasn't kicked in yet).
- You're comparing different asset classes with different volatility regimes (equities vs bonds behave differently).
- You're extrapolating from very short windows (5-day volatility × √252) to annual estimates.

## Alternative: use realized volatility over longer windows

Instead of annualizing daily volatility, calculate monthly returns and annualize those:

> Annual Volatility = Monthly Volatility × √12

Or calculate quarterly returns and annualize:

> Annual Volatility = Quarterly Volatility × √4

Monthly and quarterly volatility estimates are less noisy and less sensitive to daily clustering. They're also less susceptible to intraday volatility spikes that don't affect overnight returns.

For a portfolio you've owned for 3 years, annualized volatility from quarterly returns (12 data points, spanning multiple market regimes) is often more reliable than from daily returns (750 data points, perhaps dominated by a single market crash or rally).

## GARCH and stochastic volatility

More sophisticated volatility models recognize that volatility changes over time. GARCH models (Generalized Autoregressive Conditional Heteroskedasticity) estimate volatility as a function of recent shocks and recent volatility levels. A GARCH(1,1) model might predict tomorrow's volatility as:

> Tomorrow's Volatility² = Baseline² + Weight₁ × (Today's Return²) + Weight₂ × (Today's Volatility²)

This captures volatility clustering: big moves trigger bigger expected moves tomorrow. But GARCH is too complex for most investors and requires daily data spanning at least 5–10 years to estimate reliably. For typical portfolio management, the square-root-of-time rule is still the default.

## Practical example: a portfolio volatility calculation

You track a balanced portfolio's daily returns. Over 252 trading days, you compute:
- Daily standard deviation: 0.67%
- Annualized volatility (simple method): 0.67% × √252 ≈ 10.6%

Now, you pull together monthly returns (12 monthly observations) and compute:
- Monthly standard deviation: 2.1%
- Annualized volatility (monthly method): 2.1% × √12 ≈ 7.3%

The difference is striking. The monthly method gives a lower volatility estimate because it smooths out daily noise. The daily method is influenced by a particularly volatile month early in the year. For portfolio purposes, the monthly estimate might be more representative of the portfolio's true risk. A prudent investor would report both, note the discrepancy, and investigate whether the portfolio regime truly changed.

## The bottom line

Annualizing daily volatility via the square-root-of-252 rule is the industry standard and works reasonably well in normal markets. But it rests on the assumption that daily returns are independent and randomly distributed—an assumption that shatters during crises. Always pair annualized volatility with measures of tail risk (maximum drawdown, [value-at-risk](/value-at-risk/)), stress test your portfolio against historical crises, and don't trust a single volatility figure to capture portfolio risk. For longer holding periods (one year or more), compute volatility from monthly or quarterly returns instead, which are less sensitive to clustering.

## See also

<div class="wiki-seealso">

### Closely related

- Standard Deviation — the daily basis for annualized volatility
- [Historical Volatility](/historical-volatility/) — realized volatility from past data
- [Volatility Smile](/volatility-smile/) — non-normal distributions violating independence assumptions
- [Value-at-Risk](/value-at-risk/) — tail-risk measure complementing volatility
- [Sharpe Ratio](/sharpe-ratio/) — uses annualized volatility in its denominator

### Wider context

- Risk-Adjusted Returns — why annualized volatility matters for comparison
- [Maximum Drawdown](/maximum-drawdown/) — path-dependent risk that scaling formulas miss
- Portfolio Construction — volatility's role in asset allocation
- [Stress Testing](/stress-testing/) — how to test beyond the square-root-of-time assumption

</div>

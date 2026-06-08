---
title: "Kupiec Proportion-of-Failures Test"
description: "A binomial statistical test that checks whether a VaR model's observed exception rate matches its claimed confidence level."
keywords:
  - kupiec test
  - var validation
  - binomial test
  - proportion of failures
  - model backtesting
image: /svg/risk.svg
---

*The **Kupiec Proportion of Failures (PoF) test** is a statistical method that asks a simple question: if a [VaR](/credit-risk/) model claims a 99% confidence level, should we observe roughly 1 exception per 100 trading days, or is the observed count statistically implausible? Named for Paul Kupiec's 1995 research, it is the most widely deployed regulatory test for [VaR](/credit-risk/) model validation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Kupiec PoF Test — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement validation." />

<div class="wiki-infobox-caption">A binomial test of whether VaR exceptions match predicted frequency.</div>

|   |   |
|---|---|
| **What it is** | A hypothesis test of the proportion of [VaR](/credit-risk/) exceptions observed |
| **Null hypothesis** | The model's confidence level is correct |
| **Test statistic** | Binomial likelihood ratio; follows chi-squared distribution |
| **Key input** | Number of exceptions *x*, total days *n*, claimed probability *p* |
| **Accepts** | Models with exception counts in the "green zone" |
| **Weakness** | Ignores clustering of exceptions; misses timing patterns |
| **Complement** | [Christoffersen Interval Forecast test](/christoffersen-interval-forecast-test/) adds independence check |

</aside>

## The binomial foundation

Suppose a [VaR](/credit-risk/) model claims 99% confidence. Over a 250-day period, the model predicts exceptions (days when actual loss exceeds the [VaR](/credit-risk/) threshold) follow a binomial distribution: roughly 2–3 exceptions is expected, but 0, 4, 5, or even 10 are all possible by chance. The Kupiec test answers: is the observed count *consistent* with the model's claim, or is it so extreme that the model should be rejected?

The test is named for Paul Kupiec, who formalized it in his 1995 paper, but the mathematics are standard binomial testing. If a model is correctly specified with confidence level *p* (e.g., 0.99 for 99% [VaR](/credit-risk/)), and you observe *x* exceptions in *n* days, the probability of observing *exactly x* exceptions is:

P(X = x) = C(n,x) × p^n × (1−p)^x

where C(n,x) is the binomial coefficient "n choose x". The Kupiec test uses the **likelihood ratio** version: compare the probability of observing the data under the model's claimed parameters to the probability under the *observed* exception rate. If the claimed model fits much better, the test accepts it; if the observed rate fits better, the test rejects.

## From formula to regulatory practice

In regulatory practice, the Kupiec test is applied to a fixed backtest window—usually one year (250 trading days). For a 99% [VaR](/credit-risk/) over 250 days:

- **Expected exceptions**: 250 × 0.01 = 2.5 exceptions
- **Green zone**: 0–4 exceptions (do not reject)
- **Yellow zone**: 5–9 exceptions (flag for investigation)
- **Red zone**: 10+ exceptions (reject the model)

These thresholds are set to control the test's **Type I error** (false positive: rejecting a good model) at 5%. Roughly 5% of correctly-calibrated models will fall into the red zone by random chance, but that's deemed acceptable for regulatory purposes. The trade-off is that the test has limited power to detect bad models (Type II error): a truly broken model might still show only 3 exceptions by bad luck.

The test can also be applied monthly or quarterly. For a 99% [VaR](/credit-risk/) over a 22-day month, the expected exceptions is 0.22, so the threshold for red is much higher (often 2 or more exceptions). Monthly testing is more noisy but more frequent, allowing regulators to catch drift early.

## Kupiec in the Basel framework

The Basel Committee adopted the Kupiec test as the standard for [VaR](/credit-risk/) model validation in the 1990s and incorporated it into Basel III. Banks use it daily: their risk systems compute [VaR](/credit-risk/), track exceptions, and flag when the count enters yellow or red zones. When a model is challenged, banks and regulators run the formal Kupiec test to decide whether to recalibrate, tighten capital requirements, or scrap the model entirely.

The simplicity is intentional. The test requires only:
1. The claimed confidence level (*p*)
2. The number of days in the backtest (*n*)
3. The count of exceptions (*x*)

No assumptions about price distributions, correlation models, or volatility forecasting. A bank's risk system can compute it in milliseconds. This universality—the test works for any [VaR](/credit-risk/) model, whether parametric, historical simulation, or Monte Carlo—is why it dominated early regulatory frameworks.

## The weakness: ignoring clustering

The Kupiec test has a fatal limitation: it counts exceptions but ignores *when* they occur. Suppose two models both show 3 exceptions over 250 days (both pass the Kupiec test). Model A had exceptions on days 50, 150, and 250—scattered evenly. Model B had all 3 exceptions on days 248, 249, and 250—clustered at the end. Both pass, yet Model B's clustering suggests the model's assumptions broke down during market stress. The Kupiec test, which is agnostic to timing, misses this danger.

In the 2008 financial crisis and the 2020 pandemic shock, many banks' [VaR](/credit-risk/) models passed historical Kupiec tests on pre-crisis data but then generated exception clusters during the actual crisis. The test had been applied to calm markets and failed to anticipate stress regimes where correlations break down and volatility spikes.

This limitation prompted Christoffersen's work in the late 1990s, which extended backtesting to check for independence of exceptions.

## How banks use it in practice

A typical workflow:
1. **Daily monitoring**: Each day, the risk system computes [VaR](/credit-risk/) and checks if the next day's loss exceeded it. Exception count increments.
2. **Weekly or monthly review**: The risk team plots exceptions over the rolling window. If the count drifts into yellow, they investigate: did market regimes change? Did the portfolio shift? Is the model stale?
3. **Annual backtest**: At year-end, the risk team runs a formal Kupiec test on the full-year data. If the test rejects the model, capital charges increase (Basel framework) and the model is refit or replaced.
4. **Post-crisis revalidation**: After major market events (rate spikes, equity crashes, credit spreads widening), banks rerun backtests on the new regime to catch outdated models before they cause losses.

## Refinements and complementary tests

The Kupiec test is a *necessary* but not *sufficient* condition for a good [VaR](/credit-risk/) model. Banks now routinely apply it alongside:

- [**Christoffersen Interval Forecast test**](/christoffersen-interval-forecast-test/) – checks whether exceptions cluster, signaling model breakdown under stress.
- [**Expected shortfall (ES)**](/credit-risk/) – validates not just the frequency of breaches but their severity.
- [**Stress testing**](/stress-testing/) – applies the model to hypothetical worst-case scenarios (e.g., 2008-like crash).
- **Traffic light approach** – green/yellow/red zones, with red triggering immediate escalation to senior management.

The regulators have moved toward blended validation: Kupiec for frequency, Christoffersen for independence, and scenario analysis for extreme tail events that no historical backtest can fully capture.

## See also

<div class="wiki-seealso">

### Closely related

- [VaR backtesting](/backtesting-var/) — validating risk models by comparing predictions to realized losses
- [Christoffersen Interval Forecast test](/christoffersen-interval-forecast-test/) — tests both frequency and independence of VaR exceptions
- [Value at Risk](/credit-risk/) — the statistical measure of maximum expected loss
- [Expected shortfall](/credit-risk/) — average loss given a VaR breach
- [Stress testing](/stress-testing/) — evaluating portfolio loss under extreme scenarios

### Wider context

- [Market risk](/market-risk/) — loss from adverse price movements
- [Capital adequacy](/capital-adequacy/) — minimum capital required by regulators
- [Risk measurement](/credit-risk/) — quantitative frameworks for portfolio risk
- [Dodd-Frank Act](/dodd-frank-act/) — U.S. regulation mandating model validation and stress testing

</div>

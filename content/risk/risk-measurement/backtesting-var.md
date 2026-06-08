---
title: "VaR Backtesting"
description: "The process of validating a Value at Risk model by comparing predicted loss thresholds to actual trading results over a historical period."
keywords:
  - var backtesting
  - model validation
  - risk measurement
  - trading losses
  - var exceptions
image: /svg/risk.svg
---

*[**Value at Risk**](/credit-risk/) backtesting is the practice of comparing a model's predicted loss threshold against what actually happened in the markets. If a model claims a 99% [VaR](/credit-risk/)—meaning losses should exceed the forecast only 1% of the time—backtesting verifies whether that claim holds up over months or years of real trading data.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VaR Backtesting — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement and validation." />

<div class="wiki-infobox-caption">Checking whether forecast risk bounds match realized losses.</div>

|   |   |
|---|---|
| **What it is** | Comparing predicted [VaR](/credit-risk/) estimates to realized daily trading losses |
| **Key metric** | Exception count: days when actual loss exceeds the VaR forecast |
| **Expected exceptions** | For 99% VaR over 250 trading days, expect ~2–3 breaches |
| **Red flag** | Too many exceptions suggest the model underestimates tail risk |
| **Regulatory requirement** | [SEC](/securities-and-exchange-commission/), bank regulators, [Dodd-Frank](/dodd-frank-act/) |
| **Test types** | [Kupiec Proportion of Failures](/kupiec-test/), [Christoffersen Interval Forecast](/christoffersen-interval-forecast-test/) |

</aside>

## Why backtesting is the acid test for VaR

A [VaR](/credit-risk/) model is only as good as its assumptions. It may assume price changes follow a normal distribution, or that correlations between assets are stable, or that historical volatility predicts future volatility. None of these assumptions hold perfectly. A 99% VaR of $10 million means the model expects the portfolio to lose more than $10 million on only 1 in 100 trading days. But if actual losses exceed $10 million on 5 days in a year instead of the expected 2–3, the model is wrong—dangerously so.

Backtesting is the check. A bank or trading firm computes its [VaR](/credit-risk/) each day using the model, then compares it to the next day's actual profit and loss (P&L). Over a year or more, they count the "exceptions"—days when actual loss beat the forecast. Too many exceptions mean the model is optimistic. Too few mean the model may be wastefully conservative, locking up capital that could be deployed.

The practice is not optional. Regulators mandate backtesting for institutions that use [VaR](/credit-risk/) to justify capital levels. The [Dodd-Frank Act](/dodd-frank-act/) and Basel frameworks require banks to test their models against historical data and stress scenarios. Failure to backtest rigorously has destroyed firms: trading desks that trusted broken models discovered only after catastrophic losses that they had been 100 times more leveraged than they thought.

## The mechanics: from forecast to realized loss

On day *t*, the risk model calculates the 99% [VaR](/credit-risk/) for the next trading day—say, $5 million. This means the model predicts a 99% probability that daily losses will be less than $5 million. On day *t*+1, the actual P&L comes in: perhaps the portfolio gained $2 million (no exception), or lost $8 million (exception—the threshold was breached).

The backtester accumulates these outcomes. Over 250 trading days (roughly one year), a 99% [VaR](/credit-risk/) should produce about 2–3 exceptions on average. If a model shows 10 exceptions over 250 days, something is broken. If it shows zero exceptions over 500 days, the model may be overcautious (also a problem, if it prevents the firm from earning).

The math is binomial: if the model is correct, the probability of observing exactly *k* exceptions in *n* days follows a binomial distribution with success probability *p* = 0.01 (for 99% [VaR](/credit-risk/)). Backtesting uses this distribution to ask: is the observed exception count plausible under the model's claim, or is it statistically inconsistent?

## Green zones, yellow zones, red zones

Regulators and internal risk teams typically classify backtesting results into zones. If a 99% [VaR](/credit-risk/) model over 250 days shows:

- **0–4 exceptions**: Green zone (model passes). Expected range is roughly 1–3, so 4 is still acceptable.
- **5–9 exceptions**: Yellow zone. The model may be underestimating risk; tighten assumptions or increase capital buffers.
- **10+ exceptions**: Red zone. The model fails; capital charges rise, or the model is shelved until fixed.

These thresholds are not arbitrary. They reflect the power of backtesting to detect a bad model without false positives (rejecting a good model by chance). A test with too many false positives would erode trust and force banks to abandon working models. A test with too few detects only egregiously bad models. The zone system is calibrated to strike that balance.

## Pitfalls and biases in backtesting

Backtesting is powerful but fragile. One common trap is **data snooping**. If a bank backtests dozens of models on the same historical data, at least one will look good by chance. The bank then deploys that model, only to find it fails on new data. Rigorous practice separates the sample used to fit the model from the sample used to backtest it—often called the "out-of-sample" test. A model fit on 2015–2018 data should be backtested on 2019–2020 data.

Another pitfall is **cherry-picking the backtest window**. Testing a 99% [VaR](/credit-risk/) model over a calm period (low volatility, no crashes) will always show few exceptions, even if the model is broken. Rigorous backtesting includes periods of stress: the 2008 financial crisis, the 2020 pandemic shock, the 2022 rate spike. A model that passes backtesting only in bull markets is not credible.

[**Time decay**](/credit-risk/) also matters. A model trained on 2010–2015 data may be obsolete by 2023 if market structure, correlations, or volatility regimes have changed. Banks refresh their models and rerun backtests every quarter, and certainly after major market events.

## The limits of backtesting

Backtesting validates whether a [VaR](/credit-risk/) model's predicted exception rate matches observed exceptions. It does not validate the *severity* of breaches. A model that predicts a 99% [VaR](/credit-risk/) of $10 million might be breached only twice in 250 days (passing), but when breached, losses might reach $50 million instead of the expected $15 million. The breach count looks good; the severity is a disaster.

This is why banks also run [**stress tests**](/credit-risk/) and [**expected shortfall**](/credit-risk/) calculations, which measure the average loss *given* that a [VaR](/credit-risk/) breach occurs. These metrics capture tail risk that backtesting alone might miss. A model that passes backtesting is like a car that passed a brake test; you still need to know how hard it stops when the brakes are engaged.

Backtesting also assumes the P&L data is clean. In practice, P&L includes P&L revaluations, accounting adjustments, and reclassifications that can obscure the true trading result. A "clean" P&L that isolates trading risk from funding costs and revaluation noise is rare but essential for backtesting integrity.

## Regulatory acceptance and ongoing debate

[Regulators](/securities-and-exchange-commission/) have broadly accepted backtesting as the gold standard for [VaR](/credit-risk/) model validation, but implementation varies. Some regulators use the [Kupiec Proportion of Failures test](/kupiec-test/), a simple binomial check of exception count. Others mandate the [Christoffersen test](/christoffersen-interval-forecast-test/), which also checks whether exceptions cluster (suggesting the model misses volatility bursts) or are scattered (suggesting the model is robust). Research economists propose ever-more-sophisticated tests, but backtesting's simplicity is also its strength: if a model can't predict tomorrow's loss threshold better than a coin flip, it shouldn't guide capital allocation.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/credit-risk/) — the statistical measure of maximum expected loss at a given confidence level
- [Kupiec Proportion of Failures test](/kupiec-test/) — a binomial test of whether VaR exceptions match the model's claim
- [Christoffersen Interval Forecast test](/christoffersen-interval-forecast-test/) — tests both frequency and clustering of VaR exceptions
- [Expected shortfall](/credit-risk/) — average loss given a VaR breach; captures tail severity
- [Stress testing](/stress-testing/) — evaluating portfolio loss under hypothetical extreme scenarios
- [Exposure at default](/exposure-at-default/) — the outstanding amount at risk if a counterparty defaults

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — U.S. regulation requiring banks to validate risk models
- [Market risk](/market-risk/) — the loss from adverse price movements
- [Risk measurement](/credit-risk/) — quantitative frameworks for assessing portfolio risk
- [Model validation](/credit-risk/) — ensuring risk and valuation models reflect reality

</div>

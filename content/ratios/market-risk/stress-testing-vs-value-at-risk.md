---
title: "Stress Testing vs Value at Risk"
description: "Stress testing and value at risk are complementary risk frameworks. VaR predicts typical losses; stress tests model extreme scenarios regulators demand both."
keywords:
  - stress testing vs value at risk
  - value at risk stress testing
  - var stress testing risk management
  - scenario analysis value at risk
---

*Banks and asset managers use two distinct methods to quantify risk: **value at risk** (VaR), a statistical measure of typical losses under normal conditions, and **stress testing**, a scenario-based projection of how portfolios behave in severe market dislocations. Neither alone suffices; regulators mandate both because they capture different dangers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stress Testing vs Value at Risk — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two complementary frameworks, each exposing blind spots the other misses.</div>

|   |   |
|---|---|
| **VaR approach** | Historical or statistical distribution; normal conditions |
| **Confidence level** | 95% or 99%; probability-based |
| **Time horizon** | 1 day to 10 days typical |
| **Stress testing** | Scenario-based; historical crises or hypothetical shocks |
| **Normal market assumption** | Violated; tests extreme tail events |
| **Regulatory requirement** | Post-2008, both are mandatory for large firms |
| **Advantage of VaR** | Quantifies everyday risk; easy to communicate |
| **Advantage of stress testing** | Captures contagion, liquidity crises, regime shifts |

</aside>

## What value at risk does—and misses

**Value at risk** (VaR) is a probabilistic statement: "We are 95% confident that our losses will not exceed $X over the next trading day." It uses historical price data or statistical models to estimate the distribution of returns, then marks off a percentile (often the 5th or 1st) as the maximum expected loss under typical market conditions.

VaR is elegant and widely used because it boils risk into a single number. A bank's board can understand that a $50 million daily VaR at 95% confidence means the firm is expected to suffer a loss exceeding $50 million roughly once every 20 trading days. It is intuitive, easy to aggregate across portfolios, and suitable for day-to-day risk limits.

But VaR has blind spots. It assumes markets behave as they have in the past and that price movements follow a normal distribution. In reality, markets are "fat-tailed"—extreme moves occur more often than standard distributions predict. During the 2008 financial crisis, portfolios hedged according to historical VaR models still suffered catastrophic losses because [correlation](/concentration-risk/) structures broke down and [liquidity](/liquidity-risk/) evaporated overnight. A one-tail [duration](/duration/) calculation that looked safe in 2007 became worthless as [credit spreads](/credit-spread/) widened and [counterparty risk](/counterparty-risk/) spiked.

VaR also ignores events outside its confidence interval. A 95% VaR tells you nothing about the size of losses in the worst 5% of cases—whether they are 20% worse or 500% worse than the VaR estimate.

## What stress testing does

**Stress testing** abandons the statistical comfort zone and asks: "If markets seize up like in 2008, or if the Fed raises rates 300 basis points, or if a major counterparty defaults, what happens to our positions?"

Rather than fitting data to a distribution, stress testing specifies a scenario—often drawn from history (the 2008 crisis, the 1987 crash, the 1998 LTCM blowup) or designed hypothetically—and recalculates portfolio [value](/fair-value/) under those new conditions. A 10-year Treasury bond yield might jump 200 basis points; a [credit-default-swap spread](/credit-default-swap/) on financial stocks might widen 500 basis points; equity [volatility](/historical-volatility/) might spike 50 percentage points. These moves are coordinated and plausible, not independent random shocks.

Stress tests reveal contagion and correlation breakdown. In normal times, a bank's long equity position and its short credit-spread position might be loosely negatively correlated, providing a hedge. In a stress scenario where equity volatility explodes and risk appetite collapses, both positions sink together, and the hedge vanishes. A firm that passed its VaR test with flying colors can be wiped out by a stress scenario it did not anticipate.

Stress testing also accounts for **liquidity drying up**. Under VaR, a firm assumes it can sell positions at market price. In a true crisis, bid-ask [spreads](/bid-ask-spread/) widen dramatically, and for illiquid assets, there may be no bids at all. Stress tests force planners to ask whether they can liquidate positions or whether they will be trapped.

## Historical precedent: why both are now required

Before the 2008 crisis, VaR was the standard. It was efficient, mathematically satisfying, and endorsed by regulators. But VaR models built on 1990s and early 2000s data had no memory of a true system-wide panic. When Lehman Brothers collapsed, correlations that had been 0.3 jumped to 0.9 overnight. Positions that VaR said were uncorrelated all moved in the same direction. Banks that appeared well-hedged by VaR metrics suffered enormous losses.

The post-2008 regulatory overhaul ([Dodd-Frank Act](/dodd-frank-act/), [Basel III](/capital-adequacy/), international agreements) mandated that large financial institutions report and limit both VaR and stress-test losses. The supervisory stress test (run by the Federal Reserve in the United States) applies a standardized severe scenario to all major banks and publishes results, forcing transparency and preventing a race to the bottom in risk standards.

## Practical use: complementary frameworks

In practice, risk managers use VaR for everyday monitoring and limit-setting. A trading desk gets a daily VaR allocation; if the desk's 95% VaR exceeds the limit, trading must shrink positions. This keeps risk manageable on routine days.

Stress tests operate at a longer, policy level. A firm's chief risk officer and board review stress scenarios quarterly or annually, asking whether the firm can survive a severe dislocation without failing or requiring a government bailout. Large institutions maintain multiple stress scenarios—a 2008-style credit crisis, a rates spike, a recession—and ensure capital buffers are adequate to absorb the implied losses.

Some firms also use a middle ground: **stressed VaR** or **historical simulation** over crisis windows. Instead of using all history, the model re-estimates VaR using only data from a known crisis period (e.g., August 1998 or September 2008). This captures fat tails without fully leaving the statistical framework.

## Limitations of both

Neither VaR nor stress testing is perfect. Stress tests are vulnerable to **scenario bias**: a firm might stress-test for a 2008-like crisis but miss a novel tail risk (such as a cyberattack on financial infrastructure or a sudden policy shift). And since stress scenarios are partly subjective, a risk manager might unconsciously exclude scenarios that would expose a blind spot.

VaR, while rigorous, still depends heavily on the model chosen and the historical period. A model fit to data from 2010–2019 (a low-volatility decade) will underestimate tail risk relative to a model fit to 1980–2020 (which includes multiple crises).

Best practice combines both. Use VaR for daily control and aggregation across desks. Use stress testing to ensure tail-risk capital is adequate and to identify scenarios where models break. Periodically back-test VaR estimates against actual losses and update them when realized moves exceed predictions.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at risk](/value-at-risk/) — The statistical framework explained in detail
- [Historical volatility](/historical-volatility/) — Key input to VaR models
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — Component of many stress tests
- [Liquidity risk](/liquidity-risk/) — A major driver of stress-test losses
- [Counterparty risk](/counterparty-risk/) — Often central to crisis scenarios

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — Post-2008 regulation mandating stress tests
- [Capital adequacy](/capital-adequacy/) — Basel framework requiring both VaR and stress capital
- [Risk-weighted assets](/risk-weighted-assets/) — Regulatory capital rules tied to risk measures
- [Credit spread](/credit-spread/) — Often a key variable in stress scenarios
- [Duration](/duration/) — Critical for fixed-income stress testing

</div>

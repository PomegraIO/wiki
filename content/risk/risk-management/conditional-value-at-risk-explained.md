---
title: "Conditional Value at Risk Explained"
description: "Conditional value at risk explained: CVaR measures tail risk by looking at the average loss in the worst scenarios, going further than VaR."
keywords:
  - conditional value at risk explained
  - cvar risk measure
  - expected shortfall
  - tail risk measurement
  - value at risk alternatives
  - regulatory risk metrics
image: "/svg/risk.svg"
---

*Conditional value at risk (CVaR), also called expected shortfall, measures the average loss across the worst-case scenarios a portfolio might experience. Unlike Value at Risk, which only identifies a threshold, CVaR tells you what happens beyond that threshold—making it the risk metric regulators and sophisticated managers increasingly prefer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CVaR / Expected Shortfall — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk concepts." />

<div class="wiki-infobox-caption">CVaR quantifies tail risk by averaging the worst outcomes, not just measuring a boundary.</div>

|   |   |
|---|---|
| **What it measures** | Average loss in the worst X% of outcomes |
| **Calculation basis** | All losses beyond the [VaR](/value-at-risk/) threshold |
| **Time horizon** | User-specified (1 day, 10 days, etc.) |
| **Confidence level** | Typically 95% or 99% |
| **Main advantage** | Captures severity of tail events, not just probability |
| **Regulators** | Basel III, CFTC, EU prefer CVaR for capital requirements |

</aside>

## Why VaR alone misses the tail

[Value at Risk](/value-at-risk/) answers a narrow question: "What loss level will I exceed only 5% of the time?" At a 95% confidence level over one day, a bank's VaR might be $10 million. That number is useful—it's a hard boundary—but it tells you nothing about what happens in that worst 5%. Do losses stop at $15 million, or do they occasionally hit $50 million?

This is the critical flaw: VaR is silent on catastrophic losses. Two portfolios can have identical VaR yet vastly different tail distributions. One might see worst-case losses capped near the boundary; the other might face blow-ups far beyond. Risk managers, burned by surprise losses during 1998 (Long-Term Capital Management), 2008, and 2020, learned that a single threshold is insufficient.

Conditional value at risk directly fixes this. By averaging all losses that exceed the VaR threshold, CVaR captures the shape and severity of the tail.

## How conditional value at risk is calculated

The calculation flow is straightforward in concept, though implementation varies. Start with historical data or a simulation of portfolio returns.

**Step 1: Choose a confidence level.** Risk managers typically use 95% or 99%. A 95% CVaR means you are averaging the losses in the worst 5% of scenarios.

**Step 2: Identify the VaR threshold.** If you have 1,000 daily return simulations, the 95% VaR is the loss at the 50th-worst outcome (the 5th percentile). Sort all returns from worst to best, then count inward.

**Step 3: Average all losses worse than that threshold.** CVaR is the arithmetic mean of all returns at or below the VaR percentile. If the worst 50 outcomes range from −8% to −2%, CVaR is their average, say −4.5%.

**Example:** A hedge fund portfolio has 250 days of returns on record.

| Worst outcomes | Return |
|---|---|
| Day 47 (worst) | −12% |
| Day 93 | −11.5% |
| Day 156 | −10% |
| … | … |
| Day 204 (13th worst) | −3% |

At 95% confidence (bottom 5%, or roughly 13 days out of 250), the VaR is around −3%. The CVaR is the average of all 13 worst days: roughly −7.2%. This tells the manager: when we breach the threshold, we lose 7.2% on average, not 3%.

## CVaR vs. VaR in practice

The difference becomes concrete under stress. Suppose two traders manage $100 million each with identical 95% VaR of $2 million over one day.

**Trader A's tail losses:** The worst 5% of scenarios cluster near −$2.5 million. CVaR: −$2.3 million.

**Trader B's tail losses:** The worst 5% range from −$2 million to −$8 million. CVaR: −$4.1 million.

Both pass the VaR screen. But Trader B's portfolio has twice the expected tail loss. A bank using only VaR would allocate the same capital buffer to both; a CVaR-based regime would require Trader B to hold more capital or reduce size.

This distinction matters most during rare, violent events. When markets gap or correlations collapse, the tail matters more than the average.

## Why regulators now require CVaR

Post-2008, financial regulators worldwide shifted toward CVaR:

- **Basel III** uses CVaR (called Expected Shortfall) for calculating capital charges on market risk, replacing VaR as the standard.
- **CFTC** requires CVaR reporting for commodity futures traders.
- **EU regulations** (including the revised Capital Requirements Directive) mandate CVaR for systemically important institutions.

The logic is simple: regulators learned that institutions with low VaR can still face ruin if tail losses are extreme. By forcing banks to hold capital against the expected shortfall, not just the boundary, supervisors reduce systemic risk.

CVaR is also mathematically superior in a technical sense: it is [coherent](/value-at-risk/), meaning it respects properties that any reasonable risk measure should satisfy (diversification should reduce risk, for example). VaR fails this test in some scenarios.

## Limitations and practical challenges

CVaR is not a perfect tool. Its main weaknesses:

**Estimation error in the tail.** If you only have 250 days of data and you're measuring 99% CVaR, you're averaging just 2 or 3 observations. Small sample noise dominates. Historical data often under-represents the worst outcomes.

**Assumption sensitivity.** CVaR depends heavily on whether you use historical data, a normal-distribution assumption, or a fat-tailed model. Change the assumption, change the number.

**Computational cost.** Calculating CVaR under many scenarios (Monte Carlo simulations with 10,000+ paths) is more expensive than a simple percentile calculation.

**False confidence in precision.** A reported CVaR of −$2.347 million feels precise. It isn't. Confidence intervals around CVaR estimates are wide.

Despite these caveats, CVaR remains the best single number available for communicating tail risk. It answers the question VaR cannot: when disaster strikes, how bad is it likely to be?

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the threshold measure that CVaR builds upon
- [Stress Testing](/stress-testing/) — forward-looking scenario analysis complementary to CVaR
- [Tail Risk](/tail-risk/) — the distribution properties CVaR targets
- Risk Management — institutional framework around CVaR deployment
- Portfolio Risk — how CVaR combines across asset holdings

### Wider context

- [Basel III](/basel-iii/) — regulatory framework mandating CVaR for capital calculations
- Hedging — tactical use of CVaR in position sizing
- [Diversification](/diversification/) — why tail correlation matters

</div>

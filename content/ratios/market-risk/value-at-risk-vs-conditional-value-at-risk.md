---
title: "Value at Risk vs Conditional Value at Risk"
description: "Understand VaR as a loss threshold and CVaR (expected shortfall) as the average loss beyond it—and why regulators prefer CVaR for bank stress testing."
keywords:
  - value at risk vs conditional value at risk
  - VaR and CVaR comparison
  - expected shortfall
  - tail risk measurement
  - regulatory risk metrics
  - portfolio stress testing
---

*The **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** both quantify downside exposure, but VaR answers "what is my maximum likely loss?" while CVaR answers "if I exceed that loss, what is the average loss?" CVaR captures tail risk and is increasingly mandated in bank capital rules because VaR can hide the severity of rare, catastrophic scenarios.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Two Tail Risk Metrics — Key Facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">VaR is a threshold; CVaR is what happens when you breach it.</div>

|   |   |
|---|---|
| **VaR definition** | Maximum loss at a given confidence level (e.g., 99%) |
| **CVaR definition** | Expected (average) loss given that VaR is exceeded |
| **VaR percentile** | e.g., 99% VaR = worst 1% of outcomes |
| **CVaR percentile** | Average of losses beyond the VaR threshold |
| **Example (99% level)** | VaR = $10M; CVaR might be $15M |
| **Regulatory status** | Phased out for banks; Basel III prefers CVaR |
| **Tail-risk visibility** | VaR: limited; CVaR: explicit |

</aside>

## The VaR Shortcoming

**Value at Risk** is straightforward: if your portfolio has a 99% VaR of $10 million over a 1-day horizon, you're saying there's a 99% chance your losses won't exceed $10 million (or equivalently, a 1% chance they will). It's a single number that communicates downside in intuitive terms.

But VaR has a critical blind spot. It tells you the threshold, but nothing about what happens *beyond* it. In the 1% of cases where losses exceed $10 million, they might be $15 million or $500 million. VaR is indifferent to the difference. This matters enormously in extreme markets. During the 2008 financial crisis, portfolios that looked safe by VaR experienced catastrophic losses because the tail was far thicker than historical data suggested.

## CVaR Fills the Gap

**Conditional Value at Risk** (also called **expected shortfall**) solves this problem by asking: given that we're in the tail (beyond the VaR threshold), what is the average loss? If a 99% CVaR is $15 million, it means that in the worst 1% of scenarios, losses average $15 million. This forces risk managers to confront what really happens when things go wrong.

Mathematically, CVaR is the expected value of all losses greater than or equal to the VaR threshold. It uses all the tail information rather than just a single cutoff point. Because of this, CVaR is subadditive—the CVaR of a portfolio cannot exceed the sum of the CVaRs of its parts—while VaR can violate this principle. This property makes CVaR a "coherent risk measure" in technical terms, which regulators prefer.

## A Worked Example

Imagine a small hedge fund with a portfolio of emerging-market bonds. Historical data over 1,000 trading days shows:

- 99% daily loss threshold: $5 million (the worst 1% of days)  
- On the 10 worst days, losses were: $5.2M, $6.1M, $7.8M, $8.3M, $9.2M, $12.1M, $14.5M, $15.3M, $18.2M, $22.4M

The 99% **VaR is $5 million** (the 99th percentile). But the **99% CVaR is the average of these 10 tail days**: ($5.2 + $6.1 + $7.8 + $8.3 + $9.2 + $12.1 + $14.5 + $15.3 + $18.2 + $22.4) / 10 = **$12.1 million**.

A manager relying only on VaR would think the portfolio's downside is capped at $5 million. CVaR reveals that when the break actually comes, the average outcome is $12.1 million—more than double. This is the tail risk VaR misses.

## Why Regulators Switched

After 2008, banking regulators realized that VaR had lulled major institutions into complacency. The Basel III accord (and later updates) gradually phased out VaR as the standard risk metric and replaced it with CVaR for calculating minimum [capital-adequacy](/capital-adequacy/) requirements. The shift reflects a hard lesson: financial crises live in the tail.

Banks now use CVaR to stress-test their portfolios and determine how much equity capital they must hold. A $50 billion bank cannot reserve capital based only on the 99th percentile; it must account for what happens when the 1% event occurs and cascades across correlated positions.

## The Trade-Off: Simplicity vs. Completeness

VaR's popularity—before the regulatory shift—stemmed partly from its simplicity. One number, easily communicated to boards and investors. CVaR requires more explanation and computation. It also depends more heavily on the tail of your distribution, which can be volatile to estimate from finite historical data.

However, this trade-off increasingly favors CVaR. Institutions that survived 2008 and other crises learned that tail-risk blindness is expensive. The added complexity of CVaR is a small price for a more honest risk picture.

## Parametric vs. Historical Estimation

Both metrics can be calculated parametrically (assuming a normal distribution) or empirically (from actual historical returns). When markets behave normally, the parametric approach is clean. When they don't (which is often), empirical CVaR—looking at what actually happened in the worst cases—is more trustworthy. Historical data forces you to reckon with real tail behavior.

## Monte Carlo Simulation Approach

For complex portfolios with options and derivatives, neither historical nor parametric VaR/CVaR may be sufficient. Many institutions use Monte Carlo simulation: generate thousands of plausible future scenarios and measure the 99th percentile and its tail average. This approach is computationally intensive but can capture [tail-risk](/tail-risk/) in nonlinear instruments more accurately.

## Current Regulatory Landscape

Under Basel III (and the ongoing Basel IV discussions), major banks must report CVaR as their primary market risk metric. Insurance regulators (including Solvency II in Europe) similarly mandate CVaR-like metrics. If you're working at a regulated financial institution, you're almost certainly using CVaR—or have moved beyond both to even more sophisticated measures like [stress-testing](/stress-testing/) frameworks.

## See also

<div class="wiki-seealso">

### Closely related

- [Tail Risk](/tail-risk/) — the extreme outcomes that CVaR targets
- [Volatility](/historical-volatility/) — standard deviation, which informs both VaR and CVaR
- [Stress Testing](/stress-testing/) — scenario analysis that often accompanies CVaR
- [Capital Adequacy](/capital-adequacy/) — regulatory framework driving CVaR adoption
- [Expected Shortfall](/value-at-risk/) — another name for CVaR
- [Beta](/beta/) — market sensitivity, orthogonal to but paired with risk metrics

### Wider context

- [Risk Management](/value-at-risk/) — broader discipline encompassing VaR and CVaR
- [Basel III](/capital-adequacy/) — regulatory framework mandating CVaR
- [Portfolio Risk](/value-at-risk/) — how banks and funds measure downside

</div>

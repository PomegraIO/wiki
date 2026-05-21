---
title: "Expected Shortfall"
description: "Expected shortfall is the average loss a portfolio incurs in scenarios worse than the value-at-risk threshold — the mean loss of tail outcomes, also called conditional value-at-risk."
keywords:
  - expected shortfall
  - ES
  - CVaR
  - tail loss
  - average of tail losses
image: "/svg/risk.svg"
---

*Expected shortfall (ES) — synonymous with [conditional-value-at-risk](/conditional-value-at-risk) — is the average loss a portfolio experiences in its worst-case scenarios, specifically the mean of losses when they exceed the [value-at-risk](/value-at-risk) threshold. It directly addresses the key weakness of [value-at-risk](/value-at-risk) by measuring the magnitude of tail losses, not just the probability.*

<div class="wiki-hatnote">

This entry is a synonym and detailed treatment of expected shortfall. For the VaR threshold it builds on, see [value-at-risk](/value-at-risk); for broader exposure to tail losses, see [tail-risk](/tail-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Expected Shortfall — key facts</div>

<img src="/svg/risk.svg" alt="A graph showing a distribution curve with the tail highlighted and labeled with an average line" />

<div class="wiki-infobox-caption">Expected shortfall captures the average loss in tail scenarios.</div>

|   |   |
|---|---|
| **What it is** | Average loss when losses exceed the VaR threshold |
| **Synonyms** | CVaR, conditional value-at-risk, expected tail loss |
| **Calculation** | Average of worst X% of outcomes (e.g., worst 1% for 99% confidence) |
| **Regulatory standard** | Basel III and modern frameworks; replacing VaR |
| **Key insight** | VaR tells you the threshold; ES tells you how bad the tail actually is |
| **Advantage** | Direct measurement of tail severity; not just a percentile |
| **Mathematical property** | ES ≥ VaR; equality only if distribution is thin-tailed |

</aside>

## The simple idea behind expected shortfall

[Value-at-risk](/value-at-risk) is a threshold: the 99% VaR of $1M means there is a 1% chance of losing more than $1M. But it does not tell you what happens in that 1% tail. The loss could be $1.5M or $10M.

Expected shortfall answers: "If the worst happens (you are in the 1% tail), what is the average loss?" For example, a 99% ES of $1.5M means that when losses exceed $1M, they average $1.5M.

This directly measures tail risk severity, which [value-at-risk](/value-at-risk) does not.

## How expected shortfall is calculated

**Method 1: Empirical (historical)**

Sort all past daily returns from worst to best. For 99% expected shortfall on 1,000 days of data:
- Identify the worst 1% of days (roughly 10 days).
- Calculate the average loss over those 10 days.
- That average is the 99% expected shortfall.

**Method 2: Parametric**

If returns follow a normal distribution with mean μ and standard deviation σ:
- The 99% VaR is at x = μ - 2.33σ.
- The 99% ES is μ - σ × φ(z) / (1 - Φ(z)), where φ and Φ are the PDF and CDF of the standard normal, and z = 2.33.

This formula is more complex than VaR, but it is standard.

**Method 3: Monte Carlo**

Simulate thousands of scenarios, calculate portfolio loss in each, sort by loss magnitude, take the average of the worst 1%.

## Expected shortfall is always at least as bad as VaR

By definition, ES is the average of tail losses, and VaR is the threshold. The average of tail losses cannot be better (less negative) than the threshold itself.

Mathematically: **ES(α) ≥ VaR(α)** for any confidence level α.

- If the distribution is **normal** (thin tails), ES ≈ VaR, so the difference is small.
- If the distribution has **fat tails** (which real markets do), ES >> VaR, and the tail risk is much worse than VaR implies.

This is why the shift from VaR to ES exposed many institutions to much higher capital requirements in post-2008 regulations. Suddenly, tail risk was being measured directly rather than ignored.

## Example: ES reveals hidden tail risk

A portfolio's returns over 100 days:

**Scenario A: Normal-ish returns**
- Days 1-95: Returns between -0.5% and +0.5%
- Days 96-99: Returns of -1.5%, -2.0%, -2.5%, -3.0%
- Day 100: Return of -3.5%

95% VaR: The worst 5% is days 96-100, with returns ≥ -3.5%. The fifth-worst day is -1.5%, so VaR is -1.5%.
95% ES: Average of worst 5% = (-1.5 - 2.0 - 2.5 - 3.0 - 3.5) / 5 = -2.5%.

ES is worse, but not dramatically so.

**Scenario B: Fat-tail returns**
- Days 1-95: Returns between -0.5% and +0.5%
- Days 96-99: Returns of -1%, -1%, -1%, -1%
- Day 100: Return of -30%

95% VaR: The worst 5% includes day 100 (-30%), so VaR is the fifth-worst, which is -1%.
95% ES: Average of worst 5% = (-1 - 1 - 1 - 1 - 30) / 5 = -6.8%.

Here, VaR says -1%, but ES reveals the true tail severity: -6.8%. This is the power of ES: it reveals what VaR hides.

## Regulatory adoption of expected shortfall

After the 2008 financial crisis, regulators realized that [value-at-risk](/value-at-risk) was systematically too low. Banks held capital for 2-3% daily VaR, but experienced losses of 10%+ in bad months.

[Basel III](/capital-adequacy), adopted globally in 2013+, shifted to expected shortfall as the primary risk metric. Banks now calculate:
- 10-day 97.5% ES (instead of 1-day 99% VaR).
- And back-tested against actual daily losses.

This increased capital requirements for banks with fat-tailed portfolios (like trading desks and hedge funds) while leaving those with thin-tailed portfolios largely unchanged.

## Practical use of expected shortfall

For a portfolio manager:
- A 1-day 99% ES of $2M means: on the worst 1% of days (about 2-3 per year), the portfolio loses an average of $2M.
- This directly tells the manager: "I need at least $2M buffer, and probably more, to be safe."
- They can stress-test further to understand the absolute worst case.

For a risk manager:
- ES forces explicit modeling of tail risk.
- It cannot be dismissed as "unlikely" because it is anchored to the probability (worst 1%) and the magnitude (average of those scenarios).

## Limitations of expected shortfall

Despite its superiority to VaR, ES has limitations:

1. **Tail data sparsity.** For 99% ES on 1,000 days, only 10 tail observations inform the estimate. Those 10 days might not represent future tails.

2. **Parameter uncertainty.** If volatility or correlation estimates are wrong, ES will be wrong.

3. **Does not capture absolute worst case.** ES is the average; the absolute worst could be worse.

4. **Black swans still missed.** ES reflects historical data or distributional assumptions. A new type of tail event is not captured.

5. **Computational complexity.** ES is harder to calculate than VaR, especially for portfolios with complex instruments.

Despite these, ES is the modern standard and is far superior to VaR alone.

## See also

<div class="wiki-seealso">

### Closely related

- [Conditional-value-at-risk](/conditional-value-at-risk) — formal name; ES is the same concept
- [Value-at-risk](/value-at-risk) — the threshold that ES builds upon
- [Tail-risk](/tail-risk) — what ES directly measures
- [Stress-testing](/stress-testing) — complements ES with scenario analysis
- [Basel capital](/capital-adequacy) — regulatory framework built on ES

### Broadly related

- [Fat-tail-risk](/fat-tail-risk) — makes ES materially worse than VaR
- [Model-risk](/model-risk) — ES calculations depend on model assumptions
- [Parameter-risk](/parameter-risk) — tail estimates are uncertain
- [Black-swan](/black-swan) — extreme tail events ES might miss
- [Risk management](/value-at-risk) — ES is modern foundation

</div>

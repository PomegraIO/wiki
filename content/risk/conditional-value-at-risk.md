---
title: "Conditional Value-at-Risk"
description: "Conditional value-at-risk (CVaR), also called expected shortfall, is the average loss a portfolio incurs when losses exceed the value-at-risk threshold — the average of the worst outcomes."
keywords:
  - conditional value-at-risk
  - CVaR
  - expected shortfall
  - tail loss average
  - risk measure
image: "https://picsum.photos/seed/conditional-value-at-risk/900/600"
---

*Conditional value-at-risk (CVaR) — also called **expected shortfall** or **expected tail loss** — is the average loss incurred in the worst scenarios, specifically the average loss when losses exceed the [value-at-risk](/value-at-risk) threshold. It directly measures the severity of tail events, addressing the key limitation of [value-at-risk](/value-at-risk).*

<div class="wiki-hatnote">

This entry covers the tail-loss average metric. For the VaR threshold itself, see [value-at-risk](/value-at-risk); for broader exposure to extreme losses, see [tail-risk](/tail-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Conditional Value-at-Risk — key facts</div>

<img src="https://picsum.photos/seed/conditional-value-at-risk/900/600" alt="A distribution curve with the tail highlighted, showing average of tail outcomes" />

<div class="wiki-infobox-caption">CVaR is the average loss in the tail, beyond VaR.</div>

|   |   |
|---|---|
| **What it is** | Average loss when losses exceed VaR threshold |
| **Also called** | Expected shortfall; tail loss; expected tail loss |
| **Example** | VaR = $1M loss; CVaR = average of losses exceeding $1M |
| **Relationship to VaR** | CVaR ≥ VaR always; VaR is not informative about tail magnitude |
| **Regulatory status** | Now required by Basel III; replacing VaR as primary metric |
| **Calculation** | Average of worst outcomes (e.g., worst 1%) or formula-based |
| **Advantage over VaR** | Captures severity of extreme losses, not just threshold |

</aside>

## How CVaR differs from VaR

**Value-at-Risk (VaR)** answers: "What is the loss threshold at a given confidence level?"
- 1-day 99% VaR = $1M: There is a 1% chance of losing more than $1M in one day.

**Conditional Value-at-Risk (CVaR)** answers: "Given that losses exceed the VaR threshold, what is the average loss?"
- 1-day 99% CVaR = $1.5M: On the worst 1% of days (when losses exceed $1M), the average loss is $1.5M.

The difference addresses VaR's critical weakness: VaR tells you the threshold, but not how bad tail losses actually are. A portfolio could have a $1M VaR and yet suffer $10M average losses on bad days. CVaR makes that visible.

## Example: VaR versus CVaR

Suppose historical 1-day returns for a portfolio are:
- 95 days: +0.5% to -0.5% (close to zero)
- 4 days: -2%, -3%, -4%, -5% (bad days)
- 1 day: -10% (catastrophic day)

Total: 100 days.

**VaR at 95% confidence (worst 5%):** The worst 5% includes days with -2%, -3%, -4%, -5%, -10%. The fifth-worst day is -5%. So the 1-day 95% VaR is $5 per $100 invested.

**CVaR at 95% confidence:** The average of the worst 5% is (-2 - 3 - 4 - 5 - 10) / 5 = -4.8%. So the 1-day 95% CVaR is $4.80 per $100 invested.

In this example, VaR and CVaR are similar. But consider a different distribution with a fatter tail:

- 95 days: +0.5% to -0.5%
- 4 days: -3%, -3%, -3%, -3%
- 1 day: -50%

**VaR at 95%:** The fifth-worst is -3%, so VaR = $3 per $100 invested.

**CVaR at 95%:** The average of worst 5% is (-3 - 3 - 3 - 3 - 50) / 5 = -12.40%. So CVaR = $12.40 per $100 invested.

Here, VaR is only $3, but CVaR reveals that tail losses are catastrophic, averaging $12.40. This is why CVaR is superior: it captures the real severity of extreme scenarios.

## Why regulators prefer CVaR to VaR

The [Basel III](/capital-adequacy) capital framework shifted from VaR to CVaR as the primary risk metric for banks. The reason: VaR is a threshold, but it does not measure the magnitude of losses beyond the threshold. During the 2008 crisis, banks had low calculated VaRs but suffered losses far exceeding those thresholds.

CVaR directly measures tail losses, forcing institutions to:
- Recognize the severity of extreme scenarios.
- Hold more capital for risks with fatter tails.
- Price tail risk more accurately in derivatives and loans.

## Calculating CVaR

**Method 1: Historical average of tail losses:**
Sort historical returns from worst to best. For 99% confidence level on 1,000 days of history, take the worst 10 days. Calculate the average loss over those 10 days. That is the 99% CVaR.

**Method 2: Parametric CVaR:**
If returns are assumed to follow a distribution (e.g., normal), CVaR can be calculated using formulas. For a normal distribution with mean μ and standard deviation σ, the 99% CVaR has a known formula.

**Method 3: Monte Carlo CVaR:**
Simulate thousands of scenarios, calculate portfolio loss for each, sort them, and take the average of the worst 1% (for 99% confidence). This handles complex portfolios with non-linear instruments.

## Relationship between VaR and CVaR

Mathematical property: **CVaR ≥ VaR always.**

This is intuitive: CVaR is the average of losses in the tail, and the threshold (VaR) is the worst of the non-tail outcomes. The average of tail losses is always at least as bad as the threshold.

If returns have a normal distribution, VaR and CVaR are close. If returns have fat tails, CVaR is much worse than VaR, making the tail risk visible.

## Limitations of CVaR

CVaR is better than VaR, but it still has limitations:

1. **Still depends on parameters.** If volatility or correlation estimates are wrong, CVaR will also be wrong.

2. **Tail data is sparse.** For 99% CVaR, you only have 10 days of tail data per 1,000 days of history. Those 10 days might not represent future tails well.

3. **Does not tell you the worst case.** CVaR is the average of tail losses. The absolute worst loss could be worse.

4. **Still assumes the past predicts the future.** A new type of tail event (a [black swan](/black-swan)) is not captured by historical CVaR.

Despite these, CVaR is materially better than VaR and is now the regulatory standard.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-risk](/value-at-risk) — the threshold metric that CVaR complements
- [Expected-shortfall](/expected-shortfall) — synonym for CVaR
- [Tail-risk](/tail-risk) — CVaR directly measures tail risk
- [Stress-testing](/stress-testing) — complements CVaR with scenario analysis
- [Basel capital](/capital-adequacy) — regulatory framework using CVaR

### Broader context

- [Model-risk](/model-risk) — CVaR estimates depend on distributional assumptions
- [Fat-tail-risk](/fat-tail-risk) — widens gap between VaR and CVaR
- [Black-swan](/black-swan) — tail events CVaR might miss
- [Risk management](/value-at-risk) — CVaR is modern standard
- [2008 financial crisis](/credit-risk) — prompted shift from VaR to CVaR

</div>

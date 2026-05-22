---
title: "Conditional Value at Risk Tail Risk"
description: "Average loss exceeding the Value at Risk threshold, measuring expected shortfall in the worst-case tail of a portfolio distribution."
keywords:
  - Conditional Value at Risk
  - CVaR
  - Expected Shortfall
  - tail risk
  - risk measurement
---

*Conditional Value at Risk (CVaR), also called Expected Shortfall (ES), measures the average loss a portfolio suffers on its worst days—specifically, the mean loss beyond the [value-at-risk](/wiki/value-at-risk/) threshold. While VaR answers "what loss might I face with 95% confidence?", CVaR answers "if I breach that threshold, what is my average loss?"*

Imagine a portfolio's daily losses are distributed like most financial assets: roughly bell-shaped but with fatter tails (more extreme outliers) than a normal distribution. VaR at the 95% confidence level might be $1 million—meaning there is a 5% chance the portfolio loses more than $1 million in a day. But that says nothing about the magnitude of losses in that tail 5%. They could average $1.2 million or $2.5 million.

CVaR captures that. It is the average loss given that the loss exceeds the VaR threshold. If VaR(95%) = $1M and CVaR(95%) = $1.5M, then on days when losses exceed $1M (the 5% worst days), the average loss is $1.5M.

<div class="wiki-hatnote">For the foundation, see [value-at-risk](/wiki/value-at-risk/). For related tail measures, see [expected-shortfall](/wiki/expected-shortfall/).</div>

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| **Confidence level** | Typically 95% or 99% |
| **Calculation method** | Average of all losses exceeding VaR threshold |
| **Data requirement** | Historical or simulated returns |
| **Interpretation** | Average loss in the worst tail |
| **Advantage over VaR** | Captures severity of tail, not just frequency |
| **Regulatory use** | Basel III, advanced risk frameworks |
| **Limitation** | Sensitive to tail model assumptions; difficult in very fat tails |

</aside>

## Why VaR alone is insufficient

VaR has a blind spot: it says nothing about the magnitude of losses beyond the threshold. Two portfolios can have identical 95% VaR but wildly different expected shortfall:

- **Portfolio A:** 5% of daily losses range from $1M to $1.1M. Expected shortfall = $1.05M.
- **Portfolio B:** 5% of daily losses range from $1M to $5M. Expected shortfall = $3M.

Both have VaR = $1M, but B is far riskier. This gap is especially important for portfolios with [fat-tail-risk](/wiki/fat-tail-risk/)—those exposed to rare but catastrophic moves. Hedge funds, leveraged strategies, and portfolios holding [junk-bond](/wiki/junk-bond/) positions or [credit-default-swap](/wiki/credit-default-swap/) are vulnerable to tail events that VaR alone misses.

The 2008 financial crisis highlighted this: many firms reported acceptable VaR levels days before massive losses. Their models failed to capture tail risk; historical data ended in the 1990s and early 2000s (a calm period), so the tails looked thin. When the real tail event arrived, losses were far larger than any confidence band.

## Calculation methods

**Historical CVaR** is the simplest: compute daily returns over a long historical period (often 1-2 years), rank them from worst to best, and average the worst 5% (for 95% CVaR). If you have 250 trading days, the 5% tail is the 12–13 worst days; CVaR is the mean of those losses.

**Parametric CVaR** assumes returns follow a known distribution (usually normal or Student's t). Given that assumption, CVaR can be computed analytically without iterating through historical data. The formula depends on the distribution; for a normal distribution with standard deviation σ and mean μ, CVaR at confidence level α is approximately:

CVaR(α) = μ − σ × φ(Φ^-1(α)) / (1 − α)

where φ is the standard normal density and Φ is the standard normal CDF.

**Simulation-based CVaR** runs thousands of Monte Carlo scenarios using assumed parameters and dependencies, then computes CVaR from the simulated returns. This is slower but flexible; it can incorporate [copula-dependence-strategy](/wiki/copula-dependence-strategy/) models and non-normal distributions.

Historical CVaR is most common in practice because it requires no distributional assumptions. But it has a weakness: the tail is data-sparse. If you have only 250 daily observations, the 95% tail has only 12 points—a small sample for averaging. So CVaR estimates have high statistical noise.

## Strengths relative to VaR

- **Captures tail magnitude.** VaR says "you won't lose more than $X with 95% confidence"; CVaR says "if you do, the average loss is $Y." Y matters for capital allocation.
- **Coherent risk measure.** CVaR satisfies all mathematical properties of a "coherent" risk measure, while VaR does not. Coherence ensures the measure does not incentivize bad behavior (like CVaR of a diversified portfolio being higher than the sum of individual CVaRs).
- **Useful for optimization.** [Risk-parity-strategy](/wiki/risk-parity-strategy/) and other allocation frameworks can minimize CVaR directly, which often produces more robust portfolios than minimizing variance alone.

## Weaknesses

- **Sparse tail data.** Historical CVaR for the 99% tail is based on just 2–3 observations out of 250 days. Unreliable for extreme confidence levels.
- **Model assumptions.** Parametric CVaR depends critically on the assumed distribution. If returns have fatter tails than the model assumes, CVaR is too low.
- **Hindsight bias.** Historical CVaR depends on *past* tail events. If the next tail event is different (unlikely correlated assets, new regime), historical CVaR is irrelevant.
- **Correlation assumptions break down in crises.** CVaR often assumes correlations remain stable. In reality, correlations spike during tail events—diversifying benefits evaporate when needed most.

## Use in risk governance

Major banks and investment firms compute CVaR as part of [stress-testing](/wiki/stress-testing/) frameworks. A typical policy might be:

- "Daily 95% CVaR shall not exceed $10M."
- "99% CVaR shall not exceed $30M."
- "Intra-day CVaR monitoring for illiquid positions."

Basel III and related regulatory frameworks encourage—but do not mandate—CVaR reporting alongside [value-at-risk](/wiki/value-at-risk/).

## Practical interpretation

If a fund reports "95% CVaR of $2M," interpret it as: "On the 5% of days when losses exceed our 95% VaR threshold, the average loss is $2M." For a [hedge-fund](/wiki/hedge-fund/) or [leveraged-etf](/wiki/leveraged-etf/), this is critical information. A 2% daily CVaR is more risky than a 1% daily CVaR, even if both have the same VaR.

---

<div class="wiki-seealso">

### Closely related
- [value-at-risk](/wiki/value-at-risk/) — The VaR foundation
- [expected-shortfall](/wiki/expected-shortfall/) — Alias for CVaR
- [fat-tail-risk](/wiki/fat-tail-risk/) — Problem CVaR addresses
- [stress-testing](/wiki/stress-testing/) — Risk governance context

### Wider context
- [tail-risk-hedging](/wiki/tail-risk-hedging/) — Strategies to mitigate tail exposure
- [credit-default-swap](/wiki/credit-default-swap/) — Instrument with tail risk
- [leverage-ratio-forex](/wiki/leverage-ratio-forex/) — Leveraged positions amplify tail risk
- [risk-parity-strategy](/wiki/risk-parity-strategy/) — Portfolio construction using CVaR

</div>

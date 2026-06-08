---
title: "Maximum Drawdown vs Value at Risk"
description: "Compare maximum drawdown and value at risk—two downside metrics—to understand when each reveals the true risk in a portfolio."
keywords:
  - maximum drawdown vs value at risk
  - drawdown analysis
  - value at risk metric
  - portfolio downside risk
  - tail risk measurement
  - volatility metrics
---

*Maximum drawdown and [value at risk](/value-at-risk/) are the two most common ways to quantify how much a portfolio can lose, but they measure risk in opposite ways. **Maximum drawdown** is empirical: the biggest peak-to-trough decline a portfolio has actually experienced (or is likely to experience). **Value at risk** (VaR) is probabilistic: the maximum loss expected within a certain confidence level (e.g., 95%) over a specific time horizon. Neither is sufficient alone; together, they reveal whether a portfolio's worst historical loss is a one-off [tail risk](/tail-risk/) or a typical stress scenario.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maximum Drawdown vs Value at Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two complementary lenses on downside risk: one looks backward at experience, one predicts forward-looking probability.</div>

|   |   |
|---|---|
| **Maximum Drawdown** | Largest peak-to-trough percentage loss in portfolio history (e.g., −37% from January 2008 to March 2009) |
| **Value at Risk** | Loss magnitude below which you expect to fall in only 5% of scenarios (e.g., −8% in a single month at 95% confidence) |
| **Time horizon** | Drawdown spans months to years; VaR is typically 1 day to 1 month |
| **Strengths (Drawdown)** | Intuitive, easy to communicate, captures true historical stress |
| **Strengths (VaR)** | Probabilistic, accounts for tail behavior, comparable across portfolios |
| **Weaknesses (Drawdown)** | Only one data point; misses scenarios worse than history |
| **Weaknesses (VaR)** | Model-dependent, can underestimate rare events; gives false precision |
| **Best practice** | Use both; supplement with conditional VaR and [stress testing](/stress-testing/) |

</aside>

## Maximum Drawdown: The Historical Lens

Maximum drawdown asks: *What is the worst investors have actually suffered?*

It is calculated as the percentage decline from a portfolio's all-time peak to its subsequent lowest trough. If a portfolio reaches $1 million in July 2021, falls to $630,000 in March 2022, and then recovers, the drawdown is 37%.

**Why this matters:** A retiree or institutional investor managing withdrawals cares deeply about drawdown because it directly translates into reduced income. During the 2008 financial crisis, many equity portfolios experienced 50% drawdowns; investors who panicked and sold locked in those losses permanently. Drawdown is not theoretical—it is the ceiling on losses that real people have endured.

**Limitation:** Maximum drawdown is a single historical data point. A portfolio with a 20% max drawdown may be unusually lucky—its worst loss happened to occur in a decade of mild recessions. Or it may be genuinely less risky. Drawdown alone does not distinguish between the two.

## Value at Risk: The Forward-Looking Lens

Value at risk (VaR) asks: *If adverse conditions occur, how bad could it plausibly get?*

VaR is typically stated as: "95% VaR over 1 month is −8%," meaning there is a 95% probability the portfolio will not lose more than 8% in any given month. Equivalently, a 5% chance (1 in 20 months) of losses exceeding −8%.

**How it is calculated:**
1. Gather historical returns for the portfolio's assets over the relevant time period.
2. Simulate forward returns using the distribution implied by history (mean, variance, correlations).
3. Identify the loss level below which 5% of simulated outcomes fall.

For a simple example: a portfolio with average monthly return of 0.8% and standard deviation of 3.5%. Assuming returns follow a normal distribution, a 95% VaR (worst 5% of months) is roughly: 0.8% − (1.645 × 3.5%) = −5.0%.

**Why this matters:** VaR forces investors to think probabilistically about tail risk. It prevents the false comfort that "well, we haven't had a 40% loss yet, so it won't happen." VaR says: based on volatility and distribution of returns, a major loss is not only possible but predictable in frequency.

**Limitation:** VaR assumes returns follow a known distribution (usually normal), which is wrong during crises. Market returns have fatter tails than a normal distribution predicts. A 95% VaR might promise you will not lose more than 8% in 95% of months, but history shows losses exceed 8% far more often than 5% of the time. VaR also gives a false sense of precision (−8.1% vs −8.3%) that does not exist in practice.

## When They Diverge: Two Real Examples

**Example 1: A Stock-Heavy Equity Fund**

- **Historical maximum drawdown:** −42% (2008 crisis)
- **95% VaR (monthly):** −12%
- **Interpretation:** This fund has experienced a 42% loss in the past, but the typical bad month (worst 5%) is a 12% loss. The 42% was an extreme multi-month cascade. An investor thinking only in VaR terms might assume 12% is the ceiling; they would be blindsided by the next 40%+ crisis.

**Example 2: A Bond and Commodity Portfolio**

- **Historical maximum drawdown:** −18% (2022 rate shock)
- **95% VaR (monthly):** −8%
- **Interpretation:** The drawdown is much larger than VaR suggests. This portfolio's largest loss came from a rare, rapid interest-rate shock. Normal volatility (on which VaR is based) underestimated the tail event. VaR failed to capture the true downside threat.

## Conditional VaR: A Middle Ground

**Conditional VaR** (also called expected shortfall) mitigates VaR's blind spot. Instead of asking "what is the 95% loss level?" it asks: "Given that a loss is in the worst 5%, what is the *average* loss in that scenario?"

For a portfolio with a 95% VaR of −8%, conditional VaR might be −14%. This says: on the 5% of months when losses exceed −8%, the typical loss is −14%. Conditional VaR more closely matches historical tail experience than standard VaR.

## Stress Testing: When Models Fail

Both maximum drawdown and VaR rely on historical patterns. Neither captures unprecedented shocks. During the COVID-19 crash in March 2020, many bond [ETFs](/etf/) lost 10–15% in days—far beyond their historical drawdowns or VaR estimates. The underlying assumption (past volatility predicts future volatility) broke down.

**Stress testing** compensates by asking: "If interest rates rise 300 basis points in one quarter?" or "If equity volatility doubles?" without relying on historical precedent. Stress tests are model-driven scenarios, not probabilities; they answer "can we survive *if* X happens?" rather than "what is the probability X happens?"

## Practical Use: The Risk Dashboard

A complete portfolio risk picture uses all three:

| Metric | Use | Question Answered |
|--------|-----|-------------------|
| Max Drawdown | Communicate to trustees, sponsors, or retirees | What is the worst we've seen and might see again? |
| VaR (95%, 1-month) | Daily risk monitoring and [margining](/margin-call-forex/) | What is the normal bad outcome? |
| Conditional VaR | Reserve capital and set spending bounds | If the tail occurs, how much can we afford to lose? |
| Stress test (e.g., +300bps rates) | Board/risk committee discussions | Can we survive an extreme scenario? |

A portfolio with a 25% maximum drawdown, a 6% VaR, and conditional VaR of 12% is telling you: "In a typical bad month, expect a 6% loss; in a true crisis (like 2008), expect 12–15%; and history shows we can lose 25% over a multi-year cycle."

## When to Favor Each Metric

**Favor maximum drawdown if:**
- You are a retiree or managing a endowment with fixed spending—you care about the true worst-case lived experience.
- You have limited recovery time and cannot stomach multi-year drawdowns.
- You want a simple, conversation-friendly number.

**Favor value at risk if:**
- You are a day trader or short-term trader—you care about daily P&L bounds.
- You manage a large institution with [margin](/margin-call-forex/) requirements or collateral constraints—you need a daily risk number.
- You want a probabilistic, forward-looking framework.

**Use both if:**
- You are a long-term investor, especially retired—understanding both typical bad months and rare historical crashes matters.
- You are reporting to boards or regulators who demand both backward-looking and forward-looking risk measures.

## See also

<div class="wiki-seealso">

### Closely related

- [Value at Risk](/value-at-risk/) — the full technical definition and calculation methods
- [Tail Risk](/tail-risk/) — losses in the extreme distribution tails that historical models miss
- [Stress Testing](/stress-testing/) — scenario analysis of portfolio behavior in unprecedented shocks
- Conditional VaR — expected loss conditional on exceeding the VaR threshold
- [Volatility Smile](/volatility-smile/) — why real markets have fatter tails than models assume
- [Risk Budgeting for Retirees](/risk-budgeting-for-retirees/) — how retirees allocate drawdown tolerance

### Wider context

- [Sharpe Ratio](/sharpe-ratio/) — risk-return tradeoff for comparing portfolios
- [Beta](/beta/) — market-relative risk for equity portfolios
- [Diversification](/diversification/) — how to reduce portfolio drawdowns
- Portfolio Allocation — how asset allocation drives downside risk

</div>

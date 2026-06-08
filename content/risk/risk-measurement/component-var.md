---
title: "Component Value at Risk"
description: "The portion of a portfolio's total VaR attributable to each individual holding, showing how much risk each position contributes."
keywords:
  - value at risk
  - risk attribution
  - portfolio decomposition
  - risk management
  - position risk
image: "/svg/risk.svg"
---

*The **component value at risk** (or component VaR) is the portion of a portfolio's total [value at risk](/value-at-risk/) that stems from each individual position. It answers: of my total daily loss limit at the 95th percentile, how much comes from my S&P 500 holdings, how much from my bonds, how much from my foreign exchange exposure? Component VaR decomposes aggregate portfolio risk into pieces, each pinned to a specific holding.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Component Value at Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">The risk contribution of each position, summing to total portfolio VaR.</div>

|   |   |
|---|---|
| **Core insight** | Sum of component VaRs equals total portfolio VaR |
| **Calculation basis** | Position size × [Beta](/beta/) (or sensitivity) × [Volatility](/historical-volatility/) |
| **Time horizon** | 1 to 10 days (model dependent) |
| **Confidence level** | 95% or 99% |
| **Use case** | Risk reporting; position monitoring; limit setting |
| **Versus** | [Marginal VaR](/marginal-var/) (incremental risk of new trades) |

</aside>

## The decomposition logic

Every portfolio has a total daily [value at risk](/value-at-risk/)—the amount of money it could lose, at a chosen confidence level (typically 95% or 99%), in one trading day under normal market conditions. That total risk is not monolithic; it comes from somewhere. Component VaR disaggregates it by source.

If a portfolio of stocks, bonds, and currencies has a total daily VaR of USD 10 million at the 95% confidence level, component VaR shows that USD 6 million comes from equities, USD 3 million from fixed income, and USD 1 million from currency positions. This is intuitive for any portfolio manager: you want to know where the risk lives.

The sum of all positions' component VaRs equals the portfolio's total VaR. This additive property is central to risk reporting and governance. A trader cannot claim, truthfully, that their individual positions account for more than the total portfolio risk; component VaR enforces consistency.

## Calculation approaches

The simplest component VaR formula is:

**Component VaR = Position Size × Correlation × Portfolio σ**

where Portfolio σ is the portfolio's overall standard deviation, and Correlation is the position's correlation to the portfolio return. This approach, rooted in beta from [capital asset pricing model](/capital-asset-pricing-model/) theory, assumes a normal distribution of returns.

A more precise method, used in variance-covariance and stress-testing frameworks, calculates VaR for the full portfolio, then re-runs it excluding the target position. The difference is component VaR for that position. This avoids the assumption of normality and captures nonlinear effects.

In practice, most banks use a hybrid: a delta-based (linear) approximation for straightforward instruments, and a full revaluation for options and other nonlinear exposures.

## Why component VaR matters: seeing concentration

Component VaR is the primary tool for understanding where risk concentrates. A portfolio might have dozens or hundreds of holdings, but component VaR ranks them by their marginal contribution to total risk. The risk manager sees immediately which positions are eating the risk budget.

A trader holding a huge position in an asset with low [volatility](/historical-volatility/) might have low component VaR if that asset is uncorrelated with the rest of the book. A small position in a highly correlated, volatile asset might have high component VaR. This is the insight of diversification made concrete: size is not the same as risk.

Component VaR also supports position-limit setting. A risk manager might impose a limit of "no single position may account for more than 15% of portfolio VaR." This is far more sophisticated than a notional limit (e.g., "no position larger than USD 10 million") because it accounts for risk characteristics. A EUR 100 million position in a low-volatility bond index might satisfy the VaR limit, while a EUR 1 million position in a penny stock might violate it.

## The aggregation: proof that the numbers work

One of the great strengths of component VaR is that it is auditable. The sum of component VaRs across all positions equals total portfolio VaR. This property holds because of the linear relationship between position size and risk (under normal market conditions). If the sum does not match—due to model error, data lag, or correlated changes during the reporting period—something is wrong, and the risk manager knows to investigate.

This additive property also enables hierarchical reporting. Component VaR can be aggregated by asset class, by geography, by counterparty, or by desk. A fixed-income desk manager can see the component VaR of equities in their portfolio; the chief risk officer can roll it up by desk and by firm.

## Limitations: nonlinearity and tail events

Component VaR's core assumption—that risk scales linearly with position size—breaks down in several ways. Options exhibit [convexity](/convexity/); a long call becomes infinitely sensitive to the underlying asset at low prices and insensitive at high prices. Component VaR based on delta alone will misrepresent the option's risk if price movements are large.

More seriously, component VaR is calibrated to normal market conditions. It captures historical [volatility](/historical-volatility/) and correlation. When a crisis arrives—a credit spread shock, a geopolitical event, a fire sale—volatility and correlation can spike. Positions that appeared to have low component VaR under calm conditions can explode in drawdown. The 2008 financial crisis and 2020 COVID panic both revealed that component VaR, as reported, badly underestimated tail risk.

Estimating correlation itself is treacherous. Component VaR relies on the sample correlation between each position and the portfolio over some lookback window (typically 1–3 years of daily data). But correlation is unstable; it shifts with economic regime. In bull markets, correlations are low; in bear markets, they spike. A holding that appears diversifying in calm times may be the most correlated asset in a crash.

## Relationship to marginal VaR

Component VaR and [marginal VaR](/marginal-var/) are often confused because they both measure risk contribution, but they apply to different questions.

Component VaR asks: of my existing risk, what do I have? It decomposes the risk you already own.

Marginal VaR asks: if I add a new trade, how much incremental risk do I incur? It forecasts the impact of a proposal.

A position you own might have high component VaR (it contributes substantially to portfolio risk), but low marginal VaR (adding more of it would barely change portfolio risk, because you already hold enough of it to capture the diversification benefit). Conversely, a position with low component VaR might have high marginal VaR if the portfolio is underweight in a diversifier.

In practice, traders use component VaR for daily monitoring and marginal VaR for trading decisions.

## Implementation in risk dashboards

Risk systems calculate component VaR daily, often multiple times per day as positions change. It appears in trader dashboards, showing each position's contribution to the day's VaR limit. A trader who sees that a single equity position accounts for 25% of their desk's VaR limit might be motivated to trim or hedge it, not because the position itself is bad, but because it is consuming too much of the shared risk budget.

Senior management reviews component VaR by asset class and geography, tracking whether risk is concentrating where it should be. If equities account for 80% of portfolio VaR but represent only 30% of notional capital, questions arise: is the portfolio too equity-heavy, or are equities simply more volatile than bonds?

## See also

<div class="wiki-seealso">

### Closely related

- [Value at risk](/value-at-risk/) — the total portfolio metric that component VaR decomposes
- [Marginal VaR](/marginal-var/) — the incremental risk of adding a new position
- [Beta](/beta/) — the sensitivity used in component VaR calculation
- [Volatility](/historical-volatility/) — input to risk measurement frameworks
- [Diversification](/diversification/) — the principle that component VaR makes quantitative
- [Risk budgeting](/risk-budgeting/) — allocation of total VaR limits using component VaR

### Wider context

- [Stress testing](/stress-testing/) — complements component VaR by testing tail outcomes
- [Portfolio risk](/market-risk/) — the broader discipline of portfolio measurement
- Capital allocation — uses component VaR to decide how much risk each business should take

</div>

---
title: "Risk Budgeting in Portfolio Allocation"
description: "Risk budgeting allocates a fixed total risk budget across positions based on risk contribution rather than dollar weight, with worked examples."
keywords:
  - risk budgeting portfolio
  - portfolio allocation by risk
  - risk parity
  - risk contribution
  - volatility-based allocation
image: /svg/risk.svg
---

*In **risk budgeting**, an investor assigns each position or asset class a target share of the portfolio's total risk—not its dollar weight. A volatile tech stock might represent 5% of dollars but 20% of portfolio risk; a defensive utility might be 10% of dollars but only 5% of risk. The goal is to have each holding contribute proportionally to overall volatility, so no single bet can derail the entire strategy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Budgeting — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Allocate risk, not just dollars, to balance contribution across holdings.</div>

|   |   |
|---|---|
| **Core idea** | Target % of total portfolio risk per position, not % of dollars |
| **Risk metric** | Volatility (standard deviation) or [value-at-risk](/value-at-risk/) |
| **Risk contribution** | Position size × volatility × correlation to portfolio |
| **Extreme case** | Risk parity: equal risk weight across all holdings |
| **Advantage** | Prevents concentration risk; diversifies by risk, not just assets |
| **Disadvantage** | Requires frequent rebalancing; correlation assumptions matter greatly |
| **Suitable for** | Institutional portfolios, hedge funds, systematic traders |

</aside>

## Beyond Dollar Weighting

Traditional portfolio construction allocates by dollar weight: "I'll put 60% in stocks, 30% in bonds, 10% in alternatives." This approach is intuitive but flawed. A 60% stock allocation means nothing if 50% of those dollars are in a single volatile tech mega-cap. Meanwhile, a 30% bond allocation might contribute only 5% of portfolio volatility because bonds are stable.

Risk budgeting inverts the perspective. Instead of asking "how much money should this position get?", ask "how much of my total acceptable risk should this position take?" An investor willing to accept, say, 12% annual portfolio volatility might decide: "I'll give tech stocks a 4% risk budget, bonds a 3% budget, emerging markets a 3%, and alternatives 2%." Each bucket gets a slice of the total risk pie.

The advantage is control. In a dollar-weighted portfolio, a sharp drawdown in stocks can blow past the investor's loss tolerance. In a risk-budgeted portfolio, the investor has explicitly decided how much volatility each position can contribute, so large drawdowns are less likely to surprise.

## A Worked Example

Assume an investor has $1 million and a 12% total portfolio risk target (measured as annual volatility). She wants to allocate across three assets: U.S. stocks (S&P 500), investment-grade bonds, and a diversified hedge fund.

**Asset characteristics (hypothetical):**
| Asset | Volatility | Expected Return | Correlation to Portfolio |
|---|---|---|---|
| S&P 500 stocks | 16% | 8% | 0.95 |
| Investment-grade bonds | 6% | 3% | 0.30 |
| Hedge fund | 8% | 6% | 0.50 |

**Step 1: Assign risk budgets.** The investor decides:
- Stocks: 6% of portfolio risk
- Bonds: 3% of portfolio risk
- Hedge fund: 3% of portfolio risk
- **Total: 12% portfolio risk** (her target)

**Step 2: Calculate position sizes.** Risk contribution = position size × asset volatility × (correlation effect). This is simplified; the full formula uses the asset's marginal contribution to portfolio volatility. But intuitively:

- To get stocks to 6% risk: Size = 6% ÷ (16% × 0.95) ≈ $395,000
- To get bonds to 3% risk: Size = 3% ÷ (6% × 0.30) ≈ $167,000
- To get hedge fund to 3% risk: Size = 3% ÷ (8% × 0.50) ≈ $225,000
- **Total: ~$787,000** (leaves ~$213,000 unallocated or in cash)

**Step 3: Verify.** With these sizes and correlations, the portfolio volatility should be close to 12%. Actual portfolio volatility depends on correlations, which vary; this is where risk budgeting requires discipline: if correlations spike (e.g., bonds and stocks both fall in a crisis), realized volatility could exceed the budget.

## Risk Contribution vs. Dollar Weight

In the example above:
- Stocks: 40% of dollars, 50% of portfolio risk
- Bonds: 17% of dollars, 25% of portfolio risk
- Hedge fund: 23% of dollars, 25% of portfolio risk

Notice how stocks dominate risk despite being less than half the portfolio by value. Bonds contribute less risk than their dollar weight because their low correlation to stocks provides diversification. The hedge fund, with mid-range volatility and correlation, contributes risk closer to its dollar weight.

This misalignment is the whole point. A naive investor might have constructed "60% stocks, 30% bonds, 10% alternatives" by dollar weight—which would mean 70%+ of portfolio risk comes from stocks. A sudden 20% stock crash would then hit much harder than her 12% volatility target suggested. Risk budgeting prevents this surprise.

## The Risk Parity Extreme

One version of risk budgeting is **risk parity**: allocate so each position contributes *exactly* the same risk. With the three assets above, risk parity might allocate roughly 50% to bonds (low volatility, stable), 30% to stocks, and 20% to alternatives. Bonds dominate by dollar weight because they're less volatile.

Risk parity sounds appealing: no asset class can derail the portfolio. But it requires constant rebalancing. As volatility changes or correlations shift, positions drift away from equal risk contribution, and the portfolio must be rebalanced frequently (which incurs trading costs and taxes). Moreover, risk parity's equal risk allocation is somewhat arbitrary—there's no reason equal risk is "right" for every investor.

## Challenges and Limitations

**Estimation risk.** Risk budgeting relies on estimates of volatility and correlation. If the estimates are wrong, the actual risk contribution will be wrong. During crises, correlations can spike unexpectedly: bonds fall alongside stocks, equities become more correlated across regions. A portfolio that seemed risk-balanced during calm periods can become concentrated in one underlying risk factor.

**Concentration in macro factors.** A risk-budgeted portfolio might appear diversified (many holdings, multiple asset classes), but if all holdings are exposed to the same macro driver—say, interest rates—the portfolio has macro concentration risk. A sharp interest rate shock can hurt stocks, bonds, and alternatives simultaneously, even if individual volatilities seemed balanced.

**Rebalancing costs.** Maintaining constant risk contribution requires frequent trading, especially in volatile markets. Transaction costs and taxes can erode returns, offsetting the risk-management benefits.

**Non-normal returns.** Standard deviation (volatility) assumes normal distributions. In reality, returns have fat tails: crashes happen more often and are more extreme than a normal distribution predicts. Risk budgets based on volatility alone miss [tail risk](/tail-risk/).

## Risk Budgeting in Practice

Institutional investors—pension funds, endowments, large hedge funds—often use risk budgeting frameworks. They can afford the modeling, rebalancing, and governance. Individual investors rarely do, partly because the data and calculations are complex.

A simplified version for individuals: periodically calculate each holding's "risk contribution" using free tools or spreadsheets. Ask: "If this position drops 5%, how much would my entire portfolio drop?" If the answer is "more than proportional to its dollar weight," that position is concentrating risk. Consider trimming it and reallocating to less correlated holdings.

Over time, risk budgeting enforces diversification by a deeper logic than dollar-weight allocation: you're controlling the actual sources of volatility, not just counting positions or asset classes.

## See also

<div class="wiki-seealso">

### Closely related

- [Asset Allocation](/asset-allocation/) — The strategic framework for dividing capital; risk budgeting is an advanced variant.
- [Diversification](/diversification/) — Spread investments to reduce unsystematic risk; risk budgeting spreads risk itself.
- [Value-at-Risk](/value-at-risk/) — A quantitative measure of maximum potential loss; often used alongside risk budgets.
- [Volatility](/implied-volatility/) — The key metric in risk budgeting; understand how it's measured and forecast.
- [Concentration Risk](/concentration-risk/) — The opposite of balanced risk budgeting; what you're trying to avoid.

### Wider context

- [Risk Parity](/stock-market/) — A specific implementation of risk budgeting where each position has equal risk weight.
- [Correlation](/business-cycle/) — How assets move together; critical input to risk contribution calculations.
- [Portfolio Rebalancing](/asset-allocation/) — The discipline required to maintain risk budgets over time.
- [Mean-Variance Optimization](/capital-asset-pricing-model/) — Mathematical foundation for risk-based portfolio construction.

</div>

---
title: "Incremental Value at Risk"
description: "The marginal risk contribution of adding a new position to an existing portfolio, measured as the change in portfolio VaR."
keywords:
  - incremental value at risk
  - marginal risk
  - portfolio risk
  - value at risk
  - risk attribution
  - diversification benefit
---

*The **incremental value at risk (IVaR)** of a position is the change in a portfolio's [value at risk](/wiki/value-at-risk/) if that position is added to (or removed from) the portfolio. It captures both the position's standalone risk and how it correlates with existing holdings. A position with high standalone [volatility](/wiki/volatility-index-option/) may have low IVaR if it is negatively correlated with the rest of the portfolio.*

IVaR is used by portfolio managers, [risk officers](/wiki/operational-risk/), and asset allocators to size positions and decide whether adding an asset improves or worsens portfolio risk. It differs from [conditional value at risk (CVaR)](/wiki/conditional-value-at-risk/) (tail-risk focused) and standard [VaR](/wiki/value-at-risk/) (portfolio-level risk), though all three are used together in modern risk frameworks.

<aside class="wiki-infobox">

| Dimension | Definition |
|-----------|-----------|
| **Formula** | IVaR = Portfolio VaR (with position) - Portfolio VaR (without position) |
| **Unit** | Dollars or basis points (change in VaR) |
| **Interpretation** | How much portfolio VaR increases (or decreases) by adding the position |
| **Key driver** | Correlation with existing portfolio; not position size alone |
| **Use case** | Position sizing, [hedging](/wiki/hedge-fund/), [asset allocation](/wiki/asset-allocation/) decisions |
| **Contrast** | VaR measures absolute portfolio risk; IVaR measures marginal contribution |

</aside>

## The Logic of Incremental Risk

Suppose a portfolio's [VaR](/wiki/value-at-risk/) (95% confidence, one-day horizon) is $100,000. The portfolio manager wants to add a $10M position in a [volatile commodity future](/wiki/commodity-futures-rolling/). If the new portfolio VaR becomes $115,000, the IVaR of the new position is $15,000. This means the addition increased portfolio risk by $15,000.

Whether this is acceptable depends on the expected return of the commodity position and the portfolio's risk budget. If the expected return justifies $15,000 of additional daily risk, add it. If not, reduce the position size or reject it.

Critically, the IVaR is not simply the position's standalone VaR. A $10M commodity position might have a standalone VaR of $50,000 (if commodities are volatile). But if commodities are negatively correlated with the rest of the portfolio (which is long equities and bonds), the IVaR might be only $5,000 — or even negative if the commodity acts as a hedge. This is the essence of [diversification](/wiki/diversification/): adding a negatively correlated asset reduces portfolio risk even if the asset itself is risky.

## Relationship to Marginal VaR

Incremental VaR is closely related to **marginal VaR (MVaR)**, which is the derivative of portfolio VaR with respect to the position size. Mathematically:

**MVaR ≈ IVaR / ΔPosition Size**

If adding a $1M position increases portfolio VaR by $5,000, then the MVaR is approximately $5 per million added. This marginal cost is useful for sizing: if you want to limit the portfolio's daily VaR to $150,000, and adding commodities costs $5M per $1M exposure, you know you can add about $10M of commodities before hitting your VaR budget.

In practice, portfolio managers work with both IVaR (for discrete yes/no decisions about adding a position) and MVaR (for continuous sizing decisions).

## Calculating IVaR

The calculation depends on the [VaR methodology](/wiki/historical-var/). For a [parametric (delta-normal) VaR](/wiki/delta-normal-var/) model:

1. Compute the portfolio VaR at a given confidence level (e.g., 95%).
2. Add the proposed position (at the proposed size) to the portfolio.
3. Compute the new portfolio VaR.
4. IVaR = New VaR - Old VaR.

For [historical simulation](/wiki/historical-var/), the same logic applies: re-run the historical scenarios with the new position included.

For a [Monte Carlo VaR](/wiki/monte-carlo-var/) model, the calculation is more computationally intensive but conceptually identical: simulate future returns including the new position, compute the VaR percentile, and subtract the baseline VaR.

## IVaR and Risk Attribution

Portfolio risk attribution—decomposing total portfolio VaR into contributions from each position—uses incremental VaR as a building block. If a portfolio has 50 holdings, each holding's contribution to total VaR is approximately its IVaR.

This allows managers to answer questions like: "Which positions are contributing most to portfolio risk?" and "If I liquidate position X, how much risk do I shed?" Positions with high IVaR relative to their expected return are candidates for reduction or replacement.

A position might have high standalone risk but low IVaR (because it hedges existing risks), making it attractive to hold. Conversely, a position with low standalone risk but high IVaR (because it correlates strongly with existing holdings) may be a candidate to reduce, since it adds redundant risk.

## Practical Constraints

IVaR is forward-looking and assumes [correlations](/wiki/correlation-coefficient/) and [volatility](/wiki/historical-volatility/) remain constant. During market stress (a [black swan](/wiki/black-swan/) event or financial crisis), correlations can spike abruptly — a position that appeared to be a good hedge (negative correlation) may become highly correlated with the rest of the portfolio, causing its IVaR to soar unexpectedly.

This is why sophisticated firms complement IVaR with [stress testing](/wiki/stress-testing/) and [scenario analysis](/wiki/scenario-analysis/). They ask: "If a credit shock occurs and correlations move to crisis levels, what is the IVaR of each position then?" This reveals hidden tail risks that VaR and IVaR alone might miss.

Additionally, IVaR assumes the position can be liquidated or hedged at current prices. In a [liquidity crisis](/wiki/liquidity-crisis/), the realized cost of unwinding a position might far exceed the IVaR estimate.

## IVaR vs. Standalone Risk

A common error is confusing a position's standalone [volatility](/wiki/historical-volatility/) with its IVaR. A highly volatile asset (e.g., a call option or emerging-market equity) may have high standalone volatility but low IVaR if it is uncorrelated or negatively correlated with existing holdings.

A financial advisor might tell you, "We've added 5% in emerging-market bonds to your portfolio. They're volatile, but they're not correlated with your U.S. equities, so portfolio risk barely budged." This is IVaR logic: the bonds add diversification value despite their standalone risk.

## Role in Position Sizing

Many hedge funds and asset managers use IVaR as a formal constraint on position sizing. They set a limit on how much aggregate IVaR the portfolio can have — say, "no more than $500,000 in portfolio VaR" — then size each new position such that its IVaR is proportional to its expected return and liquidity.

A position with high expected return and low liquidity might be capped at IVaR of $100,000. A position with moderate return and good liquidity might be capped at $50,000. This ensures the portfolio is neither too concentrated in any single position nor too diluted to capture alpha.

<div class="wiki-seealso">

### Closely related
- [Value at risk](/wiki/value-at-risk/) — the baseline portfolio risk metric
- [Conditional value at risk](/wiki/conditional-value-at-risk/) — tail risk beyond VaR
- [Correlation coefficient](/wiki/correlation-coefficient/) — determines the diversification benefit
- [Volatility](/wiki/historical-volatility/) — the standalone risk of a position
- [Risk attribution](/wiki/portfolio-mental-accounting/) — decomposing portfolio risk

### Wider context
- [Asset allocation](/wiki/asset-allocation/) — using IVaR to optimize portfolio construction
- [Hedge fund](/wiki/hedge-fund/) — active users of IVaR for position sizing
- [Stress testing](/wiki/stress-testing/) — testing IVaR estimates under extreme scenarios
- [Black swan](/wiki/black-swan/) — events that invalidate IVaR estimates
- [Operational risk](/wiki/operational-risk/) — broader risk measurement framework

</div>

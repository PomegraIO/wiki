---
title: "Cointegration Strategy"
description: "A trading strategy that exploits mean-reverting relationships between correlated assets that share a long-term equilibrium."
keywords:
  - cointegration
  - mean reversion
  - statistical arbitrage
  - pairs trading
---

*A **cointegration strategy** is a [quantitative trading](/quantitative-investing/) approach that identifies two or more assets whose prices move together in the long run despite short-term divergences. The strategy trades the spread between correlated assets, betting that the relationship will revert to equilibrium. Cointegration differs from simple [correlation](/correlation-coefficient/) — cointegrated assets may diverge temporarily but are mathematically constrained to realign.*

<div class="wiki-hatnote">Part of [Statistical Arbitrage](/statistical-arbitrage/) and related to [Pairs Trading](/pairs-trading/), which use similar mechanics.</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Core premise** | Two assets share a stable long-term relationship despite short-term noise |
| **Mathematical basis** | Both assets are I(1); their combination is I(0) (stationary) |
| **Trade signal** | Spread widens → exploit mean reversion |
| **Entry rule** | Open position when spread exceeds historical bands |
| **Exit rule** | Close when spread mean-reverts to equilibrium |
| **Holding period** | Days to weeks (or months for fundamental pairs) |
| **Risk** | Cointegration relationship can break; model risk |

</aside>

## What cointegration means mathematically

Two assets are cointegrated if they both follow a random walk (integrate to I(1)), but their linear combination is stationary (I(0)). In plain English: each asset wanders seemingly randomly, but their difference is stable and mean-reverting.

Example: Two oil stocks (Company A and Company B) both follow random walks individually — price changes are unpredictable day-to-day. But their ratio is stable because they have similar exposure to oil prices, production costs, and long-term fundamentals. When the ratio widens (A outperforms B significantly), it eventually narrows again. This is cointegration.

The mathematical relationship is: P_A(t) = k * P_B(t) + constant + noise. Over time, the noise is mean-reverting. A statistical test (the Johansen test or Augmented Dickey-Fuller on the residuals) can confirm whether two assets are cointegrated.

## Cointegration vs. simple correlation

[Correlation](/correlation-coefficient/) measures how two assets move together in the short term. Two assets can be correlated but not cointegrated. Imagine two assets that both trend upward but at different rates — they might have +0.8 correlation, but if both are random walks, they are not cointegrated. They will diverge indefinitely.

Cointegration is stronger: it implies a stable long-term relationship. Cointegrated assets may diverge, but the divergence is temporary and bounded. This makes cointegration more reliable for mean-reversion trading.

## Building and backtesting a cointegration strategy

A typical cointegration strategy workflow is:

1. **Universe selection:** Screen for pairs or baskets with cointegration. The universe might be sector peers (two bank stocks), commodity-linked stocks (oil companies), or stocks with similar business models.

2. **Cointegration testing:** Calculate the spread (residual) between the paired assets. Run statistical tests (Dickey-Fuller) to confirm stationarity and mean reversion.

3. **Parameter estimation:** Estimate the equilibrium relationship using ordinary least squares (OLS) regression. The slope coefficient is the hedge ratio.

4. **Trading rules:** Define entry signals (spread exceeds 2σ of its historical distribution), exit rules (spread reverts to mean), and position sizing.

5. **Backtesting:** Simulate the strategy over historical data, accounting for transaction costs, slippage, and drawdowns.

6. **Monitoring:** Track whether the cointegration relationship is still present; if it breaks down, exit the position.

## Real-world examples: sectors and economic relationships

Natural cointegration pairs include:

- **Commodity-linked stocks:** Oil prices and energy stock valuations. Oil Majors (ExxonMobil, Chevron, Shell) have different leverage, geographies, and cost structures, but all correlate to crude oil. Pairs of oil stocks often cointegrate.

- **Two banks:** Two commercial banks in the same country operate in similar regulatory and interest-rate regimes. Their spread can mean-revert based on relative asset quality, efficiency, or exposure to specific borrower segments.

- **ETFs with overlap:** Two semiconductor ETFs track different indices but with significant overlap in holdings. Their valuations may diverge temporarily but are constrained by arbitrage.

- **Cash and derivatives:** A stock and its [index futures](/futures-contract/) contract should be tightly cointegrated. Divergences trigger cash-and-carry or reverse cash-and-carry arbitrage.

## The role of hedging and [leverage](/leverage-ratio-forex/)

A cointegration strategy typically involves long one asset and short the other — a "market-neutral" or "hedge-fund" style position. This removes [systematic risk](/systematic-risk/): if the overall market falls, the long position loses but the short position gains, offsetting the loss (in theory).

In practice, the hedge is imperfect. The two assets may have different [beta](/beta/), sector exposure, or liquidity. A 100% hedge (long $1M, short $1M notional) may still leave residual risk.

Because the strategy is theoretically market-neutral, some traders lever it — using borrowed capital to amplify returns. This is risky: if the cointegration breaks and the spread widens further, leverage amplifies losses. The [Long-Term Capital Management](/long-term-capital-management-crisis/) collapse in 1998 was partially due to leveraged relative-value (quasi-cointegration) strategies that broke down during the crisis.

## Breaking cointegration: when the strategy fails

The biggest risk is that the cointegration relationship disappears. This can happen for several reasons:

- **Structural change:** A merger combines the two companies. A regulatory change alters the business model. The fundamental drivers of the relationship shift.

- **Market regime shift:** Two stocks cointegrate during normal conditions but diverge during financial stress. This is common during crises: correlations tend toward 1 (all assets fall together), breaking long/short pairs.

- **Liquidity dry-up:** The short position becomes illiquid, forcing a costly unwind. The short may become costly to borrow, creating drag on returns.

- **Fundamental shock:** New information breaks the relationship. An acquisition target (short) collapses on antitrust concerns while its acquirer (long) soars.

## Monitoring and dynamic adjustment

Successful cointegration traders constantly monitor the relationship. They use rolling regression to track whether the hedge ratio is stable. They monitor spread distribution: has mean or variance shifted? They set stop-losses and portfolio limits to cap losses if cointegration breaks.

Dynamic strategies adjust the hedge ratio as the relationship evolves. A 2-month rolling hedge ratio differs from a static one, allowing the strategy to adapt to changing market dynamics.

## Practical implementation in modern markets

Cointegration strategies are popular in [hedge funds](/hedge-fund/) and [quantitative trading](/quantitative-investing/) firms. Retail traders can implement them using pairs of liquid stocks or ETFs and backtesting software. The barrier to entry is statistical knowledge (understanding stationarity tests) and access to historical data.

One challenge is universe size. The more pairs tested, the higher the risk of finding spurious cointegration by chance. Out-of-sample testing and forward walk-forward validation help mitigate this.

<div class="wiki-seealso">

### Closely related

- [Statistical Arbitrage](/statistical-arbitrage/) — broader category of data-driven trading
- [Pairs Trading](/pairs-trading/) — similar strategy based on relative-value relationships
- [Mean Reversion Investing](/mean-reversion-investing/) — general principle that drives cointegration trades

### Wider context

- [Correlation Coefficient](/correlation-coefficient/) — raw relationship between assets
- [Quantitative Investing](/quantitative-investing/) — systematic, model-driven approach
- [Algorithmic Trading](/algorithmic-trading/) — automated execution of systematic strategies

</div>

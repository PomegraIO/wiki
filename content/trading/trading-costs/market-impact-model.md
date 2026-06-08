---
title: "Market Impact Model"
description: "Quantitative frameworks that estimate how a trade's own size moves the execution price against the trader."
keywords:
  - market impact
  - trade execution
  - price movement
  - liquidity cost
  - trading models
image: "/svg/trading.svg"
---

*A **market impact model** is a mathematical framework that estimates the temporary or permanent price movement caused by executing a trade of a given size. The model predicts how the market will absorb the order and at what cost—a critical input for [transaction-cost-analysis](/transaction-cost-analysis/) and pre-trade decision-making.*

## Why traders care about market impact

When a trader places a large order, the market does not execute it at a single price. Instead, the order consumes available liquidity across multiple price levels, pushing the execution price progressively worse. This self-inflicted cost—the drag caused by the order's own size—is **market impact**. 

For institutional traders managing millions or billions of dollars, market impact is often the largest component of total execution cost, dwarfing commissions and fees. A portfolio manager deciding whether to rebalance a $50 million position needs to know not just the nominal bid-ask spread, but the cumulative slippage that will occur as the order floods through the [order book](/stock-market/). That estimate comes from a market impact model.

Market impact is distinct from [timing-risk-cost](/timing-risk-cost/). Timing risk is the cost of price movement *between* the decision to trade and completion of the order. Market impact is the cost of the order's *own* presence and size. A trader might face both simultaneously: the market moves against them (timing risk), and they also move it further against themselves by trading (market impact).

## Temporary versus permanent impact

Market impact models typically distinguish two components.

**Temporary impact** is the immediate price concession needed to clear a given volume. If a stock's spread is 1 cent and the [market maker](/market-maker-trading/) has only 50,000 shares at the best ask, a buyer seeking 100,000 shares must step up to the next price level to fill the remainder. The price rise needed to consume deeper liquidity is temporary impact—it often reverses within hours or days as the market reprices back toward fair value.

**Permanent impact** reflects a genuine change in the market's assessment of value because of the trade. If a large seller offloads a block, sophisticated participants may infer negative information (insider knowledge, forced liquidation, or rebalancing) and revise their valuations downward. The new, lower price may stick. Permanent impact is often smaller than temporary impact for standard rebalancing trades but can be severe for block trades or in illiquid securities.

Most traders focus on temporary impact for daily execution decisions, while researchers and risk managers model permanent impact to understand longer-term portfolio costs.

## Common model forms

### Linear impact models

The simplest model assumes impact is proportional to order size. The execution price is:

**Price = Fair Value + Spread/2 + Impact Coefficient × (Order Size / Typical Daily Volume)**

The impact coefficient is estimated from historical data—how much market impact per unit of order size. This linearity works reasonably well for small-to-medium orders and liquid securities, but breaks down for very large orders, where impact may scale non-linearly.

### Square-root rule

Empirical research by [Almgren, Thorp, and others](https://example.com) found that market impact often scales with the *square root* of the order size ratio, not linearly. The intuition is that traders can break up large orders over time, so larger orders are not proportionally more damaging. The square-root model has become a market standard:

**Impact = α × √(Order Size / Daily Volume)**

The square-root form gives smaller impact for larger orders than a linear model would predict—a useful correction for realistic trading.

### Non-linear and regime-dependent models

Modern models incorporate regime shifts: impact during volatile periods differs from quiet periods; impact on high-volume days differs from low-volume days; and illiquid stocks have a different impact curve than liquid ones. Machine-learning approaches now fit impact surfaces that vary by time of day, market condition, and security characteristics, improving accuracy for large-scale execution.

## Estimating model parameters

Market impact models are only as good as their parameter estimates. Traders use several methods:

1. **Historical backtesting**: Measure actual execution prices on past orders and fit a regression to the relationship between order size and slippage.

2. **Microstructure theory**: Use order-book dynamics, bid-ask spreads, and intraday volume patterns to calibrate impact coefficients theoretically.

3. **Broker execution data**: Major brokers collect anonymised execution statistics across thousands of orders and offer impact benchmarks to clients.

4. **Market microstructure simulators**: Simulate order submission and matching under various market conditions to derive impact curves.

The best practice combines multiple sources and reestimates regularly, as [liquidity](/liquidity-risk/) and volatility regimes shift.

## Using impact models in practice

A portfolio manager uses an impact model when deciding:

- **Whether to trade at all**: If the [opportunity-cost-of-trading](/opportunity-cost-of-trading/) is lower than the estimated market impact, it may be better to hold the current position.

- **How to split the order**: Market impact usually increases less than proportionally with size (square-root rule), so breaking a $100 million order into ten $10 million pieces over multiple hours typically costs less than one $100 million block.

- **What time of day to execute**: Market impact is usually lower during high-volume hours (open and close) than during mid-day lulls.

- **Which broker to use**: Different brokers have different algorithms, access to dark pools, and [price-discovery](/price-discovery/) capabilities. Impact models help quantify who offers the best execution.

After execution, the actual slippage is compared to the pre-trade estimate to measure execution quality—a practice called [transaction-cost-analysis](/transaction-cost-analysis/).

## Limitations and caveats

Market impact models rest on several assumptions that don't always hold:

- **Stale parameters**: Impact coefficients drift as market structure evolves (new regulations, electronic venues, changes in participation).

- **Non-stationary volatility**: Impact is sensitive to volatility regime; a model fitted during calm periods will underestimate impact in a crisis.

- **Adverse selection**: Large orders often carry an information component (someone smart is moving big). The market may respond more severely if information asymmetry is suspected.

- **Feedback loops**: During stress, many traders execute simultaneously, and order flow itself becomes a signal. Impact can be far worse than historical models predict (flash crash risk).

For most day-to-day execution, linear and square-root models perform well enough. For large, urgent, or unusual orders, traders supplement models with judgment and expert execution venues.

## See also

<div class="wiki-seealso">

### Closely related

- [Transaction Cost Analysis](/transaction-cost-analysis/) — post-trade measurement of actual execution cost versus a reference price
- [Timing Risk Cost](/timing-risk-cost/) — price drift between the decision to trade and order completion
- [Opportunity Cost of Trading](/opportunity-cost-of-trading/) — performance forfeited when uninvested cash sits idle
- [Bid-Ask Spread](/bid-ask-spread/) — the round-trip cost of immediacy in a [market order](/market-order/)
- [Market Maker Trading](/market-maker-trading/) — the intermediaries who provide liquidity and suffer market impact
- [Over-the-Counter Market](/over-the-counter-market/) — less liquid markets where impact is typically larger
- [Liquidity Risk](/liquidity-risk/) — the risk that an order cannot be executed quickly without incurring large costs

### Wider context

- [Price Discovery](/price-discovery/) — how markets aggregate information into fair prices
- [Order Book](/stock-market/) — the electronic ledger of buy and sell orders
- [Algorithmic Trading](/algorithmic-trading/) — automated execution strategies designed to minimise impact
- [Volatility Smile](/volatility-smile/) — the non-uniform pricing of options across strikes, partly driven by execution costs

</div>

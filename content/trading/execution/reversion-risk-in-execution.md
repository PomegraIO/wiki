---
title: "Reversion Risk in Trade Execution"
description: "Reversion risk describes how temporary price impact from a large trade partially reverses after execution, affecting measured slippage and execution quality assessment."
keywords:
  - reversion risk trade execution
  - price impact reversion
  - temporary market impact
  - execution slippage measurement
  - post-trade reversion
  - permanent vs temporary impact
image: "/svg/trading.svg"
---

*In trade execution, **reversion risk** refers to the tendency for temporary price movement caused by a large order to partially reverse after the trade is complete. When you sell a large block, you depress the price; minutes later, buying pressure or short-covering can push it back up. This partial recovery affects how execution quality is measured, because slippage calculated immediately after a fill may not reflect the true permanent cost of your trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reversion Risk in Execution — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Temporary market impact often reverses; understanding and accounting for reversion is crucial to fair performance assessment.</div>

|   |   |
|---|---|
| **Definition** | The degree to which temporary price movement from an order bounces back after execution |
| **Typical reversion window** | Seconds to hours, depending on order size and market conditions |
| **Impact on benchmarks** | Makes immediate slippage higher than long-term realized cost |
| **Primary cause** | Order-induced pressure is temporary; fundamental demand remains |
| **Relevant to** | Large blocks, algorithmic strategies, [arrival price](/arrival-price-benchmark-trading/) benchmarking |
| **Measurement challenge** | Timing of the "post-trade" snapshot affects whether reversion is captured |

</aside>

## Why Price Impact Reverses

When you place a large sell order, you're temporarily flooding the market with supply. Buyers immediately available pull back their bids or disappear entirely, and the price falls to clear the excess supply. But that low price doesn't represent the new equilibrium; it's a temporary discount to incentivize buyers to step in.

Once your order is complete, the excess supply is gone. If the fundamental demand for the stock hasn't changed, buyers return at higher prices, and the stock bounces back. This reversion occurs because your trade was a temporary shock to supply, not a change in the underlying asset's value.

This is distinct from permanent impact. If you're selling because you've discovered damaging news about the company, the price won't revert—it will stay low because the market now believes the stock is worth less. But if you're selling simply because you have a large block to liquidate and no news has changed, the price recovers once the block is absorbed.

In [algorithmic trading](/algorithmic-trading/) and execution analysis, distinguishing permanent from temporary impact is central to understanding whether an execution was truly efficient or merely appeared efficient by bad luck of timing.

## How Reversion Affects Slippage Measurement

Consider a concrete example. You decide to buy 1 million shares of a stock at 2:00 p.m., when the price is $50.00 (the decision price). Your [broker](/broker/) takes 10 minutes to execute, and you finish at 2:10 p.m. at an average price of $50.15. The [arrival price](/arrival-price-benchmark-trading/) slippage is $0.15 per share—$150,000 in total cost.

But here's the complication: your large buy order pushed prices up. Once you stop buying at 2:10 p.m., the excess demand vanishes, and the stock drifts back to $50.08 by 2:20 p.m. If reversion is being measured, your "true" cost is only $0.08 per share, because the remaining $0.07 bounces back.

If you measure slippage immediately after your fill (at 2:10 p.m.), you see $0.15. If you measure it 10 minutes later (at 2:20 p.m.), you see only $0.08. The difference is reversion. The longer you wait to measure, the more reversion you capture—but you also risk the stock moving for other reasons (news, sector rotation, etc.).

## The Timing Problem: When to Measure Post-Trade?

Institutional execution quality reviews face a practical question: at what point do you measure the fill price to assess performance? Options include:

1. **Immediately after execution** (within seconds): Captures what the trader actually paid, but ignores reversion entirely.
2. **30 seconds to 1 minute later**: Captures micro-reversion but still sensitive to random walk noise.
3. **End of day**: Captures more reversion but confounds it with other market movements and overnight risk.
4. **Specific window (e.g., 15 or 30 minutes):** A compromise chosen by some brokers and buy-side execution teams.

There's no universal standard. The choice depends on your investment horizon and the nature of the trading. A high-frequency trader cares about reversion within microseconds. A portfolio manager executing a 2-day program cares about multi-hour reversion. Regulators and compliance teams sometimes use different windows depending on the order type and venue.

## Permanent vs. Temporary Impact

The theoretical distinction is clear: **permanent impact** is the shift in the equilibrium price that persists, while **temporary impact** is the short-lived deviation that reverts. In practice, teasing them apart is hard because you can't know the "true" equilibrium—you only see market prices.

One approach: model the price path after your order ends. If the price quickly returns to (or past) the pre-order level, most of your slippage was temporary. If it stays moved, your slippage was more permanent—perhaps because your trade itself conveyed information (you're a sophisticated trader, so maybe you know something) or because it was large enough to permanently shift liquidity.

For very large institutional orders, some of the impact does stick. Your sale of 10 million shares permanently reduced supply; future buyers have fewer shares available at the old prices, so future prices are slightly higher. But even in that case, a meaningful portion often reverts within hours because dealers and [market makers](/market-maker-trading/) replenish inventory, or short-sellers step in to meet demand.

## How Algorithms Account for Reversion

Modern execution algorithms try to forecast reversion and price it into their decisions. An algo that expects significant reversion might execute more aggressively early on (pushing prices harder now, knowing the reversion will partially soften the total cost). An algo that expects little reversion (illiquid stocks, or trades conveying information) might execute more patiently to spread [market impact](/market-risk/) over time.

Some algorithms use statistical models trained on historical data to estimate, for a given order size and security, what fraction of impact reverts and over what time window. Armed with that forecast, the algo can compute the expected permanent cost and optimize execution accordingly.

Brokers also use reversion estimates when setting execution guarantees. If you ask a broker for a guaranteed price on a large order, the broker factors in their expected permanent impact cost plus some profit margin. Temporary reversion that the broker expects to capture post-execution can be pocketed as profit.

## Measurement in Execution Quality Reviews

When a [broker](/broker/) or trading venue reports execution quality metrics to regulators or clients, the treatment of reversion varies. SEC guidance on best execution doesn't mandate a specific reversion window, so firms choose their own—typically 30 seconds, 1 minute, or end-of-day. This creates a challenge for comparison: one firm's "excellent execution" measured at 30 seconds might look mediocre if measured at 5 minutes.

Some best-practice firms are explicit: they report multiple measurements (immediate, 1-min, 30-min, end-of-day) so clients can see how much reversion occurred and judge for themselves whether the execution quality was strong. This transparency is increasingly expected in competitive execution markets.

## See also

<div class="wiki-seealso">

### Closely related

- [Arrival Price Benchmark in Trading](/arrival-price-benchmark-trading/) — the metric most affected by reversion timing
- [Market Impact](/market-risk/) — how orders move prices; reversion is the unwinding of temporary impact
- [Algorithmic Trading](/algorithmic-trading/) — execution strategies designed to minimize permanent impact
- [Implementation Shortfall](/fair-value/) — total execution cost, which includes both temporary and permanent impact
- [Bid-Ask Spread](/bid-ask-spread/) — the baseline cost before any impact-driven movement

### Wider context

- [Liquidity Risk](/liquidity-risk/) — why large orders cannot be executed without moving prices
- [Price Discovery](/price-discovery/) — the market mechanism that determines equilibrium prices
- [Broker](/broker/) — the intermediary responsible for execution and impact management

</div>

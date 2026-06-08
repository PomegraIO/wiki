---
title: "Post-Trade Transaction Cost Analysis"
description: "Systematic measurement of realised execution costs against a benchmark after orders are filled."
keywords:
  - post-trade analysis
  - transaction cost analysis
  - execution cost measurement
  - VWAP
  - broker evaluation
image: "/svg/trading.svg"
---

*A **post-trade transaction cost analysis** is a systematic measurement of the actual execution cost incurred on a completed order, typically calculated by comparing the realised average fill price to a pre-set benchmark price. Used after fills are complete, the analysis reveals how much slippage occurred, whether costs matched expectations, and whether the [broker](/broker/) or [algorithm](/algorithmic-trading/) performed well.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Post-Trade Transaction Cost Analysis — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading execution." />

<div class="wiki-infobox-caption">Auditing actual execution costs against benchmarks to improve future trades.</div>

|   |   |
|---|---|
| **What it is** | Measurement of realised slippage: actual fill price versus benchmark |
| **Also called** | Execution cost analysis; transaction cost review; post-trade audit |
| **Calculated as** | (Actual average fill price − Benchmark price) × Shares traded |
| **Common benchmarks** | VWAP, TWAP, arrival price, mid-quote at order time |
| **Frequency** | Calculated daily, weekly, or per-trade depending on usage |
| **Purpose** | Broker/algorithm evaluation, cost attribution, trend analysis |

</aside>

## The basic calculation

Post-trade analysis begins with choosing a benchmark price—the "fair" or expected price against which to measure slippage. The most common benchmarks are:

**VWAP (volume-weighted average price)** is the average price of all transactions in a security during a specified period, weighted by the volume of each transaction. If 50,000 shares trade between 10:00 and 10:30 a.m. at varying prices, the VWAP is the weighted average price of that entire period. For many intraday trades, VWAP of the execution window is the benchmark.

**TWAP (time-weighted average price)** divides the execution window into equal time intervals, samples the price at each interval, and averages them arithmetically. It is simpler to calculate than VWAP but less precise—it does not weight by actual trading volume.

**Arrival price** (also called decision price) is the [bid-ask midpoint](/bid-ask-spread/) at the moment the order was submitted. This benchmark is useful for evaluating algorithm performance independent of market movement. If the arrival price is $50.00 and the realised average fill is $50.12, the slippage is $0.12.

**Open price** or **close price** is the official opening or closing price of the trading day. Used mainly for end-of-day block evaluations.

Once a benchmark is chosen, the realised cost is simply:

```
Execution Cost = (Actual Average Fill Price − Benchmark Price) × Shares
```

For a buy order, a higher fill price is a cost (negative slippage). For a sell order, a lower fill price is a cost. The cost can be expressed in dollars, per-share basis points, or as a percentage of the trade notional.

## Why it matters

For fund managers and traders, post-trade analysis is the primary tool for measuring whether execution was efficient. It answers critical questions: Did the broker execute well? Did the algorithm I chose minimise costs? Has execution quality deteriorated over time? Are certain stocks more expensive to execute than others?

For compliance and governance, post-trade analysis provides evidence that execution decisions were reasonable and cost-effective. Regulators and audit teams often require documentation of execution costs and how they compare to market conditions at the time.

For continuous improvement, aggregate post-trade data over weeks or months reveals trends. If a trader notices that Thursday executions average 0.15% cost while Monday executions average 0.05%, the pattern might suggest that liquidity is worse midweek, or that the trader's algorithm is poorly tuned for that day-of-week cycle. The trader can then adjust.

## Broker and algorithm evaluation

Post-trade analysis is the primary benchmark for assessing [broker](/broker/) performance. A trader using multiple brokers can measure each one's realised costs on comparable orders and decide which brokers deliver better execution.

Example: A portfolio manager executes 10 large orders per week with Broker A and 10 with Broker B. Post-trade analysis shows that Broker A's average realised cost is 0.12% of notional, while Broker B's is 0.09%. Over a year, this difference translates to tens of thousands of dollars. The manager may shift more volume to Broker B or renegotiate fees with Broker A.

Similarly, traders who build or test in-house [algorithmic execution](/algorithmic-trading/) systems use post-trade analysis to evaluate algorithm performance. If a new VWAP algorithm produces realised costs 10 basis points lower than the previous TWAP algorithm, that is meaningful evidence of improvement.

Performance benchmarking across algorithms is important because different algorithms are designed for different objectives. An "arrival price" algorithm aims to minimise slippage relative to the decision price and is best evaluated on that metric. A "VWAP algorithm" targets the full-day volume-weighted price and should be judged on VWAP slippage.

## Aggregation and trending

Individual trades are analysed, but institutional traders and asset managers also aggregate post-trade results across many trades to measure execution quality trends. Typical aggregations include:

- **By day of week**: Does Tuesday execution cost differ from Friday?
- **By market condition**: Are costs higher on high-volatility days?
- **By stock liquidity**: Are large-cap stocks cheaper to execute than small-cap?
- **By time of day**: Is early-morning execution cheaper than late-afternoon?
- **By order size**: Does slippage scale linearly or nonlinearly with order size?

These trends inform strategy. A trader who discovers that high-volatility days cost 50% more might prefer to delay discretionary orders on those days. A manager who finds that large-cap execution costs 40% less might tilt order flow accordingly.

## Decomposing shortfall

Simple post-trade analysis compares one price to another. More sophisticated analysis decomposes the shortfall using the [execution shortfall decomposition](/execution-shortfall-decomposition/) framework, separating total cost into delay cost, [market impact](/market-risk/), and timing risk. This reveals the root causes of slippage and guides improvement efforts.

Example: A trader's realised cost is 0.20% of notional. Decomposition shows:
- Delay cost: 0.08% (the algorithm executed too slowly and missed early-window liquidity)
- Market impact cost: 0.10% (the order itself moved prices; unavoidable given size)
- Timing risk cost: 0.02% (the market drifted slightly; good timing relative to volatility)

This breakdown tells the trader where to focus: either reduce order size (to lower impact), execute faster (to reduce delay), or accept market impact as the cost of the trade.

## Technology and automation

Most institutional traders and asset managers use automated post-trade analytics platforms that:

1. **Ingest trade data** from brokers, exchanges, and internal order management systems
2. **Calculate benchmarks** (VWAP, TWAP, etc.) from market data feeds
3. **Compute slippage** for each trade
4. **Aggregate results** by broker, algorithm, stock, market condition, and other dimensions
5. **Visualise trends** in dashboards and reports
6. **Flag outliers** for manual review (unusually high-cost executions)

Many of these platforms integrate with execution cost attribution models that decompose shortfall and provide deeper insight into root causes.

## Limitations

Post-trade analysis measures what happened but cannot always explain why. It captures realised cost, which includes the effect of luck (market movement during execution) alongside skill (algorithm quality). Comparing two orders with different realised costs does not necessarily mean one algorithm is better; one order might have faced worse luck.

To isolate skill from luck, managers use [execution shortfall decomposition](/execution-shortfall-decomposition/), but even that technique makes strong assumptions and may not fully separate controllable from uncontrollable costs.

Additionally, post-trade analysis depends on the choice of benchmark. Using VWAP versus arrival price as the benchmark can yield different conclusions about broker quality. Industry practice has converged on VWAP for most equity trades, but disagreement on the right benchmark persists in some markets.

Finally, post-trade analysis is reactive. It tells the trader what already happened, not what will happen on the next trade. That is the role of [pre-trade analytics](/pre-trade-analytics/).

## See also

<div class="wiki-seealso">

### Closely related

- [Pre-trade analytics](/pre-trade-analytics/) — forecasting execution cost before order submission
- [Execution shortfall decomposition](/execution-shortfall-decomposition/) — separating realised cost into delay, impact, and timing components
- [Algorithmic trading](/algorithmic-trading/) — automated systems designed to minimise execution cost
- [Minimum quantity order](/minimum-quantity-order/) — an order instruction ensuring minimum fill size or cancellation
- [Market impact](/market-risk/) — the price movement caused by the order itself

### Wider context

- [Broker](/broker/) — intermediary executing orders on behalf of clients
- [Bid-ask spread](/bid-ask-spread/) — the cost of immediate execution at market prices
- Order routing — directing orders to trading venues
- [Limit order](/limit-order/) — an order filled only at a specified price or better
- [Market order](/market-order/) — an order executed immediately at the best available price
- [Liquidity risk](/liquidity-risk/) — difficulty executing large orders without significant price movement

</div>

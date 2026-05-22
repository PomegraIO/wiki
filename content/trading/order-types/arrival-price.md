---
title: "Arrival Price"
description: "The market price at the moment an order is submitted, used as a benchmark to measure execution quality."
keywords:
  - execution benchmark
  - order quality measurement
  - implementation shortfall
  - trading performance
---

*The **arrival price** is the stock's market price at the exact moment a [market order](/wiki/market-order/) or [limit order](/wiki/limit-order/) is sent to the exchange or broker. It serves as the starting point for measuring whether a trader achieved good [execution](/wiki/order-execution-speed/) relative to what was available at the time the decision to trade was made.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Measurement** | Price at order submission time |
| **Purpose** | Baseline for execution performance |
| **Compare to** | Final fill price, implementation shortfall |
| **Key metric** | Aids assessment of slippage |
| **Relevant to** | Institutional traders, fund managers |
| **Time window** | Microseconds matter in high-frequency markets |

</aside>

## Why arrival price matters

When a portfolio manager decides to buy 100,000 shares of a stock, that decision is made at a specific moment—when the stock is trading at, say, $50.23. That price is the arrival price. The manager then routes the order to a broker or directly to the market. By the time the broker receives it, routes it, and executes it, the stock price may have moved. The manager's arrival price is the reference point for asking: did I get a good execution, or was I hurt by slippage?

If the stock trades up to $50.28 by the time the order fills, the trader paid 5 cents per share more than the arrival price—$50,000 more in total cost on the 100,000-share position. That difference is part of the [implementation shortfall](/wiki/implementation-shortfall/), the cost of executing a large order over time rather than instantly.

## Arrival price and implementation shortfall

[Implementation shortfall](/wiki/implementation-shortfall/) is the gap between the decision price and the actual execution price, including all costs (commissions, [bid-ask spread](/wiki/bid-ask-spread/), and [market impact](/wiki/market-impact-cost/)). Arrival price is the first component: the benchmark. The trader's goal is to execute as close to arrival price as possible.

Execution algorithms are judged by how much slippage they incur versus arrival price. A [TWAP algorithm](/wiki/twap-order/) (trade-weighted average price) aims to execute at the volume-weighted average price over the execution window. A [VWAP algorithm](/wiki/vwap-order/) trades at the volume-weighted average price, also using arrival price as the starting reference. If arrival price is $50.23 and the algorithm achieves $50.25, the trader paid 2 cents more—an underperformance of 2 cents, or about 0.04% on a $50 stock.

## How arrival price is calculated

Arrival price is typically the **last published price** before the order reaches the broker or exchange—what a trader sees on their screen in real time. For exchange-listed equities, this is the consolidated last-sale price from the [tape](/wiki/consolidated-tape/). For OTC securities or less liquid assets, it may be the mid-point of the [bid-ask spread](/wiki/bid-ask-spread/) or the best available bid or ask.

In high-frequency markets, the exact definition matters. If a trader submits an order at 14:32:45.123456, the arrival price is the price at that nanosecond. A millisecond delay in transmission can mean a different reference point. Broker and exchange systems timestamp orders to capture this.

## Measurement and reporting

Major brokers and [execution algorithms](/wiki/algorithmic-execution-benchmark/) report execution quality to clients by comparing:

1. **Arrival price** — what the market was at order submission
2. **Participation rate** — what volume of the stock was trading during the execution window
3. **Final execution price** — where all fills were completed
4. **Benchmark price** — often VWAP or TWAP, depending on strategy

If a trader's VWAP algorithm underperforms the actual VWAP by 1 cent, that's slippage. If VWAP itself is 5 cents worse than arrival price, that's market impact—the order itself moved the price. Separating these two is valuable for the trader's risk management.

## The role of broker selection

Choosing a broker or [execution services provider](/wiki/best-execution/) is partly about getting closest to arrival price. Brokers with direct market access ([DMA](/wiki/alternative-settlement-system/)), proprietary algorithms, and relationships with [market makers](/wiki/market-maker-obligations/) may execute tighter to arrival price than brokers without them. A high-frequency trader may see arrival prices in microseconds and need a broker that can match that latency; a retail investor with a daily order might not care about arrival price to the cent.

## Practical limitations

Arrival price assumes the trader's decision is made at a single instant. In reality, large institutional traders often decide to buy over minutes or hours, then execute gradually. The "arrival" of a sliced order (e.g., 10 tranches of 10,000 shares each) happens in steps. In these cases, some practitioners use the *first execution price* as the arrival reference, and measure the *entire execution program* against it.

Additionally, if the trader is executing a complex strategy (e.g., simultaneously buying stock and selling options, or hedging with futures), arrival prices may differ across instruments, making a single reference point less meaningful.

## Cross-market considerations

In markets with multiple venues ([lit pools](/wiki/lit-venue/), [dark pools](/wiki/dark-pool/), [crossing networks](/wiki/crossing-network/)), a trader may see different prices on different venues. The "official" arrival price is typically the last consolidated print, but a sophisticated trader might reference the best available bid and offer across all accessible venues.

<div class="wiki-seealso">

### Closely related
- [Implementation Shortfall](/wiki/implementation-shortfall/) — total cost of executing an order over time versus instant execution
- [Execution Quality Analysis](/wiki/execution-quality-analysis/) — assessing whether a broker delivered fair execution
- [Market Impact Cost](/wiki/market-impact-cost/) — the price movement caused by the order itself
- [Order Execution Speed](/wiki/order-execution-speed/) — latency between order submission and fill
- [VWAP Order](/wiki/vwap-order/) — algorithm aiming to trade at volume-weighted average price

### Wider context
- [Best Execution](/wiki/best-execution/) — regulatory requirement for brokers to achieve best possible terms
- [Slippage](/wiki/slippage/) — gap between expected and actual execution prices
- [Algorithmic Trading](/wiki/algorithmic-trading/) — automated execution strategies that optimize against arrival price
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — the cost of immediate execution relative to mid-price
- [Market Maker Obligations](/wiki/market-maker-obligations/) — requirements to maintain tight spreads

</div>

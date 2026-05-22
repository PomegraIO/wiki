---
title: "Order Execution Speed"
description: "The latency from order submission to market fill, measured in milliseconds and critical to high-frequency trading."
keywords:
  - order execution speed
  - latency
  - high frequency trading
  - market microstructure
---

*Order Execution Speed is the time elapsed between when a trader submits an order and when the exchange acknowledges a fill.* Measured in milliseconds, it is the difference between intention and action. In [high-frequency trading](/wiki/high-frequency-trading/), where firms profit from microsecond arbitrage opportunities, execution speed is paramount. A 10-millisecond delay can mean the difference between capturing a profitable trade and watching the [bid-ask spread](/wiki/bid-ask-spread/) snap shut. For most retail traders, execution speed is less critical, but it still affects slippage—the difference between the quoted price and the actual fill price.

<aside class="wiki-infobox">

| Key fact | Detail |
|----------|--------|
| **Unit** | Milliseconds (ms); HFT firms measure in microseconds |
| **Components** | Network latency + broker infrastructure + exchange matching |
| **Typical retail speed** | 100–500 ms |
| **HFT target** | 1–10 ms or sub-millisecond |
| **Colocation** | Placing servers at exchange facilities to reduce latency |
| **Impact** | Faster execution reduces [slippage](/wiki/slippage/) and improves [fill](/wiki/arrival-price/) quality |
| **Trade-off** | Speed vs. cost (colocation and infrastructure are expensive) |

</aside>

## Components of latency

Order execution speed is composed of several layers of delay:

1. **Network latency**: Time for the order to travel from the trader's device to the broker's system to the exchange. Fiber-optic cables travel at ~2/3 the speed of light, so even a 100-mile route takes ~1 ms.

2. **Broker infrastructure**: The broker's order routing engine must receive the order, validate it, and forward it to the exchange. This adds 5–50 ms depending on the broker's technology.

3. **Exchange matching**: The exchange's matching engine must receive the order, match it against the [order book](/wiki/order-book-depth/), and send back a confirmation. This takes 1–20 ms.

4. **Return network latency**: The confirmation travels back to the trader's device.

For a retail trader using a typical online broker, total latency is typically 100–500 ms. For a [high-frequency trading](/wiki/high-frequency-trading/) firm with optimized infrastructure, it can be 1–10 ms.

## Slippage and arrival price

Execution speed directly affects [slippage](/wiki/slippage/)—the difference between the expected price (when the trader decides to trade) and the actual fill price (when the order executes).

Imagine a stock with a [bid-ask spread](/wiki/bid-ask-spread/) of 1 cent. The trader places a limit buy order at $100.00. Due to 200 ms of latency, by the time the order reaches the exchange, the market has moved: the best ask is now $100.02. The trader either pays $100.02 or waits for a better price and risks no fill.

[High-frequency trading](/wiki/high-frequency-trading/) firms minimize slippage by eliminating latency. They can execute hundreds of trades per second, capturing tiny [bid-ask spread](/wiki/bid-ask-spread/) opportunities that retail traders miss.

## Colocation and latency arbitrage

To minimize network latency, [high-frequency trading](/wiki/high-frequency-trading/) firms place their servers in the same physical location (colocation) as the exchange's matching engines. The New York Stock Exchange, NASDAQ, and CME all offer colocation services where traders can rent rack space.

Colocation reduces round-trip latency from 100+ ms to 1–5 ms. A firm paying $10,000 per month for colocation can recoup that investment if they execute thousands of trades per day, capturing fractions of a cent per trade.

Latency arbitrage—exploiting the speed advantage to capture price discrepancies before slower traders can react—is controversial. Regulators worry it amounts to "front-running," and some have proposed latency floors to "level the playing field." However, latency reduction also improves market efficiency by allowing faster discovery of price.

## Order types and speed

Certain [order types](/wiki/order-types/) are designed to execute faster:

- **Market orders**: Execute immediately at the best available price, minimal latency penalty.
- **Limit orders**: Only execute at a specified price, may wait indefinitely if the price is not reached.
- **Iceberg orders**: Hidden large orders revealed in small increments to minimize market impact; they execute in stages.
- **TWAP/VWAP orders**: Execute over time at time-weighted or volume-weighted average prices, sacrificing speed for minimal [market impact](/wiki/market-impact-cost/).

[High-frequency trading](/wiki/high-frequency-trading/) firms favor market and limit orders because they execute on known schedules and trigger minimal exchange latency.

## Execution quality metrics

[Execution quality](/wiki/execution-quality-analysis/) measures more than just latency. Brokers and exchanges are assessed on:

- **Effective spread**: The cost of execution relative to the [midpoint](/wiki/midpoint-peg/) price at order submission.
- **Price improvement**: How often the trader's actual fill price is better than the quoted [bid-ask spread](/wiki/bid-ask-spread/).
- **Fill rate**: Percentage of the order actually filled (vs. partially filled or not filled).
- **Latency**: Round-trip time from submission to fill.

SEC Rule 10b-5 requires brokers to provide "best execution"—reasonably designed to obtain the best terms under prevailing market conditions. Brokers that route orders to the venue with the fastest [execution](/wiki/execution-quality-analysis/), tightest [spreads](/wiki/bid-ask-spread/), and best price improvement are considered to be meeting this standard.

## Market impact and the latency-impact trade-off

Executing slowly can incur market impact: a large order may move the market against the trader. Executing quickly minimizes market impact but incurs latency costs and may require tighter [bid-ask spreads](/wiki/bid-ask-spread/).

The optimal execution strategy balances these forces. A $100 million equity order cannot be executed in one transaction on most stocks; the price impact would be massive. Instead, [algorithm](/wiki/algorithmic-trading/)ic execution breaks the order into smaller parcels executed over time (a VWAP order), minimizing price moves but accepting longer latency and more execution risk.

## Regulatory oversight of execution speed

Regulators recognize that extreme latency inequality is problematic. The SEC proposed a "latency floor" rule to prevent firms from gaining unfair advantages through colocation, but this remains controversial and unimplemented.

The EU's MiFID II rule requires brokers to clearly disclose execution speeds and quality metrics, allowing retail investors to compare brokers. Increased transparency has motivated brokers to invest in faster infrastructure to compete on speed as a feature.

---

<div class="wiki-seealso">

### Closely related
- [High-Frequency Trading](/wiki/high-frequency-trading/) — Trading strategy relying on extreme speed
- [Slippage](/wiki/slippage/) — Cost from execution delay
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — The price difference that latency may worsen
- [Order Types](/wiki/order-types/) — Different ways to submit orders with different speeds

### Wider context
- [Market Impact](/wiki/market-impact-cost/) — Price movement from executing a large order
- [Execution Quality Analysis](/wiki/execution-quality-analysis/) — Measuring broker execution quality
- [Algorithmic Trading](/wiki/algorithmic-trading/) — Using algorithms to optimize execution
- [Arrival Price](/wiki/arrival-price/) — Expected price vs. actual fill price
- [Market Microstructure](/wiki/order-book-depth/) — How exchanges match orders and set prices

</div>

---
title: "Algorithmic trading"
description: "Algorithmic trading uses computer programs to automatically execute trading instructions based on predetermined rules. Algorithms break large orders into smaller pieces, optimize execution timing, and exploit price patterns."
keywords:
  - algorithmic trading
  - algo trading
  - automated trading
  - execution algorithm
image: "/svg/trading.svg"
---

*Algorithmic trading (or "algo trading") is the use of computer programs to automatically execute trades based on pre-set rules. An algorithm might slice a large order into small pieces and execute them throughout the day, or search for price patterns and execute when conditions are met. Algorithms range from simple (execute 10,000 shares evenly over the next hour) to complex (adapt to real-time volume, market microstructure, and estimated price impact). The vast majority of institutional trading is algorithmic.*

<div class="wiki-hatnote">

For extremely fast algorithmic trading, see [high-frequency trading](/high-frequency-trading/). For manual order placement, see [limit order](/limit-order/) and [market order](/market-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Algorithmic trading — key facts</div>

<img src="/svg/trading.svg" alt="A computer screen showing algorithmic trading logic and execution" />

<div class="wiki-infobox-caption">Algorithms automate trading decisions, breaking large orders into optimal execution pieces.</div>

|   |   |
|---|---|
| **What it is** | Computer program executing trades automatically based on rules |
| **Typical use** | Breaking large orders, optimizing execution, pattern matching |
| **Speed** | Seconds to milliseconds (slower than HFT, faster than manual) |
| **Advantage** | Minimizes market impact, improves average price, removes emotion |
| **Complexity** | Ranges from simple (split evenly over time) to very complex (adaptive) |

</aside>

## Why algorithmic trading?

**Market impact reduction:** A 100,000-share order placed at once would move the price sharply against you. An algorithm breaks it into 20 pieces of 5,000 shares each, spread throughout the day. The market does not see a huge buyer; prices move less.

**Average price improvement:** By spreading execution across the day or week, you often achieve better average prices than a single large trade.

**Emotion removal:** A human trader might panic and sell everything if the price dips slightly. An algorithm sticks to the plan, executing methodically.

**Scale:** A single algorithm can manage dozens of simultaneous orders across multiple securities and venues.

## Common algorithmic strategies

**VWAP (volume-weighted average price):** Slices the order to target executing at the day's [VWAP](/vwap-order/). See [VWAP order](/vwap-order/).

**TWAP (time-weighted average price):** Slices evenly over time. See [TWAP order](/twap-order/).

**POV (participation of volume):** Execute at a percentage of the observed volume. If 1 million shares trade throughout the day, and you set POV to 10%, the algorithm buys or sells roughly 100,000 shares as the 1 million move through.

**IS (Implementation shortfall):** Execute to minimize the "shortfall" between your target price and the actual execution price, balancing speed and market impact.

**Execution inline with volume:** Detect where large volumes are trading and execute near those prices and times.

## Algorithmic trading at different scales

**Institutional (typical):**
- Large fund wants to buy 1 million shares over one week.
- Submits an algorithm (e.g., VWAP) to their broker or a vendor.
- The algorithm automatically breaks it into pieces, executes across venues, adapts to volume, and achieves average execution near VWAP.
- Result: better average price with minimal market impact.

**Retail (limited):**
- Most retail brokers offer limited algorithmic options (usually just time-based slicing).
- Interactive Brokers and some others offer more sophisticated algorithms.

**Proprietary (HFT):**
- HFT firms use extremely sophisticated proprietary algorithms that detect patterns, exploit arbitrage, and execute in microseconds.

## Smart order routing and algorithms

A [smart order router](/smart-order-router/) is a type of algorithm that:
- Receives your order.
- Checks prices on all available venues (lit exchanges, dark pools, etc.).
- Routes your order to the venue(s) offering the best price.
- Adapts as prices change.

Smart order routing is a form of algorithmic trading that optimizes for best execution.

## Risks and challenges of algorithmic trading

**Overfitting:** An algorithm optimized for historical data might fail on new data. For example, an algorithm tuned to execute in quiet markets might fail badly during volatile periods.

**Flash crashes:** If many algorithms unwind simultaneously (all trying to sell at once), it can cause rapid price declines and market instability. The 2010 Flash Crash involved algorithmic feedback loops.

**Latency sensitivity:** If a market moves faster than the algorithm can react, results can be poor.

**Slippage during stress:** In volatile markets (earnings, crises), even sophisticated algorithms can underperform.

## Regulation of algorithmic trading

U.S. and international regulators require:

- **Disclosure:** Brokers must disclose that orders are routed algorithmically.
- **Kill switches:** Algorithms must have automated safeguards to stop trading if something goes wrong.
- **Backtesting:** Brokers and algo vendors must test their algorithms on historical data.
- **Monitoring:** Regulators monitor for suspicious patterns (e.g., too many small orders that seem designed to mislead).
- **Best execution:** Algorithms must be designed to achieve best execution, not to benefit the broker.

## Algorithmic trading fees

Algo services are typically priced:
- **Flat fee:** e.g., $50–$500 per algorithm execution.
- **Basis point fee:** e.g., 0.1–1 basis point (0.001–0.01%) of the order value.
- **Included with brokerage:** Many brokers include basic algorithms for free; advanced algorithms charge extra.

## The future of algorithmic trading

**Machine learning:** Newer algorithms use AI and machine learning to adapt to changing market conditions.

**Multi-asset:** Algorithms increasingly span stocks, options, futures, and other instruments simultaneously.

**Reinforcement learning:** Some firms experiment with algorithms that learn and improve over time.

**Regulation:** Expect tighter rules on algorithm transparency, testing, and safeguards.

## See also

<div class="wiki-seealso">

### Algorithmic orders and strategies

- [VWAP order](/vwap-order/) — volume-weighted execution
- [TWAP order](/twap-order/) — time-weighted execution
- [Smart order router](/smart-order-router/) — route to best venues
- [Iceberg order](/iceberg-order/) — simple algorithm

### Trading execution and impact

- Market impact — what algorithms reduce
- Slippage — gap between intended and actual price
- Liquidity — where algorithms find execution
- Block trading — large orders often use algos

### Market structure

- [High-frequency trading](/high-frequency-trading/) — extreme form of algo trading
- Order book — where algos find prices
- [Best execution](/best-execution/) — regulatory obligation for algos

### Risk and regulation

- Flash crash — algo-driven market event
- [Systemic risk](/systemic-risk/) — algos can amplify volatility
- Backtesting — testing algos on historical data

</div>

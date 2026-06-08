---
title: "Time-Weighted Average Price (TWAP) in Crypto Trading"
description: "How TWAP execution algorithms spread large orders over time to minimize market impact and slippage in cryptocurrency trading."
keywords:
  - twap order crypto
  - time-weighted average price cryptocurrency
  - order execution algorithms
  - crypto market impact
  - slippage reduction
  - algorithmic trading crypto
image: /svg/crypto.svg
---

*A **TWAP order** breaks a large cryptocurrency purchase or sale into smaller pieces and executes them at regular intervals across a specified time period, aiming to fill at the average price over that window rather than moving the market with a single, giant order.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TWAP in Crypto — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency trading." />

<div class="wiki-infobox-caption">A mechanical, rule-based execution strategy that trades off immediacy for price stability.</div>

|   |   |
|---|---|
| **Core goal** | Execute a large order without shocking the market or incurring massive [slippage](/slippage/) |
| **Method** | Divide order into N equal pieces; execute one every T minutes |
| **Pricing** | Final fill price gravitates toward the time-weighted average of prices during the execution window |
| **Time window** | Can range from minutes (aggressive) to hours or days (passive) |
| **Market impact** | Smaller, each slice typically has minimal impact; total impact far less than one lump order |
| **Crypto-specific risk** | 24/7 trading can extend execution; volatility may force wider slices or early termination |

</aside>

## Why TWAP Matters in Crypto

Cryptocurrency markets operate around the clock and can be volatile. When a trader or institution needs to buy or sell a large position—say, 10,000 Bitcoin or 1 million Ethereum tokens—dumping the entire order on the market in a single transaction would move prices sharply against them. The immediate market impact and [slippage](/slippage/) could cost millions of dollars.

TWAP solves this by spreading the order mechanically across time. Instead of one massive market order, the algorithm executes dozens or hundreds of smaller orders at predetermined intervals. Each small order has minimal impact; the cumulative fill price converges to a time-weighted average, which is much more favorable than the market price at the moment the large order arrived.

TWAP is especially valuable in illiquid altcoins or during periods of thin market depth, where large orders can move prices 5%, 10%, or more in seconds.

## How TWAP Execution Works

The basic algorithm is straightforward:

1. **Define a time window**: "I want to buy 100,000 coins over the next 2 hours."
2. **Calculate slice size**: 100,000 ÷ 120 minutes = ~833 coins per minute.
3. **Execute in sequence**: Every minute, buy ~833 coins at the market [bid price](/bid-ask-spread/).
4. **Track progress**: If the order is trailing the average price, accelerate; if ahead, decelerate.
5. **Complete execution**: At the end of 2 hours, the trader has filled 100,000 coins at an effective price close to the time-weighted average.

The execution algorithm often includes adaptive logic:

- **Pace adjustment**: If the price spikes upward, the algorithm may wait longer before the next slice to capture a dip.
- **Early termination**: If the remaining order becomes very small or the market becomes extremely thin, the algorithm may execute the rest in one go.
- **Volume participation**: Some TWAP algos scale slice size based on market volume; high-volume periods get larger slices.

## TWAP vs. Other Execution Strategies

### TWAP vs. VWAP

**VWAP** (volume-weighted average price) adjusts slice size based on expected trading volume; it executes larger orders when volume is heavy and smaller orders when volume is light. This theoretically achieves better execution by "hiding" in the order flow.

TWAP is purely mechanical: the same order size every period, regardless of volume. TWAP is simpler but can underperform VWAP in volatile or trending markets.

### TWAP vs. Immediate Execution

An [algorithmic trader](/algorithmic-trading/) executing a large order has three broad choices:

- **Immediate (market order)**: Execute now, accept whatever slippage occurs.
- **TWAP**: Execute over a fixed time, accepting whatever price prevails.
- **Smart order routing**: Use a routing engine to find the best available [counter-party](/counterparty-risk/) or [exchange](/stock-exchange/) for each slice.

TWAP sits in the middle: it is more predictable than smart routing but more costly than a single market order in calm markets.

## Crypto-Specific Considerations

### 24/7 Markets and Time Windows

Traditional equity markets close at 4 PM ET, so a TWAP window from 10 AM to 4 PM is natural. Crypto markets never close. A trader executing a TWAP window over 8 hours on Sunday morning may encounter radically different liquidity and volatility than planned, especially if a major news event breaks.

### Slippage Volatility

Crypto is far more volatile than equities. A TWAP window set for 2 hours might be ideal in calm conditions but catastrophic during a flash crash or volatility spike. Traders often pair TWAP with stop-loss or abort thresholds: "If the price moves more than 2% away from the 1-hour average, cancel the remaining slices."

### Custody and Exchange Integration

Many crypto exchanges offer in-house TWAP algorithms, but quality varies. Larger traders sometimes execute TWAP across multiple exchanges simultaneously—buying 1,000 coins on Coinbase, 1,000 on Kraken, 1,000 on Binance each minute—to further reduce price impact and exploit arbitrage across venues.

## Worked Example

Suppose a trader wants to buy 10,000 Ethereum tokens over 1 hour, in 10-minute intervals.

| Interval | Slice Size | ETH Price | Fill | Cost |
|----------|----|----|----|----|
| 0–10 min | 1,000 | $2,500 | 1,000 | $2,500,000 |
| 10–20 min | 1,000 | $2,510 | 1,000 | $2,510,000 |
| 20–30 min | 1,000 | $2,495 | 1,000 | $2,495,000 |
| 30–40 min | 1,000 | $2,520 | 1,000 | $2,520,000 |
| 40–50 min | 1,000 | $2,505 | 1,000 | $2,505,000 |
| 50–60 min | 1,000 | $2,515 | 1,000 | $2,515,000 |
| **Total** | **10,000** | **TWAP: $2,508** | **10,000** | **$25,045,000** |

The time-weighted average price was $2,508, slightly above the midpoint of the range. If the trader had placed one market order at minute 0, they might have moved the price to $2,530 immediately and filled at an unfavorable price; TWAP cost them less.

## When Not to Use TWAP

TWAP is not always optimal:

- **Small orders**: If you need to buy 100 tokens and market depth is good, a single market order is faster and just as cheap.
- **Extreme urgency**: If you must exit a position before a company announcement or market-moving event, waiting minutes for a TWAP to complete is too slow.
- **Trending markets**: In a strong bull or bear move, spreading the order over time can mean buying too high (in a rally) or selling too low (in a decline). A single market order captures the current price without further drift.
- **Illiquid tokens**: If the token is so illiquid that the spread is 5% wide and volume is sporadic, TWAP may not improve on one large order, and may increase [execution risk](/execution-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic trading](/algorithmic-trading/) — the broader discipline of automated order execution
- VWAP — volume-weighted average price, a refinement of TWAP
- Market impact — the price movement caused by large orders
- [Slippage](/slippage/) — the difference between expected and actual fill price
- Order routing — selecting the best venue for execution
- [Liquidity risk](/liquidity-risk/) — the danger of illiquid markets and wide spreads
- [Bid-ask spread](/bid-ask-spread/) — the friction TWAP aims to minimize

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where TWAP orders are executed
- Market depth — the volume available at each price level
- [Volatility](/volatility-smile/) — the risk that prices move during a TWAP window
- Arbitrage — multi-exchange execution strategies
- [Price discovery](/price-discovery/) — how markets aggregate information

</div>

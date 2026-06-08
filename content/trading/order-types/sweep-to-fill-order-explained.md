---
title: "Sweep-to-Fill Order Explained"
description: "A sweep-to-fill order walks up or down the order book across multiple price levels to execute a large trade immediately, improving certainty but increasing market impact costs."
keywords:
  - sweep to fill order explained
  - sweep order market impact
  - large order execution
  - order book levels
  - institutional trading tactics
  - algorithmic execution
image: "/svg/trading.svg"
---

*A **sweep-to-fill order** is a large buy or sell request that traverses multiple price levels of the order book until fully executed. Instead of placing a single limit order and waiting for the price to come to you, a sweep walks up the ask side (for a buy) or down the bid side (for a sell), accepting whatever price is necessary to fill immediately. The tradeoff: certainty of execution for worse average price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sweep Orders — speed vs. price</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Sweeps prioritize execution speed over minimizing market impact; useful for traders who must close a position now.</div>

|   |   |
|---|---|
| **Execution method** | Walk multiple order-book levels until filled |
| **Primary benefit** | Immediate, certain execution |
| **Primary cost** | Higher market impact and worse average price |
| **Typical user** | Institutions closing large positions quickly |
| **Visibility** | Creates visible impact; signals demand/supply |
| **Alternative** | Limit orders, iceberg orders, algorithms |
| **Market impact** | 30–100+ basis points depending on size |

</aside>

## How a sweep works

Imagine the order book for a stock at a given moment:

| Bid | Size | | Ask | Size |
|-----|------|---|-----|------|
| 99.50 | 1,000 | | 100.00 | 5,000 |
| 99.25 | 2,000 | | 100.05 | 3,000 |
| 99.00 | 3,000 | | 100.10 | 2,000 |

A buyer wants to execute 8,000 shares immediately. Instead of placing a limit order at 100.00 and waiting, they submit a **sweep-to-fill (or IOC, immediate-or-cancel) buy order** for 8,000 shares.

The order sweeps up the ask side:
1. Buy 5,000 shares at 100.00 (the first ask level).
2. Buy 3,000 shares at 100.05 (the second level).
3. The order is now fully filled; 8,000 shares executed.

Total cost: (5,000 × 100.00) + (3,000 × 100.05) = 500,000 + 300,150 = 800,150. Average price: 100.019 per share.

If the buyer had placed a limit order for 8,000 at 100.00, only 5,000 would have filled. The rest would wait until more sellers arrived at 100.00 or the buyer canceled and re-submitted at a higher price.

## Variants and terminology

**Sweep-to-fill** and **IOC (Immediate-or-Cancel)** are related but not identical.

An **IOC order** must fill immediately at the specified price or better; any portion that can't be filled at that price or better is canceled. This is a safety mechanism—the trader won't overpay.

A **sweep-to-fill** is a type of IOC that specifically walks the book—it accepts any price necessary to fill the full order size. Some venues use "sweep" and "IOC" interchangeably; others distinguish.

**Sniffing fills** or **pinging** is the aggressive variant: a trader places a small buy order to see if there's supply just above the current ask; if it fills, they know someone is willing to sell at that level, and a larger sweep might find deeper volume there.

## Why traders use sweeps

**Urgency**: A trader holding a large position might face margin pressure, approaching the end of a trading session, or news about to break. Waiting for favorable prices is riskier than taking worse prices now.

**Certainty**: Markets are uncertain. A limit order might wait indefinitely if the price never touches your level. A sweep guarantees execution (up to the available liquidity in the book).

**Hedging**: A hedger trying to neutralize a risk needs the hedge in place *now*, not eventually. The cost of a worse execution price is smaller than the cost of unhedged risk overnight.

**Block trades**: An institutional investor moving a large position may conclude that showing appetite on the open book (via a sweep) is faster than negotiating a block trade over the phone.

## Market impact and costs

A sweep imposes real market impact costs. The trader is paying above the best bid/ask for every share past the first level. In the example above, the average price (100.019) was 1.9 basis points higher than the best ask; for a larger order, the gap widens.

**Market impact** depends on:
- **Size**: Larger orders move the price more.
- **Liquidity**: Thin order books force sweeps into higher prices.
- **Volatility**: In volatile markets, traders demand wider compensation.
- **Time of day**: Early and late sessions have fewer liquidity providers.

A 10,000-share sweep in an illiquid microcap might cost 100+ basis points (1%). The same sweep in a highly liquid large-cap index might cost only a few basis points.

Institutional traders often model the relationship empirically: for every X shares I sweep, I expect to move the price by Y basis points. This becomes a factor in the decision to sweep immediately vs. use an algorithm to break the order into smaller pieces and execute over time.

## Alternatives to sweeping

**Limit orders** are passive. Post a limit buy at your target price and wait. If the stock doesn't fall to that price, you don't get filled, but you avoid overpaying.

**Patience and algorithms**: Slice a large order into smaller pieces and submit them over time or via a VWAP/TWAP algorithm. This reduces market impact by giving the book time to replenish between pieces, but it takes longer and assumes the trader can tolerate execution delay.

**Block trades**: Call major market makers directly and negotiate a large trade off the public book. This can be cheaper in some cases because it avoids the visible impact of a public sweep, though it requires dealer capital and time.

**Iceberg orders**: Post a visible slice of a large order; as the visible portion fills, more is revealed. This hides size and can reduce impact, but it also takes longer and some venues restrict or ban them.

## Visible impact and game theory

A sweep sends a signal: a big buyer or seller just walked up the book. Other traders see this, update their price forecasts, and may adjust their own orders. If many traders see a large buy sweep, they may interpret it as bullish information (why else would someone pay up?) and move their quotes higher, further disadvantaging the next buyer.

This is called **information leakage**. Even though a sweep fills in milliseconds, the market notices and reacts. High-frequency traders watching for such sweeps will sometimes adjust their positions preemptively, reducing liquidity further and increasing costs for the next large order.

This feedback effect is one reason institutions try to minimize visible order flow. A sweep is loud; it tells the market "I am a desperate buyer (or seller)." Algorithms and block trading try to suppress that signal.

## Regulatory and exchange rules

Most exchanges allow IOC and sweep orders, but rules vary:

- Some venues let an IOC walk the full book; others cap how far it can sweep.
- Some require disclosure of sweep orders in the trade feed (FINRA rules in the U.S. do).
- Circuit breakers may kick in if a sweep causes volatility spikes.
- Exchange fees may be different for aggressive orders, incentivizing or penalizing sweeps.

A trader using sweeps strategically will factor in exchange fees and latency. Trading off a cheaper venue might save fees but lose speed.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — immediate execution at any price
- [Limit Order](/limit-order/) — execution only at your target price
- [Bid-Ask Spread](/bid-ask-spread/) — the gap a sweep traverses
- Order Book — the levels a sweep walks through
- [Market Maker Trading](/market-maker-trading/) — who provides the liquidity being swept
- [Algorithmic Trading](/algorithmic-trading/) — alternative to sweeps for large orders
- Market Impact — the cost structure of large trades

### Wider context

- [Stock Exchange](/stock-exchange/) — where sweeps execute
- [Finra](/finra/) — regulates disclosure of sweep orders
- [High Frequency Trading](/high-frequency-trading-market-maker-vs-predatory/) — firms that capitalize on visible sweeps

</div>

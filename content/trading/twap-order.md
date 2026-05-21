---
title: "TWAP order"
description: "A TWAP (time-weighted average price) order is an algorithmic order that slices your large order into smaller pieces and executes them at fixed time intervals throughout the trading day."
keywords:
  - TWAP order
  - time-weighted average price
  - algorithmic order
  - execution
image: "https://picsum.photos/seed/twap-order/900/600"
---

*A **TWAP order** (time-weighted average price) is an [algorithmic order](/algorithmic-trading) that automatically breaks your large trade into equal-sized pieces and executes them at regular time intervals throughout the day. Unlike [VWAP](/vwap-order), which adapts to volume, TWAP simply divides time evenly. It is simpler than VWAP but may not achieve as good an average price.*

<div class="wiki-hatnote">

For volume-aware slicing, see [VWAP order](/vwap-order). For manual size control, see [iceberg order](/iceberg-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TWAP order — key facts</div>

<img src="https://picsum.photos/seed/twap-order/900/600" alt="A price chart showing TWAP execution schedule" />

<div class="wiki-infobox-caption">TWAP executes in equal-sized pieces at fixed time intervals.</div>

|   |   |
|---|---|
| **What it is** | Algorithmic order that slices evenly by time |
| **Execution method** | Equal-sized pieces at fixed time intervals |
| **Time awareness** | Yes; divides the day evenly |
| **Volume awareness** | No; ignores intraday volume patterns |
| **Best for** | Large orders in low-liquidity stocks, predictable execution |
| **Target** | Average price throughout the day |

</aside>

## How TWAP works

You want to buy 100,000 shares. You submit a TWAP order:
- **Total:** 100,000 shares
- **Window:** 9:30 a.m. to 4:00 p.m. (390 minutes of trading)
- **Interval:** 10-minute slices

The algorithm divides 100,000 shares by 39 intervals = 2,564 shares every 10 minutes:

- 9:30–9:40: Buy 2,564 at the market during this interval
- 9:40–9:50: Buy 2,564 at the market during this interval
- 9:50–10:00: Buy 2,564 at the market during this interval
- (continuing every 10 minutes until 3:50–4:00 p.m., final piece)

By end of day, you have bought all 100,000 shares at prices spread throughout the day.

## Why use TWAP?

**Simplicity.** TWAP is mechanically simple: divide total size by number of time intervals, execute evenly. No volume analysis needed.

**Predictability.** You know exactly when executions will happen (every 10 minutes, etc.). This can be useful if you want to coordinate with other strategies.

**Passive execution.** Like VWAP, you do not monitor the market; the algorithm handles it.

**Suitable for low-liquidity stocks.** In stocks with unpredictable volume patterns, TWAP's time-based approach is more reliable than VWAP's volume-based approach.

## TWAP vs. VWAP

| Feature | TWAP | VWAP |
|---|---|---|
| **Slicing basis** | Time (equal intervals) | Volume (adapts to volume) |
| **Execution schedule** | Fixed (every 10 minutes, etc.) | Variable (adapts to volume) |
| **Average price** | Based on prices throughout the day | Closer to day's actual VWAP |
| **Simplicity** | Very simple | More complex |
| **Best for** | Predictable execution, low liquidity | Optimal price in liquid names |
| **Cost** | May be worse than VWAP | Often better than simple market order |

**Example:** On a quiet day, VWAP might execute 80% of the order in the first two hours (when volume is high), then struggle the rest of the day. TWAP would spread execution evenly, potentially hitting worse prices in the quiet afternoon. Conversely, TWAP's predictability is an advantage if you do not care about average price as much as consistent execution.

## TWAP variations

**Custom intervals:** Instead of every 10 minutes, you can specify 5-minute, 30-minute, or hourly intervals.

**Randomized slices:** Some brokers offer randomized TWAP, where slice sizes vary slightly (to avoid algorithmic detection) while maintaining a time-based average.

**Limit price:** TWAP order with a [limit order](/limit-order) constraint (do not execute above a certain price).

## Practical example

A mid-cap company's stock is trading 50,000 shares per day on average — not very liquid. An institution needs to buy 100,000 shares. A [VWAP order](/vwap-order) would struggle because the 100,000-share volume represents two days of normal trading. They use a TWAP instead:

- Total: 100,000 shares
- Window: 10 trading days (two weeks)
- Interval: Hourly

The algorithm buys ~500 shares every hour for 10 days. This is passive and predictable; the institution knows execution is steady and will complete in two weeks.

## TWAP and market impact

TWAP minimizes market impact better than a [market order](/market-order) but may not minimize it as effectively as [VWAP](/vwap-order). Because TWAP ignores volume, it executes heavily during quiet periods (when the market has little liquidity) and lightly during busy periods (when plenty of buyers are trading). This is backwards from an optimization standpoint but provides simple, predictable execution.

## Broker support

Most large brokers support TWAP:
- **Interactive Brokers:** TWAP available for stocks and derivatives.
- **Schwab, Fidelity:** TWAP available for stocks.
- **Smaller brokers:** May not support TWAP; check documentation.

## When to use TWAP vs. VWAP

**Use TWAP if:**
- The stock is thinly traded (VWAP may not adapt well).
- You want simple, predictable execution.
- You do not care about minimizing average price (just want consistent execution).
- Your execution window is multiple days (VWAP assumes one day).

**Use VWAP if:**
- The stock is liquid (normal daily volume patterns).
- You want to optimize for average price.
- The execution window is one day.
- You prefer adaptive algorithms over fixed schedules.

## Real-world comparison

Suppose you need to buy 50,000 shares of a mid-cap stock over one day:

**Market order:** You get all 50,000 now at market (9:30 a.m.), moving the price $0.15. You pay $50.15 average.

**VWAP order:** The algorithm spreads execution across the day, adapting to volume. You get all 50,000 by 4 p.m., achieving an average price of $50.03 (much closer to VWAP than a single market order).

**TWAP order:** The algorithm divides the 50,000 into 6 equal 8,333-share chunks, executing every hour. You pay $49.99, $50.00, $50.02, $50.04, $50.05, $50.03 average = $50.02.

In this case, VWAP is best (captures volume dynamics), TWAP is decent (simple and steady), and a market order is worst (too much impact).

## See also

<div class="wiki-seealso">

### Algorithmic and execution orders

- [VWAP order](/vwap-order) — volume-weighted average price
- [Algorithmic trading](/algorithmic-trading) — optimal order execution
- [Iceberg order](/iceberg-order) — size-hiding mechanism
- [Smart order router](/smart-order-router) — routes across venues

### Execution and market impact

- Market impact — cost of moving the market
- Slippage — gap between expected and actual price
- Liquidity — available volume at each price
- Block trading — large orders use TWAP and VWAP

### Market structure

- Order book — TWAP executes against this
- Intraday trading — execution throughout the day
- [Best execution](/best-execution) — regulatory obligation

</div>

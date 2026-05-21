---
title: "VWAP order"
description: "A VWAP (volume-weighted average price) order is an algorithmic order that slices your large order into smaller pieces and executes them throughout the day, targeting an execution price equal to the day's volume-weighted average price."
keywords:
  - VWAP order
  - volume-weighted average price
  - algorithmic order
  - execution
image: "/svg/trading.svg"
---

*A **VWAP order** (volume-weighted average price) is an [algorithmic order](/algorithmic-trading) that automatically breaks your large trade into small pieces and executes them throughout the trading day. The algorithm targets an execution price equal to or better than the day's VWAP — the price that accounts for trading volume at each level. Institutional traders use VWAP to execute large positions with minimal market impact.*

<div class="wiki-hatnote">

For a simpler time-based slicing, see [TWAP order](/twap-order). For manual size control, see [iceberg order](/iceberg-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">VWAP order — key facts</div>

<img src="/svg/trading.svg" alt="A price chart showing VWAP line and sliced executions" />

<div class="wiki-infobox-caption">VWAP order (red line) targets the volume-weighted average price for the day.</div>

|   |   |
|---|---|
| **What it is** | Algorithmic order that slices and executes throughout the day |
| **Target** | VWAP (volume-weighted average price for the day) |
| **Execution method** | Breaks order into small pieces, adapts to intraday volume |
| **Best for** | Large orders, minimizing market impact, achieving average prices |
| **Speed** | Full day or more (all-day execution) |
| **Cost advantage** | Typically beats a single [market order](/market-order) due to execution timing |

</aside>

## What is VWAP?

VWAP is a weighted average price:

**VWAP = Σ (Price × Volume) / Σ Volume**

If a stock trades 1,000 shares at $50, then 2,000 shares at $51, then 500 shares at $52:
- VWAP = ($50×1000 + $51×2000 + $52×500) / (1000+2000+500)
- VWAP = $51.09

VWAP reflects the "fair" price during the day, accounting for when trades happen at different prices.

## How a VWAP order works

You want to buy 100,000 shares of a stock during a normal trading day. Instead of placing a 100,000-share market order at the open (which would move the price sharply), you submit a VWAP order to your broker:

- **Your goal:** Buy 100,000 shares at the day's VWAP (or better).
- **The algorithm:** Monitors intraday trading volume and prices. It slices your order into small pieces and releases them gradually, attempting to buy at prices near VWAP.

For example:
- 9:30 a.m. (open): Buy 5,000 at $50.00.
- 10:45 a.m.: Buy 8,000 at $50.02.
- 1:00 p.m.: Buy 12,000 at $50.05.
- 3:00 p.m.: Buy 75,000 at $50.04.
- (continuing throughout the day until all 100,000 are filled)

If the day's VWAP ends up at $50.03, your average fill price might be $50.02 or $50.04 — close to VWAP.

## Why use VWAP?

**Market impact.** A single 100,000-share market order would move the price sharply. VWAP slices it, so the market does not know a huge buyer is present. Sellers do not pull their offers; prices move less.

**Average price improvement.** By spreading execution throughout the day, you often achieve a better average price than an immediate market order. VWAP captures intraday price variations.

**Passive execution.** You do not have to monitor the market. The algorithm runs and executes automatically based on volume signals.

## VWAP vs. market order

| Factor | Market order | VWAP order |
|---|---|---|
| **Execution speed** | Immediate | Throughout the day |
| **Market impact** | High (large visible order) | Low (small slices) |
| **Average price** | Current market price (often not great for large orders) | Close to VWAP (often better) |
| **Certainty** | Guaranteed fill | Not guaranteed (may not fill all by day's end) |

For a 100,000-share buy:
- Market order: You get 100,000 shares now, but likely at 100k shares' worth of slippage (e.g., $50.10 instead of $50.00).
- VWAP order: You get them throughout the day at prices averaging around $50.03 (closer to VWAP), but it takes all day.

## VWAP vs. TWAP

| Feature | VWAP | [TWAP](/twap-order) |
|---|---|---|
| **Time slicing** | Adapts to volume | Fixed time intervals |
| **Volume awareness** | Yes; targets volume-weighted price | No; ignores volume |
| **When to use** | Days with normal volume patterns | Days with unpredictable volume or low liquidity |
| **Result** | Often achieves better average price | More predictable execution, less optimal price |

VWAP is volume-aware and smarter; TWAP is simpler and more mechanical.

## Limitations of VWAP

**Unfilled remainder.** A VWAP order that does not fill all shares by day's end leaves an unfilled remainder. You might get 85,000 shares filled and 15,000 still pending at 3:55 p.m. You then have to decide: cancel the rest, or convert to a market order?

**Trending markets.** If the stock is in a strong uptrend all day, VWAP might be too high (you miss the move). If it is in a downtrend, VWAP might be too low (you buy at the worst prices all day). VWAP works best in rangebound markets.

**Information leakage.** Sophisticated traders can sometimes infer a VWAP order by watching the volume and prices. Once they know you are using VWAP, they can front-run you slightly.

## VWAP and intraday liquidity

VWAP orders work best in liquid stocks with normal, predictable intraday volume patterns. In thinly traded securities or during low-volume periods, VWAP can fail to execute efficiently.

## Broker support

Most large brokers offer VWAP:
- **Interactive Brokers:** VWAP available for stocks and many derivatives.
- **Schwab, Fidelity, TD Ameritrade:** VWAP available for stocks.
- **Discount brokers:** May not offer VWAP; check documentation.

Many brokers also offer variations:
- **VWAP target:** Execute to hit a specific VWAP (not the day's actual VWAP, but a target).
- **Limit price:** VWAP order with a [limit order](/limit-order) constraint (do not execute above/below a certain price).

## Real-world example

An institution needs to buy 1 million shares of a large-cap stock. A single market order would move the price $0.20 or more. They submit a VWAP order to their broker:

- Total: 1,000,000 shares
- Execution window: 9:30 a.m. to 4:00 p.m. (full trading day)
- Limit price: Not to exceed VWAP + $0.05 (belt and suspenders)

The broker's VWAP algorithm breaks it into 50 orders of 20,000 shares each, spread throughout the day, adapting to volume. By 4:00 p.m., the institution is fully loaded, having paid an average price very close to the day's VWAP with minimal market impact.

## See also

<div class="wiki-seealso">

### Algorithmic and execution orders

- [TWAP order](/twap-order) — time-weighted average price
- [Algorithmic trading](/algorithmic-trading) — optimal order execution
- [Smart order router](/smart-order-router) — routes orders across venues
- [Iceberg order](/iceberg-order) — simpler size-hiding mechanism

### Execution and market impact

- Market impact — cost of moving the market
- Slippage — gap between expected and actual price
- Block trading — large orders often use VWAP
- Information leakage — algorithms can detect VWAP orders

### Market microstructure

- Order book — where VWAP algorithm finds liquidity
- Intraday volume — VWAP targets this pattern
- Liquidity — availability of shares at each price
- [Best execution](/best-execution) — VWAP helps achieve this

</div>

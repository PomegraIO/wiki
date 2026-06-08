---
title: "How Iceberg Order Display Size Affects Fill Rate"
description: "Trade-off between small and large display quantities in iceberg orders: less information leakage versus faster queue replenishment and higher fill probability."
keywords:
  - iceberg order display size fill rate
  - iceberg order execution strategy
  - limit order queue position
  - market impact and order information
  - hidden order trading
image: /svg/trading.svg
---

*An **iceberg order** displays only a small portion of its total quantity on the order book while hiding the rest. The trader faces a critical choice: use a tiny display size to conceal the full order size (avoiding price impact from market awareness), or show a larger display size to rebuild queue position faster and increase fill probability. This trade-off between secrecy and execution speed defines iceberg order strategy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iceberg Orders — Display size dilemma</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Smaller display conceals intent; larger display replenishes the queue faster.</div>

|   |   |
|---|---|
| **Typical display size** | 1–10% of total order |
| **Information leakage risk** | Lower with tiny displays; high with large ones |
| **Queue position loss per fill** | Resets after each tranche fills |
| **Fill probability** | Increases with larger display quantities |
| **Time to fill** | Slower with small displays; faster with large |
| **Optimal setting** | Depends on order size, volatility, target prices |

</aside>

## Why traders use iceberg orders

A trader holding a large position — say, 500,000 shares — faces a practical problem. If she places a single [limit order](/limit-order/) for 500,000 shares, every market participant sees it, anticipates her intent, and the market price adjusts against her. Competing traders jump ahead in the queue, counterparties move their own bids lower, and her average execution price deteriorates.

An iceberg order hides this intention. The trader reveals only 10,000 shares on the book (the visible **tranche**), leaves the remaining 490,000 hidden, and configures the order to refresh automatically: each time the visible tranche fills, the order algorithm replaces it with another 10,000-share tranche until all 500,000 shares are gone.

To other market participants, the order looks like a modest 10,000-share bid or offer. They do not realize the trader intends to buy 500,000 shares. This reduces the price impact of her order.

## The information leakage problem

**Information leakage** is the core risk of any large order. If the market knows you want to buy 500,000 shares, it will:

1. Assume you plan to accumulate (bullish signal)
2. Raise the offer price preemptively
3. Let you buy only if you pay higher prices
4. Increase your average cost

An iceberg order mitigates leakage by showing only the tranche. However, sophisticated algorithms and experienced traders can detect icebergs. They watch for patterns: if the same 10,000-share bid keeps appearing at the same price and refilling instantly after filling, they infer a hidden order and trade accordingly. Very small display sizes (e.g., 100 shares) are even more suspicious — they signal hidden volume and invite aggressive competition.

The solution: use a display size large enough to look natural (not obviously artificial) while still concealing the full order magnitude.

## Display size and queue position

Every time a displayed tranche fills completely, the algorithm removes it from the book and adds a new one. This creates a **queue position reset**. In [limit order](/limit-order/) books, queue position matters: if the bid is $100 and you place a bid at $100, you join the end of the queue. When the price moves to $100, your order fills in sequence. If the order ahead of you fills first, you step forward.

An iceberg order resets queue position after each fill. Suppose:

1. You place a 500,000-share iceberg order to buy, displaying 10,000 shares at $100.
2. Someone sells 10,000 shares to you; your visible tranche fills.
3. Your algorithm immediately posts a new 10,000-share tranche at $100 — but now you are at the back of the queue again.

A competing buyer who placed an ordinary 10,000-share limit order at $100 and stayed in the queue the entire time will fill before your second tranche (assuming the price stays at $100). The competing order had queue priority.

If you increase your display size to 50,000 shares, you lose queue position less often (every 50,000 shares instead of every 10,000) but you also broadcast your size more visibly, increasing information leakage and price impact.

## Fill probability and speed

**Fill probability** is the likelihood that the hidden portions of your order execute within a given timeframe. It depends on:

- **Display size:** Larger visible quantities attract more counterparties. If you show 50,000 shares instead of 5,000, more traders may cross your order, filling your iceberg faster.
- **Price level:** Aggressive pricing (a buy order at higher prices, a sell order at lower prices) fills faster.
- **Market volatility:** In quiet markets, small iceberg tranches may not fill for hours. In volatile markets, the price moves, other traders hit your order more readily, and fills happen quickly.
- **Trade direction:** Large buy orders tend to fill faster in rising markets (sellers are willing); large sell orders tend to fill faster in falling markets.

A very small display size (e.g., 100 shares of a 1-million-share order) means you will execute slowly, even if the market is favorable. Each fill is tiny, queue position resets frequently, and the full order may take days. A larger display size (e.g., 100,000 shares) accelerates fills significantly but increases the risk that the market sees the pattern and trades against your hidden intent.

## The optimization trade-off

An iceberg trader must choose a display size that balances:

| Factor | Small Display (e.g., 1% of total) | Large Display (e.g., 10% of total) |
|--------|---|---|
| **Information leakage** | Lower | Higher |
| **Price impact** | Lower | Higher |
| **Fill speed** | Slower | Faster |
| **Queue resets per execution** | More frequent | Less frequent |
| **Likelihood of pattern detection** | Very high (suspicious) | Lower (more natural) |

In practice, many traders settle on display sizes in the range of 3–10% of the total order. This is large enough to seem natural and attract fills, but not so large that the entire order size is obvious. The specific choice depends on:

- **Order size:** A 100,000-share order with a 10,000-share display is reasonable; a 100-share order with a 10-share display looks artificial.
- **Stock liquidity:** In highly liquid stocks (e.g., SPY or Apple), showing 50,000 shares is normal; in illiquid names, 5,000 shares is more natural.
- **Volatility:** In choppy markets, show less to avoid information leakage; in trending markets, show more to fill faster.
- **Time urgency:** Need the position filled today? Increase the display. Willing to wait a week? Decrease it.

## Algorithmic execution and TWAP/VWAP

Many institutional traders do not manually set iceberg display sizes. Instead, they use algorithmic execution algorithms — algorithms that automatically divide large orders into smaller orders and execute them over time. [TWAP](/moving-average/) (Time-Weighted Average Price) and [VWAP](/moving-average/) algorithms are popular examples.

These algorithms internally optimize display sizes based on market conditions, recent fill rates, and the order's progress toward completion. A VWAP algorithm, for instance, aims to execute at the market's volume-weighted average price by adjusting both the order size and timing based on real-time trading volume. It may show smaller tranches in quiet periods and larger tranches when volume spikes.

## Information leakage in practice

Sophisticated market participants use machine learning and order-flow analysis to detect hidden orders. They monitor:

- Patterns of orders appearing and disappearing at the same price
- Correlations between small visible orders and subsequent price moves
- Statistical anomalies in order placement and cancellation

This arms race between iceberg traders (trying to hide intent) and other traders (trying to detect it) is a constant feature of modern equity markets. The best-kept secret is a large order that executes at natural prices, without suspicious patterns, over a timeframe consistent with other market flow.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — Foundation for iceberg orders
- [Market order](/market-order/) — Alternative (transparent but less favorable pricing)
- [Market maker trading](/market-maker-trading/) — Creates quotes that iceberg orders target
- [Price discovery](/price-discovery/) — Influence of hidden orders on fair value
- [Bid-ask spread](/bid-ask-spread/) — Cost of large visible orders

### Wider context

- [Over-the-counter market](/over-the-counter-market/) — Alternative for large orders (more privacy)
- [Execution risk](/execution-risk/) — Risk that orders do not fill as expected
- [Market impact](/market-risk/) — General price movement from large trades
- [Order types](/limit-order/) — Other mechanisms for executing large orders

</div>

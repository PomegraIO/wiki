---
title: "Market Order vs Limit Order: Execution Risk Compared"
description: "Compare execution risk in market orders and limit orders, showing the trade-off between guaranteed fill and price certainty."
keywords:
  - market order
  - limit order
  - execution risk
  - order types
  - fill risk
  - slippage
  - trading execution
image: /svg/trading.svg
---

*A **market order** promises a nearly instant fill at the best available price in the market right now—but that price may be far from what you expected if the market moves between submission and execution. A **limit order** guarantees you will never pay more (or receive less) than a specified price—but you may not fill at all, leaving you unexecuted and exposed. The choice between them is a direct trade-off: market orders carry **price risk**, while limit orders carry **execution risk**.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order type execution trade-offs</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Every order type solves one problem at the cost of another.</div>

|   |   |   |
|---|---|---|
| **Characteristic** | **Market Order** | **Limit Order** |
| **Fill guarantee** | Nearly certain | Conditional on price |
| **Price guarantee** | None; best available | Capped at limit (buy) or floored (sell) |
| **Execution speed** | Immediate | Delayed or not at all |
| **Primary risk** | Slippage; adverse price movement | Non-execution; missing the move |
| **When to use** | Need certainty of fill | Need certainty of price |
| **Cost to fill** | Pays the [spread](/bid-ask-spread/) | Pays the spread; may wait longer |

</aside>

## Market order execution risk

When you submit a [market order](/market-order/), you are instructing the exchange or [broker](/broker/) to sell or buy immediately at whatever price is available. The execution is fast—usually fractions of a second on modern exchanges—but the price is not locked in when you click submit.

### Slippage and adverse fills

The gap between the price you see on your screen and the price at which you actually fill is called **slippage**. It arises from two sources:

1. **Market movement**: If you place a market order to buy 10,000 shares and 5,000 shares of supply evaporate before your order reaches the exchange, the price you fill at will be higher than the best price you saw when you clicked.

2. **Queue position**: On a continuous exchange, [limit orders](/limit-order/) sit in a queue at each price level. If you submit a market order, you fill against the orders already at the best [bid-ask-spread](/bid-ask-spread/). The first 1,000 shares might fill at $50.05 (the best ask), the next 2,000 at $50.10, and the next 2,000 at $50.15. Your average fill price is the weighted average, higher than the initial best ask.

### Volatile markets amplify the risk

In thin or volatile markets, slippage widens dramatically. If you submit a market order to sell 100,000 shares of a thinly traded stock when bid-ask spreads are wide, you may fill the first tranche at the best bid, the next tranche 5 cents lower, and subsequent tranches 20 cents or more lower. Your total proceeds can fall thousands of dollars below what the initial best bid suggested.

### A concrete scenario

You want to buy 5,000 shares of a stock trading at $100 bid / $100.05 ask. You submit a market buy order at 10:00 AM.

- At 10:00:00.001, the ask price is still $100.05; 2,000 shares fill at this price.
- A large sell order hits the market; the ask jumps to $100.15.
- Your remaining 3,000 shares fill at $100.15.
- **Total cost**: 2,000 × $100.05 + 3,000 × $100.15 = $500,450. The blended price is $100.09, not $100.05 as you may have anticipated.

Over 5,000 shares, you paid $200 more than the best ask you saw. This is market order execution risk.

## Limit order execution risk

A [limit order](/limit-order/) specifies a maximum price you will pay (for a buy) or a minimum price you will accept (for a sell). You fill only if the market reaches or exceeds your limit; otherwise, your order remains outstanding indefinitely—or until you cancel it.

### Non-execution and opportunity cost

The primary risk of a limit order is that it may never fill. If you submit a limit buy order at $99.50 for a stock currently trading at $100, and the stock rises instead of falling, your order sits unfilled. You miss the market move and don't get the shares you wanted.

This is **execution risk**: the risk that you remain uninvested (or unhedged, if selling) when you needed to be.

### Missing the fill window

Price moves quickly. A stock trading $100 may be $100.50 five minutes later. If your limit order at $99.50 is intended to catch a dip but the dip never materializes, you are exposed to the upside move with no position—and no way to fill your original order without canceling and submitting a market order at a worse price.

### A concrete scenario

You want to buy 5,000 shares but think the stock at $100 is overpriced. You submit a limit buy order at $99.50, expecting a pullback.

- The stock ticks up to $100.25, then $100.50, then $101.00.
- Your order is still at $99.50 and unfilled—no shares purchased.
- You decide the stock is no longer "cheap" at $101, so you cancel your limit order.
- **Result**: You have zero shares and zero execution. You missed the opportunity entirely.

If you had submitted a market order at $100, you would have filled at ~$100.05 and captured any subsequent upside. The cost of your certainty of execution was ~$250 in slippage.

## Comparing the risks side by side

| Scenario | Market Order Outcome | Limit Order Outcome |
|---|---|---|
| Stock trends in your favor after you order | You captured the move; slippage was the cost | You missed the move if your limit was not hit |
| Stock trends against you after you order | You filled anyway, at a worse price than expected | You never filled; you are unprotected but also uninvested |
| Sudden volatility spikes at the moment you order | You fill at a much worse price | You may not fill at all, depending on the size of the move |
| Liquid market with tight spreads | Slippage is minimal | The chance of non-execution is low; prices move slowly |
| Thin or volatile market | Slippage is severe; you may fill across a wide range of prices | Limit orders are safer because you control the worst price, but non-execution risk is high |

## When each order type is appropriate

**Use a market order when:**
- You need certainty of execution (e.g., you are hedging a risk and must be covered today).
- The market is liquid and spreads are tight (slippage risk is small).
- You are trading a large size and accepting the cost of impact is preferable to waiting for a limit fill.
- Price timing is less important than getting the trade done.

**Use a limit order when:**
- You have time; you can wait for your price.
- The market is thin or volatile, and avoiding a bad fill is more important than immediate execution.
- You are willing to accept the risk of non-execution in exchange for price certainty.
- You are scaling into a position and want to control your average entry price precisely.

## Hybrid approaches: iceberg orders and more

Traders seeking a middle ground use [iceberg orders](/iceberg-order-mechanics/) (which hide most of the size to avoid market impact), VWAP orders (algorithmic execution that targets a volume-weighted average), or other algorithms that blend market and limit logic.

The underlying tension remains: fill certainty and price certainty are in tension. Every execution mechanism trades one for the other.

## See also

<div class="wiki-seealso">

### Closely related

- [Market order](/market-order/) — execute at the best available price
- [Limit order](/limit-order/) — execute at a specified price or better
- [Bid-ask spread](/bid-ask-spread/) — the gap between the best buy and best sell prices
- [Iceberg order mechanics](/iceberg-order-mechanics/) — hiding order size to reduce market impact
- Order queue — how limit orders are prioritized

### Wider context

- [Market-maker trading](/market-maker-trading/) — how liquidity is provided
- [Price discovery](/price-discovery/) — how market prices emerge from trading
- Market impact — how large orders move prices
- [Algorithmic trading](/algorithmic-trading/) — automated execution strategies

</div>

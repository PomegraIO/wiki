---
title: "Crypto Order Types"
description: "Market, limit, stop-loss, and advanced order formats available on cryptocurrency exchanges for executing trades."
keywords:
  - crypto trading
  - order types
  - market order
  - limit order
  - stop-loss
  - trading algorithms
  - exchange mechanics
---

*A **crypto order type** is an instruction format used on cryptocurrency [exchanges](/wiki/cryptocurrency-exchange/) to execute buy or sell trades. Like traditional stock exchanges, crypto platforms offer [market orders](/wiki/market-order/) (immediate execution at current price), [limit orders](/wiki/limit-order/) (execution only at a specified price), [stop-loss orders](/wiki/stop-order/), and advanced formats like iceberg orders and time-weighted average price (TWAP) algorithms.*

## Market orders

A market order is the simplest: "sell 1 Bitcoin now at the best available price." Execution is near-instantaneous, but the price is uncertain—you get whatever the [order book](/wiki/order-book-depth/) offers at that moment. If the order book is thin (low liquidity), your market order might move the price significantly, creating [slippage](/wiki/slippage/). On major exchanges like Coinbase or Kraken with deep order books, slippage on market orders for major cryptocurrencies is minimal (1–10 basis points). On smaller exchanges or for altcoins, slippage can be 1–5%.

Market orders are preferred when speed is critical (e.g., during volatile moves when you want to exit immediately) and you accept some price uncertainty.

## Limit orders

A [limit order](/wiki/limit-order/) specifies a price: "sell 1 Bitcoin only if the price is at least $50,000." If the current price is $49,500, the order waits in the [order book](/wiki/order-book-depth/) until price rises to $50,000 or above. Limit orders guarantee price but not execution—if price never reaches your limit, you don't sell.

Limit orders are placed on both sides of the market. Buy limit orders ("buy 1 Bitcoin at $48,000") sit below the current price; sell limit orders sit above. The [bid-ask spread](/wiki/bid-ask-spread/) is the gap between the highest buy and lowest sell limit orders at any moment. On liquid pairs like BTC/USD, the spread might be $0.10 (1 basis point). On illiquid altcoins, it can be 2–5%.

Most exchanges offer "post-only" limit orders, which sit in the order book and earn [maker fees](/wiki/maker-taker-fee-model/) (0.01–0.1%). "Aggressive" limit orders that immediately cross the spread incur [taker fees](/wiki/maker-taker-fee-model/) (0.05–0.2%). Limit orders are preferred when you have a specific price target and are willing to wait.

## Stop-loss and stop-limit orders

A [stop-loss order](/wiki/stop-order/) is a conditional order: "if Bitcoin falls to $45,000, sell immediately." The order sleeps until the trigger price is hit, then converts to a market order and executes. Stop-loss orders are the primary risk-management tool for traders holding volatile positions.

However, stop-loss orders have pitfalls. During flash crashes or rapid declines (e.g., Bitcoin dropping 15% in 30 seconds), stop-loss orders cluster at round numbers and can trigger cascading liquidations. A trader with a stop at $45,000 sees price touch $45,000 briefly, their order sells at $42,000, and they miss the subsequent rebound. This is called a "stop-hunt" or "wick" in crypto trading.

A **stop-limit order** combines the two: "if price hits $45,000, place a limit order to sell at $45,000." This prevents selling at a worse price but risks not selling at all if price falls past $45,000 without reaching your limit. Stop-limit orders are more nuanced but carry execution risk.

## Advanced order types

**Iceberg orders** (also called "reserve orders") hide large orders in tranches. A trader wanting to sell 100 Bitcoin might submit: "Sell 100 BTC, but show only 5 BTC in the order book at a time." As the visible 5 are filled, the next 5 appear. This reduces market impact and reduces the visibility of large orders. Most exchanges offer icebergs; some charge a premium fee.

**Post-only orders** (or "maker-only" orders) are limit orders that will never cross the spread. They are guaranteed to be placed as a maker and earn maker rebates. If your post-only order would immediately fill against existing orders, it's rejected instead. Useful for passive strategies that want to avoid taker fees.

**Bracket orders** (also called "one-cancels-other" or OCO orders) pair a primary order with two exit orders: one for profit-taking, one for stop-loss. You submit: "Buy 1 Bitcoin at $49,000, with a sell limit at $51,000 (take profit) and sell stop at $47,000 (stop loss)." Once either exit triggers, the other is automatically cancelled. This is useful for risk management but is not available on all exchanges.

**Time-Weighted Average Price (TWAP)** and **Volume-Weighted Average Price (VWAP)** algorithms break large orders into smaller chunks and execute them gradually over time or across volume levels. A trader wanting to buy 1,000 Bitcoin without moving the market can submit a TWAP order to buy 50 BTC every 30 minutes for 10 hours. The algorithm reduces market impact but accepts slower execution.

## Fill-or-Kill and Immediate-or-Cancel

A **Fill-or-Kill (FOK)** order must be filled completely immediately or not at all. If you submit "buy 5 Bitcoin FOK at $49,500" and only 4 Bitcoin are available, the entire order is cancelled. FOK orders reduce uncertainty about partial fills but risk no execution.

An **Immediate-or-Cancel (IOC)** order executes whatever portion is available immediately, cancelling the remainder. "Buy 5 Bitcoin IOC at market" executes as much as possible right now, then cancels any unfilled portion. IOC orders are common in [algorithmic trading](/wiki/algorithmic-trading/) to ensure capital isn't locked in unfilled limit orders.

## Comparison across exchanges

Major exchanges (Coinbase, Kraken, Binance) offer most standard order types. Smaller exchanges may have only market and limit. Decentralized exchanges ([DEXs](/wiki/decentralized-exchange/)) that use automated market makers (AMMs) don't have traditional order books—you submit a trade, and the AMM algorithm executes it at a price determined by its reserve ratios and [slippage](/wiki/slippage/).

## Integration with margin and leverage

[Margin trading](/wiki/margin-trading-crypto/) platforms often use stop-loss orders for liquidation protection. An exchange will automatically liquidate a leveraged position if the margin ratio falls below a threshold, functioning like a stop-loss at the margin floor. Traders can set manual stop-losses above the liquidation level to exit earlier.

## Costs and considerations

Each order type carries different fees and execution certainty. Market orders fill fast but at uncertain prices; limit orders are patient but might not execute. Maker orders earn rebates on some exchanges, while taker orders incur fees. Stop orders require monitoring or automatic trigger infrastructure on the exchange's servers. The choice depends on trade urgency, certainty requirements, and cost sensitivity.

<div class="wiki-seealso">

### Closely related
- [Order Types](/wiki/order-types/) — the general framework of order types across all markets
- [Limit Order](/wiki/limit-order/) — patient price-specified execution
- [Market Order](/wiki/market-order/) — immediate execution at market price
- [Stop Order](/wiki/stop-order/) — conditional order triggered by price level

### Wider context
- [Cryptocurrency Exchange](/wiki/cryptocurrency-exchange/) — platforms where crypto order types are executed
- [Order Book](/wiki/order-book-depth/) — the matching engine that executes orders
- [Slippage](/wiki/slippage/) — the execution cost from order placement
- [Algorithmic Trading](/wiki/algorithmic-trading/) — automated execution strategies using advanced order types

</div>

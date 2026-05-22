---
title: "Market Order Execution"
description: "Instruction to buy or sell an asset immediately at the best available price without specifying a price limit."
keywords:
  - order type
  - immediate execution
  - bid-ask spread
  - market impact
  - execution quality
---

*A **market order** instructs a broker to execute a buy or sell immediately at the best available [bid-ask spread](/wiki/bid-ask-spread/), accepting whatever price the market offers at that moment. Unlike [limit orders](/wiki/limit-order/), market orders guarantee execution but offer no price protection. They are the default for urgent trades and small positions, but can incur slippage and market-impact costs on large trades.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Execution guarantee** | Nearly guaranteed for liquid securities |
| **Price guarantee** | None; you accept the market price |
| **Speed** | Typically filled in milliseconds |
| **Typical use** | Quick exit, time-sensitive trades |
| **Cost | Bid-ask spread plus potential slippage |
| **Market impact** | Large orders move prices against you |

</aside>

## Immediate execution and the cost of certainty

When you place a market order to buy a stock, your broker routes it to the market and sells to you at the current ask price—what the seller demands. If the ask is 50.15 and you market-buy 100 shares, you pay 5,015 dollars (plus commission). The advantage is certainty: your order is nearly certain to fill instantly. The disadvantage is you have no control over price; if the market moves 10 cents while your order is in flight, you bear that cost.

For a [stock](/wiki/stock/) trading with tight spreads (1 cent or less), the cost is minimal. For illiquid securities or [commodity futures](/wiki/commodity-futures-rolling/), spreads can be much wider, and a market order can cost you significantly.

## How market impact scales with order size

A market order for 100 shares of a liquid [stock](/wiki/stock/) probably fills instantly at the best ask price. A market order for 1 million shares of the same stock does not. The broker's market maker or exchange has limited inventory at the best ask and must go to the next level (a higher ask price) to fill the rest. This sequential filling from best-to-worse prices is called **price improvement** if you get better-than-quoted prices, or **market impact** if you pay worse prices deeper in the book.

Professional traders minimize market impact by breaking large orders into smaller chunks using [volume participation orders](/wiki/volume-participation-order/) or algorithmic execution. Retail traders who market-buy 100,000 shares in one order will pay dearly.

## Slippage: the gap between expectation and reality

Slippage is the difference between the price you expected to get and the actual fill price. For limit orders, slippage is explicit: you set the maximum price; if you don't get filled, nothing happens. For market orders, slippage is hidden in the bid-ask spread and market impact. You see the order confirmation, see the fill price, and might not realize you paid 10 cents worse than the market-quoted mid-price due to slippage.

On high-frequency [trading](/wiki/algorithmic-trading/) venues, large market orders face significant slippage because fast traders and [high-frequency trading](/wiki/high-frequency-trading/) firms front-run the big order, moving the price against you.

## Contrast with limit orders and their patience trade-off

A [limit order](/wiki/limit-order/) says, "Sell at 50.00 or better, but don't sell for less." This gives you price control but no execution certainty; if the stock never reaches 50.00, your order expires unfilled. A market order says, "Sell immediately at the best price, whatever it is," guaranteeing execution but leaving price to chance.

The choice is a time-vs.-price trade-off: market orders prioritize speed, limit orders prioritize price.

## When market orders are essential

A [short squeeze](/wiki/short-squeeze/) or rapidly falling stock can make limit orders obsolete. If you are short a stock that is rallying 20% in a day, you need to cover *now*, not wait for a limit price that may never come. A market order exits the position immediately, accepting whatever price the market offers.

During crises ([black swan](/wiki/black-swan/) events, central bank shocks), market orders during the chaos are often the only executable order type, and fills can be dramatically worse than the opening or closing price.

## Execution venues and order routing

When you send a market order, your broker must route it to an exchange or [alternative trading system](/wiki/alternative-trading-system/). Most brokers are obligated to route to the venue showing the best bid-ask at that moment under [regulation NMS](/wiki/reg-nms-adoption/). But execution quality varies: some brokers fill market orders at worse-than-best prices and pocket the difference (a practice called [payment for order flow](/wiki/payment-for-order-flow/)). Others route to the best price and charge a commission.

<div class="wiki-seealso">

### Closely related
- [Limit order](/wiki/limit-order/) — alternative order type with price control
- [Bid-ask spread](/wiki/bid-ask-spread/) — cost incurred by market order execution
- [Best execution](/wiki/best-execution/) — broker obligation to fill orders fairly
- [Volume participation order](/wiki/volume-participation-order/) — algorithm for large orders to reduce slippage

### Wider context
- [Order types](/wiki/order-types/) — full taxonomy of execution instructions
- [High-frequency trading](/wiki/high-frequency-trading/) — source of slippage on market orders
- [Regulation NMS](/wiki/reg-nms-adoption/) — rules governing order routing
- [Execution quality](/wiki/execution-quality-analysis/) — how to measure market order costs

</div>

---
title: "Fill-or-Kill Order"
description: "What a fill-or-kill order is, how it differs from immediate-or-cancel, and why traders use it to avoid unwanted partial fills."
keywords:
  - fill or kill order
  - fill or kill order explained
  - fok order
  - order types
  - partial fill
image: "/svg/trading.svg"
---

*A **fill-or-kill order** (FOK) is an instruction to buy or sell a security at a specified price, but only if the entire quantity can be filled immediately. If the order cannot be filled in full right away, it is automatically cancelled without executing any part of the trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fill-or-Kill Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">FOK eliminates the risk of a partial fill sitting on the books after you've walked away from a trade.</div>

|   |   |
|---|---|
| **Execution requirement** | All or nothing; no partial fill |
| **Life span** | Evaluated and cancelled within milliseconds if not fully filled |
| **Risk to trader** | Missing the trade entirely if liquidity is not available |
| **Common use** | Large block trades, arbitrage, block options trading |
| **Similar to** | Immediate-or-cancel (IOC), but FOK requires zero partial fill (IOC allows any remainder) |
| **Supported by** | Most major [exchanges](/stock-exchange/) and [brokers](/broker/) |

</aside>

## How a fill-or-kill order works

When you submit a fill-or-kill order, the exchange or market maker's system checks whether the entire quantity is available to trade at your limit price (or better) at that exact moment. If yes, the order fills completely and the trade is done. If no—meaning only part of the order can be matched—the entire order is immediately cancelled, and zero shares trade.

The key difference from a regular [limit order](/limit-order/) is immediacy and precision. A normal limit order sits on the order book waiting for sellers (if you are buying) to arrive at your price. A fill-or-kill order does not wait. It checks once, executes or cancels, and vanishes within milliseconds.

For example, suppose you submit a fill-or-kill order to buy 10,000 shares of XYZ at \$50.00. The exchange sees that only 6,000 shares are available at \$50.00 or better. Because you cannot get all 10,000, the entire order is killed—you end up with zero shares, not 6,000.

## Fill-or-kill versus immediate-or-cancel

These two order types are often confused, so the distinction matters. Both are "one-shot" orders that expire if not immediately filled, but they differ in outcome.

**Immediate-or-Cancel (IOC):** The order executes for whatever quantity is available at your limit price right now, and any remaining quantity is cancelled. You may end up with a partial fill.

**Fill-or-Kill (FOK):** The order executes only if the entire quantity is available at your limit price right now. If not, the whole order cancels and you get nothing.

A trader submitting an IOC order is saying: "I want as much as you can give me right now, up to this quantity, at this price or better." A trader submitting a FOK is saying: "I only want this trade if I can get every single share I asked for, right now, at this price or better."

Both are much less patient than an all-or-none (AON) order, which waits on the books for the entire quantity to accumulate (useful for block trades).

## Why traders use fill-or-kill orders

**Avoiding partial fills.** A trader executing a large trade may not want to own just part of their intended position. If you are hedging a derivative position or rebalancing a portfolio, a half-filled order leaves you exposed. FOK ensures you either get the full hedge or no hedge at all—no middle ground.

**Arbitrage.** In [arbitrage](/algorithmic-trading/) or statistical trading, a trader may need to simultaneously buy in one market and sell in another. If only one leg can fill completely, the trade is unprofitable. FOK on both legs ensures they all complete or none do.

**Price-sensitive trading.** If the price has moved dramatically and you are no longer confident in your limit price, you do not want an old partial fill sitting on the books. FOK cancels the whole thing and lets you reassess.

**Options and block trades.** In options and block equity trades, partial fills are particularly costly—your legs may no longer hedge, or your block negotiation depends on a specific size. FOK enforces all-or-nothing discipline.

## When fill-or-kill orders fail to execute

Fill-or-kill orders fail to execute far more often than regular limit orders, precisely because they demand 100% availability right now. During slow market hours, in illiquid securities, or after news hits and [volatility](/volatility-smile/) spikes, the depth of available liquidity at your price may dry up.

A stock that normally has 50,000 shares available at the best bid-ask might have only 10,000 at your limit price in a volatile moment. If you want all 100,000, your FOK order kills. You must then decide whether to:

- Resubmit the FOK at a slightly wider price
- Use a regular limit order and accept the risk of a partial fill
- Use an IOC order and accept whatever quantity fills

There is a trade-off between control (FOK guarantees all-or-nothing) and execution (FOK guarantees low chance of filling in a fast market).

## FOK and market impact

Large fill-or-kill orders can actually be useful for market makers because they clarify intention. A trader submitting a 100,000-share FOK is saying "I really need this size, all at once." A market maker can then decide to commit the full inventory to the trade, often at a tighter price than if the trader were nibbling away with smaller IOC orders.

However, if a trader keeps resubmitting FOK orders at increasingly aggressive prices (moving through the [bid-ask spread](/bid-ask-spread-explained/)), it signals desperation, and the market maker may widen their prices in response.

## Execution logistics

Not all trading venues support FOK, though major [stock exchanges](/stock-exchange/) and most [brokers](/broker/) do. Some options exchanges and international venues may not. Confirm that your venue supports FOK before structuring a trade around it.

When you submit a FOK order to your [broker](/broker/), it is sent to the exchange or market center where the order is immediately evaluated. The exchange checks the order book and available [reserve liquidity](/liquidity-risk/). If the full quantity is at or better than your limit price, it fills. Otherwise, it cancels. All of this happens in microseconds.

## See also

<div class="wiki-seealso">

### Closely related

- [Fill-or-Kill Order](/fill-or-kill-order/) — all-or-nothing execution within milliseconds
- [Limit Order](/limit-order/) — specify a price, wait for a match
- [Market Order](/market-order/) — instant execution at the current best price
- [Slippage in Trading](/slippage-in-trading/) — the cost of waiting versus executing immediately
- [Price Improvement in Order Execution](/price-improvement-order-execution/) — when you get a better price than the bid-ask

### Wider context

- [Stock Exchange](/stock-exchange/) — where orders are matched and filled
- [Broker](/broker/) — routes your order to the exchange or market center
- [Market Maker Trading](/market-maker-trading/) — who fills your FOK order and how they decide
- [Bid-Ask Spread Explained](/bid-ask-spread-explained/) — the gap your limit price must cross to fill
- [Algorithmic Trading](/algorithmic-trading/) — automated systems that use FOK and other order types

</div>

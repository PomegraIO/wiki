---
title: "Stop Order vs Stop-Limit Order"
description: "Why a stop order guarantees execution but not price while a stop-limit order guarantees price but not execution, with examples of failures in fast markets."
keywords:
  - stop order vs stop limit order
  - difference stop order stop limit
  - stop order execution guarantee
  - stop limit order failures
  - market order vs limit order
image: /svg/trading.svg
---

*A **stop order** becomes a [market order](/market-order/) once the trigger price is hit, guaranteeing fast execution but at an unknown price; a **stop-limit order** becomes a [limit order](/limit-order/), guaranteeing a price floor but risking non-execution if the market moves past your limit before filling.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop Order vs Stop-Limit Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">The choice between the two order types is a tradeoff: certainty of execution against certainty of price.</div>

|   |   |
|---|---|
| **Stop order** | Converts to market order at trigger price; fast execution, uncertain fill price |
| **Stop-limit order** | Converts to limit order at trigger price; execution only if price stays within limit |
| **When stop works** | Fast, liquid markets; you need out immediately, price is secondary |
| **When stop-limit works** | You have a maximum loss you can accept; willing to miss the trade if price overshoots |
| **Risk of stop** | Slippage: market price far worse than you expected when order triggers |
| **Risk of stop-limit** | No fill: price gaps past your limit and you stay in the position |
| **Fast market risk** | Stop-limit fails catastrophically if price gaps; stop always fills but potentially at terrible prices |

</aside>

## How a stop order works

A **stop order** is an instruction that waits dormant until a trigger price is reached, then immediately converts to a [market order](/market-order/). Once triggered, the order hits the market and executes at the best available price *at that moment*—not necessarily at your stop price.

Example: You own a stock at $100. You place a stop order to sell if the price falls to $90. The stock drops to $89.50. Your stop triggers instantly, converting to a market sell order. You get $89.50, or $89.40, or even $88.75—whatever the [bid price](/bid-ask-spread/) is right then. You are *guaranteed to sell*, but the exact price is a mystery.

This is why the stop order is also called a **stop loss** order—it is meant to cap losses automatically. But the loss is capped at the trigger price *only in calm markets*. In a fast-moving market, the actual fill price can be far worse.

## How a stop-limit order works

A **stop-limit order** has two prices: a stop price and a limit price. When the stop is hit, the order converts to a limit order—it will execute *only at your limit price or better*, and only if other traders are willing to trade at that price.

Example: You own a stock at $100. You place a stop-limit order with a stop price of $90 and a limit of $85. The stock falls to $89.50, triggering the stop. Now a limit sell order is active, willing to fill only at $85 or higher. If the stock bounces back to $87, your order fills at $87. If the stock crashes to $80, your order never fills—you are stuck holding the stock, having wanted to sell it at $90 (the stop), though you were willing to accept as low as $85.

## The classic fail case: gap down

Stop orders and stop-limit orders both fail catastrophically in the same scenario: a **gap down**—the stock opens or moves so fast that price jumps past your trigger before you can react or fill at any reasonable level.

**Stop order gap-down failure**: You own a biotech stock at $100 with a $90 stop-loss order, expecting a 10% protective cushion. Bad news is announced after hours. The stock opens the next morning at $65 (impossible to close at $90). Your stop triggers immediately, but your market order executes at $65—a 35% loss instead of the 10% you thought you were capping. This is called **slippage**, and it is the hidden cost of stop orders in volatile securities.

**Stop-limit order gap-down failure**: You own the same biotech stock with a $90 stop and an $85 limit. It gaps down to $65. Your stop triggers, converting the order to a limit sell at $85 or better. But the stock is trading at $65, far below your limit. Your order never fills. You are now holding a $65 stock, having set out to cap losses at $90, and unable to sell because you insisted on at least $85. You stay exposed to further downside, which defeats the whole purpose of having a stop order.

## Why each order exists

**Stop orders** are useful when you prioritize *getting out of a position* over the exact price. They are common for:
- Panic exits: the market is crashing and you just need to be gone
- Liquid stocks: large-cap, high-volume securities where slippage is usually small
- Traders who monitor actively: if you watch the stock and see your order is about to trigger at a bad price, you can cancel

**Stop-limit orders** are useful when you have a *price floor* you will not breach. They are common for:
- Protecting against catastrophic loss: you can afford a 5% loss but not a 20% gap-down hit
- Less liquid securities: where gaps can be wild and you need a price guarantee
- Investors who are patient: willing to miss the trade if price overshoots, knowing you can try again later

## Real-world scenarios

**Scenario 1: Earnings surprise**

You hold a stock at $100. The company reports earnings after hours, missing expectations. You place a stop-loss at $90 to protect against a 10% overnight drop. The stock opens down 2%, then rallies back to $99 before falling again. Your stop is never triggered—the market orders to buy push it back up. This is fine; stop orders only trigger on an actual breach of the stop price.

Now imagine instead the company had reported *much worse*. The stock opens at $75. Your $90 stop triggers immediately, and your market order executes at $75. You wanted to limit losses to $90, but you got $75 instead. This is slippage.

**Scenario 2: Sudden bad news (gap down)**

You own a stock at $100 with a $90 stop-limit (stop at $90, limit at $85). A scandal breaks: the CEO is indicted. The stock gaps down to $60 at the open. Your stop triggers, but your limit order hangs at $85, unfilled. The stock falls to $50 by afternoon. You wanted to be out, but you are trapped, holding a $50 position after setting a $90 stop.

Had you used a simple stop order instead (no limit), your market order would have filled at $60, a much less painful outcome than $50. The limit protected you from one risk (selling at $60 when you wanted $85) but exposed you to a worse risk (not selling at all, and watching it fall to $50).

**Scenario 3: Illiquid stock with no news**

You hold a small-cap stock at $50. You set a $40 stop-limit (stop at $40, limit at $35) because you know the stock is illiquid and can gap. Nothing happens for weeks. Then, a gradual drift: the stock falls to $41. Your stop triggers. A limit order is now active, willing to sell at $35 or better. The stock continues to drift slowly down: $39, $38, $37, $36. Finally, at $35 it hits your limit and executes. You got out at $35, within your protected range, without slippage. The stop-limit worked.

Had you used a simple stop at $40, it would have triggered at $39, converted to a market order, and filled at $38 or so. You would have exited sooner, but at a slightly worse price. In this case, the stop-limit's willingness to wait for the limit price paid off.

## How to choose

The decision depends on what you fear more:

- **Fear slippage and gap-down risk more than missing the trade**: Use a stop-limit order. You accept the possibility that price will gap past and you will not exit. This is right for illiquid stocks, volatile securities, and traders who can live with a position staying open.
- **Fear staying in a position that is falling more than the exit price**: Use a stop order. You accept slippage in fast markets but guarantee you will exit. This is right for liquid stocks, panic scenarios, and traders who prioritize liquidity over price.

A compromise exists: some traders use a plain stop order in liquid markets and switch to a stop-limit order when volatility spikes or the stock becomes illiquid. Others use a wide limit on their stop-limit orders—a $100 stock with a $90 stop but a $60 limit—accepting a wider range of prices but still capping catastrophic slippage.

## Broker and market mechanics

Stop orders are typically not visible on the order book—they are held in the broker's system and only sent to market once triggered. This is why they are sometimes called **off-book** orders. During extreme volatility or system overload, brokers can face delays turning stops into market orders, and fills can be worse than expected. Stop-limit orders, by contrast, once triggered, sit on the order book as a limit order and compete with other orders.

Neither stop nor stop-limit orders are filled on a guaranteed basis in all markets (e.g., options, futures, OTC derivatives). Brokers will reserve the right to reject or cancel a stop or stop-limit order under extreme conditions, and are not required to fill at the trigger price (in the case of a stop) or at the limit price (in the case of a stop-limit).

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — buy or sell immediately at any available price
- [Limit Order](/limit-order/) — buy or sell only at your specified price or better
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between buy and sell prices, determining slippage
- [Liquidity Risk](/liquidity-risk/) — the risk that an asset cannot be sold quickly without large price concessions
- Volatility — price swings that create gap-down risk
- Order Book — the real-time queue of buy and sell orders brokers execute against
- [Slippage](/slippage/) — the difference between expected and actual execution price

### Wider context

- Trading Strategy — order selection is part of broader tactical execution
- Risk Management — stops and limits are core risk tools
- [Algorithmic Trading](/algorithmic-trading/) — automated systems rely heavily on stop and limit orders
- [Options](/option/) — derivatives that can be used as hedges instead of stop orders

</div>

---
title: "Stop order"
description: "A stop order (or stop-loss order) is an instruction that becomes active only after the price hits a trigger level. Once triggered, it converts to a market order and executes immediately. Used to cut losses or enter positions."
keywords:
  - stop order
  - stop-loss
  - order types
  - trigger
  - execution
image: "https://picsum.photos/seed/stop-order/900/600"
---

*A **stop order** — also called a **stop-loss order** — is an instruction that lies dormant until the price of a security reaches a threshold you specify. Once that threshold is crossed, the order automatically converts into a [market order](/market-order) and executes at the next available price. It is the standard tool for automating losses or entering a position at a confirmation level.*

<div class="wiki-hatnote">

For price protection at the moment of trigger, see [stop-limit order](/stop-limit-order). For more sophisticated logic, see [one-triggers-other](/oto-order) and [one-cancels-other](/oco-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop order — key facts</div>

<img src="https://picsum.photos/seed/stop-order/900/600" alt="A price chart with a stop-loss level marked" />

<div class="wiki-infobox-caption">A stop order lies dormant until price crosses the trigger; then converts to a market order.</div>

|   |   |
|---|---|
| **What it is** | A market order triggered by price reaching a level |
| **Trigger event** | Price crosses your stop price (typically in the opposite direction) |
| **Execution after trigger** | Immediate market order; price uncertain |
| **Common use** | Stop-loss: exit if price falls; entry: buy if price rises |
| **Downside** | No price protection; can fill far from stop price in gaps or volatile markets |
| **Upside** | Simple, automatic, requires no monitoring |
| **Time in force** | Usually day or GTC ([good-til-canceled](/gtc-order)) |

</aside>

## How stop orders work: the trigger and the execution

A stop order has two components: the **stop price** and the **order size**. Once the price of the security touches (or crosses) the stop price, the order is activated — it is no longer dormant. At that moment, it becomes a [market order](/market-order) and goes straight into the order book to fill at the best available price.

**Key point:** Stop orders become market orders, not limit orders. Once triggered, you have no control over the execution price. The market order will fill at whatever the next available price is, which can be far from your stop price if the market is moving fast.

## Stop-loss: protecting against large losses

The most common use of a stop order is to limit losses. Suppose you buy a [stock](/stock) at $100, and you decide in advance that you do not want to lose more than 10% of your capital. You place a stop order to sell at $90. If the stock falls to $90, your stop is triggered, and you are automatically sold out.

The mechanics sound clean, but the execution can be ugly. If the stock falls from $100 to $90 in a single day, your stop will trigger at $90 or below — but in a fast market, you might fill at $88 or $85. If the stock gaps down on bad news (the opening price is $88 after a terrible earnings announcement), your stop trigger price of $90 is never touched; you might wake up to an opening fill at $83.

This risk is why [stop-limit orders](/stop-limit-order) exist: they add a second constraint (a limit price) to give you a floor on how bad the execution can be.

## Stop-entry: confirming a breakout

Traders also use stop orders to enter positions, not just exit them. Suppose the stock is trading at $100 and you want to buy only if it breaks above $105 — a sign of strength. You place a buy stop order at $105.10. Once the stock rises to $105.10, the stop is triggered and a market buy order executes. This is often used by [momentum traders](/swing-trading) and [momentum strategies](/algorithmic-trading).

Like all stop orders, the execution after trigger is a market order, so you might pay $105.50 instead of $105.10.

## The gap risk: stop orders in overnight gaps

Stop orders are particularly risky around market-opening gaps — when news hits overnight and the stock opens at a drastically different price. If your stop is at $90 and the stock gaps down to $80 at the open, your stop will be triggered, but you will not fill at $90; you will fill at the open price of $80 or lower.

Professional traders manage this risk by using [stop-limit orders](/stop-limit-order) instead, or by monitoring premarket prices closely and canceling stops before the open if the news is bad.

## Pre-triggered stops: what happens if price touches and rebounds

A stop order triggers on the first touch of the stop price or worse. Once triggered, it becomes a market order and executes. If the price then rebounds (e.g., a stock falls to $90, triggering your sell stop, but bounces back to $95 the next hour), you are already out — no second chance. Your order was filled.

## Stop orders across different venues

Stop orders are processed by your broker or the exchange, not in the order book itself. Your broker is watching the price, and when it touches your stop price, your broker converts your order to a market order and sends it to the exchange. This means:

- There is a small delay (milliseconds, but measurable) between the price hitting your stop and your order entering the market.
- During volatile periods, exchanges and brokers may experience delays processing thousands of triggered stops, particularly in panic sell-offs.
- If the stock gaps past your stop price without ever trading at your stop, your stop may still trigger on the first trade at the new price.

## Stop orders vs. limit orders vs. market orders

- A **[market order](/market-order)** executes now at any price.
- A **[limit order](/limit-order)** waits for your price and executes then, or never.
- A **stop order** waits for a price trigger, then becomes a market order.

## See also

<div class="wiki-seealso">

### Closely related

- [Stop-limit order](/stop-limit-order) — stop-triggered limit; adds price protection
- [Trailing stop order](/trailing-stop-order) — stop price adjusts automatically
- [Market order](/market-order) — what a stop becomes after trigger
- Order book — where the resulting market order lands

### Advanced stop variants

- [One-cancels-other](/oco-order) — two stops, one fires and cancels the other
- [One-triggers-other](/oto-order) — one stop triggers a second order
- [Bracket order](/bracket-order) — combines entry, profit target, and stop-loss

### Context

- Gap risk — overnight news can gap past your stops
- Order types — taxonomy of all order variants
- Slippage — gap between expected and actual fill price

</div>

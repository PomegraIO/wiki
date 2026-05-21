---
title: "Trailing stop order"
description: "A trailing stop order is a dynamic stop that automatically adjusts upward (for short positions) or downward (for long positions) as the price moves in your favor. It locks in gains while protecting against reversals."
keywords:
  - trailing stop
  - order types
  - stop-loss
  - dynamic
image: "/svg/trading.svg"
---

*A **trailing stop order** is a [stop order](/stop-order) with an automatic adjustment. Instead of a fixed stop price, you specify a **trailing distance** — a dollar amount or percentage. As the price moves in your favor, the stop price moves with it, maintaining a constant distance. If the price reverses, the stop is triggered. It is the standard tool for locking in profits while staying exposed to further gains.*

<div class="wiki-hatnote">

For a fixed stop price, see [stop order](/stop-order). For fine control over execution price, see [stop-limit order](/stop-limit-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trailing stop order — key facts</div>

<img src="/svg/trading.svg" alt="A price chart showing a trailing stop moving higher as price rises" />

<div class="wiki-infobox-caption">The trailing stop (red line) follows the price up but only falls when price reverses.</div>

|   |   |
|---|---|
| **What it is** | Dynamic stop that follows price in your favor |
| **Trailing amount** | Fixed dollar or percentage (e.g., $2 per share, 5%) |
| **Adjustment** | Only upward for long positions, only downward for short positions |
| **Execution** | Market order, once triggered |
| **Best for** | Momentum trades, letting winners run, automating profit-taking |
| **Worst for** | Choppy/whipsaw markets where reversals are frequent and small |
| **Risk** | Triggered prematurely by intraday volatility, locking in gains too soon |

</aside>

## How trailing stops work: following the high water mark

When you place a trailing stop, your broker tracks the highest price the security reaches (for a long position) or the lowest price (for a short position). The stop price is always set a fixed distance *below* that high (or *above* that low).

**Example (long position):**
- You buy a stock at $100.
- You place a trailing stop with a $5 trailing distance.
- Initial stop price: $95 (the $100 entry minus $5).
- Stock rises to $105; the high water mark is now $105, so the stop price rises to $100.
- Stock rises to $110; the stop price rises to $105.
- Stock falls to $106; the stop price stays at $105 (it does not fall).
- Stock falls to $104; the stop price still stays at $105.
- Stock falls to $104.99; finally the stop is triggered, and you are sold at the next available price (likely around $104.99 or lower).

The key rule: **the stop price only moves in your favor, never against it.**

## Dollar vs. percentage trailing stops

Most brokers allow you to specify the trailing distance as either a fixed dollar amount (e.g., $2 per share) or a percentage (e.g., 5%).

**Dollar-based trailing stops** are simple and fixed. If you specify a $2 trailing stop on a stock trading at $100, the stop is at $98. If the stock rises to $200, the stop rises to $198. This works well for stocks with stable price ranges but can become too tight (or too loose) if the stock moves a long distance.

**Percentage-based trailing stops** scale with price. If you specify a 5% trailing stop, and the stock rises from $100 to $200, the stop adjusts from $95 to $190 — always 5% below the high. This is often more intuitive and self-adjusting across large price moves.

## Trailing stops in choppy markets

The enemy of trailing stops is small, repeated reversals. Suppose a stock is in a trading range, bouncing between $100 and $105 repeatedly over a day. You place a 2% trailing stop and buy at $100.

- Stock rises to $105; stop moves to $102.90.
- Stock falls to $102.50; stop triggers.
- You are out at $102.50, having locked in just a $2.50 (2.5%) gain.
- The stock then bounces back to $108, and you are on the sideline.

This is called **whipsawing**: the trailing stop is too tight for the natural intraday volatility, so it exits before the real move. Professional traders in choppy markets often widen their trailing stops (5–10%) or simply use a fixed [stop order](/stop-order) at a level they have thought through carefully.

## Trailing stops for [scalpers](/scalping) and day traders

Trailing stops are popular with [day traders](/day-order) and [scalpers](/scalping) because they automate the core challenge of intraday trading: knowing when to take profits. You can set a trailing stop at market open and let it run; when the stock reverses even slightly, you are out with whatever gains the trade produced.

The risk is that a normal pullback in an uptrend will trigger the stop, and you miss the continuation of the trend.

## Trailing stops vs. profit-taking limit orders

An alternative to a trailing stop is to place a [limit order](/limit-order) at a target price (e.g., "sell at $110"). The limit order sits in the order book waiting to be hit; if the stock reaches $110, you are out. The advantage: if the stock continues to $115, you miss nothing (you are already out). The disadvantage: you have to guess the target price in advance.

A trailing stop is more dynamic: it grows with the stock, letting you stay in as long as the momentum continues. The disadvantage is the whipsaw risk.

## Trailing stops on short positions

For a short position, the logic inverts. You short a stock at $100 and place a trailing stop with a $5 trailing distance.

- Initial stop price: $105 (the $100 short price plus $5).
- Stock falls to $95; the low water mark is now $95, so the stop price falls to $100.
- Stock falls to $90; the stop price falls to $95.
- Stock rises to $94; the stop price stays at $95.
- Stock rises to $96; the stop is triggered, and you buy to cover at the next available price.

The trailing stop on a short protects against a violent rally, just as it protects a long position against a violent selloff.

## Limitations and broker support

Not all brokers support trailing stops for all securities. Most support them for stocks and large-cap ETFs, but some do not support them for [options](/option), futures, or international securities. Check your broker's documentation.

Some brokers also implement trailing stops on their servers; others require the order to be held on the exchange. Server-side trailing stops are more flexible but mean your stop price depends on your broker being online and responsive. Exchange-based trailing stops are more reliable but less flexible.

## See also

<div class="wiki-seealso">

### Closely related

- [Stop order](/stop-order) — fixed stop price
- [Stop-limit order](/stop-limit-order) — stop with price protection
- [Limit order](/limit-order) — alternative profit-taking mechanism

### Trading strategies and context

- [Scalping](/scalping) — very short-term trading; uses tight trailing stops
- [Swing trading](/swing-trading) — medium-term trading; uses wider trailing stops
- [Day trading](/day-order) — intraday trading; trailing stops are common
- [Momentum](/swing-trading) — trending markets where trailing stops excel

### Advanced orders

- [Bracket order](/bracket-order) — entry plus both take-profit and stop-loss
- [One-cancels-other](/oco-order) — two orders, one fires and cancels the other

</div>

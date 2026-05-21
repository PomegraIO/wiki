---
title: "One-cancels-other order"
description: "A one-cancels-other (OCO) order is a pair of conditional orders: if one fills, the other is automatically canceled. Used to handle two mutually exclusive scenarios (e.g., a profit target and a stop-loss)."
keywords:
  - OCO order
  - one-cancels-other
  - order types
  - conditional orders
image: "https://picsum.photos/seed/oco-order/900/600"
---

*A **one-cancels-other (OCO) order** is a pair of conditional orders linked so that if one fills, the other is automatically canceled. Typically used to handle two mutually exclusive outcomes: you place a profit-target [limit order](/limit-order) above the market and a stop-loss [stop order](/stop-order) below, then wait for one to trigger. Whichever fills first automatically cancels the other.*

<div class="wiki-hatnote">

For a single profit target plus stop as a unified order, see [bracket order](/bracket-order). For one order triggering a second, see [one-triggers-other](/oto-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">One-cancels-other order — key facts</div>

<img src="https://picsum.photos/seed/oco-order/900/600" alt="A price chart showing two conditional orders, one above and one below" />

<div class="wiki-infobox-caption">An OCO order: place two orders, one wins and the other is automatically canceled.</div>

|   |   |
|---|---|
| **What it is** | Two linked conditional orders; one fill cancels the other |
| **Common structure** | Profit target (limit) above + stop-loss (stop) below |
| **When both are active** | Right after you place the order |
| **Execution** | Whichever leg fills first; the other is canceled automatically |
| **Benefit** | Removes manual risk; you do not need to monitor the position |
| **Limitation** | Not all brokers support OCO; some charge fees for the feature |

</aside>

## How an OCO order works

Suppose you buy 100 shares of a stock at $100. You want to:
- **Take profit** if the stock rises to $105 (your upside target).
- **Cut losses** if the stock falls to $95 (your downside risk tolerance).

Instead of placing two separate orders and manually canceling one, you place an OCO order:
- **Leg 1:** Limit order to sell 100 at $105.
- **Leg 2:** Stop order to sell 100 at $95.

Both orders are now active. If the stock rises to $105, Leg 1 fills, and Leg 2 is automatically canceled. If the stock falls to $95, Leg 2 is triggered (becomes a market order) and fills, and Leg 1 is canceled. Either way, you are out, and you did not have to monitor or manually cancel anything.

## The benefit: one outcome, not two

Without an OCO order, you have to actively manage two separate orders:
- Place a limit at $105 and a stop at $95.
- Watch the market.
- If the limit fills, cancel the stop manually.
- If the stop fills, cancel the limit manually.

If you forget to cancel, you could accidentally double-exit: the limit fills at $105, but you forget to cancel the stop, and then the stock falls to $95 and the stop fills as well, short-selling 100 shares. Now you have unwanted leverage.

An OCO order removes that human risk. The moment one leg fills, the other is gone.

## Structure variations

The classic OCO is profit-target + stop-loss, but the structure is flexible:

- **Buy OCO:** Limit order to buy below market + stop order to buy above market. Used when you want to enter a position on either a pullback (limit) or a breakout (stop).
- **Sell OCO:** Limit order to sell above market + stop order to sell below market. Used to exit with profit or cut loss.
- **Both at market:** Two [market orders](/market-order), with OCO logic. Less common, but used for ultra-fast execution in fast markets.

## OCO orders vs. bracket orders

The main difference between an OCO and a [bracket order](/bracket-order):

- An **OCO** is two separate orders that you submit yourself, linked by the broker's logic. You decide where to place each leg.
- A **bracket order** is a bundle: one primary order (entry) plus two children (profit-taking limit + stop-loss). When the primary fills, the two children automatically become active.

A bracket order is more structured for a common pattern (entry, then choose exit). An OCO is more flexible for situations where you already have a position.

## Limitations and broker support

Not all brokers support OCO orders. Many online brokers (Schwab, Fidelity, Interactive Brokers) do; some discount brokers do not. Those that do support OCO sometimes charge a small fee (a few cents per order).

When OCO is unavailable, a common workaround is to use a [bracket order](/bracket-order) (if the broker supports that) or to manually submit the two orders and set phone reminders to cancel the loser.

## OCO orders and partial fills

If your profit-target limit order partially fills (e.g., 60 shares out of 100 fill at $105), does the stop order cancel? This depends on your broker's implementation:

- Some brokers cancel the entire OCO if *any* leg partially fills.
- Others keep both legs active, with the stop quantity adjusted to match the remaining position.

Read your broker's documentation carefully. The last thing you want is a nasty surprise: you intended to exit your entire position, but only half of it filled, and the other half is now unprotected.

## Practical use cases

**Swing trading.** You buy a stock expecting a 5% move, but you do not want to lose more than 2%. You place an OCO: profit target at +5%, stop at -2%. Whichever comes first wins.

**Mean reversion.** You are betting a stock falls from $100 to $95, but you are wrong about the direction. You place an OCO to cover short: buy limit at $95 (if you are right) or stop at $105 (if the trend is too strong). One of them will eventually fill.

**Overnight or vacation.** You are holding a position but will be away from a screen. Instead of worrying, place an OCO: profit at your upside target, stop at your loss tolerance. You are automatically exited, no monitoring required.

## See also

<div class="wiki-seealso">

### Closely related

- [Bracket order](/bracket-order) — entry plus take-profit and stop as one bundle
- [One-triggers-other](/oto-order) — one order triggers a second, not cancels
- [Stop order](/stop-order) — the stop-loss leg of a typical OCO
- [Limit order](/limit-order) — the profit-taking leg of a typical OCO

### Order types and variants

- [Stop-limit order](/stop-limit-order) — stop plus price protection
- [Trailing stop order](/trailing-stop-order) — dynamic stop that follows price
- [Market order](/market-order) — instant execution at any price

### Context and strategy

- Position management — when to exit, when to hold
- Risk management — defining upside and downside in advance
- [Swing trading](/swing-trading) — strategy commonly using OCO orders

</div>

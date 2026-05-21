---
title: "Limit order"
description: "A limit order is an instruction to buy or sell a security, but only at a price you specify or better. Your order sits in the queue waiting for the market to reach that price, sacrificing speed for price certainty."
keywords:
  - limit order
  - order types
  - price protection
  - execution
image: "/svg/trading.svg"
---

*A **limit order** is an instruction to buy or sell a security, but only if the price reaches a threshold you set in advance. If you are willing to buy a stock at $50 or less, you place a buy limit order at $50; it will sit in the order book until the price drops to that level (or better) and your order matches a seller, or until you cancel it. The price is certain; execution is not.*

<div class="wiki-hatnote">

For immediate execution at any price, see [market order](/market-order/). For automatic sell orders tied to a drop in price, see [stop order](/stop-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit order — key facts</div>

<img src="/svg/trading.svg" alt="An order book showing limit orders at different price tiers" />

<div class="wiki-infobox-caption">Limit orders form the foundation of the order book, queued and waiting for price thresholds to be hit.</div>

|   |   |
|---|---|
| **What it is** | Trade only at your specified price or better |
| **Execution certainty** | No guarantee; depends on price reaching your limit |
| **Speed** | Potentially indefinite wait |
| **Price certainty** | Complete (your fill is always ≤ your limit for buys, ≥ your limit for sells) |
| **Cost** | Zero until execution; no cost if order never fills |
| **Best for** | Patient traders, defined entry/exit prices, size traders in thin markets |
| **Worst for** | Urgent exits, fear of missing the trade entirely |
| **Time in force** | Day, [GTC](/gtc-order/), or [GTD](/gtd-order/) (see variants) |

</aside>

## The order book and price-time priority

Limit orders are the foundation of the order book. When you place a limit order, it goes into a queue alongside every other limit order at that price level. On most U.S. stock exchanges, order priority is price-time priority: within a price level, the first order placed gets first chance to match against incoming trades.

If you place a buy limit order at $50 at 10:00 a.m., and the market price drifts down to $50 at 11:30 a.m., your order will fill — but only if there are sellers at $50 and your order is near the front of the queue at that price. The smaller your size, and the more recent your order, the further back you are.

## Buy limit vs. sell limit

A **buy limit order** is an upper bound on price. You will buy at your limit or *lower*. If you place a buy limit at $50, you will fill if the market falls to $50, $49, or $48, but not if it stays at $51.

A **sell limit order** is a lower bound on price. You will sell at your limit or *higher*. If you place a sell limit at $50, you will fill if the market rises to $50, $51, or $52, but not if it stays at $49.

This can be confusing until you remember the asymmetry: when buying, you want the price to go *down*; when selling, you want it to go *up*. A limit order is patient capital waiting for the market to move in your direction.

## When limit orders work well

**Routine trading.** If you are willing to hold a stock and wait for a better entry price, or willing to wait for a modest rally to exit, limit orders are efficient. They cost nothing to place and nothing to cancel, and they sit quietly in the background waiting for the market to come to you.

**Block trading.** Institutional traders placing large orders often use limit orders (combined with [algorithmic execution](/algorithmic-trading/)) rather than market orders. A limit order at or near the current market price will usually fill gradually as other traders hit it, and you avoid the slippage of dumping a huge market order into a thin order book.

**Picking exact price levels.** Some traders use limit orders as a way to enforce discipline — forcing themselves to buy only at prices they have committed to in advance, rather than chasing a rising market.

## Risks of limit orders

**Missed execution.** The cardinal risk of a limit order is that the market never reaches your price. You are trying to buy at $50, but the stock rallies to $55 and never looks back. You are left holding cash that you wanted deployed.

**Partial fills.** Your limit order may fill only partway. You place an order to buy 10,000 shares at $50; 3,000 fill at $50.00, 4,000 at $49.99, and 3,000 never fill because the price bounces back up. You are left with a position you did not fully plan for.

**Stale quotes.** In fast markets, by the time your limit order reaches your price, the entire context may have changed. You set a buy limit at $50 expecting calm market; at 10:00 a.m. a profit warning is announced and the stock does touch $50 — but only in a panicked selloff. Your fill price is correct, but the trade thesis is now broken.

## Limit order variants

Most brokers and exchanges support variations:

- **Immediate-or-cancel (IOC):** A limit order that fills instantly at your price, or cancels. Used when you want price protection but also want to avoid a long wait. See [immediate-or-cancel](/immediate-or-cancel/).
- **All-or-none (AON):** Your entire size fills at your price, or none of it fills. See [all-or-none](/all-or-none/).
- **Fill-or-kill (FOK):** Fills now at your price, or the order dies. See [fill-or-kill](/fill-or-kill/).

## Limit orders vs. market orders: when to use each

Use a **market order** if you need to exit *now* and the spread is acceptable. Use a **limit order** if you have time and want to avoid slippage. Professional traders often use a hybrid: place a market order for the first 50% of the trade (securing the exit) and then limit orders for the rest (trying to improve price).

## See also

<div class="wiki-seealso">

### Closely related

- [Market order](/market-order/) — instant execution, any price
- [Stop order](/stop-order/) — automatic order triggered by price
- [Stop-limit order](/stop-limit-order/) — stop-triggered limit
- Order book — where limit orders live
- Price-time priority — why first-in wins

### Order types and variants

- [Immediate-or-cancel](/immediate-or-cancel/) — limit order that expires if not filled now
- [All-or-none](/all-or-none/) — your entire size, or nothing
- [Fill-or-kill](/fill-or-kill/) — all now, or nothing
- IOC order — synonym for immediate-or-cancel
- [GTC order](/gtc-order/) — limit order that sits for months

### Execution and strategy

- [Smart order router](/smart-order-router/) — routes limit orders across venues
- [Algorithmic trading](/algorithmic-trading/) — breaks large limit orders into smaller pieces
- Bid-ask spread — the gap between best buy and sell prices

</div>

---
title: "Stop-limit order"
description: "A stop-limit order combines a stop (trigger) with a limit (price constraint). Once the price hits your stop level, the order becomes a limit order, not a market order. This protects you from wild execution prices but introduces the risk of no fill."
keywords:
  - stop-limit order
  - order types
  - price protection
  - conditional order
image: "/svg/trading.svg"
---

*A **stop-limit order** is an instruction with two price thresholds: a **stop price** that triggers the order, and a **limit price** that constrains the execution. Once the stop price is crossed, the order becomes a [limit order](/limit-order/) at your specified limit price, not a [market order](/market-order/). This shields you from catastrophic fills but introduces the risk that the order never fills at all.*

<div class="wiki-hatnote">

For a simple stop that becomes a market order, see [stop order](/stop-order/). For automatic adjustments, see [trailing stop order](/trailing-stop-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop-limit order — key facts</div>

<img src="/svg/trading.svg" alt="A price chart showing stop and limit prices on a stop-limit order" />

<div class="wiki-infobox-caption">Two thresholds: the stop price triggers the order; the limit price sets the execution bound.</div>

|   |   |
|---|---|
| **What it is** | Stop-triggered limit order with two price parameters |
| **Stop price** | Trigger level (order dormant until price crosses this) |
| **Limit price** | Execution constraint (order behaves as a limit order once triggered) |
| **Execution certainty** | Not guaranteed; depends on price staying within limit after trigger |
| **Downside** | Can miss the move; triggered but unfilled if price moves past limit |
| **Upside** | Price protection; you control the worst fill price |
| **Best for** | Stop-loss orders where you want price protection, entries with limits |

</aside>

## The two-phase execution: trigger, then limit

A stop-limit order has two distinct phases:

1. **Phase 1: Dormant.** The order waits for the stop price to be crossed. Until that happens, nothing occurs.
2. **Phase 2: Active limit order.** Once the stop price is touched, the order becomes a [limit order](/limit-order/) at your specified limit price and enters the order book. It behaves exactly like a normal limit order from that point forward.

This is the key difference from a [stop order](/stop-order/): a regular stop order triggers and becomes a [market order](/market-order/) (executes at any price). A stop-limit order triggers and becomes a limit order (executes only at your limit price or better).

## Example: the classic stop-loss scenario

You buy a stock at $100. You want to limit losses to $10, so you place a stop-limit order with stop at $90 and limit at $90. If the stock falls to $90:
- The stop is triggered; your dormant order wakes up.
- It becomes a limit order to sell at $90 or better.
- If there are sellers lined up at $90 or below, you fill.
- If the price is moving down fast (now at $85), you will not fill at $90 — your limit order sits in the book at $90, hoping for the price to bounce back.

This is safer than a [stop order](/stop-order/), where you would be sold at $85 or whatever the opening price is. You have a floor ($90 is your limit). But you also have the risk of not executing, leaving you with a position you wanted to exit.

## Stop-limit vs. stop: the fundamental trade-off

| Feature | Stop order | Stop-limit order |
|---|---|---|
| **Trigger** | Yes | Yes (same) |
| **After trigger** | Market order (executes at any price) | Limit order (executes at limit price or better) |
| **Worst fill** | Potentially very far from stop | Capped at limit price (upside for you) |
| **Risk of no fill** | Low (market orders usually fill) | High (limit orders may not fill) |
| **Typical use** | Stop-losses where execution certainty > price certainty | Stop-losses where price certainty > execution certainty |

## Practical scenarios

**Scenario 1: Overnight gap down.** Stock at $100; you place a stop-limit at $90 stop, $90 limit. Overnight, a profit warning hits; stock opens at $80.
- Regular stop order: You are sold at $80 (or thereabouts) automatically.
- Stop-limit order: Stop is triggered (because $80 < $90), order enters book as limit at $90. Since the price is now $80, your limit order will not fill unless the stock bounces back above $90. You are still holding.

**Scenario 2: Gradual decline.** Stock drifts from $100 down to $90 over the course of a week.
- Regular stop order: You are sold at $90 or slightly below.
- Stop-limit order: Stop triggers at $90, order becomes limit at $90, you fill at $90 (or slightly better if the market is supportive).

Both orders work similarly in a gradual move, but differ dramatically in a gap.

## Time in force and stop-limit orders

Stop-limit orders can be [day orders](/day-order/), [GTC](/gtc-order/), or [GTD](/gtd-order/). Once the stop is triggered and the order becomes a limit order, the time-in-force rule starts. If it is a day order, the limit order expires at market close if not filled.

This creates a subtle trap: your stop-limit order can sit dormant for weeks (waiting for the trigger) and then expire as a limit order the moment it triggers (because it is a day order). Many traders forget to set the time-in-force to GTC and end up unprotected.

## When to use stop-limit orders

**Use stop-limit for:**
- Stop-loss orders where the price you are willing to accept at execution is nearly the same as your stop price (e.g., stop at $90, limit at $89.50).
- Entries where you want both a confirmation (the stop) and price protection (the limit).
- Any scenario where a catastrophic fill is unacceptable.

**Avoid stop-limit for:**
- Fast, volatile markets where gaps are common and you absolutely need to exit.
- Situations where no fill is worse than a bad fill.

## See also

<div class="wiki-seealso">

### Closely related

- [Stop order](/stop-order/) — trigger becomes market order
- [Limit order](/limit-order/) — what the order becomes after trigger
- [Trailing stop order](/trailing-stop-order/) — dynamic stop price
- [Market order](/market-order/) — instant execution at any price

### Advanced combinations

- [Bracket order](/bracket-order/) — entry plus stop and profit-taking limit
- [One-cancels-other](/oco-order/) — two stops, one fires and cancels the other
- [One-triggers-other](/oto-order/) — one stop triggers a second order

### Context

- Order types — taxonomy of all variants
- Order book — where the limit phase executes
- Time-in-force — how long the order lasts

</div>

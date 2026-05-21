---
title: "One-triggers-other order"
description: "A one-triggers-other (OTO) order is a conditional pair: one order sits dormant, and when a trigger order fills, it automatically places a second order. Used to automate multi-step trading logic."
keywords:
  - OTO order
  - one-triggers-other
  - order types
  - conditional orders
image: "/svg/trading.svg"
---

*A **one-triggers-other (OTO) order** is a pair of conditional orders where the second order is dormant until the first order fills. Once the trigger order executes, the second order is automatically placed. Used to automate sequences: enter a position, then automatically place exit orders.*

<div class="wiki-hatnote">

For two orders where one fill cancels the other, see [one-cancels-other](/oco-order). For a simpler profit/stop pair, see [bracket order](/bracket-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">One-triggers-other order — key facts</div>

<img src="/svg/trading.svg" alt="A chart showing order sequence: trigger order, then second order activates" />

<div class="wiki-infobox-caption">OTO: first order fills, then second order is automatically placed.</div>

|   |   |
|---|---|
| **What it is** | Two linked orders; second is placed only after first fills |
| **Typical use** | Entry order, then auto-place exit orders |
| **Common structure** | Buy (or short), then place take-profit limit + stop-loss |
| **Benefit** | Automates multi-step entry and exit; no manual intervention needed |
| **Limitation** | Second order is placed *after* the first fills (small delay) |

</aside>

## How an OTO order works

Suppose you want to buy a stock at $100 (via a limit order) and immediately set up a profit target and stop-loss. With an OTO order:

1. **Trigger order:** Limit order to buy 100 shares at $100.
2. **Secondary order:** OCO to sell 100 shares (profit at $105, stop at $95).

You submit the OTO. The system places the buy limit order at $100, but the sell OCO is dormant. When (if) the buy limit fills, the sell OCO is automatically placed.

This means: you are not exposed during the time between your entry and exit orders being placed. The moment your entry fills, your exit orders are placed.

## OTO vs. other order types

| Order type | Use | Timing |
|---|---|---|
| **OCO** | Two mutually exclusive orders | Both active immediately |
| **OTO** | Sequential orders; second depends on first | Second placed after first fills |
| **Bracket order** | Entry + exits as a bundle | Entry primary; exits children, active after entry fills |

A [bracket order](/bracket-order) is similar to an OTO (entry, then exits) but is often simpler and has a tighter linkage at the exchange level.

## Typical OTO workflows

**Setup 1: Buy with auto-exit orders**
- Trigger: Limit order to buy 100 at $100.
- Secondary: OCO to sell 100 (limit $105, stop $95).
- Execution: You buy at $100; immediately your profit/stop are placed.

**Setup 2: Short with auto-cover**
- Trigger: Limit order to short 100 at $100.
- Secondary: OCO to cover 100 (limit $95, stop $105).
- Execution: You short at $100; immediately your cover orders are placed.

**Setup 3: Multiple legs**
- Trigger: Buy 100 at $100.
- Secondary: Two separate orders — sell 50 at $102 (early take-profit) and a trailing stop on the other 50.
- Execution: You buy 100; then two separate exit orders are placed.

## Execution timing and risk

The key limitation of an OTO is that there is a small lag between the trigger order filling and the secondary order being placed. For most brokers, this is milliseconds, but:

- In a fast market during the gap between fill and placement, the stock could move significantly.
- If your broker's system is slow or overloaded, the delay could be longer.
- If your secondary order is a [market order](/market-order), it will execute at the current price, which could have moved.

For most retail traders, this delay is negligible. For high-frequency traders or scalpers, it can matter.

## OTO orders and partial fills

If your trigger order partially fills, what happens to the secondary order? Broker behavior varies:

- Some brokers place the secondary order for the full size you specified (not adjusted).
- Others place the secondary order for the quantity that actually filled.

This matters. Suppose your buy limit is for 100 shares but only 60 fill. If your secondary OCO is for 100 shares and the broker places it unadjusted, you will have 60 shares long and an order to sell 100. That is wrong.

Check your broker's OTO logic carefully, or specify the secondary order size after you know the fill size (some brokers allow percentage-based sizing).

## OTO orders vs. manual entry + exit

**Manual approach:**
1. Place buy limit at $100.
2. Wait for fill.
3. Check fill confirmation.
4. Place sell OCO for profit/stop.

**OTO approach:**
1. Set up both orders in advance.
2. Trigger order fills.
3. Exit orders placed automatically.

The OTO removes step 3 (manual action) and step 2 (monitoring). The trade-off: you set up the exit orders before you know if the entry will fill and at what price.

## Broker support

Like [OCO orders](/oco-order), OTO support varies:

- Major brokers (Schwab, Fidelity, Interactive Brokers, TD Ameritrade) support OTO.
- Discount brokers may not.
- Some brokers charge a fee per OTO.

If your broker does not support OTO, a [bracket order](/bracket-order) is usually the next-best alternative.

## See also

<div class="wiki-seealso">

### Closely related

- [One-cancels-other](/oco-order) — two mutually exclusive orders
- [Bracket order](/bracket-order) — entry plus fixed profit/stop; simpler than OTO
- [Stop order](/stop-order) — the stop-loss component
- [Limit order](/limit-order) — entry and profit-taking component

### Order types

- [Market order](/market-order) — instant execution
- [Stop-limit order](/stop-limit-order) — stop-triggered limit order
- [Trailing stop order](/trailing-stop-order) — dynamic stop

### Strategy and context

- Position management — entering and exiting
- Risk management — defining profit/loss in advance

</div>

---
title: "One-Triggers-Other Order (OTO)"
description: "An OTO order automatically submits a second order only after the first order fills. Common use: buy position, then automatically place a stop-loss or take-profit."
keywords:
  - one triggers other order
  - oto order
  - conditional order
  - stop loss
  - entry and exit
---

*A **one-triggers-other (OTO) order** links two separate orders: the primary order executes normally, and only after it fills (fully or partially) does the system automatically submit a secondary order at your specified price and quantity. The most common pattern is entering a position with the first order, then immediately placing a protective stop or profit-taking limit as the second.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OTO Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Automation that bundles entry and exit into a single order ticket.</div>

|   |   |
|---|---|
| **Primary order** | First order you place (buy or sell) |
| **Secondary order** | Submits automatically once primary fills |
| **Trigger** | Full or partial fill of the primary |
| **Common use** | Buy + stop-loss, or buy + take-profit limit |
| **Execution guarantee** | Primary order executes like normal; secondary submits if trigger fires |
| **Broker support** | Widely available on major platforms |

</aside>

## How OTO orders work

An **OTO order** is a one-way link: it says, "Execute my primary order, and if it fills, automatically submit my secondary order." You place both orders in a single ticket on your broker's platform, but they don't execute simultaneously. The primary order goes to the market and behaves like any normal limit, market, or [stop order](/stop-order/). Once it fills—whether immediately or after hours or days—the broker's system automatically enters the secondary order with the parameters you specified.

The secondary order is *not* submitted until the primary fills. If you place an OTO to buy 100 shares of Apple and then sell 100 shares at a higher price (your take-profit), the sell order doesn't appear on the market until your buy order has actually executed. This prevents the awkward situation of a sell order sitting on the market before you own the shares.

## Primary and secondary order anatomy

When setting up an OTO, you specify:

1. **Primary order details:** type (limit, market, stop, etc.), side (buy or sell), quantity, price, and [time-in-force](/day-order-vs-good-till-cancelled/) (day, GTC, etc.)
2. **Secondary order details:** type, side, quantity, price, and time-in-force

Most platforms let you choose different order types for each leg. For example:
- **Primary:** market buy for 100 shares (execute immediately at best ask)
- **Secondary:** limit sell for 100 shares at $150 (capture a 5% move)

Or:
- **Primary:** limit buy for 100 shares at $145
- **Secondary:** stop-sell for 100 shares at $140 (protective stop below entry)

## The most common pattern: entry plus protection

The classic OTO pattern is **buy on a trigger, then immediately place a stop-loss.** A trader thinks Apple will move up but wants downside protection. She places an OTO:
- **Primary:** Buy 100 shares at $145 (limit order)
- **Secondary:** Sell 100 shares at $140 (stop order)

If the stock never reaches $145, the buy never fills, so the stop is never submitted. No position, no risk. If the stock does hit $145, the buy fills, and the system immediately submits the stop-sell at $140. Now she's long 100 shares with a defined risk: if the stock falls to $140, she's out. If it rises to $150, she could manually cancel the stop or use a separate take-profit order.

This automation is far more convenient than manually placing the stop after the buy fills, which might take seconds and expose you to gap risk if the stock moves sharply between the buy and the stop placement.

## Entry with take-profit

Another common variant links entry with a **take-profit limit:**

- **Primary:** Buy 100 shares at $145 (market order, execute now)
- **Secondary:** Sell 100 shares at $150 (limit order, capture the 3.4% gain)

The market buy executes immediately, and the limit sell is submitted to the market. If the stock reaches $150, the sell fills, locking in the gain. If it never reaches $150, you stay long and can decide what to do at the close or next session.

Some traders use an OTO with a take-profit and *manually* place a separate stop-loss. The OTO handles the profit exit; the trader monitors the position for unexpected downside and cancels the order to avoid losing shares at an unlucky stop price.

## Partial fills and secondary triggering

If your primary order partially fills, the behavior depends on your broker's implementation:

- **Some brokers:** A partial fill triggers the secondary order immediately, even if not all primary shares have executed
- **Other brokers:** The secondary submits only when the primary is fully filled

Check your platform's documentation. This matters if you're buying 500 shares in a limit order that fills 100, then 200, then 200 more across minutes or hours. Do you want your stop-loss (or take-profit) submitted after the first 100 shares, or only after all 500 are bought?

Most platforms default to "submit on full fill," but some advanced platforms allow you to configure it as "submit on any fill" or "submit only on full fill."

## Cancelling one leg without cancelling the other

If your primary order fills and the secondary is submitted, can you cancel the secondary without affecting the primary? Yes—once both orders are live, they're independent. You can cancel the secondary (the stop or take-profit) at any time without affecting the filled primary position.

Conversely, if you want to cancel the entire OTO *before* the primary fills, most platforms let you cancel the OTO as a package, which cancels the primary and cancels the secondary (which hasn't been submitted yet). Check your broker's interface; some show this as "cancel OTO" while others show "cancel primary" and "cancel secondary" separately.

## OTO vs. one-cancels-other (OCO)

Do not confuse OTO with **OCO (one-cancels-other).** They're related but opposite:

- **OTO:** Primary fills → secondary submits
- **OCO:** One order fills → the other order cancels

An OCO is often used for exiting a position with two options: "Sell at $150 (take-profit) OR sell at $140 (stop-loss)—whichever hits first, the other cancels." An OTO is used for entry-then-exit automation.

Some platforms offer **bracket orders** or **one-triggers-one-cancels-other (OTOCO)** which combine the patterns: primary order enters, secondary take-profit submits, and a stop-loss also submits; if the take-profit fills, the stop cancels, and vice versa. These are elegant but available only on advanced platforms.

## Price refresh and real-time adjustments

OTO orders do not automatically adjust the secondary price if the market moves. If you place an OTO to buy at $145 and sell at $150, those prices are fixed. If the stock jumps to $148 while your buy is pending, your sell is still set to $150 (not adjusted upward). This is by design: you're not forced to chase price. The secondary order is a static instruction, not a pegged or moving order.

If you want the secondary to track price (e.g., always sell 1% above the entry), some advanced brokers allow you to specify an offset or percentage, and the secondary price updates based on the primary fill price. Example: "Buy at market, then sell at [entry price] + 2%."

## Time-in-force on each leg

The primary and secondary orders can have different [time-in-force settings](/day-order-vs-good-till-cancelled/):

- **Primary:** Day order (expire at close if not filled)
- **Secondary:** GTC (good-till-cancelled, remain open for days)

This is useful if you want to place a day order entry (trying to fill today), but if it fills, the exit should be patient and linger across multiple sessions. Conversely, you might use a GTC primary (a limit order that hunts over days) and a day secondary (exit today, or forget it).

## Execution order and same-price fills

OTO orders do not execute simultaneously. The primary executes first, and the secondary is submitted afterwards—usually within milliseconds, but there is a tiny gap. In extremely fast-moving stocks or during news events, that gap could matter: your buy could fill, and by the time the sell is submitted, the price could have moved.

This is rarely an issue in normal conditions, but it's worth knowing if you're trading illiquid or volatile securities.

## Broker support and limitations

OTO orders are widely supported on retail platforms like Fidelity, Schwab, Interactive Brokers, and TD Ameritrade. Institutional platforms (Morgan Stanley, Goldman Sachs, Bloomberg Terminal) typically offer them as well. However, some smaller or no-commission brokers may not support OTO; they might require you to place both orders manually.

Also, some brokers restrict the order types you can use as the secondary. For example, a few platforms don't allow a stop order as the secondary; they only allow limit or market orders. Verify your broker's rules before building your strategy around OTO.

## Example: a complete OTO trade

You expect Apple to bounce to $148 from current price of $145, but you want protection:

1. **Set up OTO:**
   - Primary: Buy 100 shares at $145 (limit order, day)
   - Secondary: Stop-sell 100 shares at $142 (GTC)

2. **Primary fills at 10:30 a.m.:** You now own 100 shares of Apple at $145. Your balance is debited.

3. **Secondary submits instantly:** The stop-sell order is placed. If Apple drops to $142, you'll be sold out, capping your loss at $3 per share.

4. **Later, at 2:15 p.m.:** Apple rises to $148. You decide you want to lock in profit rather than wait for the stop to trigger. You manually submit a limit sell for 100 shares at $148. If it fills, you now own 0 shares. Your stop-sell at $142 is still sitting on the order book, but it's orphaned (you own no shares to sell into it). You cancel it to clean up.

## See also

<div class="wiki-seealso">

### Closely related

- [Stop Order](/stop-order/) — often the secondary leg of an OTO
- [Limit Order](/limit-order/) — common primary or secondary order type
- [Day Order vs Good-Till-Cancelled Order](/day-order-vs-good-till-cancelled/) — time-in-force for each OTO leg
- [Iceberg Order vs Reserve Order](/iceberg-order-vs-reserve-order/) — other complex order structures

### Wider context

- Risk Management — why traders use OTO orders for protection
- Order Book — where primary and secondary orders are queued
- [Market Order](/market-order/) — execution type often used in OTO entries
- [Price Discovery](/price-discovery/) — how limit orders function as secondary OTO legs

</div>

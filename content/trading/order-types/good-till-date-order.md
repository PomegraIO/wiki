---
title: "Good Till Date Order"
description: "A time-limited order that stays active until a specified calendar date, automatically cancelling if unfilled."
keywords:
  - good till date order
  - gtd order
  - order expiration
  - conditional order
  - trading order types
image: "/svg/trading.svg"
---

*A **Good Till Date (GTD) order** is a standing instruction to a broker to buy or sell a security at a specified price, remaining active until a date chosen by the trader rather than until the end of the trading day. If the order has not filled by that date, the broker automatically cancels it.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Good Till Date Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A time-bound standing order that expires at trader discretion.</div>

|   |   |
|---|---|
| **What it is** | A [limit order](/limit-order/) or [market order](/market-order/) set to remain active for days, weeks, or months until expiration |
| **Also called** | GTD order, good-till-date order |
| **Typical duration** | Days to months, depending on broker rules and trader choice |
| **Auto-cancellation** | On the specified expiration date if unfilled |
| **Execution** | At the specified price (limit) or at market rates (if market order variant) |
| **Counterpart orders** | Good Till Cancel (no expiration), [Day Order](/day-order/) (expires at session end) |

</aside>

## Why traders use standing orders instead of daily resets

The core appeal of a GTD order is convenience and consistency. A trader might believe a stock is fairly valued only within a certain price band—say, £18 to £22—and want to buy automatically if it dips to £18, but would rather not log in every morning to reset the order. Rather than cancel and resubmit a [day order](/day-order/) repeatedly for weeks, a GTD allows a single instruction to persist quietly until either the order executes or the chosen expiration date arrives.

This is particularly useful for traders with medium-term views but irregular monitoring schedules. A professional fund manager deploying capital over a three-month allocation cycle might set GTD orders across a basket of securities, each expiring at a portfolio rebalance date. Once set, the orders need no daily maintenance; the broker handles the bookkeeping.

## The mechanics of GTD expiration

When you submit a GTD order, you specify a date on which the order expires—a Friday in two weeks, for example, or the last trading day of the month. On that date, if the order has not been fully or partially filled, the broker cancels the outstanding quantity without intervention from you. Some brokers cancel GTD orders at market open on the expiration date; others cancel at close. The exact mechanics vary by platform and security type.

Unlike a Good Till Cancel (GTC) order, which theoretically persists indefinitely, a GTD order has a hard sunset. This explicitness appeals to risk managers: you know exactly when the instruction ceases. It also guards against stale orders accidentally executing months later after corporate restructuring or other major shifts in trading dynamics.

## Limits and regulatory constraints

Most brokers impose maximum GTD durations—often 90 days, sometimes 180 days. A few allow custom expirations up to a year, but these are the exception. The constraint reflects both operational burden (tracking thousands of expiring orders) and a sensible safeguard: a limit order left unattended for two years might execute on stale assumptions.

Different exchanges and asset classes also impose their own rules. Some stock exchanges accept GTD orders natively; others require brokers to manually re-submit day orders on behalf of the trader. The [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) in the US does not mandate any particular duration, leaving it to broker discretion and market practice.

A critical detail: a GTD order generally does not survive broker system outages or unexpected halts. If your broker goes offline for extended maintenance, or if trading in your security halts, the GTD order status may be unclear. Always confirm your broker's disaster-recovery procedures.

## When GTD makes sense versus other order types

GTD is most suitable when you have a clear conviction and timeline. If you want to buy a stock only if it reaches £18, and you're willing to wait a month but not indefinitely, GTD is cleaner than a GTC order, which requires you to remember to cancel manually. It's also more deliberate than a [day order](/day-order/), which forces daily resubmission—a friction point that can lead to missed opportunities or careless errors.

For high-frequency or day traders, GTD is rarely relevant; they work within single sessions and cancel manually. For [market-on-open (MOO)](/market-on-open-order/) and [market-on-close (MOC)](/market-on-close-order/) orders, GTD expiration is less meaningful because these orders are pegged to intraday auctions and disappear if not executed immediately.

## Execution and partial fills

A GTD order behaves like any other standing order once placed. If the price moves to your [limit](/limit-order/), the order executes at the earliest available price at or better than your limit. If the order partially fills—you wanted 1,000 shares and 600 have traded—the remaining 400 shares remain on the order book until the GTD expires.

Some traders chain GTD orders: once one fills, they immediately submit another with the same expiration, effectively extending the trading window while maintaining discipline. This technique works well for scaling into a position over several weeks.

## Platform and cost differences

Most full-service brokers and many online platforms support GTD orders at no extra fee; it's part of standard order types. However, some ultra-low-cost platforms or market-maker brokers may not offer GTD functionality—they might support only day orders and GTC. Confirm this when choosing a broker if multi-week orders are part of your strategy.

## See also

<div class="wiki-seealso">

### Closely related

- Good Till Cancel Order — a standing order with no specified expiration date
- [Day Order](/day-order/) — an order that expires automatically at the end of the trading session
- [Limit Order](/limit-order/) — a GTD order is usually a limit order held for a longer window
- [Market Order](/market-order/) — can also be structured as GTD in some broker platforms
- Order Book — where GTD orders rest between submission and execution or expiration
- [Immediate or Cancel Order](/immediate-or-cancel-order/) — a time-sensitive order with the opposite logic
- [Market on Open Order](/market-on-open-order/) — another time-specific order variant
- [Market on Close Order](/market-on-close-order/) — pegged to session close rather than a future date

### Wider context

- [Market Maker Trading](/market-maker-trading/) — how orders are filled at exchanges
- [Stock Exchange](/stock-exchange/) — where orders are routed and matched
- [Price Discovery](/price-discovery/) — how standing orders contribute to market price formation
- [Bid-Ask Spread](/bid-ask-spread/) — why your GTD limit might or might not fill at your target price

</div>

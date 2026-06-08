---
title: "One Cancels Other Order"
description: "A paired order where execution of either leg automatically cancels the remaining leg, useful for conditional trading strategies."
keywords:
  - one cancels other
  - OCO order
  - paired orders
  - conditional execution
  - trading strategy
image: "/svg/trading.svg"
---

*A **one cancels other order** (OCO) is a pair of linked instructions where filling one leg immediately cancels the other. If the trader buys on the first leg, the sell order evaporates; if the sell order fills first, the buy is abandoned. This structure lets traders express conditional logic—"I want this position if price rises, but exit if it falls"—without manual intervention.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">One Cancels Other Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark representing order mechanics and execution." />

<div class="wiki-infobox-caption">A two-leg mechanism for hands-off conditional execution.</div>

|   |   |
|---|---|
| **What it is** | A pair of orders where execution of one leg automatically cancels the other |
| **Structure** | Two separate orders linked by a cancellation rule |
| **Typical pairing** | Buy order paired with a sell order at a different price |
| **Outcome** | Only one leg ever executes; the other is voided |
| **Typical use** | Profit targets and stop-losses; capturing a move in either direction |
| **Risk** | Neither leg may execute; timing risk if only one fills |

</aside>

## The conditional trading problem

A trader often faces a simple decision: "I expect the stock to move significantly, but I'm unsure which direction." Or: "I want to capture gains if the stock rises but protect against losses if it falls." Submitting separate buy and sell orders leaves the trader vulnerable to bad outcomes—both orders might fill, or neither might, or the wrong one might fill at an adverse time. The **one cancels other order** automates the solution: submit a buy order at a higher price and a sell order at a lower price (or any combination), and whichever executes first kills the other.

## Two common structures

The most frequent configuration is a **buy-plus-protective-sell**: a trader places a buy order at, say, $50, and simultaneously a sell order at $45. If the stock rallies and the buy fills at $50, the sell order vanishes—the trader now owns the position. If the stock falls and the sell fills at $45, the buy order is cancelled—the trader avoids the higher purchase price and has taken a small profit or minimized a loss. This pair lets the trader participate in a potential upside move while capping downside by pre-setting an exit.

Conversely, a trader who is short might place a sell order (to initiate the short) at $60 and a buy order (to close it) at $65, creating a bracket that protects against unlimited upside if the stock rallies hard.

## Execution certainty and partial fills

An important distinction: most OCO implementations on modern exchanges will execute the two legs separately, filling at whatever price-level each encounters first. When the first leg fills, the exchange immediately cancels the other without attempting a partial fill. Some order management systems support "iceberg" or "reserve" variants of OCO, where only a visible quantity is displayed and hidden reserve quantity is refreshed—but the basic OCO cancels the entire opposing leg on first execution.

## Manual discipline vs. automation

Before OCO orders were widely available, traders had to monitor positions manually and cancel standing orders by hand. This introduced operational risk: a trader could forget to cancel the opposite leg, resulting in a whipsaw (both orders filling) or missing a closing opportunity. An OCO removes the manual step and ensures only one leg ever executes. For retail traders managing a handful of positions or institutions running systematic strategies, OCO provides the execution certainty that markets demand.

## Comparison to other paired structures

The **[one cancels other order](/one-cancels-other-order/)** differs from an "if-then" conditional (where the second order is only placed if the first executes). OCO pre-commits both legs to the market simultaneously; if-then orders require the trader to actively place the second order after the first fills. OCO also differs from a **[limit on close order](/limit-on-close-order/)** or **[limit on open order](/limit-on-open-order/)**, which are single orders tied to specific auction times. An OCO is active throughout the trading day, ready to execute whenever either leg's price is reached.

## Risk and limitation: neither may execute

The primary risk of an OCO is that neither leg executes if the stock moves sideways or trades between the two order levels without touching either. A trader places a buy at $50 and a sell at $45, hoping for a decisive move, but the stock trades in the $47–$48 range all day. Both orders expire unfilled at the close, leaving the trader without a position despite expecting volatility. This is sometimes called "the worst case"—the trader missed both the rally (no buy fill) and the decline (no sell fill).

## Availability and exchange rules

Most major equity and options exchanges support OCO orders, though the mechanics vary. Some exchanges implement OCO at the broker level, combining two separate [limit orders](/limit-order/) and applying the cancellation rule. Others, like futures exchanges, build OCO into the order book itself. Retail brokers typically support OCO on stocks and ETFs, though some constraints apply (e.g., no OCO on after-hours trading, or OCO expires at end of day rather than persisting to the next day).

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — single conditional order that fills at a specified price
- [Market Order](/market-order/) — unconditional order executed immediately at market price
- Stop-Loss Order — protective order triggered when price falls below a level
- [Limit on Close Order](/limit-on-close-order/) — execution-timing condition tied to the close
- [Limit on Open Order](/limit-on-open-order/) — execution-timing condition tied to the opening
- [Reserve Order](/reserve-order/) — hidden quantity mechanism compatible with some OCO structures

### Wider context

- [Order Types](/order-types/) — taxonomy of trading instructions
- [Broker](/broker/) — intermediary that executes and manages OCO orders
- [Price Discovery](/price-discovery/) — how both legs interact with the market
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulates order practices
- [Algorithmic Trading](/algorithmic-trading/) — automated strategies that may use OCO structures

</div>

---
title: "Day Order vs Good-Till-Cancelled Order"
description: "Day orders expire at market close; GTC orders persist until filled or manually cancelled. Understand expiry rules, risks, and when to use each."
keywords:
  - day order
  - good till cancelled order
  - gtc order
  - time in force
  - order expiry
  - trading orders
---

*A **day order** expires automatically at the close of the trading session; a **good-till-cancelled (GTC) order** remains open indefinitely until filled, cancelled, or the broker enforces an expiry window. The choice depends on whether you're acting within hours or willing to let a resting order hunt for price over weeks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Day vs GTC — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two different rhythms: immediate urgency versus patient execution.</div>

|   |   |
|---|---|
| **Day order** | Expires at market close; default for most brokers |
| **GTC order** | Remains open until filled, cancelled, or broker's max window |
| **Market close** | Day orders are automatically withdrawn; GTC orders persist |
| **Price reset risk** | GTC order stays live across gaps, dividends, splits |
| **Typical window** | GTC usually enforced for 30–90 days before auto-cancel |
| **Best for** | Day orders: same-session trading; GTC: limit orders over multiple sessions |

</aside>

## How day orders work

A **day order** is the default time-in-force setting on most retail trading platforms. You place the order, and it lives until the regular market close (typically 4 p.m. Eastern for U.S. equities). If it doesn't fill by 4 p.m., the broker automatically cancels it. Any unfilled quantity simply evaporates; you do not have to manually delete it.

This applies equally to limit orders and stop orders. A day order limit to buy 100 shares of Apple at $145 will be cancelled at market close if the price never touched $145. A day order stop-sell at $180 will expire at the close if the stock never reached that trigger price.

The advantage is simplicity: you know that every morning, your order slate is clean. You won't wake up the next day to find a stale limit order still hunting for a price that made sense yesterday but not today.

## How good-till-cancelled orders persist

A **GTC order** does not expire at market close. It rolls forward into the next trading session, and the next, remaining live and able to fill until one of three things happens:

1. **The order fills** (fully or partially, depending on whether you accept partial fills)
2. **You manually cancel it**
3. **Your broker's GTC window expires** (typically 30, 60, or 90 days, varying by firm)

Because GTC orders span multiple sessions, they can catch price moves that happen days or weeks after you place them. A GTC limit order to buy at $145 placed on Monday might fill on Wednesday when Apple dips. This patience is the core appeal: you set the price and wait, rather than re-submitting the same order each day.

## Risks specific to GTC orders

Leaving an order open for weeks introduces several hazards that day orders avoid.

**Corporate actions:** If the stock pays a dividend or splits, your resting GTC order does not automatically adjust. A GTC limit order to buy 100 shares at $145 will still trigger at $145 even if the company splits 2-for-1, leaving you vulnerable to buying 200 shares (or double the intended cost) in the post-split context. It is wise to review GTC orders before ex-dividend dates and splits.

**Forgotten orders:** A GTC order left open and forgotten can suddenly fill in volatile intraday moves. Traders have reported opening a position via a GTC buy order that sat for weeks, only to have it execute during an overnight gap or pre-market spike when they weren't monitoring. The capital is then committed without your attention.

**Gap risk:** GTC orders do not account for overnight or weekend gaps. Place a GTC limit to sell Apple at $200 on Friday; if the stock gaps above $200 at Monday open—you'll sell at $200, missing the move upward. Conversely, a GTC buy order at $150 could fill on a gap down, committing capital you intended to deploy more selectively.

**Stale price anchors:** Over time, the price you picked—$145 to buy, $200 to sell—may stop reflecting current value. Market conditions shift. That limit order from six weeks ago might have made sense in a different rate regime or earnings calendar, but still sits open, poised to fill in a changed context.

## Typical broker GTC windows

Most brokers do not let GTC orders run forever. They auto-cancel after:

- **30 days** (common for many retail platforms including some Fidelity, Schwab, and Interactive Brokers accounts)
- **60 days** (some accounts)
- **90 days** (others)
- **Until end of quarter** (less common; some brokers use a calendar-driven reset)

Check your broker's documentation. Some firms offer indefinite GTC as a premium feature or on certain account types. You should know the window for your account and set calendar reminders to cancel or renew long-standing GTC orders before auto-expiry.

## When to use day orders

Choose day orders when:

- You're trading intraday or within the same session
- The trade is responsive to immediate conditions (a news event, technical bounce, or opening gap you want to exploit by the close)
- You want a clean slate each morning
- You prefer not to monitor positions left open overnight

Most active traders and day traders default to day orders for this reason: the strategy requires rapid turnover, and stale day orders can interfere with the next session's plan.

## When to use GTC orders

Choose GTC orders when:

- You're targeting a specific price and willing to wait days or weeks for it
- You want to "set and forget" a passive entry or exit point
- You're placing a tight stop-loss and don't want to re-enter it each day
- You're scaling in or out of a position over a longer horizon

A swing trader might place a GTC buy at $145 on Monday with the plan to hold if filled, then place a corresponding GTC sell at $160; if the stock reaches $145, the entry fills, and the trader is then free to manage the exit separately. The GTC setup avoids re-entry friction.

## Execution and order refreshes

Neither day orders nor GTC orders automatically refresh price. Once placed, they sit at their specified level. If your broker offers the ability to "refresh" or "re-enter" an order (some do, to reset the GTC countdown clock), you must request it manually or via API; most brokers do not auto-refresh.

Some platforms do allow you to convert a day order to GTC or vice versa without cancelling and re-entering, saving on commissions or re-entry friction. Check your platform's capabilities.

## Partial fills and remainder handling

If a GTC order partially fills—you place a GTC buy for 1,000 shares, and 600 fill on day one—the remaining 400 shares remain on the order book as a GTC, still hunting for the specified price. Again, it will persist until the broker's GTC window expires, you cancel it, or it fills in full.

Day orders that partially fill behave the same way until the market close, at which point the unfilled remainder is cancelled regardless of size.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — price-specific order type often paired with day or GTC time-in-force
- [Stop Order](/stop-order/) — execution trigger that also respects day vs. GTC rules
- [Market Order](/market-order/) — immediate execution unaffected by time-in-force settings
- [Pegged Order Types Compared](/pegged-order-types-compared/) — price-anchored orders and their refresh behavior
- [Iceberg Order vs Reserve Order](/iceberg-order-vs-reserve-order/) — hidden-quantity variants often combined with GTC

### Wider context

- [Stock Market](/stock-market/) — exchange where orders are matched
- [Market Maker Trading](/market-maker-trading/) — counterparty that may fill your resting orders
- [Bid-Ask Spread](/bid-ask-spread/) — price levels where GTC limit orders often sit
- [Price Discovery](/price-discovery/) — how limit orders contribute to fair value

</div>

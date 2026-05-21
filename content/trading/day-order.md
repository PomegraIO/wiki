---
title: "Day order"
description: "A day order is any order that expires at the end of the trading day if not filled. It is the default time-in-force for most brokers, ensuring orders do not linger after market close."
keywords:
  - day order
  - time-in-force
  - market close
  - order expiration
image: "/svg/trading.svg"
---

*A **day order** is an order that lives only for a single trading day. If it does not fill by market close, it is automatically canceled. This is the default time-in-force for most brokers — when you place a [limit order](/limit-order) and do not specify "good-til-canceled," you are placing a day order.*

<div class="wiki-hatnote">

For orders that survive across multiple days, see [GTC order](/gtc-order) and [GTD order](/gtd-order). For same-day filling only, see [fill-or-kill](/fill-or-kill).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Day order — key facts</div>

<img src="/svg/trading.svg" alt="A clock at market close showing an order expiring" />

<div class="wiki-infobox-caption">Day orders expire at market close; you must resubmit them the next day if they do not fill.</div>

|   |   |
|---|---|
| **What it is** | An order valid only for the current trading day |
| **Lifespan** | From submission until 4:00 PM ET (U.S. stock market close) |
| **Expiration** | Automatic cancellation at market close if unfilled |
| **Resubmit** | Must be resubmitted manually each day |
| **Default** | Yes, most brokers use this as the default |
| **Best for** | Intraday traders, day traders, short-term speculation |
| **Worst for** | Long-term investors wanting a persistent order |

</aside>

## How day orders work

A day order is active from the moment you place it until the closing bell of the [stock market](/stock-market). If it fills during the day, you are done. If not, it dies at 4:00 PM ET (or the local market close for international markets).

**Example:** You place a day limit order to buy 100 shares at $50 at 10:00 a.m. The stock closes at $49.99 by 3:59 PM, but your order never fills. At 4:00 PM, your order is automatically canceled. You do not own any shares, and you do not own an active order. The next day, if you still want to buy at $50, you must place a new day order.

## Advantages of day orders

**Simple and automatic.** You do not have to remember to cancel orders. No clutter in your account from old, stale orders that you forgot about.

**Force discipline.** A day order forces you to decide each day whether you still want to pursue a trade. If you place a buy limit at $50 today and do not get filled, tomorrow you have to actively decide: is that order still valid? Does $50 still make sense, given today's price action?

**Default behavior.** Most brokers use day orders as the default, so you do not have to specify anything.

## Disadvantages of day orders

**Resubmit burden.** If you want to hold an order across multiple days, you have to resubmit it every single day. For a busy trader, this is tedious but manageable. For a passive investor, it is annoying.

**Gap risk overnight.** A day order does not protect you overnight. If you place a sell limit at $55 hoping to exit a position on a bounce, and the stock gaps down overnight on bad news, your order is already gone (canceled at market close). The next day, you wake to find the stock at $40 and no active order.

**Miss multi-day moves.** If a stock takes three days to fall from $105 to $50, and you wanted to buy at $50, your day order from day one will not catch the move on day three. You have to remember to resubmit.

## Day orders vs. GTC orders

| Feature | Day order | [GTC order](/gtc-order) |
|---|---|---|
| **Lifespan** | One trading day | Until you cancel, or broker's limit (usually 30–90 days) |
| **Resubmit** | Must resubmit daily | No resubmit; persists |
| **Overnight gap** | No protection (order expires) | Protection continues overnight |
| **Good for** | Intraday traders | Long-term investors, swing traders |
| **Danger** | Forgetting to resubmit | Forgetting about old orders |

## Order expiration times

Day orders typically expire at 4:00 PM ET, which is the official closing time for U.S. equity markets. Some brokers support alternative times:

- **After-hours:** A few brokers allow you to specify that a day order remain active through after-hours trading (until 8:00 PM ET). Most do not.
- **Market on close (MOC):** Some brokers allow an order to execute at the exact closing price, if at all possible. This is a special case and is not the default.

## Market-on-open (MOO) and market-on-close (MOC) orders

These are variants of day orders that specify execution timing:

- **MOO:** A day order that executes at the opening price or is canceled. Used to catch the opening move.
- **MOC:** A day order that executes at the closing price or is canceled. Used to enter or exit exactly at the close (important for index rebalancing and fund closings).

Not all brokers support these.

## Day orders in after-hours trading

Most U.S. brokers offer extended-hours trading (4:00 PM to 8:00 PM ET, and 4:00 AM to 9:30 AM ET). A traditional day order is canceled at 4:00 PM, before after-hours trading begins. If you want to trade in after-hours, you typically need to place a GTC order, or a special after-hours day order (if your broker supports it).

## Best practice with day orders

**Intraday traders** typically embrace day orders as the default. Each morning, review positions and place new orders as needed. Simple, clean, automatic reset.

**Swing traders and longer-term traders** usually prefer GTC orders (or GTD with a multi-day window) to avoid the daily resubmit burden.

**Casual investors** often forget about day orders and miss their entry points; GTC might be more fitting.

## See also

<div class="wiki-seealso">

### Time-in-force variants

- [GTC order](/gtc-order) — good-til-canceled; persists for months
- [GTD order](/gtd-order) — good-til-date; expires on a specific date
- [IOC order](/immediate-or-cancel) — immediate-or-cancel; expires instantly if not filled
- [Fill-or-kill](/fill-or-kill) — fills now or dies immediately

### Order types

- [Limit order](/limit-order) — often submitted as a day order
- [Market order](/market-order) — executes immediately, time-in-force irrelevant
- [Stop order](/stop-order) — can be day, GTC, or GTD
- [Bracket order](/bracket-order) — time-in-force applies to the entire bracket

### Trading styles

- [Day trading](/day-order) — intraday; uses day orders heavily
- [Scalping](/scalping) — very short-term; day orders
- [Swing trading](/swing-trading) — multi-day; usually GTC or GTD

### Context

- [Stock market](/stock-market) — trading hours and close times
- [After-hours trading](/after-hours-trading) — before and after standard hours

</div>

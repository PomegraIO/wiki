---
title: "GTD order"
description: "A GTD (good-til-date) order is an order that remains active until a specific date you choose. It is a middle ground between day orders (expire at close) and GTC orders (expire at broker's discretion)."
keywords:
  - GTD order
  - good-til-date
  - time-in-force
  - order expiration
image: "https://picsum.photos/seed/gtd-order/900/600"
---

*A **GTD order** (good-til-date) is an order that remains active until a date you specify. If the order does not fill by that date, it is automatically canceled. GTD is a middle ground: longer-lived than a [day order](/day-order), but with a known expiration date (unlike a [GTC order](/gtc-order) that relies on the broker's auto-expiration).*

<div class="wiki-hatnote">

For orders that expire at day's end, see [day order](/day-order). For open-ended orders, see [GTC order](/gtc-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">GTD order — key facts</div>

<img src="https://picsum.photos/seed/gtd-order/900/600" alt="A calendar showing a GTD order expiring on a chosen date" />

<div class="wiki-infobox-caption">You choose the expiration date; the order lives until that day at market close.</div>

|   |   |
|---|---|
| **What it is** | An order that expires on a specific date you set |
| **Expiration** | Automatically canceled at market close on your chosen date |
| **Good for** | Event-driven trades, multi-week positions, avoiding forgotten orders |
| **Duration** | A few days to several weeks (depending on when you set expiration) |
| **Resubmit** | No; it lives until expiration or you cancel it |
| **Broker support** | Widely supported, but not universal |

</aside>

## How GTD orders work

When you place a [limit order](/limit-order) and specify "GTD" with an expiration date (e.g., "valid through December 15, 2024"), the order will:

1. **Fill if price is reached.** At any point before the expiration date, if the price touches your limit, you are filled.
2. **Cancel at expiration.** If the price never reaches your limit, the order is automatically canceled at market close on December 15.
3. **Allow early cancellation.** You can cancel at any time before expiration.

**Example:** You place a GTD limit order to buy 100 shares at $50, valid through Friday (five days from now). The stock closes at $52 every day. On Friday at 4:00 PM, your order is automatically canceled. If you had wanted to keep waiting, you would need to resubmit a new GTD with a later expiration date.

## GTD vs. GTC vs. day orders

| Feature | Day order | GTD order | [GTC order](/gtc-order) |
|---|---|---|---|
| **Duration** | One trading day | Until your chosen date | Until canceled or broker expires |
| **Expiration timing** | Automatic (at close) | Automatic (your chosen date) | Manual or broker-imposed |
| **Good for** | Intraday trading | Event-driven trades | Long-term, patient entries |
| **Resubmit needed** | Yes, daily | No, until expiration | No, until canceled |
| **Risk of stale orders** | Low | Medium | High (can linger months) |

## When to use GTD orders

**Event-driven trades.** Suppose you are betting on a company announcement (earnings, acquisition, etc.) expected in two weeks. You place a GTD buy limit order expiring the day after the announcement. If the stock dips before the event, you buy. If not, the order expires and you move on.

**Vacation or away time.** You are going on a two-week vacation and want to buy a stock if it falls to a certain price. You place a GTD order expiring the day before you return. If the dip happens, you are filled. If not, the order dies and you review on your return.

**Multi-day swing trades.** A swing trader might place a GTD order to buy a pullback over the next five trading days. After five days, if the pullback did not come, the trader cancels the order and reassesses.

**Earnings or dividend dates.** You want to sell a stock after its quarterly [earnings](/earnings-per-share) report (expected in 10 days). You place a GTD limit order to sell at a target price, valid through the day after earnings.

## Advantages of GTD

**Control over expiration.** Unlike a [GTC order](/gtc-order) that expires at the broker's whim (typically 60–90 days), a GTD lets you pick the date. If you want an order to live exactly seven days, you can set it to expire in seven days.

**Reduces forgotten orders.** You know when your order will die. If you place a GTD order expiring on December 15, you are mentally prepared for the order to vanish if not filled. No surprise.

**Forces decision-making.** When your GTD order is about to expire, you have to decide: should I extend it (place a new GTD)? Or is the trade thesis no longer valid?

**Clean trading diary.** By choosing expiration dates strategically, you keep your order book cleaner and more aligned with your trading plan.

## Disadvantages of GTD

**Must choose expiration in advance.** You have to guess how long to wait. If you set expiration to five days and the move comes on day seven, you miss it.

**Resubmission still required.** If you want to extend beyond the GTD date, you have to manually place a new order. Not as bad as a [day order](/day-order) (daily resubmission), but still more work than a [GTC order](/gtc-order).

**Overnight gaps still risky.** A GTD order does not protect against overnight gaps any better than a day order. If you place a sell limit and the stock gaps down overnight, your order is still there waiting to sell at the limit (which is now far below the opening price).

## Practical GTD strategies

**One-week experiments.** Place a GTD order for one week. Either it fills (trade works) or it expires (trade thesis disproved or timing off). Clean, decisive.

**Earnings-week trades.** Place a GTD to sell a position, expiring the day after expected earnings. If the stock rallies hard into earnings, you might fill. If not, you hold into the event.

**Vacation buys.** Heading away for two weeks? Place a GTD buy order expiring the day before you return. If a dip happens, you are long. If not, the order is gone and you can reassess.

**Staggered entries.** Place multiple GTD orders at different price levels, each expiring on a different date. This spreads your entry expectations over time.

## Broker support and limitations

Most large brokers (Schwab, Fidelity, Interactive Brokers, TD Ameritrade) support GTD orders. However:
- Some brokers limit how far in the future you can set a GTD (e.g., max 60 days).
- Some brokers charge slightly more for GTD orders than for day orders.
- Some brokers only support GTD for stocks, not for [options](/option) or futures.

Check your broker's documentation.

## GTD in after-hours trading

A GTD order typically expires at the standard market close (4:00 PM ET for U.S. stocks). If you place a GTD order with a Friday expiration, it will expire at Friday's 4:00 PM close, even if after-hours trading continues until 8:00 PM. The order is dead before after-hours begins.

If you want the order to remain active into after-hours, you may need a [GTC order](/gtc-order) or special broker-specific options.

## See also

<div class="wiki-seealso">

### Time-in-force variants

- [Day order](/day-order) — expires at market close (same day)
- [GTC order](/gtc-order) — expires at broker's limit (typically 60–90 days)
- [IOC order](/immediate-or-cancel) — expires instantly if not filled
- [Fill-or-kill](/fill-or-kill) — must fill now or die

### Order types

- [Limit order](/limit-order) — usually submitted with a time-in-force
- [Stop order](/stop-order) — can be day, GTD, or GTC
- [Trailing stop order](/trailing-stop-order) — dynamic stop, often GTD

### Trading context

- [Earnings](/earnings-per-share) — event-driven trades often use GTD
- [Dividends](/dividend) — ex-date and payment-date timing
- [Swing trading](/swing-trading) — multi-day trades often use GTD
- Event-driven trading — GTD orders are common

</div>

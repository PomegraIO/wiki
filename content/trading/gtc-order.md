---
title: "GTC order"
description: "A GTC (good-til-canceled) order is an order that remains active until you manually cancel it, or until your broker imposes a time limit (typically 30–90 days). Much longer-lived than a day order."
keywords:
  - GTC order
  - good-til-canceled
  - time-in-force
  - persistent order
image: "/svg/trading.svg"
---

*A **GTC order** (good-til-canceled) is an order that stays active indefinitely until you manually cancel it or your broker imposes a cutoff. Most brokers implement a "hard stop" — the order auto-expires after 30, 60, or 90 days — to prevent forgotten orders from lingering forever. A GTC order is ideal for patient investors who want to buy or sell at a specific price and are willing to wait.*

<div class="wiki-hatnote">

For orders that expire at day's end, see [day order](/day-order). For orders that expire on a specific date, see [GTD order](/gtd-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">GTC order — key facts</div>

<img src="/svg/trading.svg" alt="A calendar showing a GTC order persisting across days" />

<div class="wiki-infobox-caption">A GTC order persists across trading days until you cancel it or it auto-expires.</div>

|   |   |
|---|---|
| **What it is** | An order that lives until you cancel or broker expires it |
| **Typical broker limit** | 30, 60, or 90 days (check your broker's policy) |
| **Good for** | Patient entries, long-term investors, avoiding daily resubmission |
| **Risk** | Forgetting about old orders; overstaying in changed market conditions |
| **Default** | No; most brokers default to day orders |
| **Cancellation** | Manual (or automatic at broker's time limit) |

</aside>

## How GTC orders work

When you place a [limit order](/limit-order) and specify GTC, the order will sit in the order book across multiple days until:

1. **It fills.** The price is reached and your order matches a counterparty. You are done.
2. **You cancel it.** You log in to your broker and manually cancel the order.
3. **The broker expires it.** After 30, 60, or 90 days (depending on your broker), the order is automatically canceled.

**Example:** You place a GTC limit order to buy 100 shares at $50 on a Monday. The stock closes at $52 every day for a month. Your order sits unfilled. If you do nothing:
- After 30 days (if your broker's limit is 30), the order is auto-expired.
- If your broker's limit is 90 days, it persists for another 60 days, waiting.

If you get tired of waiting, you can cancel it any day.

## Advantages of GTC orders

**Lazy entry.** You set a price and forget about it. If the market ever falls to that level, you are bought. No daily resubmission needed.

**Swing trading.** A swing trader might place a GTC limit order to buy a pullback in a stock and then ignore it while handling other trades. If the pullback happens, the order fills. If it never happens, the trader cancels it.

**Dollar-cost averaging.** Some investors place multiple GTC orders at different price levels, letting the market gradually fill them over time.

**Patience rewarded.** In choppy, ranging markets, a GTC order can catch moves that intraday traders miss. You are patient and the market comes to you.

## Disadvantages of GTC orders

**Forgotten orders.** The cardinal sin of GTC orders is forgetting about them. You place a buy limit at $50, the stock crashes to $45, the limit fills at $50, and you now hold a position you forgot about. Worse, the thesis behind the original trade might be invalidated.

**Stale conditions.** You place a buy limit at $50 on the assumption that $50 is "cheap." Six weeks later, the stock is at $40 and you think $50 is expensive, but your GTC order is still there, waiting to buy at $50. You have to remember to cancel it.

**No overnight protection.** A GTC order provides no special protection across overnight gaps. If you place a sell limit at $55 and the stock gaps down overnight, your order is still there the next morning waiting to sell at $55 (which will not happen if the stock is now $40).

**Broker expiration.** Your broker will auto-expire your GTC order after its limit (typically 60–90 days). This can catch you off-guard if you expected the order to persist. Always check your broker's policy.

## GTC vs. day orders

| Feature | Day order | GTC order |
|---|---|---|
| **Duration** | One trading day | Until canceled or broker expires |
| **Overnight gap** | Order expires; no protection | Order persists |
| **Resubmit** | Must resubmit daily | No resubmit needed |
| **Risk of stale conditions** | Lower (forces daily review) | Higher (can linger weeks) |
| **Good for** | Intraday traders | Patient, long-term traders |

## GTC orders and corporate actions

If a company pays a [dividend](/dividend) or executes a [stock split](/stock-split), your GTC order does not automatically adjust. For example:
- You place a GTC buy limit at $50.
- The company does a 2-for-1 stock split; price falls to $25, but share count doubles.
- Your order is still set to buy at $50 for the original share count, which is now obsolete.

You typically need to cancel and resubmit orders after corporate actions.

## Managing GTC orders: best practices

**Write them down.** Keep a list (even a text file) of active GTC orders, what they are for, and when you placed them. Review weekly.

**Set calendar reminders.** If you expect an order to take weeks to fill, set a reminder to check in at the broker's expiration date. This prevents surprise expirations.

**Use GTD instead.** If you want a GTC-like order but with a known expiration date, use a [GTD order](/gtd-order) set to expire on a date you choose.

**Review before earnings or major events.** If you have a GTC order active and earnings are coming, review it. The trade thesis might change.

## Brokers with unusual GTC policies

Most brokers (Schwab, Fidelity, Interactive Brokers, TD Ameritrade) auto-expire GTC orders after 60–90 days. Some brokers have different policies:
- **Interactive Brokers:** Allows very long GTC periods with explicit policy.
- **Some international brokers:** May auto-expire after 30 days.

Always verify your broker's GTC expiration policy to avoid surprises.

## See also

<div class="wiki-seealso">

### Time-in-force variants

- [Day order](/day-order) — expires at market close
- [GTD order](/gtd-order) — expires on a specific date you choose
- [IOC order](/immediate-or-cancel) — expires instantly if not filled
- [Fill-or-kill](/fill-or-kill) — must fill now or die

### Order types

- [Limit order](/limit-order) — often submitted as a GTC order
- [Stop order](/stop-order) — can be day, GTC, or GTD
- [Trailing stop order](/trailing-stop-order) — dynamic stop, often GTC

### Trading strategies

- [Swing trading](/swing-trading) — common user of GTC orders
- [Dollar-cost averaging](/dollar-cost-averaging) — multiple GTC orders at different levels
- Patience investing — letting the market come to you

### Broker operations

- Order management — canceling and modifying orders
- Corporate actions — stock splits, dividends

</div>

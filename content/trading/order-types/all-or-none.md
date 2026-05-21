---
title: "All-or-none order"
description: "An all-or-none (AON) order will execute only if your entire specified quantity can fill at your stated price. If full size is not available, the order sits in the book waiting, rather than accepting a partial fill."
keywords:
  - all-or-none
  - AON order
  - order types
  - execution condition
image: "/svg/trading.svg"
---

*An **all-or-none (AON) order** is an instruction that your entire position must fill, or none of it fills. Unlike a [limit order](/limit-order/) that can partially fill, an AON order sits in the order book waiting for enough liquidity to appear at your price such that your entire size can trade at once. If the full size never appears, the order can sit for days.*

<div class="wiki-hatnote">

For immediate execution with partial fills, see [immediate-or-cancel](/immediate-or-cancel/). For immediate all-or-nothing, see [fill-or-kill](/fill-or-kill/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">All-or-none order — key facts</div>

<img src="/svg/trading.svg" alt="An order book showing an AON order waiting for full size" />

<div class="wiki-infobox-caption">AON order sits dormant until full size is available; then executes completely or remains waiting.</div>

|   |   |
|---|---|
| **What it is** | Order that fills only if your entire size is available |
| **Partial fills** | Not allowed; order waits |
| **Timing** | Patient; can sit for days or weeks |
| **Typical duration** | Day, GTC, or GTD |
| **Good for** | Large institutional blocks, ensuring clean trades |
| **Risk** | Order may never fill if full size never accumulates at your price |

</aside>

## How all-or-none orders work

When you place an AON order, you are saying: "I want my entire size filled, and nothing less."

**Example:** You are selling 50,000 shares at $100 as an AON order.
- At 10:00 a.m., there is only 40,000 shares of buy interest at $100; your order does not fill.
- Over the next two hours, more buyers accumulate.
- At 12:15 p.m., there are 50,000+ shares of buy interest at $100; your entire 50,000 sells at once.

Or, if the accumulation never happens, your order sits until market close (if it is a [day order](/day-order/)) or until you cancel it (if [GTC](/gtc-order/)).

## AON vs. immediate-or-cancel

Both do not allow partial fills, but they differ on timing:

| Feature | AON | [IOC](/immediate-or-cancel/) |
|---|---|---|
| **Timing** | Patient; waits for full size | Immediate; no waiting |
| **Outcome if full size unavailable** | Order sits in book | Order canceled (unfilled portion) |
| **Use case** | "I want all 50,000 shares, can wait" | "I want all 50,000 shares, right now" |

AON is patience; IOC is urgency with partial-fill tolerance.

## AON vs. fill-or-kill

Both require all-or-nothing, but differ on timing:

| Feature | AON | [FOK](/fill-or-kill/) |
|---|---|---|
| **Timing** | Patient; waits | Immediate; no waiting |
| **Outcome if full size unavailable** | Order sits waiting | Entire order canceled |
| **Duration** | Minutes, hours, days, or longer | Seconds |

AON is "I want all 50,000, and I will wait." FOK is "I want all 50,000 right now, or nothing."

## Practical use cases for AON

**Large block sales.** An institution with a large position might sell via an AON order to avoid hitting the market in pieces (which would move the price against them). They wait for a buyer large enough to take the whole block at once.

**M&A and corporate transactions.** In complex block trades (related to mergers, large acquisitions, or corporate restructuring), AON is common. Both buyer and seller want to execute a full, clean trade without multiple fills.

**Avoiding information leakage.** If a 50,000-share order is broken into 5,000-share pieces, algorithms will see each piece and make inferences. An AON order (if it eventually fills all at once) reveals the intent only at the moment of fill.

**Dark pool blocks.** AON orders are particularly popular in dark pools, where large blocks are the norm and full execution is expected.

## The risk of AON orders

The cardinal risk of an AON order is **never filling**. If you are trying to sell 50,000 shares at $100, and the market only ever accumulates 30,000 shares of buy interest at that price (the rest wants to buy at $99.99), your AON order sits forever.

If your AON is a [day order](/day-order/), it expires at 4:00 PM and you have to resubmit. If it is [GTC](/gtc-order/), it can sit for weeks or months, during which the trade thesis might change entirely.

## AON orders and liquidity in thin markets

AON orders are most practical in liquid stocks and large-cap instruments where 50,000-share blocks are not unusual. In thinly traded securities, even a 1,000-share AON order might never fill.

## AON order constraints in the order book

Most exchanges display AON orders in the public order book, but they are marked or segregated so that traders know the full size must be taken. Some brokers and venues handle AON differently:

- **NYSE:** AON orders are marked and shown in the order book; they can interact with regular orders.
- **NASDAQ:** AON orders are handled similarly, but execution rules may vary.
- **Dark pools:** AON orders are common and often executed more reliably (only shown to buyers with sufficient size).

## AON vs. block trading desks

Institutions trading large blocks often do not use AON orders; instead, they contact a block trading desk (at a bank or broker) and negotiate a direct trade. The AON order is more of a retail or semi-institutional tool for orders that are large but not so large that a dedicated negotiation is necessary.

## AON and corporate actions

If your AON order is pending and the company pays a dividend, executes a stock split, or has some other corporate action, your order does not automatically adjust. You typically need to cancel and resubmit.

## When NOT to use AON

**When you are okay with partial fills.** If getting 80% of your order filled is acceptable, use a regular [limit order](/limit-order/) or [IOC order](/immediate-or-cancel/) instead.

**When you need liquidity urgently.** If you need to exit now, use an [IOC order](/immediate-or-cancel/) or [market order](/market-order/), not an AON.

**In thin markets.** If the security trades low volumes, an AON order might never fill.

## See also

<div class="wiki-seealso">

### Closely related

- [Immediate-or-cancel](/immediate-or-cancel/) — all-or-nothing, immediate
- [Fill-or-kill](/fill-or-kill/) — all-or-nothing, immediate, or order dies
- [Limit order](/limit-order/) — standard order; allows partial fills
- Block trading — large orders; AON common

### Time-in-force variants

- [Day order](/day-order/) — expires at market close
- [GTC order](/gtc-order/) — good-til-canceled
- [GTD order](/gtd-order/) — good-til-date

### Order book and execution

- Order book — where AON orders sit
- Liquidity — how much size is available
- Partial fill — AON orders do not accept these

### Trading context

- [Dark pool](/dark-pool/) — AON orders very common in dark pools
- Block size — what qualifies as a large block

</div>

---
title: "Fill-or-kill order"
description: "A fill-or-kill (FOK) order must execute immediately and completely, or be canceled entirely. It is used when you want all-or-nothing execution without any waiting or partial fills."
keywords:
  - fill-or-kill
  - FOK order
  - order types
  - execution condition
image: "/svg/trading.svg"
---

*A **fill-or-kill (FOK) order** is an instruction that must execute completely and immediately at your specified price, or be canceled entirely. No partial fills, no waiting. If 10,000 shares are not available to buy or sell right now at your price, the entire order is killed. FOK is used by traders who want all-or-nothing execution or prefer to move on rather than split a large order.*

<div class="wiki-hatnote">

For immediate execution with partial fills allowed, see [immediate-or-cancel](/immediate-or-cancel/). For a size-constraint, see [all-or-none](/all-or-none/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fill-or-kill order — key facts</div>

<img src="/svg/trading.svg" alt="A trading terminal showing a FOK order result" />

<div class="wiki-infobox-caption">FOK: all-or-nothing, now-or-never execution.</div>

|   |   |
|---|---|
| **What it is** | All-or-nothing order that must execute immediately |
| **Execution requirement** | Full size at specified price, or the entire order is canceled |
| **Timing** | Must execute immediately (no waiting) |
| **Partial fills** | Not allowed; rejected if full size unavailable |
| **When to use** | Large orders where you want all-or-nothing, or prefer to cancel |
| **Rarity** | Uncommon for retail; mainly institutional |

</aside>

## How fill-or-kill works

When you place a FOK order, you are saying: "Fill my entire size right now at my price, or do not fill any of it."

**Example:** You place a FOK order to buy 10,000 shares at $50.
- If there are 10,000 shares available to buy at $50 or better, your entire order fills immediately.
- If there are only 8,000 shares available at $50, and the next 2,000 are at $50.01, your entire order is canceled (killed). You get nothing.

This is an all-or-nothing constraint combined with an immediate-or-never timing constraint.

## FOK vs. IOC (immediate-or-cancel)

Both FOK and [IOC](/immediate-or-cancel/) orders execute immediately or are canceled, but they differ on partial fills:

| Feature | FOK | IOC |
|---|---|---|
| **Partial fills** | Not allowed; rejected if full size unavailable | Allowed; fill what you can now, cancel the rest |
| **Outcome if full size unavailable** | Entire order canceled | Partial fill accepted, remainder canceled |
| **Use case** | All-or-nothing must execute | Maximize execution, accept partial fill |

If you place a 10,000-share FOK at $50 and only 8,000 are available, you get 0 shares. If you place a 10,000-share IOC at $50, you get 8,000 shares.

## FOK vs. AON (all-or-none)

FOK and [all-or-none](/all-or-none/) both require full size, but they differ on timing:

| Feature | FOK | AON |
|---|---|---|
| **Timing** | Immediate execution or death | Can sit in order book waiting |
| **Waiting** | Not allowed | Allowed |
| **If full size not available now** | Order canceled immediately | Order sits waiting for full size |
| **Duration** | Seconds | Can be minutes, hours, or days |

A FOK is "I want all 10,000 right now, or forget it." An AON is "I want all 10,000, and I will wait for them."

## Practical use cases for FOK

**Large block trades.** An institution wanting to buy a large position might use FOK. "If I cannot get my entire block at my target price right now, I do not want a partial fill — I will look for liquidity elsewhere."

**Arbitrage trades.** An arbitrageur might place a FOK to buy on one venue (if it executes the full size immediately). If the full size is not available, the arbitrage opportunity is likely gone anyway, so canceling the order is fine.

**Market-maker inventory management.** Market makers use FOK orders to avoid taking on unwanted partial inventory. "I want to sell 5,000 shares, all at once, at my price. If I can only sell 3,000, I will hold my inventory instead."

## Liquidity and FOK

FOK orders are only practical in highly liquid securities where your order size is small relative to available liquidity. For a large-cap stock like Apple, a 10,000-share FOK will likely execute. For a thinly traded penny stock, even a 1,000-share FOK might be killed.

Large institutions trading illiquid securities would never use FOK; they would use [all-or-none](/all-or-none/) and wait for the full size to accumulate.

## FOK and broker support

FOK support varies by broker:

- **Interactive Brokers:** Fully supports FOK for stocks and many other instruments.
- **Schwab, Fidelity, TD Ameritrade:** Support FOK for stocks and some derivatives.
- **Discount brokers:** May not support FOK; check documentation.

If your broker does not support FOK, you can sometimes approximate it with a [limit order](/limit-order/) combined with an [all-or-none](/all-or-none/) constraint and a very short time window (e.g., day order).

## FOK orders and slippage

A FOK order with a limit price is somewhat protected: your order will only fill at your limit price or better. But a FOK order that is a [market order](/market-order/) (market-FOK) will execute immediately at whatever price the market offers. This can result in slippage if you are not careful.

Most FOK orders are limit orders, not market orders.

## When NOT to use FOK

**Small orders in liquid markets.** If you are buying 100 shares of a large-cap stock, just use a regular [limit order](/limit-order/) or [market order](/market-order/). FOK is overkill.

**When you want partial fills.** If you are happy to get 80% of your order filled and move on, use an [IOC order](/immediate-or-cancel/) instead.

**When you are patient.** If you have time and want to ensure you get all your shares, use an [all-or-none](/all-or-none/) order and wait.

## See also

<div class="wiki-seealso">

### Closely related

- [Immediate-or-cancel](/immediate-or-cancel/) — immediate or death, but allows partial fills
- [All-or-none](/all-or-none/) — full size required, but can wait
- [Limit order](/limit-order/) — standard order with price protection
- [Market order](/market-order/) — immediate execution at any price

### Time-in-force and execution

- [Day order](/day-order/) — typical time-in-force for limit orders
- [GTC order](/gtc-order/) — good-til-canceled
- Fill — when an order executes

### Trading context

- Block trading — large orders; sometimes use FOK
- Slippage — gap between expected and actual fill price
- Liquidity — how much size is available at a price

</div>

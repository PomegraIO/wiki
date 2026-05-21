---
title: "Immediate-or-cancel order"
description: "An immediate-or-cancel (IOC) order executes immediately at your specified price for whatever quantity is available, and any unfilled remainder is canceled. Partial fills are allowed."
keywords:
  - immediate-or-cancel
  - IOC order
  - order types
  - execution condition
image: "/svg/trading.svg"
---

*An **immediate-or-cancel (IOC) order** is an instruction that must execute right now, for whatever size is available at your price. Any portion that cannot fill immediately is automatically canceled. IOC is the middle ground: you want quick execution and will accept partial fills, but you will not wait.*

<div class="wiki-hatnote">

For all-or-nothing execution, see [fill-or-kill](/fill-or-kill) and [all-or-none](/all-or-none). For orders that can sit and wait, see [limit order](/limit-order).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Immediate-or-cancel order — key facts</div>

<img src="/svg/trading.svg" alt="A trading terminal showing partial fill and remainder canceled" />

<div class="wiki-infobox-caption">IOC: execute now for whatever is available, or cancel the rest.</div>

|   |   |
|---|---|
| **What it is** | Executes immediately; unfilled remainder is canceled |
| **Partial fills** | Allowed and common |
| **Timing** | Must execute now, or portion dies |
| **Price** | At your specified limit (if limit order) or market price (if market IOC) |
| **Best for** | Traders wanting immediate execution with partial fill tolerance |
| **Worst for** | Traders who want guaranteed full execution |

</aside>

## How immediate-or-cancel works

When you place an IOC order, you are saying: "Give me whatever you can right now at my price, and cancel anything else."

**Example:** You place an IOC limit order to buy 10,000 shares at $50.
- 8,000 shares are available at $50; you are filled for 8,000.
- The remaining 2,000 would be $50.01; your order does not wait for them.
- The order immediately cancels the unfilled 2,000 shares.
- You walk away with 8,000 shares filled and 2,000 shares canceled (not sitting in the book).

## IOC vs. fill-or-kill

Both are immediate-execution orders, but they handle partial fills differently:

| Feature | IOC | [FOK](/fill-or-kill) |
|---|---|---|
| **Partial fills** | Allowed; fill what you can | Not allowed; reject if not full size |
| **Outcome if full size unavailable** | Partial fill accepted, remainder canceled | Entire order canceled (killed) |
| **Use case** | Maximize execution, accept partial fills | All-or-nothing or nothing |

IOC is "give me what you can." FOK is "give me all or nothing."

## IOC vs. all-or-none

Both require commitment to trade, but differ on timing:

| Feature | IOC | [All-or-none](/all-or-none) |
|---|---|---|
| **Timing** | Must execute immediately | Can sit waiting for full size |
| **Partial fills** | Allowed | Not allowed |
| **If full size not available now** | Partial fill accepted, remainder canceled | Order sits in book waiting |

IOC is "right now, whatever you have." All-or-none is "whenever the full size is available."

## Practical use cases

**Urgent exits.** You need to sell a position immediately and are willing to take whatever the market offers, but not at a terrible price. You place an IOC limit at a reasonable floor price. You get filled for what is available, and anything unfilled is canceled (you are not stuck with a lingering order).

**Avoiding toxic orders.** You want to buy at $50 but do not want your order sitting in the book (where algorithms might see it and trade against you later). You place an IOC; it fills for available size and disappears.

**Block trading.** An institution buying a large block might use IOC to "poke" the market: "How much can I buy at $50 right now?" The IOC tests liquidity without leaving a toxic order behind.

**Micro-strategy execution.** A trader with a short time window (e.g., "I want to hold this position for exactly 30 seconds") might use IOC to ensure quick execution.

## IOC and liquidity-taking

IOC orders are **aggressive** — they execute immediately, hitting the best ask for buys or the best bid for sells. They are a form of "liquidity-taking." A [limit order](/limit-order) sitting in the book is "liquidity-providing."

Exchanges sometimes charge lower fees for liquidity-providing orders (you add to the book) and higher fees for liquidity-taking orders (you remove from the book). An IOC is liquidity-taking by nature.

## IOC with limit vs. market

**IOC limit order:** You specify a price limit. The order fills at your price or better, or for available size only. Example: IOC limit to buy at $50. You might fill 8,000 at $49.99 but not the remaining 2,000 at $50.01.

**IOC market order:** You accept any price. The order fills at the current best bid-ask. For all practical purposes, an IOC market order is just a [market order](/market-order) (immediate execution at any price).

## Broker support for IOC

Most major brokers support IOC:
- **Interactive Brokers:** Full support for stocks, options, futures.
- **Schwab, Fidelity, TD Ameritrade:** Support for stocks and many derivatives.
- **Discount/budget brokers:** Check; some may not offer IOC.

If your broker does not explicitly support IOC, you might approximate it with a very short time-in-force (e.g., a 5-second GTD order), but this is not ideal.

## IOC and information leakage

An IOC order is aggressive and reveals that you are willing to trade immediately. For large orders, this can tip your hand to algorithms and market makers. Some traders use IOC orders for small test trades (to gauge liquidity) and then follow up with larger orders after confirming availability.

## IOC in different markets

IOC orders work similarly across asset classes (stocks, options, futures), but some derivatives markets have different behavior:

- **Equity options:** IOC is well-supported.
- **Futures:** IOC is common and reliable.
- **Forex/crypto:** Behavior varies by exchange/platform.

## See also

<div class="wiki-seealso">

### Closely related

- [Fill-or-kill](/fill-or-kill) — all-or-nothing; no partial fills
- [All-or-none](/all-or-none) — all-or-nothing; can wait
- [Market order](/market-order) — immediate execution at any price
- [Limit order](/limit-order) — patient execution at your price

### Time-in-force and execution

- [Day order](/day-order) — standard time-in-force
- [GTC order](/gtc-order) — good-til-canceled
- Time in force — how long orders last

### Trading context

- Liquidity — available size at each price
- Slippage — gap between expected and actual fill
- Block trading — large orders often use IOC
- Toxicity — aggressive orders reveal intent

</div>

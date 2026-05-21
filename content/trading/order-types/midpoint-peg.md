---
title: "Midpoint peg"
description: "A midpoint peg order automatically sets its price at the midpoint of the bid-ask spread and adjusts continuously as the spread widens or narrows. The order is more likely to fill on the far side (where counterparty demand exists)."
keywords:
  - midpoint peg
  - peg order
  - order types
  - midpoint
image: "/svg/trading.svg"
---

*A **midpoint peg** is a specialized [peg order](/peg-order/) that always prices itself at the midpoint of the bid-ask spread. If the bid is $50.00 and the ask is $50.02, your order price is automatically set to $50.01. As the spread moves or widens, your order price adjusts to track the new midpoint.*

<div class="wiki-hatnote">

For a peg to the bid or ask, see [peg order](/peg-order/). For a fixed limit, see [limit order](/limit-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Midpoint peg — key facts</div>

<img src="/svg/trading.svg" alt="A price chart showing an order pegged to the midpoint" />

<div class="wiki-infobox-caption">Midpoint peg: order price is always halfway between bid and ask.</div>

|   |   |
|---|---|
| **What it is** | Limit order automatically priced at (bid + ask) / 2 |
| **Price reference** | Midpoint of the spread |
| **Update frequency** | Continuous as the spread changes |
| **Execution likelihood** | Medium (better price than market order, but not at the spread edges) |
| **Good for** | Passive traders wanting fair prices without market impact |

</aside>

## How midpoint pegging works

The midpoint of the bid-ask spread is calculated as: **(Bid + Ask) / 2**

If the current quote is bid $50.00, ask $50.04:
- Midpoint = ($50.00 + $50.04) / 2 = $50.02
- A buy midpoint peg order is placed at $50.02.
- A sell midpoint peg order is also placed at $50.02.

Both a buyer and a seller can peg to the midpoint — they just agree to trade at the fair price.

As the spread changes, the peg price adjusts:
- New quote: bid $50.02, ask $50.05.
- New midpoint = $50.035.
- The peg order automatically moves to $50.035.

## Why midpoint pegging?

**Fair price discovery.** The midpoint is the midway point between supply and demand. Pricing at the midpoint is neutral — you are not trying to get the best deal, just a fair one.

**Passive participation.** By pricing at the midpoint, you are saying: "I am willing to trade at a fair price without chasing." This is attractive to passive investors and market makers who want liquidity without moving the price.

**Reduced market impact.** Unlike a [market order](/market-order/) that hits the ask (moving the market against you), a midpoint peg trades at the fair price.

## Execution dynamics of midpoint pegging

A midpoint peg order will fill only if:
1. The spread exists (there is both a bid and an ask).
2. A counterparty is willing to trade at the midpoint (or better, from their perspective).

**For a buy midpoint peg:**
- Your order sits at the midpoint.
- A seller must be willing to sell at the midpoint or lower (e.g., the seller had a limit at the midpoint, and you hit it).
- If the spread is $50.00 / $50.04, your peg at $50.02 fills when a seller hits your bid.

**For a sell midpoint peg:**
- Your order sits at the midpoint.
- A buyer must be willing to buy at the midpoint or higher (e.g., the buyer had a limit at the midpoint).
- Your sell at $50.02 fills when a buyer hits your ask.

## Midpoint peg vs. regular midpoint limit order

| Feature | Midpoint peg | Static midpoint limit |
|---|---|---|
| **Price** | Dynamically tracks midpoint | Fixed at a calculated midpoint |
| **Adjustment** | Continuous (as spread changes) | Never; stays at the price you set |
| **Execution likelihood** | Can improve as spread changes | Only if price falls to your fixed level |

A **static midpoint limit order** is just a regular [limit order](/limit-order/) set at a midpoint price you calculate once. A **midpoint peg** continuously adjusts.

## Practical example

You want to sell 1,000 shares. The current quote is:
- Bid: $100.00
- Ask: $100.04
- Midpoint: $100.02

You place a sell midpoint peg at $100.02. Over the next few hours:
- 10:30 a.m.: Bid/Ask $100.02/$100.06. Midpoint = $100.04. Your order automatically adjusts to $100.04.
- 11:00 a.m.: Bid/Ask $100.05/$100.07. Midpoint = $100.06. Your order automatically adjusts to $100.06.
- 12:00 p.m.: Bid/Ask $100.08/$100.12. Midpoint = $100.10. Your order automatically adjusts to $100.10.

As the market rises, your peg rises with it. When a buyer hits the ask or better, your midpoint peg fills.

## Midpoint pegging and market microstructure

Midpoint pegging became more popular after the rise of lit venues and algorithmic trading. It allows traders to:
- Access liquidity at fair prices (the midpoint).
- Avoid chasing (as prices move, the peg follows).
- Reduce adverse selection (by pricing fairly, you attract true counterparties, not aggressive traders front-running your orders).

## Broker and exchange support

Midpoint pegging is supported by most major brokers and exchanges, but with nuances:

- **NYSE, NASDAQ:** Support midpoint pegging for most securities.
- **Dark pools:** Many use midpoint pricing as their default execution price.
- **International exchanges:** Variable support; check your local exchange.

Some brokers offer "midpoint peg + tick" (peg at midpoint + 1 cent), which improves your execution while staying close to fair value.

## Limitations of midpoint pegging

**Very wide spreads:** If the spread is $50.00 / $50.10 (a dime), the midpoint is $50.05. A buyer at $50.02 will not hit your midpoint peg. You might never fill.

**Illiquid securities:** In thin stocks, spreads are wide and prices are erratic. Midpoint pegging does not help you fill; a [market order](/market-order/) might be better.

**Trading away from the midpoint:** If you want to buy cheaper than the midpoint, a peg at the midpoint will not help. You need a lower [limit order](/limit-order/).

## Midpoint pegging vs. dark pools

[Dark pools](/dark-pool/) often use midpoint pricing as their default execution method (trade at the midpoint of the lit market). This is similar in spirit to a midpoint peg order but in a private venue.

**Midpoint peg on lit venue:** Public, transparent, benefits from lit-market price discovery.

**Dark pool at midpoint:** Private, opaque, relies on lit-market prices for the midpoint reference.

## When to use midpoint pegging

**You want fair prices without chasing.** Place a midpoint peg and let it track the fair value.

**You are a maker (providing liquidity).** Market makers sometimes use midpoint pegs to maintain fair quotes without moving prices sharply.

**You want passive execution with no impact.** A midpoint peg is a passive way to execute without moving the market.

## When NOT to use midpoint pegging

**You want a specific price.** If you have a price target in mind, use a regular [limit order](/limit-order/).

**Spreads are wide.** In illiquid markets, the midpoint might be too far from the real trading price.

**You need urgent execution.** Midpoint pegs are passive; they may not fill if price moves away from the fair level.

## See also

<div class="wiki-seealso">

### Closely related

- [Peg order](/peg-order/) — general peg orders (bid, ask, or midpoint)
- [Limit order](/limit-order/) — standard fixed-price limit
- Bid-ask spread — the spread your order references
- [Market order](/market-order/) — immediate at current best price

### Market structure and dynamics

- Order book — where midpoint pegs sit
- [Fair value](/fair-value/) — the midpoint represents this
- Liquidity — midpoint pegs help passive participation
- Adverse selection — midpoint pricing reduces this

### Execution and venues

- [Lit venue](/lit-venue/) — where midpoint pegs are most transparent
- [Dark pool](/dark-pool/) — often uses midpoint pricing
- [Best execution](/best-execution/) — midpoint pegging helps achieve this
- [Smart order router](/smart-order-router/) — routes to best execution including midpoints

</div>

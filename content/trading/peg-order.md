---
title: "Peg order"
description: "A peg order is a limit order that automatically adjusts its price to maintain a fixed offset from a reference price (typically the bid or ask). The limit price moves with the market."
keywords:
  - peg order
  - pegged order
  - order types
  - dynamic price
image: "https://picsum.photos/seed/peg-order/900/600"
---

*A **peg order** is a [limit order](/limit-order) with a dynamic price that automatically adjusts to maintain a fixed distance from a moving reference price. If you place a buy peg order "1 cent below the bid," your limit price continuously adjusts to stay 1 cent below the current bid. When the bid moves, your order price moves with it.*

<div class="wiki-hatnote">

For a fixed limit price, see [limit order](/limit-order). For an automatic offset from the midpoint, see [midpoint peg](/midpoint-peg).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Peg order — key facts</div>

<img src="https://picsum.photos/seed/peg-order/900/600" alt="A price chart showing a pegged order tracking the bid" />

<div class="wiki-infobox-caption">Peg order: limit price moves with the reference (bid, ask, or midpoint).</div>

|   |   |
|---|---|
| **What it is** | Limit order that adjusts price to maintain an offset from a reference |
| **Reference** | Usually the best bid or ask; can also be midpoint |
| **Offset** | A fixed amount (e.g., 1 cent below the bid) |
| **Price adjustment** | Automatic and continuous as the reference changes |
| **Good for** | Passive execution near the market without chasing |
| **Broker support** | Variable; many brokers support pegging |

</aside>

## How a peg order works

You want to buy a stock at 1 cent below the current best ask (to improve price vs. a [market order](/market-order), but stay willing to trade).

**Standard limit order approach:**
- Bid is $50.00, ask is $50.01.
- You place a buy limit at $50.00.
- The bid and ask move. New bid is $50.02, ask is $50.03.
- Your limit order is now at $50.00, which is now 2 cents *below* the new bid. You are too cheap; you do not fill.

**Peg order approach:**
- Bid is $50.00, ask is $50.01.
- You place a buy peg order: "Peg to the best bid, offset 1 cent above."
- Your order price is automatically set to $50.01 (bid $50.00 + 1 cent).
- The bid and ask move to $50.02 and $50.03.
- Your order price automatically adjusts to $50.03 (new bid $50.02 + 1 cent).
- You remain just at or above the ask, ready to fill.

The peg order follows the market's reference price, always maintaining your specified offset.

## Common peg reference prices

**Peg to the bid:** Your order price equals the best bid + your offset. Used by buyers trying to stay just above the bid, improving their chance of execution.

**Peg to the ask:** Your order price equals the best ask + your offset. Less common; used by sellers trying to stay just below the ask.

**Peg to the midpoint:** Your order price equals (bid + ask) / 2 + your offset. Used when you want to trade near the middle.

## Peg order offsets

You specify an offset from the reference:
- **Buy peg at bid + 1 cent:** If bid is $50.00, your order is at $50.01. If bid moves to $50.05, your order is at $50.06.
- **Sell peg at ask - 1 cent:** If ask is $50.05, your order is at $50.04. If ask moves to $50.06, your order is at $50.05.

The offset is always a fixed amount (in cents or percentage).

## Peg orders vs. regular limit orders

| Feature | Regular limit | Peg order |
|---|---|---|
| **Price** | Fixed; does not change | Dynamic; adjusts with reference |
| **Adjustment** | Manual (you resubmit) | Automatic |
| **Execution likelihood** | Depends on how far you place the limit | Higher (adjusts to stay competitive) |
| **Simplicity** | Simple | More complex |
| **Broker support** | Universal | Variable (check your broker) |

A peg order is ideal for traders who want to be just inside the spread without manually adjusting their order price every time the market moves.

## Practical example

You want to buy a stock and you think the current ask of $50.01 is fair, but you prefer to pay $50.00 if possible. You place a buy peg order: "Peg to the best bid, offset +1 cent." (Offset means you are willing to pay the bid plus 1 cent.)

- 10:00 a.m.: Bid $50.00, ask $50.01. Your order is at $50.01 (bid + 1 cent).
- 10:05 a.m.: Bid $50.02, ask $50.03. Your order automatically adjusts to $50.03 (bid + 1 cent).
- 10:10 a.m.: Bid $50.05, ask $50.06. Your order is now at $50.06 (bid + 1 cent).

Your order follows the ask higher, always ready to buy at the bid + 1 cent. If a seller hits your price, you fill.

## Peg orders and execution

A buy peg order set at "bid + 1 cent" essentially says: "I am willing to buy at the ask, but I will back off if the ask falls." It is a passive way to participate in trading without chasing.

This makes peg orders popular for:
- **Market makers:** Adjust their bid-ask quotes all day; peg orders help them remain competitive.
- **Passive traders:** Who want to trade near the market without constantly resubmitting.
- **Limit order books:** Maintaining inventory levels with minimal manual adjustment.

## Peg order restrictions and rules

Not all brokers support peg orders, and those that do have varying rules:

- **SEC Rule 10b-1:** In the U.S., pegging rules are regulated. Brokers must disclose their peg order logic and ensure fair treatment.
- **Some exchanges:** Have rules about how tight the peg can be (e.g., minimum 1 cent offset) to prevent market abuse.
- **Regional differences:** Other countries may have different rules.

Check your broker's peg order rules before relying on them.

## Peg orders and market structure

Peg orders are somewhat controversial. Some argue they improve liquidity (more orders available at competitive prices). Others argue they can create information cascades (many peg orders tracking the same reference can amplify price moves).

Regulators monitor peg orders to ensure they are not abused (e.g., used to mislead other traders about available liquidity).

## Midpoint peg (common variant)

A **midpoint peg** is a peg order set to track the midpoint of the bid-ask spread. For example:
- Bid $50.00, ask $50.02. Midpoint is $50.01.
- A midpoint peg order might be set at "midpoint + 0 cents" = $50.01.
- If bid/ask move to $50.03/$50.05, midpoint is $50.04, and your order is at $50.04.

See [midpoint peg](/midpoint-peg) for more detail.

## When to use peg orders

**You want to stay competitive without manual adjustment.** Post a peg order at a tight offset and let it track the market.

**You are a market maker or liquidity provider.** Peg orders help you maintain tight spreads automatically.

**You want passive execution.** The peg order will fill if prices are right, without you monitoring.

## When NOT to use peg orders

**When you want a fixed price limit.** If you have a price in mind and do not want to pay more, use a regular [limit order](/limit-order), not a peg.

**In low-liquidity stocks.** Peg orders are most useful in liquid, tight-spread markets.

**If your broker does not support them.** Not all brokers offer peg orders.

## See also

<div class="wiki-seealso">

### Closely related

- [Midpoint peg](/midpoint-peg) — peg to the midpoint of the spread
- [Limit order](/limit-order) — standard fixed-price limit
- [Market order](/market-order) — instant execution at any price
- Bid-ask spread — the spread your peg order references

### Market structure

- Order book — where peg orders sit
- [Market maker](/market-maker-trading) — common users of peg orders
- Liquidity — peg orders improve competitiveness
- Price-time priority — peg orders maintain this

### Advanced orders

- [Iceberg order](/iceberg-order) — size-concealing alternative
- [Algorithmic trading](/algorithmic-trading) — uses peg logic
- [Smart order router](/smart-order-router) — routes dynamically

</div>

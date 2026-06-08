---
title: "Pegged Order Types Compared: Primary, Midpoint, and Market Peg"
description: "Primary peg anchors to the NBBO; midpoint peg targets the bid-ask midpoint; market peg follows the best price. Compare strategies, execution, and when to use each."
keywords:
  - pegged order
  - primary peg
  - midpoint peg
  - market peg
  - nbbo
  - order types
---

*A **pegged order** automatically adjusts its limit price as the market moves, anchoring to a reference point such as the [NBBO](/bid-ask-spread/) (national best bid or offer), the bid-ask midpoint, or the best bid or ask. The type you choose determines where your price sits relative to the spread—and therefore your fill likelihood and aggressiveness.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pegged Order Types — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Three ways to chase price with a resting order.</div>

|   |   |
|---|---|
| **Primary peg** | Anchors to NBBO best bid (buy) or best ask (sell) |
| **Midpoint peg** | Anchors to midpoint of bid-ask spread |
| **Market peg** | Follows the best bid or ask, including inside quotes |
| **Price refresh** | All update continuously as market quotes move |
| **Fill likelihood** | Primary peg: moderate; midpoint: low; market peg: high |
| **Use case** | Primary: passive; midpoint: mid-aggressive; market peg: aggressive |

</aside>

## Primary peg: anchoring to the NBBO

A **primary peg order** ties its limit price to the [national best bid or offer](/bid-ask-spread/). If you place a pegged buy order, it sits one tick below the current best ask; if you place a pegged sell, it sits one tick above the current best bid. As the market quotes change, your order price updates automatically.

For example, suppose Apple's best bid is $190.45 and best ask is $190.46. You place a primary peg buy order. The order will execute at $190.46 (the ask) if someone sells at market, but typically your broker allows you to specify an offset—e.g., "one cent below the offer" or "at the bid." The order then rests at $190.45 and updates each time the NBBO moves.

When the best ask ticks up to $190.50, your pegged buy order automatically adjusts to $190.49, hunting passively for the new best ask level. This keeps you perpetually near the inside of the spread without manual intervention.

**Primary peg is the most widely supported and broadly used of the three types.** It is the default pegging method on many exchange-listed securities and suits traders who want passive fill execution—letting the order sit at a competitive but not aggressive price, adjusting as the market moves, until it fills or the session ends.

## Midpoint peg: the half-way point between bid and ask

A **midpoint peg** anchors to the mathematical midpoint of the current spread. If the bid is $190.45 and the ask is $190.46, the midpoint is $190.455 (or $190.45 and a fraction of a cent). The order sits at that mid-price and adjusts as the spread widens or tightens.

Midpoint pegs are useful for algorithms and passive traders who want to be "fair" to both sides: you're not sitting at the aggressive bid or ask, you're splitting the difference. This philosophy appeals to:

- **Market makers** placing their own resting orders
- **Large institutions** executing passively to minimize signaling (you're not competing at the bid or ask, so you're less visible)
- **Algorithmic traders** who want execution somewhere between passive and aggressive

The trade-off is that midpoint pegs fill less often than primary pegs or market pegs. The counterparty must cross the spread to meet you at the midpoint, whereas a primary peg order sitting at the best ask will fill whenever someone hits the ask. For this reason, midpoint pegs are popular in larger-cap liquid stocks where small penny moves are acceptable and volume is abundant.

## Market peg: the most aggressive anchor

A **market peg** follows the best bid or ask, moving in real time with every quote update. It is the most aggressive of the three, because your order sits at the inside edge of the spread and updates as the market shifts. If you place a market peg buy, it rests at the current best ask; when the best ask moves, your order moves with it.

Market pegs fill fastest because they're always at the most competitive price. If the ask jumps from $190.46 to $190.48, your pegged buy order jumps to $190.48 to stay at the best level. Any sell at market will execute into your order immediately.

**Market pegs are preferred by aggressive traders and execution algorithms** that prioritize fill speed and certainty over price improvement. They're common in:

- High-frequency strategies where speed of execution dominates
- Block trades or large orders where getting filled is more important than saving a penny
- Volatile conditions where waiting for a better price is riskier than filling now

The risk is cost: you're often paying the full ask spread (as a buyer) or taking the full bid spread (as a seller), so you're giving away the tightest possible price in exchange for certainty of execution.

## When to use each type

**Primary peg** suits most retail and institutional traders placing passive resting orders. You want a competitive price that adjusts automatically as the market moves, without being so aggressive that you're always at the ask. It's the default choice for limit orders you're willing to let sit for hours or days.

**Midpoint peg** is best when you have size and want minimal market impact. The midpoint price signals a neutral stance to the market, and algorithms that scan for hidden resting orders may find your midpoint peg less threatening than a bid or ask order, encouraging them to route orders your way. It's also useful in choppy spreads: if a stock trades with a wide 3-cent spread, sitting at the midpoint lets you avoid being shaken out by the noise at the edges.

**Market peg** is appropriate when execution speed and certainty trump price. If you're running an algorithm that must absorb a large block within a time window, market pegs at multiple price levels keep you in front of the queue. Retail traders rarely use market pegs because they cost more, but they're essential for institutions managing slippage on large orders.

## Offset and distance parameters

Most brokers let you specify an offset or "distance" from your pegging anchor. A primary peg order might be:
- "One penny below the ask" (for a buy)
- "One cent above the bid" (for a sell)
- "Half the spread below the ask"

Midpoint pegs sometimes allow offsets too, letting you sit below or above the true midpoint. Market pegs typically offer less customization because the whole point is to follow the best price in real time; adding offsets defeats the purpose.

## Execution and refresh during gaps

All three peg types update during normal trading as new quotes arrive. However, if a stock gaps at the open—pre-market trading shows very different levels, or overnight news causes a price jump—the pegged orders will adjust to the new NBBO, bid-ask midpoint, or best price, respectively. They don't "remember" the previous session's anchor; they re-peg to current reality.

## Partial fills and queue position

Pegged orders can partially fill. If a primary peg buy at 190.46 fills 500 of 2,000 shares, the remaining 1,500 stay pegged at the new best ask price (say, 190.47) and hunt for more. You may jump queues as the price adjusts, depending on how the exchange's queue and order book handle peg refreshes; this varies by exchange.

## Regulatory and technical limits

Pegged orders are SEC-permitted under Rule 10b-1, which requires brokers to have reasonable procedures for updating peg orders. Not all small brokers or OTC platforms support pegged orders; they're most common on major U.S. exchanges (NYSE, NASDAQ) and interactive platforms like Interactive Brokers, Fidelity, and Schwab. Confirm your broker supports the peg type you need before building a strategy around it.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — static price order that pegs enhance
- [Bid-Ask Spread](/bid-ask-spread/) — where pegs anchor and adjust
- [Day Order vs Good-Till-Cancelled Order](/day-order-vs-good-till-cancelled/) — time-in-force for pegged orders
- [Price Discovery](/price-discovery/) — how pegged orders contribute to NBBO formation
- [Market Order](/market-order/) — aggressive execution pegged orders contrast with

### Wider context

- [Market Maker Trading](/market-maker-trading/) — counterparty often interacting with pegged orders
- [Stock Exchange](/stock-exchange/) — venue where pegs are implemented
- [Algorithmic Trading](/algorithmic-trading/) — field where pegged orders are heavily used
- Order Book — internal structure pegged orders update within

</div>

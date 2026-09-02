---
title: "Peg Order"
description: "Order that automatically adjusts its limit price based on a reference price, such as the national best bid or ask."
keywords:
  - peg order
  - pegging
  - dynamic limit price
  - order routing
---

*A **peg order** is a limit [order](/wiki/limit-order/) whose price is not fixed but automatically adjusts relative to a reference point — most commonly the national best bid or ask ([NBBO](/wiki/nbbo/)). If the [NBBO](/wiki/nbbo/) moves up, the pegged order moves with it. This allows traders to stay competitive without manually canceling and re-entering orders as the market shifts.*

<aside class="wiki-infobox">

| Factor | Detail |
|--------|--------|
| **Mechanism** | Limit price adjusts with reference price movement |
| **Primary Reference** | National best bid/ask (NBBO) |
| **Offset** | Typically a fixed number of cents (e.g., 1 cent inside the spread) |
| **Exchange Rules** | Regulated under SEC Rule 10b-5 anti-manipulation; FINRA rules |
| **Brokers Supporting** | Most major platforms; some retail brokers exclude |
| **Execution Speed** | Faster than manual re-entry; no human delay |
| **Cost** | May incur higher commissions; some brokers bundle at standard rate |

</aside>

## How pegging works

Suppose you want to buy XYZ stock but don't want to pay the current ask of $50.00. Instead of placing a static limit order at $49.95, you submit a peg order to buy at 1 cent below the national best ask. The order rests at $49.99. If the ask moves to $51.00 due to new market data, your pegged buy order automatically moves to $50.99. If the ask drops to $48.00, your order reprices to $47.99.

The key feature is **automation**. The exchange's matching engine re-evaluates the peg each time the reference price updates, typically every millisecond during active trading. This eliminates the lag that would occur if you were manually canceling and re-entering orders.

## Types of peg orders

**Mid-point peg:** The limit price is set to a fixed offset from the midpoint of the best bid and ask. If the bid is $50.00 and the ask is $50.10, the midpoint is $50.05. A peg at +1 cent would be $50.06.

**Best bid/ask peg:** The order pegs to the bid (for sell orders) or the ask (for buy orders), plus or minus an offset.

**Primary peg:** On multi-exchange venues, the peg references the best price on the primary listing exchange, not the consolidated NBBO. This was more common before [Reg NMS](/wiki/reg-nms-adoption/) harmonized best-price rules.

**Trade-through protection:** A peg order will not execute at a price that would constitute a trade-through under [Reg NMS](/wiki/reg-nms-adoption/) — a buy order that executes at a lower ask without first checking if a higher ask exists on another exchange.

## Advantage: staying in the queue

A pegged buy order at 1 cent below the ask gets in line to execute as soon as the ask drops to that level. A static limit order 1 cent below the NBBO risks being leapfrogged if the ask falls further before your order executes. By pegging, you maintain your relative position in the queue as the market moves, improving fill odds.

## Disadvantage: front-running perception

Early peg orders drew regulatory scrutiny because they can appear to trade-through on the opposite side of the spread. If the best ask is $50.10 and your peg order is set to buy at 1 cent inside (best ask minus 1 cent = $50.09), you're theoretically closer to the spread than was advertised to other traders. Some exchanges and the SEC have rules to prevent predatory pegging that amounts to hidden order queuing.

## Use in market making and scalping

[Market makers](/wiki/market-makers/) and [scalpers](/wiki/scalping/) rely heavily on peg orders to manage large quoting operations. A market maker might maintain dozens of pegged orders across the bid and ask simultaneously, automatically repricing as the market moves. This lets them quote many symbols without dedicating a trader to each one.

## Execution quality considerations

Peg orders can improve execution quality by keeping your order closer to the best price as the market moves. But if the reference price (the NBBO) is itself distorted by a [flash crash](/wiki/flash-crash-2010/) or a market data feed glitch, your peg order reprices into a distorted level and may execute against other erroneous orders.

## SEC and exchange regulation

The SEC's Rule 10b-5 requires that peg orders not facilitate [manipulation](/wiki/rule-10b-5/). In practice, this means peg orders must either trade at the best bid/ask or be immediately cancelled if the reference price moves past them (no hiding or layering). Most exchanges have rule books governing permissible peg types and offsets.

[Reg NMS](/wiki/reg-nms-adoption/) specifically addresses pegging to ensure that orders do not trade through the NBBO. The [NBBO](/wiki/nbbo/) check happens automatically on each repricing.

## Broker platform differences

Not all brokers support peg orders. Retail platforms like Fidelity and Charles Schwab offer basic pegging; some discount brokers and robo-advisors do not. Institutional traders use peg orders across all major venues. The cost varies: some brokers bundle peg orders at the standard commission; others charge incremental fees for the repricing logic.

## Pegging vs. time-in-force orders

A [good-till-cancelled (GTC)](/wiki/gtc-order/) order stays at a fixed price until manually cancelled. A peg order reprices continuously. A [day order](/wiki/day-order/) expires at the end of session. Most peg orders are day orders, though some brokers allow GTC pegs that reprice daily. For longer holding periods, manually managing a static limit order is often cleaner than relying on a peg.

## Relationship to hidden orders

A [hidden order](/wiki/hidden-order/) (or iceberg) shows only a small quantity to the market, with a larger reserve quantity behind it. Pegging is orthogonal: you can have a visible peg order or a hidden peg order. The two features address different problems (visibility vs. repricing).

<div class="wiki-seealso">

### Closely related
- [Limit Order](/wiki/limit-order/) — fixed-price order; peg is dynamic variant
- [NBBO](/wiki/nbbo/) — national best bid/ask; common peg reference
- [Hidden Order](/wiki/hidden-order/) — partial visibility; can be combined with pegging
- [Market Order](/wiki/market-order/) — opposite: buy/sell at any price
- [Order Types](/wiki/order-types/) — taxonomy of order structures

### Wider context
- [Market Maker](/wiki/market-makers/) — primary users of peg orders
- [Scalping](/wiki/scalping/) — intraday strategy relying on dynamic orders
- [Regulation NMS](/wiki/reg-nms-adoption/) — framework governing order handling
- [Flash Crash](/wiki/flash-crash-2010/) — risk from erroneous reference prices
- [Order Routing](/wiki/order-routing-logic/) — how orders reach venues

</div>

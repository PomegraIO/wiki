---
title: "Midpoint Peg vs Primary Peg: Key Differences"
description: "Midpoint peg and primary peg orders are alternative algorithms that adjust order prices dynamically; midpoint pegs target half the spread, primary pegs follow the best bid or ask."
keywords:
  - midpoint peg order
  - primary peg order
  - peg order comparison
  - dynamic order types
  - spread execution strategy
image: /svg/trading.svg
---

*A **midpoint peg** order and a **primary peg** order are both algorithmic orders that reprice themselves dynamically as the market moves, but they target different price levels. A midpoint peg sets its limit price at the midpoint between the current [bid-ask spread](/bid-ask-spread/), while a primary peg follows the best existing bid or ask on the opposite side of the book. Each suits different trade sizes, urgency levels, and risk tolerances.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Peg Order Types — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two dynamic repricing algorithms with different spread-capture and queue-position tradeoffs.</div>

|   |   |
|---|---|
| **Midpoint peg pegs to** | Midpoint of bid-ask spread |
| **Primary peg pegs to** | Best bid (for sell orders) or best ask (for buy orders) |
| **Spread capture** | Midpoint = half the spread; Primary = none to full spread |
| **Queue position** | Midpoint gets fresh queue each repricing; Primary stays in queue |
| **Best for** | Midpoint: patient, size-sensitive trades; Primary: minimizing impact |
| **Worst case** | Midpoint can miss entirely; Primary can be walked through |
| **Regulation** | SEC Rule 10b-5, Reg SHO compliance required for both |

</aside>

## How Midpoint Peg Works

A midpoint peg order continuously calculates the midpoint between the national best bid and national best offer ([NBBO](/bid-ask-spread/)) and sets its limit price at that level. If the bid is $100.50 and the ask is $100.60, a midpoint peg buy order will peg at $100.55. If the bid moves to $100.51, the peg moves to $100.555 (or rounds to $100.56, depending on the order entry system). The order reprices dynamically to track the market's midpoint in real time.

Midpoint peg orders do not interact with the [market maker](/market-maker-trading/) community at all. They sit passively inside the spread, never crossing it, and will only execute if an incoming order on the opposite side matches at the midpoint or better. This means the order has zero chance of improving the quoted spread—it is invisible to the market maker and adds no pressure to move prices.

The advantage is that a midpoint peg maximizes the chance of filling at a price precisely between best bid and ask, capturing half the spread in your favor. The disadvantage is that if volume never hits the midpoint (because the market tightens or trades occur above/below midpoint), the order may not fill at all during the session.

## How Primary Peg Works

A primary peg order continuously reprices to match the best bid or ask on the side of the book opposite the order's direction. A primary peg buy order pegs to the current national best ask. A primary peg sell order pegs to the national best bid. As the best ask moves, the buy order reprice upward to match; as the best bid moves down, the sell order reprices downward.

Primary peg orders sit at the top of the passive side of the book, behind any existing [limit orders](/limit-order/) at that price, but ahead of new orders that arrive after the peg order is entered. If the order is in the queue and new selling arrives that crosses the peg price, the order will execute. If the market tightens and the ask (for a buy order) moves higher, the primary peg reprice upward to follow it.

Primary peg orders do not improve the spread either; they sit at the existing best bid or ask and wait for crossing flow. However, because they match the side of the book offering the best price, they are more likely to execute than midpoint pegs in liquid markets.

## Spread Capture and Queue Position

The key operational difference is spread capture and queue dynamics. A midpoint peg captures zero spread on the side you are buying/selling against—you get filled at the midpoint, which is half the spread better than the offer (for a buy) or better than the bid (for a sell). But you capture nothing on the other side because midpoint pegs never cross.

A primary peg captures the full spread if you are buying at the ask or selling at the bid. Your primary peg buy order at the ask means you are paying the full ask price, not split improvement. In exchange, primary pegs have a meaningful chance to execute because they are at the price where passive sellers are willing to trade.

Queue position is also different. Midpoint pegs, because they continuously reprice, effectively reset their queue position each time the midpoint changes. A new buy order that enters at the same newly calculated midpoint price will jump ahead in the queue. Primary pegs, by contrast, sit in the queue at the best bid/ask and maintain their position as long as that price level remains best—they have time priority.

## Suitability by Trade Size and Urgency

For very large trades where minimizing market impact is the dominant goal, primary peg orders work better. A large passive order at the best bid will absorb natural crossing flow without moving the market; it achieves size while respecting the existing book structure. It may take longer to fill, but when it does, it does not broadcast urgency or move prices against you.

Midpoint pegs suit smaller, more patient trades where the goal is to achieve execution at a price that does not make any market maker worse off. If you have a $500,000 position and are willing to wait a full trading day or longer to fill without affecting price discovery, a midpoint peg is ideal. The risk is that if volatility is low or the security is thinly traded, the order may not fill at all.

For traders with time constraints (intraday or algorithmic mandates with deadlines), primary pegs are more reliable because they sit at a queue position where execution is likely within the time window. Midpoint pegs are more of a "set and forget" mechanism for patient limit order flow.

## Interaction with Crossing Networks and Venues

Midpoint peg orders gained popularity after the rise of alternative trading systems (ATS) and [dark pools](/alternative-trading-system/) that match orders at the midpoint as a fairness mechanism. Some venues, like CBOE's midpoint matching, exclusively execute at midpoint. A trader sending a midpoint peg to a primary exchange but wanting to access an ATS's midpoint crossing may need to submit both a primary-exchange order and a separate ATS order.

Primary peg orders, by contrast, are venue-neutral in intent. They work on any exchange or ATS and will follow the national best bid/ask as long as the order is active. Some execution algorithms specifically blend midpoint and primary peg logic—e.g., peg to the midpoint if volume is light, then switch to primary peg if order size is not filling.

## Regulatory and Operational Considerations

Both order types are subject to SEC Rule 10b-5 and Regulation SHO short-sale rule compliance. Brokers must ensure that midpoint pegs are not being used as a cover for late reporting (they must be genuinely passive) and that primary pegs do not violate short-sale uptick rule requirements if the stock is on the SHO list.

Some brokers disable midpoint peg orders entirely during periods of wide or unstable spreads, because the midpoint calculation becomes unreliable. Primary pegs are more robust in choppy markets because they simply follow the published best prices.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the core price concept that peg orders reference
- [Limit Order](/limit-order/) — the traditional passive order that peg orders automate
- [Market Maker Trading](/market-maker-trading/) — the counterparty role in peg order execution
- [Market Order](/market-order/) — the aggressive alternative to patient pegging
- [Alternative Trading System](/alternative-trading-system/) — venues that use midpoint matching

### Wider context

- [Price Discovery](/price-discovery/) — mechanism that peg orders support
- [Execution Risk](/execution-risk/) — the risk that peg orders help mitigate
- [Market Timing](/market-timing/) — strategy context for order-type selection
- [Algorithmic Trading](/algorithmic-trading/) — framework encompassing peg orders

</div>

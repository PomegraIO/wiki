---
title: "Pegged Order Types"
description: "Pegged order types automatically track the best bid or ask price (NBBO), adjusting in real time—including midpoint-peg, primary-peg, and market-peg—to reduce adverse selection and market impact."
keywords:
  - pegged order types trading
  - midpoint peg order
  - primary peg order
  - market peg order
  - nbbo tracking
---

*A **pegged order** is a [limit order](/limit-order/) that automatically adjusts its price to track the National Best Bid and Offer (NBBO) or another reference price in real time. Instead of sitting at a fixed limit price, a pegged order moves with the market, reducing the risk that you are "picked off" by adverse price movement and improving your odds of execution without sacrificing price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pegged Order Types — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Orders that hunt the market: adjust in real time to stay relevant.</div>

|   |   |
|---|---|
| **Core feature** | Limit price auto-adjusts to track NBBO or reference price |
| **Midpoint peg** | Pegged one tick inside the best bid or ask, at the midpoint |
| **Primary peg** | Pegged to the best price on the primary market |
| **Market peg** | Pegged to the NBBO with an offset (one tick away) |
| **Advantage** | Reduced adverse selection risk; dynamic pricing without manual adjustment |
| **Use case** | Passive accumulation, hedging, avoiding queue risk |

</aside>

## The three main peg types: midpoint, primary, and market

Exchanges and brokers offer several pegged order variants, each tracking a different reference price.

**Midpoint peg** places your order one tick inside the best bid or ask, at the exact midpoint between them. If the best bid is $100.00 and the best ask is $100.04, the midpoint is $100.02. A midpoint-peg buy order lands at $100.02, not $100.04 (the ask). As the market moves and the [bid-ask spread](/bid-ask-spread-and-execution-cost/) shifts, your order automatically adjusts. If the spread tightens to $100.01–$100.02, your midpoint-peg buy adjusts down to $100.015. If the spread widens, your order adjusts up. This creates a "best of both worlds" dynamic: you get the benefit of a more aggressive price than the ask without the risk of being stationary in a moving market.

**Primary peg** ties your order to the best price on a specified primary market (usually the NYSE for equities). This is useful for traders who want to ensure they are not getting stale quotes from slower market data feeds. If the NYSE bid is $100.01 and a regional exchange's bid is $100.00, a primary-peg order would peg to the NYSE $100.01, ignoring the slower regional quote.

**Market peg** pegs your order to the current NBBO with a fixed offset. You specify an offset (e.g., one tick), and the order automatically maintains that offset relative to the best bid or ask. A buy order with a market peg of minus-one-tick will sit one tick below the best ask. As the ask moves, so does your order. This is more flexible than midpoint-peg because you control the offset.

## How pegged orders reduce adverse selection risk

Without pegging, if you place a buy limit at $100.00, you are betting that $100.00 will remain competitive. If the market moves up and the best ask is now $100.10, your $100.00 bid becomes stale and will not execute. You end up chasing the market manually or giving up.

A midpoint-peg order solves this by continuously re-pricing itself. As the market ticks up, your order ticks up with it, always sitting at the midpoint. You no longer risk being left behind by a moving market. You also no longer risk being "picked off"—a term that describes what happens when your static limit order executes right before the market moves sharply against you.

**Example.** You want to accumulate shares of a stock, and you place a buy limit at $100.00. The market is bid $99.90, ask $100.10. Your order sits at $100.00. A seller crosses at your price, and you fill 1,000 shares. But one second later, bad news hits and the stock falls to $98.00. You were picked off: you bought at the worst possible time because your static limit couldn't adjust. A midpoint-peg order would have kept pace with that market move, staying at the midpoint, and likely would not have filled at all—protecting you from being picked off.

Pegged orders are thus popular with passive accumulators and [market makers](/market-maker-trading/) who want to earn small price improvements without bearing the risk of a stale quote.

## The trade-off: reduced fill probability vs. price improvement

Pegged orders come with a cost: they are less likely to fill quickly than a static aggressive limit order.

A static buy limit at the best ask will fill immediately if any volume is available (assuming no [queue priority](/order-queue-priority-rules/) rules or other market conditions delay it). A midpoint-peg buy, sitting at the midpoint between bid and ask, will fill only if prices move in your direction—i.e., if the bid rises to meet your midpoint price or the ask drops. This can take seconds or longer.

If you are in a hurry to accumulate a position, a midpoint-peg order might leave you hanging. If you are willing to wait and want to minimize market impact and avoid being picked off, a midpoint-peg order is ideal.

This trade-off is the core strategic decision: speed and fill certainty (static aggressive limit) versus price and adverse-selection protection (pegged order).

## Pegged orders and market structure

Pegged orders became popular with the rise of electronic trading and fragmentation across multiple venues. When U.S. stocks traded on a single exchange, the need for continuous price adjustment was less acute. Once trading fragmented across the NYSE, NASDAQ, regional exchanges, and [alternative trading systems](/alternative-trading-system/), traders using stale data or slower order routing risked being picked off by counterparties who had fresher quotes.

Pegged orders were introduced (and are now mandated by Regulation SHO and the SEC's Regulation National Market System) to allow traders to automatically stay compliant with the NBBO and reduce predatory order-picking practices.

Most major brokers and trading venues now support midpoint-peg and market-peg orders as standard features. They are particularly common in equities; futures and FX venues support variants but with different naming and mechanics.

## Practical use cases

**Passive liquidity providers.** A trader who wants to post liquidity passively—earning small price improvements without directional bets—uses pegged orders to stay competitive without manual repricing. A market maker might post midpoint-peg buy and sell orders that auto-adjust all day, harvesting the spread on incoming market orders.

**Large block traders.** A trader with a large order to accumulate or unwind uses pegged orders (often hidden via reserve quantity rules) to feed the market slowly and avoid market impact. Each sub-order is pegged to the midpoint or NBBO, ensuring the trader always gets fair value without aggressive pricing that would move the market.

**Hedgers and multi-legged traders.** If you are executing a spread trade (e.g., long one stock, short another) and need both legs filled without directional price movement, pegged orders on both legs ensure you maintain a stable spread between them.

**Retail investors using limit orders.** A retail investor who wants the price improvement of a limit order but fears being stale can use a market-peg order with a conservative offset (e.g., one or two ticks inside the market). The order will fill only if the market moves in the investor's favour, and the continuous repricing ensures the order stays relevant.

## Limitations and special cases

Pegged orders have constraints. Most obviously, they cannot fill at a price worse than their peg, by definition. If you have a midpoint-peg buy and the market is bid $100.01, ask $100.03 (midpoint $100.02), your order sits at $100.02. If the best ask moves down to $100.01, your peg automatically moves to $100.01, but it cannot execute at the old $100.02 price; the best ask is now $100.01, and your peg follows, so you fill at $100.01. This is often desirable (you get the better price), but it means you may miss a fill if the market moves against you.

Additionally, in very wide or volatile markets, pegged orders can be at a significant disadvantage. If the spread widens to $100.00–$100.20, a midpoint-peg order sits at $100.10, far from both the bid and the ask. Large market moves can result in zero fills while a static aggressive limit order would have at least captured some shares.

Pegged orders are also complex to implement for exchanges and brokers, requiring real-time NBBO data feeds and continuous repricing logic. Some venues or securities with sparse data or slow feeds may not support pegged orders or may have latency in repricing.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — an order that executes only at a specified price or better
- [Bid-Ask Spread as an Execution Cost](/bid-ask-spread-and-execution-cost/) — how spread width affects your execution and pricing
- [Order Queue Priority Rules in Exchange Matching Engines](/order-queue-priority-rules/) — how queue position determines fill probability
- [Market Order](/market-order/) — an order that fills immediately at the best available price
- [Fill-or-Kill Order Explained](/fill-or-kill-order-explained/) — all-or-nothing execution instruction

### Wider context

- [Market Maker](/market-maker-trading/) — trader who profits from continuously posting bids and offers
- Market Impact — the effect of your order on market prices
- [Stock Exchange](/stock-exchange/) — venue that matches orders and enforces market structure rules
- [Algorithmic Trading](/algorithmic-trading/) — automated execution using order types and price logic

</div>

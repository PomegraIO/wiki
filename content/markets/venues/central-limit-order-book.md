---
title: "Central Limit Order Book"
description: "The electronic ledger at an exchange core that maintains all resting buy and sell orders ranked by price and time."
keywords:
  - limit order book
  - order book depth
  - price-time priority
  - market microstructure
  - exchange trading
  - bid-ask spread
image: "/svg/markets.svg"
---

*A **central limit order book** (CLOB) is the electronic ledger maintained at the heart of a stock or derivatives exchange that stores every outstanding buy and sell order, ranked first by price and then by submission time. It is the engine that converts unmatched orders into a transparent, real-time display of supply and demand—and ultimately sets the price at which the next trade executes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Central Limit Order Book — how exchanges match trades</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark representing market venues and trading infrastructure." />

<div class="wiki-infobox-caption">The electronic spine of modern equity and futures markets.</div>

|   |   |
|---|---|
| **What it is** | Electronic queue of unmatched buy and sell orders, ranked by price and arrival time |
| **Also called** | Order book, CLOB, electronic communication network (partial) |
| **Maintained by** | Exchange (e.g., [NYSE](/new-york-stock-exchange/), [Nasdaq](/nasdaq/)) or alternative trading system |
| **Matching rule** | Price-time priority: best bid/ask first; within price level, earliest order first |
| **Visible to** | Market participants in real time (price, volume); individual order IDs typically hidden |
| **Core output** | [Bid-ask spread](/bid-ask-spread/), [market depth](/order-book-depth/), execution price |

</aside>

## How the order book stores and matches orders

At any instant, a CLOB holds two lists: one of live buy orders (bids) sorted from highest price downward, one of live sell orders (asks) sorted from lowest price upward. When a new order arrives, the exchange's matching engine checks whether it crosses the spread—that is, whether the new buy order price meets or exceeds the lowest ask, or the new sell order price meets or falls below the highest bid. If it does, one or more resting orders are executed at the resting order's price (not the arriving order's price). If not, the new order is added to the book at its stated price level, ranked by arrival time against any other orders at that same price.

This price-time priority is not accidental. It encourages participants to quote tight spreads (because a better price gets priority) and rewards early submission (because an order submitted at 09:45:03 executes before an identical order submitted at 09:45:04). The rule is transparent and mechanical, which is precisely why centralized exchanges adopted it: it removes discretion and builds confidence that execution is fair.

## The market microstructure beneath the price

The order book is where the idea of a market price actually lives. Before modern electronic systems, a floor trader or market maker would maintain an implicit mental inventory of buy and sell interest; now, that interest is explicit, digitized, and visible to all. The highest bid and lowest ask form the [spread](/bid-ask-spread/). The depth—the cumulative volume available at successive price levels—is a barometer of liquidity. A thin book signals risk; orders placed during low-volume hours may move prices sharply. A thick book suggests easy entry and exit.

This visibility has a discipline effect. When [market makers](/market-maker-trading/) or dealers quote on a CLOB, they know their bids and asks will sit in a public queue, open to mechanical matching at any moment. That transparency typically tightens spreads compared to over-the-counter markets, where dealers maintain private prices and quotes are less frequent. Conversely, the mechanical matching rule creates pathologies: during stress, when many participants want to sell and few want to buy, the CLOB book can become severely imbalanced, and prices can gap sharply.

## Variations across venues and asset classes

Not all electronic trading uses a single central limit order book. A [stock exchange](/stock-exchange/) like the NYSE or Nasdaq maintains one CLOB per listed security. A [futures exchange](/futures-contract/) maintains one per contract. But the equity markets also include [alternative trading systems](/alternative-trading-system/) (such as dark pools and electronic communication networks) that operate alongside the exchange CLOB. These alternatives may use their own private order books, which are not visible to the broader market—a feature attractive to large traders who wish to move without signaling intent, but controversial because it fragments market depth and complicates price discovery.

Derivatives markets introduce further variation. An options exchange will hold a CLOB for each [strike price](/strike-price/) and [expiration date](/expiration-date/). A [bond](/bond/) market, traditionally opaque and dealer-centric, has slowly adopted electronic platforms with central order books, though less uniformly than equities. Fixed-income CLOBs tend to be shallower and less transparent than equity books, reflecting the fragmentation of the bond market into thousands of distinct issuances.

## Real-time data and market participants

The order book depth—showing volume at each price level several ticks around the best bid and ask—is published by exchanges in real time. Most brokers and traders receive this "Level 2" data (best prices and aggregated volume at each level) and some subscribe to "Level 3" (full book with individual order identities, where permitted). High-frequency trading algorithms use this data to infer order flow patterns, predict future price moves, and decide when to place or cancel their own orders within microseconds.

The CLOB is thus simultaneously a neutral matching utility, a source of real-time market information, and a competitive battlefield. Participants monitor which orders are sitting in the book, how thick or thin the depth is at each level, and how quickly orders are being added and cancelled. Orders that are placed and then immediately cancelled (a practice called "order stuffing" or "layering") are used strategically to move prices without taking risk—a tactic regulators now police closely. The apparent simplicity of price-time priority masks considerable strategic complexity.

## The boundaries of order book transparency

One feature of the CLOB that is often overlooked is what it does *not* show. The exchange publishes the best bid and ask prices and cumulative volume at each level, but not necessarily the identities of the traders behind each order. It also does not typically reveal orders that are hidden or "icebergs"—large orders placed in tranches so that only a visible portion is shown at any time, the rest revealed only as the visible part executes. These tools allow large traders to place demand without moving the price before they have finished buying.

Regulators require that exchanges maintain fair and orderly markets. This has meant setting rules for order book operations: minimum price increments (tick sizes), limits on order cancellation rates, safeguards against simultaneous execution (to prevent traders from gaming the timing), and auctions to handle order imbalances at market open and close. The design of the order book is thus a blend of technology and regulation, each reinforcing the other to sustain confidence in the fairness of execution.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the gap between the best buy and sell prices in the order book
- [Market maker](/market-maker-trading/) — dealer who posts orders in the CLOB to earn the spread
- [Alternative trading system](/alternative-trading-system/) — private venue operating alongside the central exchange
- [Price discovery](/price-discovery/) — the process by which order book matching sets true market prices
- [Order routing](/order-routing-network/) — infrastructure that directs incoming orders to the CLOB
- [Stock exchange](/stock-exchange/) — the venue that maintains the central order book

### Wider context

- [Stock market](/stock-market/) — ecosystem of exchanges and trading venues
- [Market capitalization](/market-capitalization/) — value derived from stock prices set via order book matching
- [Systemic risk](/systemic-risk/) — risks from order book imbalances and flash crashes
- [Securities and exchange commission](/securities-and-exchange-commission/) — regulator of order book fairness rules

</div>
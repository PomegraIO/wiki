---
title: "Limit Order Book"
description: "The electronic ledger of pending buy and sell orders, ranked by price and time, that exchange systems use to match trades."
keywords:
  - limit order book
  - order book
  - buy-side order book
  - sell-side order book
  - price formation
  - order matching
image: /svg/trading.svg
---

*Every stock exchange maintains an electronic queue of unexecuted orders waiting to be filled. This **limit order book** is the engine of [price discovery](/price-discovery/) and continuous trading. Buy orders and sell orders sit in the book, ranked by price and arrival time, until they meet a matching order or are cancelled. The spread between the best bid and best ask in the book becomes the [market price](/stock-market/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Limit Order Book — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The visible ledger where buy and sell orders queue and prices are set.</div>

|   |   |
|---|---|
| **What it is** | Ranked queue of unmatched [limit orders](/limit-order/) on an exchange |
| **Sides** | Bid side (buyers) and ask side (sellers) |
| **Depth** | Typically shows top 5–20 levels; full book may be deeper |
| **Matching rule** | [Price-time priority](/price-priority-time-priority/) — better price first, then earliest arrival |
| **Price formation** | Best bid and ask form the top-of-book; the "spread" between them |
| **Transparency** | Most of book is public; hidden orders and reserve orders may not display |
| **Updates** | Real-time; books refresh multiple times per second during active trading |

</aside>

## The two sides of the book

The limit order book has two halves. The **bid side** (or buy side) shows all pending offers to purchase: "I will buy 1,000 shares of Apple at $150.00." The **ask side** (or sell side) shows all pending offers to sell: "I will sell 500 shares at $150.05." These orders sit in the book until they are filled by a counterparty or cancelled by the order's owner.

Within each side, orders are sorted first by price. All buy orders at $150.00 are "better" (higher) than buy orders at $149.99, so they appear above in the queue. On the ask side, all sell orders at $150.05 are better (lower) than sell orders at $150.10. The gap between the highest bid and the lowest ask is the [bid-ask spread](/bid-ask-spread/)—the cost of an immediate execution via a [market order](/market-order/).

## Price-time priority in the book

Within each price level, orders queue by arrival time. If two traders both place buy limit orders at $150.00, the one who arrived first sits ahead in the queue and will be filled first when a seller's order arrives at that price. This rule is called [price-time priority](/price-priority-time-priority/) and is standard on most US equity exchanges under [Reg NMS](/reg-nms-order-protection-rule/).

The fairness of price-time priority is one reason why traders care about order routing and venue choice. An order that arrives at the NYSE's book at exactly the same price and time as an order on NASDAQ would be equally positioned on each venue. But because order routing takes tens or hundreds of microseconds, arriving "first" requires careful infrastructure and broker practices. High-frequency traders have historically invested heavily in low-latency connectivity to improve their position in the queue.

## How orders fill

When a buyer places a [market order](/market-order/) to buy 100 shares, the exchange's matching engine automatically fills it against the best available sell orders. The 100 shares fill against the seller at the best ask price. If that seller's standing order is only for 50 shares, the buy order consumes those 50 and then looks to the next price level, filling another 50 at a slightly higher ask. If the buyer wants even more, the order continues to consume inventory down the ask side.

Similarly, when a seller places a market order to sell, it fills against the best bids first. This automatic matching ensures that every transaction takes the best available price at the time of execution—unless the buyer or seller explicitly uses a [limit order](/limit-order/) to specify a price and is willing to wait for it.

## Visible and hidden liquidity

Most limit orders in the book are displayed publicly. A trader with a market data feed can see the top of the book—the 5 to 20 best bid and ask prices and the sizes at each level. This visible liquidity helps price discovery and is republished through the consolidated tape.

However, not all orders are fully visible. An order can carry a "reserve" or "hidden" flag, which tells the exchange to show only a fraction of the order size to other traders. This might be 500 shares on display while 5,000 sit in reserve. As the visible portion fills, more of the reserve is automatically displayed. Traders use reserve orders to reduce the market impact of very large positions—if you dump 10,000 shares into the visible book all at once, other traders know a large seller is present and prices may move against you.

## Order book depth and liquidity

The "depth" of a book is how much volume sits at each price level. A stock with a deep book at the top few levels is very liquid—a large market order can be filled with minimal impact. A stock with a thin book might only have 1,000 shares at the best ask; a 100,000-share market order would have to sweep down many price levels and incur substantial slippage.

Market participants track order book depth as a signal of liquidity and volatility. A sudden collapse in depth—all those resting limit orders disappearing—often signals that traders expect a price move and are pulling orders to avoid being hit. Conversely, an order book that deepens during uncertainty is a sign of buyers and sellers willing to be patient.

## The role of algorithmic trading and HFT

Algorithmic traders and [high-frequency traders](/algorithmic-trading/) have become major participants in the limit order book. They use statistical models to predict which orders will fill next and position their own orders to capture small spreads. Most of the volume in the modern order book is driven by algorithms, not by fundamental traders.

This has changed the character of the book. Orders appear and disappear in milliseconds. The same trader might be at the top of the queue one moment and evaporate the next. From the perspective of a retail trader placing a [limit order](/limit-order/) at 9:30 a.m., the book is a chaotic environment dominated by sophisticated, fast players. The position of your order in the queue might matter less than it did decades ago because the algorithms trading around you are also quick to cancel and re-quote.

## Transparency and market data

Exchanges publish a real-time feed of top-of-book data (the best bid, best ask, and sizes at those prices) to all market participants for a nominal fee. Deeper levels of the book may be published with a slight delay or only to subscribers paying a premium. This asymmetry in information access is debated: some argue it's fair compensation to exchanges for operating the infrastructure; others contend it gives large traders an unfair edge.

The SEC and exchanges have also wrestled with whether hidden orders—reserve orders and the like—should be more transparent. If a significant amount of liquidity is hidden, the published book does not reflect the true state of supply and demand, and it can mislead other traders about where real liquidity sits.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — the order type that populates the book
- [Price-Time Priority](/price-priority-time-priority/) — the matching rule within the book
- [Market Order](/market-order/) — executed against the book
- [Bid-Ask Spread](/bid-ask-spread/) — the gap at top of book
- [Price Discovery](/price-discovery/) — driven by order book dynamics
- [Order Internalization](/order-internalization/) — orders not routed to the book

### Wider context

- [Stock Exchange](/stock-exchange/) — operates the order book
- [Reg NMS Order Protection Rule](/reg-nms-order-protection-rule/) — governs matching rules
- [Market Maker](/market-maker-trading/) — often tops the book with continuous quotes
- [Algorithmic Trading](/algorithmic-trading/) — dominates modern order flow
- [Broker](/broker/) — routes client orders into the book

</div>

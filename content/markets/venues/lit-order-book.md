---
title: "Lit Order Book"
description: "A publicly visible central limit order book that aggregates and displays all outstanding bids and offers for a security in real time."
keywords:
  - order book
  - limit order
  - market microstructure
  - price discovery
  - central limit order book
image: /svg/markets.svg
---

*A **lit order book** is a real-time, publicly viewable record of all outstanding buy and sell orders (bids and offers) for a security on a particular [exchange](/stock-exchange/). It is the foundation of [price discovery](/price-discovery/) on modern [stock exchanges](/stock-exchange/) — the mechanism through which competing market participants express their willingness to transact at specific prices.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lit Order Book — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure." />

<div class="wiki-infobox-caption">The transparent record that shows supply and demand at every price level.</div>

|   |   |
|---|---|
| **Core function** | Displays all visible buy and sell orders in real time |
| **Opposite** | Dark pool or [over-the-counter market](/over-the-counter-market/) (orders not visible pre-execution) |
| **Price formation** | Best bid and offer (BBO) sets the [current price](/intrinsic-value/) |
| **Order execution** | [Limit orders](/limit-order/) matched by price priority, then time priority |
| **Visibility** | Public, disseminated to all traders through data feeds |
| **Common venues** | [NYSE Arca](/nyse-arca/), [NASDAQ](/nasdaq/), [IEX](/iex-investors-exchange/), most national exchanges |

</aside>

## How the lit order book works

The lit order book is a ledger. On the buy (bid) side, it lists every offer to purchase at each price, stacked from highest bid down. On the sell (offer) side, it lists every offer to sell at each price, stacked from lowest offer up. The gap between the highest bid and the lowest offer is the [bid-ask spread](/bid-ask-spread/) — the transaction cost an investor pays to buy or sell immediately.

When you submit a [limit order](/limit-order/) — a directive to buy or sell only at a specific price — it is added to the book if no matching orders exist at that price or better. Your order then waits, visible to all other market participants, until someone agrees to trade with you or you cancel it. When a new order arrives that matches an existing order on the opposite side, the two orders are executed at the price of the order that was posted first (the "maker"), not the price of the incoming order (the "taker").

This sequencing — called [time priority](/time-value/) — is the operating principle of a continuous-auction limit order book. It rewards patience: if you post a bid to buy at $50 before anyone else, and the price later rises to $50, your order executes before a newer bid at the same price. This encourages liquidity provision, because market makers and patient traders know their position in the queue is protected.

The best bid and best offer (BBO) — the highest bid and lowest offer currently on the book — define the [current price](/intrinsic-value/) of the security and the effective transaction cost. If you submit a [market order](/market-order/) (a command to buy or sell immediately at any price), you will execute at or near the BBO.

## Why "lit" matters

The term "lit" emphasizes that the order book is transparent. Everyone sees the same orders at the same time. This transparency serves several purposes:

*Price discovery.* Aggregated bids and offers across the entire order book, from many competing traders, reveal the collective estimate of the security's fair value. No single trader sets prices; instead, prices emerge from the [market mechanism](/price-discovery/). This process is particularly powerful when the order book is deep — when many orders sit at multiple price levels, not just at the BBO.

*Fair execution.* Because orders are matched by price and time priority, no hidden queue exists. A retail investor's limit order to sell 100 shares at $50 will execute ahead of an institutional order to sell 10,000 shares at $50 if the retail order was posted first. This transparency reduces the risk that a trader is being discriminated against by a hidden system.

*Market quality metrics.* The depth and shape of the lit order book provide real-time signals of market liquidity and volatility. A wide spread and thin depth suggest uncertain pricing; a tight spread and thick book suggest confidence and active trading.

## The lit order book vs. dark pools

Not all trading happens on lit order books. [Alternative trading systems](/alternative-trading-system/) and dark pools — venues that do not publicly display orders before execution — have grown substantially since the early 2000s. A dark pool is attractive to large institutional traders who want to conceal their order size (to avoid moving the market against themselves) or to avoid [market maker](/market-maker-trading/) take.

However, dark pools introduce a tradeoff. By definition, they reduce price transparency. Orders in a dark pool cannot contribute to price discovery on the lit market; they are matched internally or against a "midpoint" price derived from the lit order book. In extreme cases, if too much volume migrates to dark pools, the lit order book becomes thin and prices become less reliable.

Regulators in the US and Europe have imposed limits on dark trading (sometimes called "dark pool caps") to preserve the role of lit venues in price discovery. Most US regulation requires that a certain percentage of trading in a security must occur on lit venues — typically around 65–80% depending on the security and venue.

## Order book depth and market stress

The structure of the lit order book — how many orders sit at different price levels — matters enormously for market resilience. A "thick" order book with substantial volume at multiple price levels can absorb large trades without large price moves. A "thin" book, with orders only at the BBO, can experience sudden price swaps if a large market order arrives.

During market stress — such as a flash crash or panic sell-off — the lit order book can paradoxically become less useful as a price discovery mechanism. [Market makers](/market-maker-trading/) may withdraw their orders, spreads widen dramatically, and prices become stale. Some exchanges and venues have responded by introducing [periodic auction venues](/periodic-auction-venue/) as a complement to the continuous lit order book, allowing traders to batch orders during volatile periods and agree on a midpoint price rather than chase a moving best bid-offer.

## The role of technology and speed

Modern lit order books are electronic and automated. Orders are submitted in milliseconds, and matching engines process millions of transactions per second. This speed has reduced [trading costs](/cost-of-equity/) substantially and increased the accessibility of liquid markets to retail investors.

However, speed has also created a new form of inequality: latency arbitrage. A trader collocated at the [exchange](/stock-exchange/) with a faster connection can see orders and trade before distant traders. [IEX](/iex-investors-exchange/) famously addressed this by adding a 350-microsecond intentional delay (a speed bump) so that all traders experience the same latency to the matching engine. Most other lit venues, including [NYSE Arca](/nyse-arca/) and [NASDAQ](/nasdaq/), allow latency advantages, arguing that competition for speed is a legitimate and efficient form of competition.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — the order type displayed on the lit order book
- [Market order](/market-order/) — an order that executes against the lit book immediately
- [Bid-ask spread](/bid-ask-spread/) — the cost visible in the order book
- [Price discovery](/price-discovery/) — how lit order books reveal fair value
- [Market maker (trading)](/market-maker-trading/) — the liquidity providers who populate the order book
- [Over-the-counter market](/over-the-counter-market/) — trading not on a lit exchange
- [Alternative trading system](/alternative-trading-system/) — dark pools and other venues that compete with lit books

### Wider context

- [Stock exchange](/stock-exchange/) — venues that operate lit order books
- [IEX (Investors Exchange)](/iex-investors-exchange/) — an exchange built around a lit order book with a speed bump
- [NYSE Arca](/nyse-arca/) — a major venue with a lit order book for equities and ETFs
- [Periodic auction venue](/periodic-auction-venue/) — a complement to continuous lit order books

</div>
---
title: "Order Book Mechanics: How Bids and Offers Queue Before a Trade"
description: "Learn how limit orders queue in a central order book using price-time priority, how market orders walk through available liquidity, and why order placement matters."
keywords:
  - order book mechanics
  - how an order book works
  - price-time priority
  - limit order queue
  - market order execution
  - order matching
---

*An **order book** is a live queue of buy and sell [limit orders](/limit-order/), sorted by price and then by time of arrival. When you submit a [market order](/market-order/), it walks through that queue — buying from the cheapest sellers or selling to the highest bidders — until your quantity is filled. The rules governing this queue, known as price-time priority, determine whether your order jumps the line or waits. Understanding order book mechanics reveals why microseconds matter, why crossing the spread costs money, and how [market makers](/market-maker-trading/) profit from the difference between what buyers and sellers are willing to pay.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Book Structure — Key Mechanics</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for financial markets." />

<div class="wiki-infobox-caption">The order book is the engine of modern price discovery.</div>

|   |   |
|---|---|
| **Price-Time Priority** | Best price first, then earliest arrival time within that price level |
| **Bid Side (Buy Orders)** | Highest prices at top; first to execute when a seller arrives |
| **Ask Side (Sell Orders)** | Lowest prices at top; first to execute when a buyer arrives |
| **Spread** | Difference between best bid and best ask; market makers earn this |
| **Order Types** | Limit (waits in book), Market (executes immediately), Stop-loss (triggered conditionally) |
| **Partial Fills** | Large market orders consume multiple price levels before completion |
| **Tick Size** | Minimum price increment; smaller ticks increase competition, widen spreads |

</aside>

## The Two-Sided Queue

Imagine Apple trading at 228.45 bid (buyers) and 228.46 ask (sellers). The bid side of the order book looks like this:

| Quantity | Price |
|----------|-------|
| 50,000 | 228.45 |
| 75,000 | 228.44 |
| 100,000 | 228.43 |
| 120,000 | 228.42 |

The ask (sell) side looks like this:

| Price | Quantity |
|-------|----------|
| 228.46 | 60,000 |
| 228.47 | 80,000 |
| 228.48 | 110,000 |
| 228.49 | 95,000 |

These queues exist simultaneously. At any moment, there are orders waiting to buy at 228.45 and orders waiting to sell at 228.46. The gap between them — one cent — is the [bid-ask spread](/bid-ask-spread/). When a new trade happens, it fills against one side or the other, and the queue reorders itself.

## Price-Time Priority Rules

**Price priority** is paramount: the highest bid and lowest ask always trade first. If you're a buyer, you'll only trade at 228.45 (the best ask) after all standing orders at that level are filled. You won't skip ahead to a seller offering 228.47.

**Time priority** breaks ties within a price level. If 50,000 shares are bid at 228.45 and another 75,000 are also bid at 228.45 but arrived two seconds later, the first order gets priority. When a seller arrives with 60,000 shares, the first 50,000 go to the early order, and the remaining 10,000 go to the second order. This incentivizes fast execution: arrive early, and you're first in line.

These rules are universal across US stock exchanges and most global markets. They exist to prevent chaos and ensure fairness. Without them, traders would have no way to predict order execution, and spreads would widen dramatically because uncertainty would demand a risk premium.

## Market Orders Walk Through the Book

Now suppose you place a market order to buy 100,000 shares of Apple. You don't specify a price — you just say "fill me now, whatever it costs." The exchange walks your order through the ask side:

1. First, 60,000 shares at 228.46 (fills completely)
2. Next, 40,000 of your remaining 100,000 shares at 228.47 (40,000 of the 80,000 available)
3. You're left with 60,000 shares still to buy at 228.48

Your average fill price: ((60,000 × 228.46) + (40,000 × 228.47) + (60,000 × 228.48)) / 100,000 = 228.468.

You've paid 2.8 cents per share more than the best ask (228.46). This slippage happens because your market order is large relative to the supply at the best price. In liquid stocks, slippage on a 100,000-share order might be a few cents per share. In illiquid stocks, it can be dollars per share — a brutal cost.

## Limit Orders and Queuing

A limit order is different. If you say "I will buy 100,000 shares at 228.44," your order sits in the queue at that price level. It doesn't execute immediately. Instead, it waits — potentially for hours or days — until a seller arrives at or below 228.44.

The advantage: you only pay 228.44, avoiding slippage. The cost: you might never fill. If Apple rallies and nobody wants to sell at 228.44, your order expires at the end of the trading day (or whenever you cancel it).

This is where time priority cuts deep. If two traders place a limit order to buy at 228.44 simultaneously, and then Apple falls below 228.44, the trader who clicked first gets priority. This is why [algorithmic traders](/algorithmic-trading/) obsess over latency — a 10-millisecond faster connection can put you ahead of thousands of other limit orders.

## What Happens When Orders Cross

When a new order arrives at a price where standing orders already exist, execution is automatic and instant. If the best bid is 228.45 and a seller arrives offering 228.46, the order book doesn't wait — it crosses them immediately at the best bid (228.45) or at a price determined by exchange rules (usually the maker's price, protecting the trader who arrived first).

If no standing orders exist at that price, the new order becomes a [market maker](/market-maker-vs-specialist/). It waits in the book, offering liquidity. This is why orders are sometimes called "passive" (waiting) or "aggressive" (crossing the spread immediately).

## Depth, Spreads, and Liquidity

A thick order book — one with large quantities at multiple price levels — signals liquidity. Traders can execute larger orders without significant slippage. A thin book signals illiquidity: spreads widen, and large orders cost more to fill.

Exchanges sometimes publish top-of-book data (the best bid, best ask, and quantity at each) for free. Full depth is usually proprietary or sold as market data. Market makers and algorithmic traders pay for that depth because knowing the full queue helps them predict how a large order will impact prices and where to place their own orders.

## Special Order Types

Some exchanges offer order types that modify the basic queueing rules:

**Stop-loss orders** don't enter the book immediately. They're triggered conditionally — if Apple falls to 228.00, the stop becomes a market order and executes. Stop orders are common among risk-averse investors but can cause sudden market dislocations if many stops trigger at once.

**Iceberg orders** let a trader hide their true quantity. A trader might post 10,000 shares publicly but queue 100,000 total, so when the visible 10,000 sells, another 10,000 appears. This preserves time priority while hiding the full position.

**Post-only orders** explicitly refuse to cross the spread; they'll be rejected if they would immediately execute. This forces the trader to be a [liquidity provider](/price-discovery/) and often qualifies for exchange rebates.

## Why This Matters to Investors

For retail investors, order book mechanics are mostly invisible. Your broker abstracts the complexity and gives you a simple interface: buy or sell, at market or at a limit price. But understanding the queue explains several phenomena you've likely noticed:

**Orders partially fill.** You buy 1,000 shares at a limit price, and only 600 fill. The remaining 400 entered the queue and might fill later or not at all, depending on whether enough sellers arrive at your price.

**Large orders move prices.** A 10,000-share market buy in a thin stock will walk through multiple price levels and cause a visible gap upward. The order book shows why: there simply aren't 10,000 shares available at the best ask.

**Spreads widen when volatility spikes.** As uncertainty increases, [market makers](/market-maker-vs-specialist/) pull back their quotes. The book thins, the spread widens, and market orders cost more to execute.

**Time-of-day matters.** Right at the open (9:30 AM ET), the book is often shallow because many orders haven't been entered yet. Spreads are wider. At 2:00 PM, after hours of trading, the book is deeper and spreads are tighter.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Maker vs Specialist](/market-maker-vs-specialist/) — Who provides liquidity and how they're regulated
- [Bid-Ask Spread](/bid-ask-spread/) — Why spreads exist and what determines their width
- [Limit Order](/limit-order/) — Placing an order with a price constraint
- [Market Order](/market-order/) — Executing immediately at whatever price is available

### Wider context

- [Price Discovery](/price-discovery/) — How orders and trades reveal fair value
- [Stock Market](/stock-market/) — Exchange structure and regulation
- [Algorithmic Trading](/algorithmic-trading/) — Automated order placement and execution
- [Trading Halt vs Suspension](/trading-halt-vs-suspension/) — How halts affect the order book
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Rules governing order execution

</div>

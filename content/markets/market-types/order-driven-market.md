---
title: "Order-Driven Market"
description: "Market structure in which buy and sell orders are posted publicly and matched to determine prices; the standard for stock exchanges."
keywords:
  - order-driven market
  - order book
  - central order book
  - price discovery
  - stock exchange
image: "/svg/markets.svg"
---

*An **order-driven market** is one where prices emerge from the continuous matching of publicly posted buy and sell orders. No single dealer sets prices; instead, traders post orders, and the [market](/stock-market/) automatically executes them when a buy order and sell order agree on price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order-Driven Market — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Transparency and automation replace dealer discretion.</div>

|   |   |
|---|---|
| **What it is** | Centralized venue where publicly posted orders determine prices |
| **Opposite** | [Quote-driven market](/quote-driven-market/) |
| **Typical venues** | Stock exchanges ([NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/)) |
| **Core mechanism** | Continuous order book; best bid and ask set the price |
| **Price discovery** | Direct—all available orders are visible |
| **Order types** | [Market orders](/market-order/), [limit orders](/limit-order/), others |

</aside>

## How the order book works

In an order-driven market, all traders can see a single, continuously updated list of pending buy and sell orders—the order book. The best bid (highest price anyone is willing to pay) and the best ask (lowest price anyone is willing to sell at) define the current [market price](/stock-market/). When a new order arrives, the exchange's matching engine compares it against existing orders and executes trades where prices cross.

If you enter a [limit order](/limit-order/) to buy 100 shares at $50, your order sits on the book at that price until either (1) the price falls and your order executes, or (2) you cancel it. If you enter a [market order](/market-order/), you accept the best available ask price and execute immediately. This automation is the signature of order-driven markets: no person decides whether to trade with you; the system does, based on rules.

The [bid-ask spread](/bid-ask-spread/) still exists—the gap between the best bid and best ask—but it is set by the orders on the book, not by a dealer's discretion. In a highly competitive stock, the spread might be a single penny; in a thinly traded stock, it can be much wider.

## Why stock exchanges use this structure

Order-driven markets excel where traders deal in standardized, frequently traded instruments: stocks, index futures, [currency pairs](/currency-risk/). Transparency is the key advantage. Everyone sees the same prices; there is no hidden dealing. Information is symmetric, and execution is mechanical and fair. This transparency builds trust and attracts large volumes of trading, which in turn tightens [bid-ask spreads](/bid-ask-spread/) and improves [liquidity](/liquidity-risk/).

Order-driven exchanges also require little human judgment. Matching rules are fixed—usually price-time priority, where the highest bid and lowest ask execute first, and within a price level, the earliest order executes first. Automation reduces costs and fraud risk.

## Order-driven versus quote-driven markets

A [quote-driven market](/quote-driven-market/)—common in bonds and foreign exchange—relies on dealers to post prices and stand ready to trade. You must ask a dealer for a quote; there is no public order book. The dealer profits from the [bid-ask spread](/bid-ask-spread/), and prices are less transparent.

In contrast, an order-driven market publishes all offers. You can see every bid and ask and post your own. Dealers (market makers) may participate, but they compete against ordinary traders on equal terms. The market itself, not the dealer, is the price setter.

This distinction matters. Order-driven markets favour informed traders and large volumes. Quote-driven markets suit non-standardized assets (like bonds) and are more forgiving of dealers who earn rents from the spread. Most modern stock exchanges are order-driven; most bond markets are quote-driven.

## Hybrid markets and market makers

Pure order-driven markets often employ [market makers](/market-maker-trading/) who post standing bids and asks on the order book. They compete with other traders to provide liquidity. If a stock has very few orders on the book, a market maker can widen their spread to reflect the low liquidity; if the book is thick with orders, they must tighten their spread to remain competitive. The order book retains full transparency, but market makers help ensure there is always someone ready to trade.

## Best execution and order types

In an order-driven market, traders can use many order types to manage execution risk. A [limit order](/limit-order/) guarantees price but not execution. A [market order](/market-order/) guarantees execution but not price. Conditional orders—such as stop-loss or iceberg orders—help large traders divide their intentions and avoid moving the price against themselves. [Algorithmic trading](/algorithmic-trading/) automates the execution of large orders by slicing them into small pieces and posting them over time.

## Information disadvantages in order-driven markets

Order-driven markets suffer from one subtle problem: front-running. Because orders are visible on the book, a trader with fast technology can see your order before it executes and place their own order ahead of it, profiting at your expense. Exchanges impose rules and latency floors to slow this down, but the risk persists. Quote-driven markets, where orders are private until agreed, face less front-running but more dealer opacity.

## See also

<div class="wiki-seealso">

### Closely related

- [Quote-Driven Market](/quote-driven-market/) — dealer quotes set prices
- [Limit Order](/limit-order/) — conditional order to buy or sell at a set price
- [Market Order](/market-order/) — order to buy or sell at the best available price
- [Market Maker (Trading)](/market-maker-trading/) — provides standing quotes for liquidity
- [Bid-Ask Spread](/bid-ask-spread/) — gap between best buy and sell prices
- [Two-Sided Market (Finance)](/two-sided-market-finance/) — platform must attract both buyers and sellers

### Wider context

- [Price Discovery](/price-discovery/) — process by which prices are determined
- [Algorithmic Trading](/algorithmic-trading/) — computer-driven trade execution
- [Stock Exchange](/stock-exchange/) — organized trading venue
- [New York Stock Exchange](/new-york-stock-exchange/) — major order-driven equity market
- [NASDAQ](/nasdaq/) — electronic order-driven stock exchange

</div>

---
title: "Central Limit Order Book vs Quote-Driven Market"
description: "Central limit order book (CLOB) vs quote-driven markets differ in how price is discovered: order-driven platforms match buyers and sellers; dealers quote bid-ask spreads."
keywords:
  - central limit order book
  - quote driven market
  - market structure
  - order matching
  - dealer markets
  - order-driven markets
image: /svg/trading.svg
---

*A **central limit order book** (CLOB) is an order-driven market where buyers and sellers submit limit orders that are matched against each other by a central exchange; a **quote-driven market** is a dealer market where licensed dealers post bid-ask quotes and act as intermediaries, buying and selling from their own inventory. The choice between them shapes how prices move, who profits from the spread, and which instruments thrive where.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CLOB vs Quote-Driven — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Two market structures, two paths to price discovery.</div>

|   |   |
|---|---|
| **CLOB: who matches orders** | Central exchange (computer, algorithm) |
| **Quote-driven: who sets prices** | Dealers (market makers) |
| **Price driver** | Supply and demand (CLOB) vs dealer quotes (quote-driven) |
| **Main participant** | All traders (CLOB) vs dealers (quote-driven) |
| **Transparency** | High (CLOB) vs lower (quote-driven) |
| **Liquidity source** | Order flow depth vs dealer inventory |
| **Typical use** | Stocks, futures, cryptocurrencies (CLOB) vs bonds, FX (quote-driven) |

</aside>

## Order-driven markets: the central limit order book

In a CLOB, there is no dealer middleman. Traders (or their brokers) submit orders—"buy 100 shares at $50" or "sell 1,000 shares at $51"—and the central exchange's matching engine executes trades when buy and sell orders overlap. The price is determined by where these orders meet, not by any dealer's quote.

The matching logic is transparent and mechanical. A sell order at $50 will match against a pending buy order at $50 or higher; the trade occurs at the price of the order that arrived first (the maker's price). This is called "price-time priority."

The central limit order book is highly visible: traders and market observers can see the full order book—all pending buy and sell orders at each price level. This transparency allows traders to see where supply and demand lie, to judge whether a bid is likely to be filled, and to spot price patterns. The depth on the book is also the liquidity available to a trader; if you want to sell quickly, you can see how much supply is waiting at the best bid.

The CLOB model dominates equity trading. On the New York Stock Exchange and Nasdaq, limit order books are central. Most futures exchanges, including the Chicago Mercantile Exchange, operate on CLOB principles. Cryptocurrency exchanges (Coinbase, Kraken, Binance) all use CLOBs.

### Why CLOBs work for stocks and futures

CLOBs suit liquid, standardized instruments with many participants. Stocks are all-or-nothing contracts with one per company; a deep order book for Apple stock is easy to maintain and display. Futures are even more suited: they're standardized (contract size, expiration, settlement) and often very liquid. The exchange owns the order book, making it a single source of truth for market data.

Because no dealer is required, retail traders can access the same market as institutions; the exchange connects them directly. This reduces costs and supports deep retail participation.

## Quote-driven markets: dealers as liquidity providers

In a quote-driven market, a licensed dealer (or multiple dealers) posts a bid price (the price at which they will buy from you) and an ask price (the price at which they will sell to you). The difference is the [bid-ask-spread](/bid-ask-spread/), and that's how the dealer profits. You either take the dealer's quote or walk away; there's no negotiation, and there's no visible order book of pending offers from other traders.

The dealer holds inventory. When you sell, the dealer buys into inventory; when you buy, the dealer sells from inventory. This inventory buffer absorbs short-term imbalances in supply and demand. If there's a temporary wave of selling, a dealer will accumulate inventory (at risk) until demand returns. The dealer is compensated for this risk via the spread.

Quote-driven markets are standard in bonds, currencies (forex), and over-the-counter (OTC) instruments. When you call a bond dealer for a price, you get a quote: "I'll buy at 99.50, sell at 99.75." The dealer is not running a matching engine; they're using their own inventory and market knowledge to assess risk.

### Why quote-driven markets suit bonds and FX

Bonds are heterogeneous: each Treasury bond, corporate bond, or municipal bond has different characteristics (coupon, maturity, issuer risk, embedded options). Building a central limit order book for every bond is impractical; there are millions of bond issues, and most trade rarely. Dealers, by contrast, can warehouse a range of bonds and quote prices on demand.

Foreign exchange is also quote-driven. Currencies are infinitely divisible (you can buy any amount), and liquidity is fragmented across many dealers globally. No single exchange owns the order book. Instead, traders phone or electronically message dealers to request quotes, and multiple dealers compete on spread and execution.

## Price discovery and transparency

In a CLOB, price discovery is transparent and efficient. The order book tells you instantly where supply and demand meet; prices adjust in real time as new orders arrive. Observers can see the market clearly and spot trends. Manipulation is harder because every order is visible and timestamped.

In a quote-driven market, price discovery is more opaque. Dealers have private information about their own inventory and other clients' demands; they set spreads and adjust quotes to manage risk. Prices may vary from one dealer to another, and a less-informed trader may not realize they received a worse quote than a better-connected peer. However, dealers also inject liquidity during stress; a dealer will often continue quoting during a crash, while a CLOB's order book can evaporate as traders cancel orders.

## Transaction costs and the spread

In a CLOB, the spread is usually the difference between the best bid and best ask in the order book, determined by supply-demand balance. During liquid periods, spreads tighten; during stress, they widen or the book thins. The spread is not profit for any single party; it's a gap that reflects current uncertainty.

In a quote-driven market, the spread is a dealers' revenue. Dealers can widen spreads when they're holding inventory risk or when the market is less active. They can tighten spreads to win business. Wider spreads mean higher costs to traders, but they also attract dealer inventory and can improve liquidity during stress.

## Regulation and transparency

CLOBs are typically heavily regulated. Exchanges must publish bid-ask quotes and order books in real time, and trading rules are public. The SEC mandates real-time public reporting of stock trades and the [Reg SHO](http://example.com) framework governs short sales. This transparency reduces insider advantage and market manipulation.

Quote-driven markets have lighter transparency rules, especially in OTC instruments. A bond dealer can quote a client without publishing that quote broadly; only the immediate trade may be reported (and often with a time delay). This opacity can protect market makers' inventory strategies but also allows information asymmetries to persist.

## Hybrid and evolving structures

Many modern markets blend the two models. Electronic Communication Networks (ECNs) in equities display limit order books but also allow dealers to post quotes alongside retail orders. The Treasury market has a strong quote-driven core (major dealers quote continuously) but also spot-market CLOBs. Forex platforms like Bloomberg run CLOB-like auction engines alongside dealer quotes.

Crypto and decentralized finance have pushed toward pure CLOBs, with smart contracts as the matching engine. This removes the dealer entirely but also removes the inventory buffer that dealers provide during stress.

## Choosing between models: the tradeoffs

A CLOB favors transparency, efficiency, and retail access. It works best for standardized, highly liquid instruments. But it requires a thick order book; if the book is thin, wide spreads and price gaps emerge.

Quote-driven markets provide inventory during stress and work for heterogeneous, illiquid assets. But they introduce intermediation costs and information asymmetries. They also concentrate power in the hands of a few large dealers.

Neither is universally superior; the choice depends on the instrument and its participants.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask-spread](/bid-ask-spread/) — the width of the spread in both models
- [Price-discovery](/price-discovery/) — how prices emerge in each market structure
- [Over-the-counter-market](/over-the-counter-market/) — quote-driven markets for OTC instruments
- [Market-maker-trading](/market-maker-trading/) — dealer roles and strategies
- [Limit-order](/limit-order/) — fundamental order type in CLOBs
- [Market-order](/market-order/) — execution against standing liquidity

### Wider context

- [Stock-exchange](/stock-exchange/) — CLOB-based equities platforms
- [Futures-contract](/futures-contract/) — CLOB-dominant derivatives markets
- [Alternative-trading-system](/alternative-trading-system/) — private ECNs and their market structure choices
- [Liquidity-risk](/liquidity-risk/) — how structure affects liquidity during stress

</div>

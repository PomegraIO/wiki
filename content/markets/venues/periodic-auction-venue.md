---
title: "Periodic Auction Venue"
description: "A trading system that matches buy and sell orders in discrete, scheduled time windows rather than continuously."
keywords:
  - periodic auction
  - call auction
  - batch matching
  - market structure
  - price discovery
image: /svg/markets.svg
---

*A **periodic auction venue** is a trading system that matches orders in scheduled batches (called "auctions" or "call windows") rather than executing trades continuously. All orders submitted during a window are held, then simultaneously matched at a single auction price. This design eliminates latency advantages and is increasingly used as a complement to continuous [lit order books](/lit-order-book/) to protect institutional traders and reduce volatility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Periodic Auction Venue — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure." />

<div class="wiki-infobox-caption">A discrete matching mechanism that levels the speed advantage by batching orders and executing at midpoint.</div>

|   |   |
|---|---|
| **Execution model** | Batch matching at scheduled times, not continuous |
| **Auction frequency** | Hourly, every N minutes, or end-of-day |
| **Matching price** | Typically the midpoint of the current best bid and offer, or an equilibrium price |
| **Order visibility** | Usually hidden until auction closes (no pre-trade transparency) |
| **Advantage** | Eliminates latency edge; protects block traders |
| **Drawback** | Less price discovery; execution delay for urgent traders |
| **Examples** | [IEX](/iex-investors-exchange/) opening and closing auctions, [NYSE Arca](/nyse-arca/) auctions, some [alternative trading systems](/alternative-trading-system/) |

</aside>

## The auction mechanism: how it works

In a periodic auction, traders submit orders during a window — say, five minutes — with the understanding that execution will not occur until the window closes. At the closing time, the exchange's matching engine assembles all buy and sell orders submitted during the period and computes a single "equilibrium" or "midpoint" price at which as many shares as possible can be matched.

The most common auction price is the **midpoint** — the midway point between the current best bid and best offer on the exchange's [continuous lit order book](/lit-order-book/). If the best bid is $100 and the best offer is $101, the auction price would be $100.50. All orders willing to trade at that price are matched; orders outside the price are cancelled or held for the next auction.

Some auctions use an **equilibrium price** instead: the price at which the volume of buy orders equals the volume of sell orders, clearing the market with minimal unexecuted inventory. This approach can result in better price discovery if there is significant imbalance between buyers and sellers.

Orders in the auction are typically submitted as **intraday limit orders** (bids to buy or asks to sell at specific prices) or as **market orders** (willingness to execute at the auction price, whatever it is). Because orders are hidden during the window — neither buyers nor sellers see the accumulating order flow until the auction executes — there is no opportunity for a latency-advantaged trader to exploit information about who is buying or selling.

## Why exchanges introduced periodic auctions

The rise of latency arbitrage and high-frequency trading created a problem: large institutional traders could not execute block trades without exposing their intentions and attracting adverse trading. A pension fund wanting to purchase 100,000 shares might do so in small tranches across multiple venues and time periods, incurring enormous costs just to conceal the size of their order.

[IEX](/iex-investors-exchange/) pioneered the use of periodic auctions at open and close to provide a safe venue for these trades. Institutional traders could submit orders confident that they would not be front-run by faster traders. The model proved attractive enough that other venues, including [NYSE Arca](/nyse-arca/), added periodic auctions as a complement to their continuous trading.

Most US equities venues now offer some form of periodic auction. [NASDAQ](/nasdaq/), the [New York Stock Exchange](/new-york-stock-exchange/), and regional exchanges have opening and closing auctions that batch orders from their customers. Some [alternative trading systems](/alternative-trading-system/) operate almost entirely as periodic venues, with auctions every few minutes.

## Periodic auctions vs. continuous trading

The tradeoff between periodic auctions and continuous [lit order books](/lit-order-book/) is fundamental.

*Continuous trading* allows traders to execute immediately at the [current price](/intrinsic-value/). [Price discovery](/price-discovery/) happens in real time: every trade reveals information about supply and demand. The [bid-ask spread](/bid-ask-spread/) is typically tight because [market makers](/market-maker-trading/) can see the order book and adjust their quotes continuously. However, continuous markets are vulnerable to latency advantages; traders with faster connections or closer proximity to the matching engine can gain unfair edge.

*Periodic auctions* eliminate the latency advantage entirely. All traders — local or remote, fast or slow — experience the same execution: their orders are held for the same duration and matched at the same time. Large traders can execute block trades without being hunted by algorithms. However, periodic auctions sacrifice some real-time price discovery. Orders are hidden during the window, so the continuous order book is thin. If a trader needs to buy or sell urgently, a periodic auction may force them to wait minutes for the next window.

In practice, exchanges use both. The opening and closing auctions are periods of high volume and price discovery; continuous trading during the day allows intraday [price discovery](/price-discovery/) and execution. This hybrid model balances the efficiency of real-time matching with the fairness of periodic batching.

## Order pricing and market-on-close orders

Most periodic auction venues execute at a price derived from the continuous [lit order book](/lit-order-book/) — typically the midpoint of the current best bid and offer. This design ensures that periodic auction traders do not unfairly benefit from orders they submit; their execution price is anchored to the broader market.

However, some venues offer **market-on-close (MOC)** orders, which explicitly request execution in the closing auction at the closing price, whatever that price may be. Institutional traders use MOC orders to execute at the end of day, capturing the average price during the close (which is often considered the "true" price for daily marks). MOC orders are particularly common at the New York Stock Exchange's closing auction, where trillions of dollars of index fund flows are executed each day.

## Periodic auctions in volatile markets

Periodic auctions have proven valuable during market stress. In a continuous market during a flash crash or panic sell-off, prices can swing wildly as [market makers](/market-maker-trading/) withdraw and trades execute at any available price. A periodic auction, by holding orders and batching them at a rational price (the midpoint or equilibrium), provides a natural circuit breaker. Traders know they will not execute at panic prices; instead, their orders will clear at a price that reflects the broader market consensus.

Some proposals for market reform — including those focused on reducing [systemic risk](/systemic-risk/) — have advocated for more use of periodic auctions, especially for large block trades or during periods of high volatility.

## The limit: competition and fragmentation

Despite their benefits, periodic auctions have not replaced continuous trading as the dominant venue type. Traders value speed and immediacy, and a venue that guarantees sub-second execution will always attract more volume than one that requires a multi-minute wait. Periodic auctions remain a niche offering — used by institutional traders who prioritize fairness and price improvement over speed, and by exchanges seeking to differentiate themselves from competitors.

The presence of many competing venues (some continuous, some periodic) has also limited the impact of periodic auctions. A trader who wants to access a periodic auction must route to that specific venue; if the price is better elsewhere on a faster continuous venue, the trader may choose speed over fairness. True reduction of latency advantages would require industry-wide coordination — something unlikely in a fragmented market.

## See also

<div class="wiki-seealso">

### Closely related

- [Lit order book](/lit-order-book/) — the continuous order book from which auction prices are often derived
- [Limit order](/limit-order/) — the order type typically used in periodic auctions
- [Bid-ask spread](/bid-ask-spread/) — the spread from which midpoint prices are calculated
- [Price discovery](/price-discovery/) — how auction matching contributes to fair valuation
- [IEX (Investors Exchange)](/iex-investors-exchange/) — an exchange that emphasizes periodic auctions alongside a speed bump
- [Market order](/market-order/) — an order type that can execute at the auction price
- [Alternative trading system](/alternative-trading-system/) — venues that often use periodic auctions

### Wider context

- [Stock exchange](/stock-exchange/) — venues that operate periodic auctions
- [NYSE Arca](/nyse-arca/) — a major venue offering periodic auction functionality
- [Market maker (trading)](/market-maker-trading/) — the role of liquidity in both continuous and periodic markets
- [Systemic risk](/systemic-risk/) — how periodic auctions can reduce market stress

</div>
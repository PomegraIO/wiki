---
title: "Call Market"
description: "A market structure where trading occurs periodically at a single clearing price, rather than continuously, allowing batch matching of buy and sell orders."
keywords:
  - call market
  - batch auction
  - periodic trading
  - price discovery
  - call auction
image: "/svg/markets.svg"
---

*A **call market** conducts trading at designated intervals by gathering all buy and sell orders and matching them at a single [price discovery](/price-discovery/) price. Unlike [continuous markets](/stock-market/), where prices update throughout the day, call markets concentrate liquidity and information at specific moments, then pause trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Call Market — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for markets." />

<div class="wiki-infobox-caption">Periodic order matching instead of real-time continuous trading.</div>

|   |   |
|---|---|
| **What it is** | Trading venue where orders accumulate and execute at a single price at scheduled intervals |
| **Also called** | call auction, batch auction, periodic market |
| **When prices set** | At the call (opening and closing are typically call periods) |
| **Counterpart** | [Continuous market](/stock-market/) with real-time order flow |
| **Used for** | Stock opening/closing, illiquid securities, price discovery in [over-the-counter markets](/over-the-counter-market/) |

</aside>

## How a call market works

At a scheduled time—often the opening and closing of each trading day—the market gathers all unmatched buy and sell orders into a single pool. A clearing price is computed that maximizes the volume of trades or clears as many orders as possible without artificial priority. All orders matching or better than that price execute simultaneously at the clearing price.

Consider a simple example: suppose at the opening call for a stock, there are buy orders for 1,000 shares at £10, 800 shares at £10.50, and 500 at £11. Sell orders stand at 600 shares at £9.50, 400 shares at £10, and 900 at £10.50. The clearing price is determined algorithmically, often at £10, where supply and demand balance most efficiently. Buyers willing to pay £10 or more and sellers willing to accept £10 or less all trade, often at a single price.

After the call completes and orders settle, trading halts until the next call period. For a stock exchange, this typically means the market closes at end of day, with a closing call matching all remaining orders. The [New York Stock Exchange](/new-york-stock-exchange/) still uses a call structure at its opening and closing, though intraday trading is continuous.

## Why call markets matter for price discovery

Call markets offer a distinctive advantage for [price discovery](/price-discovery/): they pool information from all participants at once before executing. In a continuous market, the first seller may hit the bid from an impatient buyer, creating a low price that later attracts more sellers and drives the price down further. In a call auction, all sellers submit at once and are matched against all buyers simultaneously, reducing the chance that impatience distorts the equilibrium.

For illiquid securities—those with few buyers and sellers—call markets can be crucial. If a stock trades once per day, a call market ensures that when trading does occur, it reflects the broadest possible set of orders. Continuous trading would mean the lone buyer and seller who happen to show up early set the price for everyone else that day.

Call markets also reduce [adverse selection](/bid-ask-spread/) and information asymmetry because all participants reveal their intentions simultaneously. In contrast, continuous markets reward speed; traders with fast computers can react to partial information and trade before slower participants adjust prices. Call markets level that playing field by batching everything.

## Trade-offs with continuous markets

The principal disadvantage of call markets is reduced flexibility. Traders cannot execute immediately; they must wait for the next call. This matters for active portfolio managers and [algorithmic traders](/algorithmic-trading/) who want to respond instantly to news. Modern equity markets are predominantly continuous because investors demand immediate execution.

Continuous trading also enables traders to split large orders across time, minimizing market impact. In a call market, a large order enters the pool all at once, potentially moving the clearing price sharply. For institutional investors moving substantial positions, the ability to trade gradually—accepting slightly wider [bid-ask spreads](/bid-ask-spread/)—often beats the certainty of a single call price.

Call markets also concentrate risk. If news breaks between calls, orders sitting unexecuted overnight face [gap risk](/interest-rate-risk/): the opening call price may jump far from the previous closing price, catching traders off guard. A continuous market allows gradual price adjustment as news flows in, reducing shocks.

## Real-world examples

Call markets remain common in specific contexts. Many [stock exchanges](/stock-exchange/)—including those in developing markets with lower trading volumes—use call-only structures. The [London Stock Exchange](/london-stock-exchange/) uses periodic batch auctions for some low-volume stocks. Some [cryptocurrency exchanges](/cryptocurrency-exchange/) offer frequent call auctions alongside continuous order books.

Equity markets typically use a hybrid: continuous intraday trading with call auctions at opening and closing. The opening call matches overnight orders accumulated since the previous close, setting a day's initial price. The closing call matches orders that arrive after the final continuous trade, allowing investors to enter exit orders that execute at end-of-day. This structure reduces overnight [gap risk](/interest-rate-risk/) while maintaining intraday liquidity.

Call markets also appear in [over-the-counter markets](/over-the-counter-market/) and [bond](/bond/) trading, where many securities are too illiquid for continuous dealing. A [broker](/broker/) might collect client orders during the day and execute them in a single call, improving execution and reducing friction.

## Comparison to dealer and alternative structures

Call markets differ fundamentally from [dealer markets](/dealer-market/), where [market makers](/market-maker-trading/) continuously quote prices and trade from inventory. In a dealer market, the dealer is always available to buy or sell, accepting [inventory risk](/operational-risk/) in exchange for [bid-ask spread](/bid-ask-spread/) profits. In a call market, there is no dealer intermediary; buyers and sellers meet directly through the clearing mechanism.

[Fragmented markets](/fragmented-market/)—where the same security trades across multiple venues—create additional complexity for both call and continuous structures. If a stock has calls on two exchanges at different times, traders face uncertainty about which venue will have the best execution.

## See also

<div class="wiki-seealso">

### Closely related

- [Dealer Market](/dealer-market/) — continuous trading with market makers quoting spreads
- [Fragmented Market](/fragmented-market/) — trading dispersed across multiple venues
- [Price Discovery](/price-discovery/) — how markets set accurate prices
- [Bid-Ask Spread](/bid-ask-spread/) — transaction cost and liquidity measure
- [Market Maker](/market-maker-trading/) — liquidity providers in continuous markets

### Wider context

- [Stock Exchange](/stock-exchange/) — organised venues for securities trading
- [Over-the-Counter Market](/over-the-counter-market/) — decentralised trading for less liquid securities
- [Algorithmic Trading](/algorithmic-trading/) — automated execution strategies
- [New York Stock Exchange](/new-york-stock-exchange/) — largest equity exchange using hybrid call-and-continuous structure
- [Liquidity Risk](/liquidity-risk/) — cost and speed of executing trades

</div>

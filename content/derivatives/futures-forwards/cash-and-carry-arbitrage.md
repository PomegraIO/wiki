---
title: "Cash-and-Carry Arbitrage"
description: "A riskless trade buying the spot asset and selling the futures contract to exploit mispricings relative to theoretical forward value."
keywords:
  - arbitrage
  - futures
  - cash markets
  - basis
  - cost of carry
  - price discovery
image: "/svg/derivatives.svg"
---

*A **cash-and-carry arbitrage** is a market-neutral strategy in which a trader simultaneously buys an asset in the [spot market](/spot-exchange-rate/) and sells a [futures contract](/futures-contract/) on the same asset, locking in a riskless profit if the futures price exceeds its theoretical fair value. The strategy is especially common in [stock index futures](/stock-index-futures/), bonds, currencies, and commodities, and has historically been a powerful mechanism for maintaining efficient pricing between cash and derivatives markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cash-and-Carry Arbitrage — key facts</div>

<img src="/svg/derivatives.svg" alt="A financial contract symbol representing derivatives and leverage." />

<div class="wiki-infobox-caption">Exploiting the gap between spot and futures to lock in riskless profit.</div>

|   |   |
|---|---|
| **What it is** | Simultaneous long spot, short futures; profits if futures overpriced relative to carry costs |
| **Fair value** | Spot price + [cost of carry](/cash-and-carry-arbitrage/) (interest, storage, minus convenience yield or dividends) |
| **Profit source** | The **basis**: futures price minus spot price exceeds fair value |
| **Risk** | Negligible (both legs offset); execution and liquidity risks remain |
| **Common assets** | [Stock indices](/stock-index-futures/), bonds, crude oil, agricultural commodities |
| **Traders** | Primarily institutions with low transaction costs and real-time execution |
| **Frequency** | Profits are typically small (10–100 basis points); large volume trades required |

</aside>

## The economics: fair value and the basis

The **basis** is the simplest version of the idea: Futures Price = Spot Price + Basis. In an efficient market, the basis should equal the [cost of carry](/cash-and-carry-arbitrage/), which is the cost of holding the spot asset until futures expiry.

For a stock or [stock index](/stock-index-futures/), the cost of carry is the [interest rate](/interest-rate/) paid to finance the purchase, minus the [dividend yield](/dividend-yield/) received while holding the shares. If you buy the S&P 500 Index at spot price 5,000 and pay 5% to finance the purchase, but the index yields 2% in dividends over six months, your cost to carry for six months is roughly 1.5% of the spot price.

Therefore, a six-month futures contract should trade near 5,000 × 1.015 = 5,075. If it trades at 5,100, it is overpriced by 25 basis points. Buying the index and shorting the future captures that 25 basis points, minus transaction costs.

## The anatomy of a riskless trade

Here is the execution:

1. **Today (Day 0):** Simultaneously:
   - Buy all 500 stocks in the [S&P 500 Index](/sp-500-index/) (or an [index fund](/index-fund/)) at spot price 5,000.
   - Sell one six-month [futures contract](/futures-contract/) at 5,100.
   - Finance the stock purchase at 5% per annum.

2. **At Futures Expiry (Day 180):** The [futures contract](/futures-contract/) converges to the spot price of the index (by definition, futures converge to spot at expiry). Say the index is then 5,050.
   - Close the futures position at 5,050 (sell leg is bought back for 5,050).
   - Sell the stocks at 5,050 (they are worth spot price).
   - Repay the loan of 5,000 plus six months of interest: 5,000 × 1.025 = 5,125.

3. **Profit:** Futures leg: Sold at 5,100, closed at 5,050 = +50. Stock leg: Bought at 5,000, sold at 5,050 = +50. Financing cost: -125. **Net = -25.** This is a loss.

Wait—this is the no-arbitrage case. Futures price was correctly set at 5,100. Let's reprice: if futures had traded at 5,150 instead, the profit would be +150 (futures) + 50 (stock gain) - 125 (interest) = **+75 basis points riskless gain**.

## Why liquidity and transaction costs matter

In theory, the trade is riskless once both legs are on. In practice, an arbitrageur must:

1. Buy 500 individual stocks (or transact in a large block), incurring [bid-ask spreads](/bid-ask-spread/) and market impact.
2. Sell [futures](/futures-contract/) quickly before the spot price moves.
3. Hold the position for months, paying financing costs and managing [margin](/margin-call-forex/).

For a mega-fund with $10 billion under management, these costs might be 2–5 basis points—leaving room for profit if the mispricing is larger than 10 basis points. For a retail trader, transaction costs might be 100+ basis points, eliminating all profit.

This is why cash-and-carry arbitrage is predominantly an institutional sport. Firms with prime brokerage relationships, algorithmic execution, and minimal borrow costs profit; everyone else is priced out.

## Reverse cash-and-carry: the flip side

When [futures](/futures-contract/) are *underpriced* relative to fair value, an arbitrageur executes the reverse: short the spot asset and buy the [futures](/futures-contract/). This strategy is less popular because [short selling](/short-selling/) has higher costs and borrowing restrictions than buying. But in liquid markets (equities, currencies), reverse arbitrage is feasible and essential for tight pricing.

## Why it matters for price discovery

Cash-and-carry arbitrage is not glamorous, but it is crucial. If [index futures](/stock-index-futures/) are overpriced relative to the spot index, arbitrageurs buy the index and sell futures. This buying pressure lifts the spot price and selling pressure pushes down the futures price, closing the gap. The market is kept honest.

Conversely, if futures are underpriced, shorts are covered and futures bought, closing the gap from the other direction. The mechanism is invisible to most traders, but it is relentless. Basis trading profits are measured in hundreds of basis points per year, but trillions of dollars of spot-futures mispricing is eliminated in the process.

## Commodities: storage and convenience yield

Cash-and-carry works differently in commodities. To carry crude oil, you must pay storage, insurance, and financing costs. You receive no "dividend" unless the market is in [backwardation](/backwardation/) (near futures cheaper than far futures), in which case the convenience of owning physical supply is a benefit valued by refineries and traders.

An oil trader buys [crude oil](/crude-oil/) at spot and sells six-month [futures](/futures-contract/), locking in the cost of carry plus storage. If the future is priced above this, the trade is profitable. If it is priced below—which can happen in [contango](/contango/)—the trader incurs a loss. This dynamic is why oil [futures curves](/futures-contract/) tell a story about supply and demand expectations.

## Bonds and repo

In government [bond](/bond/) markets, cash-and-carry is executed via the [repo](/cash-and-carry-arbitrage/) market. A trader borrows bonds, sells them, and simultaneously buys a [bond future](/bond-etf/) to be delivered later. The financing cost is the repo rate, which can be much cheaper than the nominal [interest rate](/interest-rate/). Basis trading in bonds is a staple of fixed-income desks.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the mechanics and settlement of standardised derivatives
- [Stock Index Futures](/stock-index-futures/) — the primary venue for equity index arbitrage
- [Single Stock Futures](/single-stock-futures/) — enabling arbitrage on individual equities
- [Spot Exchange Rate](/spot-exchange-rate/) — the current price in the cash market
- [Cost of Carry](/cash-and-carry-arbitrage/) — the theoretical fair value of a forward or futures contract
- [Contango](/contango/) — when far futures are more expensive; the opposite trading signal
- [Basis](/cash-and-carry-arbitrage/) — the gap between spot and futures that drives profit

### Wider context

- [Short Selling](/short-selling/) — the mechanism for reverse arbitrage
- [Margin Call (Forex)](/margin-call-forex/) — the financing and leverage side of the trade
- [Price Discovery](/price-discovery/) — how arbitrage keeps cash and derivatives markets aligned
- [Bid-Ask Spread](/bid-ask-spread/) — transaction costs that determine whether arbitrage is profitable
- [Index Fund](/index-fund/) — the passive vehicle often used as the spot leg of index arbitrage

</div>

---
title: "Market-on-Close Order Mechanics"
description: "Rules for MOC and LOC orders, imbalance publications, and the final execution process that determines how they fill at the closing price."
keywords:
  - market-on-close
  - MOC orders
  - closing auction
  - LOC orders
  - closing mechanism
  - limit-on-close
image: "/svg/markets.svg"
---

*A **market-on-close (MOC) order** is an instruction to buy or sell a security at whatever price prevails at the official market close (4:00 p.m. Eastern in US equity markets). The exchange queues these orders separately from intraday trading, executes them all at a single price in a final auction, and publishes imbalances in the minutes before close to attract offsetting liquidity. **Limit-on-close (LOC) orders** are the same mechanism with a price constraint: execute at the close only if the price is within a pre-set limit.*

## Why MOC orders exist

MOC orders serve two broad purposes: rebalancing and certainty. A portfolio manager who wants to own exactly 1,000 shares of a stock by day-end, regardless of intraday volatility, submits an MOC order and lets the exchange handle the execution at whatever the final price turns out to be. This avoids intraday slippage and the risk of being filled piecemeal throughout the day at widely varying prices.

Large index funds and exchange-traded funds use MOC orders to rebalance holdings with precision at a predictable time. Passive trackers, for instance, track their index baskets most closely at the close, so they preferentially route rebalancing orders to the closing auction rather than intraday.

For some hedge funds and systematic traders, the close is a natural endpoint for risk management: liquidate or hedge positions at the published close price, not some interim mid-day level. MOC orders also reduce the need to time intraday entry, appealing to traders who prioritize certainty over any chance of a better price.

## Cutoff times and order placement rules

On major US exchanges, traders can submit MOC orders up to **approximately 3:50 p.m. Eastern**, though the exact cutoff varies slightly by exchange and market data provider. Once an MOC order is in the system, it cannot be cancelled or modified—it will execute at the close, period. This immutability is part of the appeal: once you commit, there is no second-guessing.

[LOC orders](/market-on-close-mechanics/) work identically but include a price limit. A trader submits "sell 500 shares LOC at 45.50 or better," meaning the order will execute at the close only if the closing price is at least 45.50 (for a sell) or at most 45.50 (for a buy). If the closing price falls outside the limit, the LOC order is simply cancelled and does not trade.

Most exchanges also accept what are called **market-at-open (MAO)** and **limit-at-open (LAO)** orders for the opening auction, following the same structure as MOC/LOC but executing at 9:30 a.m. instead.

## Imbalance publication and contra-side attraction

Beginning roughly **10 minutes before the 4:00 p.m. close**, the exchange begins publishing the closing auction imbalance at regular intervals—typically every 1–2 minutes. This imbalance shows how many more shares traders wish to sell than buy (or vice versa) at the current equilibrium closing price.

The logic is identical to the [opening auction](/auction-imbalance-mechanism/): if 2 million shares want to sell MOC but only 500,000 want to buy, the exchange signals this gap to the market. Traders who see a large sell imbalance know there is an opportunity to profit by stepping in with buy orders or short covering. This flood of contra-side liquidity—attracted specifically by the published imbalance—narrows the gap and leads to a tighter final close price.

The closing imbalance publication is a high-stakes broadcast. Quantitative traders obsessively monitor these feeds, using imbalance trends to forecast intraday momentum into the close or even to predict the next day's open. Some funds specifically structure their rebalancing to participate in closing imbalances, buying when the market shows excess supply and selling into excess demand.

## Price limits and collars

To prevent the closing price from spiking wildly, the exchange enforces a **"collar"**—a price range, typically 4% or more, around some reference price (often the last intraday trade or a volume-weighted average of recent trades). If the imbalance would push the closing price outside this collar, the exchange raises or lowers the equilibrium price to bring it back within bounds. This prevents a handful of large MOC orders from distorting the day's official closing price beyond reason.

For LOC orders, the limit price acts as an additional backstop. Even if the closing price is computed fairly, a LOC order won't execute if the final price breaches its limit.

## The final execution: single price, strict hierarchy

At 4:00 p.m. sharp, the exchange **locks the closing auction**—no new MOC, LOC, or other closing orders are accepted. The system then:

1. Computes the final equilibrium price at which the maximum number of shares can trade.
2. Executes all [market orders](/market-order/) and [limit orders](/limit-order/) at that single price using a strict time-priority queue: earliest orders fill first.
3. Applies additional rules for partial fills: if 500,000 shares want to sell but 400,000 want to buy at the close, the first 400,000 shares of sell orders (in time order) execute; the remaining 100,000 shares of sell orders are cancelled.

This single-price, time-priority hierarchy ensures fairness and predictability. Everyone who traded at the close got the same price; no one paid more or less based on order size or market-maker discretion.

## Volume and market impact

Closing volume is often enormous: index-fund rebalancing, hedge-fund unwinding, and systematic rebalancing all cluster at the close. On a major stock, closing imbalances can easily exceed 5–10 million shares. This volume concentration means closing-auction participation is not casual; a trader joining the close must accept that they are moving many millions of shares at once and cannot easily undo a mistake.

For small-cap or illiquid stocks, the closing imbalance can be so large that it absorbs the entire daily trading volume at a single price—leading to a jagged final print disconnected from the day's intraday average.

## See also

<div class="wiki-seealso">

### Closely related

- [Auction Imbalance Mechanism](/auction-imbalance-mechanism/) — How exchanges publish imbalances before open and close
- [Odd-Lot Trading Mechanics](/odd-lot-trading-mechanics/) — Handling of sub-round-lot orders in auctions
- [Spoofing and Layering Mechanics](/spoofing-and-layering-mechanics/) — Fraudulent manipulation of closing imbalances
- [Limit Order](/limit-order/) — Limit orders and their execution at the close
- [Market Order](/market-order/) — Market orders during auctions
- [Price Discovery](/price-discovery/) — Role of closing auctions in discovering fair value

### Wider context

- [Stock Exchange](/stock-exchange/) — Exchanges that operate closing auctions
- [Bid-Ask Spread](/bid-ask-spread/) — How closing prices relate to intraday spreads
- [Market-Maker Trading](/market-maker-trading/) — Dealer participation in closing imbalances
- [Index Fund](/index-fund/) — Primary users of MOC orders for daily rebalancing

</div>

---
title: "Market-on-Close Orders: Strategy and Use Cases"
description: "How market-on-close orders fill at the official closing price, and why index funds and institutional traders use them for rebalancing and settlement."
keywords:
  - market on close order
  - MOC order strategy
  - closing price trading
  - index rebalancing
  - institutional trading execution
image: /svg/strategies.svg
---

*A **market-on-close order** is an instruction to buy or sell a security at the official closing price of the trading session, executed in a dedicated 15-minute window just before market close. Institutional managers use them when they need the precise closing price for accounting, index rebalancing, or when the exact execution price matters more than speed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market-on-Close Orders — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for strategies." />

<div class="wiki-infobox-caption">Guaranteed fill at the official close, but only if imbalance matches your order size.</div>

|   |   |
|---|---|
| **Execution time** | 15-min auction before official close (3:45–4:00 p.m. ET on major exchanges) |
| **Order type** | Not a market order; a conditional order filled at the closing price or not at all |
| **Price guarantee** | Fills at or very near the NBBO closing price; no price protection beyond close |
| **Primary users** | Index funds, pension plans, ETF providers, mutual fund companies |
| **Key advantage** | Eliminates execution risk from trying to trade at close manually |
| **Key risk** | Order may not fill if market imbalance does not match your order size |

</aside>

## What a Market-on-Close Order Does

When you submit a market-on-close order, you are not placing a live [market order](/market-order/) or [limit order](/limit-order/). Instead, you are entering a batch auction that runs from 3:45 p.m. to 4:00 p.m. Eastern Time on the major U.S. exchanges. At the 4:00 p.m. official close, your order either fills at the closing price or is cancelled—no partial fills, no queuing into the next session.

The closing price is set by the official close mechanism on each exchange, not by the last trade in the minute before. The [NYSE](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) both run closing auctions designed to match as many MOC orders as possible at a single "clearing price" that balances buy and sell pressure. This price is often within one cent of the last second's bid-ask spread, but volume imbalances can push it further.

The order type exists because closing prices carry immense weight in finance: mutual fund [net asset value](/net-asset-value/) is set at close, index rebalancing flows hit at close, and corporate actions are often priced off the close. For large institutions, hitting the official close with certainty is worth paying a small execution premium.

## How the Closing Auction Works

The closing auction is not a simple first-come, first-served queue. Instead, exchanges collect all MOC orders, all limit orders that cross the clearing price, and all pegged orders in a batch and solve for the price that maximizes the quantity matched.

Say a stock has buyers trying to purchase 2 million shares and sellers offering 1.5 million. The exchange will set a clearing price at which 1.5 million shares cross—likely slightly lower than the last bid, to attract more selling or cancel excess buying demand. Buyers whose orders exceed the matched quantity are not partially filled; they are cancelled. This is a feature, not a bug. Your order either executes at the close or it doesn't.

Limit orders can also participate in the close. If you place a limit order to buy at $50 on a stock that closes at $49.98, you will not fill in the MOC auction (your limit is above the clearing price). But if your limit is $50 and the clearing price is $49.99, you will fill.

## Index Rebalancing and Passive Flows

The largest use of market-on-close orders is index fund rebalancing. When a stock joins or leaves the [S&P 500](/sp-500-index/) or another major index, every fund tracking that index must buy or sell it on the same day, at the closing price. A $1 trillion fund tracking the S&P might need to buy 5 million shares of a new constituent at close. Submitting that via MOC guarantees a fill at close and locks in the price that the index uses.

Before MOC orders existed, funds had to manually trade late in the session, creating volatile spikes in the last 30 minutes as all the rebalancing trades hit. The closing auction democratizes the process: a large buy order no longer moves the price more than a small one, because all MOC volume meets at a single clearing price.

This is why market-on-close orders spike in volume on index-rebalancing days. Academic studies show that stocks added to the S&P 500 typically rise 2–3% on announcement but then flat or fall slightly into the rebalancing date, because the market anticipates mechanical buying at close.

## Mutual Fund and ETF Settlement

Mutual funds and exchange-traded funds must price their shares using closing prices, by law. When an investor redeems shares from a fund during the trading day, the fund manager does not know the exact redemption price until 4:00 p.m. official close. To hedge that exposure, large fund companies use MOC orders to execute the trades that offset expected end-of-day flows.

An ETF provider expecting $100 million in redemptions uses MOC sell orders to pre-position the portfolio at the closing price, locking in the reference price. This eliminates the risk that prices move sharply between the fund's close (4:00 p.m.) and the fund company's settlement (often 5:00 p.m. or later), which would create losses the fund would have to absorb.

## Execution Certainty vs. Execution Risk

A market-on-close order prioritizes certainty of price over certainty of fill. For an investor who must trade at the close and cannot afford slippage, MOC is ideal. For an investor who must fill a large quantity and can tolerate a few cents of variance, it is risky: if the imbalance runs against you, your order is cancelled and you must scramble to fill it in the next session or pay cash drag for a missed rebalancing.

The 15-minute window (3:45–4:00 p.m.) helps. That window is long enough for large institutional orders to accumulate and balance out, but short enough that prices do not drift far from the pre-close levels. Retail traders rarely use MOC orders because they do not have the scale or the need for the exact closing price.

## Comparison to Other Order Types

A [market order](/market-order/) executes immediately at the best available price, but slippage can be severe in the final minutes if a stock is thin or volatile. A [limit order](/limit-order/) with a limit price at or near the mid-spread might not fill at close if prices move against you. An MOC order sacrifices immediacy for precision: you wait 15 minutes and get the official close price, but if the close is too far from your limit, you get nothing.

[Pegged orders](/limit-order/), which move with the bid-ask spread, are often submitted to the closing auction as well and participate alongside MOC orders. A fund manager might place a pegged order to sell slightly above the mid if prices drift down, giving themselves one more shot to fill at a favorable close.

## Costs and Limitations

Market-on-close orders are free in the sense that brokers do not charge a commission per MOC order. However, the price you receive may be one or two cents worse than if you had placed a skilled limit order a few minutes earlier. In a fast-moving market, the closing auction can be volatile: if bad news hits at 3:55 p.m., the clearing price may be sharply lower than the 3:45 p.m. price.

Large MOC orders that exceed the available buying or selling interest at close will be cancelled, forcing the trader to retry the next day. This is why traders often split MOC orders across multiple sessions or use a combination of MOC and limit orders to cover for the risk of a partial fill.

## Strategic Uses Beyond Rebalancing

Portfolio managers occasionally use MOC orders as a signaling mechanism. A well-known buyer submitting a large MOC order sends a positive signal about the stock; an unusually large seller sends a negative one. Some sophisticated traders have tried to game these signals, placing fake MOC orders in hopes of misleading other traders, but exchange rules now require orders to be genuine and cancellations to be reported.

Tax-loss harvesting operations also rely on the close. If you want to sell a loser at a specific price to harvest the loss, and buy an equivalent replacement stock at the same close, MOC orders lock both sides in simultaneously, avoiding price gaps between the two legs.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Order](/market-order/) — immediate execution at any available price
- [Limit Order](/limit-order/) — conditional execution at or better than a specified price
- [Bid-Ask Spread](/bid-ask-spread/) — the transaction cost you pay between buy and sell prices
- [Execution Risk](/execution-risk/) — costs of not executing at the intended price or time
- Closing Price — the official settlement price used for valuations and indices

### Wider context

- [Index Fund](/index-fund/) — passive funds that must rebalance to track their benchmark
- [Exchange-Traded Fund](/etf/) — funds that price at close and need settlement certainty
- [Net Asset Value](/net-asset-value/) — fund price set daily at closing
- [Price Discovery](/price-discovery/) — how markets establish "the" price for a security

</div>

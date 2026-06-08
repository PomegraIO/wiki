---
title: "Market on Open Order"
description: "An order routed to the opening auction, guaranteeing execution at the official opening price."
keywords:
  - market on open order
  - moo order
  - opening auction
  - opening price
  - order execution timing
image: "/svg/trading.svg"
---

*A **Market on Open (MOO) order** is an instruction to buy or sell a security at the official opening [auction](/stock-exchange/) price, executed at the instant the market opens. It guarantees an execution at the session's opening price, the reference used for overnight valuations and opening-session risk assessments.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market on Open Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Locks in the first official price of the day; no price limit.</div>

|   |   |
|---|---|
| **What it is** | A [market order](/market-order/) routed to the opening auction, guaranteed to fill at the session's official opening price |
| **Also called** | MOO order, at-open order, on-open order |
| **Execution time** | At the opening auction (typically 9:30–9:35 am US equity time) |
| **Price certainty** | Guaranteed opening price; no limit applied |
| **Counterpart** | [Market on Close Order](/market-on-close-order/) (closing auction) |
| **Typical use** | Gap response, overnight news reaction, rebalancing after earnings |

</aside>

## Why the opening auction matters

The opening price reflects the overnight accumulation of supply and demand. Between yesterday's close and today's open, news breaks, earnings are announced, overseas markets trade, [futures contracts](/futures-contract/) signal expectation. By 9:30 am, thousands of traders and algorithms have queued orders waiting for the opening auction.

The opening price is more volatile and information-dense than any intraday price. It embodies the market's overnight reassessment. For this reason, institutional portfolios and trading algorithms place immense weight on the opening price: it is the entry point for the day's fresh trades and often serves as a baseline for gap-risk calculations.

A MOO order lets a trader participate in that opening intensity without guessing or market-timing. Instead of trying to catch the exact moment of the 9:30 am bell and submit an order manually, a MOO order is queued in advance and automatically executes at the opening price when the exchange confirms the clear. The trader knows in advance they will execute at the session's first official price, whatever it turns out to be.

## The mechanics of the opening auction

On the [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/), the opening auction begins shortly after 9:30 am. Traders can submit MOO orders at any point during the prior trading session and overnight. As the market approaches open, the exchange runs a "pre-opening indication"—the price at which supply and demand would clear if the auction closed at that instant. This indication updates every few seconds as new orders arrive.

At 9:30 am, the exchange executes the opening auction: a single price is determined at which all buy and sell orders for that security are matched. This is the opening price. All MOO orders (and eligible [limit orders](/limit-order/) close to that price) execute at that single price in a unified trade. Unlike regular continuous trading, the opening auction is not sequential; all orders clear simultaneously at one price.

Different securities open at different times. Some stocks open at 9:35 am due to heavy overnight order flow; others open slightly before 9:30. The exchange manages this stagger to prevent system overload. Your MOO order will execute whenever that specific security's opening auction completes.

## When MOO orders drive portfolio strategy

[Active fund managers](/actively-managed-fund/) and [hedge funds](/hedge-fund/) use MOO orders to respond to overnight events. If positive earnings are released after hours, a hedge fund might submit a MOO buy order on the stock overnight, knowing they will participate in the opening move without having to race other algorithms to the opening bell.

Traders managing gap risk often deploy MOO orders as a counterbalance. If you own a stock that gapped down in overnight futures, you might submit a MOO short-sale order to lock in the opening price before intraday buyers push it higher. This avoids the dilemma of trying to time the worst point during the 9:30–9:40 am open-and-stabilise window.

Index rebalancing often occurs at the open. If a stock joins the [S&P 500](/sp-500-index/) effective immediately, passive funds must buy. Using MOO orders ensures they all transact at the opening price, avoiding a stampede through the day that would push prices further up.

## Price risk and certainty

Like [Market on Close Orders](/market-on-close-order/), MOO orders do not specify a price limit. You are committed to executing at whatever the opening price becomes, even if it has gapped dramatically from yesterday's close.

Suppose a stock closed at £40 yesterday. Overnight, a competitor announces a major product launch. At the opening, the stock gaps to £48. An investor with a pre-set MOO sell order will sell at £48, capturing the gap. But an investor with a MOO buy order will buy at £48, having missed the opportunity to buy at yesterday's £40.

This is the trade-off of MOO execution: certainty of participation in the opening move, but zero control over the price at which that move occurs. The gap—whether favourable or unfavourable—is absorbed entirely by the MOO order holder.

## Cancellation and submission windows

Most exchanges allow MOO orders to be submitted during the prior trading session and overnight. The submission window typically closes 5–10 minutes before the opening auction—perhaps 9:20 or 9:25 am for a 9:30 am open. After that window, the exchange locks the order list to compute the opening price; new submissions are rejected.

MOO orders can generally be cancelled any time before that submission window closes. Once the window locks, your order is committed and cannot be withdrawn. If you change your mind at 9:28 am, you cannot cancel a MOO order already in the queue. This inflexibility is the price of guaranteed opening execution.

If a stock halts before opening (due to news or regulatory hold-up), the opening may be delayed. Your MOO order waits patiently and executes once the opening auction eventually clears, sometimes hours later. This is rare but possible during earnings announcements or unexpected corporate events.

## Comparison with other timing strategies

MOO is the complement to [Market on Close Orders](/market-on-close-order/). Together they bracket the trading day: one commits you to the first price, one to the last. Neither specifies a price limit.

[Good Till Date Orders](/good-till-date-order/) and Good Till Cancel Orders sit passively in the market throughout the day, waiting for a limit price to be hit. MOO is the inverse: it is purely timing-based, offering no price discretion whatsoever.

[Limit orders](/limit-order/) split the difference: they specify a price but (except at open and close) do not guarantee execution timing. An MOO order sacrifices price control to gain timing certainty.

## See also

<div class="wiki-seealso">

### Closely related

- [Market on Close Order](/market-on-close-order/) — pegged to the closing auction instead of the open
- [Market Order](/market-order/) — an unpriced instruction to execute immediately
- [Limit Order](/limit-order/) — specifies a price, but no execution timing guarantee
- [Good Till Date Order](/good-till-date-order/) — a patient, time-bound order with price discretion
- Good Till Cancel Order — stands indefinitely until filled or cancelled
- Order Book — where orders queue before the opening auction
- [Immediate or Cancel Order](/immediate-or-cancel-order/) — opposite philosophy: instant execution or cancel
- [Stock Exchange](/stock-exchange/) — operates the opening auction

### Wider context

- [Index Fund](/index-fund/) — primary user of MOO orders for rebalancing
- [Price Discovery](/price-discovery/) — the opening auction's role in forming the day's first reference price
- [Market Capitalization](/market-capitalization/) — often calculated using opening prices for baseline valuation
- [Trading Volume](/stock-market/) — concentrated at open and close
- [Futures Contract](/futures-contract/) — predict opening prices overnight

</div>

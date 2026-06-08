---
title: "Primary Peg Order"
description: "An order type that automatically adjusts its limit price to match the same-side best bid or offer, maintaining price protection without crossing the spread."
keywords:
  - primary peg order
  - pegged order
  - national best bid
  - order routing
  - limit price
image: "/svg/trading.svg"
---

*A **primary peg order** is a [limit order](/limit-order/) that automatically moves its limit price to track the best bid or offer on the same side of the [spread](/bid-ask-spread/). For a buyer, it pegs to the bid side; for a seller, it pegs to the ask side. The order never crosses the spread and never pays through the [national best bid and offer](/regulation-sho/) (NBBO), making it a conservative execution method favoured by traders who want passive participation without the risk of overpaying.*

## The peg mechanism

Imagine you want to buy 10,000 shares and the current bid is $100.00. With a standard [limit order](/limit-order/), you would specify "buy at $100.00" and wait. But if the bid ticks down to $99.95, your order stays at $100.00, and now you are willing to pay more than anyone else—guaranteed to trade, but at a worse price.

A primary peg order solves this by automatically adjusting the limit price. Instead of locking in a price, you tell the venue: "Peg my order to the current best bid." As the market moves, your order follows. If the bid is $100.00, your order is $100.00. When the bid ticks to $99.95, your order is now $99.95. You are always at the best price available on your side of the spread, and your order never pays more (for a buy) or accepts less (for a sell) than the passive side is willing to trade at.

This makes primary peg orders inherently passive. You are offering to buy at the bid or sell at the ask—the prices at which passive liquidity is supplied. You are not paying the [bid-ask spread](/bid-ask-spread/); you are sitting within it.

## Why "primary"?

The term "primary" refers to pegging to the primary best bid or offer—the [NBBO](/regulation-sho/) as determined by the [Securities and Exchange Commission](/securities-and-exchange-commission/) across all venues. Unlike some pegging mechanisms that track only a single venue's best price, a primary peg order typically tracks the national best bid (for a buy) or ask (for a sell).

This distinction matters for routing. When you submit a primary peg order, the venue (or your broker) monitors all displayed prices across the market and adjusts your order's limit to match the official national best. If the best bid on [NASDAQ](/nasdaq/) is $100.00 and the best bid on [NYSE](/new-york-stock-exchange/) is $99.95, a primary peg order to buy pegs to the national best—$100.00.

## How it differs from other pegged orders

There are several related but distinct order types:

A **primary peg order** pegs to the same-side best price (bid for buyers, ask for sellers) and is transparent about this within the exchange or venue.

A **[market peg order](/market-peg-order/)** pegs to the opposite-side best price—the ask for a buyer, the bid for a seller. It is far more aggressive, as it tracks the prices traders are willing to pay to sell (if you are buying) or willing to accept to buy (if you are selling). A market peg order can execute much faster but at a worse price.

A **midpoint peg order** pegs to the midpoint of the spread—halfway between the best bid and best ask. It is neither passive nor aggressive and is used when the trader wants balanced execution without strong direction.

## Regulatory framework

Pegged orders were formally defined under Regulation National Market System (Reg NMS), which created a standardized, auditable framework for how exchanges handle them. The [Securities and Exchange Commission](/securities-and-exchange-commission/) requires that:

- Pegged orders be clearly marked as such so clearing systems can audit them
- The peg mechanism be transparent and consistently applied across venues
- The order never trade at a price worse (less favourable) than the price it is pegged to

This regulatory clarity makes primary peg orders reliable for institutional traders. A pension fund or mutual fund can use them knowing that the execution is predictable and compliant.

## Use cases

Primary peg orders are ideal for traders who want to supply passive liquidity without taking spread risk. A [market maker](/market-maker-trading/) might submit a primary peg buy order and a primary peg sell order simultaneously, effectively offering to trade at the national best bid and ask. If the market moves, their orders move with it; they always participate at the best price available.

They are also useful for algorithms that want to "lean on" the order book passively. Instead of chasing prices with aggressive orders, an algorithm can submit primary peg orders and let the market come to it. If the market is moving against the algorithm (prices rising while the algo wants to buy), the peg order naturally moves away, reducing the chance of overpaying.

Retail traders with large orders sometimes use primary peg orders to avoid revealing their intent. A visible limit order at the best bid screams "I am a buyer"; a pegged order is more neutral and adjusts silently.

## Drawbacks and execution speed

The main drawback is that primary peg orders are reactive, not proactive. They sit at the best price and wait for the market to come to them. In a fast market or when liquidity is thin, a primary peg order may never fill because your pegged price keeps moving away as the market runs.

A [market order](/market-order/) guarantees immediate execution; a primary peg order does not. For traders who need certainty of fill, the passivity of primary pegging is a liability.

There is also the question of slippage in volatile markets. If the market is moving sharply, the time it takes for your peg order to adjust and for the venue to process the new limit price can introduce delays, and you may miss the opportunity to trade at the price you expected.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Peg Order](/market-peg-order/) — pegged to the opposite-side best price; more aggressive than primary peg
- [Limit Order](/limit-order/) — the base order type that pegged orders build on
- [Market Order](/market-order/) — immediately executable; no price limit
- [Bid-Ask Spread](/bid-ask-spread/) — the gap primary peg orders sit within
- [Order Book](/stock-exchange/) — the queue where pegged orders rest and adjust
- [Intermarket Sweep Order](/intermarket-sweep-order/) — aggressive order that may trigger passive pegged orders

### Wider context

- [Regulation National Market System](/regulation-sho/) — framework that defined pegged order rules
- [National Best Bid and Offer](/regulation-sho/) — the NBBO that primary peg orders track
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator defining peg standards
- [Stock Exchange](/stock-exchange/) — venue where pegged orders are submitted
- [Market Maker Trading](/market-maker-trading/) — primary user of peg orders for passive liquidity

</div>

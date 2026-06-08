---
title: "Dark Limit Order"
description: "A non-displayed limit order that rests in a dark pool or hidden order book, receiving price priority without pre-trade transparency."
keywords:
  - dark limit order
  - hidden order
  - dark pool
  - price priority
  - order book
image: "/svg/trading.svg"
---

*A **dark limit order** is a limit order placed on an exchange or [dark pool](/over-the-counter-market/) that is not displayed to the public. Instead of being listed in the visible order book alongside standard limit orders, it rests invisibly—yet retains priority at its price level. When a [market order](/market-order/) or aggressive order enters the venue, the dark limit order can execute without having revealed itself beforehand.*

## The mechanics of darkness

Most equity [orders](/market-order/) live in an order book that every trader can see. When you place a [limit order](/limit-order/) to buy 1,000 shares of Apple at $175, that order appears in the public book, visible to algorithms, retail traders, and [market makers](/market-maker-trading/) alike. This transparency is called "lit" trading.

A dark limit order skips this visibility step. Instead of appearing in the public book, it sits in a separate, non-displayed reserve. The venue knows the order exists; the trader's broker knows it exists; but the wider market does not. Other traders cannot see it until it trades.

Many major exchanges—[NASDAQ](/nasdaq/), [NYSE](/new-york-stock-exchange/), and others—maintain hidden order books alongside their lit books. A [broker](/broker/) can route a limit order to the hidden book rather than the main display, and the exchange will match against it as if it were visible, except no one can see it coming.

## Price priority without display

The critical rule is that a dark limit order does not sacrifice priority for its invisibility. If a dark limit order to buy at $175 is resting on an exchange, and a market-sell order arrives, the dark order gets filled first—ahead of any visible limit orders to buy at the same $175 price.

This priority comes from Regulation National Market System (Reg NMS), which states that all orders at the same price receive priority by timestamp, regardless of whether they are displayed. The invisible order is considered to have "arrived" at its price level just as much as the visible one.

From the trader's perspective, the advantage is clear: you get price priority without advertising your hand. No one knows you are there, so they cannot adjust their behaviour to exploit your presence. This is especially valuable for large [block trades](/stock-exchange/) or when entering a position without tipping off other market participants.

## Dark pools versus exchange hidden books

Dark limit orders can rest in two types of venue:

**Exchange hidden books** are non-displayed reserve queues on the same exchange where lit trading happens. An order to buy at $175 might sit hidden on NASDAQ, but it will execute at the same price and with the same priority rules as the lit book.

**[Dark pools](/over-the-counter-market/)** are entirely separate, non-exchange venues dedicated to non-lit trading. They operate under different rules and often use [alternative trading systems](/alternative-trading-system/) (ATS) to match buyers and sellers. A dark limit order in a dark pool may have different priority rules, and may execute at prices that differ from the lit market.

For regulatory purposes, hidden orders on exchanges are closely monitored. Dark pools have more flexibility but face scrutiny around [fair pricing](/fair-value/) and whether their hidden matching disadvantages retail traders.

## When traders use dark limit orders

Large institutional traders use dark limit orders to accumulate or distribute large positions without moving the market. If a mutual fund needs to buy 500,000 shares of a stock over a day, entering all of it as visible orders would push the price up as other traders front-run the flow. By using dark limit orders, the fund can acquire shares at better prices because the buying pressure is not advertised.

High-frequency trading firms often layer dark orders—placing multiple small dark limit orders at different prices to create a perception of depth that does not actually exist in the lit book. (This practice, called "layering" or "spoofing," is illegal, but detecting it is difficult.)

Retail traders occasionally use dark orders to avoid "leaning on the order book"—the intuition that displaying your order telegraphs your demand and allows other traders to step ahead or adjust prices unfavourably. In practice, this benefit is often overstated for small orders, but for large or unusual orders, it can be real.

## The transparency cost

The downside of dark limit orders is opacity. The [primary market](/primary-market/) becomes less transparent as more volume moves off-display. Retail traders and smaller institutions cannot easily see what prices are available in dark books, so they may not understand the true depth of market demand.

Some economists argue that dark limit orders harm [price discovery](/price-discovery/)—the process by which markets collectively determine fair prices. If significant volume is hidden, the visible [bid-ask spread](/bid-ask-spread/) may not reflect true supply and demand, leading to mispricing.

Regulators watch dark pools and hidden books carefully. The [Securities and Exchange Commission](/securities-and-exchange-commission/) has brought enforcement actions against [alternative trading systems](/alternative-trading-system/) that used dark orders unfairly or that did not properly execute them.

## Relationship to other order types

A dark limit order is distinct from a [market order](/market-order/), which has no price protection and executes immediately at the best available price (whether visible or not). It is also different from an [intermarket sweep order](/intermarket-sweep-order/), which sweeps multiple venues but is typically displayed or marked at the time of execution.

A dark limit order is also not the same as an iceberg order, which displays a visible tranche and hides the remainder. An iceberg order is still partially visible; a dark limit order is completely invisible until it trades.

## See also

<div class="wiki-seealso">

### Closely related

- [Dark Pool](/over-the-counter-market/) — venue type where dark limit orders are placed
- [Limit Order](/limit-order/) — the base order type; dark limit orders are non-displayed variants
- [Market Order](/market-order/) — immediately executable order without a price floor
- [Alternative Trading System](/alternative-trading-system/) — regulatory framework for dark pools
- [Order Book](/stock-exchange/) — the queue where orders wait; dark orders rest in a separate queue
- [Intermarket Sweep Order](/intermarket-sweep-order/) — aggressive order type that may trigger dark orders

### Wider context

- [Regulation National Market System](/regulation-sho/) — framework defining order priority and display rules
- [Price Discovery](/price-discovery/) — process of fair-price determination; affected by dark orders
- [Bid-Ask Spread](/bid-ask-spread/) — gap between buy and sell prices; hidden orders affect spread measurement
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of dark pools and hidden orders
- [Market Maker Trading](/market-maker-trading/) — liquidity providers who interact with dark orders

</div>

---
title: "Hidden Order vs Dark Order: What Is the Difference"
description: "Hidden orders are non-displayed quotes on lit exchanges; dark orders are routed to off-exchange dark pools with stricter price/size transparency rules."
keywords:
  - hidden order vs dark order difference
  - hidden orders exchange
  - dark pool orders
  - dark order routing
  - non-displayed orders
image: /svg/trading.svg
---

*A **hidden order** is a non-displayed quotation sitting on a public exchange's matching engine, invisible to other traders but subject to exchange price and size rules. A **dark order** is routed away from lit markets entirely to a dark pool—a private venue with minimal pre-trade transparency. Though both orders avoid full visibility, they operate under different disclosure regimes and trading mechanics.*

## The transparency divide: lit vs. dark

The core distinction hinges on **where the order lives** and **what regulators require to be disclosed**.

**Hidden orders** (also called "iceberg orders" or "reserve orders") remain on the main exchange order book. They have a price and size, but the exchange does not broadcast them to the market. If a hidden order to buy 100,000 shares is placed, only the first 10,000 shares (the "visible" portion) may be shown to other traders. When those 10,000 execute, the next 10,000 tranche appears automatically. The price, however, is fully compliant with exchange price-level rules—it must be the best bid or offer on that exchange, or tucked behind other orders at the same price level.

**Dark orders** never touch a lit exchange's order book. Instead, they are submitted to a dark pool—a private, non-exchange venue operated by brokers, exchanges, or alternative trading systems ([ATS](/alternative-trading-system/)). Dark pools match buy and sell orders internally, and trades may not be reported to the public or to exchanges until after execution (and then only in summary, under exchange/[SEC](/securities-and-exchange-commission/) time delays). The price at which a dark order executes is typically the mid-point of the best [bid-ask spread](/bid-ask-spread/) on lit exchanges, or it may negotiate within a price band.

## Regulatory disclosure rules

Exchange hidden orders fall under **Regulation SHO** and exchange rules overseen by the [SEC](/securities-and-exchange-commission/). The exchange must disclose the visible portion of a hidden order, and the exchange's system must guarantee price improvement: if a hidden order is bid at $50.00 for 100,000 shares but only shows 10,000, any execution against that hidden order must respect the $50.00 price level and the same sizing rules as normal orders.

Dark pools, by contrast, operate under **Regulation ATS** (Alternative Trading Systems). ATS operators must register with the [SEC](/securities-and-exchange-commission/) and report aggregate trading statistics, but they have much looser pre-trade transparency requirements. A dark pool may not display its order book to non-members at all. Post-trade, dark pool operators must report executed trades to a trade reporting facility (TRF), typically within seconds, but the granular details (who traded, order types) often remain private.

This means a trader submitting a hidden order on the [NYSE](/new-york-stock-exchange/) has the benefit of knowing that their unexecuted portion will eventually be seen and can interact with incoming orders. A trader routing to a dark pool accepts that their order is invisible, may not execute at the best available price elsewhere, and may only cross with other dark pool participants.

## Price discovery and execution

**Hidden orders** benefit from **price discovery** on the lit venue. The exchange continuously broadcasts the best bid and offer across all visible orders. If a hidden buy order at $50.00 and a hidden sell order at $50.01 both exist on the exchange, but only $50.00 and $50.02 are visible, a new market order for 100 shares will execute at the visible spread, not at the hidden orders. This can disadvantage hidden order placers—their better prices remain latent, and the market price moves without incorporating them.

**Dark orders** sacrifice price discovery entirely in exchange for reduced market impact. A large dark order crosses against other dark pool liquidity at negotiated or algorithmic prices, without moving the market. This is valuable for institutional investors managing large positions: they avoid telegraphing their intent to the market (which would move the price against them before execution). Dark pools trade the certainty of price to gain anonymity and execution without slippage.

## Use cases

**Hidden orders** suit traders who want to avoid large visible **market impact** but are willing to accept the possibility of suboptimal pricing or partial fills. An asset manager with a large sell order might iceberg it on the exchange: the visible tranche gets attention, but the hidden reserve prevents the entire order from crushing the price immediately. Hidden orders are also used in less liquid securities where "showing your hand" to a small market risks sharp price movement.

**Dark orders** are the choice for truly large institutional blocks or for traders seeking maximum anonymity. A hedge fund accumulating shares for a [hostile takeover](/hostile-takeover/) bid does not want the market to know. A pension fund executing a multi-million-share mandate across hours or days will likely use dark pools to minimize execution costs. The tradeoff is that dark orders may not execute at the single-best price visible on lit exchanges—the dark pool price might be slightly inside the best offer, or it might fill against a dark order at a negotiated mid-point.

## Regulatory scrutiny and market structure

Hidden orders on lit exchanges receive less regulatory scrutiny because they are subject to real-time exchange oversight and post-trade surveillance. Dark pools, conversely, have drawn criticism for potentially disadvantaging retail investors and creating information asymmetries. Regulators have tightened dark pool disclosure and market access rules, but they remain far less transparent than exchange-listed orders.

The [SEC](/securities-and-exchange-commission/) and industry participants continue to debate the optimal balance between anonymity (needed for large trades) and price discovery (needed for fair markets). More hidden order volume might improve price transparency; more dark pool volume might worsen it. Many large traders use both mechanisms strategically—routing small blocks to dark pools for speed and large or urgent orders to hidden order books where price competition is fiercest.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative trading system](/alternative-trading-system/) — regulatory definition of dark pool operators
- [Bid-ask spread](/bid-ask-spread/) — the spread at which dark orders often cross
- [Market maker trading](/market-maker-trading/) — how hidden and dark orders interact with professional liquidity providers
- [Market order](/market-order/) — how market orders interact with hidden orders on exchange books
- [Limit order](/limit-order/) — the basis for both hidden and dark orders
- [Execution risk](/execution-risk/) — why traders choose between hidden and dark routing
- Market impact — hidden orders reduce it; dark orders eliminate it

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of hidden and dark order rules
- [Price discovery](/price-discovery/) — central to lit exchange order flow
- [Stock exchange](/stock-exchange/) — venue where hidden orders sit

</div>

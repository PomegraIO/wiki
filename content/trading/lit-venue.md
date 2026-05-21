---
title: "Lit venue"
description: "A lit venue is a public trading exchange where the order book and all pending orders are visible to all participants. Prices are discovered transparently through supply and demand, and trades are reported in real time."
keywords:
  - lit venue
  - public exchange
  - order book
  - price transparency
image: "/svg/trading.svg"
---

*A **lit venue** is a public trading exchange — like the NYSE, NASDAQ, or regional exchanges — where orders are transparent and visible in the public order book. Buyers and sellers see exactly what sizes are available at each price, trades occur at the best available prices, and all transactions are reported immediately. Lit venues are the backbone of price discovery.*

<div class="wiki-hatnote">

For hidden trading venues, see [dark pool](/dark-pool/). For orders hidden on a lit venue, see [hidden order](/hidden-order/) and [iceberg order](/iceberg-order/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lit venue — key facts</div>

<img src="/svg/trading.svg" alt="A trading terminal showing a transparent lit order book" />

<div class="wiki-infobox-caption">Lit venues: full transparency, real-time reporting, price discovery.</div>

|   |   |
|---|---|
| **What it is** | Public exchange with transparent order book |
| **Visibility** | Full; all pending orders visible |
| **Price setting** | Transparent; set by supply and demand |
| **Regulation** | Stringent; SEC oversight for U.S. exchanges |
| **Market share** | ~85% of U.S. equity trading (plus dark pools) |
| **Participants** | Retail, institutional, market makers, algorithms |

</aside>

## What makes a venue "lit"?

A lit venue displays:
- **The order book:** All pending [limit orders](/limit-order/), their sizes, and prices.
- **Quotes in real time:** Best bid and best ask updated continuously.
- **Trade reports:** Every completed trade reported immediately (within seconds).
- **Price history:** Full intraday trading data available to all participants.

Anyone with a data feed can see the whole picture. This transparency is the defining feature.

## Major lit venues in the U.S.

**Equities:**
- **NYSE (New York Stock Exchange):** Largest U.S. equity market; stocks listed here trade mostly on NYSE, but can also route to other venues.
- **NASDAQ:** Second-largest equity venue; tech-heavy, electronic.
- **Regional exchanges:** CBOE EDGX, EDGA, NYSE Arca, NASDAQ PSX, and others.

All are lit venues; all display order books and report trades publicly.

**Options:**
- **CBOE, NYSE Arca Options, NASDAQ Options, etc.:** All lit.

**Futures:**
- **CME, CBOT, ICE:** All lit (with order book visibility).

## Lit venues and price discovery

A lit venue's transparent order book creates **price discovery** — the market's collective process of settling on fair prices based on supply and demand.

When you see the order book:
- **Buy orders** (bids) stacked below the market.
- **Sell orders** (asks) stacked above the market.

You immediately understand where supply and demand are. If there are 10 million shares of buy interest at $50 and only 100,000 shares of sell interest at $51, you know prices will likely rise. This information is available to everyone, and prices reflect it.

## Lit venues and best execution

U.S. regulations (Reg NMS, [best execution](/best-execution/) rules) require that:
- Your broker route your order to achieve the best available prices across all lit venues.
- If the best price to buy is on NASDAQ, your broker must route there (even if you are a customer of a NYSE broker).
- Trade-through rule: Orders cannot be executed at worse prices than the best visible price on any lit venue.

This competition between lit venues improves execution quality.

## Lit orders and information leakage

The transparency of lit venues has a downside: **information leakage.** When you post a large order on a lit exchange, algorithms immediately see it. They can:
- **Front-run** you: trade ahead of you.
- **Avoid** you: pull their orders and wait for you to move on.
- **Trade against** you: buy from you at worse prices, knowing you are a large buyer.

This is why institutions use [dark pools](/dark-pool/), [hidden orders](/hidden-order/), and [algorithmic execution](/algorithmic-trading/) — to trade large sizes with less visibility.

## Lit venues vs. dark pools

| Factor | Lit venue | Dark pool |
|---|---|---|
| **Transparency** | Full; order book public | None; orders hidden |
| **Price discovery** | Contributes directly | Piggybacks on lit prices |
| **Market impact** | High for large orders | Minimal; hidden |
| **Execution quality** | Best bid-ask available | Midpoint, variable |
| **Regulation** | Stringent | Lighter |
| **Use case** | Most trading; retail and institutions | Large blocks; institutions |

## Lit venue trading costs

Trading on a lit venue typically involves:

- **Exchange fees:** $0.0001–$0.0005 per share (varies by exchange and order type).
- **Liquidity rebates:** If you provide liquidity (place a [limit order](/limit-order/)) that sits and gets filled, you might receive a rebate of $0.0001–$0.0003 per share.
- **Taker fees:** If you remove liquidity (place a [market order](/market-order/) or hit an existing limit order), you pay $0.0001–$0.0005 per share.

For a retail investor, these costs are often absorbed by the broker and not separately visible.

## Order types and lit venues

Lit venues support a wide range of order types:
- [Market orders](/market-order/)
- [Limit orders](/limit-order/)
- [Stop orders](/stop-order/)
- [Iceberg orders](/iceberg-order/)
- [Pegged orders](/peg-order/)
- [All-or-none orders](/all-or-none/)

The specific support varies by exchange. Check your exchange's documentation.

## Lit venues and trading hours

U.S. equity lit venues have official trading hours:
- **Regular session:** 9:30 a.m. to 4:00 p.m. ET.
- **Pre-market:** 4:00 a.m. to 9:30 a.m. (some venues, lower liquidity).
- **After-hours:** 4:00 p.m. to 8:00 p.m. (some venues, much lower liquidity).

Regular hours are when most lit-venue trading occurs and spreads are tightest.

## Exchanges as utilities

Lit exchanges (regulated utilities) are required to:
- **Provide fair access:** Any qualified trader can access the exchange.
- **Maintain fair pricing:** Fees must be reasonable; rules must not discriminate.
- **Ensure integrity:** Surveillance for market manipulation, insider trading, etc.
- **Provide data:** Public quotes and trade information must be disseminated in real time.

This regulatory framework makes lit venues trusted and reliable for price discovery.

## Future of lit venues

Lit venues remain the heart of price discovery and the majority of trading. However, they face ongoing pressure from:
- **Dark pools:** Taking share of institutional trading.
- **Retail brokers:** Offering commission-free trading (they monetize data and order flow instead).
- **International competition:** European and Asian venues offer alternatives.

Despite this, lit venues are unlikely to disappear; they are too important for price discovery and regulatory compliance.

## See also

<div class="wiki-seealso">

### Closely related

- [Dark pool](/dark-pool/) — private venue alternative
- [Hidden order](/hidden-order/) — orders hidden on lit venues
- [Iceberg order](/iceberg-order/) — visible tip on lit venues
- Order book — the public display on lit venues

### Trading and execution

- [Market order](/market-order/) — executes on lit venues
- [Limit order](/limit-order/) — sits on lit-venue order book
- [Best execution](/best-execution/) — achieved via lit venues
- Liquidity — abundant on lit venues

### Regulation and market structure

- Reg NMS — regulates lit and dark venues
- Trade-through rule — requires trading at best prices on lit venues
- [NBBO](/nbbo/) — national best bid-offer across all lit venues
- SEC — regulates exchanges

### Market information

- Price discovery — lit venues' core function
- Quotes — real-time bid-ask on lit venues
- Trade reporting — required on lit venues

</div>

---
title: "Odd-Lot Orders and Their Effect on Execution"
description: "How odd-lot trading orders for fewer than 100 shares are handled differently, affecting execution and tape data."
keywords:
  - odd lot order execution
  - odd lot trading effects
  - odd lot definition
  - round lot vs odd lot
  - tape data distortion
  - execution routing
image: /svg/trading.svg
---

*An **odd-lot order** is any request to buy or sell fewer than 100 shares of a stock—e.g., 47 shares or 99 shares. Historically, brokers routed odd-lot trades through specialized dealers and reported them to the tape differently than round-lot (100-share) trades, creating execution delays and distorting published price data. Modern technology has blurred this distinction, but legacy effects on spreads and data remain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Odd Lots — Key Facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">Small orders take a different path, with measurable delays and data artifacts.</div>

|   |   |
|---|---|
| **Definition** | Any order for fewer than 100 shares |
| **Round lot** | 100 shares; the standard unit for exchange trading |
| **Historical routing** | Odd lots passed to specialized dealers; round lots to the exchange |
| **Execution lag** | Odd lots typically executed seconds to minutes after round lots at same price level |
| **Tape reporting** | Odd-lot trades historically excluded from ticker; now recorded separately |
| **Spread effect** | Odd-lot spreads typically wider than round-lot spreads for same security |
| **Modern status** | Distinction persists in execution rules but less operationally significant |

</aside>

## Origins: The 100-Share Standard

The "round lot" of 100 shares traces to the 19th century, when exchanges standardized trading units to reduce confusion and simplify settlement on paper. Anything less than 100 shares was an **odd lot**—usually an order from a retail investor or a small liquidation.

For decades, exchange rules required odd-lot orders to be routed through a **specialist** or **odd-lot dealer**—a middleman separate from the main exchange [market maker](/market-maker-trading/). The dealer would accumulate odd-lot buy orders, wait until a round-lot order came in at the same price, then bundle them together and execute the round lot on the exchange. The odd-lot customers received the same price as the round-lot trade (often plus a small fee or slightly worse execution).

This arrangement worked in a world of slow communication and manual record-keeping. But it introduced a systematic lag: an odd-lot buyer in Chicago might see his order filled 30 seconds to several minutes *after* the stock price moved higher on the exchange. The dealer bore inventory risk; investors bore timing risk.

## Routing and Execution Today

Modern technology has dismantled much of the machinery. Most U.S. exchanges now accept odd-lot orders directly and execute them alongside round-lot orders on the same price-time queue. However, regulatory and market-maker conventions preserve some separation.

**Intermarket routing**: When a retail investor places an odd-lot order through a broker, it typically travels to an electronic communication network (ECN) or the broker's own internal [market maker](/market-maker-trading/). The broker's system then checks exchanges—[NASDAQ](/nasdaq/), [NYSE](/new-york-stock-exchange/)—for the best quoted price (the [bid-ask spread](/bid-ask-spread/)) and routes the order there, or to an [alternative trading system](/alternative-trading-system/) (ATS) if the price is better.

**Odd-lot dealer networks**: A handful of specialized odd-lot dealers (such as Citadel Securities and Wolverine Trading) still operate as wholesalers. They accept odd-lot orders from brokers at the national best bid and offer (NBBO) or slightly better, then accumulate them and execute as round lots on exchanges or in the [over-the-counter market](/over-the-counter-market/). For the retail investor, the execution price is typically the NBBO at the time the order hits the wholesale desk—sometimes better if the dealer is aggressive in competing for flow.

The upshot: an odd-lot buy order of 47 shares can now be executed nearly instantaneously, often at the same price as a round-lot trade, if market conditions are liquid. The delay and fee structure have shrunk.

## Spreads and Price Quality

Despite technological progress, odd-lot trades incur wider [bid-ask spreads](/bid-ask-spread/) than round-lot trades. A [market maker](/market-maker-trading/) quoting 100 shares at a $0.01 spread might quote 50 shares at a $0.03 spread, or decline to quote odd-lot sizes altogether.

**Why?** Market makers face execution risk and inventory cost. A round lot of 100 shares is easier to hedge or offset against other orders. An odd lot of 23 shares is a burden: it is difficult to sell quickly without taking a loss, and holding it ties up capital. Market makers compensate by charging wider spreads on odd lots—the spread is the dealer's markup for absorbing that risk.

For investors, this means an odd-lot order often fills at a marginally worse [execution price](/execution-risk/) than a round-lot order for the same stock at the same instant. Over a portfolio of many small trades, these fractions add up.

## Data Distortions and Tape Reporting

Historically, the ticker tape—the published record of exchange transactions—excluded odd-lot trades. The exchange reported only round-lot trades. An investor watching the tape would see "100 shares @ $50.25" but not "47 shares @ $50.26" executed seconds later by an odd-lot dealer.

This created a **data illusion**: the published price series did not reflect all trades, only round-lot trades. Researchers discovered that odd-lot traders were systematically worse traders—buying near peaks and selling near troughs—which suggested they were unsophisticated or had inferior information. The published tape showed a spurious pattern of "odd-lot selling into strength," which some viewed as a contrarian indicator.

Modern consolidated tape (FINRA's Trade Reporting Facility, NYSE's ArcaBook, NASDAQ's NMS feeds) now reports virtually all trades, including odd lots. The data distortion has largely vanished. However, analyst platforms and [price discovery](/price-discovery/) algorithms still often filter odd-lot trades when computing [VWAP](/volume-weighted-average-price/) (volume-weighted average price) or other statistics, reinforcing the historical compartmentalization.

## The Nuts and Bolts of Execution Costs

Consider a concrete example. An investor wants to buy 37 shares of a stock quoted at a $50.00 bid / $50.01 ask (a $0.01 round-lot spread). If she routes a round-lot order of 100 shares, she will hit the ask at $50.01.

If she routes an odd-lot order of 37 shares, the dealer or ATS might quote a $50.00 bid / $50.03 ask (a $0.03 spread) to reflect the extra risk of holding the odd lot. If she is willing to buy at the market, she pays $50.03, a $0.02 (or 0.04%) penalty.

For a $50 stock and 37 shares, that is a $0.74 difference—small in absolute terms but material to an investor accumulating positions slowly. Over hundreds of odd-lot trades, the spread penalty can become significant. This is one reason some retail investors are advised to "round up" orders to 100 shares when possible, or to use limit orders to negotiate the price rather than accepting the spread.

## Regulatory Framework

The SEC and FINRA maintain rulebooks governing odd-lot handling. [FINRA Rule 6630](/finra/) sets standards for odd-lot transactions at retail, and NYSE/NASDAQ rules address odd-lot routing and reporting. The intent is to ensure odd-lot orders receive "best execution"—the most favorable price and terms reasonably available—but the rules are less prescriptive than round-lot rules, reflecting the lower volume and complexity of odd-lot trading.

Brokers are required to report odd-lot trades but are permitted to execute them through non-exchange venues (like wholesale networks) as long as the price is at or better than the NBBO. This creates a two-tier system: transparent round-lot prices on the exchange, and opaque odd-lot execution through bilateral wholesale deals.

## Modern Trends

The shrinking minimum investor account (many brokers now allow fractional shares and $1 share purchases via [apps](/fractional-shares/)) has raised the proportion of odd-lot orders relative to round-lot orders. Retail platforms like Robinhood and Fidelity report that fractional-share trading accounts for 15–20% of retail order flow.

At the same time, [high-frequency trading](/algorithmic-trading/) and market fragmentation have made the round-lot / odd-lot distinction less economically meaningful. A "round lot" of 100 shares executed on a fractional-volume ATS may have wider spreads than an odd lot executed through a tight wholesale network.

The legacy framework persists because it is embedded in exchange rulebooks and dealer infrastructure. But the economic reality—that smaller orders incur higher spreads and face routing friction—now applies across sizes, driven by liquidity concentration and [execution risk](/execution-risk/) rather than by formal round-lot / odd-lot categories.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — why odd lots face wider spreads
- [Market maker trading](/market-maker-trading/) — the dealer who accepts odd-lot risk
- [Execution risk](/execution-risk/) — the friction in small orders
- [Price discovery](/price-discovery/) — how odd-lot exclusion distorted historical tape data
- National best bid and offer — the benchmark odd-lot dealers anchor to

### Wider context

- [Alternative trading system](/alternative-trading-system/) — where odd lots often route
- [Over-the-counter market](/over-the-counter-market/) — another venue for odd-lot execution
- Ticker tape — the historical reporting standard that omitted odd lots
- [Algorithmic trading](/algorithmic-trading/) — modern execution that brackets round and odd lots alike

</div>
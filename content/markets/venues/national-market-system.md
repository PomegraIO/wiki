---
title: "National Market System"
description: "The regulatory framework linking US exchanges and trading venues into an integrated best-price network under Regulation NMS."
keywords:
  - regulation nms
  - stock exchange integration
  - best execution
  - intermarket trading system
  - order routing
image: "/svg/markets.svg"
---

*The **National Market System** (NMS) is a regulatory framework that binds competing US [stock exchanges](/stock-exchange/) and alternative trading venues into a single, electronically linked network designed to display prices transparently and route orders to the best available price. Established in stages beginning in 1975 and substantially expanded under [Regulation NMS](/securities-and-exchange-commission/) in 2007, the system guarantees that retail and institutional investors benefit from the lowest offer and highest bid available across all venues at any given moment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">National Market System — key facts</div>

<img src="/svg/markets.svg" alt="An abstract mark for equity market venues and price integration." />

<div class="wiki-infobox-caption">One integrated price, many venues—enforced by regulation.</div>

|   |   |
|---|---|
| **What it is** | A [SEC](/securities-and-exchange-commission/)-mandated network linking all US exchanges and [alternative trading systems](/alternative-trading-system/) to display and route orders at best price |
| **Regulatory basis** | Securities Acts Amendments of 1975; Regulation NMS (effective 2007) |
| **Core requirement** | [Order routing](/limit-order/) must execute at the best [bid-ask spread](/bid-ask-spread/) visible across all venues |
| **Key venues included** | NYSE, NASDAQ, regional exchanges, and [over-the-counter](/over-the-counter-market/) networks |
| **Order protection rule** | Prevents trade-through (executing below a better price displayed elsewhere) |
| **Also known as** | Consolidated tape, intermarket linkage |

</aside>

## Why the system was built: fragmentation and fraud

Before 1975, US equity trading was fragmented across the [New York Stock Exchange](/new-york-stock-exchange/), regional "provincial" exchanges, and the over-the-counter market, with limited real-time price transparency between them. A single stock could trade at different prices on different exchanges simultaneously, and investors had no systematic way to know which venue offered the best deal. The 1975 Securities Acts Amendments tasked the [SEC](/securities-and-exchange-commission/) with creating a unified system that would bind these competing venues together and make price information universally available.

The original National Market System relied on slower communication—ticker tape, telephone, and gradually computerized links—to circulate best bids and offers. By the 1980s and 1990s, electronic communication networks ([alternative trading systems](/alternative-trading-system/)) began to splinter order flow again, creating new blind spots. The gap between the "official" quoted price and the prices actually available on less-visible venues widened. Regulation NMS, adopted in 2005 and effective in 2007, modernized and toughened the rules: it required near-instantaneous electronic display of quotes, tightened the tolerance for trade-through prevention, and imposed penalties on brokers who routed orders away from the best price.

## How best execution works: the order protection rule

The centerpiece of Regulation NMS is the [Order Protection Rule](/limit-order/), which prohibits trading through a better price. If a [limit order](/limit-order/) to sell stock is resting at $50.00 on NASDAQ, no execution should occur at $50.05 on the NYSE. The system must either route the order to the better price or alert the routing [broker](/broker/) that a superior quote exists elsewhere. This sounds simple in theory, but it created operational complexity: what counts as a "displayed" quote? What latency is acceptable when routing to a remote venue? The rules address these through narrow exceptions (e.g., the "slow quote" exception) and minimum increment standards.

In practice, the Order Protection Rule means that an investor who places a [market order](/market-order/) benefits from the fragmentation it was designed to prevent: their order scans the entire network instantly, and even small price improvements cascade through the system. A fraction of a penny per share, multiplied across millions of shares, is real money.

## The consolidated tape and real-time transparency

Every trade and quote in an NMS stock flows into consolidated price feeds—the Trade Reporting and Information System (TRIX) for trades and the Best Bid and Offer (BBO) feed for quotes. These data are aggregated and published in real time by [self-regulatory organizations](/securities-and-exchange-commission/) (SROs) and disseminated to [market makers](/market-maker-trading/), brokers, and the public. A retail investor watching a stock ticker on their brokerage app is seeing data originally captured and consolidated by the NMS infrastructure.

This transparency supports [price discovery](/price-discovery/)—the process by which new information gets reflected in the quoted price—across all venues simultaneously. When a company announces earnings after hours, the open next morning reflects that information not just on the stock's primary exchange but across the entire network, because market participants see the same real-time quotes.

## Venues and their roles within the system

The NYSE, NASDAQ, and regional exchanges (NYSE American, CBOE) are all venues within the NMS. So are [alternative trading systems](/alternative-trading-system/) (ATS), which are SEC-registered networks that match orders away from the official exchanges. The Intermarket Trading System (ITS), established in the 1980s and now succeeded by more modern electronic linkages, ensures that orders can be routed between venues with minimal latency.

Each venue has a self-regulatory organization (SRO) that reports trades and enforces compliance with NMS rules. The [SEC](/securities-and-exchange-commission/) oversees the SROs and can propose rule changes, but the regulatory structure distributes enforcement across the ecosystem rather than centralizing it in a single authority.

## Trade-throughs and maker-taker fees

Despite the Order Protection Rule, trade-throughs still occur—sometimes legally (within narrow exceptions), sometimes illicitly. A trade-through happens when a broker routes an order to one venue instead of to another venue with a better price, depriving the customer of the better deal.

One unintended consequence of Regulation NMS is the prevalence of [maker-taker fees](/market-maker-trading/). Venues, competing for order flow, began rebating fees to brokers who brought liquidity to them and charging fees to brokers who executed against resting orders (the "takers"). These fees can create incentives for brokers to route orders to venues offering the highest rebate rather than the best price, at least at the margin. Regulators have debated this structure but have largely allowed it, treating the rebates as a form of price improvement that benefits the customer overall.

## Speed, latency, and the limits of integration

Regulation NMS assumes that prices are updated and quotes can be routed nearly instantaneously. Microstructure research has shown that in the microsecond realm, the system is imperfect: so-called "latency arbitrage" permits sophisticated traders with faster data feeds to trade ahead of slower market participants, creating a de facto gap in execution quality. Some regulators and investors argue this contradicts the spirit of the best-execution mandate, but attempts to impose hard latency floors have been politically fraught and technologically contentious.

The system works, but its effectiveness is bounded by physics (the speed of light, network delays) and incentives (competing venues want exclusivity, brokers want rebates). Perfect integration remains a theoretical ideal rather than a daily reality.

## See also

<div class="wiki-seealso">

### Closely related

- [Regulation NMS](/securities-and-exchange-commission/) — the 2007 regulatory overhaul that modernized the system
- [Alternative Trading System](/alternative-trading-system/) — competing venues integrated into the NMS
- [Bid-Ask Spread](/bid-ask-spread/) — the price difference the system works to minimize
- [Market Maker](/market-maker-trading/) — liquidity providers whose quotes anchor the best bids and offers
- [Order Protection Rule](/limit-order/) — the core mandate preventing trades below better available prices
- [Price Discovery](/price-discovery/) — how new information gets reflected across all venues
- [Over-the-Counter Market](/over-the-counter-market/) — legacy venue linked into modern NMS infrastructure

### Wider context

- [Stock Exchange](/stock-exchange/) — the primary venues within the NMS
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator that designed and enforces the system
- [New York Stock Exchange](/new-york-stock-exchange/) — the largest single venue in the NMS
- [Broker](/broker/) — intermediaries responsible for best-execution compliance
- [Market Order](/market-order/) — the order type that benefits most from integrated price display

</div>
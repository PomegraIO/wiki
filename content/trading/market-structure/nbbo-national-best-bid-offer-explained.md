---
title: "NBBO: National Best Bid and Offer Explained"
description: "How the national best bid and offer (NBBO) is assembled from US stock exchanges, its legal status under Reg NMS, and why it drives retail order routing."
keywords:
  - national best bid and offer
  - nbbo explained
  - best execution
  - reg nms
  - market-wide information system
---

*The **national best bid and offer** (NBBO) is the highest buy price and lowest sell price for a stock across all US protected venues at any given moment. Built by the Securities Information Processors (SIPs) and enforced under Regulation NMS, it is the legal floor for best execution and the basis for nearly all retail order routing decisions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NBBO — market backbone</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Every retail order route depends on real-time NBBO prices.</div>

|   |   |
|---|---|
| **What it is** | The best bid and offer across all US exchanges at a single moment |
| **Who compiles it** | Securities Information Processors (SIPs) |
| **Legal mandate** | Regulation NMS (SEC rule requiring best execution) |
| **Updated** | Continuously, every time a quote changes on any venue |
| **Impact on traders** | Determines whether your order gets filled at a better price, or routed away |

</aside>

## How the NBBO is built

The NBBO is a composite quote. Every US stock exchange—the New York Stock Exchange, [Nasdaq](/nasdaq/), and the regional exchanges—continuously publishes its best bid and best offer for every listed stock. The SIPs, operated jointly by exchanges and the Financial Industry Regulatory Authority (FINRA), subscribe to each venue's feed, compare all bids and all offers in real time, and publish the consolidated NBBO to market data vendors, brokers, and trading platforms.

If Apple is trading at $150.23–$150.24 on NYSE, $150.22–$150.25 on Nasdaq, and $150.20–$150.26 on a regional exchange, the NBBO is $150.23 (highest bid) and $150.24 (lowest offer). This happens continuously; the NBBO updates whenever any exchange updates its quote.

The SIP is fast but not instantaneous. There is a small but measurable delay—typically a few milliseconds—between when an exchange publishes a quote and when the SIP publishes the consolidated NBBO. This latency matters for high-speed traders, but not for retail investors.

## The legal anchoring: Regulation NMS

[Regulation NMS](/securities-and-exchange-commission/), adopted by the SEC in 2005, is the rule that makes the NBBO legally binding. The central mandate is simple: broker-dealers must execute customer orders at the NBBO price or better. If your broker is routing your buy order to an exchange, it must get you the lowest available ask price across all venues, not just what is available on its preferred exchange.

This rule applies to virtually all equity trades. If a broker knowingly fills you at a worse price than the NBBO, it has violated best execution and is subject to fines and enforcement action. In practice, brokers compete to offer order routing that captures NBBO prices or worse (i.e., tighter) prices through internalization or payment for order flow arrangements.

## NBBO and retail order routing

For a retail trader, the NBBO is invisible but consequential. When you place a market order to buy 100 shares of a stock, your broker's system checks the current NBBO offer price and routes your order to the venue offering that price, or better. If the NBBO offer is $50.10, your broker cannot legally fill you at $50.11 unless you explicitly accepted that price.

The NBBO also protects against certain predatory routing practices. Before Regulation NMS, brokers could route orders to internal markets or venues that posted inferior quotes, pocketing the difference without the client's knowledge. The rule forbids this; it institutionalizes a "price-time priority" regime where the best price across all venues wins.

Limit orders are also governed by the NBBO. If you place a limit buy order at $50.05 when the NBBO is $50.10–$50.15, your order sits in a queue waiting for the offer side to drop to $50.05. If the offer at another venue touches $50.05 before the offer at your venue, your order should be filled based on the best price first (all else equal), to preserve price priority.

## The mechanism: SIP feeds and real-time dissemination

The SIP operation is largely standardized. The main US SIP is the CTA/CQ system, operated jointly by NYSE, Nasdaq, and regional exchanges. Each exchange publishes its quote changes (bid, offer, size) to the SIP at microsecond intervals. The SIP ingests these feeds, performs the consolidated calculation (find the max bid, find the min offer), and disseminates the NBBO to subscribers.

Market data vendors like Bloomberg, FactSet, and IEX republish the NBBO to financial professionals. Retail trading platforms (Fidelity, E-TRADE, Interactive Brokers, Robinhood) receive NBBO data and display it to clients. That price you see on your phone is a cached snapshot of the SIP NBBO from a fraction of a second ago—current, but not perfectly real-time due to network and application latency.

## When the NBBO breaks: locked and crossed markets

Occasionally, the NBBO can become "locked"—the best bid equals the best offer—or "crossed"—the best bid exceeds the best offer. This is a rare anomaly caused by network delays, exchange outages, or data feed failures. When a market is locked or crossed, it signals a problem; no normal transactions should occur at a crossed price. The SEC has rules requiring exchanges to halt posting of quotes that would lock or cross the NBBO for more than a few seconds.

A crossed market usually resolves within milliseconds as data catches up. But it is a red flag for traders, because it suggests either outdated information or a technical fault.

## NBBO in practice: an example

Imagine you are holding Apple stock and see a news headline that moves the price. At the instant before the headline, the NBBO is $150.30–$150.31, and you decide to sell. You place a market sell order.

Your broker's order management system checks the live NBBO: it may have shifted to $150.28–$150.29 in the first few milliseconds as traders rush to sell. Your market sell order is routed to the exchange(s) showing the $150.29 bid (let's say Nasdaq in this case) and filled immediately at $150.29. If your broker tried to fill you at $150.27, it would be a best execution violation, regardless of the reason.

The NBBO ensures that your fill is not arbitrarily worse than what every other venue is quoting at that instant. It is the mechanism that makes equity markets transparent and prevents hidden price-setting.

## See also

<div class="wiki-seealso">

### Closely related

- [Regulation NMS](/securities-and-exchange-commission/) — The SEC rule mandating best execution and consolidated quotes
- [Market maker trading](/market-maker-trading/) — How designated market makers provide liquidity and set venue-specific quotes
- [Bid-ask spread](/bid-ask-spread/) — The cost difference between the best bid and offer
- [Alternative trading system](/alternative-trading-system/) — Venues that post quotes but are not traditional exchanges
- [Stock exchange](/stock-exchange/) — How the NYSE, Nasdaq, and regional venues publish quotes
- [Price discovery](/price-discovery/) — How aggregated quotes across venues establish fair prices

### Wider context

- [Best execution](/securities-and-exchange-commission/) — Broker obligation to seek optimal trade pricing
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The regulator enforcing Reg NMS and best execution
- [Market order](/market-order/) — How market orders interact with the NBBO
- [Limit order](/limit-order/) — How limit orders are ranked under NBBO and price-time priority

</div>

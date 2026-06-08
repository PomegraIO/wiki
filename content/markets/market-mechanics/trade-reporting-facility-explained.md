---
title: "Trade Reporting Facility Explained"
description: "How FINRA Trade Reporting Facilities work, which trades must be reported, and how off-exchange prints feed into the consolidated tape."
keywords:
  - trade reporting facility explained
  - finra trade reporting facility
  - trade reporting facility how it works
  - otc trades reporting
  - consolidated tape
image: /svg/markets.svg
---

*A **Trade Reporting Facility** (TRF) is a FINRA-operated system where [broker](/broker/)s report over-the-counter equity trades—transactions that happen off the major exchanges. Every TRF report feeds into the consolidated tape, the public record that shows every trade in a stock, regardless of where it happened. Understanding how TRFs work reveals how modern equity markets actually function beyond the New York Stock Exchange and Nasdaq.*

<div class="wiki-hatnote">

See [Over-the-Counter Market](/over-the-counter-market/) for a broader overview of off-exchange trading venues.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade Reporting Facility — Key Facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">FINRA's infrastructure for reporting and consolidating off-exchange equity transactions.</div>

|   |   |
|---|---|
| **Operator** | FINRA (Financial Industry Regulatory Authority) |
| **Purpose** | Collect and publish off-exchange trade reports to consolidated tape |
| **Who reports** | Brokers and dealers executing OTC trades |
| **What trades** | Equities traded over-the-counter (not on exchange) |
| **When to report** | Within seconds of trade execution (T+0 or T+0.5) |
| **Tape output** | Consolidated tape (CTA/UTP) shows all trades publicly |
| **Pricing impact** | TRF trades can move the official "last sale" price |
| **Related systems** | ATS (Alternative Trading Systems), market makers, [FINRA](/finra/) |

</aside>

## What Is a Trade Reporting Facility?

FINRA operates multiple Trade Reporting Facilities to handle the large volume of equity trades that occur away from formal stock exchanges. When a [broker](/broker/) arranges a trade between a buyer and seller (often two institutional clients, or a dealer and a client) without using the NYSE or Nasdaq, that trade must be reported to a TRF so the public knows it happened.

The TRF receives the report, validates it, timestamps it, and sends it to the consolidated tape—the official record of all U.S. equity trades. The consolidated tape is published in real time (or near-real time, depending on the venue) and used by all market data providers, traders, and investors to track prices.

There are two main TRFs: the ADF (Alternative Display Facility) for equities on Nasdaq's level, and the ORF (OTC Reporting Facility) for other listed equities. In practice, "TRF" often refers to either. Both feed the same consolidated tape and serve the same regulatory purpose.

## Why Off-Exchange Trades Need Reporting

When a trade happens on an exchange (NYSE, Nasdaq), the exchange itself reports the trade. It is automatic and immediate. The exchange collects fees, enforces market rules, and provides the price signal to the world.

Off-exchange trades—negotiated directly between [brokers](/broker/) or through alternative trading systems (ATSs)—would otherwise be invisible. Without a reporting requirement, traders could hide transactions, and the true price of a stock would be fragmented and opaque. Regulators and investors would not know the real volume or price discovery happening in the market.

The TRF mandate solves this: every [broker](/broker/) that executes an OTC trade must report it within a narrow time window (typically within seconds). This keeps the market transparent and prices uniform across all venues.

## Who Uses Trade Reporting Facilities?

**Block traders and institutional brokers** are the primary users. When Goldman Sachs arranges a 100,000-share block trade for a mutual fund client, it may execute the trade directly with a counterparty and then report it to the TRF.

**Market makers** operating in specific stocks report their OTC trades. A market maker might buy 10,000 shares from one client and sell 10,000 to another; that internal matching is reported to the TRF.

**Alternative Trading Systems (ATSs)** that operate outside the formal exchange structure also report to the TRF. ATSs are venues that match buy and sell orders electronically but do not operate as formal exchanges. Examples include systems run by large brokers, alternative market operators, and private trading networks.

**Retail brokers** generally do not use TRFs directly; their trades go to their broker-dealer who executes on an exchange or sends it to an ATS. But the end result is still ultimately reported somewhere on the consolidated tape.

## How Reporting Works

When a trade executes off-exchange, the executing [broker](/broker/) has a narrow window (typically 10 seconds for Nasdaq, 30 seconds for others, though this continues to tighten) to submit a report to the TRF.

The report includes:
- The stock symbol
- Number of shares
- Price per share
- Time of execution
- Identifier of the trading firm

The TRF validates the report, checks for errors and obvious inconsistencies, and forwards it to the consolidated tape vendor (CTA for NYSE-listed stocks, UTP for Nasdaq).

The tape then disseminates the trade publicly within seconds. Any trader, data provider, or retail investor can see that the trade happened, at what price, and in what volume.

## Impact on Public Price

A key rule: a TRF trade can become the "last sale" price for a stock. If a large block trades OTC at a price that is higher or lower than the recent exchange price, the TRF-reported trade becomes the new official last sale. This is important because many automated systems, algorithms, and [portfolio](/asset-allocation/) managers use the last sale price as a signal.

In practice, this means OTC market activity influences the stock's quoted price, even though it happened off-exchange. A large block trade on the TRF can move the closing price or affect the price that others see in real-time data feeds.

## Versus Alternative Trading Systems

ATSs are often confused with TRFs, but they are different. An ATS is a venue—a system that matches orders. A TRF is the reporting infrastructure. Some ATSs report to TRFs; others are formal exchanges and report directly.

The distinction matters: if you trade on an ATS, your broker will report the trade to the TRF (if it is an equity) so it shows on the consolidated tape. The ATS itself does not operate the tape; FINRA and the exchanges do.

## Consolidated Tape: The Public Record

The consolidated tape is the heartbeat of price transparency in U.S. equity markets. Every trade—whether on the NYSE, Nasdaq, an ATS, or a direct OTC deal between brokers—flows into the consolidated tape (CTA for NYSE-listed, UTP for Nasdaq-listed).

The tape is published by SIPs (Securities Information Processors) operated by the exchanges, FINRA, and OPRA (for options). Any firm that wants real-time trade data subscribes to these feeds, which cost thousands to hundreds of thousands per month depending on depth and lateness.

Retail investors see a delayed or free version of the tape through their brokers or free data providers. Institutional traders pay for low-latency direct access.

## Regulatory Significance

The TRF and consolidated tape system is central to market surveillance. Regulators monitor the tape for signs of manipulation, insider trading, or fraud. A trade that appears inconsistent with recent prices, volume, or market conditions flags for human review.

For brokers, reporting trades to the TRF is not optional. Failure to report, or submitting false information, is a violation of FINRA rules and can result in fines, suspension, or criminal charges.

The TRF also enables [price discovery](/price-discovery/)—the process by which all available information about a stock gets reflected in its price. Because OTC trades are visible, the "true" price of a stock includes signals from all market participants, not just those on formal exchanges.

## See also

<div class="wiki-seealso">

### Closely related

- [Over-the-Counter Market](/over-the-counter-market/) — off-exchange trading venues and mechanics
- [Alternative Trading System](/alternative-trading-system/) — ATS systems that use TRFs to report trades
- [Broker](/broker/) — who executes and reports trades to TRFs
- [Market Maker](/market-maker-trading/) — participants who use TRFs to report matched trades
- [FINRA](/finra/) — the regulator that operates Trade Reporting Facilities
- [Consolidated Tape](/consolidated-tape/) — the public record of all trades, including TRF reports

### Wider context

- [Stock Exchange](/stock-exchange/) — formal venues like NYSE and Nasdaq
- [Price Discovery](/price-discovery/) — how markets find the true price of a stock
- [Stock Market](/stock-market/) — broader market structure and trading
- [Bid-Ask Spread](/bid-ask-spread/) — pricing in OTC and exchange venues

</div>

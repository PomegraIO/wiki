---
title: "Off-Exchange Trade Reporting Facility"
description: "Learn how FINRA Trade Reporting Facilities capture off-exchange equity trades and why accurate reporting matters for market transparency and surveillance."
keywords:
  - off-exchange trade reporting facility
  - finra trade reporting facility how it works
  - otc trade reporting
  - trade reporting facility equity
  - market surveillance reporting
image: /svg/markets.svg
---

*An **off-exchange trade reporting facility** is a venue where brokers report equity trades executed outside traditional lit exchanges. Run by [FINRA](/finra/), these facilities collect reports of over-the-counter and [alternative trading system](/alternative-trading-system/) activity, consolidate the data, and feed it to regulators and market participants—a critical backbone for market surveillance and price transparency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FINRA TRF — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for markets." />

<div class="wiki-infobox-caption">Off-exchange reporting ensures dark-pool and OTC trades are visible to regulators.</div>

|   |   |
|---|---|
| **Operator** | [FINRA](/finra/) — Financial Industry Regulatory Authority |
| **What it captures** | Trades executed in [alternative trading systems](/alternative-trading-system/), off-exchange venues, and [over-the-counter market](/over-the-counter-market/) |
| **Reporting deadline** | T+2 (two business days post-execution); some near-real-time with conditions |
| **Data published** | Last-sale reports (price, volume, time) feed into market data vendors and regulatory feeds |
| **User access** | Market participants buy feed; regulators access full unfiltered data |
| **Coverage** | Equities; fixed income and options have separate reporting mechanisms |
| **Regulatory goal** | Aggregate dark-pool and block-trade activity to monitor market structure and detect manipulation |

</aside>

## The reporting infrastructure

Under Regulation SHO and Regulation FD, brokers trading equities off-exchange—whether in a [dark pool](/alternative-trading-system/), a block trading desk, or directly with another broker—must report the trade to a [FINRA](/finra/)-operated Trade Reporting Facility (TRF). There are multiple TRF systems (TRF Chicago, TRF Carteret, and legacy systems merged over time), but collectively they form the backbone of off-exchange trade data flow.

When a buyer and seller match inside a dark pool, the trade details—symbol, volume, price, time—go to the TRF operator (not the exchange). The TRF collects thousands of reports per day and publishes a consolidated last-sale feed. This feed is disseminated to market data vendors (Bloomberg, FactSet, broker terminals) and made available to the [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) for surveillance.

The process is invisible to most retail traders. A stock trades on both the [New York Stock Exchange](/new-york-stock-exchange/) and a dark pool simultaneously. The NYSE-traded shares appear on the tape in real-time or near-real-time. The dark-pool trade (identical price, moments apart) reaches traders via the TRF feed a few seconds or minutes later, depending on the reporting speed chosen by the broker.

## Why off-exchange reporting matters

Historically, block trades and [over-the-counter market](/over-the-counter-market/) trades were private, reported days later or not at all. A large institutional buyer could absorb 500,000 shares off-exchange without moving the public quote, because the transaction was invisible until settlement.

This opacity created two problems:

**Price discovery**: [market makers](/market-maker-trading/) and other traders making two-sided quotes did not see all trading activity. An off-market bid-ask was quoted without knowledge that a block had just crossed 100 basis points lower off-exchange. The public tape was incomplete.

**Regulatory blind spots**: the [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/) could not detect patterns of manipulation or insider trading in dark-pool activity. If a stock was being accumulated before a takeover announcement, dark-pool volume might reveal the accumulation, but only if reported and analyzed.

The TRF system addressed this by mandating report-or-get-delisted: brokers trading equities in any venue, lit or dark, must report to a TRF within a deadline or face enforcement action. This created a continuous feed of off-exchange trades flowing into the regulatory ecosystem.

## How trades are reported and processed

A broker executing a trade—say, 100,000 shares of ABC at $50.25 in a dark pool at 10:15 a.m.—submits the following to the TRF:

- **Symbol** (ticker)
- **Volume** (100,000)
- **Price** ($50.25)
- **Execution time** (10:15 a.m.)
- **Buyer and seller** (account identifiers, anonymized for public feed)
- **Trade type** (OTC, ATS, etc.)
- **Reporting broker** (clearance firm number)

The TRF validates the report against a rulebook: the symbol exists, the price is plausible, the timing is chronological. If rejected, the broker resubmits. Once accepted, the trade enters a queue for consolidation.

The consolidated feed publishes the trade to market data vendors and the SEC's Market Information Systems (MIS). Latency is critical: the SEC and [FINRA](/finra/) monitor the flow in real-time to spot anomalies (e.g., a stock trading OTC at a vastly different price than the lit market, signaling a data error or a potential manipulation). Market data vendors ingest the feed and package it for distribution to traders and investors.

## The T+2 reporting deadline and exceptions

Under current rules, a broker has two business days after execution to report an off-exchange trade. This deadline sounds generous but was designed to accommodate settlement cycles and back-office operations. A trade executed on a Monday can be reported by Wednesday.

However, certain venues and conditions allow faster reporting:

- **Same-day reporting**: some ATS operators report within hours of execution.
- **Real-time reporting**: the [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/) are pushing for closer-to-real-time reporting, and some venues now report within 15 minutes.
- **Accepted netting transactions**: if a broker nets multiple trades (e.g., buying 50,000 shares and selling 40,000 on behalf of customers), they may report the net position change rather than each trade.

The delay creates a timing arbitrage: a sophisticated trader who knows about an off-exchange trade hours before it is reported can position ahead of its public disclosure. To combat this, regulators have increasingly tightened reporting timelines, and the industry continues to push for real-time TRF feeds.

## Data standardization and the regulatory feed

[FINRA](/finra/) publishes standardized last-sale reports from all TRFs in a single consolidated feed. This feed is the source of truth for off-exchange volume and pricing. Market data vendors subscribe to it and republish it in various formats.

The data is tagged with:

- **Trade condition codes** (regular, corrected, canceled, out-of-sequence, etc.)
- **Size modifiers** (whether the trade was a block, average price, or other special condition)
- **Participant identifiers** (encrypted for privacy)

Regulators and compliance teams use these tags to analyze trading patterns. A series of trades with "out-of-sequence" conditions might signal a reporting error or deliberate obfuscation. A large block reported as a single trade (versus split into smaller prints) affects how algorithms interpret the volume profile.

## Dark pools, block desks, and TRF volume

The bulk of TRF-reported volume consists of:

- **[Alternative trading systems](/alternative-trading-system/)** (dark pools): venues like Citadel Securities' Apogee, Goldman Sachs' Sigma, and others that match buy and sell orders privately.
- **Block trading desks**: institutional brokers who facilitate large trades off-exchange, often negotiating price directly with counterparties.
- **Internalized order flow**: a broker receiving a buy order from one client and matching it with a sell order from another client without routing to the lit market.

In liquid stocks, off-exchange volume now represents 20–40% of total trading depending on the stock and market conditions. This is why the TRF feed is material: ignoring dark-pool activity means missing a substantial slice of the market.

Conversely, the TRF feed is still incomplete. Some trades—illiquid equities, certain structured transactions, cross-border flows—may not be reported through the standard TRF. And the delay in reporting means the feed is always somewhat stale compared to real-time lit-market activity.

## Surveillance use and manipulation detection

[FINRA](/finra/) and the [SEC](/securities-and-exchange-commission/) monitor the TRF feed for suspicious activity. They flag:

- **Wash trades**: identical or near-identical buys and sells, in sequence, between related parties, designed to create the illusion of volume without risk transfer.
- **Spoofing**: submitting large orders in dark pools with no intent to execute, to move the price.
- **Layering**: multiple fake orders in rapid succession to create momentum and induce others to trade.
- **Quote stuffing and algorithmic manipulation**: automated trading that floods the dark pool with orders that are canceled before execution.

The TRF data is combined with order book data, broker identifiers, and customer accounts to reconstruct trading activity and distinguish legitimate size from manipulation. Because the TRF data is time-stamped and linked to broker and trader identifiers, regulators can often trace a suspicious pattern back to the responsible firm.

## Limitations and gaps

The TRF system has blind spots:

- **Reporting delay**: T+2 reporting means surveillance is reactive, not predictive. By the time a manipulative pattern is detected, the trader may have exited.
- **Anonymization**: the public feed does not show which broker or client executed the trade, limiting market participants' ability to analyze peer behavior. Regulators have full identifiers, but the public does not.
- **Block trade treatment**: very large blocks may be reported as single prints or averaged prices, obscuring the intraday price movement and individual execution.
- **Non-U.S. equities**: foreign companies' shares trading in the U.S. have different reporting rules, and some offshore trading escapes U.S. surveillance entirely.

## See also

<div class="wiki-seealso">

### Closely related

- [FINRA](/finra/) — the self-regulatory organization operating the TRF
- [Alternative Trading System (ATS)](/alternative-trading-system/) — dark pools and other non-exchange venues that feed the TRF
- [Over-the-Counter Market](/over-the-counter-market/) — decentralized trading between brokers, also reported to the TRF
- [Market Maker Trading](/market-maker-trading/) — how dealers quote and execute off-exchange
- [Dark Pool](/alternative-trading-system/) — private liquidity venues using the TRF for reporting
- [Last-Sale Reporting](/price-discovery/) — real-time price dissemination from lit and dark venues

### Wider context

- [Price Discovery](/price-discovery/) — the role of transparent volume in establishing fair price
- [Securities and Exchange Commission (SEC)](/securities-and-exchange-commission/) — regulator overseeing TRF and market surveillance
- [Stock Market](/stock-market/) — broader structure of equity trading venues
- [Regulation SHO](/regulation-sho/) — short-sale and reporting rules governing the TRF

</div>
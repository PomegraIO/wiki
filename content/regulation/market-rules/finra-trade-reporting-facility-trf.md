---
title: "FINRA Trade Reporting Facility (TRF): How OTC Equity Trades Get Reported"
description: "FINRA Trade Reporting Facility captures off-exchange equity trades and feeds data into public tape, enforcing reporting deadlines for broker-dealers."
keywords:
  - finra trade reporting facility
  - otc equity trades
  - trade reporting requirements
  - finra regulation
  - off-exchange trades
  - market transparency
image: /svg/regulation.svg
---

*A **FINRA Trade Reporting Facility** (TRF) is a FINRA-operated facility through which broker-dealers report sales of equity securities that occur off-exchange—on the OTC market or through alternative trading systems—so that the trades appear on the consolidated tape and meet regulatory transparency requirements. Rather than listing trades on a formal exchange, firms report them to a TRF, which validates timing and details before broadcasting to the public.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FINRA TRF — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Off-exchange trades must reach a FINRA Trade Reporting Facility within strict deadlines to appear on the public tape.</div>

|   |   |
|---|---|
| **What it does** | Captures OTC and ATS equity trades and reports them to the consolidated tape |
| **Operators** | FINRA operates TRFs in New York and Chicago; feeds data to SIPs (Securities Information Processors) |
| **Who reports** | Broker-dealers executing off-exchange equity sales; both parties to a trade must be broker-dealers |
| **Reporting deadline** | Generally within 10 seconds (T+10) for most trades; slower for certain block trades and closing transactions |
| **Public visibility** | Trade information (price, volume, time) flows to [consolidated tape](/securities-and-exchange-commission/) via SIPs; delays allowed under Rule 6730 |
| **Penalty for non-compliance** | Fines, disciplinary action, or suspension of trade reporting privileges |

</aside>

## Why FINRA TRFs exist

Before the 1970s, most equity trading happened off-exchange, and regulators had limited visibility into actual transaction prices and volumes. When the SEC created the consolidated tape system, the goal was clear: bring all equity trades—whether exchange-listed or not—into one public data stream so that prices are transparent and investors can see fair market values.

A TRF is the plumbing that makes this work. Because OTC trades (and trades on [alternative trading systems](/alternative-trading-system/)) do not automatically publish, the broker-dealers on both sides must report to a TRF. The TRF validates the report, stamps a time, and feeds it into the [Securities Information Processor](/securities-and-exchange-commission/) (SIP), which merges exchange and TRF data into the tape you see on Bloomberg, your brokerage, or financial websites.

## How the reporting flow works

When two broker-dealers execute an off-exchange equity trade—whether via phone, electronic system, or block desk—one of them typically initiates the TRF report. The report includes trade price, volume, symbol, and timestamp. The TRF system checks that both the initiating firm and the other (receiving) firm are authorized to report, that the symbol exists, and that the data are internally consistent.

Once validated, the TRF assigns an official timestamp and forwards the trade record to the SIP. The SIP then includes the trade in the next public dissemination of the consolidated tape. This happens in milliseconds, so from the public perspective, the trade appears on the tape almost immediately.

Not all trades report the same way. [Exchange-listed](/stock-exchange/) equities (like those on the [NYSE](/new-york-stock-exchange/) or [NASDAQ](/nasdaq/)) route through their respective exchanges, which also report to the SIP. A single security might have simultaneous reports from its primary exchange and from TRFs for concurrent OTC trades. The SIP aggregates these into the consolidated tape, showing the best bid and offer across venues.

## The 10-second rule and exceptions

Under FINRA Rule 6730, most off-exchange equity trades must be reported within 10 seconds (T+10). This deadline applies to standard trades executed during regular hours and reported during regular hours. The rule aims to balance the need for quick transparency against operational realities: a large block trade or a trade executed near market close may need more time to document and validate.

Certain trades qualify for longer reporting windows. A **closing transaction**—a trade executed in the final moments before market close, typically to fulfill an opening order or complete a block negotiation—can be reported after the market closes on the same day. **Block trades** exceeding certain thresholds can be reported on a 30-minute delay if they meet size requirements and are properly designated.

During market volatility or system outages, FINRA may grant temporary extensions, but firms must still report as soon as technologically feasible. Repeated failures to meet the deadline trigger escalating fines.

## Who must report and what information is shared

Only **broker-dealers** can report trades to a TRF. If an investor trades directly without a broker intermediary, no reporting obligation applies (though that is rare in modern markets). If a broker-dealer is on only one side of a trade—say, acting as a principal and trading with a customer—the customer side does not report separately; the broker-dealer makes the single report covering the whole transaction.

The trade report must include:

- **Security symbol** (CUSIP or other identifier)
- **Price and volume**
- **Trade timestamp** (to the second, or finer if the systems support it)
- **Buy/sell indicator** (which party initiated the trade)
- **Capacity** (whether the broker was acting as principal, agent, or riskless principal)
- **Rule 10b5-1 notation** (if the trade was pre-planned under an insider-trading safe harbor)

This information flows through the SIP to the public tape. Investors and traders around the world see the price paid, the volume, and the time—creating a permanent record of market activity. The tape also shows aggregate depth of market (the inside bid-ask spread and size at the national best bid and offer).

## The consolidated tape and public access

The consolidated tape is not a single file or website; it is a real-time data stream managed by Securities Information Processors. There are three SIPs:

- **SIP A**: Trades in [NYSE](/new-york-stock-exchange/) listed stocks
- **SIP B**: Trades in [NASDAQ](/nasdaq/) listed stocks
- **SIP C**: Trades in other [FINRA-eligible](/finra/) issues

Each SIP collects trade reports from its relevant exchanges and TRFs, computes the national best bid and offer (NBBO), and broadcasts the aggregate trade stream. Any retail investor can access a 15-minute delayed tape for free; real-time tape access typically requires a paid data subscription.

This transparency serves a critical function: it prevents any single venue or broker from monopolizing price discovery, ensures that retail investors and professionals operate on the same price information (even if with delays), and creates the factual record that regulators use to detect manipulation.

## Common disputes and regulatory emphasis

One frequent issue is **late reporting**. A broker-dealer might claim a system failure, network latency, or operational overload caused the delay, but FINRA's enforcement record shows limited tolerance for excuses. Fines escalate with the severity and frequency of violations.

Another area of scrutiny is **accuracy**. If a TRF report contains a typo—wrong symbol, price that deviates materially from the negotiated level, or timestamp that does not match the actual trade time—the trade must be corrected. Corrections also flow through the tape and must meet tight deadlines.

A third hot spot is **conditional trade reporting**. Some trades are contingent on related transactions or are executed at prices conditional on future events. Firms must designate these correctly to comply with Rule 6730 and avoid creating false impressions about market prices.

## Enforcement and operational oversight

FINRA conducts regular audits of member firms' trade reporting systems. Examiners check logs, test systems, and review a sample of daily reports to confirm compliance. During these reviews, they look for patterns: Is a firm consistently late? Are there repeated data-quality issues? Is the firm using correct capacity designations?

Violations can result in censure, fines, or temporary suspension of trade reporting privileges. In severe cases—such as deliberate manipulation or systematic failure—FINRA can refer cases to the SEC or the Department of Justice for criminal prosecution.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative Trading System](/alternative-trading-system/) — electronic venues that also report trades through TRFs
- [Consolidated Tape](/securities-and-exchange-commission/) — the unified public record of all equity trades
- [Market Maker Trading](/market-maker-trading/) — how TRF reporting supports fair pricing and spreads
- [Regulation SHO](/regulation-a/) — short-sale rules that interact with trade reporting
- [FINRA](/finra/) — the self-regulatory authority overseeing TRFs and member compliance

### Wider context

- [SEC](/securities-and-exchange-commission/) — the regulator setting trade reporting standards
- [Stock Exchange](/stock-exchange/) — how exchange-listed trades differ from OTC reports
- [Price Discovery](/price-discovery/) — the role of transparent trade data in efficient markets

</div>

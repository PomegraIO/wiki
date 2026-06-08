---
title: "Consolidated Tape Mechanics"
description: "The system that aggregates last-sale trade reports from multiple US equity venues into a single unified real-time data stream."
keywords:
  - consolidated tape
  - tape A
  - tape B
  - tape C
  - market data
  - last-sale reporting
  - equity trading venues
image: /svg/markets.svg
---

*The consolidated tape is the unified record of every trade executed on US equity venues in real time. It merges reports from the New York Stock Exchange, NASDAQ, and all other registered markets into a single, standardized stream—allowing traders, investors, and regulators to see the true price at which stocks are actually changing hands, regardless of where the transaction occurred.*

## Why consolidation mattered

Before the consolidated tape was established in the 1970s, equity trading fragmented across multiple venues with no common reporting mechanism. A stock might trade at $50.00 on the NYSE and $50.05 on a regional exchange, with no one having a clear picture of which price was truly representative of the market. Investors had no systematic way to know whether they had received a fair deal. Traders could exploit these information gaps, executing in the dark and learning prices later, if at all.

The SEC mandated consolidated reporting to solve this fragmentation. The tape became the authoritative record—the source of truth for [price discovery](/price-discovery/) across the entire US equity market.

## The three tapes: A, B, C

The consolidated tape is divided into three separate data streams, each serving different venue categories:

**Tape A** reports trades from the [New York Stock Exchange](/new-york-stock-exchange/) and its affiliated venues. These are typically the largest, most actively traded stocks. Tape A data has been the gold standard of US market reporting since the beginning of consolidated reporting, as the NYSE was the primary venue for large-cap equities.

**Tape B** covers NASDAQ and other electronic communications networks (ECNs). When NASDAQ became a major competing venue in the 1980s and 1990s, and when alternative trading systems proliferated, Tape B was created to ensure that those venues' trades were reported alongside NYSE trades in a standardized format.

**Tape C** captures trades from regional exchanges and other smaller venues. Securities traded primarily on these venues flow through Tape C. While smaller in volume, Tape C is crucial for ensuring that even less liquid or smaller-cap stocks have centralized reporting.

All three tapes feed into a single real-time data stream that market participants subscribe to and use to gauge current prices.

## How a trade gets reported

When a stock changes hands on any registered exchange or alternative trading system, the venue has a regulatory obligation to report the trade to the appropriate [Securities and Exchange Commission](/securities-and-exchange-commission/)-approved processor within one to two seconds. The report includes the security identifier (such as the ticker), the price, the volume, and a timestamp.

The processor—which is typically operated by the exchange or by an agreed-upon third party—aggregates these reports and broadcasts them via the consolidated tape. A trader watching the tape sees the full sequence of transactions. If a stock trades 10,000 shares at $100.00 on one venue, then 5,000 shares at $100.05 on another, the tape will show both transactions in chronological order (or in the order the reports are received, to the millisecond).

This transparency is essential. It allows traders to assess whether they have executed at a competitive price and to adjust their strategies in real time. Regulators use the tape to monitor market integrity and detect suspicious activity.

## Last-sale vs. the limit order book

The consolidated tape records **last-sale data**—the price and volume of completed transactions. It does not show the [limit order](/limit-order/) book (the queued buy and sell orders waiting to be matched). The limit order book can differ significantly between venues; Tape A will show one picture of depth on the NYSE, while Tape B shows a different picture on NASDAQ.

This distinction matters for traders trying to assess the full state of supply and demand. The tape tells you what traded, but not what's waiting to trade. To see the full limit order book, a trader must subscribe to each venue's proprietary market data feeds—which is why large trading firms maintain separate connections to the NYSE, NASDAQ, and other exchanges.

## The role of SIPs

The actual mechanism for consolidating and distributing the tape is a Securities Information Processor, or SIP. The SEC oversees one or more SIPs per tape (historically, one SIP per tape). The SIP's job is to receive trade reports from all venues, sequence them, strip out duplicate reports, and broadcast the cleaned-up feed.

SIPs are mission-critical infrastructure. A SIP outage means the consolidated tape stops updating, which can trigger circuit breakers and trading halts. Because of this criticality, most major markets maintain backup SIPs. When Tape A goes down, a standby processor takes over within seconds.

## Latency and the data advantage

In modern trading, there is often a measurable delay between when a trade executes and when it appears on the consolidated tape. This delay—sometimes a few hundred milliseconds, sometimes more—creates an information asymmetry. A trader with a direct connection to an exchange's matching engine might see a trade microseconds before it appears on the public tape. High-frequency traders have long exploited this gap.

For this reason, many traders pay premium prices for "co-located" market data feeds—feeds that originate from servers sitting next to the exchange's matching engine. These feeds show data slightly before the consolidated tape does. This practice is legal but has drawn regulatory scrutiny, since it means some participants get the market picture faster than others.

## Modern consolidation challenges

As trading venues have proliferated—especially with the rise of alternative trading systems and dark pools—the consolidated tape faces scaling challenges. The volume of reports has grown exponentially. Some processors have struggled to keep up, introducing longer delays. The SEC has proposed various reforms to improve the speed and granularity of consolidated data, but implementation remains ongoing.

Additionally, there is ongoing debate about whether the current three-tape model is still optimal. Some observers argue that a single unified tape would simplify the system. Others prefer the status quo, contending that separate tapes allow for venue differentiation and competition.

## See also

<div class="wiki-seealso">

### Closely related

- [Price Discovery](/price-discovery/) — how markets aggregate information into agreed prices
- [Bid-Ask Spread](/bid-ask-spread/) — pricing layers across venues
- [New York Stock Exchange](/new-york-stock-exchange/) — major venue for large-cap trades
- Market Data — real-time information about trading activity
- [Secondary Market](/secondary-market/) — trading in already-issued securities

### Wider context

- [Stock Exchange](/stock-exchange/) — regulated venue for trading
- [Over-the-Counter Market](/over-the-counter-market/) — alternative reporting framework
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator
- [Alternative Trading System](/alternative-trading-system/) — non-exchange venues
- Order Flow — the sequence of customer demands

</div>
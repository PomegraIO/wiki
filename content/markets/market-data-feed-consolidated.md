---
title: "Consolidated Market Data Feed"
description: "The consolidated market data feed is the official, aggregated real-time data published by the Securities Information Processor, showing the best bid and ask prices across all US venues. It is the basis for regulatory compliance and is available to the public with a delay."
keywords:
  - consolidated data
  - market data
  - SIP data
  - NBBO
  - official quotes
  - real-time pricing
image: "https://picsum.photos/seed/market-data-feed-consolidated/900/600"
---

*The **consolidated market data feed** is the official, real-time aggregated market data published by the [Securities Information Processor](/sip-securities-information-processor), combining quotes and trades from all US venues. It provides the national best bid and offer (NBBO), trade reports, and other essential data. The consolidated feed is available to the public (with minimal delay) and is the basis for regulatory compliance and fair execution.*

<div class="wiki-hatnote">

This entry is about the official aggregated feed. For faster exchange-specific feeds, see [direct market data feed](/market-data-feed-direct); for the system producing it, see [SIP](/sip-securities-information-processor).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Consolidated Market Data Feed — key facts</div>

<img src="https://picsum.photos/seed/market-data-feed-consolidated/900/600" alt="A market data display showing consolidated NBBO quotes and trade volumes" />

<div class="wiki-infobox-caption">Consolidated feed is the official, public source of market data.</div>

|   |   |
|---|---|
| **Provider** | Securities Information Processor (SEC-authorized) |
| **Data type** | NBBO quotes, trades, volumes, timestamps |
| **Update frequency** | Real-time; millisecond latency for public |
| **Distribution** | Free delayed data; subscription for real-time |
| **Latency vs. direct feed** | 1–10ms slower |
| **Regulation** | SEC Rule 10b-2; mandated data |
| **Cost** | Low cost for retail; professional subscriptions higher |

</aside>

## Role and importance

The consolidated feed is the official market data source. It is mandated by SEC rules and serves as the basis for:

- **Regulatory compliance.** The SEC uses consolidated feed data to detect violations.
- **Best execution.** Brokers route orders to achieve [NBBO](/sip-securities-information-processor) as quoted on the consolidated feed.
- **Index calculations.** Market indices use consolidated feed prices.
- **Fair pricing.** Investors rely on consolidated feed quotes to understand fair market values.

## Data components

The consolidated feed includes:

**Quote information:**
- National best bid (highest price any venue is bidding).
- National best offer (lowest price any venue is asking).
- Size at each level.

**Trade information:**
- Executed trade price.
- Volume.
- Time of execution.
- Venue code.

**Aggregate volumes and statistics.** Opening prices, daily highs/lows, total volume.

## Latency characteristics

Consolidated feed latency varies but is typically:

- **Real-time for SIP subscribers:** 1–10 milliseconds from market event to data reception.
- **Delayed for public:** Professional-grade data is real-time; free retail data has a 15-minute delay.

This is slower than [direct exchange feeds](/market-data-feed-direct) but faster than historical standards.

## Public access

**Free delayed data:** Market data websites (Yahoo Finance, Google Finance, your broker's platform) show quotes delayed by 15 minutes.

**Real-time retail data:** Most brokers provide real-time quotes to active traders at no additional charge.

**Professional data:** Investment firms pay for real-time professional-grade feeds, often bundled with other data (fundamental data, news, etc.).

## Regulatory framework

The SEC mandates the consolidated feed under Rule 10b-2 and [Reg NMS](/reg-nms-detail). The feed must:

- Aggregate all venues fairly.
- Update in real time.
- Be accessible to the public (with limited delays for retail).
- Provide a basis for calculating fair prices.

## Consolidated feed vs. direct feeds: Trade-offs

| Aspect | Consolidated Feed | Direct Feeds |
|--------|-------------------|------------|
| **Latency** | 1–10ms | 10–500 microseconds |
| **Cost** | Low/free | High ($500–$10K+/month) |
| **Detail** | NBBO, top levels | Full order book |
| **Official status** | Yes, regulatory standard | No, venue-specific |
| **Fair to all** | Yes | No; favors fast participants |

Most retail investors use consolidated feed; institutions and HFTs use direct feeds for an advantage.

## Data normalization and consolidation process

The [SIP](/sip-securities-information-processor) process:

1. **Data collection.** Quotes and trades from all venues flow into the SIP.
2. **Aggregation.** The SIP combines data across venues for each symbol.
3. **NBBO calculation.** The best bid and ask are identified.
4. **Publication.** The consolidated tape is published to subscribers and the public.

This process is fully automated and occurs in near-real time.

## Use cases for consolidated data

**Regulatory monitoring.** The SEC and [FINRA](/broker) use consolidated feed data to detect market manipulation, insider trading, and violations.

**Index management.** S&P 500 prices are based on consolidated feed closing prices.

**Academic research.** Researchers use historical consolidated tape data to analyze market behavior.

**Retail investing.** Individual investors using consolidated feed data on their brokers' platforms make trading decisions.

**Benchmarking.** Fund managers benchmark their returns against market indices calculated from consolidated feed data.

## Limitations and criticisms

**Latency gap.** The [SIP](/sip-securities-information-processor) is slower than direct feeds, creating fairness concerns.

**Order routing constraints.** Brokers must route to the venue showing the NBBO, but by the time this appears on consolidated tape, the opportunity may have passed on direct feeds.

**Information asymmetry.** Participants with access to direct feeds see prices before retail investors using consolidated data.

## Future evolution

The SEC has periodically discussed speeding up the consolidated feed or harmonizing it with direct feed speeds to reduce information asymmetries. However, technological and competitive interests have prevented major changes.

## See also

<div class="wiki-seealso">

### Closely related

- [SIP](/sip-securities-information-processor) — produces consolidated feed
- [Consolidated tape](/consolidated-tape) — the trade data component
- [Direct market data feed](/market-data-feed-direct) — faster alternative
- [NBBO](/sip-securities-information-processor) — calculated from consolidated feed
- [Stock exchange](/stock-exchange) — source of consolidated feed data

### Wider context

- [Market data](/stock-market) — what the feed provides
- [Real-time pricing](/stock-market) — enabled by consolidated feed
- [Best execution](/broker) — based on consolidated feed
- [Regulation](/stock-market) — consolidated feed is mandated
- [Information asymmetry](/stock-market) — consolidated feed helps reduce this

</div>

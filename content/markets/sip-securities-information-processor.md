---
title: "Securities Information Processor"
description: "A Securities Information Processor (SIP) is a central facility that collects trade and quote data from multiple stock exchanges and over-the-counter markets and disseminates consolidated, real-time market data to the public. The SIP is the source of the official market price."
keywords:
  - SIP
  - securities information processor
  - market data
  - consolidated tape
  - real-time quotes
  - market infrastructure
image: "https://picsum.photos/seed/sip-securities-information-processor/900/600"
---

*A **Securities Information Processor (SIP)** is a centralized facility that aggregates quote and trade data from all US stock exchanges and [alternative trading systems](/alternative-trading-system), combines them, and disseminates consolidated market data in real time. In the US, the SIP is operated by exchanges and distributes data showing the best bid and ask prices and recent trades. The SIP is the official source of the national best bid and offer (NBBO) and is essential to fair market pricing.*

<div class="wiki-hatnote">

This entry is about the data aggregation mechanism. For the data feed it produces, see [consolidated tape](/consolidated-tape); for its regulatory framework, see [RegNMS](/reg-nms-detail).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Information Processor — key facts</div>

<img src="https://picsum.photos/seed/sip-securities-information-processor/900/600" alt="A data center facility processing market data from multiple exchanges" />

<div class="wiki-infobox-caption">The SIP aggregates data from all venues and publishes the consolidated national best bid and offer.</div>

|   |   |
|---|---|
| **Operator** | NYSE and NASDAQ jointly (in the US) |
| **Input data** | Quotes and trades from all venues |
| **Output** | Consolidated market data; NBBO |
| **Update frequency** | Millisecond-level real time |
| **Participants** | All market participants subscribe to SIP data |
| **Regulatory basis** | SEC Rule 10b-2 (amended by RegNMS) |
| **Cost** | Data subscriptions available to public; may have fees |

</aside>

## How the SIP works

The SIP collects data from multiple sources:

- All registered exchanges (NYSE, NASDAQ, other regional exchanges)
- Registered [alternative trading systems](/alternative-trading-system) ([dark pools](/dark-pool-detail), [lit venues](/lit-venue-detail))
- OTC market makers (for [over-the-counter](/over-the-counter-market) trades)

For each stock, the SIP receives:

- Quote data: The best bid (highest price a buyer will pay) and best ask (lowest price a seller will accept) at each venue.
- Trade data: Each executed trade's price and volume.

The SIP then aggregates this data across venues, calculates the **national best bid and offer (NBBO)** — the single best bid and ask across all venues — and disseminates this consolidated data to market participants and the public.

## The national best bid and offer (NBBO)

The NBBO is perhaps the most important market data point. It represents the best prices available anywhere in the US market for a security:

- **National best bid:** The highest price any buyer, anywhere, will pay for a stock.
- **National best offer:** The lowest price any seller, anywhere, will accept for a stock.

For example, if the NYSE has a bid at $100.00 and the NASDAQ has a bid at $99.99, the NBBO bid is $100.00. If the NASDAQ has an ask at $100.01 and NYSE has an ask at $100.02, the NBBO ask is $100.01.

Brokers are required by SEC Rule 10b-5 best execution obligations to route orders to the venue showing the NBBO (or better). This ensures that retail investors receive fair execution.

## Consolidated tape

The SIP produces the [consolidated tape](/consolidated-tape), a continuous stream of all trades in all US-listed stocks, in real time. This tape is the official record of what has traded and at what price.

## History and evolution

The SIP concept originated in the 1970s with the creation of the [consolidated tape](/consolidated-tape) system. Before that, each exchange maintained its own quotations and trades, and investors had no way to know what prices were available on other venues.

The SEC mandated the consolidation of trading and quote data, leading to the creation of the SIP operated by the major exchanges.

Over time, SIP delays have become a contentious issue. The SIP updates are not instantaneous; they are delayed by milliseconds due to data transmission. High-frequency traders exploit these delays by using direct exchange feeds, which are faster than SIP feeds. This has led to ongoing regulatory debate about SIP fairness.

## Direct exchange feeds vs. SIP feeds

Exchanges also offer **direct feeds** of their own data, separate from the SIP:

- **Direct feeds** are faster (microseconds to low milliseconds). Sophisticated traders subscribe to them and gain a speed advantage.
- **SIP data** is slower but official and fair; it is the basis for regulatory compliance and public quoting.

This two-tiered system has created a fairness concern: high-frequency traders with access to direct feeds see prices before the SIP-based public sees them, allowing exploitation of stale SIP data.

## Regulatory role

The SIP is central to market regulation. The SEC uses SIP data to:

- Verify trading volumes and prices.
- Detect manipulation or suspicious trading patterns.
- Calculate indices.
- Calculate volatility for circuit-breaker purposes.

The SEC and [FINRA](/broker) monitor SIP data for violations of trading rules.

## Global equivalents

Other countries have similar systems:

- **Europe:** ESMA regulates consolidated data under [MiFID II](/mifid-ii-trading).
- **UK:** The FCA mandates consolidated data reporting.
- **Japan:** The Japanese exchanges operate a similar consolidated data system.

## Criticisms and proposed reforms

**Speed inequality.** The SIP is slower than direct exchange feeds, creating an unfair speed advantage for well-capitalized traders. Proposals to speed up the SIP or harmonize speeds have been made but not implemented.

**Costs.** Data subscriptions to the SIP (and especially to premium direct feeds) can be expensive, creating access barriers for retail investors and smaller institutions.

**Accuracy.** The SIP occasionally experiences delays or errors, feeding stale or incorrect data. The 2010 flash crash was partly attributed to SIP delays causing traders to see incorrect quotes.

## See also

<div class="wiki-seealso">

### Closely related

- [Consolidated tape](/consolidated-tape) — the output of the SIP
- [RegNMS](/reg-nms-detail) — the regulatory framework
- [Stock exchange](/stock-exchange) — the source of SIP data
- [Alternative trading system](/alternative-trading-system) — feeds data to SIP
- [Market data](/stock-market) — what the SIP provides

### Wider context

- [Best bid and offer](/stock-market) — calculated by the SIP
- [Best execution](/broker) — regulated using SIP data
- [Price discovery](/stock-market) — facilitated by SIP transparency
- [Liquidity](/secondary-market) — displayed via SIP
- [High-frequency trading](/stock-market) — exploits SIP speed gaps

</div>

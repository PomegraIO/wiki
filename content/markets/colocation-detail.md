---
title: "Colocation"
description: "Colocation is the practice of placing trading servers physically near a stock exchange's data center to minimize network latency. Colocated traders receive market data microseconds faster than remote traders, providing a trading speed advantage in high-frequency trading."
keywords:
  - colocation
  - co-location
  - data center
  - trading infrastructure
  - proximity
  - latency reduction
image: "https://picsum.photos/seed/colocation-detail/900/600"
---

*The **colocation** of trading servers at a stock exchange's data center is a strategy used by high-frequency traders and institutions to minimize network latency. By locating their computers within the exchange's facility, traders receive market data and can execute orders microseconds faster than traders connecting remotely. Colocation is expensive and creates a tiered system where wealthier firms have a speed advantage.*

<div class="wiki-hatnote">

This entry is about infrastructure for trading speed. For latency more broadly, see [latency tier](/latency-tier); for the data accessed, see [direct market data feed](/market-data-feed-direct).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Colocation — key facts</div>

<img src="https://picsum.photos/seed/colocation-detail/900/600" alt="A server room at a stock exchange data center showing colocated trading systems" />

<div class="wiki-infobox-caption">Colocation places traders' servers meters from the matching engine.</div>

|   |   |
|---|---|
| **Cost** | $10,000–$100,000+ per year |
| **Latency advantage** | 1–10 milliseconds faster than remote |
| **Typical users** | High-frequency traders, major institutions |
| **Major exchanges** | NYSE, NASDAQ, CBOE, other US and global exchanges |
| **Speed improvement** | From 10–100ms (remote) to 0.1–10ms (colocated) |
| **Fairness concerns** | Creates unequal trading conditions |

</aside>

## How colocation works

A trader arranges with an exchange to place a server (housing their trading algorithms and order-routing software) in the exchange's data center, meters or feet away from the matching engine.

The colocated server connects to:

- **Market data feed:** Direct connection to the exchange's data publication system.
- **Order entry system:** Direct connection to the exchange's order acceptance.
- **Power and cooling:** Provided by the data center.

Result: The trader's algorithm receives market data and places orders with latency measured in microseconds, rather than milliseconds.

## Latency advantage math

**Remote trader:**
- Network latency to exchange: 5 milliseconds (data).
- Server processing: 1 millisecond.
- Network latency back: 5 milliseconds (order).
- Total: ~11 milliseconds.

**Colocated trader:**
- Server latency (within data center): 10 microseconds.
- Server processing: 1 millisecond.
- Exchange processing: 1 microsecond.
- Total: ~1.01 milliseconds.

The colocated trader is ~10 milliseconds faster. In high-frequency trading, this is an eternity; thousandfold more orders can be placed and executed.

## Costs

**Co-location rack fees:** $5,000–$20,000+ per month for server space, power, and cooling.

**Network connections:** $1,000–$5,000 per month for dedicated connections.

**Systems and staff:** Maintaining a colocated trading system requires dedicated engineers: $100,000–$500,000+ in annual salaries.

**Total annual cost:** $50,000–$200,000+ per exchange, easily $500,000+ for firms co-locating at multiple major exchanges.

This cost barrier means only well-capitalized firms can collocate.

## Who collocates

**High-frequency traders.** The primary users. Millisecond advantages can generate millions in profits; the colocation cost is easily justified.

**Large asset managers.** Firms with substantial assets under management may collocate for algorithmic trading.

**Broker-dealers.** Investment banks often co-locate to provide the best execution.

**Market makers.** Designated market makers at exchanges typically co-locate to maintain fair quotes.

Retail investors never co-locate; the infrastructure is far too expensive.

## Exchange policies

Exchanges offer co-location services and profit from the fees. However, exchanges have adopted policies to prevent unfair advantages:

- **Equal access.** All qualified market participants can access co-location (though at a cost).
- **Fairness rules.** Orders must be processed in a fair, orderly manner, regardless of co-location.
- **Dispute resolution.** Exchanges have processes to review complaints of unfair advantages from co-location.

Despite policies, co-location inherently creates information asymmetries: colocated traders see prices microseconds before remote traders.

## Controversies

**Unfair advantage.** Colocated traders have an unfair edge over retail investors with remote access.

**Flash crash contribution.** During the 2010 flash crash, colocated high-frequency traders' rapid response to cascading prices helped accelerate the decline.

**Wealth transfer.** Some argue that co-location-enabled high-frequency trading is wealth transfer from retail investors to well-capitalized HFTs.

**Systemic risk.** The concentration of colocated systems at exchanges creates operational risk; if a data center fails, many traders are affected.

## Global colocation

Major exchanges globally offer co-location:

- **US:** NYSE, NASDAQ, CBOE, and others.
- **EU:** Euronext, LSE, Deutsche Börse.
- **Asia:** Tokyo Stock Exchange, Shanghai Stock Exchange, others.

This globalization of co-location has enabled high-frequency trading worldwide.

## Regulators and proposals

Some propose limiting or eliminating co-location advantages:

- **Speed bumps.** Introduce artificial delays so all traders experience uniform latency.
- **Auction systems.** Instead of continuous order matching, use periodic auctions where speed confers less advantage.
- **Mandatory slow-down.** Slow down all systems to eliminate microsecond advantages.

However, no major regulatory changes have been implemented. Exchanges resist, as co-location is profitable for them.

## See also

<div class="wiki-seealso">

### Closely related

- [Latency tier](/latency-tier) — colocation reduces this
- [High-frequency trading](/stock-market) — enabled by colocation
- [Direct market data feed](/market-data-feed-direct) — used by colocated traders
- [Stock exchange](/stock-exchange) — offers colocation services
- [Market microstructure](/stock-market) — shaped by colocation

### Wider context

- [Trading infrastructure](/stock-market) — colocation is part of
- [Speed advantage](/stock-market) — colocation provides this
- [Information asymmetry](/stock-market) — created by colocation
- [Fair execution](/broker) — challenged by colocation
- [Systemic risk](/stock-market) — colocation data center failures pose this

</div>

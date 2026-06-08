---
title: "Securities Information Processor"
description: "The central utility consolidating and disseminating real-time quotes and trade data across US equity markets."
keywords:
  - securities information processor
  - sip
  - consolidated tape
  - market data
  - price discovery
  - market regulation
image: "/svg/trading.svg"
---

*A **Securities Information Processor** (SIP) is the official consolidator of real-time quote and trade information from every US equity trading venue. Three competing SIPs—each assigned to a subset of exchanges and [alternative trading systems](/alternative-trading-system/)—collect bids, asks, and execution data, then republish it as the "consolidated tape." This feed is the backbone of [trade-through rule](/trade-through-rule/) enforcement, order routing, and price discovery across modern fragmented markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Securities Information Processor — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for market infrastructure." />

<div class="wiki-infobox-caption">The central utility that publishes the national best bid and ask to enforce fair execution.</div>

|   |   |
|---|---|
| **What it is** | A consolidator and publisher of quotes and trades across all US equity venues |
| **Current operators** | Intercontinental Exchange (ICE), Nasdaq, Cboe—each runs one SIP |
| **Primary data** | Best bid/ask (top-of-book) and all executed trades reported within seconds |
| **Key output** | Consolidated tape: the official national best bid and offer (NBBO) |
| **Regulatory role** | Enables enforcement of the [trade-through rule](/trade-through-rule/) and market surveillance |
| **Clients** | Brokers, traders, market makers, investors, and regulators |
| **Fee model** | Participants pay fees based on data volume and distribution rights |

</aside>

## The fragmentation problem a SIP solves

Before electronic trading fragmented equities across multiple venues, price discovery was simple: look at the NYSE. One exchange, one official quote. When regional exchanges, NASDAQ, and electronic communication networks began competing in the 1990s, the market split. At any moment, the best bid on one venue might be $50.10, while the best ask sits at $50.05 on another—creating a paradox for investors. Neither quote matches the other, and no investor knows which prices are truly "the best" unless information is consolidated.

The SEC solved this by creating the SIP framework: a central utility that pulls real-time quotes from every trading venue, identifies the best bid and ask nationwide (the national best bid and offer, or NBBO), and publishes it to the entire market. This allows brokers, traders, and regulators to enforce fair execution rules and maintain confidence that prices are discovered transparently.

## How a SIP collects and publishes data

Each venue—the [NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), regional exchanges, and alternative trading systems—continuously sends its top-of-book quotes (the best bid and ask for every security) and all executed trades to the assigned SIP. The SIP collects this data from hundreds of venues and thousands of securities, processes it in real time, and publishes a consolidated quote (NBBO) and consolidated last-sale tape (the official reported trade) within milliseconds.

For example, if Apple stock's best bid is $175.50 on NYSE and $175.51 on NASDAQ, the SIP publishes $175.51 as the national best bid. If a broker executes a customer's order at $175.49, that violates the trade-through rule—the execution was at an inferior price relative to the published NBBO. Enforcement depends entirely on the SIP's accuracy and speed.

The three SIPs (ICE, NASDAQ, and Cboe) each operate one of the three original Regulation SHO "plan processors." They divide responsibility: one handles NYSE-listed stocks, one handles NASDAQ-listed stocks, and one handles securities listed on other exchanges. All three publish their tape to ensure redundancy and fair access.

## The incentive problem: who pays, and are prices fast enough?

SIPs are utilities, not for-profit entities in the traditional sense. They charge fees to participants (exchanges, brokers, and data subscribers) based on quote volume and data distribution. Yet this fee structure creates tension. Venues want to charge brokers money to access their best quotes faster than the SIP distributes them—an incentive to delay SIP publication. Brokers, in turn, face pressure to pay for "enhanced" feeds that show quotes microseconds before they hit the official consolidated tape.

In 2023, the SEC proposed to revamp SIP fees and fee-setting governance, aiming to reduce operator profits and speed up consolidated data distribution. Critics argue that the current SIP model is too slow (consolidation introduces 1–2 millisecond delays) and too expensive, and that it props up incumbent exchanges at the cost of innovation. Defenders counter that the current system has maintained market integrity and fairness for three decades.

## The role of SIPs in regulatory oversight

Regulators rely on SIP data for market surveillance. The SEC and [FINRA](/), the industry self-regulator, use consolidated tapes to detect suspicious patterns—layering (placing and canceling fake orders), spoofing (algorithm manipulation), and wash trades (round-tripping to inflate volume). A trade that seems normal on one venue might be flagged as suspicious when analyzed against SIP data from all venues. Market disruptions (such as flash crashes) also depend on SIP data for post-mortems: regulators rewind the tape to reconstruct exactly what happened across the market.

Without a central SIP, fragmentation would have made market surveillance nearly impossible. The consolidation function is not just about investor protection—it is about maintaining orderly markets and preventing systemic fraud.

## Technical reality: delays and the speed arms race

In practice, the SIP is not truly real-time. There is a 1–2 millisecond delay between a trade execution at a venue and its appearance on the consolidated tape. For retail investors, this is imperceptible. For high-frequency traders operating at microsecond speeds, it is an eternity. This gap creates an arbitrage: a trader with access to raw venue feeds (not yet consolidated) can sometimes execute a strategy based on information that the SIP has not yet published. Critics argue this gives high-frequency traders an unfair edge; defenders argue the delays are unavoidable given the volume of data flowing through the system.

The SEC's modernization efforts aim to shrink these delays and make the SIP faster and cheaper. But each improvement faces technical and cost challenges: consolidating data from hundreds of venues at sub-millisecond latency requires significant infrastructure investment, and those costs are ultimately borne by market participants.

## See also

<div class="wiki-seealso">

### Closely related

- [Trade-Through Rule](/trade-through-rule/) — the protection that depends on SIP-published NBBO to prevent execution at inferior prices
- [Market Microstructure Theory](/market-microstructure-theory/) — the academic framework explaining how information and market structure shape prices
- [Consolidated Tape](/consolidated-tape/) — the official price and trade data published by the SIP across all venues
- [Price Discovery](/price-discovery/) — the process by which prices incorporate all available information; SIP consolidation enables this
- [Alternative Trading System](/alternative-trading-system/) — venues whose quotes feed into the SIP consolidation

### Wider context

- [Stock Exchange](/stock-exchange/) — the primary trading venues whose quotes the SIP consolidates
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator that oversees SIP operations and fees
- [Market Maker Trading](/market-maker-trading/) — market makers post quotes that flow into the SIP
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between best bid and ask; SIP publishes this spread nationally

</div>

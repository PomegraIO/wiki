---
title: "Post-Trade Transparency and Reporting Obligations"
description: "What must be reported after a trade executes—price, size, time, and venue. How deferred waivers work for large trades under MiFID II and Dodd-Frank."
keywords:
  - post-trade transparency reporting
  - trade execution transparency
  - deferred publication waiver
  - transaction reporting
  - market transparency
  - mifid ii reporting
image: "/svg/trading.svg"
---

*After a trade executes, **post-trade transparency reporting** requires that the price, size, time, and venue be published to the market within minutes—ensuring all investors see the same execution data and can verify fair dealing. Large block trades can qualify for deferred publication waivers, delaying disclosure to protect market impact.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Post-Trade Transparency — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Regulatory requirement to disclose executed trades promptly.</div>

|   |   |
|---|---|
| **Core requirement** | Publication of price, size, time, and venue within minutes of trade execution |
| **Deferred waiver threshold** | Block trades exceeding size thresholds (varies by asset class and jurisdiction) |
| **Publication timeline** | EU (MiFID II): 15 minutes for equities; up to 5+ hours for deferred waivers |
| **US jurisdiction** | SEC/FINRA rules require prompt publication; large trades can request exceptions |
| **Exemptions** | Systematic internalisation, pre-trade large investor waivers, certain OTC derivatives |
| **Venue reporting** | Trades typically reported to regulated reporting facilities (MTFs) or exchanges |

</aside>

## Why post-trade transparency matters

The principle is simple: when a trade settles, the financial world should know the facts. Without transparency, investors cannot independently verify that a [broker](/broker/) executed their order fairly, large players cannot gauge whether recent trades were at outlier prices, and regulators cannot detect manipulative patterns. Transparency also deters price improvement schemes where a dealer quietly fills a customer's order at a worse price than the market.

Mandated post-trade reporting became a cornerstone of modern regulation after the 2008 financial crisis, particularly under the [Dodd-Frank Act](/dodd-frank-act/) in the United States and MiFID II in the European Union. The logic is that if you can see what executed, you can make better decisions about your next trade.

## What must be reported

A complete post-trade transaction report includes:

- **Price**: The actual execution price.
- **Size**: The number of shares or contract units traded.
- **Time**: When the trade occurred, typically to the second or millisecond.
- **Venue**: Where the trade was executed (exchange, multilateral trading facility, systematic internaliser, or over-the-counter market).
- **Party identifiers**: In regulated markets, identities may be anonymised for small trades but revealed for large ones.
- **Instrument identifier**: ISIN code, ticker, or equivalent.

The responsible party—usually the trading venue, the broker, or a designated [reporting facility](/alternative-trading-system/)—must push this data into feeds that professional investors and market data vendors access. Retail investors may see it through their brokers' interfaces or public databases within a slight delay.

## The deferred publication waiver

Not all trades report immediately. A **deferred publication waiver** allows certain trades—typically large blocks—to delay disclosure, sometimes for days. The rationale is practical: imagine a pension fund selling a 500,000-share block in a mid-cap stock. If that hit the tape instantly, prices would crater, and the final price would be worse than if the sale had remained opaque until completion.

### How deferred waivers work

Under MiFID II, a trade in an equity qualifies for a deferral if it exceeds a size trigger—such as the "large in scale" threshold (roughly 50% of average daily volume). The matched trades may be reported immediately, but the full size might be withheld until:

- A set time later that day (e.g., end of trading).
- The next calendar day.
- Up to five calendar days later for *very* large trades in lower-liquidity stocks.

After the deferral period ends, the full transaction is published. The waiver does not hide the trade forever; it merely postpones the shockwave.

### US approach (Regulation SHO, Form 4)

The SEC has parallel rules. Large trades in [equities](/common-stock/) can request an exception from the standard two-minute reporting window—a process called a "trade throughs" or block exemption—allowing publication to be delayed by hours under certain conditions. The logic mirrors MiFID II: let the market digest the information in stages rather than as a sudden volume shock.

## Who does the reporting

Reporting is typically a shared responsibility:

- **Venues** (exchanges and multilateral trading facilities) report trades that occur on their platform.
- **Systematic internalisers** (firms that match customer orders in-house) report their own trades.
- **Investment firms** (brokers and dealers) report OTC trades and client-facilitated trades.
- **Reporting facilities** (approved entities) act as a third-party hub for venues and firms that prefer to delegate the task.

In practice, a large [bank](/jpmorgan-chase/) may run a systematic internaliser desk, reporting thousands of OTC trades daily through a facility. A stock exchange reports exchange-matched trades directly. A broker handling a customer's block trade with another client's order will ensure both sides report via the venue or facility.

## Exceptions and exemptions

Not everything must report in real time:

- **OTC derivatives**: Subject to regulatory delays; some complex structures may report daily rather than minute-by-minute.
- **Pre-trade waivers**: A large investor announcing its intention to trade may receive a waiver allowing negotiated trades to settle before reporting.
- **Systematic internaliser exemption**: Certain matched-principal trades on small venues may defer reporting under narrower conditions.
- **Market making**: [Market makers](/market-maker-trading/) may receive short reporting delays for their own-account activity (typically up to 15 minutes in EU markets).

These exemptions are narrow and granted case-by-case; regulators tighten them over time.

## Regulatory oversight and compliance

Violations of post-trade reporting rules carry heavy penalties. Regulators—the SEC, FINRA, and FCA (UK)—audit venues and firms quarterly, checking that transaction reports are complete, accurate, and timely. A trade missing from the report, a misstated price, or a delayed publication can trigger warnings, fines, and (in egregious cases) enforcement action.

Compliance technology is expensive. Larger brokers run dedicated reporting teams and validate feeds before submission. A single error—such as reporting a JPY trade in GBP—can flag a surveillance system.

## Market impact and best execution

Post-trade transparency directly affects how traders execute large orders. A trader who knows that large blocks will eventually be visible has an incentive to split orders across multiple venues and times, minimizing the visible footprint at any single moment. This fragmentation is a secondary effect of transparency: in trying to avoid the market's knowledge of a large order, traders route volume across [alternative trading systems](/alternative-trading-system/) and over-the-counter venues.

Conversely, when deferred waivers are wide (allowing long delays), traders have less urgency to fragment; they can execute a large block and know they have hours to complete the next block before the first is published.

## See also

<div class="wiki-seealso">

### Closely related

- [Broker](/broker/) — Executes trades and reports on your behalf.
- [Alternative Trading System](/alternative-trading-system/) — Venues where trades execute and are reported.
- [Market Maker Trading](/market-maker-trading/) — Benefits from reporting delays under certain exemptions.
- [Dodd-Frank Act](/dodd-frank-act/) — Mandated transparency rules in the US.
- [Price Discovery](/price-discovery/) — How transparency affects the market's knowledge of fair value.
- [Execution Risk](/execution-risk/) — Risks of slippage, partial fills, and visibility.

### Wider context

- [Stock Exchange](/stock-exchange/) — Primary venue for transparent reporting.
- [Over-the-Counter Market](/over-the-counter-market/) — Often has looser transparency rules.
- [Fragmented Market](/fragmented-market/) — How traders navigate multiple venues to minimise visibility.

</div>

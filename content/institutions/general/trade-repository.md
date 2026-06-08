---
title: "Trade Repository"
description: "Regulated data warehouses that collect and aggregate OTC derivatives transaction reports to enable systemic risk surveillance and regulatory oversight."
keywords:
  - otc derivatives
  - trade reporting
  - systemic risk
  - regulatory oversight
  - transaction data
  - derivatives registry
image: "/svg/institutions.svg"
---

*A [Trade Repository](/trade-repository/) (often abbreviated TR) is a regulated database that aggregates transaction-level data on [OTC derivatives](/option/) trades. Market participants report each trade to a designated TR, which then makes the data available to [regulators](/securities-and-exchange-commission/), [central banks](/central-bank/), and the public, enabling systemic-risk monitoring and enforcement of anti-fraud rules.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade Repository — key facts</div>

<img src="/svg/institutions.svg" alt="An editorial mark for financial institutions." />

<div class="wiki-infobox-caption">The regulatory infrastructure for transparency and systemic oversight of OTC derivatives.</div>

|   |   |
|---|---|
| **Primary role** | Collect and publish OTC derivatives transaction reports |
| **Data captured** | Counterparties, notional amount, [counterparty risk](/counterparty-risk/), pricing terms |
| **Mandatory for** | Most standardised OTC derivatives post-2012 regulatory reform |
| **Key users** | Regulators, [central banks](/central-bank/), market participants |
| **Regulator** | [SEC](/securities-and-exchange-commission/), CFTC (US); national authorities elsewhere |
| **Reporting lag** | Near real-time to end-of-day, depending on jurisdiction |

</aside>

## The pre-trade-repository world

Before the 2008 financial crisis, OTC derivatives were almost entirely opaque. An institution might sell billions of dollars in [credit derivatives](/credit-risk/) to unknown counterparts, and neither the seller, the buyer's risk manager, nor any regulator had a complete picture of the exposures flowing through the system. [Counterparty risk](/counterparty-risk/) was hidden. Leverage was unmeasured. When Lehman Brothers failed in September 2008, it held massive OTC derivatives positions that had been largely invisible to the outside world, and unwind those positions required days of frantic negotiation among dozens of counterparts.

This opacity was not accidental—it was a feature of OTC markets. Bilateral trades between sophisticated institutions operated under a veil of confidentiality. Pricing was opaque, terms varied widely, and the regulatory gaze was distant. This suited some participants (dealers could capture spreads) but created systemic vulnerability. No one—not a regulator, not even a major bank's risk committee—had a bird's-eye view of aggregate OTC derivatives risk.

Trade repositories emerged from the post-2008 regulatory consensus: transparency was a public good, and systemic risk could not be managed without data.

## Mandate and structure

A trade repository is a private or public entity licensed and supervised by national financial regulators. In the United States, the Commodity Futures Trading Commission (CFTC) licenses TRs for derivatives; in Europe, the European Securities and Markets Authority (ESMA) does the same. Each TR must meet standards for data security, completeness, timeliness, and access.

The mandate is straightforward: market participants (dealers, funds, corporates) must report [OTC derivatives](/option/) trades to a designated TR within a defined window—typically within minutes or hours of execution. The TR then:

- **Aggregates** transaction data from thousands of market participants
- **Standardises** the data (converting bilateral variations into a common schema)
- **Stores** the data in a secure, audited system
- **Publishes** anonymised transaction data to the public (with a time lag)
- **Makes raw data available** to regulators, central banks, and in some cases the counterparts to a trade

## What gets reported and when

The reporting requirement covers most [standardised derivatives](/currency-volatility/): [interest-rate swaps](/interest-rate/), [credit default swaps](/credit-risk/), [currency forwards](/currency-risk/), and [commodity futures](/crude-oil/) that do not trade on exchanges. The grandfathering rules are complex—some pre-crisis trades were exempted—but the general principle is that if a derivative is not traded on a [regulated exchange](/stock-exchange/) and does not go through a [clearinghouse](/stock-exchange/), it must be reported.

Data fields include the names of both counterparties (in regulatory reports; anonymised in public data), the notional amount, the effective date, the maturity date, pricing terms, and [counterparty risk](/counterparty-risk/) metrics. For credit derivatives, the reference entity is recorded. For [interest-rate swaps](/interest-rate/), the fixed rate and floating index are recorded.

The reporting window varies by jurisdiction. US CFTC rules typically require reporting within 15 minutes of trade execution; European rules are similar. This near-real-time requirement means regulators can monitor flows almost as they happen, rather than weeks or months later.

## Regulatory surveillance and systemic-risk monitoring

The primary user of trade-repository data is the regulator and the [central bank](/central-bank/). By aggregating all reported trades, authorities can:

- **Identify concentrations**: If one institution is a counterpart in 30% of all interest-rate derivatives traded, that concentration is a systemic vulnerability.
- **Monitor leverage**: A hedge fund's notional derivatives exposure can be cross-referenced with its reported [asset allocation](/asset-allocation/) and equity positions to flag excessive [leverage](/leverage-ratio-forex/).
- **Detect fraud**: Unusual pricing or repeated trades between the same pair of institutions can signal collusion.
- **Model contagion**: If Institution A's derivatives counterparties include Institution B, which in turn is exposed to Institution C, a chain of dependencies can be mapped.

Central banks use trade-repository data in [stress testing](/stress-testing/) and [liquidity-risk](/liquidity-risk/) scenario analysis. If rates spike 200 basis points, what institutions face mark-to-market losses on their derivatives positions? Which of those institutions are also highly leveraged? Would they be forced to liquidate positions, causing a fire-sale cascade?

## Market transparency and the public record

Beyond regulatory surveillance, TRs publish anonymised transaction data to the public, usually with a time lag (e.g., end-of-day). This public data allows independent analysts, academics, and competing dealers to see aggregate market trends: the average fixed rate on interest-rate swaps, the implied [volatility](/implied-volatility/) in credit derivatives, the volume of flows in specific markets.

This transparency serves competition. Before trade repositories, dealers could claim "we got you a great rate" without the client being able to verify that claim independently. Now, with public pricing data from all TRs aggregated, a client can compare their trade to market medians and negotiating power improves.

However, the transparency is imperfect. Counterparty names are redacted in public data, and there is typically a reporting lag. So while the market can see aggregate trends, real-time bilateral positioning remains partly hidden. This is by design: regulators wanted systemic-risk visibility and fraud prevention, not a tool for front-running individual dealers.

## Challenges and limitations

Trade repositories have grown substantially since the Dodd-Frank Act and similar post-2008 reforms. But challenges persist:

**Data quality**: Different TRs use different schemas and data standards. Aggregating data across multiple repositories is tedious. A single standardised schema would improve the signal.

**Coverage gaps**: Some derivatives—particularly those between non-regulated institutions or bespoke structures—still fall outside reporting. Regulatory perimeters are constantly debated.

**Cyber risk**: A TR is a honeypot for hackers. Regulators mandate security, but data breaches are an ongoing threat.

**Timeliness**: The near-real-time reporting standard is better than pre-2008, but it is not instantaneous. A [counterparty](/counterparty-risk/) can still suffer a default between trade execution and the moment that information is reported and available to risk managers.

## Integration with central clearing and settlement

Trade repositories are often paired with central [clearinghouses](/stock-exchange/) in a coordinated regulatory model. The clearinghouse is the counterparty to every trade (novation), and the trade repository logs the transaction. This dual infrastructure—clearing for credit risk mitigation, repositories for transparency—became the post-2008 standard.

Some institutions operate both functions (clearing and data aggregation); others operate only as repositories. [Payment versus delivery](/payment-versus-delivery/) infrastructure and clearing are separate from repositories, though all three are interdependent: trades are reported to repositories, cleared through clearinghouses, and settled via central infrastructure.

## See also

<div class="wiki-seealso">

### Closely related

- [OTC derivatives](/option/) — the instruments whose transactions populate trade repositories
- [Counterparty risk](/counterparty-risk/) — the systemic vulnerability that repositories help monitor
- [Clearinghouse](/stock-exchange/) — the infrastructure that often works alongside TRs to mitigate credit risk
- [Payment versus delivery](/payment-versus-delivery/) — settlement infrastructure distinct from reporting but coordinated with TRs
- [Self-regulatory organisation](/self-regulatory-organisation/) — industry bodies that work with regulators to enforce TR reporting
- [Securities and exchange commission](/securities-and-exchange-commission/) — US regulator overseeing TRs

### Wider context

- [Systemic risk](/systemic-risk/) — the phenomenon TRs are designed to illuminate
- [Central bank](/central-bank/) — user of TR data for [financial stability](/systemic-risk/) purposes
- [Forward contract](/forward-contract/) — a common OTC derivative reported to TRs
- [Dodd-Frank Act](/dodd-frank-act/) — the regulatory framework mandating trade repositories

</div>

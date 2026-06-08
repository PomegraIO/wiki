---
title: "Clearing Fees Explained"
description: "How clearing fees work in futures and options; per-contract and per-trade charges, who pays, and how fees flow between exchange, CCP, and clearing members."
keywords:
  - clearing fees how it works
  - futures clearing fees per contract
  - options clearing fees
  - how much clearing fees cost
  - clearing member fees
image: "/svg/institutions.svg"
---

*A **clearing fee** is the charge a clearinghouse (or CCP, central counterparty) assesses for each trade executed and/or each contract held open.* These fees are separate from the [brokerage commission](/broker/) a trader pays to the exchange and the bid-ask [spread](/bid-ask-spread/). They flow from the trader, through the clearing member (broker), through the exchange, and to the clearinghouse. Understanding how clearing fees work reveals why a trader's true cost of a futures or options trade is often higher than the headline commission, and why clearinghouses must remain solvent and well-staffed to manage systemic risk.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing Fees Explained — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">Clearing fees are assessed per trade or per open contract and are collected by the CCP to cover operational costs and build a default fund.</div>

|   |   |
|---|---|
| **Fee structure** | Per-trade and/or per-contract; usually tiered by volume |
| **Typical range** | $0.10–$2.00 per contract; varies by asset class |
| **Who collects** | Clearinghouse (CCP); flows through exchange and clearing member |
| **Who pays** | Trader; deducted from settlement or charged to brokerage account |
| **Fee uses** | Operational costs, technology, default fund, risk management |
| **Clearing member rebates** | Large members may negotiate lower rates or rebates |

</aside>

## The Basic Structure

A clearing fee is charged in two main ways:

1. **Per-trade fee:** Assessed when a trade is executed. A trader buys one crude oil futures contract; the clearinghouse charges, say, $0.50 for the trade. If the trader closes the position the same day, two trades (buy and sell) incur two fees.

2. **Per-contract fee (or per-diem):** Assessed each day a contract is held overnight. A trader holds a crude contract overnight; the clearinghouse charges, say, $0.10 per day per contract for clearing. A 30-day hold incurs roughly $3 in clearing fees (not including per-trade charges at entry and exit).

Most clearinghouses use a blend of both: a per-trade charge plus a daily holding charge. The per-trade fee incentivizes efficient execution and discourages excessive order cancellations; the per-contract fee ensures the clearinghouse recovers costs from longer-term positions.

## Who Pays and How It Flows

The **end trader** pays the clearing fee, but it flows through layers:

1. The trader's **broker** (a clearing member or a broker that clears through a member) collects the fee from the trader's account at settlement or deducts it from daily profits/losses.

2. The broker passes the fee to the **exchange**, which recorded the trade.

3. The exchange passes the bulk of the fee to the **clearinghouse** (CCP), retaining a small portion for the exchange's own costs.

4. The clearinghouse retains the fee to cover operational expenses and builds a default insurance fund.

In practice, many exchanges and clearinghouses are vertically integrated. The Chicago Mercantile Exchange (CME), for example, owns its own clearinghouse (CME Clearing). The fee structure is published, but the internal allocation between exchange revenue and clearing costs is opaque. The key point: the trader bears the cost, regardless of the internal split.

## Typical Fee Levels

Clearing fees vary widely by asset class:

- **Equity index futures (e.g., S&P 500):** Typically $0.80–$1.20 per contract round-trip (entry and exit).
- **Crude oil and agricultural futures:** Often $0.50–$1.00 per contract round-trip.
- **Interest rate futures:** Cheaper, often $0.15–$0.30 per contract round-trip, because volume is high and risk is lower.
- **Equity options:** Usually $0.05–$0.15 per contract; lower absolute cost because contracts are smaller.
- **FX derivatives:** Depends on the venue; cleared FX swaps may have per-side fees of $0.10–$0.50.

Large clearing members (major banks, market makers) negotiate lower rates. A member executing 1 million contracts per month might receive a 30–50% rebate on standard fees. Retail traders pay the full standard rate through their brokers.

## What Clearing Fees Fund

The clearinghouse uses clearing fee revenue for:

1. **Operations:** Staff salaries, technology platforms, data centers, compliance monitoring.

2. **Default fund:** A portion of clearing fees is held as a default insurance pool. If a clearing member defaults, the default fund is the first line of defense before the clearinghouse taps other members' capital. The default fund often equals 1–3 months of anticipated clearing fees.

3. **Risk management:** Marking-to-market systems, margin calculation algorithms, stress testing, liquidity monitoring.

4. **Regulatory compliance:** Reporting systems, audits, regulatory filings mandated by the SEC, CFTC, or local regulators.

5. **Technology upgrades:** New matching engines, blockchain or distributed-ledger pilots, cybersecurity hardening.

6. **Insurance and hedging:** Protection against operational risk.

A well-capitalized clearinghouse invests clearing fee revenue to remain solvent and trustworthy. A underfunded clearinghouse becomes a source of systemic risk—if a major member defaults, there may not be enough in the default fund to cover losses, forcing the clearinghouse to socialize the loss across remaining members (and ultimately, traders).

## Fee Impacts on Trading Strategy

Clearing fees affect the profitability of short-term strategies. A day trader executing 100 round-trips per day on crude oil futures pays:

- 100 trades × $0.75/contract = $75/day in clearing fees alone.
- Over a month (20 trading days), that's $1,500 in clearing fees.

For a trader making $20,000/month, clearing fees are 7.5% of gross profit—a meaningful drag. High-frequency traders and market makers negotiate rebates precisely because they cannot otherwise survive. A retail trader executing just 10 round-trips per month absorbs only $7.50 in clearing fees, which is negligible if the trades are profitable.

Clearing fees also influence the bid-ask [spread](/bid-ask-spread/). Market makers must recover their clearing fees, so spreads on instruments with high clearing fees tend to be wider, all else equal. A market maker in a lightly-traded instrument with high clearing fees cannot afford to post tight spreads.

## Tiering and Volume Discounts

Clearinghouses often publish tiered fee schedules:

- **Tier 1:** If a clearing member clears 0–100,000 contracts per month, the fee is $1.00/contract.
- **Tier 2:** 100,001–500,000 contracts per month, $0.80/contract.
- **Tier 3:** 500,001+ contracts per month, $0.60/contract.

This tiering incentivizes large participants to consolidate clearing at one clearinghouse (or one member of a clearinghouse) and discourages fragmentation. It also means the marginal cost of additional volume is lower, encouraging order flow.

## The Clearing Member's Margin

A clearing member must maintain sufficient capital to cover operational losses and defaults. This capital is distinct from the [initial margin](/variation-margin-vs-initial-margin/) and [variation margin](/variation-margin-vs-initial-margin/) charged to individual traders. Clearing members also pay access fees and contribute to the default fund, in addition to processing clearing fees for their clients.

## International Variations

Different clearinghouses have different fee structures:

- **CME Clearing (Chicago):** Per-contract plus per-trade; publicly disclosed; rebates for high volume.
- **Eurex Clearing (Frankfurt):** Different fee structures for different asset classes; higher for complex instruments.
- **LCH (London):** Operates multiple clearinghouses (LCH Ltd, LCH SA); fee structures vary by venue.
- **Smaller or regional clearinghouses:** May charge higher absolute fees due to smaller volumes and higher per-contract operational costs.

A trader choosing between venues or brokers should compare clearing fees in addition to brokerage commissions.

## See also

<div class="wiki-seealso">

### Closely related

- [Variation Margin vs Initial Margin](/variation-margin-vs-initial-margin/) — clearing fees are charged alongside margin requirements
- [Open Interest and Clearing](/open-interest-and-clearing/) — how contracts are counted for per-contract fee basis
- [Broker](/broker/) — the intermediary who collects clearing fees on behalf of the clearinghouse
- [Bid-Ask Spread](/bid-ask-spread/) — market makers recover clearing fees through spreads
- [Counterparty Risk](/counterparty-risk/) — why clearinghouses need fees to fund default insurance

### Wider context

- [Stock Market](/stock-market/) — how fees are charged on exchanges and clearinghouses
- [Futures Contract](/futures-contract/) — the primary cleared instrument
- [Option](/option/) — also cleared with per-contract fees
- [Central Bank](/central-bank/) — oversees clearinghouse solvency and fee adequacy
- [Systemic Risk](/systemic-risk/) — how clearinghouse underfunding creates contagion

</div>

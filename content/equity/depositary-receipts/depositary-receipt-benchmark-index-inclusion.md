---
title: "Depositary Receipt Inclusion in Benchmark Indexes"
description: "ADRs and GDRs are treated inconsistently across major stock indexes. Some count as separate eligible securities; others apply stricter dual-listing rules, liquidity thresholds, or exclude them entirely."
keywords:
  - do adrs count in stock market indexes
  - adr index inclusion
  - depositary receipt benchmark indexes
  - adr index weight
image: /svg/equity.svg
---

*Whether a **depositary receipt** counts as an eligible security for stock market indexes varies by index vendor. While ADRs and GDRs reference foreign shares, major indexes—the S&P 500, MSCI World, FTSE—apply differing rules on eligibility, weighting, and rebalancing. Some treat ADRs as distinct securities; others tie inclusion to the underlying foreign listing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ADR and GDR Index Treatment — three models</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Index providers differ on whether receipts are treated as native securities or as proxies for foreign shares.</div>

|   |   |
|---|---|
| **S&P Global** | Dual-listing model; ADR counts only if underlying is also eligible |
| **MSCI** | Underlying foreign share determines eligibility; ADR not separately weighted |
| **FTSE Russell** | Home-market listing rule; receipt must meet UK/EU standards |
| **Nasdaq/NYSE listing** | Required; sole US-listed receipt may still require underlying dual-listing |
| **Liquidity threshold** | ADR must meet exchange volume and market-cap minimums (varies by index) |
| **Rebalancing** | ADR weight driven by underlying share price; currency effects compound |

</aside>

## The Dual-Listing Rule

The most common barrier is the **dual-listing requirement**. S&P Global, one of the largest index publishers, treats a depositary receipt as eligible for inclusion in the S&P 500, S&P 1500, or regional benchmarks only if the underlying foreign security is simultaneously listed on an acceptable home-country exchange.

Why this matters: if a Chinese company lists its ADR on the NYSE but has no concurrent listing on the Shanghai Stock Exchange or Hong Kong Stock Exchange, the ADR would not qualify for the S&P 500 under this rule. Conversely, a company with a liquid ordinary listing in London and a corresponding ADR on the Nasdaq may be eligible, because the underlying satisfies the home-market criteria.

This creates a practical barrier: the issuer must accept the cost and regulatory compliance of maintaining two concurrent listings—one in the home market and one via ADR in the US. Many companies choose sole US listing via ADR to simplify regulatory burden, but this choice disqualifies them from many major indexes.

## MSCI and Emerging-Market Treatment

MSCI (Morgan Stanley Capital International) takes a different approach. It does not separately weight an ADR as an independent security. Instead, MSCI indexes are built around a "home-market bias" model: a company's weighting is determined by its listing in its primary market. If the company is included in the MSCI Emerging Markets Index or another regional index, an ADR of the same company is not separately added to those indexes with its own weight.

However, MSCI does allow ADRs as *tactical holdings* within certain index variants or as part of adjusted methodology for specific countries. A Panamanian holding company with a primary foreign listing and a US ADR may be weighted based on the primary listing, with the ADR available as an administrative convenience for fund managers unable to access the home market directly.

The practical effect: fund managers seeking to replicate an MSCI index will usually purchase the underlying ordinary shares in the home market, not the ADR, because the weighting is anchored to the home listing.

## FTSE Russell Frameworks

FTSE Russell (London Stock Exchange Group's index division) applies similar home-market weighting rules for its primary benchmarks like the FTSE All-Share and FTSE 100. An ADR of a UK-listed company is not separately eligible for inclusion in the FTSE 100; the underlying ordinary share is. The same applies to FTSE indexes tracking European and other international securities.

FTSE also imposes stricter liquidity and corporate-governance standards on ADRs than on home-market listings, reflecting the reality that ADR trading volume is often lower than the underlying security's volume in its primary market.

## Liquidity and Volume Thresholds

All major indexes impose minimum trading volume and market-capitalization requirements. An ADR must meet these thresholds independently—even if the underlying foreign share is highly liquid, the ADR itself must demonstrate:

- Minimum daily trading volume (often $2–5 million for large-cap indexes)
- Minimum market cap in the ADR (not just the underlying)
- Bid-ask spread within acceptable bounds
- Average trading activity over a reference period

Small ADRs—those traded infrequently or in minimal volumes—fail these tests and cannot enter most broad benchmarks, regardless of the underlying company's size. This is a major reason why many smaller international companies opt for sole listing in the US via ADR but never gain index membership.

## Currency and Rebalancing Effects

ADR weighting incorporates currency exposure that the underlying share does not. An ADR's dollar price is determined by:
- The underlying foreign share price (in its local currency)
- The currency exchange rate between that currency and the US dollar
- The ADR/ordinary share ratio (e.g., 1 ADR = 5 ordinary shares)

When an index is rebalanced and the dollar weakens against a particular foreign currency, the ADR's dollar weight rises, even if the underlying company's home-market share price remains flat. This complicates index calculations and can create arbitrage opportunities between the ADR and the underlying share in the home market.

Index managers must decide whether to rebalance based on the ADR price alone (in dollars) or to calculate rebalancing based on the underlying share price adjusted for currency. Different index families apply different rules.

## Sector and Geographic Classifications

Major indexes also classify ADRs by geography and sector. An ADR of a Chinese industrial company is classified as China (not the United States), even though the ADR trades on the NYSE. This means it would not be eligible for the S&P 500 (a US-equity index), even if the dual-listing rule were satisfied.

Conversely, some index methodologies allow an ADR to "inherit" US classification if it has been US-listed for a threshold period (e.g., 12 months) and the underlying company has significant US operations or revenue. This is rarer and applies mainly to specialized or country-specific benchmarks.

## Corporate-Action and Dividend Complications

When the underlying company undergoes a corporate action—a stock split, dividend payment, or recapitalization—the ADR ratio may change. The depositary adjusts the ADR-to-ordinary-share ratio to preserve economic equivalence. Index providers must then recalculate weights and may trigger unintended rebalancing.

Dividend payments via ADR often incur currency conversion costs and may be subject to withholding-tax treaties that differ from those applied to direct foreign shareholding. Indexes factor this into their treatment of ADR yield and total return calculations.

## Practical Implications for Fund Managers

An actively managed or index-tracking fund seeking to match a major benchmark must understand these rules:

- If the benchmark includes only home-market listings, the fund should purchase ordinary shares in the primary exchange, not ADRs, to avoid basis tracking error.
- If the benchmark allows ADRs, the fund can use them where home-market access is expensive or restricted (e.g., non-residents unable to directly hold certain Chinese A-shares).
- Replicating an index using ADRs alone may diverge from the benchmark's actual weights due to currency and liquidity effects.

Some funds maintain both ordinary shares and ADRs of the same security to achieve optimal execution and cost.

## See also

<div class="wiki-seealso">

### Closely related

- [ADR](/adr/) — definition and structure of American Depositary Receipts
- [Index fund](/index-fund/) — passive funds tracking benchmark indexes
- [Market capitalization](/market-capitalization/) — key criterion for index eligibility
- [Liquidity risk](/liquidity-risk/) — affects ADR trading volumes and index rebalancing costs

### Wider context

- [Stock market](/stock-market/) — primary venues for equity trading
- [Stock exchange](/stock-exchange/) — national and international listing standards
- [Diversification](/diversification/) — rationale for multi-country index inclusion
- [Currency risk](/currency-risk/) — exchange-rate effect on ADR valuations

</div>

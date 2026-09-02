---
title: "Trade Reporting Requirements"
description: "Rules mandating the disclosure of executed trades to regulators and market participants for transparency and enforcement purposes."
keywords:
  - trade reporting
  - market transparency
  - regulatory disclosure
  - transaction reporting
---

*Every exchange and trading venue must report executed trades to regulators and, increasingly, publish them in real time or near-real time so market participants can verify fair pricing and regulators can detect manipulation.*

<aside class="wiki-infobox">

| Aspect | Details |
|---|---|
| Primary regulators | SEC, FINRA, CFTC, NFA |
| Key systems | FINRA Trade Reporting Facilities (TRF), OATS |
| Reporting delay (equities) | Same-day or next-day in US; T+2 settlement |
| Reporting delay (options) | Same-day to SEC |
| Data elements | Price, quantity, time, counterparties, venue |
| OTC enforcement | DTCC Trade Information Warehouse (TIW) |

</aside>

## Why trade reporting matters

Markets work best when prices are transparent. If a stock trades at $50 in one venue and $51 in another, without anyone knowing, traders cannot find the best price. Regulators also need to see all trades to detect manipulation—spoofing, layering, and wash trades hide in the gaps between venues. Trade reporting rules close those gaps by mandating that every trade be reported to a central clearinghouse.

The basic requirement is simple: within a defined window (same day, next day, or T+2 depending on the asset and venue), the executing broker must report the price, quantity, time, and identifying information to the regulatory authority or a delegated trade reporting facility. The trade is then timestamped and, in many cases, published to the public in real time or near-real time.

## Equity trades and FINRA trade reporting

In the US equity market, brokers must report trades to one of FINRA's Trade Reporting Facilities (TRF) or to the exchange where the trade occurred. The [consolidated tape](/wiki/consolidated-tape/) (managed by the Securities Information Processors, or [SIPs](/wiki/sip-securities-information-processor/)) then disseminates the trade data to the public via feeds like CQS (for listed stocks) and UTP (for Nasdaq stocks) with minimal latency.

Most trades report within 2 minutes; high-volume venues may achieve sub-second reporting. The SIPs were designed to level the playing field—all traders get the same consolidated price feed—but they have become bottlenecks. The SEC has periodically reviewed whether to replace the SIP model with a decentralized or faster approach, but as of 2026, the consolidated tape remains the standard.

## Regulatory complexity: OTC derivatives

Over-the-counter (OTC) derivatives, especially [swaps](/wiki/swap/) and [credit default swaps](/wiki/credit-default-swap/), faced a reporting void before the 2008 financial crisis. No one could see the entire OTC market; only individual dealers knew their bilateral counterparties and positions. The [Dodd-Frank Act](/wiki/dodd-frank-act/) mandated that most OTC derivatives be reported to Swap Data Repositories (SDRs)—centralized databases run by vendors like DTCC (Trade Information Warehouse), Bloomberg, and FactSet.

These SDR reports include trade details, but publication to the public is more limited than equity trades. The SEC and CFTC use SDR data for surveillance and enforcement but have not published the full historical SDR database. This creates asymmetry: regulators see the data; the public does not. Supporters argue this protects proprietary trading strategies; critics say it undermines market transparency.

## Reporting delays and market impact

A key tension is between timeliness and market stability. Real-time reporting of every trade can telegraph large orders and enable predatory trading (a large buyer's first trade is seen, triggering price jumps before the remaining orders execute). The SEC has allowed "large trader" and "block trade" exceptions: trades above a size threshold can be reported with a delay (often 1–2 minutes) or without exact venue routing, protecting the initiator from being front-run.

In equity futures (CBOT, CME), the reporting standard is often T+0 (same day), but "flash reporting" (public dissemination of trade details in near real-time) also has exceptions for large trades to minimize market impact.

## International frameworks and MIFID II

The European Union's MiFID II directive (Markets in Financial Instruments Directive, revised) has similar trade reporting requirements. Trades must be reported to regulators (in each member state and to ESMA, the European Securities and Markets Authority) and, for most transactions, published in real time on regulated data feeds. The EU was more aggressive than the US in mandating real-time public transparency.

This creates challenges for global banks operating across regions: the same trade may be reportable under US rules, EU rules, and UK rules (post-Brexit), each with slightly different formats and timelines. Compliance systems must map across jurisdictions.

## Technology and market data feeds

A secondary effect of trade reporting is the creation of market data feed businesses. The SIPs publish consolidated data; private vendors (Bloomberg, Reuters, Refinitiv) repackage it with analytics. Traders subscribe to multiple feeds—some get OPRA (options pricing) and CQS (equities) from SIPs; others pay for colocation and direct feeds from exchanges for faster access. This creates a pecking order: fastest traders (at colocation centers) see prices microseconds before retail traders receiving SIP data—legal but contentious.

## Enforcement and surveillance

The core purpose of trade reporting is to give regulators a permanent, timestamped record of market activity. The SEC's Division of Enforcement uses trade-by-trade reports to reconstruct suspicious trading patterns. If a stock spikes on rumored takeover news, the SEC can subpoena trade data, identify unusual volume, and find whether insiders or tipped parties traded ahead of the announcement.

Spoofing (placing and canceling large orders to manipulate prices) is nearly impossible to hide when every trade is reported. The CFTC brought hundreds of spoofing cases in the 2010s, all built on trade data analysis.

## Exemptions and loopholes

Large traders and sophisticated investors have negotiated exemptions. Block trades above a size threshold (often $200k–$500k in equities) can trade off-exchange and report with a delayed timestamp. Systematic Internalizers (SIs) can report trades with short delays. These exemptions exist because forcing real-time reporting of every block trade would make large portfolio trades impossible—the orders would be seen and front-run. The trade-off between transparency and market functionality is explicit here.

<div class="wiki-seealso">

### Closely related
- [Consolidated Tape](/wiki/consolidated-tape/) — the system that publishes reported trades.
- [Market Surveillance](/wiki/market-surveillance/) — the enforcement use of reported data.
- [Dodd-Frank Act](/wiki/dodd-frank-act/) — mandated OTC derivatives reporting.

### Wider context
- Regulation (Securities Laws) — the broader regulatory framework.
- [FINRA](/wiki/finra/) — administrator of US equity trade reporting.
- [OTC Derivatives](/wiki/over-the-counter-market/) — the asset class with complex reporting.

</div>

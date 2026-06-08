---
title: "Order Audit Trail System (OATS) and Its Replacement by CAT"
description: "FINRA's order audit trail system (OATS) required broker-dealers to record all orders, trades, and cancellations; it was replaced by the SEC's CAT in 2021."
keywords:
  - order audit trail system
  - oats finra
  - consolidated audit trail cat
  - broker-dealer compliance
  - trade surveillance
  - regulatory audit trail
---

*The **Order Audit Trail System (OATS)** was a FINRA rule that required [broker-dealers](https://www.investopedia.com/terms/b/broker/) to record every order submitted, amended, or cancelled—who entered it, when, and what happened to it. For two decades it was the watchdog for order integrity and surveillance. In 2021, the SEC's **Consolidated Audit Trail (CAT)** took over, with a broader scope and stricter standards.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OATS and CAT — A Regulatory Handoff</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">FINRA's decades-old trade-audit rule gave way to a consolidated SEC standard, raising compliance burden but deepening market transparency.</div>

|   |   |
|---|---|
| **OATS span** | 1997–2021 |
| **Adopted by** | FINRA (self-regulatory organisation) |
| **What it tracked** | Every order (buy, sell, cancel, amend) plus execution details |
| **Retention period** | 6 years |
| **CAT adoption** | 2021 (phased implementation through 2024) |
| **CAT scope** | All orders on all US exchanges and venues; includes cancel/replace activity, timing to microsecond precision |
| **CAT retention** | 7 years |
| **Key difference** | CAT is SEC-led, centralised, and captures cross-venue activity in one database |

</aside>

## The origins and purpose of OATS

OATS emerged in 1997 as a [FINRA](https://www.investopedia.com/terms/f/finra/) (then NASD) initiative to solve a fundamental compliance problem: broker-dealers processed thousands of orders daily, and regulators had no reliable way to reconstruct what happened. Was an order cancelled deliberately or by error? Did an execution price match the best available? Did a broker favour one client over another? Without a timestamped record, proving violations was nearly impossible.

OATS required member firms to record each order electronically, with timestamps, order status, size, price, account number, and the account type (retail, institutional, proprietary). When an order was partially or fully executed, firms logged the execution time and price. If a trader cancelled or amended an order, that action was recorded too.

The rule was mandatory for equities trading and most options trading; firms built systems to capture and report the data to FINRA daily or in real time. Regulators could then run surveillance algorithms to spot patterns: a pattern of scalping (entering and exiting at tiny spreads), layering (spoofing the order book), or front-running (trading ahead of a large customer order).

## How OATS worked in practice

A trader at a brokerage enters an order to buy 1,000 shares of XYZ at the market. The order-entry system timestamps it, assigns it an order ID, and routes it to an exchange. The exchange matches 700 shares at $50.15; the system logs that partial fill. The remaining 300 shares sit in the order book. Twenty seconds later, the trader cancels it; the system logs the cancellation timestamp.

All of this data—order entry time, partial execution, cancellation time—went into OATS reporting. The timestamps were critical: regulators could reconstruct the *sequence* of events and match it against [suspicious activity](https://www.investopedia.com/terms/m/market-abuse/), such as orders placed and cancelled within milliseconds to create the illusion of demand.

Firms were also required to assign a "account type" code (retail, professional, proprietary) and an "associated person" code (the trader or system that entered the order). This allowed regulators to track individuals and link unusual patterns to specific people across multiple firms.

OATS data retention was six years, so at any point a regulator could pull up orders from the past six years and audit them. [FINRA](https://www.investopedia.com/terms/f/finra/) used OATS as the foundation for much of its market-surveillance work, particularly for detecting [insider trading](https://www.investopedia.com/terms/i/insidertrading/) and [manipulative trading](https://www.investopedia.com/terms/m/market-manipulation/).

## Limitations and the push for CAT

Despite its success, OATS had structural flaws. Each firm maintained its own OATS database; FINRA received the submissions but they were siloed by broker. If a trader at one firm and a trader at another firm were colluding to manipulate a stock, seeing the full picture required manual cross-firm analysis. There was also no unified timestamp—different firms' clocks could be off by fractions of a second, making it hard to sequence events across exchanges.

Also, OATS covered broker-dealers but not all trading venues. Alternative trading systems (ATSs) had looser reporting rules. A significant fraction of US equities trading moved to non-traditional venues, and their order trails were harder to tie together.

After the 2008 financial crisis and the 2010 "flash crash," regulators saw the need for something more comprehensive. The [Dodd-Frank Act](https://www.investopedia.com/terms/d/dodd-frank-act/) of 2010 called for a centralised audit trail. The SEC proposed the **Consolidated Audit Trail (CAT)**, which would become the standard in 2021.

## How CAT superseded OATS

The SEC and all major US exchanges built CAT as a single, centralised database. Every broker-dealer and venue is required to report orders, trades, and cancellations in real time (or near-real time) to CAT. A single trade is reported once, with microsecond precision timestamps, ensuring that a buy on NASDAQ and a sell on the CBOE can be matched with absolute clarity on timing.

CAT covers all asset classes: equities, options, and future plans for other venues. The data retention period extended to seven years, and the database is built to allow for sophisticated cross-venue queries.

Compliance with CAT is far more stringent than OATS. Firms must ensure accurate order-entry systems, atomic timestamps, and reporting to CAT within strict timeframes. The penalties for late or inaccurate reporting are significant.

OATS formally ended in 2021, though firms had a transition period. Firms had to ensure that all historical OATS records were migrated or archived; CAT became the single source of truth for market surveillance.

## The impact on market participants

For most traders and investors, CAT is invisible—they do not see the audit trail or interact with it directly. But the compliance burden on broker-dealers is substantial. IT teams had to upgrade systems, ensure microsecond-precision clocks, and validate data flows. Many smaller firms outsourced CAT compliance to service providers.

For regulators, CAT unlocked new investigative capabilities. A [FINRA](https://www.investopedia.com/terms/f/finra/) investigator can now pull a single report showing all orders and trades involving a suspected spoofing scheme, with perfect timing, across all venues. The SEC uses CAT to monitor for systemic risks, such as the correlation between order cancellations and price moves.

For the public, CAT strengthens trust in market integrity. Manipulators and front-runners have nowhere to hide; every order is timestamped and linked to an individual or system. The transparency has also enabled better academic research on market structure and order behavior.

## See also

<div class="wiki-seealso">

### Closely related

- [FINRA](/finra/) — The self-regulatory organisation responsible for overseeing broker-dealers; administered OATS before the SEC took over audit-trail regulation with CAT.
- [Broker-Dealer](/broker/) — A firm that buys and sells securities; subject to order-entry and audit-trail rules under both FINRA and SEC.
- [Dodd-Frank Act](/dodd-frank-act/) — The 2010 legislation that mandated a centralised audit trail and strengthened post-crisis market oversight.
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The federal regulator that designed and operates CAT.
- Market Manipulation — Illegal practice of placing orders or trades to deceive or distort prices; audit trails help detect it.

### Wider context

- Insider Trading — Trading on material non-public information; audit trails are a key tool for detecting it.
- [Alternative Trading System](/alternative-trading-system/) — A non-exchange venue for trading securities; now required to report to CAT like traditional exchanges.
- Compliance — The process of ensuring that firms follow applicable rules and regulations.
- [Stock Exchange](/stock-exchange/) — A centralised venue where standardised securities are traded; primary source of orders and trades in CAT.
- [Price Discovery](/price-discovery/) — The process by which prices are determined; audit trails support the transparency that enables efficient price discovery.

</div>

---
title: "T+1 Settlement"
description: "Settlement cycle in which securities trades are completed one business day after execution, replacing the previous two-day standard."
keywords:
  - T+1 settlement
  - settlement cycle
  - trade settlement
  - market infrastructure
  - settlement acceleration
  - market operation
image: "/svg/regulation.svg"
---

*The **T+1 settlement** cycle requires that securities trades settle (cash and securities exchanged) on the business day after the trade is executed, rather than two days after ("T+2"). This acceleration reduces the window of time during which both parties face counterparty risk and operational uncertainty. The US fully transitioned to T+1 in May 2024, a change driven by technological capability and a desire to reduce systemic fragility.*

<div class="wiki-hatnote">

For the historical T+2 cycle, see [Settlement Finality Rules](/settlement-finality-rules/). For the regulatory framework of settlement generally, see [Securities Exchange Act of 1934](/securities-exchange-act-of-1934/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">T+1 Settlement — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">One-day settlement cycle reduces post-trade risk for both parties.</div>

|   |   |
|---|---|
| **What it is** | Securities settlement on the next business day after trade execution |
| **Transition date (US)** | May 2024 |
| **Prior standard** | T+2 (two business days) |
| **Coverage** | Equities, corporate bonds, municipal bonds |
| **Regulator** | SEC; SIFMA coordinated with industry |
| **Expected benefits** | Reduced counterparty risk, faster capital availability, lower operational costs |
| **Implementation challenge** | Compressed timeline for clearance, treasury verification, and fund transfers |

</aside>

## The shift from T+2 to T+1

US securities settled on a T+3 basis (three days after trade) for decades. In 2015, the SEC mandated T+2, which reduced counterparty exposure and freed up capital faster. By the early 2020s, technology had advanced sufficiently for T+1. In February 2024, the SEC published a final rule mandating T+1 settlement, effective May 2024. Unlike the T+3-to-T+2 transition, the move to T+1 required changes throughout the entire trading and post-trade ecosystem: brokers, custodians, payment systems, and data providers all had to compress their timelines.

## Mechanics of T+1 settlement

On a T+1 cycle, when a trade is executed on Monday, settlement occurs on Tuesday. The buyer must have funds available (or margin credit arranged) by market close on Tuesday. The seller must have the security in their account (or be able to short it, if permitted) by market close on Tuesday. The settlement instructions (the detailed routing of cash and securities) must be sent, matched, and processed by the clearing house by the deadline.

The compressed timeline affects multiple parties. Brokers must confirm trades and send settlement instructions to the clearing house within hours of trade execution, not the full day they previously had. Custodians must reconcile their positions and be ready to receive or deliver securities by Tuesday close. Fund managers must ensure their deposit accounts have sufficient funds or that their brokers have arranged credit lines. Foreign investors must arrange for currency conversion (if needed) one day faster.

The transition required significant investment in automation and coordination. Brokers upgraded their back-office systems. Custodians accelerated their settlement processes. Stock exchanges and clearinghouses like the Options Clearing Corporation and the Fixed Income Clearing Corporation adjusted their schedules to complete nightly processing and daytime matching and settlement confirmation within tighter windows.

## Benefits and rationale

The primary benefit of T+1 is the reduction in [counterparty risk](/counterparty-risk/). In the period between trade and settlement, both the buyer and seller face the risk that the other party will default, fail to deliver, or become insolvent. Longer settlement windows mean longer exposure. T+1 cuts this exposure by a full business day.

From the buyer's perspective, T+1 accelerates the availability of capital. Money received from a sale can be reinvested or loaned out one day sooner, compounding into material returns for large institutions. From the seller's perspective, the ability to access proceeds faster reduces the need for bridge financing and lowers the cost of trading.

Operationally, shorter settlement windows reduce the number of failed trades (fail-to-delivers) that must be managed or bought-in. Fewer failures mean less regulatory monitoring and lower capital charges for failures on the balance sheet.

At a systemic level, T+1 reduces financial fragility by eliminating a full day of bilateral counterparty exposure across the entire market. During periods of stress (such as 2008 or 2020), the concern is that a default by one major dealer could trigger a cascade of defaults by other dealers exposed to that dealer's obligations. Tighter settlement reduces the magnitude of those exposures at any given moment.

## Operational challenges

The compressed timeline revealed bottlenecks hidden during longer settlement windows. Payment systems like Fedwire and CHIPS had to optimize processing to handle surges in payment instructions. Municipal bonds faced challenges because many trade OTC with less automated infrastructure; the SEC granted temporary exemptions. Corporate bonds also required coordination for bilateral settlement. International traders had to navigate different settlement cycles in different markets.

## Technology and automation

T+1 required significant investment in automation. Brokers implemented systems to automatically match, confirm, and submit settlement instructions within minutes of trade execution. Custodians deployed algorithms to predict settlement failures. The accelerated timelines forced firms to eliminate manual processes; digitisation was no longer optional. This actually reduced errors and improved overall efficiency.

## Cost and impact on market structure

The transition to T+1 shifted rather than eliminated costs. Brokers saved on financing but incurred system-upgrade expenses. Custodians faced higher operating costs but these were largely one-time.

Concern that T+1 might disadvantage retail investors led to extended settlement windows (T+2 or T+3) offered at a premium, creating a two-tier system. Early data suggests trading costs did not rise significantly, though bid-ask spreads on some OTC instruments widened modestly.

## Global context and future directions

Most major markets operate on settlement cycles shorter than T+2. The EU and many other jurisdictions have considered or adopted T+1 or faster. T+0 (same-day settlement) remains technically feasible but would require significant market redesign, delayed market close, or continuous settlement infrastructure—changes unlikely to be adopted absent another financial crisis.

T+1 represents the practical equilibrium: it reduces counterparty risk and accelerates capital availability while remaining operationally feasible within existing payment systems and global trading frameworks.

## See also

<div class="wiki-seealso">

### Closely related

- [Settlement Finality Rules](/settlement-finality-rules/) — legal framework making settled trades irrevocable
- [Custodian](/custodian/) — institutions that hold securities and execute settlement
- [Counterparty Risk](/counterparty-risk/) — exposure that T+1 shortens for both parties
- [Securities Exchange Act of 1934](/securities-exchange-act-of-1934/) — foundational law under which T+1 is mandated
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator that set the T+1 transition date
- [Stock Exchange](/stock-exchange/) — venue on which trades are executed and settlement is managed

### Wider context

- [Short-Sale Circuit Breaker](/short-sale-circuit-breaker/) — regulatory rule that interacts with settlement timing
- [Market Manipulation Prohibition](/market-manipulation-prohibition/) — enforcement framework that relies on settlement finality
- [Over-the-Counter Market](/over-the-counter-market/) — bilaterally settled market where T+1 implementation was slower
- [Broker](/broker/) — intermediary managing settlement on behalf of clients
- [Systemic Risk](/systemic-risk/) — settlement compression reduces contagion risk

</div>

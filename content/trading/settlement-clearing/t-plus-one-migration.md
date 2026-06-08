---
title: "T+1 Settlement Migration"
description: "The operational and technological challenge of compressing equity settlement from two days to one, reshaping margin, liquidity, and clearance timelines."
keywords:
  - settlement-speed
  - market-infrastructure
  - clearing-timeline
  - margin-requirements
image: "/svg/trading.svg"
---

*The shift from T+2 (trade date plus two business days) to T+1 settlement marks the most fundamental compression of equity clearing cycles in decades. Markets on both sides of the Atlantic have begun or mandated the transition, forcing brokers, custodians, and [central counterparties](/central-counterparty-clearing/) to rebuild decades-old plumbing for speed.*

## Why settlement speed matters at all

Settlement is the moment money and securities actually change hands after a trade. Between trade and settlement, counterparties risk one another: the buyer's cash might be frozen; the seller's securities might be recalled. The shorter this window, the lower the [counterparty risk](/counterparty-risk/), the less capital locked in [margin](/margin-call-forex/), and the fewer collateral management headaches for brokers.

T+2 became standard in most developed markets in the 1990s because settlement infrastructure—payment systems, depository networks, and back-office clearing—could not reliably complete anything faster. T+1 was technically possible but regarded as operationally untidy. The pandemic, however, crystallized the issue: tighter credit conditions meant every hour of locked-up capital became visibly expensive.

## The operational bottleneck

The real constraint is not the clearinghouse's computer speed but the cascading flow of data and cash across a chain of intermediaries. When you buy a stock at 3:55 p.m., your broker must:
- Receive your instruction and confirm it
- Send a trade report to the exchange and clearinghouse
- Calculate intraday margin and collateral moves
- Instruct its custodian or clearing member
- Coordinate with the seller's broker and custodian
- Deliver securities from the [depository](/central-securities-depository/) (DTC in the US, Euroclear in Europe)
- Move cash through the settlement bank or payment rail

Each step involves human review in many firms still running 1990s-era systems. Compressed to T+1, all that work must complete overnight. For the US SEC mandate (effective May 2024), brokers retooled:
- Straight-through processing (STP) became mandatory, not optional
- Back-office staff expanded into evening shifts
- Custodians built urgent exception-handling queues
- Retail brokers pushed settlement failures to client accounts within hours rather than days

The challenge is magnified across borders. A US equity traded by a London fund manager settles through a German custodian—each layer adds latency.

## Margin and liquidity pressure

T+1 compresses the margin calendar. Under T+2, a broker could pool margin across days and smooth liquidity demands. Under T+1, a large trader who buys 100 million in US equities must now source margin (or cash) by the next morning. [Margin calls](/margin-call-forex/) arrive earlier, triggering forced selling in distressed positions.

For clearinghouses, T+1 means:
- Intraday margin calculations run twice as often (default funds must cover two settlement cycles)
- [Variation margin](/variation-margin/) adjustments become daily rather than next-day
- Liquidity demands on clearing members spike during morning settlement windows

Prime brokers warn that clients with tight cash management schedules may see funding strains. Smaller asset managers relying on repo financing discovered they need more cash buffer under T+1, raising funding costs.

## Cross-border and FX complexity

Settlement time is measured in business days *and* clock hours. A US equity can settle T+1 in New York, but when a European investor's instruction must route through London, undergo FX conversion, and settle at DTC, the actual window shrinks. European regulators moved to T+1 in late 2024, but misalignment remains:
- Asia and Australia still use T+2, forcing coordinated settlement windows
- Corporate actions (dividends, splits) announce ex-dates based on the *settlement* calendar, not trade date; T+1 changes which investors own shares at cutoff
- Cross-currency transactions now risk settlement mismatches—the euro leg settles T+1 in TARGET2, but the dollar leg settles T+1 in FEDWIRE on different clock times

The [clearing member default management](/clearing-member-default-management/) procedures also tighten. A member's default used to leave a 24–36 hour window to auction positions; T+1 compresses it to roughly 12 hours, forcing auction engines to run faster.

## Who bore the cost

Retail brokers absorbed heavy technology bills—some estimated $5–20 million to rebuild systems. Custodians and clearing members passed costs to smaller clients or withdrew from unprofitable segments. Asset managers with legacy order management systems (OMS) hired contractors to manually instruct settlement by late afternoon.

The compliance calendar shifted too. Previously, firms could discover and cure settlement fails overnight; now, fails are visible at market open and incur penalties immediately. Some market participants argued for T+1 in large-cap liquid stocks only, deferring smaller caps to T+2, but regulators rejected bifurcation as operationally unclean.

## The structural winners and losers

Central banks and clearinghouses reduced systemic risk—cash flowed faster, collateral chains shortened. Large bulge-bracket dealers, already running 24-hour trading floors, absorbed the cost and gained efficiency. Retail traders saw no visible benefit; execution quality and costs remained the same.

The losers were clear: regional brokers in emerging markets that depended on T+2 float financing, and fund managers whose investment theses assumed multi-day settlement windows for tactical repositioning.

## What didn't change

Speed of *execution* remained untouched. A stock still prints at 9:47 a.m., and most trades still execute in milliseconds. T+1 compressed only the post-trade pipeline. Some market participants had hoped the shift would spur real-time settlement (second-by-second or intraday), but regulators deemed the infrastructure unprepared and the benefit unclear for most instruments.

## See also

<div class="wiki-seealso">

### Closely related

- [Clearing Member Default Management](/clearing-member-default-management/) — how a CCP auctions a defaulting member's portfolio
- [Central Counterparty Clearing](/central-counterparty-clearing/) — the institution that sits between buyers and sellers
- [Securities Dematerialization](/securities-dematerialization/) — the shift from paper to electronic book-entry settlement
- [Omnibus Account Structure](/omnibus-account-structure/) — how custodians pool securities for settlement efficiency
- Settlement Bank — the agent managing cash transfer at settlement
- [Variation Margin](/variation-margin/) — daily collateral adjustments to cover mark-to-market moves
- [Counterparty Risk](/counterparty-risk/) — the risk that the other party to a trade fails before settlement

### Wider context

- Custody and Segregation — how brokers hold client assets
- Regulatory Framework for Clearing — rules governing CCP behavior
- Market Infrastructure — the plumbing connecting traders, exchanges, and settlement
- [Credit Risk](/credit-risk/) — the broader concept T+1 was designed to reduce
- [Liquidity Risk](/liquidity-risk/) — how settlement timings affect cash management

</div>

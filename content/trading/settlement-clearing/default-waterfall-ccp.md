---
title: "CCP Default Waterfall"
description: "The ordered sequence of financial resources a central counterparty exhausts when a clearing member defaults or becomes unable to meet obligations."
keywords:
  - CCP default waterfall
  - clearing house default
  - clearing member default
  - CCP recovery
  - default management
image: "/svg/trading.svg"
---

*A CCP default waterfall is the ranked sequence of pools of money and collateral that a clearing house taps in order when a member defaults. It is a carefully engineered shield designed to absorb defaults without cascading to other members. The first line of defence is usually the defaulter's own collateral; the next is the CCP's capital and insurance fund; the last is a charge against surviving members. Understanding the waterfall is essential to evaluating a CCP's safety and the true cost of clearing membership.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CCP Default Waterfall — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading, settlement, and market operations." />

<div class="wiki-infobox-caption">The financial bulwark that protects a clearing house and its members when one member goes down.</div>

|   |   |
|---|---|
| **What it is** | Ordered layers of resources a CCP accesses when a member defaults |
| **Primary purpose** | Isolate the defaulter's losses and prevent contagion to other members |
| **First layer** | Defaulter's initial and variation margin (collateral) |
| **Second layer** | CCP capital and clearing fund contributions |
| **Final layer** | Assessments or charges against surviving clearing members |
| **Legal basis** | CCP rules and participant agreements, often codified in regulation |
| **Key principle** | Preserve finality of non-defaulter trades; apply losses fairly across members |

</aside>

## Why a waterfall is necessary

A clearing house stands at the centre of thousands of contracts. When one member defaults, the CCP must:

1. **Identify losses.** Value all the defaulter's positions. If the market has moved against the defaulter, the CCP faces a shortfall.

2. **Manage the portfolio.** Either hedge the defaulter's positions or auction them to other members. Either way, the market move may lock in losses.

3. **Protect others.** Ensure that the default does not trigger a cascade, where other members face unexpected collateral calls and may themselves fail.

A waterfall solves this by pre-arranging which resources the CCP will use and in what order. Every member knows the hierarchy; no surprises. If the waterfall is properly designed and funded, losses are contained.

## The classical structure

Most major CCPs now follow a sequence that varies slightly by jurisdiction and asset class, but the general shape is:

### Layer 1: Defaulter's collateral

The clearing member has posted initial margin and may owe variation margin. The CCP liquidates the defaulter's positions and applies the margin to cover losses.

Initial margin is sized to cover market moves over 2–5 days (the "cover period")—the time needed to exit a large portfolio. If the default occurs on a calm day and the market cooperates, initial margin may cover all losses. The member's defaulted positions are auctioned to other members or hedged by the CCP.

Variation margin is the daily profit or loss accrual. If a defaulter owes variation margin, that is applied first.

If the defaulter has posted collateral, that collateral is also seized and liquidated.

### Layer 2: CCP's own capital

If the defaulter's collateral is insufficient, the CCP itself absorbs losses using its capital. This is the CCP's "first loss"—its insurance against volatility or rare tail events.

Most major CCPs (LCH, CME, Eurex) hold capital equal to 1–2% of notional cleared volumes. For a CCP clearing $500 trillion notional in derivatives, 1% capital might be $5 billion. This capital must cover multiple defaults or stress scenarios.

CCP capital is sacrosanct. If it is impaired, regulators and members lose confidence; the CCP's creditworthiness declines, and clearing demand may fall.

### Layer 3: Clearing fund (CCP contribution)

Many CCPs maintain a clearing fund—a pool of capital contributed by all members. The CCP itself contributes, usually at 10–50% of the total. This fund is a mutualized risk pool: it covers losses from any single member's default, and all surviving members have contributed to it.

The clearing fund amount is sized to cover the "cover scenario"—typically the default of the largest member in normal-stress conditions, or sometimes the two largest members in extreme stress.

When losses exceed CCP capital, the clearing fund is tapped. Surviving members know this may happen and have sized their contributions accordingly.

### Layer 4: Surviving members' assessments

If the waterfall is exhausted and losses remain, the CCP can assess surviving members for additional contributions. This is a "last resort" and is rare.

When assessed, members typically have days or weeks to pay. This creates a secondary risk: a large assessment can trigger liquidity stress at other members, potentially causing a second or third failure. Regulators have become wary of back-loaded assessments for this reason. Some modern rules cap or prohibit them.

### Layer 5: CCP guarantees and backstops

Some CCPs are backed by exchange owners or trading venues. If the waterfall is exhausted, the exchange may guarantee the CCP. Central banks may also provide emergency liquidity or credit lines.

The US Federal Reserve has standing facilities to lend to clearing houses in extremis. The ECB and Bank of England have similar frameworks.

## Variations in practice

The waterfall's exact structure varies:

**Position-level vs. member-level:** Some CCPs (CME, EUREX) run per-product or per-service default management—each asset class has its own fund and capital. Others (LCH) run a consolidated waterfall across all products. Consolidated is simpler and more efficient; segregated is more transparent but potentially less protective.

**Variation margin gains:** Most CCPs require the defaulter to pay variation margin daily. If that is not done, it is treated as a default event. Some CCPs grant a grace period (hours to a day) to allow operational delays.

**Auction mechanics:** How the CCP auctions the defaulter's positions affects how much is lost. A fast, orderly auction (hours) typically reduces loss; a forced, chaotic auction (minutes) may double it. The waterfall assumes a certain speed; if the auction is worse than expected, losses exceed plan.

**Haircuts on collateral:** The CCP may apply haircuts (discounts) when liquidating the defaulter's collateral, especially if that collateral is illiquid. A 10% haircut on $100 million of collateral reduces the Layer 1 amount by $10 million, pushing the loss into Layer 2.

## Stress testing and adequacy

Regulators require CCPs to stress-test their waterfalls. The test scenarios include:

- Single member default in a range of market conditions
- Multiple member defaults in extreme stress
- Market liquidity freeze (positions can only be liquidated at severe discounts)
- Collateral haircut widening
- CCP operational disruption

Modern CCPs typically pass these tests with high confidence. But no test is perfect; tail events (Black Monday, COVID crash) sometimes create losses larger than anticipated.

In 2020, COVID volatility created margin spikes that exhausted some CCPs' capital buffers (particularly in FX and commodities). No CCP defaulted, but the experience showed that waterfalls, however well-designed, have limits.

## Member liability and risk

Clearing members understand they have waterfall liability—if a peer defaults and the waterfall is exhausted, they will be assessed. This creates incentives:

- Members monitor each other more closely than a pure market structure would
- Members pressure the CCP to maintain adequate capital and funds
- Members avoid over-concentration in one CCP (diversify across multiple clearing houses)

Some academics argue that unlimited waterfall liability creates moral hazard: members know they will share losses, so they may take excessive risk. Others counter that the monitoring effect dominates.

Regulators now require CCPs to publish their waterfall scenarios and test results, so members can assess their true exposure.

## See also

<div class="wiki-seealso">

### Closely related

- Clearinghouses — the institutions that manage default waterfalls
- [Novation in Clearing](/novation-clearing/) — the legal substitution that creates the CCP's obligation
- [Settlement Finality](/settlement-finality/) — the legal protection that allows the CCP to execute its default plan
- [Back-Loading](/back-loading/) — the submission of bilateral trades to a CCP, creating waterfall exposure
- [Counterparty Risk](/counterparty-risk/) — the bilateral risk the waterfall mitigates
- [Initial Margin](/initial-margin/) — the first line of defence in the waterfall

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — US legislation requiring CCP default waterfall planning
- [Federal Reserve](/federal-reserve/) — backstop for US CCPs in systemic stress
- [Credit Risk](/credit-risk/) — the underlying risk the waterfall manages
- [Systemic Risk](/systemic-risk/) — the contagion the waterfall is designed to prevent

</div>

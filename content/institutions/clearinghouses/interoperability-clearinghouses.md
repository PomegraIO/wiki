---
title: "Clearinghouse Interoperability"
description: "Cross-CCP settlement and liquidity management, enabling trades to settle across multiple central counterparties."
keywords:
  - clearinghouse interoperability
  - cross-ccp settlement
  - central counterparty linkage
  - ccp risk management
---

*[Clearinghouse](/wiki/central-counterparty-clearing/) interoperability enables market participants to seamlessly settle transactions across multiple central counterparties (CCPs), reducing friction in post-trade settlement and improving overall market liquidity. Interoperable CCPs share settlement infrastructure, liquidity pools, and risk-management systems while maintaining operational independence.*

<aside class="wiki-infobox">

| Dimension | Detail |
|---|---|
| **Definition** | Ability to settle trades across multiple linked CCPs |
| **Key Participants** | LCH, CME, Eurex Clearing, ICE Clear Credit |
| **Settlement Method** | Bilateral netting, multi-lateral netting, or central novation |
| **Major Challenge** | [Default waterfall](/wiki/ccp-default-waterfall/) complexity when one CCP fails |
| **Liquidity Benefit** | Consolidation of cash and margin across CCPs |
| **Risk** | Contagion: one CCP default affects members of all linked CCPs |
| **Regulatory Focus** | CPMI-IOSCO standards for operational resilience and default management |

</aside>

## Why interoperability matters

Before widespread interoperability, a market participant might clear interest-rate swaps at LCH, equity derivatives at Eurex, and credit derivatives at ICE Clear. Each CCP maintained separate cash accounts, margin pools, and settlement procedures. This fragmentation forced firms to hold redundant liquidity buffers and caused inefficient use of capital.

Interoperable CCPs allow a participant to move collateral between them, net positions across venues, and reduce overall margin requirements. If a trader has a $50 million surplus at LCH and a $50 million deficit at Eurex, interoperability enables the firms to consolidate those positions, potentially halving the margin needed.

For small participants and non-bank intermediaries (hedge funds, asset managers), interoperability lowers costs by consolidating clearing services. Rather than maintaining relationships with multiple CCPs, they can clear through a single interface and access multiple venues.

## Technical interoperability: how it works

Clearinghouse interoperability operates through several mechanisms:

**Liquidity pooling:** Participants maintain pooled settlement accounts at linked CCPs, permitting real-time movement of cash and securities. A firm short at one CCP can transfer liquidity from another.

**Cross-CCP novation:** When a trade moves from one CCP to another (e.g., transferring a swap from LCH to Eurex), the trade is **novated**—the original contract is cancelled and a new one is created with the new CCP. The participants' economics don't change, but the CCP of record does.

**Multilateral netting:** Instead of settling each position to each CCP separately, participants net across all linked CCPs simultaneously. This reduces the total cash needed for settlement.

**Collateral fungibility:** Some linked CCPs recognize collateral posted at one venue as eligible at another, allowing participants to optimize their collateral portfolio.

## The big three: LCH, CME, Eurex

**LCH Clearnet** (part of LSE Group) is the dominant global CCP for interest-rate swaps and credit derivatives. Its SwapClear service clears roughly 70% of all OTC interest-rate swaps globally.

**CME Clearing** (part of CME Group) dominates futures and options across commodities, financials, and equities. Its ClearPort system enables electronic clearing of financial futures.

**Eurex Clearing** handles equities and equity derivatives across European venues. It has interoperability agreements with LCH and CME that enable participants to access all three ecosystems.

**ICE Clear Credit** is the major player in credit derivatives clearing. It links with LCH for interest-rate exposures and Eurex for equity-linked derivatives.

These four interconnected CCPs handle the majority of globally cleared derivatives. Their interoperability framework is the backbone of post-trade settlement.

## Default waterfall: complexity in a crisis

When a CCP member defaults, the [CCP default waterfall](/wiki/ccp-default-waterfall/) must determine how to allocate losses. In a single-CCP environment, this is straightforward: liquidate the defaulted member's positions, use their margin, then the CCP's guarantee fund, then apply haircuts to other members' collateral if needed.

With interoperable CCPs, the question becomes: does the default affect other members of the linked CCP? If Firm A (member of Eurex and LCH) defaults on Eurex contracts but is solvent at LCH, does LCH's waterfall trigger?

Current frameworks apply **waterfall segregation**—each CCP applies its own waterfall independently. Only Eurex members are at risk from Eurex's waterfall; LCH members are protected by LCH's. This limits contagion but creates complexity: netting across CCPs is suspended, liquidity pools are frozen, and participants must backstop margin separately at each venue.

## Stress testing and resilience

Regulators (CPMI-IOSCO) require interoperable CCPs to stress test jointly. Can LCH and Eurex survive a simultaneous default of a major participant? What happens if two large banks default simultaneously? These scenarios require collaborative modeling that involves all linked CCPs.

The operational complexity is significant. In 2017, LCH and Eurex conducted a joint default simulation involving a firm with large positions at both venues. The test exposed gaps in automated netting and margin segregation; remediation took over a year.

## Regulatory pressure and future direction

Post-2008, regulators pushed for more CCP interoperability to reduce systemic risk through diversification. The idea: if all swaps cleared at one CCP and that CCP failed, the entire market would seize. Interoperability spreads risk.

But interoperability also increases operational complexity and creates coordination problems. Recent regulatory focus has shifted toward **resilience over interoperability**—ensuring each CCP is so robust it doesn't need to be bailed out, rather than relying on links to distribute risk.

The EU's DLT Pilot Regime (2023+) explicitly allows experimental interoperability frameworks, including ones between traditional CCPs and blockchain-based settlement systems. This next frontier could enable programmable netting, atomic settlement across venues, and settlement finality in minutes rather than days.

## Blockchain and future interoperability

A potential future direction is **cross-chain bridges** that enable settlement across decentralized and traditional CCPs. Imagine a swap that clears on LCH for EUR-denominated legs and on a [Ethereum](/wiki/ethereum/)-based protocol for dollar legs, with atomic [settlement finality](/wiki/crypto-settlement-finality/) and cross-chain netting. This would require [bridge protocols](/wiki/bridge-protocols/) that are currently experimental.

<div class="wiki-seealso">

### Closely related
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — CCP role in post-trade settlement
- [CCP Default Waterfall](/wiki/ccp-default-waterfall/) — Loss allocation sequence when CCP members fail
- [Settlement T+2](/wiki/settlement-t2/) — Standard settlement timeline
- [Clearing Member Risk](/wiki/clearing-member-risk/) — Participant risk at a CCP
- [Clearing Firm](/wiki/clearing-firm/) — Firms participating in clearing

### Wider context
- [Derivatives Exchange Crypto](/wiki/derivatives-exchange-crypto/) — Decentralized clearing alternatives
- [Bridge Protocols](/wiki/bridge-protocols/) — Cross-chain settlement technology
- [Novation Central Counterparty](/wiki/novation-central-counterparty/) — Novation mechanism in clearing
- [Financial Stability Oversight Council](/wiki/financial-stability-oversight-council/) — Regulatory body monitoring systemic risk
- [Systemic Risk](/wiki/systemic-risk/) — Contagion and interconnection

</div>

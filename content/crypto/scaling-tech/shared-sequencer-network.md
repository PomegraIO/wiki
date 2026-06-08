---
title: "Shared Sequencer Network"
description: "A neutral sequencing layer that coordinates transaction ordering across multiple rollups to enable atomic cross-rollup execution and improved capital efficiency."
keywords:
  - sequencer
  - rollup
  - layer-2-scaling
  - atomic-settlement
  - cross-chain-interoperability
  - transaction-ordering
image: "/svg/crypto.svg"
---

*A **shared sequencer network** is a neutral infrastructure layer that orders transactions for multiple rollups simultaneously, enabling them to execute atomic transactions across each other without trusting a single sequencer. Rather than each rollup running its own sequencer (centralized or decentralized), multiple rollups share a common sequencing service that respects ordering guarantees and transaction atomicity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Shared Sequencer Network — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain scaling infrastructure." />

<div class="wiki-infobox-caption">Decentralized transaction ordering for multi-rollup settlement.</div>

|   |   |
|---|---|
| **What it is** | A sequencing protocol that orders and batches transactions across multiple independent rollups |
| **Why it matters** | Unlocks atomic cross-rollup transactions without introducing new trust assumptions |
| **Key benefit** | Reduces friction and capital inefficiency from multi-step bridges between rollups |
| **Trade-off** | Requires coordination among rollup operators; rollup sovereignty reduced slightly |
| **Related concepts** | Rollup, sequencer, bridge, settlement |

</aside>

## How a shared sequencer coordinates multiple rollups

In the typical rollup design, each rollup maintains its own sequencer—a single entity (or eventually a decentralized committee) that orders incoming user transactions into a canonical sequence. That sequencer then bundles the ordered transactions and submits them to the base layer for settlement. The problem: if Alice on Rollup A wants to swap assets with Bob on Rollup B, she must first bridge her tokens, wait for confirmation, then execute the swap on Rollup B—all with intermediate delays and bridge fees.

A shared sequencer network inverts this. Instead of Rollup A and Rollup B each running separate sequencers, they both consume ordered transactions from a common sequencing service. This service sees transactions from both rollups and can order them together. If Alice's bridge-out on Rollup A arrives before Bob's deposit on Rollup B, the shared sequencer respects that ordering and ensures both operations settle atomically within the same block or sequencing round.

The sequencer does not validate the rollups' state or execution—that remains the rollup's job. The sequencer only provides a neutral, tamper-proof ordering service. Think of it as a distributed clock that multiple rollups trust rather than each building their own.

## Why atomicity across rollups matters

Cross-rollup atomic execution solves a category of inefficiency that has plagued multi-layer systems. Consider a liquidity provider who wants to rebalance capital between two rollups to capitalize on a price difference. Today, they must use a bridge: withdraw from Rollup A (one transaction), wait for finality, deposit to Rollup B (another transaction), and only then execute their trade. The delay creates slippage and operational friction.

With shared sequencing, a single atomic instruction can say: "Withdraw X from Rollup A AND deposit it to Rollup B in the same logical block." If either step fails, both roll back. This dramatically improves capital efficiency because sophisticated users and [market makers](/market-maker-trading/) no longer need to lock liquidity in transit.

The other benefit: reduced MEV leakage. When Rollup A's sequencer and Rollup B's sequencer operate independently, an adversarial sequencer on Rollup A can see a pending transaction that will move price on Rollup B, and extract value by front-running it on Rollup A before the shared sequencer can order the pair atomically. A unified sequencer prevents this—it orders all cross-rollup pairs as atomic bundles, denying any single sequencer the ability to profit from asymmetric information.

## Who runs the shared sequencer—and what could go wrong

The sequencing service itself must be run decentrally to avoid becoming a bottleneck or single point of failure. Most designs propose a committee of sequencers (similar to a validator set) that collectively attest to transaction ordering. [Proof-of-Stake](/proof-of-stake/) or another economic model can penalise sequencers that lie about order, creating a cost to attacks.

However, a shared sequencer does slightly reduce rollup sovereignty. Each rollup gives up the ability to unilaterally control its own sequencing and censor or reorder transactions at will. If the shared sequencer committee is captured or colluding, all connected rollups face the same sequencer risk. Some view this as acceptable because the risk is distributed across multiple rollups and can be monitored collectively; others argue it reintroduces centralization.

A second risk is liveness: if the shared sequencer goes down, all connected rollups halt transaction ordering. Rollups can mitigate this by fallback mechanisms—if the sequencer delays beyond a threshold, each rollup can switch to a local sequencer mode and catch up later. But this adds complexity and creates a window of vulnerability.

## Comparison to other scaling solutions

Rollups already sit between the base layer and single-chain apps, accepting some sequencing risk. A shared sequencer is a layer *above* individual rollups but *below* the base layer. It trades rollup isolation for atomic cross-rollup execution.

This differs from a full settlement layer, which would validate execution and guarantee finality; a shared sequencer only orders. It also differs from a traditional bridge, which is asynchronous and non-atomic—a bridge relies on independent validators to attest a transfer after the fact, introducing a multi-hop confirmation delay.

## The role of ZK proofs in sequencer design

Some shared sequencer designs use [zero-knowledge proofs](/zk-coprocessor/) to allow each rollup to independently verify that the shared sequencer's claimed ordering is canonical and that transactions were included (or excluded) correctly. This lets rollups retain strong security guarantees even while outsourcing sequencing. Others rely purely on economic incentives and reputation.

## See also

<div class="wiki-seealso">

### Closely related

- Rollup — a scaling technique that bundles transactions off-chain and settles them on-chain
- Sequencer — the entity that orders transactions in a blockchain or rollup
- Settlement layer — the final blockchain where state changes are verified and secured
- Bridge — a protocol for transferring assets or data between separate blockchains
- Atomic settlement — the guarantee that a group of transactions either all succeed or all fail
- MEV — the value extractable by reordering or censoring transactions
- [ZK Coprocessor](/zk-coprocessor/) — off-chain ZK proofs that enable efficient verification of data and ordering claims

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — platforms where atomic settlement of trades is critical
- Ethereum scaling — the ecosystem of rollup and layer-2 solutions
- [Proof-of-Stake](/proof-of-stake/) — the consensus mechanism often used to secure sequencer committees
- [Distributed ledger](/distributed-ledger/) — the underlying technology for transaction ordering and finality
- [Blockchain fundamentals](/blockchain-fundamentals/) — the principles behind decentralized transaction ordering

</div>

---
title: "Layer 2 Scaling"
description: "Off-chain execution systems that settle transactions on a base layer to reduce fees and increase throughput."
keywords:
  - layer 2 scaling
  - ethereum scalability
  - rollups
  - off-chain transactions
  - state channels
  - throughput
image: "/svg/crypto.svg"
---

*A **layer 2** is a secondary blockchain or execution system that processes transactions off the main chain, then periodically settles a summary of those transactions back onto the base layer (layer 1). By moving computational load away from the congested base chain, layer 2 systems dramatically reduce [gas fees](/gas-fee/) and increase transaction throughput.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Layer 2 Scaling — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and blockchain topics." />

<div class="wiki-infobox-caption">Layer 2 systems inherit security from the base chain while offering speed and cost advantages.</div>

|   |   |
|---|---|
| **What it is** | A secondary execution environment that batches and settles transactions on a main blockchain |
| **Typical use** | Reducing transaction costs and latency for high-volume applications |
| **Main types** | Optimistic rollups, zero-knowledge rollups, state channels, sidechains |
| **Settlement** | Periodic "batch" submission back to layer 1 for finality and dispute resolution |
| **Security model** | Derives finality guarantees from the base chain's consensus |
| **Trade-off** | Lower cost and speed; slightly higher latency before finality |

</aside>

## The scaling trilemma and layer 2's solution

Blockchain designers face a fundamental tension: decentralization, security, and scalability are difficult to maximize simultaneously. Bitcoin and Ethereum prioritize security and decentralization but sacrifice transaction throughput; they process ~15 transactions per second. Ethereum's [gas fees](/gas-fee/) spike during congestion because block space is scarce.

Layer 2 systems sidestep this trilemma by moving computation *off* the main chain. Instead of every user transaction being validated and stored by thousands of nodes, a layer 2 network validates transactions internally, then publishes a cryptographic proof or summary back to the base chain. The base chain doesn't execute every transaction; it merely verifies that off-chain activity was done correctly.

This division of labour allows layer 2 networks to achieve thousands of transactions per second while Ethereum itself remains fast enough to serve as a secure settlement layer.

## Optimistic rollups

An **optimistic rollup** bundles hundreds of transactions into a single batch, then submits a compressed representation (a "rollup") to Ethereum alongside a claim: "These transactions are valid." The system is "optimistic" because it assumes the claim is true unless someone proves otherwise.

For a few days (the challenge period), anyone can submit a **fraud proof**—a cryptographic argument showing the batch was invalid. If a fraud proof is accepted, the batch is reverted and the dishonest operator is penalised. If no one challenges it after the period expires, the batch is finalised.

Optimistic rollups are simpler to build and compatible with existing Ethereum smart contracts. Arbitrum and Optimism are the dominant examples. Their weakness: the challenge period means users must wait ~7 days for absolute certainty that a transaction is final. For most applications, transactions are "effectively final" much sooner, but high-value settlements may need to wait.

## Zero-knowledge rollups

A **zero-knowledge (ZK) rollup** uses cryptographic proofs called zero-knowledge proofs instead of optimistic assumptions. The operator generates a proof that says, mathematically, "These transactions are valid without revealing any transaction details." Ethereum instantly verifies the proof; no challenge period is needed.

ZK rollups offer faster finality and arguably stronger security (mathematical certainty rather than game-theoretic assumption). However, they are harder to build and currently less compatible with arbitrary smart contracts. Projects like StarkNet and zkSync are leading this space.

## State channels and sidechains

**State channels** (like the Lightning Network on Bitcoin) allow two or more parties to transact repeatedly off-chain, signing each transaction between themselves. Only when they settle or dispute do they touch the main chain. State channels excel for repeated, bilateral interactions (payment channels) but scale less well to multiparty interactions.

**Sidechains** are semi-independent blockchains that periodically peg to Ethereum, typically using a bridge. Polygon is the largest sidechain ecosystem. They offer more flexibility than rollups but sacrifice some security properties: a sidechain's validators are separate from Ethereum's, so a sidechain could theoretically suffer a consensus failure independent of Ethereum.

## Trade-offs and user experience

Layer 2 networks reduce per-transaction costs by 100–1,000x in typical conditions. But there are costs:

- **Bridging**: Moving assets from Ethereum to a layer 2 requires a cross-chain bridge, which introduces some latency and operational risk.
- **Fragmentation**: Different layer 2 systems are not compatible. A user with assets on Arbitrum must bridge them to Optimism to interact with an Optimism dapp. This friction discourages switching and can lead to isolated pools of liquidity.
- **Finality latency**: Even with ZK rollups, settling large transactions back to Ethereum takes time.

For small transactions, microtransactions, and gaming, layer 2s are superior. For large financial settlements or bridging between multiple layer 2s, users may still prefer to settle directly on Ethereum or use [distributed-ledger](/distributed-ledger/) alternatives.

## The future of base layer and layer 2

Ethereum developers are working on improvements that complement layer 2s. Proto-Danksharding (EIP-4844) reduces the cost to publish data to Ethereum, making layer 2 settlement cheaper. Full Danksharding (planned) would further lower costs. The goal: layer 2s become so efficient that they become the natural home for most user activity, with Ethereum serving as a settlement and security layer.

This architectural shift—moving from "Ethereum as application layer" to "Ethereum as settlement layer"—is a deliberate choice. It acknowledges that not all transactions need full Ethereum security; many only need the guarantee that final settlement is anchored to Ethereum's consensus.

## See also

<div class="wiki-seealso">

### Closely related

- [Gas Fee](/gas-fee/) — the base-layer cost that layer 2 systems reduce
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the underlying consensus and data structures that enable layered architectures
- [Distributed Ledger](/distributed-ledger/) — the broader architecture of decentralized transaction settlement
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — venues where layer 2 liquidity is fragmented across chains

### Wider context

- [Bitcoin](/bitcoin/) — also facing scalability challenges; Lightning Network is Bitcoin's equivalent to Ethereum's layer 2s
- [Ethereum](/ethereum/) — the base chain; layer 2s extend its capacity
- [Proof of Work](/proof-of-work/) and [Proof of Stake](/proof-of-stake/) — base-layer consensus mechanisms that ensure settlement security
- [Securitization](/securitization/) — conceptually, layer 2 batching is a form of financial bundling

</div>

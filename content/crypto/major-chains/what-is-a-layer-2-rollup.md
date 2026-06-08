---
title: "What Is a Layer 2 Rollup"
description: "A layer 2 rollup bundles blockchain transactions off-chain and posts compact proofs to the base layer, scaling throughput while preserving security."
keywords:
  - what is a layer 2 rollup blockchain
  - rollup scaling
  - layer 2 solutions
  - transaction batching
  - blockchain scalability
  - ethereum scaling
---

*A **layer 2 rollup** is a scaling solution that bundles dozens or hundreds of transactions into a single batch, processes them off the main blockchain, and posts a cryptographic proof of the result back to the base layer. This design lets a blockchain handle far more transactions per second while keeping the security guarantees of the underlying chain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Layer 2 Rollup — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Rollups compress transaction data and post settlement to the main chain.</div>

|   |   |
|---|---|
| **Core function** | Bundle and compress off-chain transactions; post proof to base layer |
| **Primary benefit** | Higher throughput with lower fees |
| **Security model** | Depends on proof type: fraud-proof (optimistic) or validity-proof (ZK) |
| **Data availability** | Transaction data posted to base layer; base layer acts as judge |
| **Withdrawal mechanism** | Slower for optimistic (fraud-proof period); near-instant for ZK-rollups |
| **When introduced** | Early 2020s as Ethereum scaling gained momentum |

</aside>

## The Core Problem

A blockchain's throughput is constrained by its block size and block time. Bitcoin, for instance, creates a new block roughly every 10 minutes and caps data per block at 1 MB. This bottleneck creates a trade-off: keep blocks small for decentralization, or enlarge them at the cost of node bandwidth and storage. Rollups sidestep this by doing the hard computation *off-chain* and only asking the main chain to verify a summary.

## How Rollups Bundle Transactions

The basic flow is straightforward. Users send transactions to a **sequencer**, a service that collects transactions into a batch. The sequencer executes all the transactions in that batch, updates a new state root (a cryptographic hash representing the new account balances), and packages a proof of that state transition. This proof—just a few kilobytes—is then posted to the base layer, where a smart contract verifies it. The base layer never executes each individual transaction; it only checks that the proof is valid.

Because transaction data can be compressed (addresses, amounts, and signatures are repetitive across a batch), the rollup can encode dozens of transactions in the space a single on-chain transaction would occupy. This compression alone gives a 10–100× improvement in throughput, depending on the data type and proof size.

## Optimistic vs. Zero-Knowledge Proofs

**Optimistic rollups** assume that sequencers are honest unless proven otherwise. The sequencer posts a batch and claims it is correct. Anyone can then run the transactions themselves, and if the sequencer lied, they can submit a **fraud proof** showing where the computation went wrong. If a fraud proof is accepted, the sequencer's batch is rolled back and it loses a stake. This approach is cheap to generate—no complex cryptography—but imposes a **challenge period** (typically 7 days on Ethereum) before a withdrawal is final.

**Zero-knowledge rollups** (ZK-rollups) generate a cryptographic proof that the computation was done correctly. No one needs to re-run the batch; the proof is mathematically verifiable. This approach is more computationally expensive to generate but offers faster withdrawals (minutes or less) and no challenge period. Both approaches are secure; they simply trade computational cost and withdrawal speed differently.

## Data Availability and Security

A rollup's security hinges on data availability. Even though transactions are processed off-chain, the transaction data itself must be posted to the base layer so that anyone can reconstruct the rollup state if the sequencer disappears. If transaction data is hidden, users could be trapped: they would not be able to prove they own assets on the rollup or withdraw to the base layer.

For this reason, rollups post transaction data (in compressed form) to the base layer blockchain, where it becomes part of the permanent record. The base layer acts as both a final settlement layer and a data keeper, giving rollups their security without forcing the base chain to execute every transaction.

## Throughput and Cost Trade-offs

Posting data to the base layer does consume space and incurs a cost, known as the **data availability fee**. This is typically the largest component of a rollup user's cost, alongside the sequencer's profit margin. Despite this cost, rollup fees are 10–100× lower than base-layer fees during periods of congestion because a single rollup batch can clear hundreds of transactions' worth of data onto the main chain in one go.

The throughput scaling is real but capped: a rollup cannot exceed the base chain's data throughput. If Ethereum can accept 8 MB of data per block and a rollup posts one batch per block, the rollup's throughput is fundamentally limited by Ethereum's block space. Multiple rollups can exist simultaneously, competing for the same base-layer bandwidth. This constraint is partly why Ethereum governance has debated block sizes, data structures like blobs, and alternative base-layer approaches.

## The Sequencer Question

One lingering centralization risk is the sequencer. Early rollups used a single company-run sequencer that ordered all transactions. If that sequencer censors a user or goes offline, the rollup stalls. Newer designs include **sequencer decentralization**, where multiple parties can propose blocks in rotation or competition. However, most production rollups still rely on a single sequencer or a small group, making the solution's decentralization weaker than a fully peer-to-peer blockchain.

## Why Rollups Matter

Rollups represent a pragmatic scaling path: they preserve the security and finality of the base layer (Bitcoin or Ethereum) while letting applications move to a faster, cheaper execution environment. For payments, NFTs, and decentralized finance, the 100–1000× throughput improvement is transformative. They do not solve all problems—cross-rollup communication remains clunky, and user experience still lags traditional applications—but they have become the dominant scaling strategy for Ethereum and other Layer 1 blockchains seeking to handle mainstream transaction volume.

## See also

<div class="wiki-seealso">

### Closely related

- [Optimistic Rollup vs ZK-Rollup](/optimistic-rollup-vs-zk-rollup/) — Compares fraud-proof and validity-proof models in depth
- [Blockchain Fundamentals](/blockchain-fundamentals/) — The distributed-ledger foundation enabling rollups
- [Ethereum](/ethereum/) — The primary base layer for rollup scaling
- [Bitcoin Block Size Limit Explained](/bitcoin-block-size-limit-explained/) — Why base-chain throughput constraints matter

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where rollup-native assets are traded
- [Distributed Ledger](/distributed-ledger/) — The broader ledger-technology context
- [Hash Rate](/hash-rate/) — Consensus security that rollups rely upon

</div>

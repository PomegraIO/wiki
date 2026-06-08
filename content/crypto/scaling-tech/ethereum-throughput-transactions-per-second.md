---
title: "Ethereum Throughput: Transactions Per Second Explained"
description: "Why Ethereum processes 15–30 transactions per second on its base layer, what causes this bottleneck, and how Layer 2 solutions scale throughput."
keywords:
  - ethereum transactions per second limit
  - ethereum throughput TPS
  - ethereum scaling solution
  - layer 2 scaling ethereum
  - blockchain transaction capacity
image: /svg/crypto.svg
---

*Ethereum processes roughly 15–30 transactions per second on its base layer — far slower than Visa's 24,000 TPS. This ceiling exists because of hard trade-offs between **decentralization**, **security**, and **throughput**. Every validator must independently verify every transaction, and block times and sizes are deliberately kept modest. Layer 2 solutions multiply effective throughput by batching thousands of transactions into a single base-layer proof.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ethereum Throughput — The Numbers and Trade-Offs</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Blockchain throughput is capped by the cost of full verification across a global network.</div>

|   |   |
|---|---|
| **Base Layer TPS** | ~15–30 tx/sec (varies by network load, uncle blocks, MEV) |
| **Block Time** | ~12 seconds; varies with difficulty |
| **Block Size** | ~64–128 KB typical; dynamic with blob space (post-Dencun) |
| **Bottleneck** | Every node must validate every tx; CPU + storage + network bandwidth limited |
| **Layer 2 TPS** | 100s to 1000s (Arbitrum: ~40k, Optimism: ~4k, Starknet: ~1000) |
| **L2 Trade-Off** | Higher throughput; reduced decentralization (fewer full nodes); increased latency to finality |

</aside>

## Why 15–30 TPS: The Fundamental Constraint

**Ethereum transactions per second** are limited by the need for **full decentralization**. Unlike a credit-card network run by Visa (a centralized company with high-throughput servers), Ethereum is maintained by thousands of independent validators worldwide, each running a full node.

Every one of those validators must:
1. Receive the transaction from the peer-to-peer network (network bandwidth constraint)
2. Validate the transaction's signature and nonce (CPU constraint)
3. Execute the transaction against the state (CPU constraint, storage reads)
4. Store the resulting state changes (storage constraint)

If Ethereum increased its block size from ~128 KB to 1 MB, or reduced block time from 12 seconds to 1 second, validators in remote regions with modest internet would be unable to keep up. They would fall out of sync, and the network would lose decentralization. A smaller group of well-connected validators would dominate, and security would suffer.

This is the **blockchain trilemma**: you can easily maximize any two of scalability, decentralization, and security, but optimizing all three is hard. Ethereum's design explicitly prioritizes **decentralization** (thousands of independent validators) and **security** (proof of stake, finality, censorship resistance), and accepts **throughput** as the trade-off.

## Block Time and Block Size

Block time on Ethereum is roughly 12 seconds. This is a protocol constant (though actual times vary slightly due to proof-of-stake randomness). In each 12-second slot, validators propose a block containing as many transactions as fit within the block size limit.

The block size has two components:

- **Calldata and state changes** fit into an ~128 KB envelope, determined by gas limits and computational cost.
- **Blob storage** (post-Dencun upgrade, March 2024) allows rollups to post compressed data in temporary "blobs" up to 128 KB each, per block.

Blobs are cheaper than calldata because they are not stored permanently on-chain; after ~18 days they are pruned. This makes Layer 2 postings cheaper but doesn't increase base-layer transaction throughput.

In a 12-second block, you might fit 100–300 simple transactions (e.g., token transfers) or fewer if transactions are complex (smart contract interactions, swaps). Across 7,200 blocks per day, that yields ~10–21 million transactions daily, or ~115–240 TPS — but this is an upper bound when blocks are full and network load is high. In practice, average TPS is ~15–30 because blocks are rarely completely full outside periods of congestion.

## Network and Storage Bottlenecks

Each transaction's data must propagate across the peer-to-peer network to every validator. The larger the block, the longer propagation takes. If blocks propagated too slowly, validators would start building competing chains, and the network would fragment.

Similarly, validators must store the blockchain's historical state. A full Ethereum node requires ~700 GB of disk space (as of 2024). If blocks were 10 MB instead of 128 KB, storage requirements would grow proportionally, and fewer people could run nodes. The network would become more centralized — bad for security.

This is why Ethereum (and most blockchains) deliberately constrain block size. The "cost" of a transaction includes not just CPU to execute it, but the network bandwidth and storage burden it imposes on 15,000+ validators globally.

## Why Not Just Raise the Limit?

Ethereum developers have repeatedly debated raising block sizes. Larger blocks would increase base-layer throughput. But the trade-off is clear:

- **Bandwidth**: Validators with 10 Mbps internet (common in developing regions) would struggle to download 10 MB blocks in a 12-second slot.
- **Storage**: Running a node would require terabytes of space, accessible only to datacenters. Solo validators would disappear.
- **Latency**: Uncle blocks and reorgs would increase, reducing finality.
- **Centralization**: Fewer entities would run full nodes; fewer would validate. This increases censorship risk and attack surface.

Ethereum's philosophy is that a slower but more decentralized chain is preferable to a faster but more centralized one. This reflects the core value proposition: **censorship resistance and credible neutrality over speed**.

## Layer 2 Solutions: Scaling Without Sacrificing Decentralization

Layer 2 blockchains (rollups) solve this by moving transactions *off* the base layer. Instead of every Ethereum validator executing every transaction, a Layer 2 system:

1. Accepts transactions from users (often 1000s per second).
2. Batches them together.
3. Compresses the data (removing redundancy, using succinct formats).
4. Posts a single batch proof or claim to Ethereum every 5–60 minutes.

An **Optimistic Rollup** (Arbitrum, Optimism) assumes the batch is valid unless someone disputes it. Validators and users can re-execute the batch to catch fraud.

A **ZK Rollup** (Starknet, Polygon zkEVM) posts a cryptographic proof that the transactions are valid, without requiring re-execution.

The result: Layer 2 networks can process 100s to 1000s of TPS while posting only 1 byte of data per transaction to Ethereum (versus 16 bytes per byte of calldata on-chain).

## The Finality and Risk Trade-Off

The catch: Layer 2 transactions are faster and cheaper, but they aren't "final" on the base layer immediately. An Optimistic Rollup user must wait 7 days for a withdrawal to settle (the challenge period). A ZK Rollup is final once the proof is posted, but the proof generation takes time (minutes to hours depending on design).

For trading and low-value swaps, this latency is acceptable. For settlement of large sums or cross-chain bridges, the delay matters. Most users accept the trade-off: **fast and cheap** on Layer 2, with **final and censorship-proof** settlement on Layer 1.

## Ethereum's Post-Merge Outlook

Since the Merge (September 2022), Ethereum has shifted to proof-of-stake, improving energy efficiency but not directly raising throughput. Future upgrades (Dencun with blobs, and later Proto-Danksharding) compress Layer 2 data further, making rollups even cheaper.

Base-layer throughput will remain ~15–30 TPS as long as Ethereum prioritizes decentralization. But with mature Layer 2 ecosystems, the *effective* throughput accessible to users — across all rollups — could reach thousands or tens of thousands of TPS, at a fraction of the security cost of raising base-layer limits.

This layered model is the current Ethereum roadmap: a modest, conservative base layer + high-throughput Layer 2 solutions. It reflects a deliberate choice: **Ethereum is the settlement layer, not the transaction layer**.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — The underlying consensus and verification model
- [Proof-of-Work](/proof-of-work/) — The prior consensus mechanism (Ethereum 1.0)
- [Proof-of-Stake](/proof-of-stake/) — The current Ethereum consensus mechanism
- [Smart Contract](/smart-contract/) — What transactions execute on Ethereum
- [Distributed Ledger](/distributed-ledger/) — The general framework for decentralized networks

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where high throughput is visibly demanded
- Scalability Trilemma — The conceptual framework limiting all blockchains
- Consensus Mechanism — Trade-offs inherent in decentralized validation
- Finality — Why fast settlement and proven finality are different

</div>

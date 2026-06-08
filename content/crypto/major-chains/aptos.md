---
title: "Aptos"
description: "A Move-based Layer 1 using Block-STM to execute transactions in parallel within a single shard, maximising throughput without sharding complexity."
keywords:
  - aptos blockchain
  - move language
  - block-stm
  - parallel execution
  - layer 1
image: "/svg/crypto.svg"
---

*Where [Sui](/sui/) organises parallelism around discrete objects, **Aptos** takes a different path: it executes all transactions in a block speculatively and in parallel, resolving conflicts only at commit time. This approach, called Block-STM, treats the blockchain as a shared-memory multiprocessor, squeezing maximum throughput from a single validator set without breaking apart into shards.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Aptos — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain technology." />

<div class="wiki-infobox-caption">Aptos Labs' Move-based chain optimises throughput via parallel execution within a single shard.</div>

|   |   |
|---|---|
| **Blockchain type** | Layer 1 consensus chain |
| **Consensus mechanism** | Delegated Proof of Stake (DPoS) |
| **Language** | Move bytecode |
| **Native asset** | APT token |
| **Launch** | Mainnet October 2022 |
| **Execution model** | Block-STM (software transactional memory) |
| **Parallelism scope** | Per-block; no sharding |
| **Finality** | Probabilistic; ~2–3 second confirmation |

</aside>

## The Block-STM approach

Transaction parallelism in traditional blockchains is hard because you don't know in advance which accounts a transaction will touch. Ethereum's solution: process them sequentially and accept the throughput ceiling. Sui's solution: design contracts to touch only independent objects, which parallelise naturally.

Aptos chose a third path: *software transactional memory*. During block production, Aptos executes every transaction in a block speculatively and in parallel. Each execution optimistically assumes it won't conflict with others. The runtime tracks which accounts and storage locations each transaction reads and writes. If two transactions conflict—both write to the same account, say—the slower one aborts and re-executes, reading the updated state from the first transaction's commit.

This is familiar to computer scientists from multicore programming. You gain parallelism for free when data accesses don't overlap. Conflicts cause retries, but if those are rare (and they usually are in practice), you get near-linear speedup.

Block-STM is elegant because it imposes nothing on developers. You write a Move contract as if it were sequential. The Aptos runtime figures out the parallelism. No need to restructure your protocol around objects or avoid shared state—it just works, and shared state is cheap.

## Why a single shard?

Aptos doesn't shard its state across validators. Every validator maintains the full account state. This means every validator can execute every transaction. That might sound inefficient, but it has major benefits.

First, finality is simple. Once a supermajority of validators have executed and committed a block, it's final. There's no coordination across shards, no cross-shard synchronisation primitives, no risk of one shard lagging behind another. You get instant atomicity for any transaction in the block.

Second, DApp complexity drops. A smart contract can modify any account, execute any transaction, read any historical state. There's no "shard 3 can't touch shard 7" constraint. This is hugely valuable for protocols that evolved on Ethereum—lending platforms, DEXs with complex state dependencies, DAOs—which can port to Aptos with minimal redesign.

Third, it enables instant finality for some transactions (those that don't conflict) and fast finality for the rest. The latency is measured in seconds, not epochs.

The tradeoff: you can't grow throughput by adding validators in a naive sense. If every validator processes every transaction, adding more validators doesn't increase throughput—it just adds redundancy. Aptos' scaling story isn't "add shards"; it's "optimise the Block-STM algorithm and increase validator CPU".

This is a bet that hardware will keep getting faster, and that software parallelism within a single shard will outpace the complexity of coordinating across multiple shards. Time will tell if that bet holds.

## Move bytecode and developer experience

Like Sui, Aptos uses Move as its smart-contract language. But Aptos' relationship with Move is slightly different: it evolved the language further, adding more built-in types and standard library functions for things like coins and collections.

Move's safety properties—no reentrancy, no phantom state, explicit ability constraints—are inherited. But on Aptos, you don't redesign your contract to avoid shared mutable state. You just write it, and the Block-STM runtime handles the parallelism.

This has made Aptos more accessible to Solidity developers. The mental model is simpler: treat Aptos like a traditional blockchain, write contracts as if they're sequential, and trust the runtime to parallelise. This contrasts with Sui, where embracing the object model is often necessary for good performance.

## Throughput in practice

Aptos' theoretical throughput advantage is substantial. Block-STM can scale transaction throughput roughly linearly with CPU cores (absent conflicts). Early benchmarks showed 160,000+ transactions per second in controlled settings. Real-world throughput has been lower, constrained by network bandwidth, consensus latency, and real conflict rates.

But it's still impressive. On-chain activity (swaps, NFT mints, interactions) sees sub-second confirmation times. For dApps where latency matters—games, high-frequency trading, interactive protocols—this is a real improvement over Ethereum's 12-second blocks or Bitcoin's 10-minute epochs.

The catch: throughput gains only accrue if the runtime executes speculatively. If most transactions conflict, retry rates soar and parallelism collapses. Aptos' design mitigates this: the runtime can order transactions heuristically to reduce conflicts. But pathological cases exist—a popular DEX where every trade reads and writes the same liquidity pool will serialise despite Block-STM's sophistication.

## Network effects and ecosystem

Aptos has attracted significant capital and developer attention. The Aptos Foundation (Aptos Labs' ecosystem arm) has been an aggressive funder, sponsoring hundreds of projects. The community is dense, particularly in gaming and NFTs.

But market share has remained modest. Aptos trails Ethereum by vast margins in TVL (total value locked), developer count, and user base. The Layer 1 narrative has saturated; chains that aren't Bitcoin, Ethereum, or Solana struggle for mindshare.

Where Aptos has found traction: specific verticals where latency matters. Some gaming studios prefer Aptos for its speed. Some trading desks have built on it. These are niche use cases, but they're real.

The Move language, shared with Sui, hasn't become the industry standard some hoped. Solidity remains dominant; developers see the friction of learning a new language as a barrier. Aptos would need order-of-magnitude adoption to reverse this trend.

## Comparison with Sui

Both chains share Move. Both prioritise parallelism. The differences:

- **Sui** organises parallelism around objects, making simple transactions instant but complex shared state slow.
- **Aptos** makes all transactions fast via Block-STM, at the cost of no sharding and thus a throughput ceiling tied to validator hardware.

For a user sending a coin, Sui is faster. For a contract that modifies multiple accounts atomically, Aptos is simpler. Sui scales horizontally (more shards, more throughput). Aptos scales vertically (faster hardware, more throughput).

Neither has won decisively. Aptos' ecosystem is larger; Sui's technology is (arguably) more elegant. Both remain experiments in post-Ethereum blockchain design.

## See also

<div class="wiki-seealso">

### Closely related

- [Sui](/sui/) — parallel execution via object-centric design
- Move language — the smart-contract language both chains use
- Block-STM — the parallel execution algorithm Aptos relies on
- [TON Blockchain](/ton-blockchain/) — multi-chain architecture for massive scale
- [Delegated Proof of Stake](/proof-of-stake/) — Aptos' consensus mechanism

### Wider context

- Layer 1 — blockchain classification; what Aptos is
- Smart contracts — programmable transactions on Aptos
- [Distributed ledger](/distributed-ledger/) — the underlying technology
- Finality — how certainty is achieved in consensus
- Scalability trilemma — the fundamental constraints Aptos addresses

</div>
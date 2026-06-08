---
title: "NEAR Protocol"
description: "A blockchain platform using Nightshade sharding to split state and transaction processing across multiple shards while maintaining unified security."
keywords:
  - near protocol
  - nightshade sharding
  - blockchain scalability
  - layer-1 blockchain
  - proof of stake
image: "/svg/crypto.svg"
---

*[NEAR Protocol](https://near.org) is a layer-1 blockchain that scales through Nightshade, a sharding architecture that partitions both state and transaction processing across multiple chains—called shards—while preserving a single unified [validator](https://near.org/docs) set. Rather than forcing every node to process every transaction, NEAR lets different validators handle different parts of the network's state, multiplying throughput without splitting security.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NEAR Protocol — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A sharded layer-1 blockchain where consensus spans fragments of state.</div>

|   |   |
|---|---|
| **What it is** | A [proof-of-stake](/proof-of-stake/) blockchain using Nightshade sharding |
| **Consensus mechanism** | Doomslug (finality-yielding Byzantine consensus) |
| **Shard count** | Variable; designed to scale to hundreds |
| **Finality** | ~2 seconds post-commitment |
| **Block time** | ~1.3 seconds per shard |
| **Native asset** | NEAR token (staking, gas, governance) |
| **Max throughput** | Scales with shard count; currently handles ~100s TPS |

</aside>

## Why existing blockchains hit a scaling wall

[Bitcoin](/bitcoin/) and [Ethereum](/ethereum/) impose a hard rule: every full node validates every transaction. That guarantee—that you can run a node on a laptop and hold the network to account—is admirable. But it creates a bottleneck. Bitcoin processes ~7 transactions per second. Ethereum, with faster blocks, manages higher throughput but still chain all transactions into a single sequence that every validator must execute in order. Once you've done that, you cannot scale horizontally. A network processing 15 million transactions daily hits a ceiling: nodes either drop out (losing decentralization) or transactions queue indefinitely (losing usability).

Layer-2 solutions like Polygon and Optimism bundle transactions off-chain, then post cryptographic proofs to the base chain. That works, but it trades finality and composability for speed. NEAR chose a different path: split the chain itself.

## How Nightshade partitions state and work

Nightshade is a sharding design where the network divides into multiple parallel shards, each maintaining its own shard state and processing its own shard transactions. The innovation is that a *single validator set* secures all shards—there's no separate validator committee per shard.

Here's the mechanics. NEAR's network is divided into, say, ten shards. When you submit a transaction, it targets a specific shard (determined by the account or contract address involved). That shard's chunk producers—a rotating subset of validators—bundle transactions for their shard into a chunk. All chunks are then included in a single block proposal. A blockchain-wide consensus round (using Doomslug, NEAR's finality mechanism) votes on the entire block, validating all chunks at once.

The result is that a 10-shard network can theoretically process 10× the transactions per second compared to a non-sharded chain at the same block time and validator count. NEAR's current configuration achieves roughly 100–150 transactions per second and is designed to scale to thousands as shard count increases.

## Why a unified validator set matters

Other chains have attempted sharding—Ethereum 2.0's early designs included shards, for instance—but often run into a problem: if each shard has its own validator committee, a validator is responsible for only a fraction of the network's security. That makes it cheaper to corrupt a shard (you only need to bribe one committee) than to corrupt the whole chain.

NEAR sidesteps this by requiring *all* validators to attest to *all* shards in a single consensus round. A validator cannot validate shard 1 without also validating shard 3; they vote on the whole block. This keeps the [cryptographic security](/proof-of-work/) of a sharded network as strong as a non-sharded one, even as throughput scales.

## Finality and cross-shard communication

Doomslug, NEAR's consensus algorithm, finalizes blocks (and therefore all chunks within them) in roughly 2 seconds. That's fast enough for most real-time applications—far faster than waiting for Bitcoin's ~10-minute blocks.

Cross-shard transactions are more complex. If a smart contract on shard A needs to call a contract on shard B, NEAR uses a receipt system: the transaction on A generates a receipt that is executed asynchronously on B in a later block. This ensures correctness but introduces a delay—atomic composability across shards is not free. Application developers must design carefully if they rely on tightly coupled logic across shards, though most applications fit neatly within a single shard.

## Developer experience and ecosystem

NEAR's developer story aims for simplicity. Smart contracts are written in Rust or AssemblyScript (TypeScript-like). Account model is closer to traditional systems (each account has its own state) rather than Ethereum's storage tree. The fee model is predictable: storage costs are reclaimed when you delete state, and gas prices are metered in small units, avoiding the sharp spikes seen on Ethereum during congestion.

The NEAR ecosystem includes wallets (like NEAR Wallet), an exploratory testnet for experimentation, and a community of DeFi, gaming, and social projects. Because sharding allows inexpensive computation, applications that would be unaffordable on Ethereum (small micropayments, frequent state updates) become viable.

## Trade-offs and limitations

Nightshade's elegance comes with practical constraints. Developers writing contracts must understand shard assignment and receipt semantics if their app spans shards. The unified validator set, while secure, means running a full NEAR node requires significant computational resources—there is no "light client" equivalent to Ethereum 2.0's light clients, though work is underway.

Finality at 2 seconds is fast but not instant. For applications requiring true atomicity across shards (certain DEX architectures, for example), the receipt-based execution model can be awkward. And relative to [Solana](/solana/), which uses a different scaling approach, NEAR trades per-shard throughput for architectural simplicity and lower hardware requirements.

## The broader sharding narrative

NEAR's Nightshade is not the only sharding design in production. [Ethereum](/ethereum/) is implementing stateless shards in later roadmap phases. [Polkadot](/polkadot/) uses a parachain model where independent chains (parachains) connect to a relay chain—similar intent (parallel processing), different architecture. Each trades different properties: NEAR for unified security and predictable composability; Ethereum for eventual maximal decentralization; Polkadot for sovereign chain flexibility.

NEAR's bet is that unified validators plus a single consensus round give you scale without the fragmentation headaches that plague other approaches.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of stake](/proof-of-stake/) — consensus mechanism securing NEAR's network
- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger concepts NEAR builds on
- [Ethereum](/ethereum/) — alternative layer-1 with different scaling choices
- [Tezos](/tezos/) — another layer-1 with distinct governance and architecture
- [Algorand](/algorand/) — pure proof-of-stake network with different finality model
- [Hedera Hashgraph](/hedera-hashgraph/) — enterprise blockchain using DAG consensus instead of chains

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where NEAR tokens trade
- [Distributed ledger](/distributed-ledger/) — foundational concept for sharded systems
- Layer-2 — off-chain scaling as alternative to sharding

</div>

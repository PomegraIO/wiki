---
title: "Hedera Hashgraph vs Blockchain"
description: "Hedera Hashgraph uses a DAG-based data structure instead of a chain of blocks, trading simpler consensus and faster finality for different decentralization and security properties."
keywords:
  - hedera hashgraph vs blockchain
  - hashgraph
  - dag distributed ledger
  - directed acyclic graph
  - hedera consensus
---

*While most cryptocurrencies arrange transactions in a linear chain of blocks, Hedera Hashgraph uses a **directed acyclic graph** (DAG) structure where each node can reference multiple parents, not just one. This architectural difference—sometimes called a "hashgraph"—eliminates the need for traditional mining, enables faster finality, and simplifies consensus. However, it trades away some of blockchain's redundancy and introduces different trust assumptions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hedera Hashgraph vs Blockchain — Key Differences</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Two data structures lead to different consensus models and throughput profiles.</div>

|   |   |   |
|---|---|---|
| **Aspect** | **Blockchain (e.g., Bitcoin)** | **Hashgraph (Hedera)** |
| **Data structure** | Linear chain of blocks | DAG (multiple references per node) |
| **Consensus mechanism** | Proof of work or stake | Gossip about gossip + virtual voting |
| **Finality time** | ~10 min to hours | Seconds |
| **Throughput** | Limited by block size/time | ~10,000 transactions per second |
| **Decentralization model** | Open (anyone can mine) | Permissioned (governed council) |
| **Transaction ordering** | Total order imposed by blocks | Deterministic order via timestamps |
| **Forks possible** | Yes (temporary reorganizations) | No (single definitive history) |

</aside>

## Blocks vs. DAGs

A traditional blockchain works by consensus on a single chain. Miners or validators compete to create the next block, which references the previous block by its hash. This linear structure is simple and robust: any node can independently verify the chain by checking each block's reference to its parent.

A hashgraph, by contrast, is a **directed acyclic graph** where each node can reference multiple previous nodes (events), not just one parent. Think of it as a tree with multiple branches merging rather than a single-threaded rope. Each transaction or batch of transactions (an "event") includes pointers to two or more previous events, creating a mesh of references.

This design choice eliminates the "mining race": there is no competition to find the next block first. Instead, nodes gossip about events they have heard, and the DAG grows organically as events reference prior events. All nodes can build the same DAG because they all receive and process events in the same causal order.

## Gossip About Gossip (Virtual Voting)

Hedera's consensus mechanism, often called "gossip about gossip," is elegant. Nodes communicate about which events they have seen and from which source. If node A saw event X and tells node B, then B knows A saw X. When B tells node C about A's knowledge, C can infer that A, B, and X have certain causal relationships.

From these gossip chains, validators can compute a **virtual voting** result: which events have been seen by which supermajority of validators. This computation is deterministic, requiring no additional messages. If two-thirds or more of validators have seen an event (directly or transitively), the event is effectively finalized.

This avoids the traditional Byzantine consensus round-trips (where validators send messages, aggregate votes, and reach agreement). Instead, the network reaches consensus implicitly, just by sharing information about who has seen what.

## Finality and Transaction Ordering

In Bitcoin, finality is probabilistic: after 6 blocks, a transaction is considered final (reversing it would cost more energy than the block subsidy is worth, so it is economically irrational). A user waits ~10 minutes for one block confirmation, then 60 minutes for six, to feel safe.

In Hedera, finality is reached in seconds, deterministically. Once an event enters the DAG and two-thirds of validators have had the opportunity to reference it, the event is final and cannot be reordered.

Transaction ordering is also different. In a blockchain, the order of transactions is set by the block they enter: all transactions in block N are ordered before block N+1. In a hashgraph, ordering is computed post-hoc from timestamps and causal relationships embedded in the DAG. Hedera uses a "consensus timestamp" assigned to each transaction, which is determined by the majority of validators' clocks and the DAG structure, ensuring all nodes agree on the same ordering.

## Throughput and Scalability

Hedera claims ~10,000 transactions per second at consensus-layer throughput, compared to Bitcoin's ~7 tx/sec or Ethereum's ~12 tx/sec on its main chain. How? The DAG structure allows every node to participate in consensus simultaneously, rather than waiting for the next block creator. There is no "block slot" bottleneck; events flow and are finalized continuously.

However, this throughput comes with caveats. Hedera operates as a **permissioned network**: only approved validators (council members) can participate in consensus. This is faster and more efficient than proof-of-work, which must puzzle-solve to prove work, or large proof-of-stake networks with many anonymous participants. But it shifts trust to the council members, who must be vetted and trusted not to collude.

## Decentralization Trade-off

Bitcoin's blockchain is permissionless: anyone can download the code, run a node, and earn the right to propose blocks by solving a cryptographic puzzle. This openness comes at a cost: consensus is slow (6 confirmations, 60 minutes) and throughput is low.

Hedera's permissioned council can operate a faster, simpler consensus protocol. But only council members vote on transaction validity; ordinary users cannot participate. Hedera's council is governed by the Hedera Governing Council, a consortium of enterprises and organizations. This is more like a consortium blockchain (e.g., R3 Corda, Hyperledger Fabric) than a fully permissionless public blockchain.

For enterprise use cases—supply chain tracking, inter-bank settlement, corporate governance—a permissioned setup is acceptable and even preferable, because participants are known and can be held accountable. For an aspirational open network (like Bitcoin), the permissioning is a step backward.

## Data Availability and Verification

A blockchain's strength is redundancy: every node stores every block and can independently verify the entire history. This makes it expensive to censor or alter the past; you would need to recompute and re-broadcast millions of blocks.

A hashgraph is lighter on data: nodes only need the events and their causal relationships, not necessarily every byte of every transaction's signature. However, a DAG-based system must be more careful about data availability. If validators gossip about events but do not share the full event data, nodes cannot independently verify the computation. Hedera addresses this by requiring full transaction data to be available; nodes sync with each other to reconstruct the full state.

The net effect is that a hashgraph can be faster and lighter than a blockchain for consensus, but the security and independence of verification depend on the implementation. Hedera's architecture works well for a permissioned network with honest-majority assumptions; it is less suited to a fully adversarial, permissionless setting.

## Why Blockchains Persist

Despite the elegance of DAG-based systems, blockchains remain dominant. The reasons are partly social (Bitcoin's first-mover advantage, the rallying of the crypto community around a permissionless ideal) and partly practical. A linear blockchain is conceptually simpler; any developer can audit a block and verify it is correct. DAG systems are newer and more complex, making implementation errors more likely.

Additionally, blockchains have proven themselves in adversarial environments, where validators are unknown and potentially adversarial. The redundancy and simplicity of Bitcoin is a feature: it is hard to attack or corrupt because there is little innovation to break.

Hedera works for applications that trust the governing council and value speed. Bitcoin and Ethereum work for applications that require permissionlessness and will tolerate slower settlement.

## Current Adoption

Hedera is used for enterprise applications like supply chain management, real estate title recording, and identity verification. It is less prominent in the broader "cryptocurrency" sphere, where Bitcoin and Ethereum (and their layer 2 systems) dominate. The permissioning and council governance make Hedera less appealing to decentralization maximalists and cryptocurrencies focused on censorship resistance.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — The core principles underlying both blockchains and DAGs
- [What Is a Layer 2 Rollup](/what-is-a-layer-2-rollup/) — An alternative approach to scaling consensus throughput
- [Distributed Ledger](/distributed-ledger/) — Broader context for ledger structures

### Wider context

- [Proof of Work](/proof-of-work/) — Bitcoin's consensus mechanism and its role in permissionlessness
- [Proof of Stake](/proof-of-stake/) — Modern delegated consensus
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where Hedera and blockchains trade

</div>

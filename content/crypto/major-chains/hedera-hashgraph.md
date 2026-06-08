---
title: "Hedera Hashgraph"
description: "An enterprise blockchain using directed acyclic graph consensus to achieve asynchronous Byzantine fault tolerance without traditional mining or validator elections."
keywords:
  - hedera hashgraph
  - dag consensus
  - byzantine fault tolerance
  - distributed ledger
  - enterprise blockchain
image: "/svg/crypto.svg"
---

*[Hedera](/hedera-hashgraph/) is a public [distributed ledger](/distributed-ledger/) that replaces the traditional blockchain data structure (a chain of blocks) with a **directed acyclic graph (DAG)**, where each transaction references one or more prior transactions, creating a web of dependencies. Using the Hashgraph consensus algorithm, it achieves Byzantine fault tolerance at high throughput while removing the intermediary of a central validator set: consensus emerges from the graph structure itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hedera Hashgraph — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An enterprise ledger using DAG consensus and council governance.</div>

|   |   |
|---|---|
| **What it is** | A public ledger using directed acyclic graph and Hashgraph consensus |
| **Data structure** | DAG (not a chain of blocks) |
| **Consensus mechanism** | Hashgraph with virtual voting |
| **Block time** | Continuous (no discrete blocks) |
| **Finality** | ~5–10 seconds (probabilistic, formal) |
| **Throughput** | 10,000+ TPS capability |
| **Governance** | Council of public institutions |
| **Native asset** | HBAR (staking, gas, governance fees) |

</aside>

## Why chains are not inevitable

Since [Bitcoin](/bitcoin/), "blockchain" has meant a linear chain of blocks, each referencing the previous one. This design is intuitive—blocks line up like links in a chain—but it is not the only way to structure a distributed ledger. [Hedera](/hedera-hashgraph/) chose a different topology: instead of a chain, transactions are organized into a directed acyclic graph (DAG).

In a DAG, each new transaction typically references (cryptographically commits to) one or more prior transactions rather than just one. Over time, transactions build up a web of dependencies. No two transactions directly contradict each other; instead, the graph records an ordering derived from the structure of references. The big innovation is that you can reach consensus on the correct ordering—which transactions came first—without running a global vote or mining race.

## How Hashgraph consensus works

The Hashgraph consensus algorithm is the engine that makes DAG-based consensus practical. Here's the intuition. When a new transaction arrives, its creator stamps it with a timestamp and references two prior transactions (one from themselves, one from a randomly selected peer). These references encode information about causality: if transaction A references transaction B, then A came after B.

Nodes gossip these transactions throughout the network using a protocol called **gossip-about-gossip**. When node X receives a transaction from node Y, it doesn't just record the transaction—it also records the fact that Y now knows about it. This "gossip about gossip" creates layers of knowledge: X knows the transaction, X knows Y knows it, X knows Y knows that Z knows it.

From this layered gossip graph, the network can compute which transactions happened in what order, even though no central coordinator assigned timestamps. The algorithm uses a concept called the **virtual voting** protocol: instead of explicit votes, nodes infer from the DAG structure whether a supermajority of the network has "seen" a transaction. Once a transaction is seen by enough nodes (determined formally), it is considered decided and can never be undone.

The result is that [Hedera](/hedera-hashgraph/) achieves Byzantine fault tolerance (safety against up to one-third corruption) and liveness (progress even under network delay) without traditional mining or validator rotation.

## Advantages of the DAG model

Because [Hedera](/hedera-hashgraph/) doesn't package transactions into discrete blocks, it sidesteps a bottleneck inherent in blockchains. [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/) must wait until a block's worth of time has passed (or a block's worth of transactions have accumulated), finalize the block, and move to the next. [Hedera](/hedera-hashgraph/) finalizes transactions continuously as they arrive.

This allows extremely high throughput—[Hedera](/hedera-hashgraph/) claims 10,000+ transactions per second on the base layer, with sub-second finality. It also means the network doesn't require artificial block times or miner/validator elections to sequence transactions. Transactions order themselves through gossip and the DAG structure.

Another advantage is resistance to certain attacks. In [Proof-of-Work](/proof-of-work/) chains, a 51%-hash-power attacker can rewrite history. In traditional [proof-of-stake](/proof-of-stake/) systems, a 51%-stake attacker can prevent consensus. [Hedera](/hedera-hashgraph/), like other Byzantine protocols, is safe against up to one-third corruption—whether that corruption is wealth-based (stake) or power-based (hash). You'd need one-third of all nodes (not wealth or hardware) to act maliciously.

## Governance via a public council

[Hedera](/hedera-hashgraph/) is unusual in that it is not wholly decentralized in the classical sense. The network is governed by a council of public institutions: companies like Google, IBM, Boeing, and DLA Piper, plus academic institutions and nonprofits. The council determines protocol parameters, hash of the canonical transaction order (in case of disputes), and strategic direction.

This is a trade-off. On one hand, you get expert governance and institutional accountability: it's harder for a council member to act against the network without reputational damage. On the other hand, you've concentrated power. [Hedera](/hedera-hashgraph/) is permissionless to use (anyone can transact and run a node), but not permissionless to govern. This makes it an "enterprise blockchain" more than a purely decentralized system.

The council model appeals to enterprises and regulated institutions, which is [Hedera](/hedera-hashgraph/)'s positioning. It is less attractive to ideological decentralization advocates who see Hedera's governance as a failure of the "no trusted third party" principle.

## Smart contracts and the application layer

[Hedera](/hedera-hashgraph/) supports smart contracts via the Hedera Virtual Machine (HVM), which runs a variant of the Ethereum Virtual Machine (EVM). This means contracts written in Solidity (the most common smart contract language) can be deployed on [Hedera](/hedera-hashgraph/) with minimal modification.

[Hedera](/hedera-hashgraph/) also offers a native token service (HTS), allowing users to mint and manage custom tokens without writing smart contracts. This is simpler than [Algorand](/algorand/)'s ASA but less flexible.

Gas fees on [Hedera](/hedera-hashgraph/) are fixed in HBAR (the network's native token) rather than floating based on network congestion, which makes fee prediction easier for developers and users but also means capacity is implicitly capped by the council's tolerance.

## Finality and use-case fit

[Hedera](/hedera-hashgraph/) finalizes transactions in roughly 5–10 seconds with formal Byzantine guarantees. This is faster than [Bitcoin](/bitcoin/) (minutes) or [Ethereum](/ethereum/) (seconds but probabilistic), and comparable to other proof-of-stake systems.

The speed and throughput make [Hedera](/hedera-hashgraph/) attractive for enterprise use cases: supply-chain tracking, audit logs, licensing, and high-frequency settlement. It is less attractive for retail or DeFi use cases, where network effects and ecosystem richness (which [Ethereum](/ethereum/) dominates) matter more.

## Comparison to other consensus models

[NEAR](/near-protocol/) uses sharding to scale while maintaining a blockchain structure. [Algorand](/algorand/) uses cryptographic lotteries within a blockchain. [Tezos](/tezos/) uses traditional proof-of-stake with on-chain governance.

[Hedera](/hedera-hashgraph/)'s DAG approach is less well-known than blockchain-based consensus, and it has fewer third-party integrations and developer tools than Ethereum-compatible systems. However, it is not the only DAG project; IOTA also uses DAG consensus, though with a different design.

The choice of DAG over blockchain is partly philosophical (some argue DAGs are more "natural") and partly practical. For [Hedera](/hedera-hashgraph/)'s use cases—high throughput, institutional governance, predictable finality—the DAG structure is well-suited. For permissionless, decentralized, community-driven ecosystems, blockchain consensus has won out in practice.

## Adoption and ecosystem

[Hedera](/hedera-hashgraph/) has gained traction in enterprise and institutional circles, with pilots in logistics, healthcare, and government. The council governance gives regulators comfort. But retail adoption has been limited. HBAR, the native token, trades on [cryptocurrency exchanges](/cryptocurrency-exchange/), but [Hedera](/hedera-hashgraph/) dApp and DeFi ecosystems remain small relative to [Ethereum](/ethereum/).

This is a classic "enterprise blockchain" challenge: you gain institutional adoption but lose decentralized developer community. Moving the needle requires either breakout enterprise wins (major supply-chain adoption, for instance) or a tipping point in developer sentiment toward the platform.

## See also

<div class="wiki-seealso">

### Closely related

- [Directed acyclic graph](/distributed-ledger/) — DAG consensus model Hedera uses
- [Byzantine fault tolerance](/byzantine-fault-tolerance/) — formal safety guarantee
- [Proof of stake](/proof-of-stake/) — alternative consensus for comparison
- [Algorand](/algorand/) — pure PoS with immediate finality
- [NEAR Protocol](/near-protocol/) — sharding-based scalability
- [Tezos](/tezos/) — on-chain governance alternative

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger concepts
- [Distributed ledger](/distributed-ledger/) — foundational tech for all these systems
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where HBAR trades
- Smart contracts — application layer on Hedera

</div>

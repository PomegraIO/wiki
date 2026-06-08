---
title: "Flow"
description: "A blockchain that scales without sharding state by separating validator roles into execution, verification, and consensus nodes."
keywords:
  - flow blockchain
  - execution nodes
  - verification nodes
  - consensus nodes
  - blockchain scaling
  - dapps
image: "/svg/crypto.svg"
---

*[Flow](/flow-blockchain/) is a [blockchain](/distributed-ledger/) designed to scale transaction throughput by partitioning validator work across specialised node types—execution nodes that process transactions, verification nodes that check correctness, and consensus nodes that order transactions—rather than fragmenting state across shards. Built to support media and gaming applications, Flow demonstrates that you can increase capacity without asking every validator to maintain every account.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Flow — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain topics." />

<div class="wiki-infobox-caption">A blockchain that scales by role specialisation rather than state sharding.</div>

|   |   |
|---|---|
| **What it is** | A public [blockchain](/distributed-ledger/) with a [proof-of-stake](/proof-of-stake/) consensus layer and role-separated validators |
| **Consensus model** | Practical Byzantine Fault Tolerance (PBFT) with dedicated consensus nodes |
| **Primary use case** | Media, gaming, and user-friendly dapps (NFTs, marketplaces, games) |
| **Key innovation** | Separation of execution, verification, and consensus into distinct node roles |
| **Native token** | FLOW |
| **Notable characteristic** | Developer-friendly tooling; designed for mainstream adoption |

</aside>

## Why the traditional blockchain bottleneck exists

Every [blockchain](/distributed-ledger/) faces a fundamental tension: consensus requires that a supermajority of validators agree on the next block, which demands communication among them. The more validators you add for security, the more messages they must exchange. At the same time, every validator typically maintains a copy of the entire [blockchain](/distributed-ledger/) state—all accounts, balances, contracts. This redundancy is the source of security, but it also sets a hard ceiling on throughput. If you want to process 100,000 transactions per second, each validator would need hardware capable of executing 100,000 transactions per second locally. That bar climbs faster than hardware improves.

Most scaling solutions bite the bullet and shard state: split the [blockchain](/distributed-ledger/) into multiple independent chains that execute transactions in parallel. [Ethereum](/ethereum/), [Bitcoin](/bitcoin/), and others have explored or adopted sharding. But sharding introduces its own costs—cross-shard communication is expensive, and security becomes fragmented across shards.

## Flow's answer: role separation

Flow takes a different path. Instead of asking all validators to do all work, it splits validator responsibilities into three roles.

**Execution nodes** receive transactions, execute them against their current state copy, and produce a cryptographic proof (technically, a collection-state commitment). They do the hardest computational work but do not participate in consensus ordering. Hundreds of execution nodes can run in parallel.

**Verification nodes** check that execution nodes performed their work correctly. They do not re-execute every transaction; instead, they sample transactions and verify the proofs submitted by execution nodes. This sampling is probabilistic but statistically sound: if even a small fraction of verification nodes are honest, they will catch any misdeclared proof.

**Consensus nodes** form a tight committee that orders transactions and produces the canonical [blockchain](/distributed-ledger/) history. They communicate using [Practical Byzantine Fault Tolerance](https://en.wikipedia.org/wiki/Byzantine_fault_tolerance), a protocol that tolerates up to one-third malicious nodes. A dedicated consensus layer is fast because there are fewer of them and they only order transactions, not execute them.

In addition, **collection nodes** act as gateways, accepting user transactions and routing them to the network.

This separation allows execution and verification to scale independently of consensus. Flow can add more execution nodes to handle more transactions without slowing down the consensus layer or requiring every validator to store every state change.

## The trade-offs

Flow's design is elegant but comes with costs. First, it requires more infrastructure. A full validator on Flow runs multiple node types, and smaller participants may only run one type. This creates a spectrum of involvement rather than the homogeneous validator set that [Bitcoin](/bitcoin/) or early [Ethereum](/ethereum/) aspired to.

Second, the role separation introduces latency. Execution and verification add steps between transaction submission and finality. A transaction must be executed, then verified, then consensus must order it. Chains like [Bitcoin](/bitcoin/) with a single unified validator role can achieve finality in a single round of consensus (modulo Nakamoto finality); Flow adds extra layers.

Third, the correctness of the entire system depends on the statistical honesty of verification nodes. If the sampling probability is set too low, a coordinated set of execution nodes might slip false state past them. Flow's parameters try to make this infeasible, but the threat model is more complex than a simple majority-of-stake requirement.

## Implementation and adoption

Flow was built by Dapper Labs (now rebranded as Dapper), the team behind CryptoKitties, the early [blockchain](/distributed-ledger/) game that made Ethereum's scalability limits visible. That pedigree shows: Flow is engineered to feel smooth for non-technical users. It supports flow wallets that work with phone numbers, offers low transaction fees, and has attracted games, NFT marketplaces, and media companies.

The network uses [Proof of Stake](/proof-of-stake/) and offers staking rewards in FLOW tokens. As of recent checks, the network remains active but has smaller total value locked than [Ethereum](/ethereum/) or [Solana](/solana/), reflecting both its smaller developer base and its narrower use case (media and gaming rather than general finance).

Flow demonstrates a real architectural choice: rather than chase the highest possible throughput via sharding or rollups, you can achieve meaningful scale by reconceptualising what a validator does. By letting execution be stateless and distributed, and consensus be narrow and fast, Flow sidesteps the need to fragment state. For applications that fit its design—particularly those that can tolerate the additional latency—it offers a cleaner scalability story than sharded systems.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — consensus model used by Flow validators
- [Distributed Ledger](/distributed-ledger/) — underlying technology shared by all blockchains
- [Blockchain Fundamentals](/blockchain-fundamentals/) — broader context for how blockchains operate
- [Ethereum](/ethereum/) — primary smart contract platform, different scaling approach
- [Solana](/solana/) — alternative high-throughput blockchain design

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where FLOW tokens are traded
- [Bitcoin](/bitcoin/) — the original blockchain with simpler validator roles
- [Internet Computer](/internet-computer/) — alternative L1 with different execution model
- [Celo](/celo/) — another L1 focused on specific user needs
- [Scroll](/scroll/) — L2 scaling solution using different technique

</div>

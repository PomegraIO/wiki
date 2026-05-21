---
title: "Distributed Ledger"
description: "A distributed ledger is a database maintained across many independent computers, each holding a copy of the same data. No single entity controls it, and consensus mechanisms ensure agreement on state."
keywords:
  - distributed ledger
  - decentralised
  - ledger
  - blockchain
  - peer-to-peer
  - consensus
image: "/svg/crypto.svg"
---

*A **distributed ledger** is a database that is replicated and synchronised across multiple independent computers without a central authority. Each computer (called a node) holds a full or partial copy of the ledger, and the network uses a consensus mechanism to ensure all copies agree on the state of accounts and transactions.*

<div class="wiki-hatnote">

This entry covers distributed ledgers as a concept. For blockchains specifically, see [blockchain fundamentals](/blockchain-fundamentals/); for specific implementations, see [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Distributed Ledger — core characteristics</div>

<img src="/svg/crypto.svg" alt="Distributed network of nodes maintaining copies of ledger" />

<div class="wiki-infobox-caption">A distributed ledger: many copies, no central authority.</div>

|   |   |
|---|---|
| **What it is** | A replicated database across independent nodes |
| **Governance** | Decentralised consensus |
| **Copies** | Each node maintains a full or partial copy |
| **Synchronisation** | Consensus mechanism (proof-of-work, proof-of-stake, etc.) |
| **Immutability** | Difficult to alter past records without detection |
| **Authority** | No single point of control or failure |
| **Key advantage** | Trust without a trusted intermediary |

</aside>

## Contrast with centralised systems

Traditional databases — used by banks, governments, and most organisations — are centralised. A single entity owns the database, controls who can access it, and determines which transactions are valid.

A distributed ledger inverts this model. Instead of a single source of truth, there are many copies. Instead of a single entity deciding what is valid, the network reaches consensus. This eliminates the need for a trusted intermediary.

The trade-off is efficiency and simplicity. A centralised bank can process transactions far faster than a distributed ledger and can offer customer service (reversing errors, recovering lost passwords). A distributed ledger is slower but does not require trusting a bank.

## Nodes and replication

In a distributed ledger, each participating node stores a copy of the ledger and validates incoming transactions. When a new transaction occurs, nodes gossip about it — forwarding it to other nodes — until all nodes have heard about it.

Some systems use full replication, where every node stores every transaction (e.g., [Bitcoin](/bitcoin/)). Others use partial replication, where nodes store a subset of data relevant to them. Partial replication reduces storage and bandwidth requirements but complicates auditing.

## Consensus mechanisms

For a distributed ledger to function, all nodes must agree on the order and validity of transactions. This is the **consensus problem**. Various mechanisms exist:

- **[Proof-of-work](/proof-of-work/)** — nodes compete to solve puzzles; the fastest wins the right to add the next block.
- **[Proof-of-stake](/proof-of-stake/)** — validators with locked collateral are randomly selected to propose blocks.
- **[Delegated proof-of-stake](/delegated-proof-of-stake/)** — token holders vote for a small number of validators.
- **Practical Byzantine Fault Tolerance** — a voting-based consensus used in some enterprise systems.

Each mechanism has trade-offs between decentralisation, scalability, and energy efficiency.

## Immutability and fork resistance

Distributed ledgers are often called immutable because altering past records is extremely difficult. If a node tries to rewrite history, other nodes will reject it as invalid. An attacker would need to control a majority of nodes simultaneously, which is expensive on large networks.

However, no distributed ledger is perfectly immutable. With a majority attack (called a 51% attack), an attacker can rewrite history. The security of a distributed ledger depends on its consensus mechanism and the cost of controlling a majority of validators.

## Use cases

Distributed ledgers are valuable when:

- **Eliminating intermediaries.** Payments can move directly between parties without a bank.
- **Censorship resistance.** No single entity can prevent transactions.
- **Transparency.** All participants can audit the ledger.
- **Reduced fraud.** Immutability makes altering records difficult.

Common use cases include:

- **Cryptocurrencies.** [Bitcoin](/bitcoin/) and [Ethereum](/ethereum/) are distributed ledgers.
- **Supply-chain tracking.** Recording the journey of goods from manufacture to sale.
- **Smart contracts.** Programs that execute automatically on a distributed ledger.
- **Land registries.** Recording property ownership in jurisdictions without reliable government records.

## Challenges and limitations

Distributed ledgers are slower than centralised systems. A bank's database can process thousands of transactions per second; [Bitcoin](/bitcoin/) processes about seven. This latency is inherent — distributed consensus takes time.

They are also more expensive to operate. Each node maintains a copy of the ledger, consuming storage and bandwidth. Consensus mechanisms require computational work (puzzles or voting), consuming electricity.

Additionally, distributed ledgers are worse at reversing errors. If a transaction is sent to the wrong address by mistake, it cannot be undone like a bank transfer can be. This makes the user experience worse for genuine mistakes.

## Variations and alternatives

Not all distributed ledgers use [blockchain](/blockchain-fundamentals/) architecture. Some use a **directed acyclic graph** (DAG), where each transaction references multiple previous transactions, rather than grouping transactions into blocks. DAGs are potentially faster but more complex to implement.

Others use **consensus algorithms** that are less energy-intensive than [proof-of-work](/proof-of-work/), such as [proof-of-stake](/proof-of-stake/) or voting-based mechanisms.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledgers as chains of blocks
- [Proof-of-work](/proof-of-work/) — a consensus mechanism
- [Proof-of-stake](/proof-of-stake/) — an alternative consensus mechanism
- [Bitcoin](/bitcoin/) — the first famous distributed ledger
- [Ethereum](/ethereum/) — a distributed ledger with smart contracts

### Wider context

- [Public blockchain](/public-blockchain/) — decentralised and permissionless
- [Private blockchain](/private-blockchain/) — restricted and permissioned
- Smart contract — programs on distributed ledgers
- [Consensus mechanism](/proof-of-work/) — how agreement is reached
- 51% attack — attacking a distributed ledger with majority power

</div>

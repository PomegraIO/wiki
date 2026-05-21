---
title: "Blockchain Fundamentals"
description: "A blockchain is a distributed ledger that records transactions in blocks of cryptographically linked data. Each block references the previous block, creating an immutable chain of records secured by decentralised consensus."
keywords:
  - blockchain
  - distributed ledger
  - block
  - hash
  - cryptography
  - consensus
image: "/svg/crypto.svg"
---

*A **blockchain** is a [distributed ledger](/distributed-ledger/) — a database maintained across many independent computers without a central authority. Data is grouped into blocks, each cryptographically referencing the previous block, creating an immutable chain. Blockchains use consensus mechanisms to ensure agreement across the network about which transactions are valid.*

<div class="wiki-hatnote">

This entry covers the core technology of blockchains. For specific consensus mechanisms, see [proof-of-work](/proof-of-work/) or [proof-of-stake](/proof-of-stake/); for cryptocurrencies built on blockchains, see [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Blockchain — core concepts</div>

<img src="/svg/crypto.svg" alt="Blockchain structure with chained blocks" />

<div class="wiki-infobox-caption">A blockchain: blocks of transactions linked cryptographically into an immutable chain.</div>

|   |   |
|---|---|
| **What it is** | A distributed database with cryptographic linking |
| **Core function** | Record and verify transactions without central authority |
| **Participants** | Nodes (computers running the protocol) |
| **Verification** | Consensus mechanism (proof-of-work, proof-of-stake, etc.) |
| **Immutability** | Past blocks become increasingly difficult to alter |
| **Key innovation** | Solving the "double-spend" problem without a bank |
| **Key limitation** | Slow and resource-intensive compared to centralised systems |

</aside>

## How a blockchain works

A blockchain is fundamentally a ledger of transactions. When users initiate transactions, they are broadcast to a network of independent computers (called nodes). These nodes collect transactions, verify them, and bundle them into a block.

Each block contains:

- **Transactions.** The data being recorded (payments, contracts, etc.).
- **Timestamp.** When the block was created.
- **Hash of the previous block.** A cryptographic fingerprint that links it to the block before it.
- **Nonce or proof.** Data proving the block is valid according to the consensus rules (varies by mechanism).

The hash of each block is computed from its contents. If a single transaction in an old block is altered, the block's hash changes, which breaks the chain for all subsequent blocks. This makes altering past transactions extremely visible and difficult.

## Decentralisation and consensus

Traditional databases are controlled by a single organisation, which can alter records, censor transactions, or go offline. Blockchains distribute control across many independent nodes, eliminating a single point of failure or corruption.

But with no central authority, nodes must agree on the state of the ledger. This is the **consensus problem**. Blockchains solve it through mechanisms like:

- **[Proof-of-work](/proof-of-work/)** — nodes compete to solve puzzles; the first to solve it proposes the next block and is rewarded.
- **[Proof-of-stake](/proof-of-stake/)** — validators who lock up collateral are selected to propose blocks; if they misbehave, they lose their collateral.

Both mechanisms align incentives: nodes are rewarded for honest participation and punished for attacks.

## Immutability and finality

A key property of blockchains is immutability — once a block is old enough, altering it becomes prohibitively expensive. On [Bitcoin](/bitcoin/), a transaction buried under six blocks is considered final; reversing it would require re-mining all six blocks, costing more than the value stolen.

This is stronger than traditional databases, which rely on access controls and auditing. A blockchain records history in a way that is mathematically difficult to fake.

However, "immutable" does not mean "perfectly immutable." With sufficient resources (>50% of the [hash rate](/hash-rate/) on [Bitcoin](/bitcoin/)), an attacker could reverse transactions. Blockchains trade off perfect immutability for economic finality — reversing old transactions is so expensive that it is not worth attempting.

## Transparency and pseudonymity

Most blockchains, including [Bitcoin](/bitcoin/) and [Ethereum](/ethereum/), are transparent — all transactions are public and visible to anyone. This allows anyone to verify the ledger independently, increasing confidence in its integrity.

However, transparency does not mean users are identified. Addresses are pseudonymous strings of characters; unless someone publicly reveals which address they control, their identity remains private. This is why [Bitcoin](/bitcoin/) is often called "pseudonymous" rather than "anonymous." With sufficient analysis, transactions can sometimes be linked to identities.

[Monero](/monero/) is an exception — it uses cryptographic techniques to hide sender, recipient, and amounts, achieving stronger privacy at the cost of requiring trust that the cryptography is sound.

## Public versus private blockchains

A [public blockchain](/public-blockchain/) like [Bitcoin](/bitcoin/) is permissionless — anyone can run a node, validate transactions, or participate in consensus. No gatekeeper controls access.

A [private blockchain](/private-blockchain/) restricts participation to approved entities. Private blockchains are useful for enterprise applications (supply-chain tracking, internal record-keeping) where decentralisation is less critical than control and efficiency.

## The blockchain trilemma

Blockchains face a fundamental trade-off called the **scalability trilemma**: it is difficult to achieve decentralisation, security, and scalability simultaneously.

- **Decentralisation.** Many independent nodes, each able to run on modest hardware.
- **Security.** Difficult and expensive to attack or alter past transactions.
- **Scalability.** Fast transactions with high throughput (thousands per second).

Different blockchains prioritise differently. [Bitcoin](/bitcoin/) prioritises security and decentralisation; [Solana](/solana/) prioritises scalability and security, sacrificing decentralisation slightly; [Ethereum](/ethereum/) aims for a balanced approach, with layer-2 solutions adding scalability.

## Use cases and criticisms

Blockchains are suited for scenarios where:

- A central authority cannot be trusted.
- Multiple parties must agree without intermediaries.
- Transparent record-keeping is valuable.

Criticisms include:

- **Slow and expensive.** Blockchains are orders of magnitude slower than centralised databases.
- **Energy-intensive.** [Proof-of-work](/proof-of-work/) consensus consumes substantial electricity.
- **Immutability as a bug.** The inability to reverse transactions is problematic if errors or fraud occur.
- **Not-invented-here syndrome.** Many proposed uses for blockchains could be solved more simply without one.

## See also

<div class="wiki-seealso">

### Closely related

- [Distributed ledger](/distributed-ledger/) — the foundational concept
- [Proof-of-work](/proof-of-work/) — a consensus mechanism
- [Proof-of-stake](/proof-of-stake/) — an alternative consensus mechanism
- [Bitcoin](/bitcoin/) — the first and most famous blockchain
- [Ethereum](/ethereum/) — a blockchain with smart contracts

### Wider context

- [Public blockchain](/public-blockchain/) — decentralised and permissionless
- [Private blockchain](/private-blockchain/) — restricted and permissioned
- Smart contract — programs running on blockchains
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where blockchain assets trade
- Layer-2 — scaling solutions built on top of blockchains

</div>

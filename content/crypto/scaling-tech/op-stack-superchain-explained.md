---
title: "OP Stack and the Superchain Explained"
description: "Learn how the OP Stack is a modular codebase for building Optimism-compatible Layer 2 chains and how the Superchain vision aims to unify them."
keywords:
  - op stack superchain explained
  - optimism layer 2
  - rollup scaling
  - shared sequencing
  - blockchain composability
image: /svg/crypto.svg
---

*The **OP Stack** is a modular software framework that allows developers to spin up Ethereum-compatible Layer 2 blockchains using Optimism's battle-tested code. The **Superchain** is Optimism's vision for linking many OP Stack chains through shared sequencing, unified messaging, and interoperability—transforming a fragmented ecosystem of separate chains into a coordinated network that shares security and liquidity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OP Stack & Superchain — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">Modular rollup infrastructure and cross-chain coordination.</div>

|   |   |
|---|---|
| **OP Stack core** | Open-source modules (sequencer, contracts, proof system) that can be configured to build optimistic rollups |
| **Target:** Optimism-compatible | Chains built on OP Stack are compatible with Ethereum and can run EVM (Ethereum Virtual Machine) code |
| **Deployment flexibility** | Developers can customize gas pricing, sequencing, data availability, and settlement layers |
| **Superchain coordination** | Planned infrastructure to link OP Stack chains: shared sequencing, atomic cross-chain messaging, unified liquidity |
| **Sequencing** | A single sequencer collects transactions, orders them, and commits batches to Ethereum (or another layer) |
| **Proof system** | Fault proofs: if a sequencer commits a fraudulent state transition, any participant can prove it wrong and revert |

</aside>

## What Is the OP Stack?

The OP Stack is a **modular framework** for building optimistic rollups—Layer 2 blockchains that process transactions off-chain and periodically post commitments to Ethereum. Rather than monolithic software, the OP Stack is structured in layers:

- **Execution layer**: The virtual machine and state transition function (typically EVM-compatible)
- **Sequencing layer**: The server that collects pending transactions, orders them, and proposes blocks
- **Derivation layer**: Rules for how the sequencer's commitments are interpreted and verified
- **Settlement layer**: Where the rollup posts compressed transaction data and state roots (usually Ethereum, but configurable)
- **Proof layer**: Fault proofs or validity proofs used to verify the correctness of state transitions

The genius of the OP Stack is that each layer is *replaceable*. A developer can use Optimism's standard components, or swap out the sequencer, the settlement layer, the data availability scheme, or even the virtual machine—and still achieve Ethereum compatibility and the security properties of the rollup model.

This modularity unlocked what was previously impossible: dozens of teams building their own Layer 2 chains without rewriting rollup infrastructure from scratch. Arbitrum, Polygon, Starknet, and other scaling platforms all use proprietary stacks; the OP Stack is Optimism's open-source, composable alternative.

## How It Works: The Optimistic Rollup Model

All OP Stack chains operate on the same fundamental principle as Optimism itself: **optimistic rollup**. Transactions are executed off-chain by the sequencer. The sequencer posts a commitment (a state root) to the settlement layer (Ethereum) along with compressed transaction data. Everyone assumes the sequencer is honest *until proven otherwise*.

If anyone suspects the sequencer has committed a fraudulent state transition, they can post a **challenge** or **fault proof**—a cryptographic proof that the claimed state is incorrect. The settlement layer (Ethereum) then verifies the proof and, if it's valid, reverts the fraudulent state.

This design is secure because Ethereum itself is the final arbiter. The rollup is only as secure as Ethereum—if Ethereum can verify a proof, the rollup cannot be attacked without also attacking Ethereum.

For users, the flow is:

1. **Deposit**: User sends ETH or tokens to the rollup contract on Ethereum.
2. **Use**: User interacts with the OP Stack chain at Layer 2, which processes transactions in seconds.
3. **Withdraw**: User initiates a withdrawal. After a challenge window (7 days on Optimism, configurable), the withdrawal is finalized and funds return to Ethereum.

The 7-day withdrawal window allows time for anyone to post a fault proof if the sequencer misbehaved. If no challenge is posted, the withdrawal is assumed valid and executed.

## Configurability: Why It Matters

The OP Stack's modularity means developers can customize:

- **Gas pricing** and transaction costs (different pricing models than Ethereum)
- **Sequencer identity** (centralized sequencer, rotating sequencers, or decentralized sequencing)
- **Data availability** (post data to Ethereum calldata, blobs, or an external DA layer)
- **Settlement confirmation time** (how long until withdrawals are final)

A developer might create a specialized rollup for gaming (low latency, high throughput) with a trusted sequencer and no fault-proof overhead. Another might build a high-security chain with decentralized sequencing and full on-chain proof verification. Both use the OP Stack; both run EVM code; but they have radically different security and performance tradeoffs.

This flexibility explains why dozens of teams have adopted OP Stack: Coinbase's Base, Lyra's Layer 2, Aevo, Mantle, and others are all OP Stack chains with different configurations.

## The Superchain Vision

The Superchain is Optimism's grand ambition: linking many OP Stack chains into a **unified, interoperable network**. Currently, each OP Stack chain is isolated. To move assets from Base to Optimism, users must bridge through Ethereum, which is slow and expensive.

The Superchain would enable:

**Shared Sequencing**: A single sequencer (or a small set) orders transactions across *all* Superchain chains at once. This eliminates the race condition where the sequencer on Chain A prioritizes transactions ahead of the sequencer on Chain B, causing arbitrage or unfair ordering across chains.

**Atomic Cross-Chain Messaging**: The protocol would guarantee that a message sent from Chain A to Chain B is either fully executed or fully reverted—no in-between states. This allows smart contracts on different chains to atomically swap assets or coordinate state changes.

**Unified Liquidity**: Bridges between Superchain chains would be faster, cheaper, and more trustworthy because they operate under the same shared sequencing and messaging layer.

**Shared Security**: All Superchain chains would ultimately settle to Ethereum, so they all inherit Ethereum's security. A successful attack on one chain would require attacking Ethereum itself.

The Superchain is **not yet live**. Optimism is still designing and testing the shared sequencer, the cross-chain messaging protocol, and the governance structures needed to coordinate many chains. But it represents the long-term vision: instead of a fragmented ecosystem where each rollup is an island, chains would be part of a coordinated, interoperable fabric.

## Differences from Other Scaling Solutions

The OP Stack differs from other approaches:

- **Sidechains** (like Polygon's PoS chain) are independent blockchains with their own validators, not settlement layers. They do not inherit Ethereum's security.
- **Validiums** like Starknet use validity proofs (cryptographically proven correct) rather than optimistic rollups (assumed correct until challenged). This allows faster finality but requires more computational resources.
- **Sovereign rollups** post data to Ethereum but do *not* settle to Ethereum; they remain fully independent. Some OP Stack chains can be configured as sovereign rollups.

The OP Stack's strength is its balance: it is Ethereum-secured, EVM-compatible, and modular enough to serve many different use cases.

## Adoption and Ecosystem Fragmentation

Dozens of OP Stack chains now exist, but they remain isolated from one another. This has created a **fragmentation problem**: users must choose which chain to use, and liquidity is spread across many chains rather than concentrated.

The Superchain aims to solve fragmentation by making chain selection transparent to users. Instead of "Which Base address should I use, or which Optimism address?" the network would feel like a single protocol with many execution contexts. The Superchain would be the Ethereum ecosystem's answer to a single, mega-chain.

## See also

<div class="wiki-seealso">

### Closely related

- [Optimistic Rollup](/optimistic-rollup/) — how optimistic rollups achieve scalability while inheriting Ethereum security
- [Layer 2 Scaling](/layer-2-scaling/) — off-chain solutions that settle to Ethereum periodically
- [Smart Contract](/smart-contract/) — programmable agreements that run on blockchains
- Sequencer — the entity that orders transactions and proposes blocks
- [Ethereum](/ethereum/) — the settlement and security layer for OP Stack chains

### Wider context

- Blockchain Scalability — challenges and solutions for throughput and cost
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where assets move between chains via bridges
- Cross-Chain Messaging — protocols for communicating between separate blockchains
- Ethereum Virtual Machine — the runtime that executes smart contracts

</div>

---
title: "Scroll"
description: "An Ethereum layer 2 that uses zero-knowledge proofs to verify transactions while remaining bytecode-equivalent with the Ethereum Virtual Machine."
keywords:
  - scroll
  - layer 2
  - zk-evm
  - zero knowledge proof
  - ethereum scaling
image: "/svg/crypto.svg"
---

*[Scroll](/scroll/) is an Ethereum layer 2 that batches transactions and settles them on [Ethereum](/ethereum/) using zero-knowledge proofs, while preserving bytecode compatibility with the [Ethereum](/ethereum/) Virtual Machine—meaning existing smart contracts deploy unchanged. Unlike rollups that emulate the EVM or rely on optimistic fraud proofs, Scroll uses cryptographic validity proofs to guarantee correctness, trading computational overhead for finality.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Scroll — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain topics." />

<div class="wiki-infobox-caption">A ZK-rollup that maintains EVM bytecode compatibility without modification.</div>

|   |   |
|---|---|
| **What it is** | An Ethereum L2 using zero-knowledge proofs (zk-SNARK) to verify transaction batches |
| **EVM compatibility** | Bytecode-equivalent; no recompilation or redeployment needed |
| **Settlement** | Validity proofs posted to [Ethereum](/ethereum/) ensure L2 state is correct |
| **Throughput** | 10–100x higher than Ethereum mainnet depending on transaction type |
| **Finality** | Transactions final once ZK proof is verified on-chain (no optimistic delay) |
| **Native asset** | Ether (ETH); uses Ethereum's security |

</aside>

## Why layer 2s exist

[Ethereum](/ethereum/) mainnet processes roughly 12–15 transactions per second and charges fees in dollars per transaction during periods of congestion. For applications that require cheap, high-throughput settlement—payments, exchanges, gaming—mainnet is prohibitively expensive and slow.

A layer 2 runs a separate blockchain that rolls up thousands of transactions into a single proof or assertion posted back to [Ethereum](/ethereum/). Users interact with the L2 directly, experiencing fast confirmation times and low fees. Periodically, the L2 submits evidence of its correctness to [Ethereum](/ethereum/), which acts as an anchor and arbiter of last resort.

There are two main flavours of layer 2: optimistic rollups (Arbitrum, Optimism) and zero-knowledge rollups (Scroll, StarkNet). Optimistic rollups assume transactions are valid unless someone provides evidence of fraud. ZK rollups cryptographically prove validity upfront. The trade-off is computation: ZK proofs require heavy cryptographic machinery, whereas optimistic rollups are lighter but add a delay (fraud-proof window) before finality.

## Scroll's approach: bytecode equivalence

Most ZK-EVM projects face a puzzle: how do you prove the execution of [Ethereum](/ethereum/) code using zero-knowledge circuits? The EVM has 150+ opcodes, complex state transitions, and intricate gas mechanics. Building a ZK circuit that faithfully reproduces all of this is difficult and slow.

Scroll's solution is bytecode equivalence: instead of building circuits for the EVM itself, Scroll built an architecture where the EVM bytecode is proved directly. This is possible through a technique called "lookup tables" and careful circuit design, but it is not trivial. The result is that Scroll can accept any [Ethereum](/ethereum/) smart contract—Uniswap, Aave, OpenZeppelin libraries, custom code—without any modification or recompilation. A contract that costs 100,000 gas on [Ethereum](/ethereum/) will cost roughly the same on Scroll.

This is different from chains like [Internet Computer](/internet-computer/), which require WebAssembly, or the original Polygon, which requires Solidity to be recompiled for a different execution environment. Scroll's bytecode-equivalence means zero migration friction for developers and no risk of subtle semantic divergence.

## How Scroll settles

A Scroll sequencer batches transactions into blocks and executes them, building up a new state root. Once the batch is complete, the sequencer generates a zero-knowledge proof that the batch was executed correctly according to EVM rules. This proof is a small-ish file (in the megabyte range after compression) that cryptographically certifies: "Given state root A and this batch of transactions, the result is state root B, and every operation is valid."

That proof is posted to [Ethereum](/ethereum/), where a smart contract verifies it. Verification is fast—typically under a second—and cheap relative to the cost of executing those transactions on [Ethereum](/ethereum/) directly. Once verified, the new state is canonical, and funds can be withdrawn to [Ethereum](/ethereum/) mainnet with certainty.

This design offers several benefits. First, finality is faster than optimistic rollups, which must wait a week or more to confirm no fraud-proofs are submitted. Second, there is no "safety committee" of chosen verifiers; anyone with the proof can verify it using [Ethereum](/ethereum/) consensus. Third, the security is purely cryptographic—no assumptions about economic incentives or honest-majority participants.

## Practical trade-offs

Scroll's main cost is proof generation time and computational overhead. Generating a validity proof for a batch of transactions takes longer than simply executing them. This means Scroll's block times are slower than [Ethereum](/ethereum/) (around 12–15 seconds rather than 12 seconds for [Ethereum](/ethereum/], but the difference compounds). For high-frequency trading or latency-sensitive applications, this is a consideration.

Proof generation is also capital-intensive: it requires dedicated proving hardware. Scroll has invested heavily in proof acceleration and aggregation (proving proofs of proofs) to keep proof times reasonable. As hardware improves and proving circuits are optimised, this overhead will decline.

Gas costs on Scroll are lower than [Ethereum](/ethereum/]—typically 10–100x cheaper depending on transaction type. Simple transfers might cost $0.01; a Uniswap swap might cost $0.10. This is sufficient for retail users and applications that depend on marginal economics.

## Governance and ecosystem

Scroll is maintained by the Scroll Foundation, a non-profit, with contributions from the broader developer community. The network operates with a decentralised sequencer set; multiple sequencers can propose blocks, reducing centralisation risk. Over time, the goal is full decentralisation of sequencing and proving.

Because Scroll maintains EVM bytecode compatibility, the ecosystem is growing rapidly. Major protocols like Uniswap, Aave, and Curve have deployed to Scroll. Wallet and tooling developers find Scroll easy to integrate: it is [Ethereum](/ethereum/) with the same JSON-RPC API and contract interface.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum/) — base layer that Scroll settles to
- Zero-Knowledge Proofs — cryptographic foundation of Scroll's validity proofs
- Layer 2 Solutions — broader category Scroll belongs to
- Smart Contracts — applications that run on Scroll
- [Distributed Ledger](/distributed-ledger/) — fundamental blockchain technology

### Wider context

- [Flow](/flow-blockchain/) — alternative L1 scaling via role separation
- [Internet Computer](/internet-computer/) — another L1 with different execution model
- [Celo](/celo/) — L1 focused on financial inclusion
- [Bitcoin](/bitcoin/) — original blockchain, different design constraints
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where ETH is traded

</div>

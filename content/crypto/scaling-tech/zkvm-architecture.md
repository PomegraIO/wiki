---
title: "zkVM Architecture"
description: "A zero-knowledge virtual machine that proves arbitrary computation for rollup state transitions, replacing traditional fraud proofs with cryptographic certainty."
keywords:
  - zkvm
  - zero-knowledge virtual machine
  - rollup proofs
  - computation verification
  - state transition
  - zk-stark
image: "/svg/crypto.svg"
---

*A **zkVM (zero-knowledge virtual machine)** is a specialized computer system that executes arbitrary transactions and generates a cryptographic proof that the computation was correct, without revealing the transactions themselves. Rollups use zkVMs to prove state transitions instead of relying on fraud challenges or traditional re-execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">zkVM Architecture — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain architecture." />

<div class="wiki-infobox-caption">A zkVM proves state correctness without exposing computation details.</div>

|   |   |
|---|---|
| **What it is** | A virtual machine that generates zero-knowledge proofs of correct execution |
| **Main job** | Execute rollup transactions and produce a proof the state transition is valid |
| **Proof system** | Usually zero-knowledge SNARK or STARK for scalability |
| **Contrast to** | Optimistic rollups, which post state roots and wait for fraud challenges |
| **Output** | A single proof (a few hundred bytes) proving correctness of millions of transactions |
| **Cost** | Proof generation is slow; on-chain verification is cheap and fast |

</aside>

## The execution-to-proof pipeline

A zkVM operates in two phases: execution and proving. First, the zkVM runs the rollup's transactions, just like a normal [Ethereum](/ethereum/) or application-chain node would. It maintains state: account balances, contract storage, nonces. It applies transactions one by one. After executing all transactions in a block, the zkVM outputs a new state root (a hash representing the updated state) and a proof.

This proof is the revolutionary part. Instead of saying "trust me, I ran these transactions correctly," the zkVM says "here is a cryptographic proof that my state root is correct." The proof uses zero-knowledge mathematics to guarantee correctness without requiring an independent verifier to re-execute every transaction.

The on-chain verifier—a smart contract on Ethereum or another settlement layer—needs only to check the proof, which takes milliseconds and consumes a few thousand gas. The actual computation, which might have taken minutes off-chain, is compressed into a verification operation that's orders of magnitude cheaper.

## Why zkVM over fraud proofs

[Optimistic rollups](/optimistic-rollup/) use a different approach: they post a state root and wait 7 days for a challenger to prove the root is wrong. If no challenge materialises, the state is considered final. This is elegant but slow and capital-inefficient—a user wanting to withdraw funds must wait a week.

A zkVM is faster to finality. Once the proof is verified on-chain, the state is cryptographically final. No waiting period, no challenge window. This is why [zero-knowledge rollups](/zero-knowledge-rollup/) (which use zkVMs) are called "validity rollups": their state is valid immediately.

The tradeoff is computational complexity. Generating a zkVM proof is hard work. The zkVM must trace every step of execution, prove each step's logical correctness, and then compress that trace into a small proof. For a complex computation with millions of steps, this can take minutes on modern hardware. For high-frequency trading or frequent state updates, this latency might be unacceptable.

Optimistic rollups avoid this: posting a state root is instant (bounded by sequencing time). They defer the hard work to the challenge phase, and only do it if someone disputes. zkVMs do the hard work upfront for every block.

## Proof systems: SNARK vs STARK

zkVMs typically use one of two proof systems: SNARK or STARK.

**SNARKs** (Succinct Non-interactive Argument of Knowledge) are compact proofs, often under 1 KB. They use elliptic curve cryptography and are well-established. The catch: they require a "trusted setup"—a one-time ceremony where cryptographic parameters are generated and destroyed. If the ceremony is compromised, proofs can be forged. Most major SNARKs (Groth16, PLONK, KZG) have undergone public ceremonies with thousands of participants, so the risk is low but non-zero.

**STARKs** (Scalable Transparent Argument of Knowledge) are larger proofs, typically 100–500 KB, but don't require a trusted setup. They use only hash functions and collision-resistant mathematics, so there's no secret to compromise. STARKs are more transparent, but the proof size makes them more expensive to verify on-chain.

zkVM designers choose based on priorities. Starknet uses STARKs for transparency. zkSync, Scroll, and others use SNARKs for compactness. Some hybrid designs (like proof aggregation) compress many SNARK or STARK proofs into one smaller proof, splitting the difference.

## Hardware acceleration and latency

Generating a zkVM proof by a general-purpose CPU is slow—tens of minutes for a block of thousands of transactions. Production zkVMs offload to specialized hardware: GPUs accelerate field arithmetic, and FPGAs or custom silicon (like Starkware's Giza or Scroll's chips) make proving nearly real-time.

This hardware dependency is a practical reality. A zkVM without hardware acceleration is academic; a production rollup needs it. This creates supply-chain concentration: as zkVM performance becomes hardware-dependent, the manufacturers of that hardware—and the expertise to operate it—become critical infrastructure.

Newer proof systems (like Binius, which uses smaller fields) aim to reduce hardware requirements, but state-of-the-art proving still benefits from parallelisation and optimised arithmetic.

## Recursion and aggregation

A zkVM can prove another proof. This recursive property is powerful: instead of generating one giant proof for a week's worth of transactions, you can break the transactions into chunks, generate proofs for each chunk, then generate a proof that all the chunk-proofs are correct. The final proof is much smaller and faster to generate than a monolithic one.

Recursion is also the basis of [proof aggregation](/proof-aggregation/), where thousands of transaction-level proofs are compressed into a single on-chain proof. Verifying one aggregated proof on Ethereum costs roughly the same as verifying one transaction-level proof, so you've amortised the cost across thousands of transactions.

This is a key advantage of zkVMs: their mathematical properties allow structural efficiency that optimistic fraud proofs cannot match.

## Limitations and open problems

**Proof latency**: Proving takes time. For real-time systems (like trading bots), a multi-minute proving delay is unacceptable.

**Hardware dependency**: Leading zkVMs require specialised hardware. This creates barriers to entry and centralises proving to a few operators with the gear.

**Compatibility**: zkVMs must faithfully reproduce computation. If a zkVM supports Solidity [smart contracts](/smart-contract/), it must prove all of Solidity's semantics—memory, storage, gas, exceptions. This is complex and error-prone. Some zkVMs support a limited language (like Cairo on Starknet) to simplify proving; others accept slower proving to support full EVM compatibility.

**Proof verification cost**: SNARK verification is cheap (a few thousand gas per proof), but STARK verification is expensive (hundreds of thousands of gas). This drives the choice of proof system and the adoption of aggregation.

These are not showstoppers, but they explain why zkVMs are not yet dominant. Optimistic rollups, which avoid these problems, still power most L2 value.

## See also

<div class="wiki-seealso">

### Closely related

- [Zero-Knowledge Rollup](/zero-knowledge-rollup/) — a rollup built on zkVM proofs
- [Proof Aggregation](/proof-aggregation/) — compressing many zkVM proofs into one
- [Data Availability Layer](/data-availability-layer/) — where zkVM transactions are stored
- [Volition Hybrid Rollup](/volition-hybrid-rollup/) — uses zkVMs to handle mixed data availability
- Zero-Knowledge Proof — the cryptographic foundation of zkVMs
- [Optimistic Rollup](/optimistic-rollup/) — the fraud-proof alternative

### Wider context

- Rollup — broader scaling solution context
- [Smart Contract](/smart-contract/) — what zkVMs execute
- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundation

</div>

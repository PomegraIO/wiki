---
title: "Recursive SNARK"
description: "A cryptographic proof that verifies other proofs, enabling nested computation compression and exponential scaling of proof batching."
keywords:
  - recursive proof composition
  - snark verification
  - proof aggregation
  - computational scaling
  - zero-knowledge compression
image: "/svg/crypto.svg"
---

*A **recursive SNARK** is a zero-knowledge proof that verifies the validity of other proofs, not just raw data. By nesting proofs inside proofs, this technique compresses arbitrarily large computations into a single, small proof — the engine behind many blockchain scaling solutions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Recursive SNARK — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptographic proof composition." />

<div class="wiki-infobox-caption">Proofs that verify other proofs, enabling exponential compression.</div>

|   |   |
|---|---|
| **What it is** | A [zero-knowledge proof](/crypto/zero-knowledge-proof/) that takes another proof as input, verifies it, and outputs a new proof of correctness |
| **Key property** | Composability: proofs can be nested indefinitely without growing in size |
| **Primary use** | Batch aggregation of transactions, computations, or other proofs across many rounds |
| **Proof size** | Constant, regardless of the computation verified (typically a few hundred bytes) |
| **Verification cost** | Logarithmic in the depth of recursion, or constant with amortisation |
| **Also called** | Proof composition, proof aggregation, [SNARK](/crypto/snark/) folding |

</aside>

## How recursion transforms proofs

In a conventional SNARK, you prove that a specific input satisfies a computation. A recursive SNARK goes a step further: it proves that a *previous proof* is valid. This shift from verifying computation to verifying proofs unlocks a new paradigm.

Imagine a chain of 1,000 transactions. A naive approach requires generating a proof for all 1,000 together. A recursive approach works layer by layer: prove transactions 1–10, then prove that the proof-of-transactions-1–10 is correct *and* combine it with a proof of transactions 11–20, then fold that combined proof again with the next batch. Each step produces a proof of constant size. At the end, a single small proof certifies the entire chain.

This is why recursion is exponential: one level of recursion can halve the number of remaining proofs to verify. After *k* recursive steps, you've reduced 2^k proofs to just one.

## Folding: the practical mechanism

The most practical recursive SNARK construction uses **folding**. Instead of verifying a previous proof cryptographically (which is expensive), folding allows you to verify it *algebraically* by producing a new constraint that represents both the old proof's validity and the new computation in a single fold.

[IVC (Incremental Verifiable Computation)](/crypto/ivc/) and [Nova](/crypto/nova-folding/) are the canonical implementations. They reduce the verifier's work to a few cryptographic checks, regardless of how many times you've folded proofs together. The cost doesn't compound; it stays linear in the number of folds, not exponential.

## Why size doesn't grow

The insight that makes recursion practical is that proof verification itself is a computation, and that computation is usually *much smaller* than the original computation being proved. A SNARK for verifying a SNARK is far cheaper to generate than a SNARK for the underlying transaction data.

This asymmetry means you can afford to nest proofs dozens or hundreds of times and still end up with a proof smaller than the original. The constant-size property holds even as the depth of recursion grows.

## Applications in scaling

Rollups and other [layer 2](/crypto/layer-2/) systems use recursive SNARks to batch thousands of transactions into a single proof. Instead of posting 1,000 transaction proofs onchain, you post one recursive proof that says "I have verified all 1,000 proofs." The Ethereum [mainnet](/crypto/ethereum/) still performs one proof verification, not 1,000.

This compression extends beyond transactions. Recursive proofs can verify entire blocks, state transitions, or even other blockchains. Some designs layer recursion across multiple chains: a [rollup](/crypto/rollup/) proves its state, another rollup's proof verifies that proof, and so on.

## Practical limitations and tradeoffs

Recursive SNARK systems require careful engineering. The prover must generate intermediate proofs, which takes time and memory. Folding approaches like Nova are more efficient than traditional proof verification but still incur latency. A recursive prover cannot practically nest proofs more than 100–200 times in production before memory or computational time becomes prohibitive.

The verifier gains the most: verification time is cheap and constant. But the prover's work is nonlinear in the recursion depth. This tradeoff favours scenarios where verification happens frequently (blockchains) but proving happens less often (behind-the-scenes batch aggregation).

## Recursion meets other scaling techniques

Recursive SNARks work alongside other compression methods. [Danksharding](/crypto/scaling-tech/danksharding/) decouples data from computation; [proto-Danksharding](/crypto/scaling-tech/proto-danksharding/) stages the transition. Recursive proofs handle the *proof* layer. A full scaling stack might use data sharding for throughput and recursive proof folding for settlement assurance.

The two are complementary. Sharding pushes data availability in parallel; recursion compresses the proof of correct execution.

## See also

<div class="wiki-seealso">

### Closely related

- [Zero-Knowledge Proof](/crypto/zero-knowledge-proof/) — the cryptographic primitive underlying all SNARks
- [SNARK](/crypto/snark/) — succinct non-interactive arguments of knowledge
- [Rollup](/crypto/rollup/) — layer 2 solution that batches transactions and proves them recursively
- [Proto-Danksharding](/crypto/scaling-tech/proto-danksharding/) — EIP-4844 blob mechanism for proof and data availability
- [Danksharding](/crypto/scaling-tech/danksharding/) — full sharding design orthogonal to proof recursion

### Wider context

- [Layer 2](/crypto/layer-2/) — scaling solutions built on top of layer 1 blockchains
- [Proof of Work](/crypto/proof-of-work/) — consensus mechanism that benefits from compact proofs
- [Blockchain Fundamentals](/crypto/blockchain-fundamentals/) — the settlement layer that recursive proofs serve

</div>

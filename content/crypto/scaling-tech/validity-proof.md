---
title: "Validity Proof"
description: "Cryptographic evidence that a state transition was computed correctly, enabling instant finality without optimistic dispute periods."
keywords:
  - validity proof
  - zero-knowledge proof
  - zk-rollup
  - proof of computation
  - finality
  - rollup design
image: "/svg/crypto.svg"
---

*A **validity proof** is a cryptographic commitment that a transaction or batch of transactions was computed correctly, generated off-chain and verified on-chain in one deterministic check. Unlike [fraud-proof-mechanism](/fraud-proof-mechanism/) systems that wait for challengers to cry foul, validity proofs establish truth immediately — making them slower to generate but faster to settle.*

The fundamental trade-off in rollup design is computational cost versus settlement finality. Fraud proofs assume innocence and require weeks to prove guilt. Validity proofs assume nothing — they demand cryptographic proof from day one. That proof is expensive to generate (especially for complex computations) but cheap and instant to verify on-chain.

The most prominent validity proof systems use zero-knowledge techniques: the prover constructs a proof that transactions executed correctly without the on-chain verifier having to re-execute them. A ZK-rollup produces one proof per batch, the proof is verified in a single transaction, and finality is immediate.

## Zero-knowledge versus other proof systems

Validity proofs are most often zero-knowledge proofs (ZKPs), meaning the proof reveals no information about the computations except that they were done correctly. But the category is broader. A cryptographic commitment that "state A correctly transformed to state B" can be non-zero-knowledge (revealing execution details) and still be valid.

Zero-knowledge variants dominate because they offer privacy and compactness. A ZKP for a block of transactions can be under a kilobyte, verifiable in milliseconds on-chain, and reveal nothing about transaction details to observers. This is why most modern rollups targeting finality use ZK schemes.

## Instant finality and capital efficiency

The killer application of validity proofs is instant settlement. A user deposits funds, they appear in the rollup immediately, and a validity proof is generated within minutes. Once that proof hits the layer-1 chain and passes verification, the user can withdraw. No 7-day wait. No dispute window.

This speed advantage matters enormously for bridges, cross-chain activity, and merchant settlement. It also reduces proof-of-reserves requirements and improves [capital-adequacy](/capital-adequacy/) for rollup operators. In contrast, [optimistic-rollup](/optimistic-rollup/) systems must either lock capital during the dispute period or assume some watchers are trusted.

## Proof generation overhead

The cost is computational: generating a validity proof for a batch of transactions requires solving thousands of constraint equations, often using specialized hardware like GPUs or FPGAs. A single block proof might take minutes to an hour to generate, depending on complexity and circuit design.

This overhead is invisible to users but critical to rollup operators. If proof generation is too slow or expensive, the rollup's throughput drops or operators lose money. Many ZK-rollup teams are building proof acceleration hardware and pooling prover resources to amortise costs across many batches.

## Proof verification gas cost

On-chain, a validity proof verification is a single operation: check that the cryptographic commitment matches the claimed state transition. For most modern schemes, this costs 200,000–500,000 gas per batch, far cheaper than re-executing all transactions. But it's not free. At high transaction volumes, verification gas becomes a recurring cost that operators pass to users through fees.

Rollups may batch multiple transaction blocks into one proof to reduce per-transaction verification cost, but this delays finality slightly.

## Scheme diversity and risk

Validity proofs rest on hard cryptographic assumptions. ZK-SNARKs (succinct non-interactive arguments of knowledge) are widely used but depend on elliptic curve discrete-log hardness and specialised setup ceremonies. ZK-STARKs avoid trusted setup but produce larger proofs. Newer schemes like STNARKs and Bulletproofs trade off proof size, verification cost, and setup requirements.

If a scheme's underlying assumption breaks — say, discrete log becomes efficiently solvable — an entire rollup could be compromised. Most projects use well-studied schemes, but audits and real-world use remain the strongest signal of safety.

## Comparative advantage

Validity proofs beat fraud proofs on finality and settlement speed. Fraud proofs have an advantage in simplicity: the verification logic is just deterministic re-execution of a transaction, which is easier to audit and less likely to harbour cryptographic surprises. This is why some projects embed both: use fraud proofs as a backup dispute layer while relying on validity proofs as the fast path.

## See also

<div class="wiki-seealso">

### Closely related

- [Fraud Proof Mechanism](/fraud-proof-mechanism/) — Dispute-based security alternative requiring challenge periods
- ZK-Rollup — Rollup architecture using validity proofs for instant finality
- [Optimistic Rollup](/optimistic-rollup/) — Rollup architecture using fraud proofs for deferred verification
- [Modular Blockchain Design](/modular-blockchain-design/) — Settlement and execution layer separation enabling proof systems

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Consensus and cryptographic foundations
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Markets where rollup assets settle
- [Distributed Ledger](/distributed-ledger/) — State machines that validity proofs secure

</div>

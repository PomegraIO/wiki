---
title: "ZK-EVM Compatibility Types Explained"
description: "ZK-EVM compatibility types range from bytecode-equivalent to language-equivalent. Understand the engineering trade-offs in building zero-knowledge Ethereum."
keywords:
  - zk evm compatibility types
  - zero knowledge evm levels
  - bytecode compatible zk
  - language equivalent zk rollup
image: /svg/crypto.svg
---

*When a **ZK-EVM** (zero-knowledge Ethereum Virtual Machine) is built to prove Ethereum transactions, developers must choose how closely it mirrors the original EVM. This choice defines the compatibility level: from proving bytecode directly (expensive, slow) to reproof of high-level logic (fast, but requires rewriting contracts). Each level trades engineering complexity against developer convenience.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ZK-EVM Compatibility Types — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for zero-knowledge systems." />

<div class="wiki-infobox-caption">Compatibility is not binary; it exists on a spectrum of proof complexity versus ease of use.</div>

|   |   |
|---|---|
| **Level 1** | Bytecode-equivalent: proves EVM bytecode directly (hardest, slowest) |
| **Level 2** | Memory-equivalent: efficient memory and storage simulation |
| **Level 3** | Language-equivalent: reproof of Solidity or high-level semantics |
| **Trade-off** | Lower compatibility = faster proofs but more rewriting for developers |
| **Used by** | zkSync (Level 2), Polygon zkEVM (Level 2), Matter Labs experiments (Level 3) |
| **Adoption barrier** | Contracts not written in the target language may not compile or work |

</aside>

## What EVM Compatibility Means

The Ethereum Virtual Machine is a specification: it defines how opcodes behave, how memory is addressed, how gas is consumed, and how state is updated. An EVM-compatible chain (like Polygon or Avalanche) implements this specification in software so that Solidity contracts compile and run the same way.

A **ZK-EVM** does something harder: it creates a zero-knowledge proof that proves *correct execution* of EVM bytecode without revealing the internal state. Instead of a single chain validating all transactions in real time, a prover (off-chain or in a proving network) generates a cryptographic proof: "I executed this transaction against this state, and the result is this new state. The proof is a mathematical guarantee."

The catch: proving bytecode execution is expensive. A single Ethereum transaction might involve thousands of opcodes, each of which must be encoded into a constraint system and proved. The system designer must decide whether to prove at the bytecode level (easiest for existing contracts) or at a higher level (faster proofs, harder for developers).

## Level 1: Bytecode-Equivalent

A **bytecode-equivalent** ZK-EVM proves the exact behavior of the EVM instruction set. When a transaction calls `SSTORE` (store to state), the prover proves the storage write happened correctly. When a contract jumps to a label, the prover proves the `JUMPI` (conditional jump) condition was evaluated correctly.

Bytecode equivalence is the holy grail for compatibility. Any contract compiled to EVM bytecode—whether written in Solidity, Vyper, or hand-assembled opcodes—can run without modification.

But it comes at a price:

**Proof size and time:** Proving thousands of opcodes per transaction inflates the proof size and slows the prover. A complex contract might take minutes to prove, or require specialized hardware.

**Constraint complexity:** Each opcode must be encoded as a set of polynomial constraints. The Keccak-256 hash function, for instance, has been one of the biggest bottlenecks in bytecode-equivalent systems, requiring thousands of constraints per hash.

**Memory modeling:** The EVM's random-access memory model must be faithfully reproduced in arithmetic constraints, which is non-trivial.

No production ZK-EVM currently operates at pure bytecode equivalence because it is too slow. Instead, systems optimize specific opcodes or introduce limited incompatibilities.

## Level 2: Memory-Equivalent (Practical Bytecode Compatibility)

Most deployed ZK-EVM systems, such as Polygon zkEVM and zkSync Era, aim for **memory-equivalent** compatibility. The goal: prove correct execution for all *essential* opcodes while optimizing or approximating the rest.

Memory-equivalent systems typically:

- Prove Solidity's common paths (function calls, storage access, arithmetic) with native circuits
- Cache or approximate expensive operations like Keccak or elliptic-curve verification
- May diverge slightly in gas metering or memory layout

The result: nearly all existing Solidity contracts work without recompilation. A few edge cases—contracts that rely on specific gas costs, or that use very cheap operations in tight loops—may behave differently.

**Trade-off:** Proof time drops to seconds or minutes instead of hours. Proof size shrinks. But there is a small risk of incompatibility.

## Level 3: Language-Equivalent

A **language-equivalent** ZK-EVM abandons EVM bytecode entirely and instead proves the semantics of a high-level language—typically a custom variant of Solidity or a restricted subset.

Starkware's StarkNet is the prominent example. Contracts are written in Cairo (StarkNet's native language) or compiled from Solidity to Cairo. The ZK system proves Cairo execution, not EVM execution.

**Advantages:**

- Proofs are much faster because the constraint system models the language directly, not the intermediate bytecode.
- The prover can optimize for the language's specific operations.
- No need to handle all EVM edge cases.

**Disadvantages:**

- Existing Solidity contracts must be recompiled or rewritten, or a compiler bridge must exist.
- Contracts that rely on EVM-specific features (like inline assembly) often cannot be ported.
- Developers must learn new tooling and may hit incompatibilities.

Language equivalence is attractive for new systems or those willing to invest in tooling, but adoption friction is real.

## Practical Examples: The Spectrum in Action

**Polygon zkEVM** (now Polygon Labs) targets memory equivalence. Most Solidity contracts work out of the box. A few contracts using hand-rolled inline assembly or relying on specific gas costs may need tweaking.

**zkSync Era** similarly targets memory equivalence but has introduced the "zkSync EVM" virtual machine, which diverges slightly to optimize proof generation. Developers using standard Solidity rarely notice the differences.

**StarkNet** enforces language equivalence. Solidity must be compiled to Cairo (via Solc-to-Cairo or Braavos), and contract behavior may differ subtly. Developers must test thoroughly.

**Scroll**, another Layer 2, uses a more bytecode-near approach, proving more opcodes directly, at the cost of slower proof generation.

## Why Compatibility Matters for Liquidity

The choice of compatibility level affects which contracts can migrate. If a ZK-EVM is bytecode-equivalent, any contract from Ethereum can deploy with minimal friction. If it is language-equivalent, only contracts written in the supported language, or carefully recompiled contracts, will work.

This affects the ecosystem:

- **Developer experience:** Bytecode equivalence = copy-paste; language equivalence = rewrite and retest.
- **Contract migration:** Bridge protocols, liquidity aggregators, and oracles may not work if their dependencies are incompatible.
- **Interoperability:** A bytecode-equivalent system can more easily interoperate with cross-chain protocols.

For a ZK-EVM seeking adoption, bytecode or near-bytecode compatibility is a significant competitive advantage. The extra proof time is a cost the operator bears; the developer bears the cost of incompatibility.

## The Future: Hybrid Approaches

Newer designs (or future improvements to existing systems) may blend levels. For example, a system could prove most opcodes directly (memory-equivalent core) but delegate expensive operations like hashing or cryptographic verification to specialized ZK components or oracles. This hybrid reduces the overall proof burden while maintaining high compatibility.

Another direction: standardize a "ZK-EVM canonical form"—a simplified bytecode that all ZK systems support, allowing contracts to compile once and run anywhere in the ZK ecosystem.

For now, the choice of compatibility level remains a fundamental trade-off. Higher compatibility demands more proving work; lower compatibility demands more developer effort to adapt.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Publication in Blockchain Scaling](/proof-of-publication-blockchain/) — How ZK rollups commit transactions to the base layer
- [Modular Data Availability: How Celestia-Style Chains Work](/celestia-modular-data-availability/) — Data-availability chains supporting ZK rollups
- [Blockchain fundamentals](/blockchain-fundamentals/) — Smart contracts and execution models
- [Distributed ledger](/distributed-ledger/) — Foundation for blockchain systems

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — ZK rollup tokens and trading
- [Bitcoin](/bitcoin/) — Alternative blockchain design philosophy

</div>

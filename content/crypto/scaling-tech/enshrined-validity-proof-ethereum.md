---
title: "Enshrined Validity Proofs on Ethereum"
description: "Enshrined validity proofs would allow Ethereum's consensus layer to natively verify ZK proofs, enabling rollups without custom verifiers. The trade-off: increased protocol complexity and security surface."
keywords:
  - enshrined validity proof ethereum
  - ethereum ZK proofs
  - rollup verification
  - ethereum consensus layer
  - zero-knowledge proof scalability
  - ethereum protocol upgrade
---

*An enshrined validity proof on Ethereum would embed zero-knowledge proof verification directly into the protocol's consensus layer, allowing the network to natively verify ZK proofs rather than relying on smart-contract verifiers. **Enshrined validity proofs on Ethereum** promise to simplify rollup design and reduce fees, but require adding cryptographic complexity to the base layer and accepting new security trade-offs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Enshrined Validity Proofs — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Move proof verification from EVM to consensus; gains simplicity at the cost of protocol surface.</div>

|   |   |
|---|---|
| **Current approach** | Rollups verify ZK proofs via smart contracts; adds cost and limits proof system choice |
| **Enshrined proposal** | Consensus layer natively verifies proofs; any rollup can prove validity without a custom verifier |
| **Main benefit** | Reduces proof verification cost; enables lightweight rollups; decouples rollup design from EVM limits |
| **Main cost** | Increases base-layer protocol complexity; broadens consensus-layer attack surface |
| **Status** | Actively researched; no concrete Ethereum timeline; rollups shipping today use contracts |
| **Cryptography** | SNARK-friendly curves (e.g., BN254, Pasta, Grumpkin) or other zero-knowledge schemes |

</aside>

## The Current Architecture: Proofs Inside the EVM

Today's optimistic and ZK rollups verify state transitions in different ways. Optimistic rollups rely on fraud proofs: they assume transactions are valid unless someone posts a bond and challenges the result. The challenge is then adjudicated on-chain using interactive dispute resolution. This is economical because it avoids proving every transaction.

ZK rollups (also called validity rollups) take the opposite approach: every batch of transactions is accompanied by a cryptographic proof that the state transition is correct. The proof is verified on-chain, eliminating the need for a dispute window. Transactions are final as soon as the proof is verified and included in a block.

The verification happens inside a smart contract. A rollup like [StarkNet](/smart-contract/) or Polygon's ZKEVM publishes a ZK proof to Ethereum—typically a [SNARK](/proof-of-work/) using the BN254 curve or a [STARK](/proof-of-stake/)—and a verifier contract checks the proof's validity. If the proof is valid, the new state root is accepted.

This architecture has consequences. Verifying a proof on-chain consumes gas: a SNARK verification might cost 200,000–500,000 gas, which at current Ethereum fees is substantial. The verifier contract itself is custom to the specific proof system and circuit architecture the rollup uses. If you want to use a different proof system, you need a different verifier. This couples rollup design to what fits inside the EVM and creates a proliferation of verifier contracts.

## The Enshrined Proposal

The enshrined approach would move proof verification from the EVM to the consensus layer—making it a native operation like signature verification (which Ethereum already does at consensus). Instead of deploying a smart-contract verifier, the protocol would include a built-in SNARK verifier (or multiple verifiers supporting different proof systems).

In this model, a rollup would package its transactions, generate a proof off-chain using whatever circuit and prover it prefers, and submit it to Ethereum. The consensus layer—the nodes validating blocks—would natively verify the proof as part of block validation. If the proof is invalid, the block is rejected before it enters the chain. If valid, the state update is final immediately.

Benefits would include:

**Lower cost**: Removing proof verification from the EVM eliminates 200,000–500,000 gas per proof. This saves rollup users meaningful fees and makes validity rollups more competitive with optimistic rollups on cost.

**Design freedom**: Rollups are no longer constrained by what fits cheaply in the EVM. They could use more complex circuits, richer proof systems, or custom cryptography without paying prohibitive verification costs.

**Unified interface**: Rollups would verify against a standard base-layer verifier, reducing the need for custom per-rollup verifiers and simplifying Ethereum's contract layer.

**Enabling lightweight rollups**: A small-footprint rollup or sidechain could prove validity to Ethereum without maintaining a full smart-contract infrastructure.

## The Security and Complexity Trade-offs

Enshrining a capability is not free. It enlarges Ethereum's consensus-layer attack surface and increases the protocol's implementation complexity.

**Cryptographic risk**: The verifier must be correct. If there's a bug in the SNARK verification logic (e.g., accepting invalid proofs due to a cryptographic flaw), an attacker could publish a false proof and corrupt the Ethereum state. This is a more severe risk than a bug in a smart contract, which only affects users of that contract. A consensus-layer bug affects the entire chain.

The cryptography supporting ZK proofs—especially SNARKs—is younger and less battle-tested than the ECDSA signature scheme Ethereum currently uses. While SNARKs have academic foundation, production implementations are newer. Enshrining the wrong verifier or a prover supporting a weak curve could introduce a permanent vulnerability.

**Upgrade rigidity**: Once enshrined, changing the verifier logic is difficult. If a vulnerability is discovered, Ethereum would need a hard fork—a major protocol upgrade affecting every node. If the verifier is in a smart contract, updates are simpler.

**Validator burden**: Validators would need to perform proof verification as part of block validation. This adds computational work and latency. If verification is slow, it could increase block times or reduce throughput. Ethereum's roadmap includes better validator economics, but enshrining expensive operations is a risk.

**Incentive alignment**: Who pays for consensus-layer verification? Currently, rollups pay gas fees for on-chain proof verification. If verification is enshrined, the cost is distributed across all Ethereum users via increased validator resource requirements. This shifts the incentive structure.

## Proof System Selection

Ethereum would likely support SNARKs initially, and possibly STARKs or other schemes later. The choice matters.

**BN254 and other pairing-friendly curves**: These curves support pairing-based SNARK constructions that are relatively fast to verify but were originally designed for cryptographic pairings. The curves have smaller bit sizes (254 bits) than general-purpose curves, which some researchers see as adequate but others view as a long-term risk.

**STARK systems**: These use hash-based proofs and post-quantum-resistant assumptions, but produce larger proofs and slower verification. If Ethereum were to support STARKs, it would handle the additional verification work, but it would be a more substantial protocol change.

**Curve selection matters**: Different curves have different security assumptions. The cryptographic community has higher confidence in well-studied curves (e.g., secp256k1, which Ethereum currently uses for signatures), but most SNARK-friendly curves are younger. Enshrining a curve is a long-term commitment.

## Comparison to Current Alternatives

Some arguments against enshrining validity proofs:

**Optimistic rollups are sufficient**: Arbitrum and Optimism have shown that optimistic rollups with fraud proofs scale effectively. They're simpler, less cryptographically novel, and easier to upgrade. The cost difference from ZK rollups may not justify the added consensus complexity.

**Smart-contract verifiers are flexible**: If a proof system is broken or a better system emerges, a smart-contract verifier can be replaced without a hard fork. Enshrining sacrifices flexibility for cost savings.

**Hardware acceleration is improving**: Proof generation and verification are becoming faster due to hardware and algorithmic improvements. The cost differential between contract and enshrined verification may narrow, reducing the motivation.

**Other scaling layers**: [Ethereum's roadmap](/smart-contract/) includes Danksharding and other techniques that may reduce the need for rollup verification to be extremely cheap.

## Where This Stands

As of 2024–2025, there is active research and discussion about enshrined validity proofs (sometimes called "proof consensus" or "precompiled verifiers"), but no concrete proposal has been included in Ethereum's consensus upgrade roadmap. The Ethereum core developers are cautious about expanding consensus complexity without clear necessity.

Some researchers argue that the protocol should wait until proof systems are more mature and standardized. Others contend that Ethereum should embrace the change early to enable the next generation of rollups. The outcome will depend on how proof-system security confidence grows and whether the cost of contract-based verification becomes a material bottleneck.

## See also

<div class="wiki-seealso">

### Closely related

- [Zero-Knowledge Proof](/proof-of-stake/) — the cryptographic primitive underlying validity rollups
- [Smart Contract](/smart-contract/) — current venue for proof verification on Ethereum
- [Rollup](/smart-contract/) — scaling solutions that publish proofs to Ethereum
- [Consensus Mechanism](/proof-of-work/) — the layer where verification would be enshrined

### Wider context

- [Ethereum Roadmap](/smart-contract/) — Danksharding and other proposed upgrades
- [Cryptographic Assumptions](/smart-contract/) — underlying security foundations of ZK systems
- [Scalability Trilemma](/smart-contract/) — the broader context for rollup design trade-offs
- [Layer 2 Scaling](/smart-contract/) — other approaches to Ethereum throughput

</div>

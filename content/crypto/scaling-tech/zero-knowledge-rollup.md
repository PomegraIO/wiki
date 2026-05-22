---
title: "Zero Knowledge Rollup"
description: "Cryptographic proof mechanism bundling thousands of layer-2 transactions into a single verifiable proof, enabling blockchain scalability without trusted intermediaries."
keywords:
  - zero knowledge proofs
  - layer 2 scaling
  - rollups
  - zk-SNARK
---

*A **zero knowledge rollup** is a blockchain scaling solution that batches thousands of transactions off-chain, compresses them into a cryptographic proof called a zk-SNARK, and submits only that proof to the main chain—dramatically reducing on-chain data and computational burden.*

<div class="wiki-hatnote">
Distinct from optimistic rollups, which assume transactions are valid unless challenged, and from sidechain architectures, which maintain independent consensus.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Layer** | Layer 2 (off-chain computation, on-chain settlement) |
| **Transaction batch size** | 1,000–10,000+ per proof |
| **Proof type** | zk-SNARK or zk-STARK |
| **Verification cost** | O(1) operations regardless of batch size |
| **Finality** | Immediate once proof is verified on-chain |
| **Trust model** | Cryptographic; no sequencer trust |
| **Current examples** | StarkNet, zkSync, Polygon Hermez |

</aside>

## How zero knowledge proofs compress transactions

A traditional [blockchain](/wiki/blockchain-fundamentals/) records every transaction individually on-chain, consuming time and space. A zero knowledge rollup instead sends transactions to an off-chain sequencer, who bundles 2,000 of them and runs a computational circuit that proves: "I processed each transaction correctly, checked signatures, executed smart contracts, and computed the new state root." The circuit produces a compact cryptographic proof (a few kilobytes) rather than posting all 2,000 transactions (megabytes). The main chain verifies the proof in microseconds and updates the state—**[throughput](/wiki/capacity-utilization-rate/) explodes** from ~10 transactions per second to thousands.

## Difference from optimistic rollups

An [optimistic rollup](/wiki/optimistic-rollup/) assumes batches are valid by default; anyone can challenge and force re-execution if they suspect fraud. Zero knowledge rollups prove correctness upfront via cryptography—no challenge window, no re-execution. This means zero knowledge rollups achieve finality in one block rather than waiting 7 days for a fraud-proof window. The trade-off: zero knowledge proofs are computationally harder to generate (though verification is trivial), so sequencers need specialized hardware.

## Zk-SNARKs and zk-STARKs: proof systems compared

A **zk-SNARK** (zero knowledge Succinct Non-interactive Argument of Knowledge) requires a **[trusted setup](/wiki/trust-establishment/)**—a one-time ceremony where participants generate cryptographic keys. If those keys leak, someone could forge proofs. Most production systems now use **transparent zk-STARKs**, which need no trusted ceremony but generate larger proofs. [Ethereum](/wiki/ethereum/) developers are betting on transparent systems to avoid centralization risk. Both prove correctness; the choice hinges on performance and trust assumptions.

## Economics: who pays for proofs?

Generating a zero knowledge proof for 2,000 transactions costs electricity and specialized hardware—perhaps $10–$100 in compute. A traditional batch of 2,000 [Ethereum](/wiki/ethereum/) transactions would cost $1,000–$10,000 in [gas fees](/wiki/ethereum/). The rollup operator amortizes proof cost across users, cutting per-transaction cost by 100–1,000x. The on-chain footprint (the proof itself) is tiny, so gas costs for posting the proof to the main chain are minimal. Users pay a small markup; operators capture the arbitrage.

## Cross-chain atomic swaps and [state channels](/wiki/state-channel/) vs. rollups

State channels allow two parties to transact off-chain indefinitely and settle once. **[Atomic swaps](/wiki/atomic-swap/)** let parties exchange assets across chains trustlessly. Zero knowledge rollups instead focus on **[throughput](/wiki/capacity-utilization-rate/)** for many users on a single chain—not one-to-one channels or cross-chain swaps. Rollups eventually settle to a home chain; they don't replace cross-chain infrastructure but reduce the demand for it by cutting on-chain costs so sharply that [liquidity fragmentation](/wiki/liquidity-pool/) becomes less costly.

## Privacy and anonymity trade-offs

"Zero knowledge" technically means proving facts without revealing inputs. In practice, zero knowledge rollups today don't hide transaction details—they're pseudonymous, not private. A user's address and transferred amount are on-chain. Some systems (e.g., **Tornado Cash**) layer privacy atop rollups via **[mixers](/wiki/automated-market-maker/)**; others are exploring private execution layers. The cryptography is neutral; privacy depends on application design.

## Validator economics and centralization risk

A zero knowledge rollup sequencer collects transactions, builds batches, and submits proofs—a centralized gatekeeper role. If the sequencer goes offline or censors transactions, users are stuck. Many projects plan to **[decentralize](/wiki/decentralized-exchange/)** sequencing via [proof-of-stake](/wiki/proof-of-stake/) or a rotating committee. However, decentralized sequencing increases latency and proof-generation cost, narrowing the scalability gains. The trade-off between [throughput](/wiki/capacity-utilization-rate/), decentralization, and cost remains unsolved.

## Network effects and liquidity fragmentation

If rollup A has lower fees but rollup B has more [liquidity](/wiki/liquidity-pool/), users fragment. Cross-rollup **[atomic swaps](/wiki/atomic-swap/)** via [bridges](/wiki/bridge-protocols/) help but add latency and trust. Solutions like **[Polygon](/wiki/polygon/)** and **[Arbitrum](/wiki/arbitrum/)** compete on developer UX and [ecosystem](/wiki/emerging-markets-fund/) size. The winner may consolidate liquidity, or apps may multi-deploy, fragmenting again. This mirrors the [Ethereum](/wiki/ethereum/) vs. [Solana](/wiki/solana/) dynamic at the base layer.

## Regulatory and compliance implications

A zero knowledge rollup's sequencer is a centralized entity (initially) operating in some jurisdiction. Regulators may classify it as a custodian or exchange, triggering [AML](/wiki/aml-compliance/) and [KYC](/wiki/kyc/) rules. Proof generation and proof verification are mathematical; no one can censor a valid proof. But if regulators demand the sequencer block addresses or transactions, rollups face the same compliance burdens as [centralized exchanges](/wiki/centralized-exchange/).

<div class="wiki-seealso">

### Closely related
- [Blockchain Fundamentals](/wiki/blockchain-fundamentals/) — base layer concepts
- [Optimistic Rollup](/wiki/optimistic-rollup/) — competing scaling approach
- [Proof of Stake](/wiki/proof-of-stake/) — security model for decentralized sequencing
- [Atomic Swap](/wiki/atomic-swap/) — trustless cross-chain settlement
- [Automated Market Maker](/wiki/automated-market-maker/) — liquidity for rollup tokens

### Wider context
- [Ethereum](/wiki/ethereum/) — primary rollup host chain
- [Arbitrum](/wiki/arbitrum/) — major optimistic rollup
- [Polygon](/wiki/polygon/) — sidechain and rollup ecosystem
- [Bridge Protocols](/wiki/bridge-protocols/) — cross-chain communication
- [Decentralized Exchange](/wiki/decentralized-exchange/) — typical rollup application

</div>
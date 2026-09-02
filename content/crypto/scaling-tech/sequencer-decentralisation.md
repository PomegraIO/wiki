---
title: "Sequencer Decentralisation"
description: "The problem of centralised rollup sequencers creating censorship and MEV risks, and proposed solutions like threshold encryption and encrypted mempools."
keywords:
  - rollup sequencer
  - censorship resistance
  - mev mitigation
  - encrypted transactions
  - threshold cryptography
image: "/svg/crypto.svg"
---

*A **centralised sequencer** is a rollup's single ordering engine, creating a critical point of failure. If the sequencer is dishonest or controlled, it can censor transactions, extract unfair MEV, or stall the network. Sequencer decentralisation seeks to distribute ordering power among many parties, restoring trustlessness.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sequencer Decentralisation — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for rollup architecture." />

<div class="wiki-infobox-caption">Distributing ordering power to remove the centralised chokepoint.</div>

|   |   |
|---|---|
| **Problem** | Single sequencer can censor transactions and extract MEV without competition |
| **What it is** | A rollup architecture where multiple parties jointly order transactions |
| **Key candidates** | Threshold encryption, encrypted mempools, probabilistic sequencers, stake-based rotation |
| **Challenge** | Coordination overhead; decentralisation trades latency and complexity for safety |
| **Also called** | Sequencer rotation, democratic sequencing, distributed ordering |

</aside>

## The centralised sequencer problem

Rollups process transactions faster than Ethereum because they do not require full consensus. A single **sequencer** orders transactions, executes them, and posts the result onchain. This is fast and cheap but introduces a trusted party.

A malicious or negligent sequencer can:

- **Censor transactions**: refuse to include certain transactions, denying users service.
- **Extract MEV**: see pending transactions and reorder them for profit, unfairly disadvantaging users.
- **Stall**: simply stop sequencing, halting the rollup until a backup takes over.
- **Reorder**: rearrange transactions after seeing them to favour certain users or strategies.

In traditional finance, this would violate anti-discrimination rules. In crypto, it contradicts the decentralised ethos. A rollup should not ask users to trust a single entity with ordering power.

## Why centralisation was initially necessary

Early rollups (Arbitrum, Optimism) launched with centralised sequencers for speed. Decentralised ordering requires coordination overhead—consensus rounds, encryption handshakes, or threshold schemes—all of which add latency and complexity.

A centralised sequencer can order transactions in milliseconds. A decentralised sequencer needs coordination time, reducing throughput. The tradeoff favoured speed in the early days; as rollups matured and security concerns grew, attention shifted to decentralisation.

## Threshold encryption approach

One prominent decentralisation design uses **threshold encryption**. Transactions are posted encrypted to the rollup. The sequencer cannot see them until a threshold of parties cooperatively decrypts them.

Under this scheme:
1. Users encrypt their transactions with a public key.
2. Multiple sequencer candidates (or validators) hold shares of the decryption key.
3. Only when a threshold (e.g., 2-of-3) of them cooperate can transactions be decrypted and ordered.
4. No single party sees transaction contents before ordering.

This eliminates MEV extraction at the sequencer level. Even if a sequencer is dishonest, it cannot reorder your transaction without a quorum of others. It shifts MEV pressure to the decryption layer but removes the single-sequencer advantage.

The cost: sequencers must communicate to decrypt, introducing latency. A rollup that was sub-second now might be ~2–5 seconds per block.

## Encrypted mempools

**Encrypted mempools** take a simpler approach. Users post transactions to a private mempool (not public), encrypted or obfuscated. Sequencers cannot see them until after ordering.

Protocols like MEV-Burn or threshold encryption-based mempools use this pattern. The sequencer orders transactions by hash or identifier, *then* decrypts and executes them. This prevents the sequencer from front-running or reordering based on content.

The challenge is security during decryption. If decryption happens onchain, the full transaction data is revealed and can be exploited by the very sequencer nominally prevented from seeing it. If decryption happens offchain, additional trust assumptions arise.

## Stake-based sequencer rotation

Another model rotates sequencer duties among a group of staked parties. Each party gets a turn to sequence for a fixed period (e.g., one hour). If a sequencer behaves badly, it can be slashed (stake burned) or removed.

This distributes censorship risk: a single sequencer can refuse transactions for only its slot. After rotation, a new sequencer takes over. A cartel of sequencers could still censor globally, but this is harder to coordinate and easier to detect.

Rotation also permits fallback: if a sequencer goes offline, the next in rotation can pick up. Rollups like Arbitrum are exploring post-launch sequencer rotation.

## Probabilistic sequencer selection

Some designs use **probabilistic selection**: the network randomly chooses a sequencer from a pool each round. This prevents a single party from controlling ordering persistently, though a large stakeholder could rig elections.

Typically combined with slashing: if a sequencer misbehaves, it is financially penalised. The penalty must be large enough to deter attack and small enough that honest sequencers can afford to participate.

## MEV-aware designs

Decentralised sequencing does not eliminate MEV; it redistributes it. If sequencers cannot extract MEV, builders or validators might, depending on the rollup's architecture.

Some designs explicitly address this:
- **MEV-Burn**: MEV is destroyed rather than extracted, benefiting no one.
- **MEV Sharing**: MEV is distributed to users or staked sequencers.
- **Dark pools**: private execution sidechains that hide transaction contents until settlement.

Each tradeoff between fairness (no MEV extraction) and efficiency (MEV is economically necessary for incentive alignment).

## Practical constraints and latency

Decentralisation introduces overhead. Threshold encryption requires cryptographic operations and multiparty communication. Rotation adds handoff delay. Probabilistic selection requires fresh randomness each round.

A rollup aiming for sub-second confirmation times cannot easily adopt decentralised sequencing. The best-in-class decentralised designs achieve ~2–10 second latency, acceptable for most financial transactions but not high-frequency trading or gaming.

This is a key reason many rollups keep sequencers centralised early, planning decentralisation after mainnet maturity, when speed is less critical than security.

## Interaction with proof systems

Decentralised sequencing interacts with rollup proof types. An [Optimistic Rollup](/optimistic-rollup/) relies on transaction data availability for fraud proofs. A decentralised sequencer must still post all data onchain, preserving auditability.

A ZK Rollup proves correctness cryptographically; sequencer decentralisation is independent. However, ZK Rollups often use private sequencers (to hide internal state during proof generation), making decentralisation harder.

## Industry direction

Most major rollups (Arbitrum, Optimism, StarkNet) have published sequencer decentralisation roadmaps. Few have deployed production decentralised sequencers. The engineering complexity and latency tradeoffs are genuine obstacles.

The preferred near-term path is **restricted decentralisation**: a fixed set of known sequencers, rotating duties among them, with robust slashing and exit mechanisms. Full decentralisation—permissionless sequencer entry—is a longer-term goal.

## See also

<div class="wiki-seealso">

### Closely related

- Rollup — the layer 2 architecture that requires sequencers
- [Optimistic Rollup](/optimistic-rollup/) — fraud-proof based rollup dependent on data availability
- ZK Rollup — proof-based rollup with different sequencer dynamics
- MEV (Maximal Extractable Value) — the ordering power sequencers exploit
- Threshold Encryption — cryptographic primitive enabling blind ordering

### Wider context

- Layer 2 — scaling solutions managing sequencer risk
- Censorship Resistance — the principle decentralisation serves
- [Ethereum](/ethereum/) — the base layer for rollups and sequencers

</div>

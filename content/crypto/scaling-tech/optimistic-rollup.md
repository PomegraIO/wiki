---
title: "Optimistic Rollup"
description: "A layer-2 scaling solution that assumes transactions are valid unless proven otherwise through a fraud-proof mechanism."
keywords:
  - layer-2 scaling
  - rollups
  - optimistic assumption
  - fraud proofs
---

*An **optimistic rollup** is a layer-2 [blockchain](/blockchain-fundamentals/) scaling technique that processes thousands of transactions off-chain, then periodically publishes a cryptographic commitment (a "rollup") to the main chain. The system is "optimistic" because it assumes all transactions are valid unless proven fraudulent; a challenger can submit a [fraud proof](/zero-knowledge-rollup/) to overturn a fraudulent rollup before it is finalized.*

<div class="wiki-hatnote">Contrasts with [Zero-Knowledge Rollup](/zero-knowledge-rollup/), which proves validity upfront rather than relying on fraud-proof challenges.</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Settlement layer** | Ethereum mainnet (or other layer-1 blockchain) |
| **Transaction execution** | Off-chain, batched by operator/sequencer |
| **Validation mechanism** | Fraud-proof system (dispute period before finality) |
| **Finality time** | 7 days (Arbitrum, Optimism) due to dispute window |
| **Proof requirement** | Challenger must prove fraud, not operator |
| **Major examples** | Arbitrum, Optimism, Base |
| **Data availability** | Transaction data posted on-chain in compressed form |

</aside>

## The optimistic assumption: innocence until proven guilty

Optimistic rollups operate on the principle of "optimistic" validation. Instead of immediately proving that every transaction is correct (which would require complex zero-knowledge proofs), the system assumes the operator (called a "sequencer") is honest. Transactions are bundled into batches and committed to the layer-1 chain without cryptographic proof of validity.

The security comes from a **fraud-proof mechanism**. If someone believes an optimistic rollup batch is invalid, they can submit a fraud proof — a cryptographic argument showing that a specific transaction in that batch violated the rules. If the fraud proof is valid, the rollup is invalidated, the operator is penalized, and transactions are reverted. This model creates a strong incentive for honesty: a dishonest operator risks financial loss and reputational damage.

## How finality and dispute windows work

When a batch of transactions is posted to the main chain, it enters a **dispute window** (typically 7 days on [Arbitrum](/arbitrum/) and Optimism). During this period, validators can challenge the batch. If no one submits a fraud proof before the window closes, the batch is considered final and the transactions are immutable.

This finality delay is the trade-off of optimistic rollups. A zero-knowledge rollup can finalize instantly because the proof is computational; an optimistic rollup must wait for the dispute period to expire. For users withdrawing funds back to the main chain, this means a 7-day wait. [Bridging protocols](/bridge-protocols/) exist to offer faster liquidity, but they introduce counterparty risk.

## Compression and cost reduction

An optimistic rollup's main value is **cost reduction**. Instead of posting 1000 transactions individually to the main chain (each using 20,000+ gas), the operator posts a single commitment (a Merkle root or similar) that represents all 1000 transactions. On-chain, this costs ~500 gas, plus the gas to store the transaction data in a compressed form (roughly 16 bytes per transaction).

For a user, a transaction on Arbitrum costs 0.01–0.1 ETH compared to 0.5–5 ETH on Ethereum, depending on network congestion. That 10–100x reduction in cost makes optimistic rollups appealing for high-frequency traders, NFT minters, and other bandwidth-hungry applications.

## Sequencers and centralization risks

Early optimistic rollups like Arbitrum and Optimism relied on a single sequencer — a central operator who ordered transactions and submitted rollups. A single sequencer is a centralization point: if the sequencer is offline, no one can submit transactions. If the sequencer is malicious, it can censor transactions or front-run users.

Both protocols are moving toward decentralized sequencing, where multiple operators can propose batches and a [consensus mechanism](/consensus-layer-security/) selects which one to accept. Arbitrum's Sequencer Decentralization Protocol is a step in this direction, but neither protocol has fully decentralized sequencing yet.

## Fraud-proof complexity and game theory

The fraud-proof mechanism is elegant in theory but complex in practice. A challenger must identify the exact transaction that violated the rules, re-execute it on-chain (or via a fraud-proof game), and submit proof. This requires sophisticated infrastructure; most users cannot submit their own fraud proofs. In practice, a handful of professional validators monitor rollups for fraud.

The game theory is delicate. A validator must post a bond when submitting a fraud proof; if they lose, the bond is slashed. This discourages frivolous challenges but requires validators to have sufficient capital. Large protocol teams (Arbitrum Foundation, Optimism Collective) have stated they will fund validators to ensure security, but decentralized validation remains a work in progress.

## Data availability and transaction recovery

Optimistic rollups post transaction data on-chain, ensuring that anyone can reconstruct the rollup state independently. This is critical for security: even if the sequencer is offline, users can prove ownership of funds and withdraw via a "exit" transaction. If data availability were compromised, users could lose access to funds.

Ethereum's [data availability solutions](/consensus-layer-security/) (such as proto-danksharding and danksharding) are designed in part to support rollups. As Ethereum's blob space expands, rollup costs will continue to fall.

## Optimism and Arbitrum as production systems

[Arbitrum](/arbitrum/) and Optimism are the two largest optimistic rollups by total value locked. Both have matured from experimental systems to production-grade platforms hosting billions in user assets. Arbitrum has a more permissive fraud-proof system and faster virtual machine, making it attractive for developers. Optimism has closer integration with Ethereum and a simpler design, making it easier to audit.

Both have announced plans to move toward decentralized sequencing, which would further reduce centralization risk. The trade-off is higher latency: a decentralized sequencer must wait for consensus before finalizing a batch, which takes longer than a single operator.

<div class="wiki-seealso">

### Closely related

- [Zero-Knowledge Rollup](/zero-knowledge-rollup/) — alternative scaling approach using cryptographic proofs
- [Arbitrum](/arbitrum/) — major optimistic rollup deployment
- [Bridge Protocols](/bridge-protocols/) — enabling movement of assets between layers

### Wider context

- [Consensus Layer Security](/consensus-layer-security/) — how layer-2 protocols achieve security
- [Blockchain Fundamentals](/blockchain-fundamentals/) — layer-1 and layer-2 architecture
- Sequencer — the entity that orders transactions in rollups

</div>

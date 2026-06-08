---
title: "Ethereum Stateless Clients and Verkle Trees"
description: "How Verkle trees enable Ethereum stateless clients by embedding cryptographic witnesses in blocks, eliminating the need to store the full world state."
keywords:
  - ethereum stateless client
  - verkle tree
  - ethereum scaling
  - stateless validation
  - block witnesses
image: "/svg/crypto.svg"
---

*An **Ethereum stateless client** is a node that can validate blocks without storing the complete account and storage data (the "world state") on disk; **Verkle trees** enable this by compressing proofs of account state into compact witnesses embedded in each block. Together they aim to let everyday users run full nodes without terabyte-scale storage.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stateless Clients and Verkle Trees — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A step toward making Ethereum nodes lightweight and widely runnable.</div>

|   |   |
|---|---|
| **The problem** | Full nodes must store ~600+ GB of state; ordinary users run light clients instead |
| **Verkle tree** | A merkle-like tree using vector commitments to create tiny proofs of state |
| **Stateless validator** | Receives blocks with witnesses; verifies without storing history |
| **Witness size** | ~129 bytes per account touched, vs ~256 bytes in current merkle proofs |
| **Block expansion** | Witnesses add bandwidth; more data per block but faster validation |
| **Current status** | Testnet and research phase; mainnet rollout uncertain timeline |

</aside>

## The State Storage Problem

Every [Ethereum](/ethereum/) full node maintains a complete copy of all account balances, contract storage, and nonces—the "world state." This dataset grows as new accounts are created and contracts store data. Today, a full archive node requires roughly 600–800 GB or more, putting it beyond reach for most individual operators. Most users instead run light clients (which sync only headers) or rely on third-party RPC providers, reducing decentralization.

Statelessness solves this by letting a node validate new blocks without storing the full state. Instead, the block producer (or a relay service) attaches a compact proof—a "witness"—to each block that cryptographically vouches for all the state needed to execute that block's transactions. The validating node downloads the witness, checks it against the block's header, and accepts the block. No terabyte disk required.

The challenge is making the witness small enough to fit in a reasonable block size, and the proof fast enough to verify. This is where Verkle trees enter.

## Merkle Trees and Their Limits

Today's Ethereum uses **merkle trees** to commit to the world state. Each leaf represents an account, and hashes bubble up to a root hash stored in the block header. To prove that an account exists and has a certain balance, a node includes a "merkle proof"—a path of sibling hashes from leaf to root. The proof is typically 256 bits × 15 levels ≈ 30–50 bytes per account.

For a block that touches 100 accounts, the proof becomes several kilobytes. Scale this to thousands of accounts across all of Ethereum, and the witness overhead becomes substantial. Additionally, merkle proof verification requires a hash computation for each level of the tree, which is slow.

## Verkle Trees: Vector Commitments

**Verkle trees** use a different cryptographic primitive: **vector commitments**. Instead of binary branches (like a merkle tree), a Verkle tree has many children per node—often 256. A witness to an account is not a series of sibling hashes but a single small proof (roughly 48–129 bytes, depending on the scheme) that cryptographically binds the account to the root.

The key insight: rather than hashing many siblings, Verkle relies on elliptic curve cryptography to create a succinct commitment. Verifying the proof is a single [zero-knowledge](/distributed-ledger/) proof check, not multiple hash operations.

For a large tree with many accounts, Verkle witnesses stay small even as the state grows. A proof for any account in Ethereum remains roughly 128 bytes, regardless of tree depth.

## Stateless Validation in Action

Here's how stateless validation would work:

1. A block producer (validator or builder) executes transactions, tracking which accounts and storage slots are touched.
2. The producer generates a Verkle witness—a cryptographic proof—for every state element needed by that block.
3. The block is broadcast with the witness attached.
4. A stateless node (not holding the full state) receives the block and witness. It verifies the witness against the previous block's state root.
5. If the witness is valid, the node accepts the block. No state download needed.

The stateless validator never stores account data persistently. It validates in-flight and moves to the next block.

## Bandwidth and Block Size Trade-offs

Embedding witnesses in blocks increases bandwidth per block. A block touching 1,000 accounts might carry 130 KB of witnesses. This is not negligible, but it is acceptable within a 128 MB block size limit (or whatever future consensus agrees on).

The trade-off: higher bandwidth, but much lower disk storage and CPU overhead for nodes. For users who run nodes on constrained hardware (home servers, low-end cloud VMs), stateless validation is a win.

## Proof of Validity vs. Proof of History

Stateless clients shift security assumptions slightly. Instead of "I have the full state, so I can verify," it becomes "I trust the witness embedded in the block." If a malicious block producer includes a false or incomplete witness, a stateless node might accept invalid state transitions. This is mitigated by having a subset of full nodes (state-holders) who do verify against the full state and fork off if they detect fraud. The honest minority protects the network.

This is philosophically closer to how [proof-of-stake](/proof-of-stake/) already works: validators attest to block validity without executing every transaction themselves; a slashing mechanism penalizes dishonesty.

## Current Status and Timeline

Verkle trees are still in active research and testnet phases. The Ethereum Foundation and researchers have published specifications, and testing is underway. Full mainnet deployment requires:

- Completion of Verkle tree logic and proofs.
- Execution layer integration (allowing Ethereum nodes to switch to Verkle trees for state).
- A transition period where the network migrates from merkle to Verkle, or runs both in parallel.
- Confidence that the new scheme is secure and performant.

As of 2026, this remains a multi-year effort. It is not imminent, but it is a key part of Ethereum's long-term scaling roadmap, sitting alongside sharding, [rollups](/proof-of-work/), and other solutions.

## Relation to Other Scaling Solutions

Stateless clients are not a replacement for [layer-2 rollups](/active-etf/) or [sharding](/ethereum-stateless-client-verkle-tree/), which also reduce on-chain congestion. Rather, they are complementary. Rollups move transaction volume off-chain; stateless clients make on-chain validation cheaper. Together they aim to make Ethereum secure, fast, and accessible to individual operators.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Work](/proof-of-work/) — mining and block validation in earlier blockchains
- [Proof of Stake](/proof-of-stake/) — Ethereum's current consensus mechanism
- [Smart Contract](/smart-contract/) — what stateless clients must validate

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — distributed ledger technology and consensus
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — how users interact with blockchains
- [Distributed Ledger](/distributed-ledger/) — broader decentralized data structures

</div>

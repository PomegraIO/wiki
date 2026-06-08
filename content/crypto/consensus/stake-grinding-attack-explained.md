---
title: "Stake Grinding Attack Explained"
description: "How attackers in proof-of-stake systems iterate block parameters to bias future leader elections and the protocol mitigations used to prevent it."
keywords:
  - stake grinding attack proof of stake
  - proof of stake security attacks
  - validator selection bias
  - proof of stake grinding
  - consensus mechanism attacks
image: "/svg/crypto.svg"
---

*In a **stake grinding attack** on a [proof-of-stake](/proof-of-stake/) blockchain, an attacker with some amount of staked cryptocurrency manipulates block production parameters to bias the pseudorandom selection of future validators in their favor, improving their odds of producing additional blocks.*

## The Core Mechanic

Most proof-of-stake protocols use a **pseudorandom function** to select who gets to propose the next block. To avoid bias and prevent predictable target selection, the randomness source is derived from data in the blockchain itself—commonly the hash of a recent block or the aggregated randomness commitments from validators.

The stake grinding attack exploits this circular dependency: an attacker who produces a block can tweak small, malleable parameters within that block—such as transaction ordering, timestamps, or certain fields—to change the hash. By trying multiple versions of the block, the attacker searches for one whose hash, when fed into the validator selection function, selects them (or a colluding validator) as the next proposer.

Example: A protocol says "the proposer for block 101 is determined by hash(block 100) mod N, where N is the number of validators." An attacker producing block 100 tries variations—reordering transactions, adjusting a timestamp—until they find a version whose hash selects themselves at block 101. They then broadcast that version.

## Preconditions and Impact

The attack requires:

- The attacker to control at least one block (or have proposer rights)
- Block parameters to be malleable (i.e., parts of the block can be varied without invalidating it)
- The randomness source to be derivable from data the attacker can influence

The impact depends on stake held and network size. An attacker with 5% of the stake might normally have a 5% chance of proposing each block. Through grinding, they could artificially inflate this to 10% or higher, gaining extra block rewards and, more dangerously, more opportunities to censor transactions or manipulate protocol state.

In extreme cases, repeated grinding could allow a minority attacker to accumulate enough consecutive blocks to finalize a canonical fork, breaking consensus. More commonly, it subtly shifts block reward distribution and degrades fairness.

## Historical Context

**Ethereum's Proof-of-Stake (Beacon Chain)** designers were aware of grinding attacks during development. Early versions of Casper (the finality layer) and randomness designs were found to be vulnerable to variants of this attack. The protocol was hardened through several iterations, and the transition from Ethash (proof-of-work) to [proof-of-stake](/proof-of-stake/) included deliberate anti-grinding measures.

Similar concerns arise in other protocols like Polkadot and Cardano, each of which implemented specific defenses.

## Standard Mitigations

### 1. Verifiable Random Functions (VRFs)

Instead of using a simple hash of recent data, protocols employ **VRFs**—cryptographic functions that produce publicly verifiable random output and a proof of correct computation. An attacker cannot efficiently search for favorable VRF outputs because each computation is as costly as a full cryptographic operation.

Example: A validator calls a VRF with their private key and a block-based seed. The VRF produces an output and a proof. The protocol uses the output to determine leader selection. Even though the seed is on-chain, the attacker cannot find a seed that yields a favorable VRF output without owning the validator's private key.

### 2. Beacon Chain Randomness

Ethereum 2.0 uses a **separate randomness beacon** that accumulates entropy from all validators over time, rather than deriving randomness from individual blocks. Each validator submits a commitment to a random value, which is revealed later. The aggregated randomness becomes the seed for leader selection, and no single validator (or small colluding group) can influence it enough to grind effectively.

### 3. Blacklist Mutable Fields

Protocols can restrict which fields in a block are mutable and which are fixed. If transaction ordering, timestamps, and other malleable data are excluded from the randomness source, grinding becomes much harder. The attacker is left with immutable block data (like the parent hash) and cannot vary it.

### 4. Lookahead Randomness

Some protocols use randomness from many blocks ahead (e.g., block N is produced using randomness from block N+256). By the time an attacker can grind to influence randomness at block N, block N+256 may already be far in the past and irreversible. This dramatically increases the cost of grinding.

### 5. Threshold Encryption and Distributed Randomness

In protocols like Dfinity's Internet Computer, randomness is generated via threshold cryptography: multiple parties each hold a key share, and the aggregate randomness is only revealed once a threshold of participants have contributed. No single participant can manipulate randomness, preventing grinding.

## Grinding vs. Other Stake-Based Attacks

Stake grinding is distinct from but related to other attacks on proof-of-stake:

- **Nothing-at-stake**: An attacker creates an alternate fork at no cost because forking requires no computational work (mitigation: slashing penalties for voting on competing blocks).
- **Long-range attacks**: An attacker uses an old, low-security state to extend a history backward (mitigation: checkpoints and finality gadgets).
- **Grinding**: An attacker influences present randomness to bias future block selection (mitigation: VRFs and separated randomness).

All three are possible in naively designed proof-of-stake systems; mature protocols deploy multiple defenses.

## Residual Risk

Even with mitigations, some grinding risk persists if:

- A protocol uses randomness that includes proposer commitments and an attacker can refuse to reveal their commitment (forcing re-randomization in their favor)
- Validators can shift stake between shards or slots, creating timing windows to grind
- Protocol upgrades accidentally re-introduce malleable fields into randomness derivation

Protocols continue to audit randomness functions and refine anti-grinding measures as research identifies new angles.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — Consensus mechanism secured by staked capital
- [Smart Contract](/smart-contract/) — Automated code execution on blockchain
- [Distributed Ledger](/distributed-ledger/) — Shared, tamper-resistant record-keeping
- Nothing at Stake — Attacker creating competing chains costlessly
- Consensus Mechanism — Protocol for agreeing on canonical state
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Core concepts and architecture

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Trading platform for digital assets
- [Ethereum](/ethereum/) — Blockchain using proof-of-stake
- [Bitcoin](/bitcoin/) — Original blockchain using proof-of-work
- [Proof of Work](/proof-of-work/) — Consensus secured by computational work

</div>

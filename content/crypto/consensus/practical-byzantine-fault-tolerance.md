---
title: "Practical Byzantine Fault Tolerance"
description: "Castro and Liskov's 1999 state-machine replication protocol that achieves consensus finality in permissioned and proof-of-stake networks."
keywords:
  - practical byzantine fault tolerance
  - pbft
  - consensus protocol
  - state machine replication
  - byzantine consensus
image: "/svg/crypto.svg"
---

*Practical Byzantine Fault Tolerance, or PBFT, is a deterministic consensus algorithm developed by Miguel Castro and Barbara Liskov in 1999. Unlike [Nakamoto Consensus](/nakamoto-consensus/), which tolerates malicious nodes probabilistically through proof-of-work, PBFT reaches absolute finality: once a message is committed, it cannot be reversed. The protocol works in permissioned settings (known identities) and tolerates up to one-third of nodes acting maliciously. PBFT underpins many permissioned blockchains and modern [proof-of-stake](/proof-of-stake/) systems, making it foundational to distributed consensus at industrial scale.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Practical Byzantine Fault Tolerance — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">State-machine replication with finality and active Byzantine-fault tolerance.</div>

|   |   |
|---|---|
| **Authors** | Miguel Castro, Barbara Liskov (MIT) |
| **Published** | 1999 |
| **Fault tolerance** | 1/3 of nodes (malicious or faulty) |
| **Finality** | Deterministic; one-block |
| **Message complexity** | O(N²) per round (N nodes) |
| **Consensus rounds** | 3–4 message phases per block |
| **Requires** | Known participant identities; synchronous communication |
| **Applications** | Hyperledger Fabric, Cosmos, proof-of-stake blockchains |

</aside>

## The state-machine problem

PBFT solves a classic distributed-systems problem: how do N replicas of the same service (each holding a copy of state) stay synchronized when some replicas are faulty or compromised?

In a banking system, every node maintains a ledger. If Node A receives a deposit before Node B does—and Node B is controlled by an attacker—the attacker might fork the ledger, creating two histories. PBFT ensures all nodes execute the same sequence of transactions in the same order, so the ledger remains consistent even if one-third of nodes collude.

## How PBFT works: the three phases

PBFT requires three message phases to commit a block (client request → primary → replicas).

**Pre-prepare phase**: The primary (designated leader) broadcasts a message proposing a new block. All replicas receive it and enter a "pre-prepared" state, signalling agreement on the sequence number and content.

**Prepare phase**: Each replica broadcasts a "prepare" message, confirming it saw the pre-prepare. Replicas wait until they receive a quorum (2/3 + 1) of matching prepare messages. This ensures that even if the primary is faulty, an honest quorum has agreed on the block.

**Commit phase**: Once a replica has received 2/3 + 1 prepare messages, it broadcasts a "commit" message. After receiving 2/3 + 1 commits, it executes the block and writes it to its local state.

A block is **finalized** after the commit phase: it cannot be reverted, even if subsequent blocks are. This is absolute finality—a major difference from [Nakamoto Consensus](/nakamoto-consensus/), where reorg risk never fully vanishes.

## Why 2/3 quorums, not 1/2?

With 1/3 Byzantine faults (F out of N), a quorum must contain at least N − F + 1 nodes. Why? An attacker controlling F nodes can partition the network into two groups of size N − F each. If the quorum is only 50%+1, the attacker's group might form a majority and commit conflicting blocks.

A 2/3 quorum ensures that any two quorums overlap by at least one honest node, preventing forks. This is why PBFT scales linearly with fault tolerance: tolerating 1/3 malice requires 2/3 honest nodes.

## O(N²) message complexity and scalability limits

PBFT is robust but communication-intensive. In each phase, every node sends a message to every other node—O(N²) messages per round. With 100 nodes, that's 10,000 messages. With 1,000 nodes, it's 1,000,000.

This overhead limits PBFT to smaller validator sets. Hyperledger Fabric (a permissioned blockchain using PBFT-like consensus) typically operates with 10–100 validators. Ethereum 2.0 uses PBFT-inspired mechanisms but adds committees to reduce message complexity.

## PBFT vs. Nakamoto Consensus

| Aspect | PBFT | Nakamoto |
|--------|------|----------|
| Finality | Absolute; one block | Probabilistic; 6+ blocks |
| Fault tolerance | 1/3 malice | ~50% malice (expensive) |
| Message rounds | 3–4 per block | 0 (async broadcast) |
| Throughput | Higher (no PoW waste) | Lower (PoW overhead) |
| Decentralization | Permissioned (known nodes) | Permissionless (unknown nodes) |
| Security model | Cryptographic quorums | Economic incentives |

PBFT is ideal for consortium blockchains (private networks with a fixed validator set). [Nakamoto Consensus](/nakamoto-consensus/) is ideal for permissionless networks where anyone can join.

## Modern applications in proof-of-stake

Modern [proof-of-stake](/proof-of-stake/) systems (Ethereum 2.0, Polkadot, Cosmos) adopt PBFT's core ideas but modify them:

- **Economic penalties**: Instead of pure algorithm design, misbehaving validators are slashed (lose their stake). This raises the cost of attack without requiring 2/3 quorums.
- **Shorter consensus windows**: Validators are chosen randomly each round, reducing the set size and thus message complexity.
- **Hybrid approaches**: Some systems layer PBFT on top of a longest-chain rule, gaining finality after a quorum commits while maintaining fallback liveness.

## The view-change problem

One weakness of PBFT is handling primary failure. If the primary (leader) is faulty, the protocol must detect this and elect a new primary—the "view change." This adds complexity and communication overhead.

If a primary is slow or offline for 60 seconds, the network must wait, detect the failure, and restart. In [Nakamoto Consensus](/nakamoto-consensus/), miners simply build on the last valid block; no coordinator is needed. This is why PBFT systems are typically permissioned: a smaller set of known nodes allows faster failure detection and recovery.

## When PBFT is the right choice

- **Consortium blockchains**: A group of organisations (banks, trading firms) want a shared ledger without a central authority, but trust each other's identity.
- **High throughput, low latency**: PBFT commits blocks in seconds, not minutes.
- **Regulatory compliance**: Absolute finality and known validators satisfy auditability requirements.
- **Smaller networks**: 10–100 validators; O(N²) messaging is acceptable.

When permissionless consensus is required, or when scalability demands exceed 1,000 validators, [Nakamoto Consensus](/nakamoto-consensus/) or sharded proof-of-stake becomes more practical.

## See also

<div class="wiki-seealso">

### Closely related

- [Byzantine Fault Tolerance](/byzantine-fault-tolerance/) — the theoretical foundation PBFT implements.
- [Proof-of-stake](/proof-of-stake/) — modern consensus mechanism that incorporates PBFT principles with slashing.
- [Nakamoto Consensus](/nakamoto-consensus/) — permissionless, probabilistic alternative to PBFT.
- [Distributed ledger](/distributed-ledger/) — the technology PBFT secures.
- [Blockchain fundamentals](/blockchain-fundamentals/) — broader consensus landscape.

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — entities that rely on PBFT-based networks for custody finality.
- [Proof-of-work](/proof-of-work/) — alternative consensus with different tradeoff profile.
- [Hashrate](/hash-rate/) — computational cost in proof-of-work systems; absent in PBFT.
- Finality — concept central to PBFT's appeal over probabilistic consensus.
- [Bitcoin](/bitcoin/) — the original permissionless consensus system; different design philosophy from PBFT.

</div>

---
title: "Byzantine Fault Tolerance"
description: "A distributed-systems property that allows a network to reach agreement even when a fraction of participants act maliciously or fail unpredictably."
keywords:
  - byzantine fault tolerance
  - distributed consensus
  - byzantine generals problem
  - fault tolerance
  - blockchain
image: "/svg/crypto.svg"
---

*Byzantine Fault Tolerance, or BFT, is the theoretical and practical capacity of a [distributed ledger](/distributed-ledger/) or network to reach consensus despite the presence of faulty, malicious, or unpredictably behaving participants. The term originates from Leslie Lamport's 1982 Byzantine Generals Problem—a thought experiment in which separated generals must coordinate an attack despite some generals potentially being traitors or communicating unreliably. In blockchain and distributed systems, BFT defines the fraction of participants that can be tolerated as adversaries while the network still converges on a single agreed truth.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Byzantine Fault Tolerance — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The mathematical threshold at which a distributed network can tolerate misbehaviour and still function.</div>

|   |   |
|---|---|
| **Definition** | Consensus despite malicious or faulty nodes |
| **Tolerance threshold** | Generally 1/3 of participants (varies by protocol) |
| **Formal origin** | Lamport, Shostak, Pease, 1982 |
| **Application** | [Blockchain](/blockchain-fundamentals/), [distributed ledger](/distributed-ledger/) consensus |
| **Key protocols** | [PBFT](/practical-byzantine-fault-tolerance/), [proof-of-stake](/proof-of-stake/), [practical-byzantine-fault-tolerance](/practical-byzantine-fault-tolerance/) |
| **Assumes** | Asynchronous network; cryptographic authentication |

</aside>

## The generals problem

Lamport's framing remains the clearest intuition. Imagine five generals, each commanding an army, coordinating an attack by messenger. They must all agree to either attack or retreat at the same time—disagreement means disaster. But at least one general is a traitor: he sends contradictory messages, or sends no message, or claims false messages from others. The generals have no way to identify the traitor in advance.

The question is simple: *Can the loyal generals agree on a decision despite the traitor's interference?*

The mathematical answer depends on the fraction of traitors tolerated. If N generals exist and F are traitors:

- **If F ≤ N/3**, consensus is possible with cryptographic signing.
- **If F > N/3**, consensus cannot be guaranteed under asynchronous conditions (no bounds on message delay).

The 1/3 threshold is not arbitrary. With more than 1/3 traitors, a traitor-controlled quorum can break the agreement protocol by forking the message flow so that different groups of honest nodes receive inconsistent information.

## Why this matters in blockchain

In a blockchain or [distributed ledger](/distributed-ledger/), thousands or millions of participants must agree on which transactions are valid and in what order. No single authority certifies truth. Instead, the network itself must be designed so that:

1. Honest nodes reach consensus despite some nodes being offline, slow, or genuinely adversarial.
2. An attacker controlling 1/3 or fewer nodes cannot forge a false history or reverse past transactions.
3. The cost of controlling 1/3 of the network (buying hardware, [hashpower](/hash-rate/), or stake) exceeds the benefit of any attack.

[Bitcoin](/bitcoin/)'s [proof-of-work](/proof-of-work/) and later [proof-of-stake](/proof-of-stake/) systems both rely on Byzantine fault tolerance, though they achieve it through different mechanisms.

## The asynchronous catch

Lamport's work assumes a partially synchronous model: messages eventually arrive, but with unbounded delay. Under pure asynchrony (adversaries can delay messages indefinitely), the BFT bound is impossible to exceed. This is the FLP Impossibility Result: no algorithm can guarantee consensus in an asynchronous system with even one faulty process.

In practice, blockchains and real networks operate in a partially synchronous regime: messages have a reasonable delivery time, but not a hard guarantee. Protocols are designed to make honest behavior cheaper and faster than dishonest behavior, so misbehavior gets expensive even if not theoretically impossible.

## Fault types

Byzantine fault tolerance is broader than just malice. Faults include:

- **Crash faults**: A node goes offline and stops responding (easiest to handle).
- **Omission faults**: A node receives a message but fails to send it onward.
- **Arbitrary (Byzantine) faults**: A node sends any message, honest or dishonest, including signing contradictory claims.

BFT protocols tolerate the worst case: arbitrary Byzantine faults.

## Practical implications

A [practical-byzantine-fault-tolerance](/practical-byzantine-fault-tolerance/) protocol like PBFT, designed by Castro and Liskov, can run on permissioned networks where node identity is known. It tolerates up to ⌊(N−1)/3⌋ faulty nodes and reaches finality in O(N²) message rounds, meaning every transaction is irreversible once confirmed.

In contrast, [nakamoto-consensus](/nakamoto-consensus/) (Bitcoin's longest-chain rule) is simpler but probabilistic: an attacker with ≤50% hashpower cannot rewrite the past, but a longer reorganisation (a fork) remains theoretically possible with exponentially decaying probability. It tolerates more faults in practice but doesn't guarantee finality.

Most modern [proof-of-stake](/proof-of-stake/) systems (Ethereum 2.0, Polkadot) blend PBFT-like mechanisms with economic incentives (slashing), achieving Byzantine tolerance with finality guarantees while remaining permissionless.

## Why not 1/2?

A common question: if one group of nodes is loyal and another group of traitors, can't they just pick the larger group?

No. A single traitor can be perfectly honest *most of the time*, sending consistent messages, then suddenly fork and send different messages to different groups. The network then sees two competing histories and has no way to know which is true without knowing identity beforehand. With 1/3 malice, the traitor majority can't trick the honest minority into accepting their fork; with 1/2, they can.

## Tradeoffs

Byzantine fault tolerance isn't free. Protocols that tolerate high fractions of Byzantine nodes typically require:

- Higher message complexity (O(N²) rounds in PBFT).
- Larger quorums and voting overhead.
- Lower throughput compared to crash-fault-tolerant systems.
- Cryptographic operations (signatures, cryptographic proofs) on every message.

A system tolerating 1/3 Byzantine faults is very robust but slower than a system that only tolerates 50% crash faults.

## See also

<div class="wiki-seealso">

### Closely related

- [Practical Byzantine Fault Tolerance](/practical-byzantine-fault-tolerance/) — the 1999 protocol by Castro and Liskov; the standard algorithm for permissioned BFT.
- [Nakamoto Consensus](/nakamoto-consensus/) — Bitcoin's probabilistic fault-tolerant consensus using proof-of-work.
- [Proof-of-stake](/proof-of-stake/) — modern consensus mechanism that combines BFT ideas with economic incentives.
- [Distributed ledger](/distributed-ledger/) — the technology that relies on BFT to function without a central authority.
- [Blockchain fundamentals](/blockchain-fundamentals/) — the broader ecosystem in which BFT is a foundational component.

### Wider context

- [Proof-of-work](/proof-of-work/) — alternative consensus mechanism with different fault-tolerance properties.
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — exchanges trust BFT-based systems to custody and transfer value.
- [Hash rate](/hash-rate/) — in proof-of-work, the cost of controlling 1/3 of the network.
- [Bitcoin](/bitcoin/) — the first practical application of probabilistic Byzantine consensus.
- [Ethereum](/ethereum/) — uses BFT-like proof-of-stake for consensus finality.

</div>

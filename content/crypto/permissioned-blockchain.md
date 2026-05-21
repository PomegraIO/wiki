---
title: "Permissioned Blockchain"
description: "A permissioned blockchain restricts who can participate in the network. Only approved nodes can validate transactions and join, contrasting with permissionless blockchains where anyone can participate."
keywords:
  - permissioned
  - private blockchain
  - access control
  - enterprise blockchain
  - validator
image: "https://picsum.photos/seed/permissioned-blockchain/900/600"
---

*A **permissioned blockchain** is a [distributed ledger](/distributed-ledger) where participation is restricted — only approved nodes can validate transactions, submit data, or access the network. Access is controlled through identity management and authentication. Permissioned blockchains are typically used in enterprise and institutional settings.*

<div class="wiki-hatnote">

This entry covers permissioned blockchains as a concept. For permissionless blockchains, see [public blockchain](/public-blockchain); for private blockchains generally, see [private blockchain](/private-blockchain).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Permissioned Blockchain — characteristics</div>

<img src="https://picsum.photos/seed/permissioned-blockchain/900/600" alt="Permissioned network with approved participants" />

<div class="wiki-infobox-caption">A permissioned blockchain: access by approval only.</div>

|   |   |
|---|---|
| **Who can join** | Approved entities only |
| **Who can validate** | Approved validators |
| **Access control** | Identity-based authentication |
| **Governance** | Controlled by operators or consortium |
| **Speed** | Typically faster than permissionless |
| **Immutability** | Lower than permissionless blockchains |
| **Privacy** | Often enhanced (transaction privacy) |
| **Use case** | Enterprise, inter-organisational systems |

</aside>

## Access control mechanisms

Permissioned blockchains use identity management to control who participates. Each potential validator is vetted and issued cryptographic credentials. When a node attempts to join the network, it must authenticate using these credentials.

This contrasts with permissionless blockchains like [Bitcoin](/bitcoin), where any computer can download the software and start validating. A permissioned blockchain's operators can revoke a node's access at any time.

## Validator selection

In a permissionless blockchain, validators are selected through competition ([proof-of-work](/proof-of-work)) or randomisation ([proof-of-stake](/proof-of-stake)). In a permissioned blockchain, validators are typically selected by the operators or through a formal process (e.g., a voting mechanism among consortium members).

This means fewer validators validate the network. A permissioned blockchain might have 10–100 validators; a permissionless blockchain like [Ethereum](/ethereum) has thousands. Fewer validators means faster consensus but greater centralisation.

## Consensus mechanisms in permissioned systems

Permissioned blockchains often use consensus mechanisms optimised for speed rather than decentralisation:

- **Practical Byzantine Fault Tolerance (PBFT)** — tolerates Byzantine faults (nodes acting maliciously) and reaches consensus through voting.
- **Raft** — a simpler consensus for systems where Byzantine faults are not a concern (because validators are trusted).
- **Voting-based mechanisms** — validators simply vote on the state, and majority wins.

These are faster than [proof-of-work](/proof-of-work) but require strong assumptions about validator honesty and synchronisation.

## Transaction visibility and privacy

Permissioned blockchains often provide fine-grained privacy controls. In a supply-chain network, one transaction might involve only suppliers A and B; suppliers C and D should not see it. Smart privacy mechanisms allow this while still preventing double-spending.

This is harder on [public blockchains](/public-blockchain), where all transactions are broadcast to all nodes.

## Immutability and reversibility

Permissioned blockchains often have weaker immutability than permissionless ones. The operators can theoretically reverse transactions or change history, because they control the validator set.

In some enterprise use cases, this is a feature — if a transaction is made in error, the operators can correct it. In other cases, it is a weakness — if you do not trust the operators, a permissioned blockchain does not provide strong guarantees.

## Governance

Governance of permissioned blockchains is usually hierarchical, not democratic. The operators (or a consortium of operators) decide on protocol upgrades, rule changes, and network parameters.

This is faster than democratic governance on [public blockchains](/public-blockchain) but requires trusting the operators.

## Examples and platforms

**Hyperledger Fabric** — an open-source permissioned blockchain framework. Fabric is modular: participants can plug in different consensus algorithms and privacy mechanisms.

**R3 Corda** — designed for financial institutions. Each Corda network is a separate universe; interoperability between networks is limited.

**Quorum** — a permissioned variant of [Ethereum](/ethereum). It retains EVM compatibility but adds access controls and privacy mechanisms.

**Hedera** — a permissioned network with asynchronous Byzantine Fault Tolerance (aBFT) consensus.

## Use cases

Permissioned blockchains excel in:

- **Supply-chain tracking.** A coalition of companies recording the provenance of goods. All participants are vetted; speed and privacy matter.
- **Inter-bank settlement.** Banks settling with each other, with each bank as an approved validator.
- **Digital assets.** Institutions issuing and trading digital representations of assets (securities, commodities).
- **Voting systems.** An organisation running an election with approved voters.

## Criticisms

Critics argue that if you trust a consortium of validators, you do not need a blockchain — a traditional database is faster and simpler. Blockchains are useful because they allow strangers to transact without trusting a central authority; if you already trust the operators, the blockchain adds complexity without benefit.

Proponents counter that blockchains provide transparency and auditability even in trusted environments, and can prevent collusion among validators.

## Permissioned versus permissionless trade-offs

Permissioned blockchains trade decentralisation and censorship resistance for control, efficiency, and privacy. Neither is universally superior; the choice depends on whether the use case values decentralisation or operational efficiency.

## See also

<div class="wiki-seealso">

### Closely related

- [Public blockchain](/public-blockchain) — permissionless and decentralised
- [Private blockchain](/private-blockchain) — restricted participation
- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Validator](/validator) — who validates permissioned blockchains

### Wider context

- [Proof-of-work](/proof-of-work) — consensus for permissionless blockchains
- [Proof-of-stake](/proof-of-stake) — alternative consensus mechanism
- [Distributed ledger](/distributed-ledger) — the general concept

</div>

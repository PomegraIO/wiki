---
title: "Private Blockchain"
description: "A private blockchain is a restricted network where participation and validation are controlled by approved entities. Transactions may or may not be visible to the public, and governance is centralised."
keywords:
  - private blockchain
  - permissioned
  - consortium blockchain
  - enterprise
  - hyperledger
image: "https://picsum.photos/seed/private-blockchain/900/600"
---

*A **private blockchain** is a [distributed ledger](/distributed-ledger) where participation and validation are restricted to approved entities. Access, transaction visibility, and governance are controlled by the operators. Private blockchains are often called "permissioned" blockchains and are used in enterprise settings.*

<div class="wiki-hatnote">

This entry covers private blockchains as a category. For public blockchains, see [public blockchain](/public-blockchain); for permissioned blockchains generally, see [permissioned blockchain](/permissioned-blockchain).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Private Blockchain — characteristics</div>

<img src="https://picsum.photos/seed/private-blockchain/900/600" alt="Private blockchain with restricted nodes" />

<div class="wiki-infobox-caption">A private blockchain: controlled access, centralised governance.</div>

|   |   |
|---|---|
| **Who can participate** | Approved entities only |
| **Who can see transactions** | Approved participants (or public, varies) |
| **Who controls the network** | Network operators |
| **Immutability** | Weaker than public blockchains |
| **Key advantage** | Efficiency, control, compliance |
| **Key disadvantage** | Requires trust in operators; less decentralised |
| **Examples** | Hyperledger Fabric, Corda, private Ethereum |

</aside>

## Permissioned access and governance

A private blockchain requires permission to participate. Only approved organisations can run validators, submit transactions, or view certain data. An operator or consortium of operators maintains a whitelist of participants and can revoke access.

This stands in stark contrast to [public blockchains](/public-blockchain) like [Bitcoin](/bitcoin), where anyone can participate. The trade-off is that private blockchains sacrifice decentralisation in exchange for control and efficiency.

## Use cases and deployment

Private blockchains are deployed in enterprise and institutional settings where:

- **Control is necessary.** Banks want to enforce KYC (know-your-customer) rules and block certain participants.
- **Performance matters.** Speed is more important than censorship resistance.
- **Confidentiality is required.** Transaction details should not be visible to the public.
- **Liability is clear.** One organisation owns the system and is responsible for its operation.

Common use cases include:

- **Inter-bank settlement.** Banks using a shared ledger to settle transactions between each other.
- **Supply-chain tracking.** A coalition of companies recording the movement of goods.
- **Voting systems.** An organisation running an election on a private ledger.

## Popular private blockchain platforms

**Hyperledger Fabric** — an open-source project backed by the Linux Foundation. Fabric is designed for modularity; participants can choose different consensus mechanisms and privacy models.

**R3 Corda** — designed for financial institutions. Corda transactions are visible only to counterparties, not broadcast to all validators.

**Private Ethereum** — some organisations run private instances of [Ethereum](/ethereum) with restricted validators and visibility.

## Transaction visibility

Private blockchains vary in visibility:

- **Fully private.** Transactions are visible only to participants; the public cannot see them.
- **Semi-private.** Transactions are recorded but encrypted; only parties with keys can read them.
- **Public ledger, private access.** The ledger is publicly visible, but only approved entities can add transactions.

The choice depends on the use case. A supply-chain ledger might be fully private (competitors should not see details). A voting ledger might be public (transparent governance) but have private access (only approved voters can vote).

## Governance and immutability

Private blockchains have weaker immutability guarantees than public blockchains. Because the operators control the network, they can theoretically reverse transactions, change the rules, or rewrite history.

This is sometimes a feature. If a transaction is recorded in error, the operators can correct it. But it also means participants must trust the operators not to abuse their power.

Governance is often hierarchical rather than decentralised. An operator or consortium makes decisions about rule changes, rather than a global community voting.

## Comparison with public blockchains

| Aspect | Public | Private |
|--------|--------|---------|
| **Access** | Permissionless | Permissioned |
| **Validators** | Many, decentralised | Few, controlled |
| **Speed** | Slower | Faster |
| **Immutability** | Stronger | Weaker |
| **Privacy** | Pseudonymous | Controllable |
| **Censorship resistance** | High | Low |
| **Regulatory compliance** | Difficult | Easier |

Public blockchains prioritise decentralisation and censorship resistance. Private blockchains prioritise control and efficiency.

## Criticism and controversy

Critics argue that private blockchains are not truly "blockchain" — they are just databases with extra steps. If you trust the operators, you do not need a blockchain; a traditional database is faster and simpler.

If you do not trust the operators, a private blockchain does not help, because the operators can still cheat (by reversing transactions or lying about state).

Proponents counter that private blockchains are useful for organisations that want the benefits of immutability and multi-party verification without sacrificing control.

## Hybrid approaches

Some organisations use **hybrid blockchains** — a private network with periodic checkpoints to a public blockchain (like [Ethereum](/ethereum)). This provides the efficiency and control of a private network with the immutability guarantees of a public blockchain.

## See also

<div class="wiki-seealso">

### Closely related

- [Public blockchain](/public-blockchain) — open and permissionless
- [Permissioned blockchain](/permissioned-blockchain) — restricted participation
- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Distributed ledger](/distributed-ledger) — private blockchains are distributed ledgers

### Wider context

- [Proof-of-work](/proof-of-work) — consensus mechanism
- [Proof-of-stake](/proof-of-stake) — alternative consensus mechanism
- [Ethereum](/ethereum) — can be deployed privately or publicly

</div>

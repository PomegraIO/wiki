---
title: "Proof-of-Authority"
description: "Proof-of-authority is a consensus mechanism where a set of approved validators validate transactions. Validators stake their reputation rather than cryptocurrency. It is used in permissioned blockchains and testnets."
keywords:
  - proof-of-authority
  - poa
  - validator
  - reputation
  - consensus
  - permissioned
image: "/svg/crypto.svg"
---

*A **proof-of-authority** (**PoA**) is a consensus mechanism where a set of known, approved validators validate transactions based on their reputation rather than cryptocurrency stake. PoA is highly efficient but requires trusting the validators. It is commonly used in [permissioned blockchains](/permissioned-blockchain/), testnets, and private networks.*

<div class="wiki-hatnote">

This entry covers proof-of-authority as a mechanism. For proof-of-stake, see [proof-of-stake](/proof-of-stake/); for proof-of-work, see [proof-of-work](/proof-of-work/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proof-of-Authority — key characteristics</div>

<img src="/svg/crypto.svg" alt="Approved validators validating blocks" />

<div class="wiki-infobox-caption">Proof-of-authority: trust through reputation.</div>

|   |   |
|---|---|
| **How it works** | Approved validators take turns proposing blocks |
| **Who validates** | A set of known, approved entities |
| **Security basis** | Reputation (not economic stake) |
| **Decentralisation** | Low (small validator set) |
| **Energy cost** | Negligible |
| **Speed** | Very fast |
| **Immutability** | Weak (validators can rewrite history) |
| **Used in** | Testnets, permissioned networks, private blockchains |

</aside>

## How proof-of-authority works

In proof-of-authority, a fixed set of validators are identified (e.g., "Alice, Bob, and Carol will validate our blockchain"). Validators take turns proposing blocks in a rotation (Alice proposes block 1, Bob proposes block 2, Carol proposes block 3, repeat).

Other nodes simply verify that the block was proposed by an approved validator and that the transactions are valid. If a node detects an invalid block from a validator, it rejects it.

## Reputation instead of cryptoeconomics

Unlike [proof-of-stake](/proof-of-stake/) where validators lose cryptocurrency for misbehaviour, in PoA validators risk their **reputation**. If a validator proposes an invalid block or attacks the network, they can be revoked and expelled from the validator set.

This works if validators are known entities with real-world reputation to protect. An exchange, bank, or government agency would not risk their reputation for the minor gains from attacking a blockchain.

For anonymous validators or entities with no reputation to lose, PoA provides no security.

## Use cases

**Testnets.** Ethereum's testnet (Rinkeby, Goerli) uses PoA to provide a free, fast environment for testing before deploying to mainnet.

**Permissioned blockchains.** A consortium of banks might use PoA, where each bank is a validator with known identity.

**Private blockchains.** A company's internal ledger might use PoA, with the company itself as validators.

**Alternative chains.** Some networks (e.g., Polygon PoS sidechain for certain periods) use hybrid models involving PoA.

## Advantages

**Speed.** Block time is deterministic and fast (seconds), since there is no competition or consensus delay.

**Energy.** PoA requires no mining or staking — validators simply take turns.

**Simplicity.** No complex cryptoeconomics; the system is easy to understand and audit.

**Fairness.** In a round-robin rotation, each validator has equal opportunity to propose blocks.

## Disadvantages

**Centralisation.** A small number of validators control the network.

**Weak immutability.** If validators collude (or are compromised), they can rewrite history.

**No decentralisation.** The network depends on trusting specific entities, defeating the original purpose of cryptocurrencies (removing trusted intermediaries).

**Lack of incentives.** Validators earn no direct reward (often), so they must be incentivised through other means (governance participation, prestige).

## Comparison with other consensus mechanisms

| Mechanism | Decentralisation | Speed | Energy | Immutability |
|-----------|---|---|---|---|
| **Proof-of-work** | High | Slow | High | Strong |
| **Proof-of-stake** | High | Fast | Low | Strong |
| **Delegated PoS** | Moderate | Fast | Low | Strong |
| **Proof-of-authority** | Low | Very fast | None | Weak |

PoA sacrifices decentralisation and immutability for speed and efficiency. It is useful only when decentralisation is not a priority.

## Real-world examples

**Ethereum Rinkeby testnet** — used PoA to provide a free, fast testing environment. (Goerli replaced Rinkeby in 2023.)

**Kovan testnet** — another Ethereum testnet using PoA.

**VeChain** — a blockchain focused on supply-chain tracking, uses PoA with a set of approved validator nodes.

Some networks describe themselves as using PoA but actually use variants with economic incentives; calling something "PoA" is not strictly standardised.

## Criticism and controversy

Critics argue that PoA is not truly "blockchain" — if you must trust specific validators, you could use a traditional database. The appeal of blockchains is supposedly to eliminate trusted intermediaries.

Proponents counter that PoA is appropriate for specific contexts (testnets, permissioned consortia) where decentralisation is not needed.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake/) — decentralised consensus
- [Proof-of-work](/proof-of-work/) — alternative consensus mechanism
- [Validator](/validator/) — who validates in PoA
- [Permissioned blockchain](/permissioned-blockchain/) — uses PoA often

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Consensus mechanism](/proof-of-work/) — how agreement is reached
- [Private blockchain](/private-blockchain/) — PoA is used in private chains

</div>

---
title: "Polkadot"
description: "Polkadot is a multi-chain blockchain network that connects parallel chains (parachains) through a shared security model. It enables interoperability between different blockchains and uses proof-of-stake consensus."
keywords:
  - polkadot
  - dot
  - blockchain
  - parachain
  - interoperability
  - relay chain
image: "/svg/crypto.svg"
---

*A **Polkadot** (**DOT**) is a multi-chain blockchain platform designed to enable interoperability between different blockchains. It connects specialised "parachains" to a central "relay chain," allowing tokens and data to move between chains while sharing security provided by validators on the relay chain.*

<div class="wiki-hatnote">

This entry covers the Polkadot network architecture. For its native token, see the DOT token page; for competing interoperability platforms, see Cosmos or [Avalanche](/avalanche/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Polkadot — key facts</div>

<img src="/svg/crypto.svg" alt="Polkadot relay chain and parachain architecture" />

<div class="wiki-infobox-caption">Polkadot: a heterogeneous multi-chain network with shared security.</div>

|   |   |
|---|---|
| **What it is** | A multi-chain blockchain network |
| **Native currency** | Dot (DOT) |
| **Created** | 2020 |
| **Founder** | Gavin Wood (Ethereum co-founder) |
| **Consensus mechanism** | [Proof-of-stake](/proof-of-stake/) (Nominated Proof-of-Stake) |
| **Core component** | Relay chain + parachains |
| **Max parachains** | ~100 (currently) |
| **Interoperability** | Cross-chain messaging protocol |

</aside>

## Vision and architecture

Gavin Wood, co-founder of [Ethereum](/ethereum/), created Polkadot to solve the "scalability trilemma" — the tension between decentralisation, scalability, and security. While other platforms chose different trade-offs, Polkadot proposed a novel solution: heterogeneous multi-chain architecture.

The network consists of a **relay chain** (the core) connected to numerous **parachains** (specialised side-chains). Each parachain can have different rules, different consensus mechanisms, even different purposes. They share security from the relay chain's validators but maintain independence otherwise.

## The relay chain

The relay chain is Polkadot's beating heart. It uses [proof-of-stake](/proof-of-stake/) consensus (called Nominated Proof-of-Stake) to select [validators](/validator/). These validators secure not only the relay chain but also all connected parachains.

This "shared security" model is a crucial innovation. A new parachain does not need its own set of miners or validators; it immediately inherits security from Polkadot's global validator set. This makes launching a parachain much cheaper and faster than launching an independent blockchain.

## Parachains and heterogeneity

Unlike [Ethereum](/ethereum/), where all smart contracts run on a homogeneous virtual machine, Polkadot parachains can be designed differently. One parachain might optimise for financial transactions; another for gaming; another for supply-chain tracking. They can even have different security models or native currencies.

This heterogeneity gives developers flexibility but also complexity. Each parachain must still conform to Polkadot's interface and consensus.

## Becoming a parachain: auctions and slots

Parachain slots on Polkadot are limited (originally 100, later expanded). Projects compete in "parachain auctions" to secure a slot, typically by paying a deposit in DOT and gathering community support. Winners lease the slot for a fixed period (typically two years), after which they must re-auction.

This mechanism aims to allocate scarce relay-chain capacity to the most valued projects while preventing permanent centralisation of slots. However, it creates financial barriers and has favoured well-funded teams.

## Cross-chain interoperability

Polkadot implements a **cross-consensus message passing** (XCM) protocol that allows parachains to send messages to each other and to the relay chain. This enables token swaps, asset transfers, and more complex interactions between chains.

XCM is not a general-purpose solution; the receiver chain must know how to handle each message type. But it provides a foundation for multi-chain applications, where logic is spread across parachains.

## Governance and the Kusama testnet

Polkadot has a sophisticated on-chain governance model where DOT holders vote on protocol upgrades. This includes an optional peer review period and a security council that can prevent catastrophic upgrades.

Kusama is Polkadot's "canary network" — a fully functional blockchain using identical code but lower security and faster governance, allowing new features to be tested before deploying to Polkadot.

## Market position and adoption

Polkadot has consistently ranked in the top ten cryptocurrencies by [market capitalisation](/market-capitalization/). However, practical adoption of parachains has been slower than anticipated. Many teams that won slots have since abandoned or pivoted their projects.

DeFi and NFT activity on Polkadot lags [Ethereum](/ethereum/), and existing DeFi protocols often run on Ethereum and Polkadot in parallel, rather than choosing Polkadot exclusively.

## Challenges and criticisms

Critics point out that Polkadot's promise of "scalability through multi-chain architecture" does not inherently solve throughput problems — a parachain can only process as much as its own bandwidth allows, and the relay chain remains a bottleneck for cross-chain messages.

Others argue that heterogeneity increases complexity without sufficient benefit; developers prefer the simplicity of deploying to a single, well-established chain (Ethereum) over managing multiple parachains.

The initial distribution of DOT tokens was heavily concentrated among insiders, and the high cost of participating in governance (voting requires locked DOT) limits participation to wealthier holders.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake/) — Polkadot's consensus mechanism
- [Validator](/validator/) — who secures Polkadot parachains
- [Staking](/staking/) — earning rewards on Polkadot
- Smart contract — programs deployed on parachains
- Cross-chain bridge — related but separate interoperability method

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Distributed ledger](/distributed-ledger/) — Polkadot's network architecture
- [Ethereum](/ethereum/) — a competing platform with different trade-offs
- [Avalanche](/avalanche/) — another network supporting multiple chains
- Layer-2 — Ethereum's scaling approach, conceptually different from Polkadot's

</div>

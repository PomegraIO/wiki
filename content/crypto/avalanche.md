---
title: "Avalanche"
description: "Avalanche is a blockchain platform offering fast transaction finality through its DAG-based consensus mechanism. It uses proof-of-stake and supports subnets, allowing custom blockchains sharing its security model."
keywords:
  - avalanche
  - avax
  - blockchain
  - proof-of-stake
  - consensus
  - subnet
image: "/svg/crypto.svg"
---

*An **Avalanche** (**AVAX**) is a blockchain platform and cryptocurrency designed to deliver fast transaction finality and high throughput using a novel consensus protocol. It uses [proof-of-stake](/proof-of-stake) and supports "subnets" — custom blockchains that inherit security from Avalanche's main network.*

<div class="wiki-hatnote">

This entry covers the Avalanche network and platform. For similar platforms, see [Polkadot](/polkadot), [Solana](/solana), or [Ethereum](/ethereum); for the consensus mechanism, see [proof-of-stake](/proof-of-stake).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Avalanche — key facts</div>

<img src="/svg/crypto.svg" alt="Avalanche logo and consensus diagram" />

<div class="wiki-infobox-caption">Avalanche: a platform emphasising speed and finality.</div>

|   |   |
|---|---|
| **What it is** | A blockchain platform |
| **Native currency** | Avax (AVAX) |
| **Created** | 2020 |
| **Founder** | Emin Gün Sirer |
| **Consensus mechanism** | [Proof-of-stake](/proof-of-stake) (Avalanche consensus) |
| **Block time** | ~1 second |
| **Finality** | Near-instant |
| **Active validators** | ~7,000+ (as of 2024) |
| **Subnets** | Custom blockchains available |

</aside>

## Origins and consensus innovation

Emin Gün Sirer created Avalanche to address a fundamental problem: traditional [proof-of-stake](/proof-of-stake) consensus requires nodes to reach agreement through synchronous communication, which is slow. Avalanche's approach is asynchronous — nodes periodically query a random sample of peers about the state of transactions.

This gossip-based protocol is inspired by epidemiological models of disease spread. A transaction is secure once a sufficient majority of validators have heard about it (and agreed it is valid), even if not all nodes communicate in lock-step.

## The consensus mechanism

Avalanche's consensus works through **avalanche sampling**. When a node needs to determine if a transaction is valid, it samples a random subset of validators and asks for their opinion. If a super-majority agree, the node accepts the transaction. Crucially, once a node has accepted a transaction, it continues voting for it in future samples, creating a snowball effect.

This approach provides near-instant finality — transactions are final within seconds, far faster than [Ethereum](/ethereum) (which requires ~15 minutes for confidence) or [Bitcoin](/bitcoin) (which requires ~1 hour).

## Three chains on one network

Avalanche's network comprises three blockchains:

1. **The Exchange Chain (X-Chain)** — for asset issuance and trading.
2. **The Platform Chain (P-Chain)** — for [validator](/validator) registration and subnet coordination.
3. **The Contract Chain (C-Chain)** — for smart contracts (EVM-compatible).

All three share Avalanche's validator set and consensus, creating a unified security model while allowing different chains to optimise for different purposes.

## Subnets and customisation

Avalanche's innovation beyond consensus is **subnets** — custom blockchains that can be created by anyone. A subnet inherits security from Avalanche's main network (as long as the subnet's validators are a subset of Avalanche validators), but can have different rules, token economics, or even programming languages.

This allows enterprise blockchains, gaming-specific chains, or other specialised use cases to launch quickly without building an independent validator set. However, many subnets have struggled to attract significant activity.

## Ethereum compatibility

The C-Chain is compatible with the [Ethereum](/ethereum) Virtual Machine (EVM), meaning developers can port Ethereum smart contracts to Avalanche with minimal changes. This lower barrier has attracted some projects but has also meant Avalanche primarily competes for scraps of Ethereum's ecosystem rather than establishing an independent identity.

## DeFi ecosystem

Avalanche has a active DeFi ecosystem with protocols like Aave, Curve, and Trader Joe, but trading volumes and total value locked remain far below [Ethereum](/ethereum). Avalanche's advantage — lower fees — is also enjoyed by [Polygon](/polygon) and [Arbitrum](/arbitrum), so differentiation is limited.

## Market position

Avalanche has consistently ranked in the top 10 cryptocurrencies by [market capitalisation](/market-capitalization). However, adoption has lagged expectations set at launch, when founders optimistically discussed displacing [Ethereum](/ethereum) as the dominant smart-contract platform.

## Criticisms and limitations

Avalanche's fast finality comes with the cost of higher validator hardware requirements, which could limit decentralisation over time. The three-chain architecture, while innovative, has sometimes confused developers and users about which chain to use for different purposes.

Additionally, the consensus mechanism, while elegant in theory, has seen fewer academic audits than [Ethereum](/ethereum)'s or [Bitcoin](/bitcoin)'s algorithms, raising questions about edge-case robustness under extreme network conditions.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake) — Avalanche's consensus mechanism
- [Validator](/validator) — who secures Avalanche
- [Staking](/staking) — how to earn rewards on Avalanche
- Smart contract — programs on Avalanche's C-Chain

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Distributed ledger](/distributed-ledger) — Avalanche's network architecture
- [Ethereum](/ethereum) — a competing platform
- [Polkadot](/polkadot) — another multi-chain approach
- Layer-2 — Ethereum's scaling solution
- [Cryptocurrency exchange](/cryptocurrency-exchange) — where AVAX trades

</div>

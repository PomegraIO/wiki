---
title: "Optimism"
description: "Optimism is an Ethereum layer-2 rollup using optimistic rollup technology. It bundles transactions and posts them to Ethereum in compressed form, reducing costs and increasing throughput while inheriting Ethereum's security."
keywords:
  - optimism
  - op
  - layer-2
  - ethereum
  - rollup
  - scaling
image: "https://picsum.photos/seed/optimism/900/600"
---

*An **Optimism** (**OP**) is an Ethereum layer-2 scaling solution built on optimistic rollup technology. It compresses transactions and posts them to [Ethereum](/ethereum), reducing costs by 10–100x while maintaining [Ethereum](/ethereum)'s security guarantees. It is EVM-compatible and designed to be a drop-in replacement for [Ethereum](/ethereum).*

<div class="wiki-hatnote">

This entry covers the Optimism network. For Ethereum's base layer, see [Ethereum](/ethereum); for competing layer-2 solutions, see [Arbitrum](/arbitrum) or [Polygon](/polygon); for the underlying rollup technology, see optimistic rollup.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Optimism — key facts</div>

<img src="https://picsum.photos/seed/optimism/900/600" alt="Optimism rollup architecture" />

<div class="wiki-infobox-caption">Optimism: an Ethereum layer-2 scaling the network through compression.</div>

|   |   |
|---|---|
| **What it is** | An Ethereum layer-2 rollup |
| **Governance token** | OP |
| **Created** | December 2021 |
| **Developer** | Optimism Collective |
| **Technology** | Optimistic rollup |
| **EVM compatibility** | Full (Ethereum Virtual Machine) |
| **Transaction cost** | Fractions of a cent |
| **Block time** | ~2 seconds |
| **Security** | Inherits Ethereum's consensus |

</aside>

## Origins and technology

Optimism was developed as an optimistic rollup scaling solution for [Ethereum](/ethereum). Like [Arbitrum](/arbitrum), it compresses transactions and posts proofs to [Ethereum](/ethereum), but with a slightly different technical implementation.

The core mechanism is identical: a sequencer collects transactions, bundles them, and posts the compressed data and state root to [Ethereum](/ethereum). Transactions are assumed valid unless a fraud proof challenges them. If challenged, the transaction is re-executed on [Ethereum](/ethereum), and the honest party's version becomes truth.

## EVM equivalence

Optimism's key design goal is **EVM equivalence** — not just compatibility, but exact equivalence. The bytecode, memory layout, and execution of [Ethereum](/ethereum) smart contracts should be identical on Optimism. This means developers face zero porting friction.

This design choice contrasted with some competing solutions that offered EVM compatibility but not equivalence, forcing developers to use transpilers or accept subtle differences.

## The OP token and governance

In April 2023, Optimism launched its governance token (OP). Token holders vote on protocol upgrades and treasury allocation. The distribution included airdrops to early users and developers, helping decentralise governance.

Optimism Collective, the governance structure, is designed to include not only token holders but also "citizens" who contribute to the ecosystem, attempting to broaden participation beyond token wealth.

## Data availability and future upgrades

Optimism posts transaction data to [Ethereum](/ethereum) as calldata, making transactions verifiable on-chain. This is secure but expensive. Optimism has explored **EIP-4844 blobs**, a proposed [Ethereum](/ethereum) upgrade that provides cheaper data availability, potentially reducing Optimism fees further.

Future versions of Optimism (sometimes called "Bedrock") have focused on simplifying the proof system and reducing withdrawal times from the current ~7 days to near-instantaneous.

## Ecosystem and adoption

Optimism has attracted major DeFi protocols, bridges, and applications. As of 2024, it has significant total value locked, though [Arbitrum](/arbitrum) maintains a larger share of layer-2 activity.

Optimism has benefited from strong institutional support, including backing from Andreessen Horowitz and the Ethereum Foundation. This has translated into developer grants and marketing resources.

## Withdrawal and exit security

A key concern with layer-2 solutions is the exit mechanism. If a user wants to move funds back to [Ethereum](/ethereum) and the layer-2 is compromised, can they be assured of escaping?

Optimism's design ensures that any transaction that has been posted to [Ethereum](/ethereum) can ultimately be verified and enforced on-chain, making exits secure even if the sequencer becomes hostile. However, exit currently takes ~7 days (the fraud proof window), which is inconvenient for urgent needs.

## Competition and differentiation

[Arbitrum](/arbitrum) and Optimism occupy very similar technical and market spaces. Differentiation comes down to ecosystem effects, token community alignment, and governance philosophy.

Arbitrum has higher transaction volumes currently, while Optimism has emphasised its cleaner architecture and governance-first approach. Both are Ethereum rollups backed by strong development teams and venture capital.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum) — the layer-1 that Optimism settles to
- Layer-2 — scaling solutions generally
- Optimistic rollup — Optimism's underlying technology
- [Arbitrum](/arbitrum) — a competing rollup
- [Polygon](/polygon) — another Ethereum scaling solution

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Validator](/validator) — who verifies fraud proofs on Optimism
- Smart contract — programs deployed on Optimism
- ZK-rollup — a competing rollup technology
- Sidechain — a less secure scaling approach
- [Cryptocurrency exchange](/cryptocurrency-exchange) — where OP trades

</div>

---
title: "Polygon"
description: "Polygon is a framework for building Ethereum-compatible blockchains and scaling solutions. It provides multiple scaling options, from sidechains to rollups, allowing developers to customise security and performance trade-offs."
keywords:
  - polygon
  - matic
  - layer-2
  - ethereum
  - scaling
  - sidechain
image: "https://picsum.photos/seed/polygon/900/600"
---

*A **Polygon** (formerly Matic, **MATIC**) is a framework for building Ethereum-compatible blockchains and layer-2 scaling solutions. It offers multiple options ranging from sidechains (which sacrifice some Ethereum security) to rollups (which inherit Ethereum's security), allowing developers to choose their preferred security and performance trade-offs.*

<div class="wiki-hatnote">

This entry covers the Polygon network and ecosystem. For Ethereum's base layer, see [Ethereum](/ethereum); for other scaling solutions, see [Arbitrum](/arbitrum) or [Optimism](/optimism); for the underlying rollup technology, see optimistic rollup.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Polygon — key facts</div>

<img src="https://picsum.photos/seed/polygon/900/600" alt="Polygon network architecture diagram" />

<div class="wiki-infobox-caption">Polygon: a framework for Ethereum scaling with multiple options.</div>

|   |   |
|---|---|
| **What it is** | A scaling framework for Ethereum |
| **Native currency** | Matic (MATIC) |
| **Created** | 2017 (launched as Matic in 2019) |
| **Consensus mechanism** | [Proof-of-stake](/proof-of-stake) (main chain) |
| **EVM compatibility** | Full (Ethereum Virtual Machine) |
| **Scaling options** | Sidechains, rollups, stand-alone chains |
| **Transaction cost** | Fractions of a cent to a few cents |
| **Block time** | ~2 seconds (Polygon PoS) |

</aside>

## Origins and vision

Polygon emerged from Matic Network, founded by Jaynti Kanani, Sandeep Nailwal, and Anurag Arjun. The team recognised that [Ethereum](/ethereum) could not scale to billions of users on its base layer alone, and layer-2 solutions would be necessary.

Rather than building a single scaling solution, Polygon took a broader approach: providing a framework and set of tools so developers could build custom Ethereum-compatible blockchains optimised for their specific use case.

## The Polygon PoS sidechain

Polygon's flagship product is the **Polygon PoS sidechain** — a sidechain that runs its own [proof-of-stake](/proof-of-stake) validators. Users and developers can move assets from [Ethereum](/ethereum) to Polygon using a bridge, trade and deploy contracts on Polygon at minimal cost, then move assets back to Ethereum.

Polygon PoS sacrifices some security guarantees compared to [Ethereum](/ethereum). If the sidechain's validators (a smaller set than Ethereum's validators) collude or turn malicious, assets could be lost. However, this is the trade-off: lower security for much higher throughput and lower fees.

## Rollups and rollups

More recently, Polygon has developed **Polygon Rollups** — optimistic rollups and ZK-rollups that bundle transactions on Polygon, publish proofs to [Ethereum](/ethereum), and inherit Ethereum's full security.

Polygon Rollups offer higher security than the PoS sidechain but lower throughput than a sidechain. They are designed for applications that need Ethereum-grade security but cannot afford Ethereum's fees.

## EVM compatibility

All Polygon solutions are compatible with the [Ethereum](/ethereum) Virtual Machine. A smart contract written in Solidity can be deployed to Polygon with zero or minimal changes. This means developers already familiar with Ethereum can build on Polygon without relearning concepts.

This compatibility has been crucial to Polygon's success. Rather than fragmented ecosystems, Polygon attracts projects that want the benefits of Ethereum's developer ecosystem but lower fees.

## Ecosystem and adoption

Polygon has become one of the most-used blockchains globally, with more daily transactions than [Ethereum](/ethereum) base layer in many periods. Major DeFi protocols (Uniswap, Aave, Curve), NFT marketplaces (OpenSea), and gaming projects run on Polygon.

However, much of this activity may be speculative or low-value transactions attracted by the low cost per transaction. More important by [total value locked](/liquidity-pool), Ethereum still dominates.

## Governance and vision

Polygon has a governance token (MATIC) that allows holders to vote on protocol changes. This decentralised governance distinguishes Polygon from many other scaling solutions, though the concentration of voting power among early investors and the team is substantial.

Polygon's stated vision has evolved from "Ethereum scaling" to "becoming the leading platform for Web3" — a broader ambition that includes support for multiple types of blockchains, not just Ethereum-compatible ones.

## Competition from other L2s

Polygon faces increasing competition from [Arbitrum](/arbitrum) and [Optimism](/optimism), which are also Ethereum rollups. These competitors have received substantial venture capital and developer support, particularly from the Ethereum Foundation.

Some developers view rollups (which inherit Ethereum security) as preferable to sidechains (which do not), creating a technical advantage for Arbitrum and Optimism. However, Polygon's earlier market entry and larger active user base give it structural advantages.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum) — the network Polygon scales
- Layer-2 — scaling solutions generally
- Sidechain — Polygon's architecture
- Optimistic rollup — Polygon Rollups' mechanism
- ZK-rollup — an alternative rollup approach

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Proof-of-stake](/proof-of-stake) — Polygon PoS consensus
- [Validator](/validator) — who secures Polygon
- [Arbitrum](/arbitrum), [Optimism](/optimism) — competing layer-2 solutions
- Smart contract — programs deployed on Polygon
- [Cryptocurrency exchange](/cryptocurrency-exchange) — where MATIC trades

</div>

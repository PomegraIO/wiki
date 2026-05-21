---
title: "Arbitrum"
description: "Arbitrum is an Ethereum layer-2 rollup that bundles transactions and submits them to Ethereum in batches. It uses optimistic rollup technology and is EVM-compatible, inheriting Ethereum's security while offering lower fees."
keywords:
  - arbitrum
  - arb
  - layer-2
  - ethereum
  - rollup
  - scaling
image: "https://picsum.photos/seed/arbitrum/900/600"
---

*An **Arbitrum** (**ARB**) is an Ethereum layer-2 scaling solution that bundles transactions together and posts them to [Ethereum](/ethereum) in batches. It uses optimistic rollup technology, inheriting [Ethereum](/ethereum)'s security while reducing transaction fees by 10–100x and processing transactions much faster.*

<div class="wiki-hatnote">

This entry covers the Arbitrum network. For Ethereum's base layer, see [Ethereum](/ethereum); for competing layer-2 solutions, see [Optimism](/optimism) or [Polygon](/polygon); for the underlying rollup technology, see optimistic rollup.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Arbitrum — key facts</div>

<img src="https://picsum.photos/seed/arbitrum/900/600" alt="Arbitrum rollup architecture" />

<div class="wiki-infobox-caption">Arbitrum: an Ethereum layer-2 that scales while inheriting security.</div>

|   |   |
|---|---|
| **What it is** | An Ethereum layer-2 rollup |
| **Governance token** | ARB |
| **Created** | 2021 |
| **Developer** | Offchain Labs |
| **Technology** | Optimistic rollup |
| **EVM compatibility** | Full (Ethereum Virtual Machine) |
| **Transaction cost** | Fractions of a cent |
| **Block time** | ~0.25 seconds |
| **Security** | Inherits Ethereum's consensus |

</aside>

## Technology and design

Arbitrum was developed by Offchain Labs (founded by Ed Felten, Steven Goldfeder, and Steven Juvekar) to bring [Ethereum](/ethereum) transactions on-chain at scale. It uses optimistic rollup technology: a sequencer collects transactions, compresses them, and posts a "commitment" to [Ethereum](/ethereum).

The commitment is trusted optimistically (hence "optimistic rollup") — it is assumed correct unless someone posts a fraud proof. If a fraud proof is provided, the transaction is re-executed on [Ethereum](/ethereum) to determine the true outcome. This design keeps [Ethereum](/ethereum) as the ultimate arbiter of truth while moving computation off-chain.

## The rollup mechanism

Arbitrum's sequencer processes transactions and generates state roots. These roots are periodically posted to [Ethereum](/ethereum) as part of the rollup's state. Users can always exit to [Ethereum](/ethereum) if they lose faith in the sequencer.

The security model relies on the assumption that at least one honest node is watching the network. If a fraudulent state is posted, an honest observer can submit a fraud proof, forcing re-execution on [Ethereum](/ethereum] and correcting the record.

This is less paranoid than [Ethereum](/ethereum) requiring consensus from thousands of validators, but it is far more secure than a sidechain where a dishonest validator set can steal funds.

## EVM compatibility

Arbitrum is fully compatible with the [Ethereum](/ethereum) Virtual Machine. Developers can compile Ethereum smart contracts to Arbitrum with zero or minimal changes. This drastically lowers the barrier to deployment.

This compatibility is a major advantage over competing technologies. A developer who knows Solidity can deploy to Arbitrum immediately without learning new languages or debugging environment differences.

## Fees and speed

Arbitrum transactions cost fractions of a cent, compared to $1–$100+ on [Ethereum](/ethereum) base layer during periods of high demand. Block time is roughly one-quarter second, providing near-instant confirmation (though transactions are not final until the sequencer posts to [Ethereum](/ethereum], which happens periodically).

For most users and applications, this speed and cost are indistinguishable from finality — certainly sufficient for nearly all use cases.

## Ecosystem and adoption

Arbitrum has attracted a vibrant ecosystem. Major DeFi protocols (Uniswap, Aave, Curve), bridges, and lending protocols have deployed on Arbitrum. As of 2024, it is the largest layer-2 by total value locked.

Many projects deploy to Arbitrum not exclusively but as one of several chains they support, allowing users to choose where to trade or interact based on cost and liquidity.

## Arbitrum Nova and Beyond

Offchain Labs has experimented with additional configurations. **Arbitrum Nova** uses a different data availability layer (hosted committees instead of [Ethereum](/ethereum)) to reduce costs further, though with slightly reduced security. This is intended for applications like gaming or social networks where ultra-low costs matter more than maximal security.

## Governance and the ARB token

In March 2023, Offchain Labs decentralised Arbitrum through the ARB governance token. ARB holders vote on protocol upgrades, fee structures, and treasury spending. This was a significant step toward decentralisation, though the core team and venture capital holders hold substantial voting power.

## Competition with Optimism

Arbitrum and [Optimism](/optimism) are the two largest Ethereum rollups and are conceptually very similar. They compete for developer mindshare and user liquidity. Arbitrum has larger total value locked and more daily transactions, but Optimism has strong venture capital backing and strategic partnerships.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum) — the layer-1 that Arbitrum settles to
- Layer-2 — scaling solutions generally
- Optimistic rollup — Arbitrum's underlying technology
- [Optimism](/optimism) — a competing rollup
- [Polygon](/polygon) — another Ethereum scaling solution

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Validator](/validator) — who watches for fraud proofs on Arbitrum
- Smart contract — programs deployed on Arbitrum
- ZK-rollup — a competing rollup technology
- Sidechain — a less secure scaling approach
- [Cryptocurrency exchange](/cryptocurrency-exchange) — where ARB trades

</div>

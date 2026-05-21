---
title: "Ethereum Dencun"
description: "Ethereum Dencun was an upgrade in March 2024 that introduced blobs for cheaper data availability. It dramatically reduced layer-2 transaction costs by allowing layer-2 solutions to post data to Ethereum more cheaply."
keywords:
  - ethereum dencun
  - blob
  - proto-danksharding
  - layer-2
  - eip-4844
  - scaling
image: "https://picsum.photos/seed/ethereum-dencun/900/600"
---

*An **Ethereum Dencun** upgrade was deployed on 13 March 2024, introducing **blobs** — a new temporary data type that stores information for 18 days before being deleted. This dramatically reduced costs for layer-2 solutions, which use blobs instead of calldata to post transactions, reducing fees by 10–100 times.*

<div class="wiki-hatnote">

This entry covers Ethereum Dencun as an upgrade. For Ethereum broadly, see [Ethereum](/ethereum); for layer-2 solutions, see layer-2 or optimistic rollup.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ethereum Dencun — key facts</div>

<img src="https://picsum.photos/seed/ethereum-dencun/900/600" alt="Blob data structure for layer-2 compression" />

<div class="wiki-infobox-caption">Dencun: blobs enable cheap data availability for layer-2.</div>

|   |   |
|---|---|
| **Deployed** | 13 March 2024 |
| **Key feature** | Blob data type (EIP-4844) |
| **Purpose** | Reduce layer-2 costs |
| **Blob size** | ~128 KB per blob |
| **Blob retention** | 18 days |
| **Cost reduction** | 10–100x for layer-2 transactions |
| **Data availability** | Commitments stored on-chain; data deleted after 18 days |

</aside>

## The problem Dencun solves

Layer-2 solutions like [Arbitrum](/arbitrum) and [Optimism](/optimism) bundle transactions and post them to [Ethereum](/ethereum) for security. However, they posted transaction data as calldata — a permanent part of the ledger.

Storing data on-chain is expensive. [Arbitrum](/arbitrum) and [Optimism](/optimism) transactions could cost a few cents, far cheaper than [Ethereum](/ethereum) base layer (~$10–$100+) but not as cheap as they could theoretically be.

The bottleneck was data availability: layer-2 solutions needed to post enough data to [Ethereum](/ethereum) so that anyone could reconstruct the layer-2 state independently (a security property). But permanent storage on [Ethereum](/ethereum) is expensive.

## Blobs and proto-danksharding

Dencun introduced **blobs** — temporary data storage. A blob is a commitment (a cryptographic hash) that proves data existed, without storing the data permanently on-chain.

Blobs are inspired by a proposal called "Danksharding" (a longer-term Ethereum scaling road map). Dencun implements a precursor: **proto-danksharding** (EIP-4844).

Here is how it works:

1. A layer-2 creates a blob (up to ~128 KB) containing transaction data.
2. The blob commitment is posted to [Ethereum](/ethereum) (small, constant size).
3. Nodes must temporarily store the blob (for ~18 days) to verify layer-2 validity.
4. After 18 days, the blob data can be deleted; only the commitment remains.

This gives layer-2 solutions all the security properties (anyone can reconstruct state from commitments and archived blobs) without permanent storage overhead.

## Cost reduction

The impact was dramatic:

- **Before Dencun:** [Arbitrum](/arbitrum) and [Optimism](/optimism) transactions cost $0.05–$0.50 (depending on congestion).
- **After Dencun:** Transactions dropped to $0.005–$0.05, a 10–100x reduction.

This made layer-2 solutions competitive with alternative chains like [Solana](/solana) and [Polygon](/polygon) in terms of cost, while maintaining [Ethereum](/ethereum)'s security.

## Blob pricing

Blobs have their own gas market, separate from calldata. This allows layer-2 solutions to post cheaper data without competing with base-layer [Ethereum](/ethereum) users for block space.

Blob gas prices can spike if layer-2 solutions flood the network but generally remain low compared to calldata.

## Data availability and archived data

Critics raised a concern: if blob data is deleted after 18 days, how do new layer-2 nodes sync? The answer: layer-2 services (like [Arbitrum](/arbitrum)) run archive nodes that maintain blob data longer than 18 days. Additionally, some projects archive blobs off-chain using services like Arweave or IPFS.

This reintroduces a small trust assumption (that archive nodes persist data), but it is far weaker than relying on a centralised service.

## Impact on layer-2 adoption

Dencun's cost reduction significantly improved layer-2 user experience. Previously, a swap on [Arbitrum](/arbitrum) might cost $0.10–$1.00; after Dencun, it costs $0.01–$0.10. This dramatic reduction likely accelerates layer-2 adoption.

## Future work: full Danksharding

Dencun is proto-danksharding. Full **Danksharding** (a future Ethereum upgrade) would further optimise data availability by using techniques like data availability sampling and 2D sharding, potentially enabling thousands of transactions per second.

Full Danksharding is conceptually designed for, but not yet deployed. Dencun is a pragmatic intermediate step that achieves much of the benefit (low layer-2 costs) with simpler implementation.

## Comparison with competing scaling solutions

Layer-2 solutions now compete with alternative chains on cost:

| Chain | Cost per transaction |
|-------|---|
| [Ethereum](/ethereum) | $10–$100 |
| Layer-2 (post-Dencun) | $0.01–$0.10 |
| [Solana](/solana) | $0.00025 |
| [Polygon](/polygon) | $0.01–$0.10 |

Layer-2 solutions maintain [Ethereum](/ethereum)'s security but now match competing chains' costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum) — the network upgraded
- [Ethereum Merge](/ethereum-merge) — prior upgrade
- [Ethereum Shanghai](/ethereum-shanghai) — prior upgrade
- Layer-2 — the primary beneficiary
- Optimistic rollup, ZK-rollup — use blobs for cost reduction

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- Smart contract — deployed on [Ethereum](/ethereum) and layer-2
- [Arbitrum](/arbitrum), [Optimism](/optimism) — layer-2 solutions using blobs

</div>

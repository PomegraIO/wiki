---
title: "Ethereum Blob Fee Market"
description: "EIP-4844 introduced blobs, a separate fee market for rollup data on Ethereum that expires after ~18 days, allowing cheaper transaction scaling than storing data on-chain permanently."
keywords:
  - ethereum blob fee market
  - EIP-4844
  - proto-danksharding
  - rollup data
  - ethereum scaling
  - blob expiration
---

*EIP-4844 ("**proto-danksharding**") introduced **blobs**—a separate, cheaper fee market for temporary data storage on Ethereum. Rollups bundle thousands of transactions into a blob and post it to Ethereum; validators keep it for ~18 days, then discard it. This separation from permanent on-chain storage allows blob fees to fluctuate independently of execution gas, making it far cheaper to scale Layer 2 transactions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ethereum Blobs — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">Blobs are temporary data; execution gas is forever—the fee markets are separate and designed to be independent.</div>

|   |   |
|---|---|
| **EIP number** | EIP-4844 (proto-danksharding), activated March 2024 |
| **Blob size** | ~128 KB per blob; multiple blobs per block |
| **Retention period** | ~18 days (1,966 Ethereum slots at 12 seconds per slot) |
| **After expiration** | Validators prune blobs; data is no longer available on-chain |
| **Fee market** | Separate from execution gas; uses independent base fee and EIP-1559 dynamics |
| **Rollup benefit** | Cost per transaction drops by 10–100x since blobs are cheaper than calldata |
| **Target fees** | Blob base fee targets ~21,000 wei per byte; executes gas remains ~1–2 wei per byte |

</aside>

## Why Blobs Were Needed

Before EIP-4844, rollups posted transaction data as calldata in regular transactions. Calldata is permanent—stored on every Ethereum node forever—so it costs the same as execution gas (~16 wei per byte). A rollup batch could cost tens of thousands of dollars in gas, making Layer 2 transactions expensive despite the bundling.

The core insight: rollups don't need data *forever*. Validators need a few weeks to download a batch, verify it, and compute the rollup's state. After that, the data can be deleted. A transaction on Arbitrum or Optimism that happened three months ago is final and auditable; its original data batch is no longer essential for network security.

Blobs provide temporary storage—the Ethereum network treats them as ephemeral consensus objects, cleared after ~18 days. This allows a separate fee market with lower prices.

## How the Blob Fee Market Works

Each Ethereum block reserves space for blobs (initially 3–6 blobs per block, expandable via a governance vote). The network uses an EIP-1559-style fee mechanism: a base fee for blobs adjusts dynamically based on how full recent blocks were.

If demand for blob space is light, the base fee is low. Rollups post blobs cheaply. If demand spikes (many rollups posting data simultaneously), the base fee rises exponentially. This creates a price signal and incentivizes users and rollups to defer non-urgent data or choose alternative times.

Unlike execution gas, which is priced in gwei and determined by users' willingness to pay, blob fees are priced in a separate denomination and auto-adjust based on utilization. A rollup operator might wait hours for blob congestion to clear rather than pay 100x the base fee.

## Blob Expiration and Data Availability

The 18-day retention period is engineered to be long enough for:
- Block proposers and full nodes to sync and verify the chain
- Rollup nodes to download batches and compute state transitions
- Users and auditors to verify that rollup operators committed data honestly
- Light clients and bridges to cross-check state roots

After 18 days, validators clear blob data from memory. Archival nodes (operated by Ethereum enthusiasts, rollup infrastructure providers, and centralized services) may retain it longer, but the blockchain itself no longer requires it.

This creates a new security model: rollup sequencers and users must *download* historical data from archive services or P2P networks, not from consensus nodes. It shifts responsibility for data preservation away from Ethereum validators onto rollup-specific infrastructure. For most users, this is invisible—their rollup client downloads data automatically.

## Blob Fees vs Execution Fees

The critical feature is independence. On a congested day when Ethereum is handling heavy NFT minting or large transfers, execution gas may spike to 50 gwei. Blob base fees are unaffected because they use separate block space. Rollups can post data cheaply while execution is expensive.

Conversely, if many rollups are posting blobs simultaneously (e.g., during a market crash when liquidations surge on Layer 2 DEXes), blob fees spike and execution fees remain low. This separation prevents rollups from competing for the same scarce resource.

In practice, blob fees have remained far lower than calldata. On days when a calldata batch would cost $2,000, blob storage costs $20–50. This 50–100x savings per transaction compounds across thousands of bundled transactions, making Layer 2 transactions feasible at $0.01–$0.10 rather than $1–$10.

## Proto-Danksharding and Future Scaling

EIP-4844 is named "proto" danksharding because it's a step toward full danksharding—a future design where Ethereum can support even more blobs (hundreds per block) and shorter retention periods, using cryptographic commitments to make proof-of-availability lighter.

Current blobs are full data downloads; full danksharding uses sampling so validators only need to download a small random fraction of each blob to verify availability. This could increase throughput by another 10–100x without requiring larger blocks.

The phased rollout (proto → full) reflects Ethereum's conservative approach to consensus rule changes. Each step is tested, monitored, and integrated before the next major upgrade.

## Rollup Implications and Competition

EIP-4844 fundamentally changed Layer 2 economics. Arbitrum and Optimism now compete primarily on execution speed, developer experience, and sequencer design, not solely on transaction cost. Smaller or newer rollups can now scale affordably because blob storage is commodity-priced.

It also enabled rollup-centric scaling narratives: instead of expanding Ethereum's base layer, the network provides cheap staging for rollup data, and rollups handle execution parallelism.

## Risks and Tradeoffs

The 18-day expiration window is non-negotiable from the network layer, but rollup operators must ensure they have adequate archival infrastructure. If a rollup's sequencer disappears and no archive retains the data, users lose the ability to reconstruct the rollup's state independently. Most major rollups mitigate this via decentralized sequencers or multiple archive providers, but the risk exists.

Blob pricing is also not immune to manipulation. A sophisticated user could exploit the fee market's exponential dynamics to cause temporary spikes, though the cost of doing so and the rapid base-fee adjustment make this unlikely in practice.

## See also

<div class="wiki-seealso">

### Closely related

- Ethereum scaling — Broader context for Layer 2 and data availability
- Layer 2 Ethereum — Rollups and sidechains that use blobs
- EIP-1559 — Fee mechanism that inspired blob base-fee dynamics
- Zero-knowledge proof — Cryptographic primitives enabling future danksharding
- Data availability — The core problem blobs solve for rollups
- Ethereum gas fees — Execution gas, distinct from blob fees post-EIP-4844

### Wider context

- [Ethereum](/ethereum/) — The network that deployed blobs
- [Optimism](/optimism/) — Rollup using blobs for cost reduction
- [Arbitrum](/arbitrum/) — Rollup using blobs for cost reduction
- [Blockchain fundamentals](/blockchain-fundamentals/) — Consensus and data structure concepts

</div>

---
title: "Blob Transactions on Ethereum"
description: "How EIP-4844 blob-carrying transactions reduce rollup costs by offering cheaper data availability than calldata."
keywords:
  - blob transactions ethereum
  - eip-4844 dencun upgrade
  - rollup calldata costs
  - ethereum data availability
  - proto-danksharding
---

*Blob transactions, introduced in Ethereum's Dencun upgrade via EIP-4844, allow transactions to carry large data payloads at a fraction of the cost of traditional calldata. Because rollups must post transaction data on chain for users to verify state, cheaper data availability directly cuts rollup fees and enables higher throughput.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Blob Transactions on Ethereum — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Blobs separate transaction data from execution, enabling cheaper rollup posting.</div>

|   |   |
|---|---|
| **What it is** | Transactions that carry large blobs of data without requiring the data to be stored long-term in Ethereum state |
| **Data capacity per blob** | ~125 KB per blob; up to 6 blobs per block (~750 KB per block) |
| **Pricing mechanism** | EIP-1559 fee market; blob fees scale with network congestion independently of gas prices |
| **Storage duration** | ~18 days; nodes prune blob data, but availability is guaranteed during that window |
| **Primary use case** | Rollups posting transaction batches; reduces rollup fees by 10–100x vs. calldata |
| **Verification** | Blobs are cryptographically committed; rollup contracts verify commitment, not full data |
| **Fallback** | If blobs are too expensive, rollups can still post data as calldata, but at higher cost |

</aside>

## The Calldata Cost Problem

Before EIP-4844, rollups had one way to store transaction data on Ethereum: as calldata, the input bytes passed to a smart contract function. Calldata is permanently stored in the blockchain's history (every node retains it forever) and costs 4 gas per zero byte and 16 gas per non-zero byte.

For a rollup batching 100 transactions, the calldata might be 5,000 bytes. At 16 gas per byte (a typical average), that's 80,000 gas, or roughly USD 1–5 per rollup batch depending on Ethereum's base fee. For rollups processing thousands of transactions per second, calldata costs quickly dominate user fees.

More importantly, this cost structure doesn't scale. Calldata is priced as if it will be retained forever by every node, but rollups only need data available temporarily—long enough for users to verify the state transition and download it if needed. Paying for eternal storage was economically wasteful.

## How Blobs Solve the Storage Economics

Blob transactions solve this by separating **data commitment** from **data availability**. A blob transaction includes:

- A cryptographic commitment (proof) that the blob contains specific data.
- The blob itself, available to the network for roughly 18 days.
- A verification target: rollup contracts on Ethereum can verify the commitment without the blob ever being "called" into the EVM or stored in state.

Nodes download and verify blobs for 18 days, then prune them. Users who need to verify the rollup's state or recover data can download blobs during that window. After 18 days, blobs are discarded—but the commitment on chain proves they existed and what they contained.

This means Ethereum secures the rollup's data availability guarantee (someone has the data, and the commitment proves what it is) without storing it forever. Blobs cost far less: roughly 1–2 gas per byte, or 10–20 times cheaper than calldata.

## Proto-Danksharding and Future Expansion

EIP-4844 is officially called "proto-danksharding" because it mimics the data-availability sampling technique that will underpin full danksharding. In full danksharding (planned for future Ethereum upgrades), hundreds or thousands of blobs per block would be supported, and nodes would only download a small random sample of each blob to verify availability. This trades off trust (sampling is probabilistic, not deterministic) for massive scalability.

Proto-danksharding simplifies the design by requiring nodes to download and verify all blobs—no sampling. It supports 6 blobs per block, a practical limit for current hardware. As Ethereum upgrades, this could grow to 8, 12, or more blobs per block without requiring sampling logic.

## The Blob Fee Market

Blobs have their own fee market, separate from the gas market. When block space is congested with regular transactions, blob fees may remain low; when blocks are empty but many rollups need to post data, blob fees rise independently.

This separation is intentional: it prevents rollups and normal users from competing in the same fee auction, which could make rollups unpredictably expensive during high-demand periods. Blob fees are published as a separate metric (in wei per blob) and follow EIP-1559 logic: if blobs are underutilized, fees drop; if the network consistently has 3+ blobs per block, fees rise.

## Rollup Economics Before and After EIP-4844

A rollup with 100 transactions per batch, averaging 50 bytes per transaction, must post 5,000 bytes of data. Pre-EIP-4844 calldata cost: 5,000 bytes × ~16 gas/byte = 80,000 gas. At a 30 gwei base fee (roughly USD 2 per gwei), that's 0.0024 ETH or ~USD 8.

Post-EIP-4844, the same 5,000 bytes in a blob costs roughly 5,000 bytes × 1 gas/byte = 5,000 gas equivalent, or 0.00015 ETH per batch, ~USD 0.50. Depending on blob congestion, fees might be slightly higher, but typically 10–50 times cheaper than calldata.

For users, this translates to lower rollup fees. A rollup that was charging USD 0.50–1.00 per transaction due to data costs might drop to USD 0.05–0.10. This has a direct effect on rollup adoption and competitiveness.

## Verification and Rollup Contract Design

When a rollup posts a blob transaction, the rollup's smart contract on Ethereum receives a commitment (hash) of the blob. The contract's job is to verify that the commitment is correct—meaning the blob indeed contains the batch data the rollup claims.

The contract does not execute the blob or store it. Nodes verify the cryptographic commitment (via KZG polynomial commitment schemes in EIP-4844) and ensure the blob is available. If a rollup attempts to post a false commitment or claims data that wasn't actually included in a blob, the fraud is detectable.

This is why rollups can use blobs safely: the commitment is as binding as calldata, but the storage is temporary and cheaper.

## Data Availability and User Security

Users need to download and verify rollup batches to confirm their transactions are included and correctly processed. With blobs, users must do this within 18 days of the batch being posted. In practice, rollups and community members run archive nodes (or data-availability services like Celestia or EigenDA) to ensure data persists longer.

Most users don't verify blobs themselves; they rely on wallet providers, block explorers, or rollup nodes. But the 18-day window is sufficient for:

- Validators to detect and challenge fraudulent proofs or invalid state transitions.
- Users to download data and recover funds if the rollup is attacked or shuts down.
- Full-node operators to archive data if they want permanent history.

In an optimistic rollup, a fraud prover could use the blob data to construct a fraud proof challenging the rollup's on-chain state. The 18-day window gives ample time for this before data is pruned.

## When Blobs Become Expensive and Fallbacks

If a large demand surge causes blob congestion, blob fees can spike significantly. During such periods, a rollup might choose to post data as calldata instead, accepting higher fees for that batch. This fallback is automatic in rollup contracts: if blobs are too expensive, the rollup will use calldata (or another data-availability chain like Arbitrum's AnyTrust or Optimism's proposed Plasma).

The existence of blobs has created a competitive pressure on data costs across Ethereum and alternative solutions, benefiting users regardless of which data-availability method a rollup ultimately uses.

## See also

<div class="wiki-seealso">

### Closely related

- ZK Rollup — rollup using validity proofs; heavily relies on cheap data availability
- [Optimistic Rollup](/optimistic-rollup/) — rollup using fraud proofs; requires posting full transaction data on chain
- Calldata — traditional, permanent data storage on Ethereum; more expensive than blobs
- Data Availability Sampling — technique for verifying data availability without downloading all data
- [ZK Proof Generation Time](/zk-proof-generation-time/) — computational cost of creating rollup proofs; separate from data costs

### Wider context

- Ethereum Layer 2 — category of solutions building on top of Ethereum
- Dencun Upgrade — Ethereum upgrade that activated EIP-4844 and blobs
- EIP-1559 — fee market mechanism underlying blob pricing

</div>

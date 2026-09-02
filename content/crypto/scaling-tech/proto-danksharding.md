---
title: "Proto-Danksharding"
description: "EIP-4844, Ethereum's 2024 upgrade introducing blob-carrying transactions as the interim step toward full Danksharding data scaling."
keywords:
  - eip-4844
  - blob transactions
  - ethereum scaling
  - data availability
  - sharding roadmap
image: "/svg/crypto.svg"
---

*[Proto-Danksharding](/proto-danksharding/) (EIP-4844) is Ethereum's 2024 upgrade that introduced blob-carrying transactions, decoupling data fees from execution and laying groundwork for full [Danksharding](/danksharding/). Blobs are temporary, data-only storage; they prove that data existed without requiring it to stay available forever.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proto-Danksharding — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for Ethereum scaling phases." />

<div class="wiki-infobox-caption">Temporary blobs decouple data costs from execution, stepping toward full sharding.</div>

|   |   |
|---|---|
| **What it is** | EIP-4844; transaction type carrying up to 4–6 MB of temporary data per block |
| **Lifespan** | Data kept by validators for ~18 days, then discarded (data availability window) |
| **Fee mechanism** | Separate fee market for blob space; independent of gas |
| **Primary user** | Rollups and other layer 2 systems aggregating transactions |
| **Throughput gain** | ~3–5× reduction in settlement costs for rollups |
| **Next stage** | Full [Danksharding](/danksharding/) with attester sampling |

</aside>

## Why blobs fill the gap

Before EIP-4844, rollups had to compress transactions and post them as calldata—the ordinary transaction data field. Calldata is stored forever, which is wasteful: a rollup needs data only long enough for users to verify and reconstruct the state. After that, the data can be safely deleted.

Proto-Danksharding introduces **blobs**: temporary data fields designed exactly for this use case. A blob is committed to the chain (so rollups can prove they posted it), but validators automatically discard it after ~18 days. This two-tier model—commitment without permanence—is the architectural innovation that makes scaling possible.

The fee is separate too. Gas fees pay for computation and storage. Blob fees pay for data availability. This isolation lets the network scale data throughput independently from execution throughput.

## How blobs work

A blob transaction includes up to four blobs, each up to 131,072 bytes. Validators store blobs in memory during the validity window, then garbage-collect them. The blobs are committed using **KZG commitments**, a cryptographic scheme that lets anyone prove a blob's contents without transmitting the whole blob.

When a rollup sequencer posts a batch, it includes blob commitments onchain. Users download blobs from gossip peers (or from archival nodes) to verify the rollup state. After 18 days, they're gone—no longer anyone's burden.

This simplicity is the strength. Blobs do not require new consensus rules beyond KZG polynomial commitments. No random sampling, no new staking, no complex fairness protocols. Every validator still handles all blobs; the difference is they do not keep them forever.

## Fee dynamics

Proto-Danksharding introduced a separate fee market for blobs. As blob demand rises, blob fees rise; as it falls, they fall. The algorithm mimics EIP-1559's dynamic base fee but for blobs independently.

Before EIP-4844, a rollup posting 1 MB of data paid roughly the same as executing a transaction. After, the same 1 MB costs much less, proportional to actual network bandwidth rather than storage cost. Rollup fees dropped by 3–5×, instantly.

This fee model is temporary. Full Danksharding will use attester sampling instead, removing the need for all validators to download all data.

## The bridge to full Danksharding

Proto-Danksharding is intentionally incomplete. It is the staging post on the path to [full Danksharding](/danksharding/).

Full Danksharding removes the "all validators download all blobs" constraint. Only a random sample of validators attests to each data chunk. This allows Ethereum to commit to far more data—potentially hundreds of MB per slot—without overloading individual validators.

Proto-Danksharding does all the hard work of decoupling data from execution. Full Danksharding adds the sampling layer to remove the bandwidth bottleneck entirely.

## Impact on rollups

Rollups are the main beneficiary. A [Optimistic Rollup](/optimistic-rollup/) must post transaction data onchain so anyone can reconstruct the state and validate proofs. A ZK Rollup needs to post commitments proving its state is correct.

Proto-Danksharding made both cheaper by an order of magnitude. A ZK Rollup that once paid 90% of its fees for data now pays 10–20%. An Optimistic Rollup that cost users $1 per transaction now costs $0.10–0.30. The network's throughput, as seen by end users, rose immediately.

This created new use cases: dApps that were uneconomical on-chain became viable on rollups. NFT minting, smaller financial transactions, and gaming all moved to layer 2.

## Technical constraints

The 131 KB per-blob limit exists for network propagation reasons. If blobs were larger, validators would struggle to download them within a single slot (~12 seconds). The 4–6 blob limit per block is arbitrary but conservative; Ethereum could increase it as network efficiency improves.

The 18-day retention window is also tuneable but chosen to balance security (time for light clients to download data) against validator storage burden. Longer windows risk accumulated blob storage; shorter windows reduce data availability window for offchain verifiers.

## Comparison to other scaling approaches

Proto-Danksharding solves data availability for layer 2, not throughput directly. It does not increase Ethereum's own transaction capacity. Instead, it makes layer 2s cheaper and more viable.

Alternatives like sidechains or [state channels](/state-channel/) avoid publishing data onchain altogether. But they trade off security: a sidechain is only as safe as its validators, not Ethereum's. Blobs preserve security while reducing cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Danksharding](/danksharding/) — the full sharding design Proto-Danksharding leads toward
- [Recursive SNARK](/recursive-snark/) — proof compression used alongside blob data
- Rollup — layer 2 system that pays for blob space
- [Optimistic Rollup](/optimistic-rollup/) — rollup using data availability for fraud proofs
- ZK Rollup — rollup using blobs for proof commitments and state roots

### Wider context

- Layer 2 — scaling solutions relying on Proto-Danksharding economics
- [Ethereum](/ethereum/) — blockchain implementing EIP-4844
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the scalability constraints Proto-Danksharding addresses

</div>

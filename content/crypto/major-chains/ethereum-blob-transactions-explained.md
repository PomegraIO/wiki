---
title: "Ethereum Blob Transactions Explained"
description: "What are Ethereum blob transactions? Learn how EIP-4844 reduces rollup data costs by storing calldata in a temporary, cheaper fee market."
keywords:
  - ethereum blob transactions explained
  - eip-4844 blob transactions
  - calldata storage ethereum
  - layer 2 scaling blobs
  - ethereum dencun upgrade
image: /svg/crypto.svg
---

*An **Ethereum blob transaction** (EIP-4844, activated in the Dencun upgrade of March 2024) separates transaction calldata into a cheaper, temporary storage market that expires after 4,096 epochs (~18 days). Instead of storing rollup batch data forever on-chain at full gas rates, blobs sit in a separate fee market that's orders of magnitude cheaper, slashing layer-two rollup costs by 80–90% and making high-frequency DeFi and payments practical at scale.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ethereum Blob Transactions — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A second-layer fee market that expires automatically, unlocking cheaper scaling.</div>

|   |   |
|---|---|
| **EIP number** | EIP-4844 (Proto-Danksharding) |
| **Blob size** | 128 KB per blob |
| **Maximum blobs per block** | 6 blobs (768 KB total) |
| **Blob lifetime** | 4,096 epochs (~18.2 days) |
| **Fee market** | Separate from execution gas; EIP-1559 mechanics apply |
| **Primary user** | Layer 2 rollups (Arbitrum, Optimism, Starknet) |
| **Cost reduction** | 80–95% cheaper than calldata for rollups |

</aside>

## The Problem Blobs Solve: Calldata Bottleneck

Before blobs, Ethereum layer-two rollups faced a brutal economic constraint. To achieve [finality](/blockchain-fundamentals/), a rollup operator must post all transaction data on Ethereum mainnet—not just a state commitment, but the full calldata that allows anyone to re-execute the rollup's history and verify it's correct.

Calldata stored in Ethereum transactions costs 16 gas per byte (or 4 gas per zero byte). For a rollup processing 2,000 transactions per second, that's roughly 200 KB of data per second hitting mainnet, burning 800,000–2,000,000 gas per second just on data storage. Since mainnet can only handle ~15 million gas per block (every 12 seconds), data volume becomes the binding constraint on throughput.

This is why rollups existed: to move transactions off-chain, then post compressed summaries on mainnet. But even compressed, the data was expensive. Arbitrum and Optimism each pay millions in weekly Ethereum fees just to post calldata. Users bear this cost in the form of rollup fees that don't scale linearly with execution complexity—they're mostly determined by data volume.

Blobs attack the root of the problem: create a separate fee market for data that doesn't need to live forever.

## How Blobs Work: Temporary Storage at Cheaper Rates

A **blob** is a 128 KB chunk of data attached to a transaction. Unlike calldata (stored in transaction logs permanently), blobs are stored in the consensus layer and are available to validators for only ~18 days. After that, the data is pruned.

This design works because rollups don't need the data forever. A rollup needs 18 days to allow users to:
1. Verify the rollup's state commitment
2. Challenge any invalid state transitions
3. Withdraw their funds if the rollup is censoring them

For honest rollups with working fraud-proof systems, 18 days is ample. For users taking on smart-contract risk, trusting the rollup operator, 18 days is more than sufficient to prove non-inclusion or theft.

Blobs follow EIP-1559 fee mechanics, but in their own marketplace. Instead of burning transaction base fee, the network dynamically adjusts the blob base fee based on blockspace usage. When demand for blobs is high, the fee rises; when low, it falls (approaching a floor of 1 wei per blob). This means blob fees are typically 10–100x cheaper than calldata rates, since rollups can batch thousands of user transactions into a single blob.

## Blob Economics for Rollups

Consider a simple example: an Arbitrum transaction paying 0.001 ETH in fees. Before blobs, that 0.001 ETH was split between:
- Execution (smart-contract compute): ~0.0002 ETH
- Calldata (posting to Ethereum): ~0.0008 ETH

After blobs, the calldata component drops to ~0.00008 ETH, and the user pays 0.0002 ETH, a 5x reduction.

Scaled across a busy rollup processing millions of transactions daily, the savings are staggering. Arbitrum's costs fell from ~$3–5 million weekly to ~$500,000 weekly after EIP-4844. Optimism saw similar reductions. These savings are passed to users, making rollups viable for payments, NFTs, and high-frequency trading that were previously uneconomical.

The trade-off is data availability. Rollups must trust that Ethereum validators will keep blobs available for 18 days. This is not cryptographically enforced; it's enforced by protocol rules (validators are penalized if they attest to blocks whose blob data is unavailable). For the current Ethereum validator set, this is a reasonable assumption—but it's less strong than on-chain calldata, which is auditable forever.

## EIP-4844 (Proto-Danksharding): The Roadmap

EIP-4844 is called "Proto-Danksharding" because it's a stepping stone to full Danksharding, a more ambitious design that uses [zero-knowledge proofs](/proof-of-work/) to verify data availability rather than trusting validator attestation.

Under full Danksharding (proposed for later versions of Ethereum):
- Blobs scale to megabytes per block
- Data availability is proven cryptographically, not trusted
- Rollups can become effectively as cheap as posting transactions to a local database

For now, EIP-4844 caps blobs at 6 per block (768 KB total per 12-second block). This is still enough to reduce rollup costs by 80–95%, but it's not the ultimate scaling solution. It's an incremental improvement.

## Blob Expiry and Finality Considerations

The 18-day blob expiry creates a design question: what guarantees do users have after the blobs are pruned?

For a well-functioning rollup with working fraud proofs:
- Users can challenge invalid state transitions during the 18-day window
- Once challenged, the state is frozen and users can exit
- After 18 days, the rollup's historical data is gone, but the rollup's current state commitment remains on-chain

For users withdrawing funds from the rollup to Ethereum, the process must complete within 18 days (for optimistic rollups) or near-immediately (for zero-knowledge rollups). As long as the rollup is not actively censoring withdrawals, users are safe.

The risk is **censoring rollups**: if a rollup operator intentionally stops including withdrawal transactions, users can try to exit via the fraud-proof mechanism within 18 days. After the blobs expire, those users have no recourse except to hope the rollup operator relents or was replaced.

This is not a new risk—it exists with any rollup—but blob expiry makes it explicit. High-stakes applications (custody, exchanges) may run light clients that validate the rollup continuously, rather than trusting the 18-day window.

## Blob Transaction Format and Validators

A blob transaction includes:
- Standard transaction fields (to, value, data, gas price)
- Blob commitments (KZG commitments proving the blob data)
- Blob data (up to 128 KB)

Validators include blobs in the block and attest to their availability. Full nodes download and validate blobs but do not permanently store them. Archive nodes retain blobs beyond the 18-day window for historical analysis.

This creates new hardware requirements: validators running Ethereum after EIP-4844 must handle an additional ~100–150 GB per month of blob data (at current usage rates), though the network will eventually prune it. This has raised concerns about validator hardware requirements, though the consensus is that it's manageable.

## Adoption and Future Evolution

Since EIP-4844, Arbitrum, Optimism, Starknet, and other rollups have integrated blob transaction support. Cost reductions were immediate and dramatic. Some rollups have started bundling transactions more aggressively, packing more user data into each blob.

The next question is whether Ethereum core developers will raise the blob capacity (say, from 6 to 9 or 12 per block) to reduce costs further. Current discussions suggest modest increases are likely, but full scaling to thousands of blobs requires the full Danksharding fork, which is years away.

In the interim, blobs represent a major unlock for Ethereum scaling—cheap enough for payments and DeFi, but within an intentionally conservative envelope that lets the network prove the model works before scaling further.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — Distributed consensus that underpins blob validation
- [Proof of work](/proof-of-work/) — Ethereum's historical consensus mechanism
- [Proof of stake](/proof-of-stake/) — Current Ethereum consensus; validators attest to blob availability
- [Smart contract](/smart-contract/) — Layer-two applications that benefit from cheaper calldata via blobs
- [Distributed ledger](/distributed-ledger/) — The underlying architecture for blob storage

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where users trade tokens affected by scaling changes
- [Ethereum](/ethereum/) — The host blockchain for blobs and rollup scaling
- [Execution risk](/execution-risk/) — Operational risk of rollups relying on blob data availability
- Layer 2 solutions — Rollups and sidechains that use blobs for cost reduction

</div>

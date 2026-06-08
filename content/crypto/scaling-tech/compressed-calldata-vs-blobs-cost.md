---
title: "Compressed Calldata vs Blobs: Cost Comparison"
description: "Compare compressed calldata vs blobs cost for Layer 2 rollups: break-even throughput, fee mechanics, and when each scaling solution saves money."
keywords:
  - compressed calldata vs blobs cost
  - EIP-4844 blobs
  - rollup compression
  - Layer 2 scaling economics
  - blob storage cost
  - calldata pricing
---

*Layer 2 rollups post transaction data to Ethereum to ensure security, but **compressed calldata vs blobs cost** depends on the volume of transactions and current market conditions. **Blobs** (EIP-4844) offer cheaper data storage for high throughput, while **compressed calldata** can be cheaper when throughput is low or when blob demand spikes the blob fee market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Calldata vs Blobs — cost factors</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain scaling." />

<div class="wiki-infobox-caption">The choice between storage methods hinges on data volume, network congestion, and whether the rollup can fill blob space efficiently.</div>

|   |   |
|---|---|
| **Pricing model** | Calldata: per-byte cost tied to gas price; Blobs: separate market with lower baseline fee |
| **Target throughput** | Calldata: economical below ~50–100 tx/s; Blobs: economical above that range |
| **Scalability** | Calldata: capped by Ethereum gas limit; Blobs: larger per-block allowance (1–6 MB per block) |
| **Cost volatility** | Calldata: high (moves with all gas); Blobs: independent fee market (less correlated) |
| **Data persistence** | Calldata: on-chain forever; Blobs: pruned after ~18 days (data availability, not archival) |
| **Compression overhead** | Calldata: compression ratio 2–3x helps; Blobs: compression still beneficial but raw blob cost is already low |

</aside>

## How Calldata Costs Work

Rollups store compressed transaction data as calldata (input to a verification smart contract) on Ethereum Layer 1. Calldata costs 16 gas per byte for zero bytes and 4 gas per byte for non-zero bytes. When gas price is high (during network congestion), calldata becomes expensive.

A typical rollup transaction compresses to roughly 50–200 bytes after zstd or similar compression. If Ethereum's base gas price is 50 gwei, a 100-byte compressed transaction costs:
- 50 bytes of zeros + 50 bytes of non-zeros: (50 × 16 + 50 × 4) × 50 gwei = 50,000 wei = 0.00005 ETH ≈ $0.15 (at \$3,000 per ETH)

At 100 transactions per second, that is 360,000 ETH per day in data costs alone—unsustainable. Even at lower throughput, calldata becomes the dominant cost lever in a rollup's fee structure.

## How Blob Costs Work

EIP-4844 introduced "blobs" (data blobs), a new transaction type with a separate fee market. Each Ethereum block can include up to 6 blobs, each blob is ~128 KB, providing ~768 KB of blob space per 12-second block. This is more than 100x the calldata capacity of the same block.

Blob fees are priced independently of regular gas, using a similar EIP-1559 mechanism: a base blob fee that adjusts based on how full blob space is, plus a priority fee. The base blob fee starts low (currently on the order of 1–10 wei per byte under low demand) and climbs only if blocks consistently exceed the target (half the max blob space).

The same 100-byte transaction posted as a blob might cost 0.001 ETH at low blob demand, versus 0.00005 ETH of calldata cost at 50 gwei base gas. At first glance, blobs seem 20x more expensive, but the key is scale: because blob space is so abundant, a rollup can fill it densely without driving up the blob fee.

## Break-Even Throughput

The crossover point where blobs become cheaper than calldata depends on gas price and blob demand.

**Scenario 1: Low congestion (base gas 30 gwei, low blob demand)**
- Calldata: 100 bytes = (50 × 16 + 50 × 4) × 30 gwei ≈ 0.00003 ETH
- Blob (at 1 wei per byte): 100 bytes ≈ 0.0001 ETH
- Calldata wins

**Scenario 2: Moderate congestion (base gas 100 gwei, low blob demand)**
- Calldata: 100 bytes ≈ 0.0001 ETH
- Blob (at 1 wei per byte): 0.0001 ETH
- Roughly breakeven

**Scenario 3: High congestion (base gas 200 gwei, moderate blob demand at 50 wei/byte)**
- Calldata: 100 bytes ≈ 0.0002 ETH
- Blob: 100 bytes ≈ 0.005 ETH
- Calldata wins again if blob demand is high

The practical break-even throughput threshold sits around 50–150 transactions per second, depending on the specific market state. Below that, calldata is often competitive; above it, blobs offer much larger headroom and lower marginal cost.

## Why Rollups Still Compress Both

Even with blobs, rollups compress transaction data. Compression ratios of 2–3x are standard, using algorithms like zstd or brotli.

For calldata, compression is essential because every byte is expensive. For blobs, compression is less critical (the byte cost is lower), but it still matters for throughput: a 2x compression ratio allows a rollup to fit twice as many transactions in the same blob space, doubling effective throughput without increasing on-chain costs. This becomes important when a rollup wants to offer very low fees at scale.

## Market Conditions and Volatility

Calldata costs are volatile: they move in lockstep with Ethereum's base gas price, which spikes whenever network demand is high (not necessarily high for the rollup specifically). If a major DeFi protocol has a price oracle update or a large NFT mint happens on Ethereum, base gas rises, and all rollups suddenly pay more to post data, even if their own throughput is unchanged.

Blob fees are decoupled, so they only rise if many rollups (or other blob users) are posting a lot of data simultaneously. This provides more stable pricing for rollups in the medium term but introduces a new vector: if a rollup becomes very popular and fills blobs to capacity, the blob base fee will climb, potentially outpacing calldata again.

In practice, as of 2025, blobs have not been consistently full. Blob fees remain very low (under 10 wei per byte most days), making blobs the default choice for new and existing rollups at any non-trivial throughput. Arbitrum and Optimism have begun migrating to blob-based data posting.

## Strategic Considerations for Rollups

A rollup operator must decide whether to post all data as blobs, all as calldata, or split between them. Some rollups use a hybrid approach:

- **High-priority or batched transactions** → blobs, because the cost is predictable and scales well
- **Sparse transactions during low-demand periods** → calldata, because base gas fees may be cheaper
- **Critical state updates** → calldata, because calldata data persists permanently (blobs are pruned after ~18 days)

The choice also depends on user behavior. A gaming rollup with thousands of small transactions will benefit enormously from blobs. A settlement-layer rollup handling larger transactions may care less about the marginal data cost and more about finality and security guarantees.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — Ethereum's consensus mechanism, including blob mechanics
- [Rollup](/blockchain-fundamentals/) — Layer 2 scaling solution that depends on data availability
- [Data Availability](/blockchain-fundamentals/) — why posting transaction data on-chain matters
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where users interact with rollup assets
- [Hash Rate](/hash-rate/) — computational proof-of-work (contrast with data-availability layers)

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundation for understanding Ethereum and rollups
- [Distributed Ledger](/distributed-ledger/) — the broader concept of decentralized state
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — user-facing platforms for rollup tokens
- Ethereum — Layer 1 chain supporting Layer 2 rollups

</div>

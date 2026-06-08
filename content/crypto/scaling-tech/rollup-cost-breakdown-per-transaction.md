---
title: "Rollup Cost Breakdown Per Transaction"
description: "A rollup transaction fee splits across L2 execution, data posting, and proof costs—each scales differently as network throughput rises."
keywords:
  - rollup cost breakdown
  - layer 2 transaction costs
  - rollup fees
  - ethereum scaling
  - transaction fee components
  - blockchain economics
image: "/svg/crypto.svg"
---

*A **rollup cost breakdown per transaction** reveals that the fee you pay is not a single number but a composite: a small slice for executing your transaction on Layer 2, a much larger piece for posting proof data back to the base chain, and a tiny fraction for the cryptographic proof itself. Understanding how each component scales with network volume is essential to grasping why rollups reduce costs, and how much room they have left to improve.*

<div class="wiki-hatnote">

This article covers the technical cost structure of rollups. For the broader mechanism, see [distributed-ledger](/distributed-ledger/) and [smart-contract](/smart-contract/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rollup Transaction Costs — Breakdown</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain." />

<div class="wiki-infobox-caption">A typical rollup fee is dominated by the cost of publishing batches to Layer 1.</div>

|   |   |
|---|---|
| **Typical L2 execution cost** | 0.5–2% of total fee |
| **Data posting to L1** | 60–85% of total fee |
| **Proof generation & verification** | 5–15% of total fee |
| **Sequencer/operator markup** | 5–20% of total fee |
| **Savings vs. L1** | 50–100x cheaper for simple transfers |

</aside>

## The Three Cost Buckets

A rollup transaction incurs three distinct costs, each paid to a different party or system:

**L2 Execution Cost** — Your transaction is executed on the Layer 2 virtual machine (whether optimistic or zero-knowledge based). This cost is tiny: the L2 has spare capacity compared to Layer 1, and execution is simple to compute. You pay this to the [sequencer](/smart-contract/) or operator who organizes transactions into a block.

**Data Posting Cost** — The rollup must publish a summary of all transactions (or the raw transaction data itself, depending on the scheme) back to Ethereum or another Layer 1. This is by far the largest component. You are not paying for computation; you are paying for the raw cost of storing data on the most expensive blockchain in the world—Ethereum mainnet. A single byte of calldata on Ethereum costs roughly 16 gas units, or about USD 0.10–0.50 per kilobyte at typical gas prices. Your single transaction might cost 100–200 bytes when batched with others, translating to USD 10–100 per kilobyte in batch overhead.

**Proof Generation & Verification** — The rollup produces a cryptographic proof (either a succinct zero-knowledge proof in ZK rollups, or a fraud proof in optimistic rollups) and posts it to Layer 1. Generating the proof is expensive; verifying it on Layer 1 is also expensive. This cost is typically spread across a batch of thousands of transactions.

On top of these three, the sequencer or operator may add a markup—a profit margin or fee to run the infrastructure.

## How Data Cost Dominates

In a typical rollup, the data posting cost is 60–85% of your fee. Here is why:

A single Ethereum transaction can hold perhaps 1,000–2,000 bytes of calldata. If 5,000 Layer 2 transactions are batched together, each transaction "consumes" roughly 0.2–0.4 bytes of L1 space—but that scales linearly. If batches grow, the per-transaction cost of data shrinks.

Conversely, if a rollup uses data [availability](/distributed-ledger/) solutions (like EigenDA or a separate data availability committee) instead of posting to Ethereum directly, the cost drops dramatically. A commitment to off-chain data is far cheaper than calldata on mainnet. This is why newer rollups like Arbitrum (which uses ArbOS compression) and Optimism (which uses [brotli](/smart-contract/) compression) have aggressively optimized data posting. They cannot eliminate it, but they can shrink the bytes per transaction.

## Proof Cost and Sequencer Profit

Proof generation is expensive upfront but amortized over a batch. A zero-knowledge proof for a rollup block might cost USD 1,000–10,000 in compute to generate, but if you spread that over 10,000 transactions in a batch, it is only USD 0.10–1.00 per transaction. As batches grow larger, proof cost per transaction shrinks toward zero.

Verification cost on Layer 1 is fixed per proof: a single proof verification on Ethereum might cost 100,000–500,000 gas. At USD 30–50 per 1 million gas, that is USD 3–25 per proof. Again, spread over 10,000 transactions, it is negligible.

The sequencer's profit margin varies widely. Some rollups use decentralized sequencing pools, which compete down margins. Others are centralized, with a single sequencer that captures the spread between transaction fees and actual costs. As rollups mature and more sequencers enter the market, competition should compress margins toward actual costs.

## Scaling Dynamics

The cost structure has a crucial implication: **data cost dominates, but execution and proof costs approach zero at scale**.

|   | Cost per TX (Low throughput) | Cost per TX (High throughput) |
|---|---|---|
| L2 execution | USD 0.01 | USD 0.001 |
| Data posting | USD 1.00 | USD 0.10 |
| Proof | USD 0.50 | USD 0.05 |
| **Total** | **USD 1.51** | **USD 0.151** |

This is why Ethereum's Dencun upgrade (March 2024) was a game-changer: it introduced EIP-4844, which created a separate "blob" space on the blockchain with much cheaper data posting (roughly 1/100th the cost of calldata). Suddenly, rollup fees dropped by 50–90%, because the dominant cost component was slashed.

Similarly, this explains why rollups that use external data availability layers (like Celestia or EigenDA) can offer even lower fees: they sidestep the L1 data bottleneck entirely.

## Why Rollups Are Still Cheaper Than L1

A direct Ethereum transaction costs USD 0.50–5.00 in fees, depending on network congestion. A rollup transaction costs USD 0.01–0.50. The gap persists because:

1. **Rollup execution is lighter** — A rollup does not need to reach consensus among thousands of validators. It is a single sequencer or a small committee.

2. **Data is batched** — One thousand transactions are compressed into a single L1 posting.

3. **Proof is amortized** — One proof covers thousands of transactions.

Even with these optimizations, the rollup cannot go below the cost of publishing some commitment to Layer 1. You cannot have a rollup that is truly on-chain without posting data somewhere expensive. That is the fundamental trade-off: more on-chain security, higher data cost.

## The Remaining Frontier

The next frontier in rollup cost reduction is fourfold:

**Data availability innovation** — Celestia, EigenDA, and other [distributed-ledger](/distributed-ledger/) solutions aim to offer cheaper data publishing without sacrificing security.

**Compression** — Zstd, Brotli, and custom rollup-specific compression can squeeze transaction data into fewer bytes.

**Encryption and redaction** — Partial rollups that only post what is needed (not the full transaction) for fraud-proof purposes.

**Proof recursion** — Recursively stacking proofs (a proof of a proof) so that final verification on Layer 1 is tiny.

None of these eliminate the cost; they optimize it. As long as rollups anchor to Ethereum for security, there is a floor below which cost cannot fall.

## See also

<div class="wiki-seealso">

### Closely related

- [Distributed ledger](/distributed-ledger/) — Consensus and data storage in decentralized networks
- [Smart contract](/smart-contract/) — Programmable transactions on blockchains
- [Proof of stake](/proof-of-stake/) — Consensus mechanism based on asset locking
- [Proof of work](/proof-of-work/) — Consensus mechanism based on computational effort
- [Ethereum](/ethereum/) — The primary blockchain platform for rollups

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — Core concepts of decentralized ledgers
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Platforms for trading digital assets
- [Bitcoin](/bitcoin/) — The original decentralized ledger
- [Market maker trading](/market-maker-trading/) — How liquidity is provided in decentralized systems

</div>

---
title: "Rollup Transaction Fees Explained"
description: "How users on optimistic and ZK rollups pay fees, including the split between L2 execution cost and L1 data-posting cost."
keywords:
  - rollup transaction fees
  - how do rollup transaction fees work
  - optimistic rollup fees
  - zk rollup fees
image: "/svg/crypto.svg"
---

*On **rollup** [blockchains](/blockchain-fundamentals/), transaction fees consist of two distinct components: the cost to execute the transaction on Layer 2 and the cost to post compressed transaction data to Layer 1 (Ethereum or another chain). Understanding this split is key to predicting fees during network congestion and comparing different rollup designs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rollup Transaction Fees — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Fees split between L2 execution and L1 data posting; L1 cost dominates in times of congestion.</div>

|   |   |
|---|---|
| **Total fee** | L2 execution cost + L1 data-posting cost (calldata or blob) |
| **L2 execution** | Small; depends on computation (smart contract logic, storage reads) |
| **L1 data cost** | Largest component; depends on transaction size and Ethereum gas price |
| **Fee ordering** | Typical: 1–10% execution, 90–99% data posting during normal conditions |
| **Blob impact (EIP-4844)** | Reduces data-posting cost by 10–100x by separating blob gas from calldata gas |
| **Fee variability** | Spikes when Ethereum is congested; minimal when Ethereum is quiet |
| **User perspective** | Fee is quoted in ETH or USD; breakdown usually hidden in wallet |

</aside>

## The Two-Part Fee Structure

Unlike Ethereum or Bitcoin, where all computation and storage is on-chain, rollups outsource execution to a second layer and post only a compressed summary (or proof) to Layer 1. This design reduces fees because:

1. **Execution is cheaper on L2.** Rollup sequencers process transactions locally with less validation overhead than Ethereum.
2. **Compression saves L1 space.** Instead of posting every transaction in full, the rollup batches thousands of transactions and compresses them into a few kilobytes.

But this requires splitting the fee:

**Rollup Fee = L2 Execution Cost + L1 Data-Posting Cost**

### L2 Execution Cost

The L2 execution cost covers the resources the rollup sequencer uses to process your transaction:
- **CPU:** Running the transaction logic (e.g., a smart contract call, token transfer).
- **Memory:** Storing temporary state during execution.
- **Storage:** Writing permanent data (account balances, contract state).

This cost is typically **tiny**—far cheaper than Ethereum. A simple token transfer might cost 10–100 wei on Arbitrum or Optimism, compared to thousands or millions on Ethereum itself. Rollup sequencers have low overhead because they trust each other; they don't replicate computation across thousands of nodes.

L2 execution costs are set by rollup **sequencers** (operators who bundle transactions) and follow basic supply-demand rules. If the rollup is congested and users bid higher for priority, the execution fee rises. If it's quiet, fees drop to near-zero.

### L1 Data-Posting Cost

The L1 data-posting cost is the larger component and depends directly on **Ethereum network conditions**.

Each rollup must post proof of its transactions on Ethereum so that:
- **Optimistic rollups** can be monitored for fraud (anyone can challenge an invalid batch).
- **ZK rollups** can be verified cryptographically (a proof attests all transactions are valid).

When posting data, the rollup compresses thousands of transactions into a single batch and submits it as a transaction on Ethereum. That batch transaction consumes **calldata** (in older systems) or **blob space** (post-EIP-4844), and the cost depends on:
- **Batch size:** Larger batches = more data, higher cost.
- **Ethereum gas price:** When Ethereum is busy, gas spikes, and posting costs soar.

A typical Optimism batch might compress 1,000–5,000 transactions into 20–100 KB. If Ethereum gas is 50 Gwei and calldata costs 16 gas per byte:
- Batch cost = 80 KB × 16 gas/byte × 50 Gwei = ~64 ETH (or ~$150,000)
- Per transaction = 64 ETH / 3,000 transactions = ~0.02 ETH (~$50)

This per-transaction data cost dominates the user's fee, often representing 90%+ of total cost when Ethereum is congested.

## Optimistic Rollups vs. ZK Rollups: Fee Implications

### Optimistic Rollups (Arbitrum, Optimism)

Optimistic rollups post raw transaction data on Ethereum, which sequencers can later use to reconstruct the rollup state. The data itself must be readable; it is calldata or blobs.

**Fee structure:**
- L2 execution: minimal (1–10%)
- L1 data posting: dominant (90–99%)

The data cost scales with **transaction size**. A complex contract interaction that writes many state variables results in more calldata and higher fees.

### ZK Rollups (Starknet, zkSync, Polygon Hermez)

ZK rollups post a zero-knowledge proof instead of raw data. The proof is small (a few hundred bytes) and cryptographically verifies all transactions were valid, so the rollup doesn't need to post raw transaction data.

**Fee structure:**
- L2 execution: includes proof-generation cost
- L1 data posting: much smaller (no raw transaction data needed)

Because ZK rollups post far less data, their L1 data costs are typically **lower**. However, they offload **proof-generation cost** to the L2 execution component, so the actual per-transaction fee may not be dramatically cheaper. But ZK rollups avoid the data-posting spike when Ethereum is congested, since they post small proofs regardless.

## How Ethereum Congestion Affects Rollup Fees

The critical insight: **rollup fees move with Ethereum gas prices.**

When Ethereum is quiet (low congestion):
- Optimistic rollup fees: ~$0.10–$1 per transaction.
- ZK rollup fees: ~$0.05–$0.50 per transaction.
- L1 data cost is low relative to L2 execution.

When Ethereum is congested (high gas):
- Optimistic rollup fees: ~$5–$50 per transaction.
- ZK rollup fees: ~$1–$10 per transaction (still proportionally lower).
- L1 data cost spikes; it dominates the total fee.

During the 2021 Ethereum fee crisis (gas reaching 500+ Gwei), even rollup transactions cost dollars. During quiet periods, rollup fees are cents or less.

This is why rollup users are highly sensitive to **Ethereum network activity**. If Ethereum itself is being hammered by a popular mint or exchange bug, rollup users feel the pain even though they're not transacting on Ethereum.

## EIP-4844 (Dencun Upgrade): The Fee Improvement

In March 2024, Ethereum implemented **EIP-4844**, which introduced a new transaction type called "blobs" (Binary Large Objects). Blobs are data that live on Ethereum only temporarily (not permanently in the blockchain history), so they are cheaper to post than calldata.

**Impact on rollups:**
- **Before EIP-4844:** Rollup data cost 16 gas per byte of calldata.
- **After EIP-4844:** Rollup data cost ~0.3–1 gas per blob byte (a ~10–50x reduction).

Rollups that switched to blobs (Optimism, Arbitrum) saw fees drop sharply overnight. The L1 data cost component fell from dominating fees to becoming negligible even during moderate Ethereum congestion.

However, the fee improvement is temporary. As blob space fills (if adoption accelerates), blob gas prices will rise. Eventually, blob pricing may equilibrate with calldata pricing, eliminating the fee advantage.

## Fee Breakdown Example

Here's a worked example for an Optimism transaction during moderate Ethereum congestion:

| Component | Cost |
|-----------|------|
| L2 execution (token swap) | 0.0001 ETH (~$0.25) |
| L1 data posting (per-tx share of batch) | 0.0004 ETH (~$1.00) |
| **Total fee** | **0.0005 ETH (~$1.25)** |
| **Breakdown** | 20% execution, 80% data posting |

If Ethereum gas rises 5x (to 250 Gwei):
| Component | Cost |
|-----------|------|
| L2 execution (unchanged) | 0.0001 ETH (~$0.25) |
| L1 data posting (5x higher) | 0.002 ETH (~$5.00) |
| **Total fee** | **0.0021 ETH (~$5.25)** |
| **Breakdown** | 5% execution, 95% data posting |

Notice: L2 execution remained flat; the fee spike is entirely due to Ethereum gas.

## User Experience and Fee Quotes

Most rollup wallets and explorers hide this complexity and simply show a single **estimated fee** in ETH or USD. But understanding the split helps explain why:
- Fees spike when Ethereum is congested, even if the rollup sequencer is not.
- Complex transactions (which generate more calldata) cost slightly more.
- ZK rollups might have lower fee floors but not always much lower average fees.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Core architecture and transaction processing
- [Proof-of-Stake](/proof-of-stake/) — Consensus mechanism used by Ethereum and rollup finality
- [Hash Rate](/hash-rate/) — Block production and validation overhead
- [Distributed Ledger](/distributed-ledger/) — Technology underlying blockchains and rollups
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where users convert rollup assets to fiat

### Wider context

- [Bitcoin](/bitcoin/) — Comparison: Bitcoin has single-chain fees, no rollups
- [Ethereum](/ethereum/) — Layer 1 that rollups post to
- Scalability trade-offs — Rollups sacrifice decentralization/security slightly for throughput

</div>

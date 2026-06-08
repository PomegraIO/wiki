---
title: "Proof of Publication in Blockchain Scaling"
description: "Proof of publication blockchain data availability guarantees rollups can post transactions and recover state. Learn why broadcast ≠ storage."
keywords:
  - proof of publication blockchain
  - data availability scaling
  - blockchain rollup data
  - optimistic rollup sequencing
image: /svg/crypto.svg
---

*A **proof of publication** is the guarantee that transaction data was broadcast and available on-chain at block time, even if no one is storing it permanently. This concept is foundational to rollups: without proof that the sequencer published rollup transactions to the base layer, users cannot prove what state should be, and the entire scaling solution collapses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proof of Publication — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain scaling." />

<div class="wiki-infobox-caption">The base layer's ability to verify that rollup data was published separates recoverable scaling from black-box sequencing.</div>

|   |   |
|---|---|
| **What it is** | Cryptographic or structural proof that data was available for reading at a past block height |
| **Why it matters** | Allows rollups to be trustless: users can always reconstruct the rollup state from base-layer history |
| **Not the same as** | Data storage, archival, or long-term availability; proof of publication is ephemeral |
| **Enforced by** | Base-layer full nodes and light clients that verify inclusion or commitment proofs |
| **At risk when** | Data becomes unavailable *after* publication (the "data withholding" problem) |

</aside>

## Why Broadcast Is Not the Same as Storage

A common point of confusion: if data is "on-chain," does that mean it is stored forever? No. Every Ethereum node needs hard-drive space, and not every node retains the full history. Bitcoin nodes that have pruned old blocks have verified the history was valid but no longer store the actual transaction bytes.

Proof of publication asks a simpler question: *Did this data exist and was it readable at block time?* That is all a rollup needs to maintain trustlessness. A rollup sequencer publishes compressed transaction data (a batch or blob) to the base layer. Full nodes process that data, verify signatures and state roots, and then may discard it. As long as the data *was* available when published, any participant can later fetch it from archive nodes or reconstruct it from a fraud proof.

This is why rollups differ fundamentally from sidechains or centralized sequencers. A sidechain has no proof of publication to a settlement layer—its validators could agree on state without ever telling the base chain. A rollup is only safe because the base chain records and validates the data stream.

## The Problem Proof of Publication Solves

Imagine a rollup sequencer receives thousands of transactions, orders them, compresses them into a batch, and publishes a hash of that batch to Ethereum. The sequencer claims: "Here is my batch. I've posted the commitment. Process it." If Ethereum has no way to verify the batch existed, it has no way to force the sequencer to be honest about what transactions were included or what the resulting state is.

If the sequencer withholds the actual data after publishing the commitment, users cannot:

- Prove which transactions were included or excluded
- Detect censorship
- Withdraw funds or exit to the base layer
- Reconstruct the rollup state independently

Proof of publication solves this by requiring the sequencer to broadcast the full (or compressed) data to the base layer. Ethereum nodes must be able to access it, verify the commitment matches, and either store it for a period or verify a proof that it was available.

In older designs, proof of publication was achieved by posting raw calldata to Ethereum—expensive but transparent. Modern designs use rollup-specific commitments or zero-knowledge proofs, all aimed at proving the data was published without forcing every node to store gigabytes.

## Publication, Not Availability

A critical distinction: proof of publication says "the data *was* there." It does not guarantee the data remains available indefinitely. Once Ethereum nodes have validated a blob and moved it to archival tier, the base chain has done its job. Rollup nodes must store the rollup history themselves—or rely on archive services—to stay in sync.

This is where **data availability sampling** enters the picture. A base-layer light client cannot download an entire blob; it would be too expensive. Instead, it randomly samples small chunks of the data, verifies them against a cryptographic commitment (like a polynomial evaluation), and concludes with high confidence that the full data exists. This allows even light clients to verify proof of publication without becoming full nodes.

## Why Rollups Depend on It

Optimistic rollups, like Optimism or Arbitrum, work like this:

1. Sequencer receives transactions.
2. Sequencer publishes them (as calldata, blobs, or commitments) to the base layer.
3. Sequencer proposes a state root update.
4. If a challenger disagrees, they reference the published data to prove the sequencer lied.

If the data were never published, the challenger has nothing to reference. They cannot construct proof of fraud. The sequencer's lie stands.

Zero-knowledge rollups also depend on proof of publication. The prover generates a ZK proof that a set of transactions, when applied to the old state, produce the new state. But the base layer has no way to know if the prover included only the transactions the sequencer intended, or if they cherry-picked, censored, or fabricated some. By requiring the sequencer to publish the transaction list, the base layer can force the prover to prove against *that exact set*, preventing censorship.

## How Base Layers Enforce It

Ethereum enforces proof of publication through transaction inclusion: the sequencer pays fees to post data to the blockchain. The network reaches consensus on the canonical chain, including that data. Any node replaying the chain from genesis will process that data as real.

For **calldata**, this is straightforward—the data is part of the transaction and every node sees it.

For **EIP-4844 blobs**, Ethereum nodes do not store blobs forever, but they validate the blob's commitment against the transaction header. Light clients can verify the blob was included without downloading all of it, using data availability sampling.

Other chains use **validity proofs** where the sequencer must provide a proof of correct execution *against published input data*. The proof itself proves the data was available and correctly interpreted.

## The Economics of Publication

Publishing costs money. On Ethereum, calldata is expensive; blobs are cheaper than calldata but costlier than storage. Rollup operators optimize by compressing transactions: instead of posting 100 transactions of 100 bytes each, they post a single batch commitment and rely on the assumption that, if anyone needs to dispute the state, they can recover the original transactions from off-chain sources (full rollup nodes or archive services).

This creates a risk: if *no one* stores the rollup data and the sequencer disappears, users may be unable to exit. Some rollups mitigate this by requiring operators to store data for a period (e.g., 7 days) or by delegating storage to decentralized networks or specialized data-availability chains.

## See also

<div class="wiki-seealso">

### Closely related

- [ZK-EVM Compatibility Types Explained](/zk-evm-compatibility-types/) — ZK rollups and their approach to data availability
- [Modular Data Availability: How Celestia-Style Chains Work](/celestia-modular-data-availability/) — Dedicated chains for proof of publication
- [Blockchain fundamentals](/blockchain-fundamentals/) — Consensus and data model
- [Distributed ledger](/distributed-ledger/) — Foundation for blockchain design

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where blockchain tokens trade
- [Bitcoin](/bitcoin/) — Original blockchain design

</div>

---
title: "Modular Data Availability: How Celestia-Style Chains Work"
description: "Modular data availability chains like Celestia separate data ordering from execution. Learn how rollups benefit from outsourcing publishing to a dedicated chain."
keywords:
  - modular data availability chain
  - celestia data availability
  - rollup execution separation
  - data ordering blockchain
image: /svg/crypto.svg
---

*A **modular data availability** (DA) chain is a blockchain built specifically to order and publish transaction data without executing it. Rollups and other light clients use it to prove that sequencer data was broadcast and available, decoupling the cost and complexity of settlement from the cost and complexity of execution. Celestia is the flagship example.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Modular Data Availability — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for modular blockchain design." />

<div class="wiki-infobox-caption">Instead of one chain doing execution, settlement, and data ordering, a DA chain handles ordering and publication while rollups handle only execution.</div>

|   |   |
|---|---|
| **Purpose** | Provide [proof of publication](/proof-of-publication-blockchain/) cheaply and reliably |
| **What it does** | Orders transactions and publishes them via data-availability sampling |
| **What it does NOT do** | Execute transactions or validate state machines |
| **Rollup benefit** | Cheaper than posting to Ethereum; decoupled from execution bloat |
| **Sampling mechanism** | Light clients randomly verify chunks of block data without downloading all of it |
| **Examples** | Celestia, Avail, EigenDA |

</aside>

## The Monolithic vs. Modular Split

For most of blockchain history, a single chain did everything: order transactions, execute them, store them, and settle disputes. Bitcoin and Ethereum are monolithic. A node must run all four functions to stay in sync.

This works, but it is expensive. If you are a light client (like a mobile wallet), you must still verify every transaction header and sample enough data to catch a censoring validator. If you are a rollup, you must pay Ethereum gas to post your compressed transactions as calldata or blobs, which costs money because you are competing with everyone else for block space.

A **modular** architecture splits these functions:

- **Data availability layer:** Handles ordering and publishing; makes data publicly available.
- **Execution layer:** Runs transactions, updates state, validates signatures.
- **Settlement layer:** Anchors the execution to finality, resolves disputes.

Celestia-style systems focus on the data-availability piece. They are pure DA layers: they accept data from users (rollups, light clients), order it into blocks, and make it available. They do not care what the data means. A rollup executing on Celestia does not need Celestia's validators to understand EVM bytecode or contract state. Celestia simply guarantees: "This data was here at block time."

## How Modular DA Layers Work

A traditional blockchain validator must:

1. Download the full block.
2. Execute every transaction.
3. Verify signatures and state transitions.
4. Vote on the canonical chain.

A Celestia validator also downloads and verifies blocks, but the verification is simpler: instead of checking execution correctness, they check **data availability**. Did the proposer actually publish the claimed block data? This is verified via **data-availability sampling** (DAS).

### Data-Availability Sampling

A Celestia light client does not download the full block. Instead:

1. It downloads block headers (tiny, ~1 KB).
2. It randomly samples small chunks of the block's data.
3. It verifies that sampled chunks match the header's cryptographic commitment (typically a 2D Reed-Solomon code or Merkle tree).
4. It repeats sampling hundreds of times.

If a block is, say, 100 MB and a light client samples 1% of it, the light client can be highly confident (99.9%+) that the full block is available. If the proposer tried to hide data (a "data withholding attack"), the light client would catch it when a sample fails to match the commitment.

This is the key innovation: light clients and rollups can verify data availability *without downloading the full block*, making the DA layer very efficient.

## Why Rollups Use Modular DA

A rollup sequencer must post transaction data somewhere so that users can:

- Verify the rollup state.
- Exit to the base layer.
- Dispute invalid state roots.

Historically, rollups posted to Ethereum. Ethereum calldata costs ~16 gas per byte (expensive), and blob space is ~1 gas per byte (cheaper, but still competes with other Ethereum users). A rollup handling 1,000 TPS might spend millions per day just on data posting.

With a modular DA layer like Celestia:

- The rollup pays Celestia's fees, which are much lower because Celestia validators do not execute transactions.
- The rollup does not compete with Ethereum users; Celestia is a separate, purpose-built chain.
- The rollup can choose its DA layer independently of settlement (it might settle disputes on Ethereum but post data to Celestia).

This is the **economic decoupling** that modular systems provide.

## Modular vs. Monolithic Trade-offs

**Monolithic (e.g., Ethereum):**
- Single validator set, shared consensus.
- Tightly coupled: execution cost directly affects data availability cost.
- One rule set for all; hard to specialize.

**Modular (e.g., Celestia + Rollups):**
- Separate validator sets, separate consensus.
- Decoupled: rollup can use any DA layer, any settlement layer.
- Each layer optimizes for its job (DA for throughput, rollup for latency, settlement for finality).

The downside: more complexity. A rollup now depends on two separate chains' liveness. If Celestia goes down, the rollup cannot post data (though it can continue executing locally). Interop between rollups on different DA layers requires bridging, which is not free.

Also, a modular stack requires more cryptographic assumptions. A rollup on Celestia must trust both Celestia's DA and Ethereum's settlement. A monolithic chain requires trust in one validator set.

## Variations: DA Committees and Validiums

Not all DA layers are chains. Some rollups use **DA committees:** a set of validators (or a threshold subset) who commit to storing data. If they fail to provide data on demand, users can slash them. This is cheaper than a full chain but riskier (fewer parties, higher collusion risk).

**Validiums** go further: they post a commitment to data (a hash) without publishing data on-chain at all. Data is stored off-chain by operators. Validiums are even cheaper but require more trust in the operators.

Celestia-style public DA chains sit in the middle: they have the security of a full blockchain (distributed validator set, cryptographic proof) but the efficiency of specialized design.

## Examples and Ecosystem

**Celestia:** Purpose-built DA chain with DAS, modular settlement. Rollups (like Rollkit) can deploy to Celestia easily. Settlement typically happens on Ethereum via bridge validators.

**Avail:** Another DA blockchain with similar goals, developed by Polygon.

**EigenDA:** Ethereum-based DA service where Ethereum restakers provide DA guarantees. Settles disputes on Ethereum itself.

**Ethereum itself (post-EIP-4844):** With blobs, Ethereum is partially playing the role of a DA layer for rollups, though it still executes all transactions monolithically.

## The Ecosystem Constraint

Modular designs introduce a new constraint: **where does your settlement happen?** A rollup can post data to Celestia, but it must settle disputes or finalize state on some chain. Often this is Ethereum (for security), but it could be another DA chain, or even an application-specific chain.

This creates a form of **fragmentation**: a rollup on Celestia + Ethereum settlement is not directly compatible with a rollup on Celestia + Avail settlement, even though both use Celestia for DA.

Protocols like **Interop DA** and **IBCs** (inter-blockchain communication) aim to bridge this gap, but they add more complexity and latency.

## Conclusion: Specialization vs. Cohesion

The modular thesis is that blockchains should specialize: one layer for DA, another for execution, another for settlement. This allows each to optimize independently and reduces costs.

The cost: more moving parts, longer finality, and coordination complexity.

Whether modular systems ultimately offer better economics than monolithic chains—or whether the complexity negates the savings—remains an open question that the market is actively testing.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Publication in Blockchain Scaling](/proof-of-publication-blockchain/) — How DA layers guarantee data was published
- [ZK-EVM Compatibility Types Explained](/zk-evm-compatibility-types/) — ZK rollups using modular DA
- [Blockchain fundamentals](/blockchain-fundamentals/) — Consensus and validators
- [Distributed ledger](/distributed-ledger/) — Foundation for blockchain design

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Tokens from DA-layer ecosystems
- [Bitcoin](/bitcoin/) — Early monolithic design

</div>

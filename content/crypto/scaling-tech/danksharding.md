---
title: "Danksharding"
description: "Ethereum's full sharding design that separates data availability from execution, using proposer-builder separation and attester sampling."
keywords:
  - ethereum sharding
  - data availability
  - proposer-builder separation
  - consensus scaling
  - execution sharding
image: "/svg/crypto.svg"
---

*A **Danksharding** is Ethereum's proposed full sharding architecture that decouples data availability from execution validation. Validators sample random subsets of sharded data, allowing the network to guarantee data is available without requiring every node to download everything.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Danksharding — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain scalability design." />

<div class="wiki-infobox-caption">Sharding that scales data availability independently from execution.</div>

|   |   |
|---|---|
| **What it is** | A consensus-layer scaling design that partitions data and uses probabilistic sampling to guarantee availability |
| **Key innovation** | Separates data propagation from execution verification |
| **Data guarantee** | Attester sampling provides cryptographic proof data is retrievable without all-or-nothing fallback |
| **Predecessor** | [Proto-Danksharding](/proto-danksharding/) (EIP-4844) introduced the blob mechanism |
| **Validator role** | Attest to random subsets of data; honest majority ensures all data is covered |
| **Also called** | Full danksharding, execution sharding (when paired with execution) |

</aside>

## The core insight: separate data from computation

Traditional blockchain designs bind data availability to transaction validation. Every validator verifies the entire block and holds the full ledger. This creates a bottleneck: throughput is capped by what a single validator can compute and store.

Danksharding inverts the relationship. Instead of "verify execution to prove data is available," it asks: "prove data is available independently, and trust execution follows." This decoupling allows the network to commit to *far more data* than it can fully compute or store redundantly.

The mechanism uses **attester sampling**. Rather than requiring all validators to download all data, a small random subset of validators attests to each chunk of data. If an honest majority are online, then with overwhelming probability, *someone* has every chunk. Data is proven available without universal replication.

## How sampling works in practice

Ethereum's Danksharding uses a 2D array of data. Blobs are arranged in rows and columns; validators randomly sample cells. If an attacker withholds a single cell, an honest sampler will detect its absence and trigger a fallback. The number of samples needed grows logarithmically with the number of validators, not linearly with data size.

This is mathematically elegant but operationally strict: validators must be online and responsive during the sampling window, typically a single slot (~12 seconds). Missing attesters reduce safety guarantees; offline validators are penalised.

## Proposer-builder separation

Danksharding pairs with proposer-builder separation (PBS). A **proposer** (validator) creates a block header; a **builder** (often a sophisticated relay or MEV-aware actor) constructs the actual data and proof. This division allows builders to specialise in data packing efficiency while proposers focus on consensus participation.

Without PBS, every validator would need to be a competent data packer. With PBS, the network automatically routes data-packing work to those best equipped to do it. The builder's incentive is to maximise MEV extraction; as a side effect, they optimise data density.

## Relationship to proto-Danksharding

[Proto-Danksharding](/proto-danksharding/) (EIP-4844) was Ethereum's 2023 upgrade introducing blob-carrying transactions. Blobs are data-only; they do not execute. Proto-Danksharding is the *interim* design: data is still distributed to all validators, but execution and data handling are decoupled in the protocol.

Full Danksharding removes the "all validators download blobs" requirement. Only a random sample attests; the rest can safely skip the download. This is a significant further scaling boost.

## Why data availability matters

A blockchain is only useful if data can be retrieved. Without it, users cannot verify state or rebuild the chain. An attacker could convince a light client that a transaction occurred, then later reveal that the data supporting it never existed.

Danksharding guarantees data availability through math, not altruism. Sampling is theoretically sound: if an attacker withholds data, the sampling process will eventually detect it. Ethereum can thus commit to *gigabytes* of data per slot, far beyond what individual validators store.

## Execution shards and future plans

Early Danksharding plans included **execution shards**: different validators would execute different parts of the state tree in parallel. This would multiply throughput further. The current design focuses on data sharding first; execution sharding is deferred or deprioritised.

The reason: execution sharding is operationally harder. Validators must coordinate state proofs across shards, manage cross-shard messaging, and handle shared storage. Data sharding requires only probabilistic honesty from samplers—a simpler safety model.

## Practical implications for users

For most users, Danksharding is transparent. They send transactions; rollups or other layer 2 systems batch them, pay for blob space, and post compressed proofs onchain. The user benefits through lower fees and higher throughput, but the underlying sampling is invisible.

For node operators, the shift is significant but manageable. Running a full node no longer requires downloading all data; you can sample and attest selectively. This lowers barriers to becoming a validator.

## Challenges and open questions

Sampling introduces liveness requirements. If attesters are offline, data availability guarantees degrade. Network conditions, geography, and coordinated outages could impair safety during critical windows.

Also, Danksharding assumes reasonably sized data blobs. If individual blobs exceed network propagation latency, sampling breaks down—attesters cannot verify data they cannot download quickly. Ethereum's design targets ~128 KB blobs per slot, balancing throughput and propagation time.

## See also

<div class="wiki-seealso">

### Closely related

- [Proto-Danksharding](/proto-danksharding/) — EIP-4844, the interim stepping stone before full Danksharding
- [Recursive SNARK](/recursive-snark/) — proof composition used to verify batched data and execution
- Rollup — layer 2 systems that benefit from cheap blob space
- Attestation — validator commitment to data availability and block validity
- Proposer-Builder Separation — the architectural pattern enabling specialist data packing

### Wider context

- Layer 2 — scaling solutions leveraging Danksharding's data availability
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the consensus and throughput model Danksharding scales
- [Ethereum](/ethereum/) — the blockchain implementing Danksharding

</div>

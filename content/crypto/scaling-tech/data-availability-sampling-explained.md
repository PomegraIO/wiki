---
title: "Data Availability Sampling Explained"
description: "Data availability sampling explained: how light nodes verify block data is available without full download, enabling blockchain scaling."
keywords:
  - data availability sampling explained
  - das blockchain light nodes
  - ethereum data availability
  - light client verification
image: /svg/crypto.svg
---

*A light node running on a smartphone cannot download and verify every piece of transaction data on a blockchain—that would require the bandwidth and storage of a full node. **Data availability sampling** (DAS) solves this by having light nodes randomly request small chunks of block data from the network. If enough samples return successfully, the light node can probabilistically confirm the block data is available, without downloading the full block. This enables rollups and other scaling solutions to post more data on-chain without forcing all validators to be high-powered servers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Data Availability Sampling — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency technology." />

<div class="wiki-infobox-caption">A probabilistic technique for light nodes to verify block data availability without full download.</div>

|   |   |
|---|---|
| **Purpose** | Verify data is available without downloading entire block |
| **Who benefits** | Light nodes, mobile clients, layer 2 rollups |
| **Mechanism** | Random sampling of block chunks + erasure coding |
| **Trade-off** | Probabilistic proof vs. deterministic verification |
| **Scalability impact** | Allows larger blocks while maintaining light-client viability |
| **Current use** | Proposed for Ethereum; live on some layer 2s |

</aside>

## The data availability problem

A blockchain's security relies on the ability for any participant to verify the chain's state. In practice, a full node downloads every transaction, computes the state after each block, and checks that all rules are followed. This is safe but expensive: a full node needs substantial bandwidth and storage.

Light nodes, typically run on phones or in browsers, cannot afford this. They instead download only block headers (a few hundred bytes per block) and trust that the network is honest. But this introduces a vulnerability: what if a block producer publishes a header but withholds the actual transaction data? Users relying on the header would not know they are victims of fraud, because they cannot verify that the transactions claimed in the header actually exist.

This is the data availability problem. A light node needs assurance that the data behind a header has been published to the network, without downloading the gigabytes of data.

## How data availability sampling works

DAS uses **erasure coding** to split block data into many redundant pieces. If the original block is 1 MB, erasure coding might create 4 MB of coded data—enough so that possessing any half of the coded pieces allows reconstruction of the original block. This is called 2x redundancy.

A light node then samples a small, random subset of these coded pieces from the network. If it successfully retrieves, say, 30 samples out of 100 possible pieces, and the samples are randomly distributed across the coded data, the light node can conclude with high probability that the full block data is available on the network.

Here is the key insight: the light node does not need to download half the block (which would defeat the purpose of being light). Instead, it downloads perhaps 1–2% of the total encoded data in small samples. If even one honest node holds the full data, the light node will find some samples. If an attacker tries to suppress the data by controlling a portion of the network, the probability that all light-node samples fail is exponentially low—making suppression economically impractical.

## Why erasure coding is necessary

Without erasure coding, data availability sampling would not work. Consider a naive approach: split the block into 100 pieces, and have light nodes sample a few. If an attacker controls 50% of the network and withholds their half of the pieces, a light node sampling randomly would miss those pieces and falsely conclude data is unavailable.

Erasure coding solves this. If 100 pieces of encoded data can reconstruct the original, then an attacker must control at least 50% of the 100 pieces to prevent reconstruction. But the light node's samples are distributed across all 100, so the attacker cannot hide their withholding selectively—to suppress data, they must suppress across many pieces, making detection obvious.

In practice, the threshold is set so that light nodes need only 25–40% of the encoded data for high confidence. If an attacker controls more than the redundancy threshold, the chain assumes data is unavailable and rejects the block. If they control less, the light node's samples will eventually hit available pieces.

## Connection to rollup scaling

Data availability sampling is a key enabler for layer-2 scaling. Optimistic and ZK rollups post compressed transaction data to Ethereum. If that data is large, the cost of posting it increases, and throughput is limited by how much data fits in each Ethereum block.

If Ethereum mainnet deployed DAS, block producers could include larger amounts of rollup data without requiring every validator to download it in full. Validators would use DAS to verify the data is available; light nodes would do the same. The rollup data could grow, but the burden on validators and light clients would stay manageable.

Projects like Celestia were designed around DAS from the start, offering a "data availability layer" that rollups can use instead of posting directly to Ethereum. This unbundles the validator role into two: consensus providers (who order blocks) and data providers (who store data and respond to DAS requests).

## Trade-off: probabilistic vs. deterministic

There is a subtle but important difference. A full node downloading a block knows with certainty that the data exists and is correct. A light node using DAS only has probabilistic confidence—with each sample, the probability of false confidence decreases exponentially.

However, for practical purposes, this is acceptable. If a light node requests 40 samples and all succeed, the chance that an attacker is suppressing data is less than 2^-40, or roughly one in a trillion. This is lower than the risk of a consensus-layer attack or a deep blockchain reorganization.

Projects have tuned DAS parameters (number of samples, redundancy factor) to balance light-node bandwidth against confidence levels. Most proposals target a light node needing only 10–50 MB of bandwidth per block, versus potentially 100+ MB for a light node using other weak-verification methods.

## Challenges in deployment

Implementing DAS on Ethereum mainnet requires consensus-layer changes, since nodes must coordinate on which block contains how much encoded data. The Ethereum protocol would need to specify erasure-coding parameters, and full nodes would need to reconstruct and serve sampled pieces on demand.

Additionally, there is a risk of denial-of-service attacks. An attacker could query thousands of light nodes with requests for DAS samples, consuming their bandwidth. Defenses include rate-limiting and reputation systems, but these add complexity.

Another concern is the "magic number" problem: if an attacker controls enough of the network infrastructure, they can suppress samples without triggering the consensus-layer alarm. DAS relies on a fairly distributed node and peer-to-peer network; if network connectivity is highly concentrated, the guarantees weaken.

Despite these challenges, the Ethereum Foundation has explored DAS as part of its scaling roadmap, and the technique is already live in some layer-2 systems and data availability layers.

## Current and future adoption

As of mid-2026, DAS is primarily used by layer-2 projects and standalone data availability chains. Ethereum mainnet has not yet integrated it, though research into 2D sampling (a refinement that handles both row and column data) is ongoing. The technique is increasingly seen as essential for blockchain scalability without requiring all participants to become data-center operators.

The transition from theory to practice is gradual, driven by the need for light clients to scale alongside growing block sizes.

## See also

<div class="wiki-seealso">

### Closely related

- [ZK Rollup vs Optimistic Rollup: Key Differences](/zk-rollup-vs-optimistic-rollup-comparison/) — scaling solutions that benefit from DAS
- [Cross-Rollup Message Passing](/cross-rollup-message-passing/) — bridging between rollups
- [Ethereum Gas Limit and Its Role in Scaling](/ethereum-gas-limit-scaling/) — foundational block size constraints
- [Distributed Ledger](/distributed-ledger/) — how data is distributed across nodes

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — introduction to consensus and validation
- [Proof of Stake](/proof-of-stake/) — Ethereum's consensus mechanism
- [Smart contracts](/smart-contract/) — applications using DAS-enabled data

</div>

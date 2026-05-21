---
title: "Solana"
description: "Solana is a high-throughput blockchain designed to process transactions rapidly through parallel transaction processing and a proof-of-history consensus mechanism. It prioritises speed over decentralisation."
keywords:
  - solana
  - sol
  - blockchain
  - high-throughput
  - proof-of-history
  - validator
image: "https://picsum.photos/seed/solana/900/600"
---

*A **Solana** (**SOL**) is a [blockchain](/blockchain-fundamentals) platform and cryptocurrency engineered for maximum transaction throughput. It uses **proof-of-history** — a novel consensus innovation — combined with parallel transaction processing to achieve thousands of transactions per second, prioritising speed and low fees over strict decentralisation.*

<div class="wiki-hatnote">

This entry covers the Solana network and its cryptocurrency. For similar high-throughput platforms, see [Avalanche](/avalanche), [Polygon](/polygon), or [Arbitrum](/arbitrum); for Ethereum-compatible alternatives, see layer-2.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Solana — key facts</div>

<img src="https://picsum.photos/seed/solana/900/600" alt="Solana logo and transaction flow" />

<div class="wiki-infobox-caption">Solana: engineered for extreme transaction throughput.</div>

|   |   |
|---|---|
| **What it is** | A high-throughput blockchain platform |
| **Native currency** | Sol (SOL) |
| **Created** | 2020 |
| **Founder** | Anatoly Yakovenko |
| **Consensus mechanism** | Proof-of-history + [proof-of-stake](/proof-of-stake) |
| **Target throughput** | 65,000+ transactions per second |
| **Practical throughput** | 1,000–4,000 TPS (as of 2024) |
| **Block time** | ~400 milliseconds |
| **Validator count** | ~1,000 active validators |

</aside>

## Origins and vision

Anatoly Yakovenko created Solana to solve a fundamental problem: How can a blockchain achieve both decentralisation and high throughput? [Bitcoin](/bitcoin) and [Ethereum](/ethereum) favour decentralisation and security; Solana made speed the primary goal, accepting some decentralisation trade-offs.

The network launched in March 2020. Yakovenko's key insight was **proof-of-history** — instead of nodes independently verifying when transactions occurred, a designated leader (the block producer) creates a historical record, cryptographically proving the sequence and timing of transactions. This removes a major source of delay in consensus.

## Proof-of-history

Proof-of-history is not a consensus mechanism itself but rather a clock — a way to prove that data existed at a specific time and in a specific order. Combined with [proof-of-stake](/proof-of-stake) for validator selection, it creates a highly efficient consensus model.

A validator broadcasts transactions in a block, along with a hash that incorporates all previous transactions plus a timestamp. This hash serves as cryptographic proof of the ordering and timing. The next validator must build atop this proof, creating an unbreakable chain of history.

This innovation allows Solana to avoid the expensive consensus rounds required by [Ethereum](/ethereum)'s design, dramatically increasing throughput.

## Parallel transaction processing

Solana's second innovation is **Sealevel**, a runtime that processes transactions in parallel. Most blockchains are forced to execute transactions sequentially to avoid conflicts; Sealevel identifies which accounts (addresses) each transaction touches and processes non-conflicting transactions concurrently on separate CPU threads.

This is theoretically sound — two transfers between different accounts do not conflict and can execute simultaneously. In practice, however, Sealevel's benefits are limited by the number of CPU cores available, and many real-world transactions do interact, limiting parallelism.

## Network topology and centralisation concerns

Solana's validators require high-end hardware to keep up with the fast block time (400 milliseconds). This creates a hardware barrier to entry, reducing the number of nodes that can profitably validate. As of 2024, roughly 1,000 validators participate in consensus — significantly fewer than [Ethereum](/ethereum)'s tens of thousands of validators or [Bitcoin](/bitcoin)'s hundreds of thousands of nodes.

Critics argue that Solana's validator set is dangerously centralised. Defenders note that as long as the set is permissionless (anyone can become a validator with sufficient hardware investment), decentralisation is maintained in principle.

## Network stability and outages

Solana has experienced multiple complete network outages since launch, due to bugs or unexpected load. In January 2021 and September 2021, the network halted for extended periods, unable to reach consensus. These incidents damaged confidence and highlighted the risks of prioritising speed over robustness.

Since then, client implementations have been hardened, and validator operators have improved redundancy and monitoring. However, the possibility of cascading failures remains higher on Solana than on [Bitcoin](/bitcoin) or [Ethereum](/ethereum), where fault tolerance is more fundamental.

## Ecosystem and adoption

Solana has attracted a vibrant ecosystem of DeFi protocols, NFT marketplaces, and gaming projects. The low fees — often a fraction of a cent — and fast finality make Solana attractive for applications where microseconds and small costs matter.

However, Solana's ecosystem remains smaller than [Ethereum](/ethereum)'s. Many DeFi protocols run on both, but those built exclusively for Solana are at a disadvantage if developers migrate to layer-2 Ethereum solutions, which offer comparable fees with greater liquidity and established user bases.

## The relationship to Ethereum

Some view Solana and [Ethereum](/ethereum) as offering a fundamental trade-off: Ethereum prioritises decentralisation and security (with layer-2 solutions adding speed), while Solana prioritises speed at the cost of some decentralisation. Others view Solana's approach as a valid option for applications that value throughput over paranoia.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake) — Solana's validator-selection mechanism
- [Validator](/validator) — who secures Solana
- [Staking](/staking) — how to earn rewards on Solana
- Smart contract — programs on Solana (written in Rust)
- DeFi lending — applications on Solana

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Distributed ledger](/distributed-ledger) — Solana's network architecture
- [Ethereum](/ethereum) — a competing platform prioritising other trade-offs
- Layer-2 — Ethereum's scaling approach
- [Avalanche](/avalanche), [Polygon](/polygon) — other high-throughput chains
- [Cryptocurrency exchange](/cryptocurrency-exchange) — where SOL trades

</div>

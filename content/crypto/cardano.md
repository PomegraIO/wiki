---
title: "Cardano"
description: "Cardano is a blockchain platform founded by Charles Hoskinson with a focus on academic research and formal verification. It uses proof-of-stake consensus and supports smart contracts through its Plutus language."
keywords:
  - cardano
  - ada
  - blockchain
  - proof-of-stake
  - smart contract
  - plutus
image: "https://picsum.photos/seed/cardano/900/600"
---

*A **Cardano** (**ADA**) is a [blockchain](/blockchain-fundamentals) platform and cryptocurrency created by Charles Hoskinson (co-founder of [Ethereum](/ethereum)) and formally established through the Cardano Foundation. It prioritises academic rigour and formal verification, using [proof-of-stake](/proof-of-stake) consensus to secure the network.*

<div class="wiki-hatnote">

This entry covers the Cardano network and its cryptocurrency. For its native token, see the ADA token page; for similar platforms, see [Ethereum](/ethereum), [Polkadot](/polkadot), or [Solana](/solana).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cardano — key facts</div>

<img src="https://picsum.photos/seed/cardano/900/600" alt="Cardano logo and network diagram" />

<div class="wiki-infobox-caption">Cardano: a research-driven blockchain with formal verification and academic foundations.</div>

|   |   |
|---|---|
| **What it is** | A blockchain platform and cryptocurrency |
| **Native currency** | Ada (ADA) |
| **Created** | 2015 |
| **Founder** | Charles Hoskinson |
| **Consensus mechanism** | [Proof-of-stake](/proof-of-stake) (Ouroboros) |
| **Smart contract language** | Plutus |
| **Block time** | ~20 seconds |
| **Total supply** | 45 billion ADA |
| **Governance** | Decentralised through voting |

</aside>

## Philosophy and origins

Charles Hoskinson, dissatisfied with [Ethereum](/ethereum)'s direction, founded Cardano to build a blockchain with uncompromising academic rigour. Every feature proposed for Cardano was to be peer-reviewed and formally verified — mathematically proven correct rather than tested in production.

This academic approach is reflected in Cardano's governance: the Cardano Foundation, IOHK (Input Output Hong Kong), and Emurgo jointly guide the platform. Major decisions are submitted to the community for voting through a formal voting system.

## Ouroboros proof-of-stake

Cardano's consensus mechanism, called **Ouroboros**, was one of the first [proof-of-stake](/proof-of-stake) algorithms to provide formal security proofs. It divides time into "epochs" of fixed length and uses a verifiable random function to select which [validator](/validator) proposes each block.

Cardano's approach to [staking](/staking) is designed to discourage centralisation. Validators receive rewards proportional to their stake, but the protocol includes mechanisms to reward smaller pools equally with larger ones, maintaining a wide distribution of validation power.

## Plutus and smart contracts

Unlike [Ethereum](/ethereum)'s Solidity, which is a traditional programming language, Plutus is based on Haskell — a functional programming language favoured in academia for its mathematical properties. This design choice reflects Cardano's bet that formal verification is easier in functional languages.

Plutus contracts are compiled to bytecode that runs on Cardano's virtual machine. Early adoption of Plutus-based DeFi was slower than on [Ethereum](/ethereum), partly because functional programming has a steeper learning curve and partly because the ecosystem was smaller.

## The roadmap: Alonzo and beyond

Cardano's development has been unusually methodical. The network launched in 2017 with only basic transactions. Smart contract support arrived years later with the Alonzo upgrade (September 2021). This glacial pace frustrated some observers but aligned with Cardano's philosophy of deliberate, formally verified development.

Subsequent upgrades have added features piecemeal: Babbage (2023) expanded smart contract capabilities, and Ouroboros improvements continue to enhance scalability and finality.

## Scalability and layer-2

Cardano's base layer remains relatively modest in throughput. The platform has embraced sidechains and layer-2 solutions to scale, but adoption of these has lagged Ethereum's alternatives like [Arbitrum](/arbitrum) or [Optimism](/optimism).

One notable sidechain is Cexplorer, which uses Cardano for transaction settlement while moving computation off-chain. However, integration with Cardano's main consensus remains limited compared to more tightly coupled scaling solutions.

## Market position

Cardano has consistently ranked in the top ten cryptocurrencies by [market capitalisation](/market-capitalization). Its large supply of 45 billion ADA (versus Bitcoin's 21 million) makes individual tokens cheaper, though this is economically irrelevant.

Institutional adoption of Cardano has been slower than Ethereum, and DeFi activity on Cardano trails far behind. However, Cardano has found use cases in supply-chain tracking and identity verification, particularly in developing economies.

## Criticism and controversy

Critics argue that Cardano's academic rigour and slow development pace are liabilities. While Ethereum moved fast and broke things, Cardano moved cautiously — by which time Ethereum had already captured most developers and users.

Others question whether formal verification of smart contracts actually prevents hacks, given that the contracts themselves (which use Plutus) must still be written correctly. Security ultimately depends on the programmer, not just the language.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum) — founder Charles Hoskinson's previous project
- [Proof-of-stake](/proof-of-stake) — Cardano's consensus mechanism
- [Validator](/validator) — participants in Cardano's Ouroboros
- [Staking](/staking) — how Cardano is secured
- Smart contract — Plutus programs on Cardano

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Distributed ledger](/distributed-ledger) — Cardano's network structure
- Layer-2 — Cardano's scaling approach
- [Solana](/solana), [Polkadot](/polkadot), [Avalanche](/avalanche) — competing smart contract platforms

</div>

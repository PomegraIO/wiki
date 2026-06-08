---
title: "Stacks"
description: "A Bitcoin layer that enables smart contracts and programmability by anchoring state to Bitcoin blocks via Proof of Transfer, without modifying Bitcoin itself."
keywords:
  - stacks
  - bitcoin layer 2
  - proof of transfer
  - smart contracts
  - microblocks
image: "/svg/crypto.svg"
---

*[**Stacks**](/stacks/) is a blockchain layer built on top of [Bitcoin](/bitcoin/) that brings smart-contract programmability to the Bitcoin network without requiring changes to Bitcoin's protocol. Using a consensus mechanism called Proof of Transfer (PoX), Stacks anchors its state transitions and smart-contract execution to Bitcoin blocks, inheriting Bitcoin's security while enabling a full virtual machine for decentralized applications.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stacks — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptographic ledgers." />

<div class="wiki-infobox-caption">Bitcoin's smart-contract layer, secured by proof anchoring to Bitcoin blocks.</div>

|   |   |
|---|---|
| **What it is** | A Bitcoin-backed layer that settles smart-contract state to Bitcoin blocks every ~10 minutes |
| **Consensus mechanism** | Proof of Transfer (PoX): miners bid Bitcoin to mine Stacks and earn Bitcoin rewards |
| **Settlement** | Every Bitcoin block includes a Stacks commitment; finality ~10 minutes (Bitcoin blocktime) |
| **Smart contracts** | Clarity language; non-Turing-complete by design for verifiability |
| **Finality** | Bitcoin's finality (~10 minutes median, ~1 hour practical); can assume ~6 confirmations |
| **Native token** | STX; required for transaction fees and smart-contract deployment |
| **Launched** | Testnet 2019; mainnet January 2021 |

</aside>

## Why Bitcoin needs layers, and why programmability matters

[Bitcoin](/bitcoin/) is designed for one job: secure, immutable ledger of accounts and balances. It does not execute arbitrary code; it does not track state machines. This is intentional—simplicity and immutability are Bitcoin's selling points. Yet users want more: decentralized finance, NFT markets, conditional payment logic, and atomic swaps without centralized intermediaries.

Previous layers (e.g., Liquid, conventional sidechains) require either a new security model (federated signers, trusted custodians) or a separate blockchain entirely. Stacks inverts the problem: instead of moving Bitcoin off-chain, it settles Bitcoin-backed smart-contract transactions *to Bitcoin blocks*, using Bitcoin's security directly.

## Proof of Transfer: the novel mechanic

Stacks' breakthrough is Proof of Transfer (PoX), invented by Muneeb Ali and the Stacks Foundation. Here's how it differs from Proof of Work or Proof of Stake:

Miners competing to extend the Stacks blockchain must burn Bitcoin (or transfer it to stackers—participants who lock STX). The Bitcoin sent by miners goes to stackers as a reward, creating a direct economic feedback loop: Stacks security is directly purchased with Bitcoin.

When a miner broadcasts a block on Stacks, it includes a commitment (a cryptographic hash) of the block's state. This commitment is embedded in a Bitcoin transaction. The next Bitcoin block that confirms this transaction acts as a checkpoint: Stacks gains Bitcoin-level finality.

This mechanism achieves two things simultaneously: it makes Stacks expensive to attack (you must acquire Bitcoin and burn/transfer it), and it ties Stacks' narrative to Bitcoin's network effects. Stacks is not a separate blockchain competing for market share; it is a Bitcoin enhancement.

## Clarity: a non-Turing-complete smart-contract language

Stacks' virtual machine executes Clarity, a smart-contract language invented specifically for Bitcoin settlement. Unlike Solidity or Rust (on other chains), Clarity is not Turing-complete: loops and recursion are not primitives.

This is a philosophical choice. A Turing-complete language allows arbitrary computation, which can make verification and security analysis very hard. Clarity limits expressiveness to make smart contracts analyzable: you can reason about resource costs and correctness statically.

For most DeFi use cases—swaps, lending, bridges—Clarity is sufficient. It explicitly supports Bitcoin primitives like UTXO management and atomic cross-chain swaps.

## Settlement cadence and finality model

Stacks produces microblocks every ~10 seconds, allowing high transaction throughput. But final settlement to Bitcoin happens roughly every 10 minutes (one Bitcoin block). This means:

- Transactions appear on Stacks within seconds.
- Full finality (Bitcoin-level) occurs within 10 minutes, or longer if you want more Bitcoin confirmations (standard practice is 6 confirmations, ~1 hour).

This is a genuine trade-off. Optimistic rollups like Arbitrum offer faster pseudo-finality but require faith in fraud-proof mechanisms. [zkSync Era](/zksync-era/) requires 15–30 minutes for proof generation. Stacks' finality is straightforward: when Bitcoin confirms, it is final.

## Ecosystem state and practical adoption

Stacks has attracted attention from Bitcoin-native projects. Major DeFi protocols (Alex, Magic Eden, BTCPay) have Stacks deployments. Bitcoin bridge protocols allow moving Bitcoin to Stacks as "sBTC" (a wrapped representation) for use in smart contracts.

Adoption remains smaller than Ethereum or its layer-2s. Liquidity is concentrated in a few pools; developer tooling is maturing but not yet as rich as Solidity's ecosystem. The non-Turing-complete design limits expressiveness, which some developers see as a feature (safety) and others as a limitation.

## PoX stacking rewards for token holders

Stacks has an innovative tokonomic model: STX holders can "stack" (lock) their tokens and earn a share of the Bitcoin rewards that miners send as part of PoX consensus. This is unusual—it creates a direct incentive to hold STX and participate in network security, without diluting the token supply (as pure Proof of Stake would).

This model aligns incentives: Bitcoin miners want Stacks to be secure and valuable (so they can earn mining rewards); token holders want Stacks to be secure (so their stacking rewards are valuable). The circular dependency is elegant.

## Positioning relative to other Bitcoin layers

[Lightning Network](/lightning-network/) focuses on payments and micropayments off-chain, requiring no settlement delays; finality is instant between peers. Stacks is for general smart contracts, accepting 10-minute settlement. Liquid Network (federated sidechain) trades decentralization for faster finality and privacy. Each serves different needs.

Stacks' claim is simple: full smart-contract capability with Bitcoin-level security guarantees. The cost is architectural complexity (maintaining two blockchains in sync) and 10-minute settlement windows.

## Future roadmap: sBTC and atomic settlement

Stacks' current version uses a wrapped Bitcoin model for DeFi (sBTC). The team is working toward native Bitcoin settlement: smart contracts that directly control Bitcoin UTXOs on the Bitcoin blockchain, without intermediaries. This would make Stacks even more deeply integrated with Bitcoin, though the technical and protocol challenges are substantial.

The long-term vision is Bitcoin as a settlement layer, with Stacks and other protocols as programmable overlays. This narrative attracts Bitcoin maximalists who want Ethereum-style functionality without abandoning Bitcoin as the base.

## See also

<div class="wiki-seealso">

### Closely related

- [Lightning Network](/lightning-network/) — Bitcoin's payment-channel network for instant micropayments
- [zkSync Era](/zksync-era/) — Ethereum layer-2 using zero-knowledge proofs for faster settlement
- [Fantom](/fantom/) — EVM-compatible layer using DAG-based consensus for sub-second finality
- [Bitcoin](/bitcoin/) — The base layer that Stacks settles to and derives security from
- [Proof of Transfer](/stacks/) — Stacks' consensus mechanism where miners burn Bitcoin for block rights
- [Smart contracts](/ethereum/) — General programmability concept; Stacks implements via Clarity
- [Blockchain fundamentals](/blockchain-fundamentals/) — Consensus and settlement-layer concepts

### Wider context

- [Distributed ledger](/distributed-ledger/) — The broader family of decentralized systems
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where STX and wrapped Bitcoin trade
- [Capital flows](/capital-flows/) — Movement of Bitcoin between layers and through DeFi
- [Decentralized finance](/ethereum/) — The primary use case for Stacks' smart contracts

</div>

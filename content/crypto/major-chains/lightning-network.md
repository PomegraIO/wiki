---
title: "Lightning Network"
description: "A peer-to-peer payment-channel network that enables instant Bitcoin transactions and micropayments by routing payments off-chain, settling only the final balance on-chain."
keywords:
  - lightning network
  - bitcoin payments
  - payment channels
  - off-chain transactions
  - routing
image: "/svg/crypto.svg"
---

*The [**Lightning Network**](/lightning-network/) is an off-chain payment-routing system built on top of [Bitcoin](/bitcoin/) that allows two parties to conduct an unlimited number of transactions without recording each one on the blockchain. By opening a payment channel (a 2-of-2 multi-signature address), peers can send Bitcoin instantly to each other; the network routes payments across channels, settling only the final net balance to the blockchain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lightning Network — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptographic ledgers." />

<div class="wiki-infobox-caption">Bitcoin's off-chain payment network for instant, near-zero-fee transactions.</div>

|   |   |
|---|---|
| **What it is** | A network of peer-to-peer payment channels that route Bitcoin off-chain |
| **Channel mechanism** | Two parties lock funds in a 2-of-2 multi-sig address and exchange signed updates |
| **Transaction speed** | Instant (routing latency; typically seconds) |
| **Settlement** | Only channel open and close events recorded on Bitcoin blockchain |
| **Fees** | Typically fractional satoshis (millionths of a Bitcoin) per hop |
| **Finality** | Instant between peers; on-chain confirmation when closing channels |
| **Maturity** | Active since 2018; production use by merchants and traders |
| **Protocol standard** | BOLT (Basics of Lightning Technology) specifications |

</aside>

## The Bitcoin scalability problem Lightning solves

[Bitcoin](/bitcoin/) processes roughly 7 transactions per second on-chain. At peak demand, fees spike to tens of dollars per transaction, and confirmation times stretch to hours. For everyday payments—a coffee, a small peer-to-peer transfer, a merchant payout—this is impractical.

Lightning inverts the scaling approach. Instead of trying to fit more transactions on the blockchain, it moves transactions off-chain entirely, using the blockchain only as a final settlement layer and security anchor.

## How payment channels work

Suppose Alice and Bob want to transact repeatedly. They create a payment channel:

1. Alice and Bob jointly create a multi-signature address (2-of-2) and fund it with Bitcoin (e.g., Alice sends 1 BTC, Bob sends 1 BTC).
2. They exchange a series of signed transactions that update the balance: "Alice has 0.5 BTC, Bob has 1.5 BTC." Each update is signed by both parties.
3. They can create hundreds or thousands of updates without touching the blockchain.
4. When they want to close the channel, they broadcast the final state to the Bitcoin blockchain. The blockchain confirms who gets what.

If either party tries to cheat (broadcasting an old state where they have more funds), the other party can produce the newer signed state, proving the cheater wrong. The blockchain arbitrates disputes using the cryptographic proof.

This mechanism is trustless: neither party can steal from the other; neither party needs a bank or intermediary.

## Routing: connecting channels into a network

A channel between two people is useful, but a network of channels is transformative. The Lightning Network routes payments across channels, allowing Alice to pay Carol (a stranger) through Bob:

Alice sends Bob a hash-locked atomic payment: "Forward 0.1 BTC to Carol; if Carol confirms receipt by showing me a secret value, I'll settle 0.1 BTC to you." Bob repeats this with Carol. Carol reveals the secret to Bob; Bob reveals it to Alice. The payment is atomic: either it goes through end-to-end, or it fails entirely. No intermediate party can steal funds.

This routing can span dozens of channels. Each hop charges a small routing fee (a few satoshis). The total fee for a global payment might be under one cent.

## Practical constraints and trade-offs

Lightning is elegant but not without limits:

**Channel liquidity**: If Alice and Bob's channel has Alice=1 BTC, Bob=0, Alice cannot receive Bitcoin without Bob initiating a channel rebalance (opening a new channel elsewhere). Liquidity management is an emerging service industry on Lightning.

**Bi-directional balance**: Payment channels require both parties to fund them. A merchant accepting Lightning payments must either regularly close channels (settling on-chain, incurring fees) or arrange liquidity services to rebalance.

**Watchtowers**: If Alice goes offline, Bob could broadcast an old channel state to the blockchain, stealing Alice's funds. Alice can use a "watchtower" (a service that monitors the blockchain and broadcasts the correct state if needed), but this adds complexity and trust.

**Channel closure time**: Closing a channel takes ~10 minutes (one Bitcoin block), or longer if the other party contests it.

## Real-world usage today

Lightning is actively used by Bitcoin merchants, exchanges, and payment processors. El Salvador's Bitcoin Beach project uses Lightning for everyday transactions. Strike (a payments app) routes through Lightning. Shopify merchants can accept Lightning payments. Gaming services, lending protocols, and streaming platforms have integrated Lightning.

Adoption is still niche relative to on-chain Bitcoin or traditional payment systems, but the network effect is accelerating. As more liquidity providers join, routing becomes cheaper and more reliable.

## Privacy and scalability advantages

Lightning transactions are not recorded on the public blockchain, offering privacy: an observer cannot easily trace who paid whom. On-chain, every transaction is permanently visible.

Scalability is the second advantage. A payment channel can theoretically support millions of updates per second. The global Lightning Network, aggregating millions of channels, could handle billions of transactions annually with only a few on-chain channel opens and closes.

## Competitive positioning vs. other layers

[Stacks](/stacks/) and [zkSync Era](/zksync-era/) are smart-contract platforms; Lightning is payments-only. [Stacks](/stacks/) settles to Bitcoin every 10 minutes; Lightning settles when channels close (which could be weeks or months). Lightning's focus is laser-sharp: maximize payment throughput and minimize fees.

This narrow ambition is a strength. Lightning is unlikely to run DeFi smart contracts, but for payments, it is the best Bitcoin scaling solution to date.

## Technical challenges and open questions

**Channel capacity**: The total value locked in Lightning channels (roughly 5,000 BTC as of 2025) is small relative to Bitcoin's market cap. Expanding this requires attracting liquidity providers and solving rebalancing.

**Routing reliability**: As the network grows, finding optimal routes through thousands of nodes becomes computationally harder. Some researchers worry about potential chokepoints.

**Privacy trade-offs**: Routing requires intermediaries to learn sender and recipient (though not amounts). Protocols like rendez-vous routing and multi-path payments are being developed to improve privacy.

## Development and standardization

Lightning is maintained by multiple independent implementations (LND, c-lightning, Eclair, Rust Lightning), each following the BOLT standard. This fragmentation ensures no single entity controls the network; it also requires careful coordination for new features.

The protocol is stable but still evolving. Active development continues on privacy, routing efficiency, and integration with higher-layer protocols.

## See also

<div class="wiki-seealso">

### Closely related

- [Stacks](/stacks/) — Bitcoin layer for smart contracts, settling every ~10 minutes
- [zkSync Era](/zksync-era/) — Ethereum layer using zero-knowledge proofs for faster settlement
- [Fantom](/fantom/) — EVM-compatible layer with sub-second finality
- [Bitcoin](/bitcoin/) — The base blockchain that Lightning builds upon
- [Payment channels](/lightning-network/) — The foundational technology Lightning uses
- [Atomic swaps](/bitcoin/) — Cross-chain payments enabled by Hash Time-Locked Contracts (HTLC)
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where Bitcoin and Lightning-native tokens trade

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — Consensus and off-chain scaling concepts
- [Distributed ledger](/distributed-ledger/) — The broader family of decentralized systems
- [Capital flows](/capital-flows/) — Movement of Bitcoin between layers
- [Decentralized finance](/ethereum/) — The economic ecosystem Lightning services

</div>

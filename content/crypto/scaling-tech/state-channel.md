---
title: "State Channel"
description: "Off-chain transaction protocol enabling participants to transact repeatedly without touching the blockchain, settling periodically on-chain."
keywords:
  - off-chain transactions
  - payment channels
  - scalability
  - settlement finality
---

*A **state channel** is a layer-two scaling technique that lets two or more parties exchange transactions repeatedly off-chain, settling the net result on-chain only when they choose to close the channel. Transactions are instantaneous and gas-free within the channel; the blockchain is used only for opening, funding, and settling disputes.*

<aside class="wiki-infobox">

| Attribute | Detail |
|---|---|
| **Settlement** | Periodic on-chain; parties agree to final state |
| **Throughput** | Unlimited off-chain; on-chain limited by blockchain capacity |
| **Latency** | Microseconds (no confirmation wait) |
| **Participants** | Two to many parties, depending on channel design |
| **Dispute resolution** | On-chain smart contract enforces rules if closed unilaterally |
| **Examples** | Lightning Network (Bitcoin), Raiden (Ethereum) |

</aside>

## How a state channel works: the mechanics

A state channel opens with both parties depositing funds into a smart contract. Alice and Bob each lock 1 ETH; the contract now holds 2 ETH as collateral. Alice and Bob then sign transaction states off-chain—Alice sends 0.1 ETH to Bob, Bob acknowledges and signs. Both parties hold the same signed state, but the blockchain has not yet recorded it. They can repeat this process hundreds or thousands of times, with each new state superseding the last, without spending gas or waiting for confirmation.

When they decide to settle, either party can broadcast the final agreed-upon state to the blockchain. The smart contract receives the latest signed state, verifies both signatures, and distributes funds accordingly. Alice withdraws 0.9 ETH, Bob withdraws 1.1 ETH. The blockchain now knows the net outcome, but only saw two on-chain transactions: the initial lock and the final settlement.

## Why bidirectional state matters

The power of state channels is symmetry. Alice can send to Bob, Bob can send back to Alice, all without on-chain friction. This is what makes the [Lightning Network](/wiki/bitcoin/) practical: Alice pays Bob, Bob pays Carol, Carol pays back to Alice—all instant, all off-chain. The blockchain is a final arbiter and a secure anchor, but it does not see every transaction.

Traditional [payment channels](/wiki/payment-system-stability/) were unidirectional: Alice paid Bob, and only Alice could initiate transactions. [State channels](/wiki/crypto-settlement-finality/) are bidirectional; either party can send value in either direction.

## Dispute resolution and proof of fraud

What if Bob tries to cheat? Suppose Alice and Bob agree on a final state where Alice has 0.8 ETH and Bob has 1.2 ETH. Bob then broadcasts an older state (from three transactions ago) where Alice has 0.3 ETH and Bob has 1.7 ETH. Alice, holding the more recent state, can submit it to the on-chain contract as a challenge. The contract sees both states, compares their sequence numbers (a nonce or timestamp), and rejects Bob's older state. Alice wins.

This is the crux of [crypto settlement finality](/wiki/crypto-settlement-finality/): the blockchain enforces consensus on which state is current. Cheating requires rewriting the blockchain, which is computationally infeasible on [proof-of-work](/wiki/proof-of-work/) networks.

## Limitations and practical constraints

State channels work well for repeated transactions between a fixed pair (or small group) of parties. If Alice and Bob never interact after their first payment, the overhead of opening and closing the channel is not worth the savings. Channels are best suited to high-frequency peers: merchants and customers, payment hubs, liquidity providers.

Channel capacity is also fixed at opening. If Alice and Bob each deposit 1 ETH, the maximum they can exchange is 2 ETH total. Rebalancing requires closing the channel and opening a new one, which costs gas.

## Comparison to other layer-two solutions

Unlike [rollups](/wiki/zero-knowledge-rollup/), which bundle many transactions and post a proof to the main chain, state channels require no proof computation. They are faster and cheaper but less general—rollups work for any smart contract, while state channels work best for payments and simple state updates. [Optimistic rollups](/wiki/optimistic-rollup/) and [zk-rollups](/wiki/zero-knowledge-rollup/) post compressed transaction data or validity proofs every few minutes; state channels post only when a party explicitly chooses to settle.

The Lightning Network demonstrates the model's viability: payments are confirmed in milliseconds, fees are near-zero, and millions of transactions happen off-chain monthly.

## Multi-party channels and hub topologies

A state channel need not be pairwise. [Generalized state channels](/wiki/layer-three-protocol/) can involve three or more parties updating a shared state. This enables topologies where a payment hub sits in the center and routes transactions between customers. A customer in Shanghai pays a vendor in São Paulo through the hub; the hub routes the payment instantly, settling on-chain only when necessary.

[Plasma](/wiki/plasma-exit-mechanism/) and [sidechains](/wiki/sidechain-bridge/) are adjacent concepts that also move computation off-chain, but with different trust models and settlement timelines.

<div class="wiki-seealso">

### Closely related
- [Lightning Network](/wiki/bitcoin/) — The most deployed state-channel network (Bitcoin layer-two)
- [Payment channels](/wiki/payment-system-stability/) — The ancestor of generalized state channels
- [Layer-three protocol](/wiki/layer-three-protocol/) — Multi-party state channels
- [Plasma](/wiki/plasma-exit-mechanism/) — Alternative layer-two with different semantics

### Wider context
- [Crypto settlement finality](/wiki/crypto-settlement-finality/) — How settlement is guaranteed on-chain
- [Zero-knowledge rollup](/wiki/zero-knowledge-rollup/) — Another layer-two scaling method
- [Optimistic rollup](/wiki/optimistic-rollup/) — Rollup variant with fraud proofs
- [Sidechain bridge](/wiki/sidechain-bridge/) — Parallel chain with its own consensus

</div>

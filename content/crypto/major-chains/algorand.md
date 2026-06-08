---
title: "Algorand"
description: "A pure proof-of-stake blockchain achieving immediate transaction finality without forks through cryptographic lotteries."
keywords:
  - algorand
  - proof of stake
  - transaction finality
  - byzantine consensus
  - cryptocurrency
image: "/svg/crypto.svg"
---

*[Algorand](/algorand/) is a [proof-of-stake](/proof-of-stake/) blockchain that achieves single-block finality—transactions become irreversible in the same block that includes them—using a cryptographic lottery system instead of traditional mining or validator election. Every token holder is eligible to propose blocks or participate in consensus, selected at random, making the network probabilistically Byzantine-fault-tolerant without requiring known validator sets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Algorand — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Pure proof-of-stake with instant finality and no forks.</div>

|   |   |
|---|---|
| **What it is** | A [proof-of-stake](/proof-of-stake/) blockchain with cryptographic leader election |
| **Consensus mechanism** | Pure proof-of-stake with Byzantine agreement |
| **Block time** | ~4.5 seconds |
| **Finality** | Single-block (immediate, probabilistic) |
| **Token holder participation** | Direct (all Algo holders eligible for committee selection) |
| **Native asset** | Algo (ALGO) — staking, gas, consensus participation |
| **Smart contract language** | TEAL (specialized for Algorand) |

</aside>

## The challenge of proof-of-stake consensus

Most [proof-of-stake](/proof-of-stake/) blockchains, including [Ethereum](/ethereum/) and [Tezos](/tezos/), use a known set of validators. These validators are elected through staking or delegation, and they produce blocks and vote on consensus rounds. This is efficient: protocol designers know who the players are, can set quorum rules, and can make stronger guarantees about liveness and safety.

But known validator sets have a flaw. If validator selection is public and deterministic, adversaries can target them for attack (network disruption, physical coercion, bribery). If the set is small, consensus is faster but more centralized. [Algorand](/algorand/) took a different approach: make validator selection random and unknown until the moment it's needed.

## How Algorand's cryptographic lottery works

In [Algorand](/algorand/), the network reaches consensus through a multi-step Byzantine agreement protocol, and every step relies on random selection from the full token-holder set.

When it's time to propose a new block, [Algorand](/algorand/) runs a **sortition** (cryptographic lottery). Every Algo holder has a chance to be selected as a proposer, weighted by their stake. Crucially, the selection happens locally—no central authority announces the winner. Each token holder computes, using cryptographic hashes of public randomness and their own secrets, whether they've won the sortition. If they have, they propose a block.

Because the sortition is *deterministic but secret* (only the winner knows they won, until they broadcast), an adversary cannot predict in advance who will propose the next block and cannot mount targeted denial-of-service attacks on proposers.

After a block is proposed, a **consensus committee** is selected the same way. Thousands of token holders are randomly chosen (weighted by stake) and receive a cryptographic proof that they're committee members. The committee then votes on the block proposal using a sub-protocol called BA* (Byzantine Agreement star). Each committee member signs their vote; honest nodes wait for a quorum (usually 67% or higher) of committee signatures before accepting the block as final.

## Immediate finality without forks

A key property of [Algorand](/algorand/) is that once a block is committed by the consensus committee, it is **final**—it cannot be undone, even in the presence of adversarial network partitions. There are no competing forks, no "canonical chain" that might later reorganize. This is different from [Proof-of-Work](/proof-of-work/) systems like [Bitcoin](/bitcoin/), where deeper chains can overtake shallower ones, or from early [Proof-of-Stake](/proof-of-stake/) designs where reorganizations are possible if the attacker controls enough stake.

Algorand achieves this through Byzantine fault tolerance (BFT). The consensus protocol guarantees that if fewer than one-third of the committee is dishonest, the protocol will not finalize conflicting blocks. Since committee members are randomly selected from all stake holders, and an attacker would need to own one-third of all Algo to guarantee representation, single-block finality is guaranteed so long as the attacker doesn't control that threshold.

In practice, Algorand finalizes blocks in roughly 4.5 seconds and tolerates high levels of network latency. The randomness of committee selection means there is no "leader" to blame if consensus is slow—Byzantine fault tolerance guarantees hold regardless of network conditions or adversarial behavior.

## Pure proof-of-stake and dilution

[Algorand](/algorand/) is truly permissionless: you do not need to run a node or lock up a minimum stake to be eligible for selection. Anyone holding Algo in an account is automatically eligible. This is called **pure proof-of-stake** and contrasts with systems where only validators who explicitly register and meet minimum stake thresholds participate in consensus.

The trade-off is that [Algorand](/algorand/)'s network creates new Algo over time to pay for consensus participation (epoch rewards) and to fund development. This dilutes existing token holders. The inflation rate is managed through protocol parameters, and the foundation has committed to specific token emission schedules.

## Smart contracts and the asset framework

[Algorand](/algorand/) uses TEAL (Transaction Execution Approval Language), a stack-based language for smart contracts. TEAL emphasizes simplicity and auditability over expressiveness. Contracts on [Algorand](/algorand/) are often simpler and more predictable than on [Ethereum](/ethereum/), but also more limited in what they can express.

[Algorand](/algorand/) also introduced an "Algorand Standard Asset" (ASA) framework, allowing anyone to mint custom tokens directly on the protocol without writing smart contracts. This makes tokenization straightforward and reduces complexity for simple use cases.

## Finality versus throughput trade-off

[Algorand](/algorand/) achieves immediate finality with 4.5-second blocks and supports roughly 1000 transactions per second on the base layer. This is respectable but not extraordinary compared to some other chains. [Solana](/solana/), for example, theoretically supports much higher throughput, though with less reliable finality. [NEAR](/near-protocol/) scales through sharding.

[Algorand](/algorand/)'s design choice prioritizes correctness and finality over raw throughput. The cryptographic commitments that guarantee safety—random committee selection, Byzantine fault tolerance, single-block finality—constrain how much can be packed into each block and how quickly blocks can be confirmed. The payoff is a network where you can trust that transactions are irreversible and safe within seconds.

## Criticism and adoption challenges

[Algorand](/algorand/) faces competition from other proof-of-stake systems. [Ethereum](/ethereum/)'s shift to proof-of-stake (completed in 2022) gave it a well-known, battle-tested alternative. [Tezos](/tezos/) offers on-chain governance. [Hedera Hashgraph](/hedera-hashgraph/) targets enterprise with DAG-based consensus.

In practice, [Algorand](/algorand/) has attracted mainstream institutions and developers but remains smaller than [Ethereum](/ethereum/) in terms of total value locked and ecosystem activity. The adoption challenge is partly path dependency (Ethereum network effects are strong) and partly that [Algorand](/algorand/)'s simpler smart contract language appeals to different use cases (simpler tokens, basic DeFi) rather than complex protocols.

The cryptographic lottery mechanism is sound, but it is also less intuitive to developers and users than traditional validator models. There is no obvious "stake pool" to join; instead, you simply hold tokens and are implicitly eligible. This has given [Algorand](/algorand/) a reputation as a "technically superior but less user-friendly" blockchain—though this perception may not reflect current reality.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of stake](/proof-of-stake/) — Algorand's consensus mechanism
- [Ethereum](/ethereum/) — alternative layer-1 using proof-of-stake
- [NEAR Protocol](/near-protocol/) — another layer-1 with different scalability approach
- [Tezos](/tezos/) — layer-1 with on-chain governance
- [Hedera Hashgraph](/hedera-hashgraph/) — enterprise blockchain using DAG consensus

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger concepts
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where Algo tokens trade
- [Byzantine fault tolerance](/byzantine-fault-tolerance/) — consensus model underlying Algorand
- [Distributed ledger](/distributed-ledger/) — foundational technology

</div>

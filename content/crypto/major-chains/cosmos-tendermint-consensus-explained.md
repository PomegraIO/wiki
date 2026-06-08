---
title: "Cosmos Tendermint Consensus Explained"
description: "How Cosmos Tendermint consensus works: Byzantine fault-tolerant proof-of-stake with two-round voting for instant finality."
keywords:
  - cosmos tendermint consensus explained
  - tendermint bft algorithm
  - proof of stake consensus
  - instant finality blockchain
  - byzantine fault tolerance
  - validator voting rounds
image: /svg/crypto.svg
---

*The **Cosmos Tendermint consensus** algorithm is a Byzantine fault-tolerant proof-of-stake system that achieves instant transaction finality through a two-round voting process among validators. Tendermint's design trades some throughput flexibility for security certainty and speed — once a block is committed, it cannot be reorganized, and confirmation happens immediately rather than requiring dozens of confirmations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tendermint BFT — Consensus at a glance</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Instant finality and deterministic safety through two voting rounds.</div>

|   |   |
|---|---|
| **Consensus type** | Byzantine fault-tolerant proof-of-stake |
| **Finality** | Instant (one confirmation = permanent) |
| **Validator participation** | Fixed set required to vote each round |
| **Fault tolerance** | Tolerates up to 1/3 validators Byzantine |
| **Block time** | Configurable (typically 1–5 seconds) |
| **Energy model** | Proof-of-stake (no mining required) |

</aside>

## The problem Tendermint solves

Early blockchains like Bitcoin faced a fundamental problem: how do you reach agreement on a shared ledger when you cannot trust all participants? Proof-of-work answered by making an attacker pay computational cost. Tendermint answers the same question differently. In Tendermint networks, a known set of validators locks in their stake and proposes or votes on new blocks. If a validator misbehaves, its stake is slashed. This approach — called proof-of-stake — requires far less electricity than proof-of-work and delivers finality instantly rather than probabilistically.

Tendermint's name references Byzantine generals — the classical computer science problem where loyal generals must agree on a battle plan despite the presence of traitors. Tendermint achieves this by tolerating up to one-third of validators being dishonest. So long as two-thirds of voting power acts honestly, the system reaches consensus and executes a block irreversibly.

## How a Tendermint consensus round works

A Tendermint consensus round consists of two voting phases: **Prevote** and **Precommit**. The sequence is deterministic and repeats every block.

**Propose phase:** A designated proposer (selected by the [proof-of-stake](/proof-of-stake/) algorithm based on validator stake and other criteria) creates a new block and broadcasts it to all other validators.

**Prevote phase:** Validators receive the proposed block, check its validity, and cast a prevote vote. Each validator either votes for the block it received, votes for `<nil>` (rejecting it), or votes for nothing (if the block was malformed or hadn't arrived). After this phase, validators tally prevotes. If the proposer's block received more than two-thirds of prevotes, the protocol proceeds to precommit. If no block achieves two-thirds, the round proceeds with `<nil>`.

**Precommit phase:** Validators now vote again — this time on whether to precommit the block that won the prevote round. If two-thirds of validators precommit the same block, that block is **committed** and becomes part of the canonical chain. From that moment, it cannot be unrolled: finality is achieved.

If neither phase reaches two-thirds agreement, the round times out and a new proposer is selected for the next round.

## Instant finality and the advantage of determinism

Unlike Bitcoin's longest-chain rule — where reorganizations are theoretically possible until a block has enough proof-of-work buried behind it — Tendermint blocks achieve finality the moment they receive two-thirds precommit votes. A Tendermint block confirmed by validators cannot be removed or reorganized without slashing (destroying) the stake of two-thirds of the active validator set.

This means that once you see a transaction in a committed block on a Tendermint chain, it is final. There is no waiting for "six confirmations" or worrying about a chain reorganization. For applications that settle payments or execute smart contracts, instant finality reduces settlement risk to zero (or to the cost of slashing two-thirds of validators, which is economically prohibitive).

The trade-off: Tendermint's throughput depends on the network's capacity to collect and tally two rounds of votes. As the validator set grows, voting becomes slower. This is why Cosmos chains typically run 50–150 validators rather than thousands. Bitcoin, by contrast, has no fixed validator set and can add mining power freely.

## Liveness and safety guarantees

Tendermint guarantees two properties:

**Safety:** Two conflicting versions of history can never both be committed. If two-thirds of validators precommit block A at height 100, no two-thirds majority can later precommit a different block B at the same height. This prevents forks by design.

**Liveness:** The network continues making progress as long as fewer than one-third of validators are Byzantine (faulty or malicious). If one-third or more are dishonest, liveness may halt — the chain stops producing blocks until the Byzantine validators are removed or the system recovers.

This reflects a classic trade-off in distributed consensus: systems can be safe but not live, live but not safe, or (like Tendermint) both, but only under honest-threshold assumptions.

## Evidence and slashing

Tendermint penalizes misbehavior through **slashing**. If a validator signs two different blocks at the same height, or signs a precommit for a block without having prevoted for it, that contradiction — called **evidence** — is broadcast across the network and recorded on-chain. The validator's stake is then slashed (usually 5% or more, configurable per chain), and the validator is jailed (temporarily or permanently removed from the validator set).

Evidence-based slashing is the core security mechanism. It makes attacking the network expensive: to rewrite history, a validator would have to slash enough stake to achieve two-thirds of the network. That cost must exceed any gain from the attack.

## Validator selection and proof-of-stake

Tendermint chains use proof-of-stake to choose validators. The more tokens a validator stakes, the more often it is selected as proposer and the more voting power it wields. A chain's [Cosmos](/cosmos-tendermint-consensus-explained/) validator set size is fixed (e.g., the top 125 staked validators become the active set; others wait in standby). Delegators can stake their tokens to a validator of choice and earn a share of block rewards and fees.

This design creates economic incentive: validators want to stay online and vote correctly because the rewards come from their stake. Misbehavior triggers slashing, so dishonest validators lose money. Over time, the Cosmos ecosystem tuned validator selection, jail duration, and slashing rates to balance security and decentralization.

## Practical implications

Tendermint's instant finality and security have made it the basis for the Cosmos Hub and hundreds of interoperable blockchains. Applications built on Tendermint chains can confirm critical transactions in seconds without waiting for confirmations. Cross-chain bridges and [smart contract](/smart-contract/) platforms (like Ethereum-compatible Cosmos chains) benefit from deterministic safety.

The downsides are fewer validators and lower absolute throughput than some proof-of-work chains. But for financial settlement, governance, and deterministic state machines, those trade-offs are often worth it.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake/) — Economic incentive model underlying Tendermint validator selection
- [Byzantine fault tolerance](/distributed-ledger/) — The theoretical foundation for consensus under adversarial conditions
- [Validator](/proof-of-stake/) — Role and incentives in Tendermint networks
- [Smart contract](/smart-contract/) — Applications that benefit from instant finality

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — Core distributed ledger concepts
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where Cosmos tokens trade
- [Distributed ledger](/distributed-ledger/) — General consensus mechanisms and alternatives

</div>

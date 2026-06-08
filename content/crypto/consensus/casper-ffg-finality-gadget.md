---
title: "Casper FFG: Ethereum's Finality Gadget Explained"
description: "How Casper FFG's checkpoint voting model layers deterministic finality onto longest-chain fork rules."
keywords:
  - casper ffg
  - ethereum finality
  - finality gadget
  - checkpoint voting
  - proof of stake finality
image: "/svg/crypto.svg"
---

*The **Casper FFG** (Friendly Finality Gadget) consensus mechanism adds a layer of checkpoint voting on top of a longest-chain fork rule, allowing Ethereum to achieve deterministic finality—meaning once a block is finalized, reorganizing it requires a validator to lose a substantial amount of stake, making re-orgs economically infeasible.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Casper FFG — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A hybrid finality mechanism that layers Byzantine fault tolerant checkpoints onto a proof-of-work-like longest-chain rule.</div>

|   |   |
|---|---|
| **Mechanism** | Two-phase voting (source → target) on epoch boundary blocks |
| **Finality threshold** | 2/3 of active validator stake voting in lockstep |
| **Checkpoint distance** | One epoch (~6.4 minutes on Ethereum) |
| **Fork rule** | LMD GHOST (longest message-driven acyclic GHOST) for non-finalized blocks |
| **Penalty for violation** | Slashing up to 32% of stake if validator votes for conflicting finalizations |
| **Finality latency** | Two epochs (~12.8 minutes) in normal conditions |
| **Re-org resistance** | Requires 1/3 of validators to be slashed; therefore economically infeasible |

</aside>

## How Casper FFG layers finality atop longest-chain

Casper FFG solves a fundamental problem: longest-chain rules (like [proof-of-work](/proof-of-work/)) can reorganize past blocks, making finality probabilistic. Casper adds explicit finality by having validators vote on checkpoint blocks at regular intervals.

The mechanism works in two stages:

1. **Longest-chain for recent blocks**: Validators follow a fork-choice rule called LMD GHOST (Latest Message-Driven Greatest Observed SubTree), which is similar to selecting the longest chain. This rule allows short-term flexibility and liveness—validators can freely vote for different forks without penalty, as long as they haven't violated the [finality gadget](/casper-ffg-finality-gadget/) rules.

2. **Checkpoint finality for settled blocks**: At regular intervals (every [epoch](/epoch-based-consensus-how-epochs-work/)), a new checkpoint block is elected. Validators vote on this checkpoint, attesting that they view it as the canonical choice. Once 2/3 of the validator set has voted in lockstep (from the same source checkpoint to the same target checkpoint), that target becomes **finalized**—reorganizable only if 1/3 of validators are caught breaking finality rules and slashed.

This hybrid design gives the network the liveness benefits of longest-chain (no halts when validators disagree) while adding the finality benefits of Byzantine fault tolerance (irreversible settlement).

## The two-phase voting structure

A Casper FFG vote is not a single message; rather, it is a two-phase commitment. A validator votes for a pair of checkpoints: a **source** (previously finalized) checkpoint and a **target** (the new checkpoint being finalized).

The votes must follow strict rules:

- A validator cannot vote for a target earlier than its current source.
- A validator cannot vote for a target on a fork that is incompatible with a target it has already voted for at the same height.
- If a validator violates either rule, its stake is slashed.

These rules ensure that once 2/3 of validators have voted from source A to target B, no other target at the same height can ever be finalized, because the overlap between any two 2/3 supermajorities would contain honest validators that would have to violate the rules to change their vote.

## Why Casper is called "Friendly"

The "Friendly" in Casper FFG reflects the design goal: the mechanism is forgiving to offline validators while being very strict about Byzantine behavior.

If a validator goes offline and misses [epochs](/epoch-based-consensus-how-epochs-work/), it does not get slashed—it simply loses its reward for that epoch via the inactivity leak. It can come back online, re-synchronize, and resume participation without penalty.

But if a validator *equivocates*—signs two conflicting votes or votes on two incompatible forks at the same checkpoint height—it is immediately slashed. This asymmetry means honest validators can recover from temporary faults (outages), but malicious validators cannot engage in double-signing without severe consequences.

The slashing amount varies with network conditions. A single violation might result in a small penalty; however, if many validators are caught equivocating in the same epoch (a "mass slashing" event), each validator's penalty increases, scaling up to 32% of stake. This discourages coordinated attacks, where many validators might try to finalize an alternative chain simultaneously.

## Checkpoint finality and reorg-resistance

Once a checkpoint is finalized, reorging it requires a validator to broadcast conflicting votes, which triggers slashing. The cost of a reorg is therefore the slash penalty (typically 10–32% of stake per validator) multiplied by the number of validators involved.

To reorg a finalized block, an attacker would need to control at least 1/3 of the stake and convince them all to break the protocol rules. Given the slash penalties, this is economically irrational unless the attacker's motive is to destroy the network (rather than profit from it).

In contrast, longest-chain systems (like [proof-of-work](/proof-of-work/)) allow reorgs if an attacker controls more compute power than the honest network. But in Casper, even if an attacker controls 51% of stake, it cannot reorg a finalized block without paying the slashing penalty.

This makes Casper finality very strong. A finalized block is finalized for all practical purposes; unfinalized blocks (produced in the current epoch) can still be reorganized if the longest-chain rule shifts, but once the next epoch's checkpoint is voted in, finality spreads backward.

## Latency and the checkpoint distance tradeoff

Checkpoints are spaced one epoch apart. On Ethereum, this is ~6.4 minutes (32 slots × 12 seconds per slot). A block becomes finalized after the next two epochs have been voted in: roughly 12.8 minutes.

This latency is a design choice. Shorter checkpoint distances (e.g., every 4 slots) would achieve finality faster but would increase voting overhead and make the network less scalable. Longer distances reduce overhead but delay finality.

Most [proof-of-stake](/proof-of-stake/) systems that use Casper-like finality choose epoch-length distances to balance these concerns. The result is that finality is not instant, but it is predictable and strong.

## The relationship to Tendermint and other consensus algorithms

Casper FFG is a hybrid: it uses a longest-chain rule for liveness (allowing validators to follow different forks temporarily) and overlays finality voting for safety (ensuring that 2/3 agreement is irreversible).

In contrast, [Tendermint](/tendermint-bft-consensus-explained/) achieves finality *within* each round; there is no longest-chain phase. Tendermint finality is immediate (a few seconds) but requires 2/3 quorum at each step, so a network that loses 1/3 of its validators stops finalizing blocks entirely.

Casper trades immediate finality for liveness under partition: even if 1/3 of validators are offline, the network continues producing blocks via the longest-chain rule. Finality is delayed until the next checkpoint, but it is still achieved once the network resynchronizes.

Both approaches are valid; the choice depends on whether you prioritize instant finality (Tendermint-style) or graceful degradation under partitions (Casper-style).

## How Casper enables weak subjectivity

Casper FFG introduces a concept called **weak subjectivity**: the idea that a new node joining the network must trust a recent (but not necessarily current) state in order to determine the canonical chain.

Here is why: suppose an attacker wants to create an alternative chain that reorgs past all finalized blocks. The attacker would need to convince 1/3 of validators to sign conflicting finality votes, then slash them. Once slashed, those validators' stake is gone, but the alternative chain still has finalized checkpoints.

A new node with no prior knowledge of the network cannot tell which chain is "real" just by looking at the signatures. However, if the new node trusts a state from the last two weeks or so, it can verify that the canonical chain's finality votes were cast by the majority of validators *at that time*. Nodes that left the network longer ago might not be able to verify this, hence "weak" subjectivity.

In practice, this means staking infrastructure and exchanges publish regular finality checkpoints, which new nodes can reference. This is simpler than the absolute subjectivity required for [Byzantine fault tolerance](/byzantine-fault-tolerance/) in some other systems.

## Casper in Ethereum 2.0 deployment

Ethereum transitioned to [proof-of-stake](/proof-of-stake/) using Casper FFG as its finality mechanism. The longest-chain rule is LMD GHOST, and checkpoints are finalized at epoch boundaries.

Validators earn rewards for attesting to the correct checkpoint, and they are slashed if they equivocate or vote for incompatible forks. The protocol also includes an inactivity leak: if 1/3 of validators go offline, the remaining online validators' voting power increases (via the leak reducing offline validators' balances) until they reach 2/3 quorum and can resume finality.

This design has proven robust across multiple years of network operation and has become the reference model for proof-of-stake finality.

## See also

<div class="wiki-seealso">

### Closely related

- [Tendermint BFT Consensus Explained](/tendermint-bft-consensus-explained/) — An alternative Byzantine fault tolerant consensus with immediate finality
- [Epoch-Based Consensus: How Epochs Structure Validator Duties](/epoch-based-consensus-how-epochs-work/) — How epoch boundaries determine checkpoint timing
- [Staking Rewards Calculation](/staking-rewards-calculation/) — How Casper finality votes are incentivized through rewards and slashing
- [Proof-of-Stake](/proof-of-stake/) — The broader framework in which Casper operates

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Finality and consensus as core properties of blockchains
- [Byzantine Fault Tolerance](/byzantine-fault-tolerance/) — The formal security model underlying Casper
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — How finalized blocks enable trading and settlement

</div>
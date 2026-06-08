---
title: "Tendermint BFT Consensus Explained"
description: "How Tendermint consensus works through two-phase commit, safety guarantees, and liveness trade-offs under network partitions."
keywords:
  - tendermint consensus
  - byzantine fault tolerance
  - consensus algorithm
  - two-phase commit
  - blockchain consensus
image: "/svg/crypto.svg"
---

*The **Tendermint consensus** algorithm uses a two-phase voting process to finalize blocks instantly, assuming Byzantine fault tolerance with fewer than one-third malicious validators. Understanding its design means learning how its safety and liveness properties make explicit trade-offs under network partitions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tendermint BFT — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A leader-based Byzantine fault tolerant consensus achieving immediate finality over a committed set of validators.</div>

|   |   |
|---|---|
| **Fault threshold** | Tolerates up to 1/3 Byzantine (malicious) validators |
| **Finality** | Deterministic, immediate once 2/3 consensus reached |
| **Phases** | Prevote and precommit (two rounds per block) |
| **Leader role** | Proposer selects transactions; validators vote |
| **Liveness cost** | Pauses rather than forking if 1/3 or more are offline |
| **Confirmation time** | ~1–2 seconds per block under normal conditions |

</aside>

## How the two-phase voting process secures blocks

Tendermint's core innovation is replacing longest-chain rules with explicit voting. When a block is proposed, validators move through two phases before commitment:

1. **Prevote phase**: Each validator broadcasts a "prevote" message for the block it believes is valid (or nil if it sees no valid proposal). Once a validator has seen 2/3 of the set prevote for the same block, that block is "prevoted."

2. **Precommit phase**: Validators then broadcast "precommit" messages. If a validator has seen 2/3 prevotes for a block, it may precommit to it. Once 2/3 precommit, the block is locked and final.

This two-phase structure prevents conflicting finalizations. A validator that precommits to block A becomes "locked" to A; it cannot vote for block B in a later round without seeing 2/3 of the network prevote for B first. This lock mechanism is the bedrock of safety.

The process repeats for each new block: a single proposer (rotating by round) suggests a block, the network votes, and finality occurs when thresholds are crossed. No reorganization is possible once 2/3 precommit. This stands in sharp contrast to [longest-chain](/stock-market/) systems, where the canonical chain can shift.

## Safety guarantees under Byzantine actors

Tendermint's safety proof rests on a simple idea: at most 1/3 of validators can be Byzantine (malicious or faulty). Under that assumption, any two sets of 2/3 validators must overlap by at least 1/3, and that overlap includes at least some honest nodes.

The locking mechanism ensures that if honest validators precommit to block A in round *r*, no honest validator will precommit to a conflicting block B in any future round *r'* — because to do so, it would need to see 2/3 prevotes for B, which cannot happen if an honest minority saw 2/3 precommit to A in round *r*.

This property holds even if up to 1/3 of validators lie about their votes or go offline. As long as the 1/3 honest supermajority remains connected and follows the protocol, no two blocks can be finalized on conflicting branches.

The algorithm also detects Byzantine behavior. If a validator signs conflicting prevote or precommit messages, it can be proven and the validator slashed (losing stake). This accountability deters misbehavior in systems that adopt Tendermint.

## Liveness: when the network grinds to a halt

Safety comes at a cost: Tendermint sacrifices liveness—the ability to finalize new blocks—if 1/3 or more of validators are offline or partitioned. Rather than fork, it simply waits.

This is by design. If the network were to fork when 1/3 go offline, the fork rule would eventually cause both branches to claim 2/3 majorities, violating the safety guarantee. Instead, Tendermint's protocol requires 2/3 of the entire set; if fewer than 2/3 are responding, no block finalizes.

This creates a practical tension: a network can guarantee safety OR continue finalizing blocks, but not both during severe partitions. Most Tendermint deployments choose safety, accepting temporary halts over finality violations. Recovery is automatic: once the partition heals or offline validators restart, consensus resumes.

The time it takes to reach finality (or timeout and move to the next round) is known as the "block time" and is typically 1–3 seconds, depending on network conditions and the timeout configuration. If many validators are slow or unreliable, the protocol increases the timeout, further delaying finality.

## Proposer selection and round-robin fairness

Each round has a proposer—a single validator chosen to build the block. Tendermint uses a weighted round-robin: validators with more stake have a higher chance of being chosen as proposer in each round.

If the proposer is offline or its proposed block is invalid, validators move to the next round and a new proposer is chosen. This rotation ensures no single validator can monopolize block production and gives all validators a fair turn.

The proposer selects which transactions to include, subject to the protocol's validity rules. Honest proposers include high-fee transactions and valid pending mempool entries; Byzantine proposers might try to censor or reorder, but cannot force the network to finalize an invalid block, as validation rules are enforced during the voting phases.

## How the algorithm behaves under network delays

Tendermint's timeout mechanism accommodates variable network speeds. If a validator does not receive 2/3 prevotes within a timeout window, it broadcasts a "nil" prevote (voting for no block) and moves to precommit. If it does not see 2/3 precommits, it increments the round and waits for a new proposal.

The timeout increases with each failed round (exponential backoff), giving slower networks a chance to catch up. This flexibility means Tendermint can operate across a range of latencies—from low-latency LAN deployments to geographically distributed validators with higher round-trip times.

However, extremely slow or partitioned validators will cause the network to timeout repeatedly, slowing overall block production. This is a trade-off: the network can tolerate any network speed, but not at the cost of liveness during partitions.

## Applications and real-world deployments

Tendermint has powered [consensus systems](/proof-of-stake/) including the Cosmos Hub and numerous other proof-of-stake blockchains. Its deterministic finality and Byzantine fault tolerance make it attractive for systems that prioritize security and avoid re-orgs, such as supply-chain and permissioned ledger applications.

The algorithm's simplicity and well-understood security model have made it a reference point in blockchain consensus design, influencing systems like [Ethereum](/ethereum/) 2.0's finality gadget and other PoS variants.

## See also

<div class="wiki-seealso">

### Closely related

- [Epoch-Based Consensus: How Epochs Structure Validator Duties](/epoch-based-consensus-how-epochs-work/) — How validators organize into rotation schedules within Tendermint and similar systems
- [Casper FFG: Ethereum's Finality Gadget Explained](/casper-ffg-finality-gadget/) — An alternative finality mechanism layered on longest-chain rules
- [Staking Rewards Calculation](/staking-rewards-calculation/) — How validators earn compensation in systems using Tendermint-style consensus
- [Proof-of-Stake](/proof-of-stake/) — The broader family of stake-based consensus systems
- [Byzantine Fault Tolerance](/byzantine-fault-tolerance/) — The theoretical foundation underlying Tendermint's guarantees

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Consensus as a core building block of decentralized systems
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where consensus-secured tokens are traded

</div>
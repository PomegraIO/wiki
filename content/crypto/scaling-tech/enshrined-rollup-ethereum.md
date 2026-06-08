---
title: "Enshrined Rollups on Ethereum"
description: "An enshrined rollup bakes rollup logic directly into Ethereum's consensus layer, giving it protocol-level guarantees instead of relying on permissionless deployment."
keywords:
  - enshrined rollup ethereum
  - ethereum protocol rollups
  - base layer rollup
  - ethereum scaling
image: "/svg/crypto.svg"
---

*An **enshrined rollup** is a rollup whose logic and sequencing rules are built directly into Ethereum's consensus layer, as opposed to running as a separate smart contract. The idea is to give rollups the same protocol-level security and resource allocation that Ethereum's execution layer enjoys, rather than having them operate independently on top.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Enshrined Rollups — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Protocol-level rollup integration with Ethereum consensus.</div>

|   |   |
|---|---|
| **Current state** | Proposed and debated; not yet implemented |
| **Difference from today** | Today's rollups are smart contracts deployed permissionlessly; enshrined rollups would be baked into Ethereum core |
| **Key benefit** | Protocol-level sequencing fairness and resistance to MEV; potential for lower fees |
| **Main tradeoff** | Reduces modularity and flexibility; ties Ethereum's governance to rollup choices |
| **Candidate for** | Ethereum's next major upgrade cycle |

</aside>

## What Enshrined Rollups Mean

Today, when a Layer 2 rollup like Arbitrum or Optimism launches, it deploys a smart contract on Ethereum. That contract holds state, processes withdrawals, and validates proofs or fraud claims—but the rollup's sequencer (the entity that orders transactions) is a separate system operating independently. Ethereum's consensus layer doesn't know or care about the rollup's internals; it simply executes the contract code like any other DApp.

An **enshrined rollup** flips this model: Ethereum's consensus rules would explicitly include rollup sequencing and state transitions. Instead of a rollup contract running inside the EVM, the rollup would become part of the protocol itself, governed by the same validators who secure Ethereum's main chain.

The word "enshrined" comes from the idea of something being written into the foundation—not added on top, but baked in.

## Enshrined vs. Permissionless Rollups Today

The current model—what we might call "permissionless rollups"—has clear strengths and weaknesses.

**Strengths of permissionless rollups:**

- Any team can deploy a rollup without asking Ethereum for permission.
- Rapid innovation: new sequencing schemes, fraud-proof designs, and data structures can be tested without protocol upgrades.
- Modularity: rollups can choose their own validators, data availability strategies, and upgrade paths.
- No governance bloat: Ethereum's validator set doesn't grow with each new rollup.

**Weaknesses:**

- The sequencer chooses transaction order, creating **MEV (maximal extractable value)** opportunities; a user has no guarantee their transaction will be processed fairly.
- Rollup-specific risks: if the sequencer censors or goes offline, users may be stuck until a fallback mechanism (like a force-exit) activates.
- Fragmented liquidity: each rollup is its own system; bridging tokens between chains is friction-prone and trust-dependent.

**Enshrined rollups would aim to fix some of these problems:**

- The base layer consensus would order transactions in all enshrined rollups, eliminating per-rollup sequencer MEV at the top level.
- Users would have the same finality guarantees on an enshrined rollup as on Ethereum mainchain—no reliance on a separate sequencer's liveness.
- State roots could be included directly in Ethereum blocks, making exits and settling faster and cheaper.

## How Enshrined Rollup Sequencing Might Work

In a plausible enshrined-rollup design, Ethereum validators would do more than just validate transactions; they would also order rollup transactions.

**Sketch of the mechanism:**

1. Users submit rollup transactions to the public mempool (the same one as mainchain transactions).
2. Ethereum's proposer (the validator building the next block) orders both Ethereum transactions and rollup transactions, applying the same time-fair ordering rules to both.
3. Rollup execution happens "inside" the block-building process: validators compute state transitions for all enshrined rollups and include the updated state roots in the block.
4. Other validators verify both Ethereum and rollup execution; if a rollup state root is invalid, the block is rejected.

This would give rollups the same MEV-resistant guarantees that Ethereum's protocol-PBS (proposer-builder separation) is trying to achieve for mainchain: users get fair ordering without a sequencer playing intermediary.

## The Governance and Modularity Question

The biggest tradeoff of enshrining rollups is **protocol ossification**. Once a rollup design is part of Ethereum consensus, changing it requires a hard fork, which is politically difficult and slow. Today's permissionless rollups can pivot quickly; an enshrined rollup is locked in.

This raises hard questions:

- How many rollups should be enshrined? One, to avoid choice? Multiple, risking complexity?
- Who decides which rollup design is the "standard"? Ethereum governance, which is already contentious, would have even more at stake.
- What happens to innovative but niche rollup schemes that don't fit the enshrined template?

Some Ethereum researchers argue for **"enshrined enshrined rollups,"** in which Ethereum commits to a single, well-engineered rollup design; others prefer a hybrid: enshrine a basic rollup for simplicity and safety, while leaving room for permissionless rollups to experiment on the side.

## Efficiency Gains From Enshrinement

If rollup sequencing were moved into Ethereum's consensus, there are concrete efficiency wins:

**Reduced redundancy:** Today, Ethereum validators run Ethereum, and rollup validators run the rollup separately; some computation is duplicated. Enshrining merges the validator sets and eliminates duplication.

**Shared data availability:** If rollups are enshrined, Ethereum's data-availability layer (already being optimized with EIP-4844 blob space) serves rollups directly, rather than rollups negotiating separate DA with external providers.

**Cheaper exits:** Users exiting the rollup to Ethereum can do so with a simpler proof, since the rollup's state root is included in Ethereum blocks.

In theory, enshrined rollups could be 2–5x cheaper than permissionless ones for the same throughput.

## Risks and Unknowns

Enshrining rollups is a radical change, and several risks are worth naming.

**Liveness dependency:** If Ethereum consensus slows or stalls, all enshrined rollups are also stuck. Today's permissionless rollups can keep operating even if Ethereum is congested (though withdrawals are delayed).

**Governance complexity:** Every upgrade to an enshrined rollup requires Ethereum-level consensus. This could slow innovation or lead to political disputes.

**Increased validator requirements:** Validators would need to compute more state transitions and store more data, raising the hardware bar for running a node.

**Ecosystem fragmentation:** If not all Layer 2s are enshrined (likely), the ecosystem splits between protocol-level and application-level rollups, complicating bridges and liquidity.

## Current Thinking

As of 2026, enshrined rollups remain a thought experiment and long-term proposal rather than active roadmap. Ethereum's near-term focus is on EIP-4844, [danksharding](/danksharding/), and optimizing data availability for permissionless rollups.

Some researchers (notably at the Ethereum Foundation) have published sketches of enshrined-rollup designs; others worry that enshrinement locks Ethereum into a single scaling strategy when the ecosystem might benefit from pluralism. The debate is likely to heat up as Ethereum's throughput needs grow and permissionless rollups mature.

## See also

<div class="wiki-seealso">

### Closely related

- [Layer 2 Scaling](/layer-2-scaling/) — the category enshrined rollups serve
- ZK Rollup — a rollup flavor that could be enshrined
- [Optimistic Rollup](/optimistic-rollup/) — another rollup flavor relevant to enshrinement debates
- [Forced Transaction Inclusion in Rollups](/forced-transaction-inclusion-rollup/) — a related fairness mechanism
- [Volition: User-Chosen Data Storage in ZK Rollups](/volition-user-choice-data-storage/) — orthogonal scaling innovation

### Wider context

- [Ethereum](/ethereum/) — the protocol being extended
- Consensus Mechanism — the layer enshrined rollups would integrate with
- MEV and Maximal Extractable Value — a problem enshrined rollups aim to reduce
- [Danksharding](/danksharding/) — a complementary scaling technique

</div>

---
title: "Finality Time in PoS vs PoW: How Long Until a Transaction Is Irreversible"
description: "Comparing finality time proof of stake vs proof of work—why PoS offers deterministic guarantees while PoW relies on probabilistic depth."
keywords:
  - finality time proof of stake vs proof of work
  - deterministic vs probabilistic finality
  - blockchain transaction irreversibility
  - consensus finality speed
  - proof of work confirmation time
image: /svg/crypto.svg
---

*The **finality time proof of stake vs proof of work** difference is fundamental: PoS networks can define a block as truly irreversible after a fixed time (often minutes), while PoW networks only give probabilistic guarantees that grow stronger the deeper a block sits in the chain—making PoS faster and more predictable, but not necessarily more secure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Finality Comparison — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">PoS defines irreversibility by protocol rule; PoW requires economic waiting.</div>

|   |   |
|---|---|
| **Ethereum PoS finality** | ~13 min (2 epochs, 64 slots); economic guarantee at 2/3 of stake slashed if reversed |
| **Bitcoin (PoW)** | Probabilistic; 6 blocks (~60 min) gives ~99.9% safety; no hard irreversibility |
| **Polkadot PoS finality** | 2–4 blocks (~12 sec); GRANDPA gadget finalises once supermajority votes |
| **Solana PoS finality** | Varies; ~26 sec to ~13 min depending on network conditions |
| **Why PoW is slow** | Attacker can always recompute a longer fork; depth is psychological, not protocol law |

</aside>

## What finality means

**Finality** is the point at which a transaction is guaranteed irreversible—either by the protocol's rules or by economic incentives so strong that reversal is impossible. A transaction that is not final can still be unmade if the chain reorganises.

In proof-of-work, there is no formal finality defined by protocol—Bitcoin's rules do not forbid a 100-block reorg. Finality emerges from economic reality: if a block is 6 blocks deep (60 minutes of work on Bitcoin's 10-minute average), the attacker would need more cumulative hash power than the honest network has expended since that block. The probability of a successful reorg drops exponentially with depth.

In proof-of-stake, finality is explicit: once a block receives a 2/3+ supermajority vote from the active validator set (via a "finality gadget"), the protocol says it cannot be reverted without slashing. Ethereum calls this the "Casper FFG" (Friendly Finality Gadget). Polkadot uses GRANDPA. The difference is stark: PoW has no hard line; PoS draws one.

## Ethereum's two-epoch finality

Ethereum's consensus layer uses a **Casper FFG** mechanism that finalises a block once 2/3 of active validators have voted for a chain containing it, across multiple attestation slots. In practice, finality occurs roughly every 2 epochs—64 slots, or ~12.8 minutes.

Here is the flow: a block is proposed in slot 0. For it to become final, validators must include it in their fork-choice, attest to it, and build on it. By the start of the next epoch, 2/3 of validators have included that block in their votes. At that moment, Casper FFG triggers and the block is "final"—reversing it would require 2/3 of stake to be slashed.

The key difference from PoW: the block is not "probably irreversible after lots of work." It is irreversible by protocol definition, backed by a 2/3 supermajority putting $100+ billion at risk (Ethereum's staked capital). An attacker would need to control 2/3 of stake, be caught, and accept those validators being slashed out—an economic loss orders of magnitude larger than any transaction value.

## Bitcoin and deep confirmation

Bitcoin has no finality gadget. Instead, the convention is that transactions deeper than **6 blocks** (roughly 60 minutes) are safe. Why 6? Because the attacker would need to find >6 blocks faster than the honest network—a task with probability (q/(1−q))^6, where q is the attacker's hash share. With q=0.1 (10%), this is roughly 1 in 1 billion.

But this is probabilistic and informal. Bitcoin's protocol does not forbid a 100-block reorg. If an attacker controls 49% of hash power and mines in secret, they can eventually produce a longer chain and overtake the honest network. The deeper the target block, the more computational power must be expended; at some point, the economic cost exceeds any gain.

The practical result: Bitcoin transactions are "final" when the marginal cost of reversal exceeds the transaction value. For small payments, this may be 1–2 blocks; for large payments or exchanges, 6+ blocks. There is no hard rule.

## Polkadot's block-by-block finality

Polkadot's GRANDPA finality gadget finalises blocks more rapidly: once 2/3 of validators vote on a chain, that chain (and all prior blocks) is final, typically within 2–4 blocks (~12 seconds). This is faster than Ethereum because Polkadot uses a **commit-based** gadget: validators explicitly vote "I commit to this chain," and 2/3 commits trigger finality.

The trade-off is that GRANDPA requires all validators to be online and communicating; network partition or heavy congestion can stall finality. Ethereum uses a lighter-weight attestation model (validators attest per slot, not per block), which is more robust to degraded conditions but slower to finality.

## Why PoS finality is faster: a comparison

**PoW finality is slow because:**
- Attackers can always mine a longer chain (given enough time and hash power).
- Depth must be chosen empirically; deeper is always safer, but slower for users.
- There is no consensus signal—just a race between honest and attacker chains.

**PoS finality is fast because:**
- Attackers must control 2/3 of *staked* capital (not hash power, which is cheaper and fungible).
- Once 2/3 vote, the block is irreversible by protocol—no race.
- Validators are identified and slashable; the cost of attack is known and large.

On Ethereum, a block is final in ~13 minutes; the next person to spend its coins is guaranteed they can do so irreversibly. On Bitcoin, a merchant might wait 30–60 minutes for 6 confirmations. For high-value transactions, the difference compounds.

## The caveat: PoS requires honest majority

PoS finality assumes 2/3 of stake is honest. If 2/3 is compromised (an attacker controls $100+ billion of Ethereum or Polkadot stake), they can fork at will and finality breaks. PoW does not require honesty—an attacker needs computational majority, which is harder to maintain over time because mining hardware is replaceable.

In practice, both have large cost barriers to attack. Ethereum's 2/3 slashing requirement means attackers lose billions; Bitcoin's 51% hash majority requires buying or renting half the world's mining capacity, which is visible and costly. The nature of the cost is different—economic vs. computational—but both are steep.

## Solana's variable finality

Solana does not have a formal finality gadget. Instead, it relies on the network's validator set to vote on confirmation. Blocks are "confirmed" once validators have processed them and voted (via the PoH, Proof of History); "finalised" once supermajority voting confirms them. In practice, this takes 26 seconds to 13 minutes depending on network health.

The disadvantage is that Solana can experience consensus failures (forks, rollbacks) if the network partition or validators drop offline; there is no hard finality guarantee like Ethereum's Casper FFG. The advantage is speed under good conditions—Solana can move faster because confirmation is tied to block processing, not a separate voting round.

## Reorg risk in practice

Even after finality is "reached," attacks remain theoretically possible but economically absurd:
- Bitcoin: a 6-block reorg is ~1 in 1 billion with 10% attacker hash power.
- Ethereum: a 2-epoch reorg is impossible without 2/3 of stake being slashed for billions.
- Polkadot: a GRANDPA-finalised block reorg requires 2/3 stake and slashing.

In theory, both PoW and PoS can be attacked; in practice, the cost is prohibitive. PoS makes the cost explicit and irreversible (slashing destroys capital); PoW makes it probabilistic but economically irrational.

## Finality gadgets across PoS networks

Other PoS networks have adopted or designed finality gadgets:
- **Cosmos**: uses Tendermint BFT, which finalises on 2/3 vote per block (~5 sec).
- **Cardano**: uses Ouroboros, with ~2 epochs (~20 min) to finality.
- **Avalanche**: uses snowball consensus, with probabilistic finality (similar to PoW's depth).

The theme is that mature PoS networks tend toward explicit finality gadgets, because they offer speed and certainty. Networks that lack them (Avalanche, Solana sometimes) trade finality clarity for performance under adversary-free conditions—useful for high throughput but riskier during attacks or partition.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — the consensus model with deterministic finality
- [Proof of Work](/proof-of-work/) — the consensus model with probabilistic finality
- [Minimum Stake Requirements in Proof-of-Stake Networks](/proof-of-stake-minimum-stake-requirements/) — how stake size affects finality strength
- [Validator Set Rotation: How Networks Cycle Active Validators](/validator-set-rotation-mechanics/) — how rotation interacts with finality timing
- [Slashing](/slashing/) — the penalty mechanism that makes PoS finality irreversible

### Wider context

- Consensus Mechanisms — how blockchains reach agreement
- [Blockchain Fundamentals](/blockchain-fundamentals/) — distributed ledger principles
- [Bitcoin](/bitcoin/) — the original PoW system
- [Ethereum](/ethereum/) — the major PoS network

</div>

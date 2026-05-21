---
title: "Ethereum Merge"
description: "The Ethereum Merge was a major upgrade in September 2022 where Ethereum transitioned from proof-of-work mining to proof-of-stake validation. It reduced energy consumption by ~99.95% and represented a fundamental change to the network's consensus mechanism."
keywords:
  - ethereum merge
  - proof-of-stake
  - transition
  - validator
  - beacon chain
  - energy
image: "/svg/crypto.svg"
---

*The **Ethereum Merge** was a major network upgrade executed on 15 September 2022, where [Ethereum](/ethereum/) transitioned from [proof-of-work](/proof-of-work/) consensus (using miners) to [proof-of-stake](/proof-of-stake/) consensus (using validators). The upgrade reduced Ethereum's energy consumption by roughly 99.95% and was the most significant change to the network since its launch.*

<div class="wiki-hatnote">

This entry covers the Merge as a technical event. For Ethereum's broader history, see [Ethereum](/ethereum/); for the consensus mechanisms involved, see [proof-of-work](/proof-of-work/) and [proof-of-stake](/proof-of-stake/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ethereum Merge — key facts</div>

<img src="/svg/crypto.svg" alt="Ethereum transition from mining to staking" />

<div class="wiki-infobox-caption">The Merge: 99.95% energy reduction overnight.</div>

|   |   |
|---|---|
| **Date** | 15 September 2022 |
| **Transition** | [Proof-of-work](/proof-of-work/) → [proof-of-stake](/proof-of-stake/) |
| **Energy reduction** | ~99.95% |
| **Stake required** | 32 ETH per [validator](/validator/) |
| **Block time** | Unchanged (~12 seconds) |
| **Consensus finality** | Improved (faster) |
| **Miner rewards** | Eliminated (replaced by [staking](/staking/) rewards) |

</aside>

## The Beacon Chain and timeline

Ethereum's transition to proof-of-stake was not instantaneous. In December 2020, the "Beacon Chain" was launched as a parallel network running proof-of-stake consensus. The Beacon Chain existed independently for ~20 months while the main Ethereum network continued using proof-of-work.

This parallel running allowed:

- Testing the proof-of-stake mechanism on a live network.
- Accumulating [validators](/validator/) and staked ETH without disrupting existing users.
- Debugging unforeseen issues before the final merge.

## The technical merge

On 15 September 2022, the Ethereum mainnet (the proof-of-work chain) and the Beacon Chain (proof-of-stake) were merged. The mainnet adopted the Beacon Chain's consensus mechanism and continued building on it.

From a user's perspective, the change was invisible — transactions continued flowing, smart contracts continued executing. Only the underlying consensus mechanism changed.

## Energy efficiency

Before the Merge, [Ethereum](/ethereum/) consumed ~70 terawatt-hours (TWh) of electricity annually, equivalent to the consumption of some countries. This consumption came from miners running specialised hardware globally.

After the Merge, [Ethereum](/ethereum/) energy consumption dropped to roughly 0.03 TWh annually — a reduction of over 99.95%. This dramatic reduction addresses one of the primary criticisms of proof-of-work cryptocurrencies.

## The end of GPU and ASIC mining

Before the Merge, Ethereum miners used GPUs and ASICs. After the Merge, these became useless for Ethereum. Many miners transitioned to mining other proof-of-work coins ([Litecoin](/litecoin/), Dogecoin, etc.) or exited mining entirely.

This created a one-time economic shock: billions of dollars in mining equipment became obsolete, and many mining operations shut down.

## Staking and validator participation

The Merge enabled [staking](/staking/). Users who locked 32 ETH in the Beacon Chain before the Merge became validators after the Merge, earning staking rewards (~3–6% annually, depending on total stake).

Participation in staking grew significantly after the Merge, as users sought to earn yield. By 2024, roughly 16–18 million ETH (~40% of total supply) were staked.

## Transition challenges

The Merge was not without challenges. Some issues encountered:

- **Finality delays.** For the first few days after the Merge, finality (irreversibility of blocks) took longer than expected. Software updates fixed this.
- **MEV dynamics.** Proposer-builder separation and MEV (maximal extractable value) mechanisms had to be refined post-Merge.
- **Minority fork.** A small group of proof-of-work loyalists continued a "Ethereum Classic" fork (called ETC, though confusingly, the original Ethereum Classic already existed), though it garnered minimal adoption.

## Preparation for Shanghai and Dencun

The Merge was the first of several upgrades. [Ethereum Shanghai](/ethereum-shanghai/) (April 2023) enabled staking withdrawals (the ability to unstake and move ETH). [Ethereum Dencun](/ethereum-dencun/) (March 2024) improved layer-2 scaling through blob transactions.

These upgrades were enabled by the Merge's shift to proof-of-stake, as they require validator participation and were incompatible with proof-of-work.

## Market reception

The Merge was met with generally positive reception, particularly from environmental advocates. However, some community members viewed proof-of-stake as less secure or more "centralised" than proof-of-work.

Interestingly, the Merge did not lead to the expected price appreciation. [Ethereum](/ethereum/)'s price was relatively flat around the Merge event, suggesting the market had already priced in the transition.

## Comparison with Bitcoin

[Bitcoin](/bitcoin/) remains on [proof-of-work](/proof-of-work/) and has no announced plans to transition to proof-of-stake. Bitcoin maximalists argue that proof-of-work is more secure and decentralised; Ethereum developers argue that proof-of-stake's energy efficiency is vital for sustainability.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum/) — the network that merged
- [Proof-of-stake](/proof-of-stake/) — the mechanism after the Merge
- [Proof-of-work](/proof-of-work/) — the mechanism before the Merge
- [Validator](/validator/) — who validates after the Merge
- [Staking](/staking/) — how to earn rewards after the Merge
- [Ethereum Shanghai](/ethereum-shanghai/) — subsequent upgrade

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Bitcoin](/bitcoin/) — remains on proof-of-work
- Layer-2 — enabled by the Merge's design changes

</div>

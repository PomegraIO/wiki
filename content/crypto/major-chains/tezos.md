---
title: "Tezos"
description: "A self-amending blockchain where protocol upgrades are governed and executed on-chain, eliminating contentious hard forks."
keywords:
  - tezos
  - on-chain governance
  - self-amendment
  - proof of stake
  - formal verification
image: "/svg/crypto.svg"
---

*[Tezos](/tezos/) is a [proof-of-stake](/proof-of-stake/) blockchain with an unusual property: it can upgrade itself through on-chain governance without requiring miners or developers to fork the code and run incompatible versions. Proposed protocol changes are voted on by stakeholders, implemented as a new smart contract that becomes the network's rules, and activated in lockstep across all nodes—no contentious split, no community schism.*

<div class="wiki-hatnote">

For the Tezos cryptocurrency, see [Tezos Foundation](https://tezos.com). For governance concepts generally, see Algorithmic governance.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tezos — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A self-amending blockchain where stakeholders vote on protocol changes.</div>

|   |   |
|---|---|
| **What it is** | A [proof-of-stake](/proof-of-stake/) blockchain with on-chain governance |
| **Consensus mechanism** | Liquid proof-of-stake (delegated) |
| **Governance model** | Voter-approved amendment periods |
| **Block time** | ~30 seconds |
| **Transaction finality** | ~1 minute |
| **Native asset** | Tez (XTZ) — staking, gas, voting power |
| **Smart contract language** | Michelson (stack-based, formally verifiable) |

</aside>

## The hard fork problem

When [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/) need to change their rules—say, to fix a security bug or increase throughput—they face a coordination problem. Developers propose a change, implement it in client software, and ask all miners and node operators to upgrade. If consensus is strong, everyone upgrades and the fork is "soft" (backward-incompatible changes become mandatory). If consensus fractures, the network splits: [Bitcoin Cash](/bitcoin-cash/) emerged this way from Bitcoin in 2017 over a block-size dispute. The result is fragmented value, community acrimony, and investors holding two competing versions.

Tezos was designed to avoid this. Instead of debating off-chain and coordinating a software release, governance happens on-chain. There is one true protocol, one set of rules, and changes to those rules are enacted through a formal process that has supermajority buy-in baked in.

## How Tezos's amendment process works

Tezos's governance unfolds in several stages, each lasting a fixed number of blocks (currently about two weeks per period).

**Proposal period**: Developers submit a hash of a proposed protocol amendment (a new Tezos codebase implementing the change). Token holders vote with their stake. The top proposal advances.

**Exploration period**: A more formal review. Token holders signal whether they want to explore this proposal further. If at least 20% participation and a supermajority (67%) agree, it moves forward.

**Testing period**: The proposal is activated on the network as a "testnet" version of the protocol. Real blocks are produced under the new rules, real users can transact and test, and the community gauges the change's maturity and impact.

**Promotion period**: Token holders vote on whether to activate the proposal as the canonical protocol. Another supermajority is required.

**Activation**: If promotion passes, the new protocol code becomes law on all nodes at a pre-agreed block height. No forking. No alternative clients. One network, one set of rules.

This cycle repeats; Tezos's protocol has evolved through dozens of amendments since launch. Notably, changes include increasing gas limits, introducing new smart contract languages, and adjusting the economic parameters of staking.

## Why voting is on-chain

One might ask: could Tezos just use off-chain governance? Executives and miners vote, publish a decision, and release software. The answer is that off-chain governance concentrates power. In [Proof-of-Work](/proof-of-work/) systems, miners decide which code to run, giving them veto power. In [Proof-of-Stake](/proof-of-stake/) systems without on-chain voting, token holders have no direct mechanism to contest; core developers could propose a change and claim it's essential, and if token holders disagree, their only recourse is to exit (sell) or hard fork.

On-chain voting makes protocol changes a contract: stakeholders explicitly ratify new rules. Supermajority thresholds prevent tyranny of a slim majority. Anyone holding Tez can vote (or delegate their vote to a baker—a validator—who votes on their behalf). The governance process is transparent and auditable on the chain itself.

## Formal verification and Michelson

Tezos's design reflects concern with correctness. Smart contracts on Tezos are written in Michelson, a stack-based language intentionally designed to be amenable to formal verification. Formal verification is a mathematical proof that code behaves as specified—stronger than testing. This comes at a cost: Michelson is more constrained than Solidity (Ethereum's language), and development is slower.

The bet is that this friction, and the emphasis on proving correctness, reduces exploits and catastrophic bugs. Certainly, Tezos has not seen the sort of billion-dollar smart contract failures that have plagued Ethereum (though it's also a smaller ecosystem).

## Liquid proof-of-stake and participation

Tezos uses liquid [proof-of-stake](/proof-of-stake/), where anyone with 6,000 Tez can become a baker (validator) and participate in consensus. Most token holders delegate their stake to a baker, and the baker shares rewards with delegators. This is liquid: you can undelegate at any time and switch validators, or remove your stake.

The staking pool is dynamic. Bakers earn rewards proportional to the stake they secure (plus delegations). This creates pressure toward decentralization: large bakers cannot monopolize rewards, because delegators can easily move to smaller bakers who may offer better terms.

Voting power is tied to stake. The more Tez you hold (or have delegated to you), the more weight your vote carries. This is a standard approach in [proof-of-stake](/proof-of-stake/) systems, though it means wealthy stakeholders have outsized influence—a criticism Tezos shares with other PoS chains.

## Trade-offs in self-amendment

Self-amendment is not without friction. Protocol changes must pass multiple voting periods over several weeks. If a critical security bug is discovered, patching is slower than in centralized systems (or even than in Bitcoin/Ethereum, where miners can coordinate upgrades relatively quickly). Tezos's governance model assumes that supermajority consensus is valuable and that waiting for it is worth the security-by-consensus trade-off.

Additionally, not all stakeholders participate in voting. Typically, 30–50% of tokens vote in any given proposal. This means a vocal minority of engaged token holders effectively decides protocol direction, which may not reflect the true preference distribution if most holders are passive.

The amendment process is also constitutional in one sense: you cannot amend the amendment process itself without first amending the amendment process—a paradox Tezos has had to navigate carefully. Some changes to governance structure must be proposed and voted like any other proposal, creating a bootstrapping question.

## Real-world amendments

Tezos has amended itself many times since launch in 2018. Early upgrades added performance improvements and new smart contract languages (LIGO, a more traditional syntax). Later upgrades introduced new financial mechanisms: Tezos 10 (Babylon) added liquidity baking (a built-in market maker), and Tezos 14 (Lima) adjusted inflation and staking economics.

These changes have been substantive and sometimes contentious. Some in the community have argued the governance process is too slow; others argue recent amendments have favored certain stakeholders over others. But crucially, the network has never split over a governance disagreement. The process, while imperfect, works.

## Contrast with other governance models

[Algorand](/algorand/) and [Hedera Hashgraph](/hedera-hashgraph/) have different governance structures—Hedera is governed by a council of public institutions, Algorand uses a different voting model. [Ethereum](/ethereum/) has no on-chain governance; upgrades are proposed and discussed off-chain, and core developers implement consensus. [Bitcoin](/bitcoin/) uses a hybrid: miners vote implicitly by choosing which rules to enforce, and developers propose changes.

Tezos's model is unique in making governance fully on-chain and supermajority-required. It is a bet that transparency and explicit stakeholder buy-in matter more than speed and executive decisiveness.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of stake](/proof-of-stake/) — Tezos's consensus mechanism
- Michelson — Tezos's formally verifiable smart contract language
- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger concepts
- [Near Protocol](/near-protocol/) — another layer-1 with different scaling approach
- [Algorand](/algorand/) — alternative layer-1 with pure PoS finality
- [Hedera Hashgraph](/hedera-hashgraph/) — enterprise blockchain with council governance

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where Tez tokens trade
- [Distributed ledger](/distributed-ledger/) — foundational tech for blockchains
- Formal verification — mathematical proof of correctness

</div>

---
title: "Tezos On-Chain Governance Explained"
description: "How Tezos lets bakers propose, vote on, and automatically apply protocol upgrades without hard forks through its five-period amendment process."
keywords:
  - tezos on-chain governance
  - tezos protocol upgrade voting
  - tezos amendment process
  - tezos bakers governance
image: /svg/crypto.svg
---

*Tezos is a **[blockchain-fundamentals](/blockchain-fundamentals/)** network that upgrades itself through formal, on-chain voting rather than informal consensus or a central authority. **Tezos bakers**—operators who validate blocks—and **token holders** collectively propose and vote on protocol changes, and approved amendments automatically roll out across the network without a disruptive hard fork.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Tezos On-Chain Governance — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency topics." />

<div class="wiki-infobox-caption">Five-period cycle ensures deliberate, transparent protocol upgrades.</div>

|   |   |
|---|---|
| **Voting participants** | Tezos bakers (validators) and delegators |
| **Amendment process** | Five periods: proposal, exploration, cooldown, promotion, adoption |
| **Each period length** | ~2 weeks (28,800 blocks) |
| **Voting mechanism** | Quorum-adjusted supermajority (80% approval required) |
| **Hard forks required** | Zero; upgrades apply automatically |
| **Failed proposals** | Dropped; start over with new proposal period |

</aside>

## Why Tezos chose on-chain governance

Most [blockchain-fundamentals](/blockchain-fundamentals/) networks like Bitcoin and Ethereum rely on **informal governance**—core developers propose changes, the community debates them on forums and social media, miners or validators adopt upgrades, and everyone else follows or forks off. This is decentralized in theory but often controlled by a small number of developers and mining pools in practice. Disputed upgrades can split the network (Ethereum's fork to Ether Classic after the DAO hack).

Tezos took a different approach from launch in 2018: **formal, on-chain governance**. Every proposed upgrade is voted on-chain, and if it wins by the required supermajority, the network automatically adopts it. No informal consensus needed, no fork risk if dissenters lose the vote—dissidents can exit or start their own fork, but the main chain evolves in a predictable way.

The design assumes that if people use Tezos tokens (XTZ), they have "skin in the game" and will vote rationally to improve the network rather than destroy it. Bakers—who earn rewards for validating—have even stronger incentives to maintain and grow the network.

## The five-period amendment cycle

Tezos upgrades follow a fixed, five-period schedule. Each period lasts approximately 2 weeks (28,800 blocks at roughly 60-second block times). This rigid structure ensures time for deliberation and prevents rushed governance.

**Period 1: Proposal Phase**
Bakers submit upgrade proposals. Any baker can submit up to 20 proposals per cycle. Proposals are typically written in **Michelson** (Tezos's smart contract language) or bundled as protocol specifications. The proposals that receive the most upvotes from bakers advance to the next period. The top-ranked proposal wins. If no proposals gain traction, the cycle restarts.

**Period 2: Exploration Phase**
The winning proposal from the proposal phase goes to a vote. Bakers vote "yes" or "no" on the proposal itself. The goal is to test whether there's *interest* in the proposal, not final approval. If the proposal reaches a supermajority (currently 80% yes votes) and quorum (currently at least 40% of all bakers participate), it advances. If it fails, the cycle restarts at the proposal phase.

**Period 3: Cooldown Period**
A waiting period where bakers and the wider community assess the proposal in more detail. No voting occurs. Developers can publish test reports, community members discuss implications, and delegates can shift their vote allocation if they wish. This period prevents hasty governance and surfaces issues.

**Period 4: Promotion Phase**
A second vote on the same proposal. This time, the bar is explicit: 80% yes votes and 40% quorum again. The vote confirms that despite cooldown debate, the proposal still has strong support. If it fails, the cycle restarts. If it passes, the proposal moves to adoption.

**Period 5: Adoption Phase**
A final vote to confirm. If the proposal reaches the supermajority again, it's adopted. The protocol upgrade is encoded in the proposal itself and automatically activates at a predetermined height (block number). No manual deployment by node operators is needed—the upgrade "just happens" across the network.

## Quorum and supermajority mechanics

Quorum is the percentage of bakers who must participate in a vote. Tezos adjusts quorum dynamically: it starts at a baseline (historically ~40% in the Ithaca upgrade) and then drifts toward the previous period's actual participation. If 60% of bakers voted last period, the current period's quorum target rises slightly. This prevents a small, engaged minority from forcing through unpopular changes.

The **supermajority** requirement is 80% of voting power. If 50% of bakers participate and 80% of those vote yes, the proposal passes (only 40% total support). This is much lower than Bitcoin's informal supermajority (which is vaguely defined and often 95%+ in practice), but Tezos compensates by requiring both quorum *and* explicit voting.

Bakers can also **delegate** their voting power to other bakers or governance experts, so most XTZ holders vote indirectly through a baker they trust.

## No hard forks, automatic activation

Once an amendment is adopted, the upgrade is baked into the proposal code. At a predetermined block height (usually around the time the adoption period ends), every node on the network automatically switches to the new protocol rules. There's no period where some nodes run old code and others run new code—the switch is atomic and coordinated.

This eliminates the messy **hard fork** scenario that plagues other blockchains. When Bitcoin or Ethereum upgrades, they set a target block height, core developers release the new client code, and node operators must manually download and restart. If operators don't upgrade, their nodes fork off and stop syncing with the main chain. Disputes over whether to upgrade can split the chain permanently (Ethereum Classic, Bitcoin Cash, etc.).

Tezos avoids this by embedding the upgrade rules in the on-chain code itself. Nodes don't need a software download; they simply apply the new rules at the designated block height. Dissenting operators can refuse to upgrade and will cease syncing, but they're making an explicit choice to fork, not accidentally splitting the network via outdated code.

## Historical amendments and their outcomes

Tezos has completed several amendment cycles:

- **Babylon** (2019): Improved scripting language and governance mechanics.
- **Carthage** (2020): Gas model optimization.
- **Delphi** (2020): Reduced storage costs (critical for smart contract adoption).
- **Edo** (2021): Introduced Sapling privacy and tickets, increased contract expressiveness.
- **Florence** (2021): Gas improvements and new voting rules (introduced the quorum drift mechanism).
- **Granada** (2021): Reduced block time and improved consensus.
- **Hangzhou** (2022): View and Timelock features for smart contracts.
- **Ithaca** (2023): Further Proof-of-Stake improvements.

All of these passed their governance cycles and activated automatically. No failed amendments have halted the network; proposals that fail simply restart at the proposal phase.

## Criticisms and limitations

Critics argue that Tezos's governance is *too formal*. The five-period, 10-week cycle means urgent security fixes take months to roll out. Ethereum, despite its informal governance, can deploy emergency patches in days if needed. Bitcoin's stability is often praised precisely because upgrades are conservative and rare.

Voter apathy is also a risk. If most bakers or delegators don't participate, a small, organized minority could push through changes that wouldn't win in a genuine supermajority. Tezos's quorum-drift mechanism helps, but participation is still lower than ideal in some periods.

Finally, proposing complex upgrades through on-chain voting requires sophisticated technical knowledge. The community relies on a small group of core developers to write coherent proposals, which reintroduces informality and centralization risk—the governance structure is on-chain, but the *decision-making* happens off-chain in developer forums and discussions.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain-fundamentals](/blockchain-fundamentals/) — overview of how blockchains work and what governance means
- [Proof-of-stake](/proof-of-stake/) — Tezos's consensus mechanism and how bakers earn rewards
- [Smart-contract](/smart-contract/) — Tezos smart contracts written in Michelson
- [Ethereum](/ethereum/) — comparison: Ethereum's informal governance and difficulty upgrading
- [Bitcoin](/bitcoin/) — comparison: Bitcoin's conservative, slow-moving governance model

### Wider context

- [Distributed-ledger](/distributed-ledger/) — broader decentralized governance challenges
- [Cryptocurrency-exchange](/cryptocurrency-exchange/) — how Tezos tokens (XTZ) are traded and staked
- Consensus-mechanism — other blockchain governance and upgrade models
- Fork — hard forks and chain splits caused by governance disputes
- Token — Tezos XTZ token and its voting rights

</div>

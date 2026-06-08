---
title: "Selfish Mining"
description: "A block-withholding strategy that lets a minority miner earn outsized rewards by controlling the timing of block release."
keywords:
  - selfish mining
  - block withholding
  - mining strategy
  - mining incentives
  - blockchain attacks
image: "/svg/crypto.svg"
---

*Selfish mining is a rational but non-cooperative strategy in which a miner withholds valid blocks from the network, releasing them strategically to gain a competitive advantage over honest miners. Though it requires only a fraction of the network's hashing power, selfish mining can generate returns that exceed a miner's proportional share of rewards.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Selfish Mining — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain consensus mechanisms." />

<div class="wiki-infobox-caption">A minority miner's advantage through strategic block suppression.</div>

|   |   |
|---|---|
| **What it is** | A strategy where a miner withholds solved blocks to maintain a private lead on the chain |
| **Also called** | Block withholding attack, strategic mining |
| **Requires** | A significant fraction of network hashrate (typically 33%+ for profitability) |
| **Risk to network** | Reduced [blockchain-fundamentals](/blockchain-fundamentals/) finality; incentive misalignment |
| **First described** | 2014 academic paper ("Majority is not Enough") |
| **Countermeasures** | Difficulty adjustments, faster block times, alternative [fork-choice-rule](/fork-choice-rule/) designs |

</aside>

## How the attack works

In a standard [proof-of-work](/proof-of-work/) system, miners compete to solve a difficult mathematical puzzle. The first to publish a valid solution earns the block reward. Honest miners immediately broadcast their blocks so the network can validate them and extend the chain.

Selfish miners operate differently. When they solve a block, they keep it secret instead of broadcasting it. They continue mining on their private branch, building a private chain ahead of the public one. This hidden advantage—called a "lead"—persists as long as their private blocks remain unreleased.

The strategy hinges on block timing. If the public chain catches up and matches the length of the private chain, the selfish miner broadcasts their private blocks immediately. Because they arrived first, the network accepts them as the canonical history, making all blocks mined on the public branch orphaned and worthless to their solvers. The selfish miner captures not only their own rewards but also invalidates the work of honest miners who mined the competing branch.

## Why it remains rational

The intuition behind selfish mining violates standard game theory intuition: a miner with, say, 40% of the network's hashrate should earn roughly 40% of all rewards. But selfish mining breaks that rule. By orphaning competitors' blocks, the attacker reduces the effective return on honest mining, making their own relative share larger.

The strategy requires a threshold. A miner with fewer than roughly 25% of total hashrate will struggle to sustain a profitable lead; even if they solve blocks faster than the public chain advances, the probability of detection and the cost of mining in isolation usually exceed the gain. But a miner with 33% or more can systematically outpace honest miners, making selfish mining economically rational—even if it harms the entire network.

This creates an uncomfortable incentive problem. In a [proof-of-work](/proof-of-work/) system like Bitcoin, miners are supposed to be profit-maximizers, yet the existence of a profitable non-cooperative strategy means that a sufficiently large miner has an incentive to deviate from the honest protocol, even if the deviation damages transaction finality and network security.

## Detection and outcomes

Selfish mining is difficult to detect in real time. Public observers see only the blocks that miners release, not the private chains they may be holding. However, statistical anomalies—unexpected orphaning patterns or unusually fast block discoveries—can hint at the presence of a private fork.

Once a selfish mining attack is recognized, the network's response depends on its governance. Bitcoin and Ethereum have no built-in mechanism to punish selfish miners; they operate on the assumption that such attacks are either infeasible or economically irrational at scale. Most protocols rely instead on the social friction of coordination: launching a full selfish mining operation requires significant capital and technical sophistication, and the longer it runs, the more likely participants are to face legal or regulatory pressure.

Proof-of-stake systems present a different profile. In [proof-of-stake](/proof-of-stake/) networks, participants put up collateral ("stake") that can be forfeited if they behave badly. Slashing conditions—automatic penalty mechanisms—can be designed to punish withholding or other non-cooperative acts, making selfish strategies far riskier than in proof-of-work.

## Defences and design responses

Protocol designers have explored several countermeasures. One approach is to shorten block times, reducing the window in which a private fork can exist undetected. Another is to adjust [fork-choice-rule](/fork-choice-rule/) logic to penalise chains with suspicious orphaning patterns or to reward the first honest announcement of a block, not just its presence in the chain.

Some proposed protocols incorporate explicit selfish-mining resistance. Proof-of-work variants like CryptoNote adjust difficulty based on inter-block arrival times, making it harder to maintain an undetected lead. Proof-of-stake designs like Casper include heavy penalties for withholding and for building on competing forks, raising the cost of selfish behaviour to unsustainable levels.

The practical reality is that selfish mining has remained largely theoretical. No major blockchain has suffered a sustained, documented selfish mining attack. This may be because the coordination and capital required exceed what a single attacker possesses, or because the reputational and legal risk deters would-be attackers. Nevertheless, the attack highlights a fundamental tension in decentralised systems: the protocol's security depends partly on participants choosing to follow the rules even when breaking them might be profitable.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Work](/proof-of-work/) — the consensus mechanism vulnerable to selfish mining
- [Fork Choice Rule](/fork-choice-rule/) — how nodes select the canonical chain; design affects selfish mining feasibility
- [51% Attack](/51-percent-attack/) — majority-control attack; selfish mining requires less power but operates differently
- Block Reward — the incentive that selfish mining aims to capture disproportionately
- Consensus Mechanism — the broader class of protocols selfish mining exploits

### Wider context

- [Proof of Stake](/proof-of-stake/) — alternative consensus with built-in selfish mining resistance
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where miners liquidate rewards and execute arbitrage
- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundational concepts for understanding mining economics
- [Hash Rate](/hash-rate/) — the denominator in selfish mining feasibility calculations

</div>

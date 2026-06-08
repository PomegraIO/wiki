---
title: "Fork Choice Rule"
description: "The algorithm that nodes use to select the canonical chain when competing branches exist, ranging from longest-chain rules to sophisticated graph-based approaches."
keywords:
  - fork choice rule
  - longest chain rule
  - GHOST algorithm
  - LMD-GHOST
  - blockchain consensus
image: "/svg/crypto.svg"
---

*A fork choice rule is the algorithm that determines which branch of a blockchain's history nodes accept as canonical when the chain splits. These rules range from simple (longest chain wins) to sophisticated graph-weighted schemes that explicitly penalise attacks. The choice of rule profoundly affects a network's security, finality guarantees, and vulnerability to attacks like [selfish-mining](/selfish-mining/) and [51-percent-attack](/51-percent-attack/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fork Choice Rule — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain consensus mechanisms." />

<div class="wiki-infobox-caption">The rule nodes follow when chain forks create competing versions of history.</div>

|   |   |
|---|---|
| **What it is** | An algorithm determining the canonical chain when multiple valid branches exist |
| **Also called** | Chain selection rule, consensus rule, [fork-choice-rule](/fork-choice-rule/) algorithm |
| **Scope** | Applies across [proof-of-work](/proof-of-work/), [proof-of-stake](/proof-of-stake/), and hybrid systems |
| **Key examples** | Longest chain, GHOST, LMD-GHOST, Tendermint |
| **Security tradeoff** | Simplicity vs. resistance to specific attacks |
| **Updates** | Protocol-level changes require hard or soft forks across the network |

</aside>

## Why forks occur and why rules matter

Blockchains split whenever multiple valid blocks are mined or proposed for the same position. In a decentralised network with latency, two miners may simultaneously solve a block, and different portions of the network receive them in different orders. Alternatively, an attacker may deliberately broadcast a competing block to fork the chain.

Without a clear rule for which fork to follow, the network fragments. Some nodes accept one branch, others accept another, and there is no consensus. The fork choice rule prevents this chaos. It gives every node a deterministic way to select a single canonical chain, so that despite network delays and adversarial behaviour, the system converges on a shared history.

The choice of rule is not cosmetic. Different rules have different security properties. A rule that is simple and fast might be vulnerable to [selfish-mining](/selfish-mining/). A rule that is highly resistant to attacks might require expensive computation or long finalisation times.

## The longest-chain rule

Bitcoin uses the simplest possible fork choice rule: accept the chain with the most cumulative proof-of-work, which is almost always the longest chain. When two branches exist, nodes follow the longer one. The attacker must control more than 50% of the network's hashrate to consistently build a longer chain than honest miners, making the rule secure against most adversaries.

The longest-chain rule has three major strengths. It is simple to implement, quick to compute, and it aligns incentives: an honest miner's best strategy is to mine on the longest known chain rather than attempt strategic behaviour. 

But the rule has weaknesses. It does not actively penalise selfish or attacking behaviour—it only requires that attackers reach a sufficiently high threshold. A miner with 49% of hashrate might execute a profitable [selfish-mining](/selfish-mining/) attack. The rule also does not distinguish between different types of work; in principle, a more efficient attacker could do more damage than the rule's mathematics suggest. And forks can persist for longer than necessary because there is no explicit incentive to converge quickly.

## GHOST and Ommer blocks

As block times shortened and network latency became noticeable, the longest-chain rule's inefficiency became problematic. Ethereum faced this issue: at a twelve-second block target, significant network delays meant many valid blocks were orphaned, wasting their security contribution.

Ethereum solved this with GHOST (Greedy Heaviest-Observed Subtree), a refinement of the longest-chain rule. Instead of counting only the blocks in the main chain, GHOST counts all valid blocks that nodes have observed, including orphaned blocks (called "ommer blocks" or "uncles"). A chain that includes more total work—even if that work is spread across multiple branches—is weighted higher than one with fewer total blocks.

GHOST improves security by rewarding all work, not just work on the main chain. An attacker who wants to build a longer competing fork must now outpace not just the main chain's work but also the work of all ommer blocks the honest network has accumulated. This makes attacks significantly more expensive.

Ethereum paid a price for this improvement: GHOST is more computationally expensive to evaluate, and the ommer reward structure added complexity to the protocol. But the security gain justified the cost.

## LMD-GHOST and proof-of-stake

As Ethereum transitioned to proof-of-stake, a new fork choice rule became necessary. Proof-of-stake has different timing and liveness properties than proof-of-work: validators propose blocks in rounds, and there is no notion of hashrate.

Ethereum 2.0 adopted LMD-GHOST (Latest Message Driven Greedy Heaviest-Observed Subtree). The algorithm weighs branches not by cumulative work but by the total stake voting for them. When a branch accumulates votes from a majority of validators, it becomes canonical. Validators are economically incentivised to vote for the same branch via slashing: if you vote for a block and it is later reverted, your stake is forfeited.

LMD-GHOST, combined with Ethereum's Casper finality mechanism, creates very fast consensus. A block is often considered final after two Ethereum epochs (roughly twelve minutes). No reorg deeper than that is possible without destroying the attacker's stake. This is much faster than Bitcoin's probabilistic finality, which requires many blocks of confirmation.

## Other rules and tradeoffs

Tendermint and similar Byzantine Fault Tolerant (BFT) systems use explicit voting and state machines to choose the canonical chain. Validators vote on blocks, and a block becomes final once a supermajority (often two-thirds) of validators vote for it. This offers very fast finality but requires validators to actively participate.

Other protocols explore middle grounds. Some use variations of GHOST tailored to their specific consensus model. Others introduce fork choice rules that explicitly penalise withholding or other adversarial behaviours, making certain attacks provably unprofitable.

The proliferation of rules reflects a fundamental tradeoff: simpler rules are easier to understand and implement but may leave exploitable gaps. Sophisticated rules can be more robust but add complexity that may hide subtle bugs. Choosing the right rule is one of the most consequential decisions in a blockchain's design.

## Evolution and governance

Fork choice rules can be updated, but only through network consensus. A soft fork may change the rule in a backward-compatible way, so that nodes running old code still accept the new chain. A hard fork requires all nodes to upgrade; any that do not are left behind on an old chain.

Changing a fork choice rule is a significant event. In 2016, Ethereum's fork choice rule was modified to address problems with high reorg rates. In 2024, Ethereum's developers have proposed further refinements to LMD-GHOST to reduce latency and improve attack resistance. Such changes must be widely tested and socially agreed before deployment, because a poorly chosen rule can break consensus or introduce new attack vectors.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Work](/proof-of-work/) — the consensus mechanism using longest-chain rules
- [Proof of Stake](/proof-of-stake/) — the mechanism using voting-weighted fork choice
- [51% Attack](/51-percent-attack/) — majority attack that exploits fork choice rules
- [Selfish Mining](/selfish-mining/) — strategic block withholding that fork rules can defend against
- Consensus Mechanism — the overarching protocol that embeds the fork choice rule

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundational concepts in blockchain architecture
- [Proof of History](/proof-of-history/) — alternative ordering mechanism that reduces fork choice complexity
- [Byzantine Fault Tolerance](/byzantine-fault-tolerance/) — formal model for consensus under adversarial conditions
- [Hash Rate](/hash-rate/) — the metric in longest-chain rule calculations

</div>

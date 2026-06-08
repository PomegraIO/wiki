---
title: "51% Attack"
description: "A majority-control attack in which a single entity commanding over half the network's consensus power can double-spend and censor transactions."
keywords:
  - 51% attack
  - majority attack
  - double spending
  - consensus power
  - blockchain attacks
image: "/svg/crypto.svg"
---

*A 51% attack occurs when a single party controls more than half of a blockchain's consensus power—whether through accumulated hashrate in [proof-of-work](/proof-of-work/) systems or staked capital in [proof-of-stake](/proof-of-stake/) networks. This majority control allows the attacker to rewrite transaction history, double-spend coins, and censor transactions on a massive scale.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">51% Attack — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain consensus mechanisms." />

<div class="wiki-infobox-caption">Majority control enables chain rewriting and transaction reversal.</div>

|   |   |
|---|---|
| **What it is** | Control of over 50% of consensus power to rewrite or censor the blockchain |
| **Also called** | Majority attack, 50% attack |
| **Required consensus share** | Over 50% of hashrate (PoW) or staked capital (PoS) |
| **Primary threats** | Double-spending, transaction censorship, [fork-choice-rule](/fork-choice-rule/) hijacking |
| **Detection** | Statistical anomalies in block production or sudden chain reorgs |
| **Feasibility varies** | Extremely expensive for major networks; realistic for small chains |

</aside>

## The mechanics of majority control

In any blockchain, consensus nodes or miners follow a [fork-choice-rule](/fork-choice-rule/) to decide which version of the chain is canonical. The simplest such rule—used in Bitcoin—is "the longest valid chain wins." An attacker with 51% of the network's hashrate can mine blocks faster than all honest nodes combined. Over time, their private chain grows longer than the honest chain, and when they release it, the network adopts it as the true history.

Once the attacker's chain becomes canonical, all transactions on the old, orphaned branch are reversed. If an attacker transferred coins to a merchant on block 100,000, then mined a longer alternative chain that excludes that transaction, the coins revert to their original owner. The merchant's payment disappears. This is double-spending in its most powerful form.

Proof-of-stake systems face identical vulnerabilities. An attacker who accumulates over 50% of the total staked capital can propose blocks at will and vote to finalise their version of the chain. Honest validators cannot overrule them. The attacker can rewrite history, censor transactions, and reverse finality—all while their stake remains intact.

## Double-spending and finality

The core consequence of a 51% attack is the destruction of transaction finality. In an honest network, a transaction buried under several blocks is cryptographically irreversible. With a 51% attack, no depth is safe. The attacker can mine an arbitrary number of blocks in secret, then release a fork that resets the entire chain to any previous state.

This makes merchants vulnerable. An attacker could send a large payment, wait for confirmation, then reclaim the coins by rewriting history. The longer the merchant waits—the deeper the transaction sits—the more work the attacker must perform. But with 51% of the network's power, the attacker can eventually outpace any honest opposition, no matter the depth.

Proof-of-stake networks address this partly through "economic finality." A transaction is considered final once enough validators have staked penalties (called slashing) on its inclusion. An attacker would have to destroy their own stake to reverse it—a cost that exceeds any gain from double-spending. But only if the protocol is designed correctly. Flawed implementations can still be attacked.

## Censorship and chain capture

A 51% attacker need not rewrite the entire chain. They can simply exclude transactions they dislike. By mining only blocks that omit certain transactions, they can prevent those transactions from ever being confirmed. This is censorship at the consensus layer.

Censorship is sometimes harder to detect than double-spending. If an attacker censors transactions from a rival exchange or political opponent, the censored user may not immediately notice—they see that their transaction is unconfirmed, but cannot prove why. Over time, patterns emerge: certain addresses are always excluded, certain types of transactions never confirm. At that point, the attack is obvious, but the damage is done, and the attacker's majority power means the network cannot reject their blocks.

## Cost and feasibility

The primary defence against 51% attacks is cost. For major networks with billions of dollars in consensus power, acquiring 51% is astronomically expensive. Mining 51% of Bitcoin's hashrate would require hundreds of millions of dollars in hardware and electricity. Accumulating 51% of Ethereum's staked capital would require buying roughly thirty billion dollars' worth of ether. These costs are designed to make the attack infeasible for any rational attacker.

However, on smaller blockchains, the calculus shifts. A network with a few million dollars of total hashrate or staked capital can be attacked for a few hundred thousand dollars—a cost that might be recouped by attacking a major exchange or protocol built on that chain. Such attacks have occurred. In 2019, a 51% attack on the Ethereum Classic network created a double-spend valued at about one million dollars. The attacker likely rented hashrate rather than buying hardware, minimising upfront costs.

## Responses and mitigations

Large networks rarely experience sustained 51% attacks because the cost-benefit equation favors defence. However, several architectural responses exist.

Proof-of-stake networks can increase validator slashing penalties, raising the economic cost of attack. Proof-of-work networks can adjust difficulty to absorb new hashrate, slowing any attacker's rate of chain growth. Some protocols incorporate "weak subjectivity checkpoints"—hardcoded recent block hashes that nodes use to anchor their understanding of the canonical chain, preventing attackers from rewriting far-back history.

Community coordination also plays a role. If the broader ecosystem detects a 51% attack, nodes can fork to exclude the attacker's blocks or their coins entirely. This happened on Bitcoin Gold in 2020, when a 51% attacker was ejected after the community consensus shifted against them. The attacker still controlled the majority of hashrate, but their blocks were ignored—a reminder that consensus is ultimately a social phenomenon, not a purely technical one.

## Why 51% does not mean certain victory

Paradoxically, controlling 51% of the consensus power does not guarantee a successful 51% attack. If the attacker's presence is obvious, the network can fork to exclude them. If the attack damages economic value substantially, users and merchants abandon the network in favour of alternatives, making the attacker's coins worthless. And on proof-of-stake networks, an attacker who has accumulated 51% of the stake has massive economic exposure; destroying the network destroys the value of their own holdings.

These forces mean that large, established networks are effectively immune to 51% attacks, not because the attack is technically impossible, but because the incentives are wrong. Attacking is more expensive than the attacker can realistically gain, and the political response to an obvious attack would be swift.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Work](/proof-of-work/) — the consensus mechanism most vulnerable to 51% attacks
- [Proof of Stake](/proof-of-stake/) — alternative consensus with economic finality built in
- [Fork Choice Rule](/fork-choice-rule/) — the rule that determines which chain is canonical; attackers exploit this
- Double Spending — the primary attack enabled by 51% control
- Consensus Mechanism — the rules attackers aim to subvert
- [Selfish Mining](/selfish-mining/) — a weaker attack requiring less than 50% of power

### Wider context

- [Hash Rate](/hash-rate/) — the denominator in consensus power measurement
- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundational security model
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — common targets of 51% attacks
- Ethereum Classic — network that experienced a documented 51% attack

</div>

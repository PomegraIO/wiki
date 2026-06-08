---
title: "Long-Range Attack"
description: "A proof-of-stake-specific attack where an adversary compromises old validator keys to rewrite deep historical blocks after the validators have unbonded and withdrawn."
keywords:
  - proof-of-stake security
  - long-range attack
  - validator key compromise
  - blockchain history
  - consensus rewriting
  - finality threat
image: /svg/crypto.svg
---

*Proof-of-stake security rests on the premise that attacking the network is expensive: validators risk their staked collateral if they misbehave. But that premise has an expiration date. Once a validator exits, unbonds, and withdraws their stake, their capital is no longer at risk. An attacker who later compromises that validator's old cryptographic keys can rewrite ancient history with impunity. This is the long-range attack.*

## The setup: keys and stakes diverge over time

In **[proof-of-stake](/proof-of-stake/)** systems, each validator signs blocks and attestations with a private key. That key proves ownership of the staked balance. A validator might run an honest node for years, earning **[rewards](/dividend-yield/)**, then decide to exit. They unbond their stake (withdrawing collateral from the network) and retire their key.

Time passes. Months or years later, an attacker acquires that old, inactive key through some means: a stolen hardware wallet, a compromised offline backup, or social engineering. The attacker now controls a key that once wielded significant voting weight in the blockchain.

Here is the problem: the validator's stake is no longer on the line. **[Slashing mechanisms](/slashing-mechanisms/)** that protected consensus when the stake was active are now useless. The validator has already unbonded. There is no balance left to slash, and the attacker faces no penalty for using the old key to sign blocks on a competing fork.

## How the attack unfolds

The attacker uses the compromised key to create an alternative history of the blockchain. They build a competing fork starting from some point in the past—say, block 1,000,000. Using the old key, they sign blocks and create attestations as if that validator were still active, earning the validator's historical rewards on the alternative fork.

If the attacker has compromised multiple old keys, they can accumulate enough historical voting weight to make their competing fork credible. To a new node joining the network with no prior knowledge of which fork is legitimate, both histories may appear equally valid, both signed by what were once active validators.

The attacker does not necessarily want the competing fork to overtake the main chain today. Instead, the goal is to create reachable competing history. A new node downloading the blockchain for the first time has no way to distinguish which fork is "real" without consulting out-of-band sources (a trusted checkpoint list, a centralized directory, or other nodes it trusts). The attacker has effectively split consensus.

## Why this is distinct from nothing-at-stake

The **[nothing-at-stake problem](/nothing-at-stake-problem/)** arises when validators are incentivised to vote on all forks simultaneously because their stake is inert. A validator loses nothing by voting for both fork A and fork B while both are active.

A long-range attack is different. The attacker is not a validator currently securing the network. They are an outside party exploiting the fact that old stakes are no longer protected. The validators themselves may have been entirely honest; the attacker is impersonating them using stolen keys.

Moreover, slashing does not directly defend against long-range attacks. The mechanism designed to punish equivocation cannot punish someone who is no longer a validator. The key is already inactive; there is no slashable balance.

## Historical context: Ethereum's early vulnerability

Ethereum's initial Casper proof-of-stake design (before the full transition in 2022) took several approaches to mitigate long-range attacks. One was to require validators to include a **"source"** (a recent finalized checkpoint) in their attestations. A validator claiming to attest to a block far in the past had to reference a recent finalized block to do so. This made it difficult for an attacker using an old key to create a competing history that diverges from the finalized main chain without also rewriting the finalized checkpoint, which would require the attacker to control a supermajority of current validators—a much harder task.

In Bitcoin and proof-of-work chains, long-range attacks do not apply because the attacker would need to redo all the mining work from the point of divergence forward. The computational cost is prohibitive. In proof-of-stake, no such work is required; signatures alone suffice.

## Modern defences: checkpoints and finality

Contemporary proof-of-stake systems defend against long-range attacks through **finality gadgets** or **weak subjectivity checkpoints**. The idea is simple: the chain designates certain blocks (typically finalized blocks) as historical anchors that cannot be undone without a supermajority of current validators conspiring to slash themselves.

Ethereum's **finality mechanism** works this way. A block that has been attested to by two-thirds of active validators is deemed final. To produce a competing history that rewrites a finalized block, an attacker would need to control those two-thirds of current validators, which is economically implausible. The attacker cannot use old, unbonded keys to achieve a two-thirds supermajority of the present; they would need to compromise keys of validators who are currently active and whose stake is at risk.

This defence relies on a notion called **weak subjectivity**: newly joining nodes must download from a recent, trusted checkpoint (within a few months) to safely bootstrap. A node that has been offline for years and comes back online is expected to sync from a recent checkpoint provided by its software or a trusted peer, not from the genesis block. This prevents the attacker from presenting an alternative deep history as the truth.

## The depth of vulnerability

The window of vulnerability for a long-range attack depends on how old a validator's keys can be. A key from a validator who exited one year ago is vulnerable if it remains compromised. A key from a validator who exited ten years ago is still vulnerable, assuming the attacker can still find infrastructure to compute with it.

However, finality mechanisms significantly reduce the practical threat. An attacker cannot rewrite finalized blocks using old keys alone. They must either (1) rewrite history starting from an unfinalized fork far in the past, which limits the fork's utility (new nodes will prefer the finalized chain), or (2) compromise current validators, at which point they face slashing penalties and are not executing a pure long-range attack.

## Slashing and recovery

In theory, a long-range attack could be paired with **[slashing](/slashing-mechanisms/)** if current validators could be induced to attest to the attacker's fork. For example, if an attacker compromises both old keys and some current validators, they could engineer a scenario where current validators sign blocks on a competing fork and then slash them post-hoc for equivocation. This is sometimes called a "hybrid" attack, combining long-range and contemporary components.

Defences against this include **liveness** provisions: if finalized validators disagree on a checkpoint, the chain may activate an emergency protocol that reduces slashing penalties or requires governance intervention. The trade-off is that finality becomes contingent on governance, not purely cryptographic, a nuance that different chains handle differently.

## Practical implications

For users and exchanges, the long-range attack is largely a theoretical concern mitigated by finality and checkpoints. A long-range fork has been present since the chain's inception in many attacks; new nodes downloading the blockchain are instructed to use a recent finalized checkpoint, not a deep historical one.

For node operators and light clients, the attack matters more. A light client that tries to validate the entire history without relying on checkpoints remains vulnerable to long-range attacks using old, compromised keys. This is why light clients in modern proof-of-stake chains are encouraged to sync from recent trusted block headers, not the genesis block.

The long-range attack reminds us of a fundamental design principle: **finality is as strong as the current set of validators, not the historical ones**. Once a validator exits and their stake is unbonded, they no longer have skin in the game. Consensus mechanisms must account for this and protect against impersonation using old keys.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-Stake](/proof-of-stake/) — the consensus mechanism targeted by long-range attacks
- [Blockchain Finality](/blockchain-finality/) — finality mechanisms that defend against this attack
- [Slashing Mechanisms](/slashing-mechanisms/) — penalties that cannot directly stop long-range attacks
- [Nothing-at-Stake Problem](/nothing-at-stake-problem/) — a related but distinct incentive problem
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where checkpoint safety matters for trading

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — consensus security principles
- [Distributed Ledger](/distributed-ledger/) — broader attack and defence taxonomy
- [Bitcoin](/bitcoin/) — proof-of-work immunity to this attack class

</div>

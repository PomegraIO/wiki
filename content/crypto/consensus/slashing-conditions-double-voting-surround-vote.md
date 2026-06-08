---
title: "Slashing Conditions: Double Voting and Surround Votes Explained"
description: "Slashing conditions penalize validators who commit provably malicious acts like double voting and surround voting, protecting proof-of-stake consensus."
keywords:
  - slashing conditions double voting
  - surround vote validator
  - equivocation proof of stake
  - validator slashing rules
  - proof of stake penalties
  - byzantine validator
  - validator misconduct
image: "/svg/crypto.svg"
---

*In a **proof-of-stake** network, validators lock up capital and earn rewards by honestly proposing and attesting to blocks. To punish validators who break the rules in ways that threaten the chain's integrity, the protocol defines specific **slashing conditions**—objective, cryptographically verifiable evidence of misbehavior that automatically destroys a portion (or all) of a validator's stake.*

<div class="wiki-hatnote">

Not to be confused with [liquidation](/liquidation/) (which happens in lending protocols) or [margin calls](/margin-call-forex/) (which affect leveraged traders). Slashing is PoS-specific enforcement against validator malfeasance.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Slashing Conditions — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for consensus mechanisms." />

<div class="wiki-infobox-caption">Slashing penalizes provably malicious validator behavior to secure proof-of-stake networks.</div>

|   |   |
|---|---|
| **Purpose** | Deter validators from attacking the chain; make attacks economically ruinous |
| **Evidence** | Cryptographic proof (two signed messages) — not hearsay or reputation |
| **Slash severity** | Usually 1–100% of stake, depending on extent of damage and protocol design |
| **Trigger detection** | Automatic; the chain verifies slashing conditions on chain, no off-chain jury |
| **Examples** | Double voting, surround voting, and other equivocation |
| **Recovery** | Slashed stake is generally burned; validator may withdraw unstaked balance after delay |

</aside>

## Why Slashing Exists

In proof-of-work, a miner's cost of attack is the electricity bill to outcompute the honest chain. In [proof-of-stake](/proof-of-stake/), the validator's cost is the capital at risk—their stake. But _economic punishment alone_ is not enough: a validator with a $10 million stake could theoretically try to fork the chain or revert history if they believed the upside (stealing $100 million) outweighed the loss of their stake.

Slashing conditions exist to make certain attacks **provably impossible** or so damaging that no rational validator would attempt them. The key insight is that valid evidence of an attack is a **contradiction**—two signed messages that violate protocol rules and both bear the validator's cryptographic signature. No validator can credibly deny they issued both. This objectivity means the network can punish the attacker without trusting external judges or committees.

## Double Voting (Equivocation)

The most straightforward slashing offense is **double voting**: a validator signs two different blocks for the same **slot** (the time interval during which a single block should be produced) or two different **attestations** for the same target [epoch](/proof-of-stake/).

**Concrete example:**
- Validator Alice is assigned to propose a block for slot 100.
- She creates block A (with transaction set X) and signs it.
- She then creates block B (with transaction set Y) for the same slot 100 and signs it.
- Both blocks are broadcast to the network.
- Anyone observing both signatures can prove Alice violated the rule "propose at most one block per slot."
- The protocol automatically slashes her stake.

Why is this dangerous? If validators could equivocate without penalty, a malicious validator could sign competing chains simultaneously, trying to convince different parts of the network that each is canonical. This breaks **finality**—the guarantee that once a block is finalized, it cannot be reverted.

The severity of double voting is usually high: Ethereum slashes 1/32 of the validator's entire balance (not just the stake for that epoch) immediately, plus forces the validator to exit.

## Surround Votes

A **surround vote** is a more subtle form of equivocation that specifically targets the [finality](/proof-of-stake/) gadget. In Ethereum's Casper Finality, each [epoch](/proof-of-stake/) produces attestations with a "source" (the last finalized epoch) and a "target" (the current epoch). A surround vote occurs when a validator attests to a (source, target) pair that logically contradicts a previous attestation—specifically, when the new source is earlier and the new target is later.

**Concrete example:**
- In epoch 100, Validator Bob attests: source=95, target=100 (this attestation contributes to finalizing epoch 100).
- In epoch 105, Validator Bob attests: source=90, target=105.
- The second attestation _surrounds_ the first: it goes further back in history (source 90 < 95) while jumping further ahead (target 105 > 100).
- This contradiction proves Bob is trying to revert the finalized epoch 100 while also claiming epoch 105 is valid.
- The protocol detects this and slashes Bob.

Surround votes are dangerous because they allow a validator to vote for two _incompatible_ views of history that _both_ claim to be finalized. Even if each individual message looks plausible in isolation, the pair proves intent to attack finality itself.

## Why Cryptographic Proof Matters

All slashing conditions require **objective cryptographic proof**, not subjective judgment. This is crucial:

- The evidence (two conflicting signed messages) exists on chain and can be verified by any node.
- No external committee needs to decide whether a validator was misbehaving—the contradiction is self-evident.
- Slashing happens automatically, without delay or human discretion.
- A validator cannot plead ignorance ("I didn't mean to") or claim network conditions forced their hand; the signature is definitive.

This objectivity is why PoS security does not depend on the honesty or consensus of external judges. The network simply enforces mathematical rules.

## Slash Amounts and Network Safety

Most PoS chains parameterize slashing to increase in severity as more validators are caught in coordinated attacks. This is called **correlation penalty** or **inactivity leak** in some protocols.

On Ethereum:
- A single equivocation slash removes 1/32 of the validator's 32 ETH stake (~1 ETH).
- If multiple validators are slashed in the same epoch (a sign of a coordinated attack), the slash multiplier increases, potentially destroying 100% of slashed validators' stakes.

The logic: if only one validator misbehaves, a small penalty deters them but does not paralyze the network. If 30% of validators try to attack simultaneously, the protocol should obliterate their stake to make the attack maximally expensive.

## Detection and Enforcement

Slashing detection is **automatic and permissionless**:

1. A whistleblower (any node, any validator) observes two conflicting signed messages from the same validator.
2. They bundle both messages into a **slashing transaction** and submit it to the chain.
3. The protocol verifies the signatures and the contradiction.
4. If valid, the validator's stake is immediately reduced and the validator is exited.

Some chains offer **slashing rewards** to the whistleblower (a fraction of the slashed stake), creating economic incentive to monitor and report attacks.

## Common Misconceptions

**Misconception:** "Slashing only happens if a validator is caught on camera."
- _Reality:_ Slashing is triggered by cryptographic proof (conflicting signatures), not reputation or observation. The validator's own signature proves their guilt.

**Misconception:** "A validator can negotiate their way out of slashing."
- _Reality:_ Slashing is deterministic. Once the slashing condition is met, the penalty is applied automatically by the protocol.

**Misconception:** "Slashing is the same as losing rewards."
- _Reality:_ Slashing destroys principal (the locked capital). Loss of rewards is a separate penalty that applies to offline or underperforming validators.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-Stake](/proof-of-stake/) — the consensus mechanism that enables slashing as punishment
- [Solo Staking vs Pooled Staking: Security and Reward Trade-Offs](/solo-staking-vs-pooled-staking-tradeoffs/) — how validator setup affects slashing risk
- [Weak Subjectivity and Checkpoint Sync in Proof-of-Stake](/weak-subjectivity-checkpoint-sync/) — the finality guarantee that surround voting attacks
- [Why Proof-of-Work Consumes So Much Energy: The Mechanics](/proof-of-work-energy-consumption-explained/) — how PoW differs from PoS in security model

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — distributed consensus and chain security
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where validators stake their capital and earn rewards
- [Distributed Ledger](/distributed-ledger/) — the underlying technology enabling validator networks

</div>

---
title: "Blockchain Finality"
description: "The guarantee that a confirmed transaction cannot be reversed, distinguished by consensus mechanism—probabilistic in proof-of-work, absolute in proof-of-stake."
keywords:
  - blockchain consensus
  - finality guarantees
  - proof-of-work
  - proof-of-stake
  - transaction confirmation
  - chain reorganization
image: /svg/crypto.svg
---

*In a traditional database, a transaction is final when the company controlling the ledger says it is. On a decentralised blockchain, finality means something harder to achieve: a guarantee that once a transaction is recorded, no participant can rewrite it no matter how much computational power or coordination they can summon. The form that guarantee takes—and how long it takes to arrive—differs radically between blockchain designs.*

## Finality is not confirmation

Before a block reaches the mainchain, a transaction lives in a mempool: a staging area where nodes hold unconfirmed transactions waiting to be bundled. Once a block is mined or proposed and accepted by the network, the transaction has been confirmed. But confirmation is not finality. A confirmed transaction can still be reversed if a majority of the network agrees to rewrite history. Finality is the threshold at which reversal becomes economically or technically impossible.

In **[Bitcoin](/bitcoin/)** and other **[proof-of-work](/proof-of-work/)** blockchains, confirmation is probabilistic and time-bound. A transaction buried six blocks deep (the loose industry standard for "final") has, from a practical standpoint, almost zero chance of being undone. But the word "almost" matters. A deep-pocketed adversary with sufficient hashpower could theoretically reorganise the chain and erase that transaction, though the cost would be staggering. Finality here is a probability that approaches certainty as blocks accumulate, never quite reaching it. Miners confirm transactions; they do not certify them as irreversible.

In contrast, **[proof-of-stake](/proof-of-stake/)** systems built on Byzantine Fault Tolerant consensus—like Ethereum 2.0, Polkadot, or Cosmos—offer **absolute finality**. Once a supermajority of validators (typically two-thirds) have attested to a block, that block is final. No amount of subsequent computational work can undo it. A transaction final under this model cannot be reversed unless the validators themselves coordinate to do so, which would require them to destroy their own collateral via **[slashing mechanisms](/slashing-mechanisms/)**—a severe economic penalty that makes such coordination irrational.

## Why proof-of-work finality is probabilistic

The proof-of-work security model relies on one immutable fact: rewriting history costs energy. A miner who wants to alter a block buried ten blocks deep must outrun the rest of the network, redoing all the hashing work for those ten blocks while everyone else continues adding new blocks ahead. As the chain grows, this cost becomes astronomical. Finality emerges not from explicit agreement but from the disproportion between the energy spent to create the history and the energy needed to undo it.

This design has an important consequence: there is no moment at which a transaction tips from "could be reversed" to "cannot be reversed." Instead, the probability of reversal decays with each successive block. After six blocks, reversal is so expensive that Bitcoin stakeholders treat the transaction as final. After one hundred blocks, it is astronomically improbable. But the technical possibility remains, which is why some institutional exchanges demand thirty to one hundred confirmations for large deposits of Bitcoin.

The security guarantee also depends on the assumption that no single entity controls more than 50% of the network's hashpower. If that assumption fails, finality fails. A 51% attacker can rewrite the chain at will. This is why proof-of-work chains are sometimes described as having "economic finality rather than cryptographic finality"—the reversal is cryptographically possible but economically irrational for the majority.

## Absolute finality in Byzantine consensus

A proof-of-stake chain using a BFT consensus protocol introduces a formal definition of finality. Once more than two-thirds of the active validator set (the "supermajority") has signed attestations to a block, that block is final. The protocol rules forbid any validator from signing a conflicting fork without losing their staked collateral.

This difference is more than semantic. In Ethereum's Gasper protocol, for instance, an attester who votes for two conflicting blocks in the same epoch incurs automatic slashing. The penalty is severe—a validator can lose between 1% and 100% of their stake depending on how many others were slashed simultaneously, a mechanism designed to make coordinated attacks economically catastrophic.

Absolute finality means the longest-chain rule, which governs Bitcoin and traditional proof-of-work systems, no longer applies. A shorter chain is final if it has supermajority agreement, even if a longer chain exists. This resolves a subtlety in proof-of-work: if the network temporarily splits into two branches of equal computational weight, the eventual reunion requires one side to be abandoned. With Byzantine consensus, this choice is made once consensus is locked in, not retroactively.

## Confirmation time and finality lag

A practical trade-off emerges between speed and certainty. Bitcoin finalises transactions very slowly (roughly one block every ten minutes, with true finality typically assumed at sixty minutes for six blocks). Ethereum's Gasper finalises epochs roughly every thirteen minutes, but the time from transaction arrival to final confirmation depends on the validator schedule and network conditions. Newer systems like Solana aim for sub-second finality through different consensus designs, though at the cost of centralising validator participation.

Some chains blur the line. Ethereum Classic, which uses proof-of-work, has adopted checkpoint-based finality, grafting Byzantine consensus onto its mining protocol to achieve faster irreversibility. Cardano's Ouroboros protocol achieves formal finality through stake-weighted voting without traditional BFT overhead.

## Finality and fork safety

The ultimate question finality answers is: how deep does a fork have to be to survive? In proof-of-work, fork survival is a race. In Byzantine consensus, it is a supermajority covenant. This matters operationally: an exchange running on proof-of-work watches for deeper confirmations and waits for reorganisation risk to decay; an exchange on proof-of-stake watches for supermajority attestations and knows with economic certainty when reversal would cost validators more than they could possibly gain.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-Stake](/proof-of-stake/) — consensus mechanism securing modern PoS chains
- [Slashing Mechanisms](/slashing-mechanisms/) — penalties enforcing validator honesty in PoS
- [Nothing-at-Stake Problem](/nothing-at-stake-problem/) — the finality threat unguarded PoS systems face
- [Long-Range Attack](/long-range-attack/) — a finality-breaking attack on PoS networks
- [Proof-of-Work](/proof-of-work/) — the consensus foundation of Bitcoin and early chains
- [Byzantine Fault Tolerance](/proof-of-stake/) — the consensus theory underlying modern finality

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundational concepts in distributed ledgers
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where finality guarantees matter operationally
- [Distributed Ledger](/distributed-ledger/) — broader taxonomy of consensus systems

</div>

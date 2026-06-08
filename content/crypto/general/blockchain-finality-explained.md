---
title: "Blockchain Finality Explained"
description: "Understanding probabilistic vs deterministic finality and why different blockchains require varying numbers of block confirmations."
keywords:
  - blockchain finality explained
  - what is blockchain finality
  - finality confirmation blocks
  - probabilistic finality ethereum
  - deterministic finality proof of stake
---

*A transaction is final once it cannot be reversed, but different blockchains guarantee finality in different ways. **Blockchain finality** comes in two flavors: probabilistic (where each new block makes reversal exponentially harder) and deterministic (where a hard rule guarantees irreversibility after N blocks). The number of confirmations required depends on the network's security model and what an exchange or merchant deems safe.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Blockchain Finality — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Finality protocols determine when a transaction truly cannot be reversed.</div>

|   |   |
|---|---|
| **Probabilistic finality** | Risk of reversal decreases exponentially with each block |
| **Deterministic finality** | After N blocks, reversal is cryptographically impossible |
| **Bitcoin confirmations** | Typically 6; probabilistic (exponential security) |
| **Ethereum PoW finality** | Typically 12–15 blocks; probabilistic |
| **Ethereum PoS finality** | 2 epochs (≈13 min); deterministic via consensus |
| **Layer-2 finality** | Varies widely; may depend on mainnet confirmation |

</aside>

## The Problem: When Is a Transaction Really Done?

A blockchain transaction is not instantaneous. When you broadcast a transaction, it enters a network of nodes, gets included in a block, and that block is added to the chain. But the transaction remains reversible for some time afterward—typically because a longer chain could be built that excludes it, or because validators could organize a consensus reorg.

Finality answers the question: at what point is reversal economically or cryptographically impossible? The answer matters for high-value transfers, merchant payments, and withdrawals from exchanges. A buyer of a house using blockchain is not comfortable until reversal is genuinely off the table. An exchange crediting your withdrawal account needs certainty too.

## Probabilistic Finality: Bitcoin and Proof-of-Work Chains

In [proof-of-work](/proof-of-work/) systems like Bitcoin, finality is **probabilistic**. Each new block added to the chain makes it harder to reorg the transaction out—but it's never mathematically impossible, only exponentially unlikely.

Bitcoin's consensus rule is simple: the longest valid chain is the canonical chain. If a miner (or group of miners) controls more than 50% of the network's hash power, they could theoretically build a longer chain that excludes your transaction, then broadcast it and make it the accepted history. The probability of a 51% attack drops exponentially as blocks pile up on top of your transaction.

The industry standard is **6 confirmations** for Bitcoin transactions. This means 6 blocks have been mined on top of your block. Reverting your transaction would require an attacker to simultaneously recompute all 7 blocks (the original block plus 6 on top) faster than the honest network adds new blocks. With Bitcoin's ~10-minute block time and the vast hash power distributed globally, the probability of a 51% attack lasting 6 blocks is negligible—roughly 1 in a billion under normal conditions.

Ethereum during its proof-of-work era (before September 2022) used the same model. 12 to 15 confirmations were typical thresholds for high-value transactions, offering similar security margins.

## Deterministic Finality: Proof-of-Stake and Consensus Rules

In [proof-of-stake](/proof-of-stake/) systems, finality can be **deterministic**—meaning there is a point after which reversal is cryptographically impossible, enforced by consensus rules rather than energy and computation.

Ethereum, after switching to proof-of-stake in 2022, employs deterministic finality through two mechanisms:

**Justification**: A block is "justified" when two-thirds of validators have attested to it. Attesting validators are cryptographically committed to that block. Violating that commitment (voting for a conflicting block) incurs a penalty called slashing. Once justified, a block cannot be reverted without destroying the attesting validators' stakes.

**Finalization**: A block becomes final when a new block is justified *on top of it*, with two-thirds of validators again in agreement. This creates a chain of justified blocks, and older blocks in that chain are finalized. As of Ethereum 2.0 specs, finality is guaranteed after two epochs, or roughly 13 minutes.

This is fundamentally different from Bitcoin. No amount of hash power can reorg a finalized block because validators have already put their own capital (their stake) at risk. A reorg would require slashing the attesting validators, which is ruled out by consensus.

## Why Block Count Varies Across Networks

Different blockchains require different numbers of confirmations because their security models differ:

- **Bitcoin, Litecoin (PoW)**: 6 blocks standard. Security decays exponentially; 6 blocks = ~99.9% probability of irreversibility.
- **Ethereum PoS**: 2 epochs (≈13 min). Deterministic; finality is absolute after this point.
- **Solana (Proof-of-History)**: Finality typically immediate or within 1–2 slots; the network reaches supermajority consensus faster due to its block structure.
- **Cardano (Proof-of-Stake)**: 5 blocks typical; deterministic finality applies after finality rules are met.

Layer-2 systems (Lightning, Arbitrum, Optimism, Polygon) introduce complexity. Finality on the Layer-2 itself may be fast, but true finality often depends on settlement on the mainnet. An Arbitrum transaction might show as final on Arbitrum in milliseconds, but full security depends on a [proof-of-stake](/proof-of-stake/) commitment or Ethereum mainnet confirmation.

## The 51% Attack Revisited

In proof-of-work, a 51% attack is the ultimate reversal threat. In proof-of-stake, the equivalent is a **two-thirds consensus attack**, where two-thirds or more of validators collude to reorg the chain. The cost is prohibitive: validators lose their stake (slashing). This transforms the risk from energy/hardware (proof-of-work) to capital at stake (proof-of-stake).

For Bitcoin, a 51% attack requires continuous majority hash power. For Ethereum, a 2/3+ attack requires validators to collectively fork away from their gains and face penalties. Each model has different barriers and incentive structures, but both are designed to be astronomically costly.

## Exchange and Merchant Thresholds

In practice, exchanges and merchants set their own finality thresholds:

- Most Bitcoin exchanges require 3 to 6 confirmations before crediting deposits, even though the network technically provides some security after 1 block.
- Ethereum exchanges might accept finalized blocks (post-Merge PoS), or require 12+ blocks for extra conservatism.
- Stablecoin [bridges](/cryptocurrency-exchange/) (connecting Ethereum to Arbitrum, for example) often wait for mainnet finality, making the process slower than individual on-chain transfers.

A $10 coffee purchase might require only 1 confirmation; a $10 million transfer might require 20 or more, pending the merchant's or exchange's risk appetite.

## Reorg Events and Network Disruptions

Deterministic finality does not mean zero reorgs. Unfinalized blocks can be reverted. Ethereum PoS has experienced reorgs of up to 2 blocks before finality was reached, typically due to transient network splits or consensus rule updates.

In 2022, the Beacon Chain on Ethereum briefly experienced a four-epoch-deep reorg due to a network composition change. This did not affect finalized transactions, but it showed that even modern PoS systems can reorg earlier blocks if validators fork or network conditions change rapidly.

Bitcoin reorgs are rarer and shallower because proof-of-work requires constant computational power to build a competing chain. Reorgs of 2 to 3 blocks are historically documented; anything deeper is vanishingly rare.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-Work](/proof-of-work/) — how hash power secures Bitcoin and other PoW chains
- [Proof-of-Stake](/proof-of-stake/) — how validator deposits secure Ethereum and similar networks
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — platforms where finality directly affects settlement
- [Distributed Ledger](/distributed-ledger/) — the core technology behind blockchain networks

### Wider context

- [Mempool Explained](/mempool-explained/) — the waiting room before blockchain inclusion
- [Bitcoin](/bitcoin/) — the original proof-of-work blockchain
- [Ethereum](/ethereum/) — history and evolution from PoW to PoS

</div>
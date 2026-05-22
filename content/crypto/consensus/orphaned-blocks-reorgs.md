---
title: "Orphaned Blocks and Reorgs"
description: "Chain reorganization when a longer block sequence supersedes shorter one; transaction finality implications."
keywords:
  - orphaned blocks
  - blockchain reorg
  - chain reorganization
  - longest chain rule
  - transaction finality
  - double spend risk
  - consensus mechanism
---

*An **orphaned block** is a valid block that is created but not incorporated into the main [blockchain](/blockchain-fundamentals/) because a competing block is chosen instead. A **reorg** (reorganization) occurs when the network's consensus shifts to an alternative chain, reversing transactions that were considered "final" moments before. This is a fundamental feature of [proof-of-work](/proof-of-work/) and [proof-of-stake](/proof-of-stake/) systems and has profound implications for transaction security.*

<aside class="wiki-infobox">

| Attribute | Value |
|-----------|-------|
| **Cause** | Network split, slower block propagation |
| **Bitcoin** | ~6 block depth for "finality" (95% safe) |
| **Ethereum PoW** | ~30 blocks confirmed standard |
| **Ethereum PoS** | ~32 epochs (~13 min) for finality |
| **Risk window** | Hours for small reorg, seconds for deep reorg |
| **Double-spend vector** | Spend on old chain, new chain ignores it |
| **Frequency** | Bitcoin: ~1–2 per month (1-2 blocks) |
| **Market impact** | Rare, but catastrophic if large |

</aside>

## How orphaned blocks arise

In [proof-of-work](/proof-of-work/), thousands of miners compete to solve the next block's cryptographic puzzle. When two miners solve the puzzle at nearly the same time, they both broadcast valid blocks to the network. Nodes receive these blocks in different order depending on network latency and geography.

One block will propagate faster and be extended by miners who receive it first. The second block, even though valid, is orphaned—it sits on a shorter chain and is rejected by the consensus rule (longest chain rule, or in [proof-of-stake](/proof-of-stake/), the "correct" fork as determined by validator attestations).

The miner who mined the orphaned block receives no reward—a financial loss that drives competition for faster networking and strategic pool placement.

## Reorgs: longer chains override shorter

A **reorg** is an extreme version: an entire segment of the chain (say, blocks 100–105) is discarded in favor of an alternative sequence (blocks 100–110 from a competing fork). This can happen if:

1. A fork in the network isolates two groups of miners for several blocks.
2. Both groups extend their respective chains in parallel.
3. When the network reunites, one chain is longer and becomes canonical.
4. All transactions in the discarded blocks are undone; those blocks are orphaned.

For example, suppose blocks 100–102 are on Chain A (produced by miners in Asia) and blocks 100–105 are on Chain B (produced by miners in Europe). When the network partition heals, if Chain B reaches block 106 first and is longer, nodes revert to Chain B. Blocks 103–105 from Chain B are now canonical, and blocks 103–102 from Chain A are orphaned. Transactions in the orphaned blocks may return to the mempool (for possible inclusion in future blocks) or be lost entirely if they double-spend transactions in the new canonical chain.

## Transaction finality and depth

For a transaction to be considered **final** (irreversible), it must be buried deep enough in the chain that a reorg cannot undo it. This depends on the consensus mechanism.

In Bitcoin's proof-of-work:
- A transaction in the latest block (0 confirmations) is not final; a reorg could undo it.
- After 1 block (1 confirmation), the transaction is final with very high probability but still vulnerable to an extreme reorg.
- After 6 blocks (~60 minutes), the transaction is considered final by most exchanges and services. A reorg of 6+ blocks would require 51%+ attack (majority of hash power).
- After 30+ blocks, finality is very strong.

In Ethereum proof-of-stake (post-Merge):
- Validators attest to blocks; once a supermajority (2/3) attests, the block is **justified**.
- When the next epoch is similarly justified, the prior is **finalized**—reorg would require slashing major amounts of validator collateral.
- Finality takes ~32 epochs (~13 minutes), much slower than Bitcoin's practical finality time.

## Causes and frequency

**Network latency**: If a miner or mining pool is geographically distant or has poor connectivity, its blocks propagate slowly. By the time other miners receive it, they have already started working on a competing block. This is rare but happens in every blockchain occasionally.

**Network partitions**: If the network splits (e.g., a backbone ISP outage divides the internet into two regions), two separate chains grow. When the partition heals, the longer chain wins, and the shorter side is orphaned. This is very rare in mature networks but can happen.

**Selfish mining**: A theoretical attack where a miner withholds blocks, creates a private fork longer than the public chain, and releases it suddenly, causing a reorg. This requires significant hash power and is economically irrational in most cases, but has been documented in smaller blockchains.

**51% attack**: An attacker controlling majority hash power can deliberately create an alternative chain and revert transactions. This is the worst-case but requires enormous capital.

## Implications for exchanges and applications

Exchanges typically require:
- Bitcoin: 2–6 confirmations (to wait out potential reorgs)
- Ethereum: 12+ blocks post-merge (not relying on finality but empirical safety)

A deposit of 1 BTC is not fully credited until 6 blocks later. If a reorg happens, the deposit might never arrive (if it was in the orphaned chain) and the user is not refunded—a financial loss. This is why depth matters.

DeFi applications [like automated market makers](/automated-market-maker/) are vulnerable if they do not wait for finality. A transaction that swaps tokens, if it is later orphaned, could leave balances inconsistent.

## Economic incentives and security

The security of a blockchain against reorgs is the cost to attack. To reorg Bitcoin 6 blocks deep, an attacker needs to control enough hash power to produce 7 blocks faster than the rest of the network. At current hash rates, this would cost tens of millions of dollars in hardware and electricity, making it economically irrational for any profit less than that.

As a network matures and hash power concentrates, reorg risk decreases because attacks become more expensive and less profitable. However, extreme price movements (e.g., Bitcoin crashing 50%) can make old attacks profitable for a brief window.

## Detection and notification

Some blockchain monitoring services watch for reorgs and notify traders. A reorg of more than 2–3 blocks is unusual and warrants investigation—it might signal a network attack or unusual latency event. Validators and stakers are incentivized to adopt fast, secure practices to avoid reorg losses.

---

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Core distributed ledger concept
- [Proof of Work](/proof-of-work/) — Consensus mechanism prone to orphaned blocks
- [Proof of Stake](/proof-of-stake/) — Consensus with stronger finality
- Double Spend — Ability to spend same coin twice
- [Consensus Layer Security](/consensus-layer-security/) — Finality and 51% attacks

### Wider context

- [Bitcoin](/bitcoin/) — Most analyzed reorg history
- [Ethereum](/ethereum/) — Shift from PoW to PoS for finality
- [Validator Economics](/validator-economics/) — Stake-based security
- [Settlement Finality](/crypto-settlement-finality/) — Transaction irreversibility
- [Sybil Attack](/sybil-attack/) — Attack type on distributed consensus

</div>

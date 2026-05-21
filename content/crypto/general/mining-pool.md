---
title: "Mining Pool"
description: "A mining pool is a collective of miners who combine their computational power to increase their chances of finding blocks and earning rewards. Pool members receive regular payouts proportional to their contributed work."
keywords:
  - mining pool
  - pool mining
  - shares
  - variance reduction
  - mining collective
  - payout scheme
image: "/svg/crypto.svg"
---

*A **mining pool** is a collective of [cryptocurrency miners](/mining-bitcoin/) who combine their computational power to mine blocks more reliably. Rather than each miner independently solving puzzles and waiting months or years to find a block, pool members contribute shares of work and receive regular payouts proportional to their contribution.*

<div class="wiki-hatnote">

This entry covers mining pools as an organisational structure. For individual mining, see [mining Bitcoin](/mining-bitcoin/); for mining hardware, see [ASIC mining](/asic-mining/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mining Pool — key facts</div>

<img src="/svg/crypto.svg" alt="Mining pool network and reward distribution" />

<div class="wiki-infobox-caption">A mining pool: shared hash power, distributed rewards.</div>

|   |   |
|---|---|
| **What it is** | Collective mining operation |
| **Participants** | Individual miners pooling power |
| **Operator** | Pool administrator (manages distribution) |
| **Payout** | Proportional to contributed hash power |
| **Fee** | 0.5–2% of rewards (pool operator cut) |
| **Variance reduction** | Regular payouts instead of rare big payouts |
| **Decentralisation risk** | Concentration of mining power |
| **Major pools** | Foundry USA, AntPool, Stratum, others |

</aside>

## The problem pools solve

A solo miner with a single [ASIC](/asic-mining/) might generate 1 terahash per second (TH/s). The Bitcoin network has ~1 exahash per second (EH/s) of total hash power — roughly 1,000,000 solo miners.

A solo miner would, on average, wait ~1,000,000 blocks (roughly 19 years) to find a block alone. This is impractical.

Mining pools solve this problem by aggregating miners. If 10,000 miners with 1 TH/s each join a pool, they collectively contribute 10,000 TH/s. They will find a block roughly every 100 times faster than an individual miner, dramatically reducing variance.

## How mining pools work

1. **Miners connect to the pool.** A miner configures their [ASIC](/asic-mining/) to connect to the pool's server, providing their address.
2. **Pool distributes work.** The pool sends each miner a **mining job** (a candidate block with a different target difficulty).
3. **Miners submit shares.** When a miner finds a partial solution (called a "share"), they submit it to the pool, proving they did work. Not every share is a valid [Bitcoin](/bitcoin/) block (the difficulty is lower), but every valid block is composed of many shares.
4. **Pool finds a block.** When one of the pool's miners finds a valid block, the pool announces it to the network.
5. **Rewards distributed.** The pool collects the block reward and transaction fees, deducts its fee (usually 0.5–2%), and distributes the remainder to members proportional to their contributed work.

## Payout schemes

Pools use different systems for distributing rewards:

**Pay-per-share (PPS):** The pool guarantees a fixed payout per share submitted, regardless of whether the pool finds blocks. The pool operator bears the variance risk. This is the safest for miners but requires a well-capitalised pool operator.

**Proportional:** Rewards are distributed proportional to shares submitted. If a pool finds a block and you submitted 5% of the shares, you receive 5% of the reward. This shares variance between the pool and miners.

**Pay-per-last-N-shares (PPLNS):** Rewards are based on the last N shares submitted across the pool. This discourages miners from jumping between pools mid-round.

**Bitcoin-as-a-service:** Some modern pools use other schemes to reduce variance further.

## Centralisation concerns

Mining pools create centralisation pressure. If a single pool controls >50% of the network [hash rate](/hash-rate/), it could (theoretically) perform a 51% attack and rewrite Bitcoin history.

Historically:

- **2014:** GHash.io briefly reached 51% hash rate, raising alarms.
- **2017:** Mining pools were quite concentrated, with a few pools controlling much of the power.
- **2024:** Hash power is more distributed among pools, though concentration remains an issue.

To address this, the Bitcoin community encourages miners to join smaller pools or run solo mining. Some mining pools implement **block template generation** on the miner side, reducing the pool's ability to censor transactions or perform attacks.

## Pool operators

Major Bitcoin mining pools include:

- **Foundry USA:** Operated by Digital Currency Group, supports independent miners and does not censor transactions.
- **AntPool:** Operated by Bitmain, one of the largest.
- **Stratum V2:** An emerging standard that aims to reduce pool operator power.
- Others: SBI Crypto, Mara Pool, and smaller pools.

Pool operators earn fees (typically 0.5–2% of block rewards) and derive influence from controlling the pool members' hash power.

## Mining pool hopping

Some miners "hop" between pools, joining pools that are close to finding a block and leaving before the block is found. This allows miners to gain disproportionate rewards per share.

Most pools combat hopping with PPLNS or other schemes that reward consistent participation.

## Transparency and trust

Pools are services operated by companies or individuals. Miners must trust the pool operator to:

- Honestly distribute rewards.
- Not censor transactions.
- Not perform attacks.

Regulatory oversight of mining pools is limited. If a pool operator disappears with funds or conducts fraud, miners have limited recourse.

## See also

<div class="wiki-seealso">

### Closely related

- [Mining Bitcoin](/mining-bitcoin/) — the activity mining pools facilitate
- [ASIC mining](/asic-mining/) — hardware used in pools
- [Hash rate](/hash-rate/) — measure of pool power
- [Block reward](/mining-bitcoin/) — what pools distribute
- [Variance reduction](/mining-bitcoin/) — why pools exist

### Wider context

- [Bitcoin](/bitcoin/) — the network being mined
- [Proof-of-work](/proof-of-work/) — the mechanism
- 51% attack — the centralisation risk
- [Difficulty adjustment](/difficulty-adjustment/) — responds to pool power

</div>

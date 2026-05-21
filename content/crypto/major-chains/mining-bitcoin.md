---
title: "Mining Bitcoin"
description: "Bitcoin mining is the process of validating transactions and creating new blocks using proof-of-work. Miners compete to solve difficult cryptographic puzzles, earning newly minted Bitcoin and transaction fees as rewards."
keywords:
  - bitcoin mining
  - miner
  - proof-of-work
  - hash
  - block reward
  - mining pool
image: "/svg/crypto.svg"
---

*A **Bitcoin miner** is a participant in the [Bitcoin](/bitcoin/) network that validates transactions and creates new blocks using [proof-of-work](/proof-of-work/) consensus. Miners compete to solve difficult cryptographic puzzles; the first to solve a puzzle gets to propose the next block and receives a reward of newly minted Bitcoin plus transaction fees.*

<div class="wiki-hatnote">

This entry covers the mechanics of Bitcoin mining. For the broader technology, see [proof-of-work](/proof-of-work/); for mining pools, see [mining pool](/mining-pool/); for the hardware, see [ASIC mining](/asic-mining/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bitcoin Mining — key facts</div>

<img src="/svg/crypto.svg" alt="Bitcoin mining operation with ASICs" />

<div class="wiki-infobox-caption">Bitcoin mining: solving puzzles to earn Bitcoin.</div>

|   |   |
|---|---|
| **What it is** | Validating transactions and creating blocks |
| **Consensus** | [Proof-of-work](/proof-of-work/) |
| **Participants** | Miners with specialised hardware |
| **Block time** | ~10 minutes (on average) |
| **Block reward** | ~6.25 BTC (as of 2024) + transaction fees |
| **Halving** | Every 210,000 blocks (~4 years) |
| **[Hash rate](/hash-rate/)** | ~1 exahash/second (global) |
| **Energy cost** | ~10 GW globally |

</aside>

## The mining process

When a user broadcasts a Bitcoin transaction, it spreads across the network to miners' memory pools (lists of unconfirmed transactions). Miners select transactions from their mempool and bundle them into a candidate block.

To add the block to the [blockchain](/blockchain-fundamentals/), a miner must find a **nonce** (a random number) such that the hash of the block (with that nonce) is smaller than a target value. This is the [proof-of-work](/proof-of-work/) puzzle.

Because hash functions are unpredictable, there is no shortcut — miners must try billions of nonces until finding one that works. The miner that finds a valid nonce first broadcasts the block to the network, other nodes verify it, and the miner receives the block reward.

## Block rewards and fees

A miner who successfully creates a block receives:

1. **Block reward:** Newly minted Bitcoin. Originally 50 BTC, halved every four years. Currently ~6.25 BTC (as of 2024).
2. **Transaction fees:** The sum of fees paid by users whose transactions are included in the block. Miners prioritise high-fee transactions to maximise revenue.

The block reward will eventually decrease to zero (around 2140). At that point, transaction fees must be sufficient to incentivise mining, or the network becomes insecure.

## Mining difficulty

The [difficulty](/difficulty-adjustment/) of the puzzle is adjusted automatically every 2,016 blocks (~two weeks) to maintain an average block time of 10 minutes. If more miners join the network (increasing the total [hash rate](/hash-rate/)), the difficulty increases, making puzzles harder.

This self-regulation is crucial: it ensures that even as hardware improves, blocks continue arriving every ~10 minutes.

## Mining hardware evolution

Mining has evolved through several hardware generations:

1. **CPU mining (2009–2010).** Ordinary computers could mine Bitcoin using their processors.
2. **GPU mining (2010–2011).** Graphics processing units (GPUs) were 10–100x faster.
3. **FPGA mining (2011–2012).** Field-programmable gate arrays offered custom logic.
4. **[ASIC mining](/asic-mining/) (2012–present).** Application-specific integrated circuits designed solely for Bitcoin mining, thousands of times faster than GPUs.

Modern Bitcoin mining is dominated by [ASIC](/asic-mining/) miners, which cost hundreds of thousands of dollars but are the only economically viable option.

## Mining pools and solo mining

A solo miner waiting to find a block might wait years before a block is found. To reduce variance, miners join **[mining pools](/mining-pool/)** — consortiums that bundle hash power and share rewards based on contribution.

A [mining pool](/mining-pool/) operator collects transactions, distributes the hashing work to pool members, and distributes rewards when someone in the pool finds a block. The pool typically takes a small percentage (0.5–2%) as an operating fee.

This allows smaller miners to earn steady income rather than waiting for occasional large payouts.

## Profitability

Mining profitability depends on:

1. **Hardware cost:** [ASIC](/asic-mining/) miners cost $1,000–$10,000+.
2. **Electricity cost:** Miners consume 5–10 watts per gigahash of compute. At global electricity costs (~$0.05–$0.15 per kilowatt-hour), electricity is the primary operating cost.
3. **Bitcoin price:** Higher prices improve profitability; lower prices can make mining unprofitable.
4. **[Hash rate](/hash-rate/):** Higher network hash rate increases competition, reducing individual miner revenue.

Marginal miners (those with high electricity costs or older hardware) exit when Bitcoin price falls below their breakeven cost.

## Geographical distribution

Bitcoin mining occurs globally, but is concentrated in regions with cheap electricity:

- China (prior to 2021 ban)
- Iceland (hydroelectric power)
- El Salvador (geothermal)
- Parts of the US with stranded hydroelectric capacity

This geographical distribution is itself a security feature — no single country can easily shut down Bitcoin mining.

## Environmental impact and debates

Bitcoin mining consumes ~10 gigawatts of power globally (comparable to Argentina or Pakistan). Environmental critics argue this is wasteful. Proponents counter that:

1. The energy expenditure buys genuine decentralised security.
2. Mining often uses renewable energy (hydroelectric, geothermal).
3. Environmental costs should be weighed against benefits.

## Selfish mining and attack vectors

Theoretically, a miner with >50% of the [hash rate](/hash-rate/) could perform a "selfish mining" attack, forking the chain to their advantage. However, controlling 51% of Bitcoin's hash rate would cost billions of dollars in hardware and electricity, making this impractical.

Other minor attacks exist (e.g., "eclipse" attacks targeting network connectivity), but Bitcoin has proven robust to them since 2009.

## See also

<div class="wiki-seealso">

### Closely related

- [Bitcoin](/bitcoin/) — the network being mined
- [Proof-of-work](/proof-of-work/) — the mechanism
- [ASIC mining](/asic-mining/) — specialised hardware
- [Mining pool](/mining-pool/) — collaborative mining
- [Hash rate](/hash-rate/) — measure of mining power
- [Difficulty adjustment](/difficulty-adjustment/) — regulates mining pace

### Wider context

- [Bitcoin halving](/bitcoin-halving/) — reduces block rewards over time
- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Validator](/validator/) — the proof-of-stake equivalent

</div>

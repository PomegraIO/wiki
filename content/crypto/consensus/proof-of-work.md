---
title: "Proof-of-Work"
description: "Proof-of-work is a consensus mechanism where nodes (miners) compete to solve difficult mathematical puzzles. The first to solve a puzzle gets to propose the next block and receives a reward, securing the network through energy expenditure."
keywords:
  - proof-of-work
  - mining
  - consensus
  - bitcoin
  - hash puzzle
  - difficulty
image: "/svg/crypto.svg"
---

*A **proof-of-work** is a consensus mechanism used in [blockchains](/blockchain-fundamentals/) where [miners](/mining-bitcoin/) compete to solve difficult cryptographic puzzles to propose the next block. The first miner to solve the puzzle broadcasts the solution (the "proof of work") to the network; if valid, other nodes accept the block. Miners are rewarded with newly minted cryptocurrency and transaction fees.*

<div class="wiki-hatnote">

This entry covers proof-of-work as a consensus mechanism. For its implementation in Bitcoin, see [mining Bitcoin](/mining-bitcoin/); for alternatives, see [proof-of-stake](/proof-of-stake/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proof-of-Work — key characteristics</div>

<img src="/svg/crypto.svg" alt="Miners solving puzzles to produce valid blocks" />

<div class="wiki-infobox-caption">Proof-of-work: security through computational effort.</div>

|   |   |
|---|---|
| **How it works** | Miners solve puzzles; first wins the right to add a block |
| **Security model** | Computational work makes attacks expensive |
| **Who validates** | Miners (or mining pools) |
| **Reward** | Newly minted coin + transaction fees |
| **Energy cost** | Substantial (global Bitcoin network: ~10 GW) |
| **Decentralisation** | High (anyone can mine, though ASICs create barriers) |
| **Time to finality** | ~1 hour (Bitcoin) for high confidence |
| **Used by** | [Bitcoin](/bitcoin/), [Litecoin](/litecoin/), [Dogecoin](/dogecoin/) |

</aside>

## The puzzle

In proof-of-work, miners compete to find a nonce (a random number) such that the hash of the block (which includes the nonce) meets a certain condition. The condition is set by the network's [difficulty](/difficulty-adjustment/): the hash must be smaller than a target value.

Because hash functions are unpredictable, there is no way to find a valid nonce other than trial-and-error. A miner must try billions of nonces until finding one that works.

Formally: given a block of transactions, a miner must find a nonce $n$ such that $H(B \| n) < T$, where $H$ is a hash function, $B$ is the block data, $\|$ is concatenation, and $T$ is the difficulty target.

## Security through work

The security of proof-of-work comes from the cost of attacking the network. If an attacker wants to rewrite history by mining an alternative chain faster than the honest network, they must do more computational work than all honest miners combined.

On [Bitcoin](/bitcoin/), this means controlling more than 50% of the total [hash rate](/hash-rate/) — the aggregate computational power of all miners. As of 2025, Bitcoin's hash rate is enormous, making a 51% attack prohibitively expensive.

This is elegant: security derives from real-world scarcity (electricity and hardware), not from trust in entities or clever cryptography.

## Mining incentives

Miners are incentivised by:

1. **Block reward.** The first miner to find a valid nonce receives newly minted Bitcoin. On [Bitcoin](/bitcoin/), the reward started at 50 BTC per block and halves every four years; currently it is about 6.25 BTC.
2. **Transaction fees.** Users include a small fee with their transactions. Miners collect fees from all transactions in a block.

As block rewards decrease (due to [halving](/bitcoin-halving/)), transaction fees become increasingly important for miner incentives.

## Decentralisation and mining pools

Initially, miners used CPUs (their computers). As mining became profitable, GPU mining became dominant. Eventually, specialised [ASIC miners](/asic-mining/) (application-specific integrated circuits) were developed.

ASICs are thousands of times more efficient at solving the puzzle than GPUs, but they cost hundreds of thousands of dollars. This creates a barrier to entry; only well-capitalized entities can mine competitively.

[Mining pools](/mining-pool/) allow smaller miners to combine their hash power and share rewards. Instead of waiting years to find a block individually, they contribute to a pool, which distributes rewards proportionally.

## Energy consumption

Proof-of-work requires substantial energy. Bitcoin's global network consumes ~10 gigawatts of power continuously (comparable to some small countries).

Environmentalists argue this is wasteful; proponents counter that:

1. This energy expenditure buys genuine security — an attacker must spend billions on electricity to mount an attack.
2. Mining often uses stranded or renewable energy (e.g., hydroelectric dams in regions with no transmission infrastructure).
3. The environmental cost should be weighed against the benefit: a global settlement network not controlled by any government.

## Alternatives and criticisms

[Proof-of-stake](/proof-of-stake/) uses far less energy — [Ethereum](/ethereum/) reduced energy consumption by ~99.95% after switching from proof-of-work to proof-of-stake.

However, proof-of-stake has different security assumptions: instead of economic security through energy cost, it relies on slashing (penalising misbehaving validators). Some argue this is weaker than proof-of-work's physical security.

## See also

<div class="wiki-seealso">

### Closely related

- [Mining Bitcoin](/mining-bitcoin/) — proof-of-work in practice
- [ASIC mining](/asic-mining/) — specialised hardware
- [Mining pool](/mining-pool/) — collaborative mining
- [Hash rate](/hash-rate/) — measure of mining power
- [Difficulty adjustment](/difficulty-adjustment/) — regulates mining pace

### Wider context

- [Proof-of-stake](/proof-of-stake/) — alternative consensus mechanism
- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Bitcoin](/bitcoin/) — the primary proof-of-work system
- 51% attack — attacking a proof-of-work network
- [Bitcoin halving](/bitcoin-halving/) — reduces block rewards over time

</div>

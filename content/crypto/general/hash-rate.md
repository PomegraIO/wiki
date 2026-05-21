---
title: "Hash Rate"
description: "Hash rate is a measure of the total computational power in a blockchain network, typically measured in hashes per second. It reflects the combined power of all miners or validators securing the network."
keywords:
  - hash rate
  - computational power
  - mining power
  - hashrate
  - network security
  - bitcoin
image: "/svg/crypto.svg"
---

*A **hash rate** is a measure of the total computational power in a [proof-of-work](/proof-of-work/) [blockchain](/blockchain-fundamentals/), measured in hashes per second. The network's hash rate indicates how much work is being performed to secure the blockchain. Higher hash rate means more security but also more energy consumption.*

<div class="wiki-hatnote">

This entry covers hash rate as a network metric. For the underlying mining, see [mining Bitcoin](/mining-bitcoin/); for the consensus mechanism, see [proof-of-work](/proof-of-work/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hash Rate — key facts</div>

<img src="/svg/crypto.svg" alt="Network hash rate over time" />

<div class="wiki-infobox-caption">Hash rate: a measure of mining power securing the network.</div>

|   |   |
|---|---|
| **What it is** | Total hashing power in the network |
| **Units** | Hashes per second (H/s) |
| **Bitcoin current** | ~1 exahash/second (10^18 hashes/s) |
| **Measurement** | Estimated from block times and difficulty |
| **Security indicator** | Higher hash rate means more expensive to attack |
| **Energy proxy** | Higher hash rate correlates with energy consumption |
| **Variability** | Increases over time as miners join and hardware improves |

</aside>

## Definition and units

A **hash** is one computation of a cryptographic hash function. When a miner solves a [proof-of-work](/proof-of-work/) puzzle, they compute millions of hashes until finding one that meets the target.

Hash rate is the number of hashes computed per unit time, typically per second:

- **H/s** (hashes per second) — 1 hash per second.
- **MH/s** (megahashes per second) — 1 million hashes per second.
- **GH/s** (gigahashes per second) — 1 billion hashes per second.
- **TH/s** (terahashes per second) — 1 trillion hashes per second.
- **PH/s** (petahashes per second) — 1 quadrillion hashes per second.
- **EH/s** (exahashes per second) — 1 quintillion hashes per second.

Bitcoin's current hash rate is approximately 1 EH/s, meaning the network collectively computes 10^18 hashes per second.

## How hash rate is calculated

The network does not directly report hash rate. Instead, it is estimated from:

1. **Block difficulty.** The protocol adjusts difficulty every 2,016 blocks to maintain ~10-minute block times.
2. **Actual block time.** If blocks are coming faster than 10 minutes, hash rate has increased; if slower, it has decreased.
3. **Formula.** Hash rate ≈ (Difficulty × 2^32) / (Average block time in seconds).

This estimation has a margin of error but is accurate enough to track trends.

## Security implications

Hash rate is a proxy for network security. A higher hash rate means more computational work is required to attack the network.

To perform a 51% attack on [Bitcoin](/bitcoin/), an attacker must control more than 50% of the hash rate. With 1 EH/s total, the attacker would need 500 PH/s of their own, costing billions of dollars in hardware and electricity.

As Bitcoin's hash rate increases, attacks become exponentially more expensive.

## Hash rate growth over time

Bitcoin's hash rate has grown exponentially:

- **2009:** Megahashes per second.
- **2013:** Terahashes per second.
- **2020:** Petahashes per second.
- **2024:** Exahashes per second.

This growth reflects:

- **Adoption:** More miners joining the network.
- **Hardware improvements:** Newer [ASIC](/asic-mining/) miners are more efficient.
- **Bitcoin price increases:** Higher prices incentivise mining, attracting new miners.

## Relationship to energy consumption

Hash rate and energy consumption are closely related but not identical. A higher hash rate means more computational work, which typically consumes more energy.

However, energy consumption also depends on hardware efficiency (joules per hash). Modern [ASIC](/asic-mining/) miners consume less energy per hash than older ones, so hash rate can increase without proportional energy growth.

Bitcoin's energy consumption is estimated at ~10 GW of power continuously (comparable to a medium-sized country).

## Mining incentives and hash rate volatility

Hash rate is not constant. When Bitcoin's price rises, [mining](/mining-bitcoin/) becomes more profitable, and miners deploy additional hardware, increasing hash rate. When price falls, mining becomes less profitable, unprofitable miners shut down, and hash rate declines.

This creates a feedback loop:

1. Bitcoin price rises.
2. Mining becomes profitable.
3. Miners add hardware (hash rate increases).
4. More difficulty, reduced block reward per hash.
5. Some miners become unprofitable and exit.
6. Hash rate stabilises at a new equilibrium.

## Hash rate and difficulty adjustment

The protocol adjusts [difficulty](/difficulty-adjustment/) every 2,016 blocks to maintain ~10-minute block times. If hash rate increases (blocks come faster), difficulty increases. If hash rate decreases (blocks come slower), difficulty decreases.

This feedback mechanism ensures that despite hash rate volatility, blocks arrive predictably.

## Hash rate as a bullish signal

Some analysts view hash rate growth as a bullish signal for Bitcoin, interpreting it as miner confidence in future Bitcoin price appreciation. If large-scale miners deploy new hardware, they are betting on higher future prices.

Others argue this is circular reasoning — high hash rate simply reflects current economic conditions, not future price.

## Comparison with proof-of-stake

[Proof-of-stake](/proof-of-stake/) blockchains like [Ethereum](/ethereum/) do not have a hash rate (or it is irrelevant). Instead, security is measured by the amount of staked cryptocurrency and the slashing penalty.

## See also

<div class="wiki-seealso">

### Closely related

- [Mining Bitcoin](/mining-bitcoin/) — what generates hash rate
- [Proof-of-work](/proof-of-work/) — the mechanism hash rate measures
- [ASIC mining](/asic-mining/) — hardware contributing to hash rate
- [Mining pool](/mining-pool/) — aggregates hash power
- [Difficulty adjustment](/difficulty-adjustment/) — responds to hash rate changes

### Wider context

- [Bitcoin](/bitcoin/) — the network being measured
- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- 51% attack — requires controlling hash rate
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where Bitcoin price (and mining profitability) is determined

</div>

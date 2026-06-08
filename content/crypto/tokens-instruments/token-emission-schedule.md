---
title: "Token Emission Schedule"
description: "Understand how a token emission schedule defines new coin creation over time, why the curve shape matters, and how to forecast long-term inflation."
keywords:
  - token emission schedule
  - token emission schedule crypto
  - coin inflation schedule
  - emission rate blockchain
image: /svg/crypto.svg
---

*A **token emission schedule** is the protocol's pre-defined blueprint for how many new tokens are created per block or epoch, and over what time horizon. It governs inflation, incentive timing, and the long-term dilution that existing holders face. Reading an emission schedule tells you whether a protocol is front-loading rewards to bootstrap the network or stretching incentives over decades.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Token Emission Schedule — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and tokens." />

<div class="wiki-infobox-caption">Inflation curves shape a protocol's economics and early adopter incentives.</div>

|   |   |
|---|---|
| **What it controls** | Total new tokens created per unit time (block, epoch, year) |
| **Why it matters** | Determines dilution, liquidity supply, and staking/mining rewards |
| **Common shapes** | Linear, exponential decay, step-wise (halvings), flat after a cap |
| **Units of time** | Blocks (Ethereum every ~12 sec), epochs (Solana every 432k blocks), years |
| **Typical duration** | 4–100+ years, or uncapped (but limited by max supply) |
| **How to read it** | Multiply daily emissions by price to forecast reward value; compare to max supply |

</aside>

## Why Protocols Define an Emission Schedule

A protocol must answer: *How do we reward miners or validators? How much new liquidity flows in each period?* Leaving this to ad-hoc decisions invites controversy and price instability. A transparent, immutable schedule builds trust and predictability.

The schedule also kickstarts network security. Bitcoin and early Ethereum paid miners almost entirely in newly created coins, not transaction fees. As networks mature and adoption grows, transaction fees replace block rewards, and emission tapers. Without a public schedule, early miners wouldn't know if rewards would persist, and late participants wouldn't know how much dilution to expect.

## Common Emission Curve Shapes

**Linear emission:** A constant number of tokens per block, forever or until a cap. Simple, transparent; early adopters get the same reward per unit work as later ones.

**Exponential decay (halving schedule):** Rewards are cut in half (or by a fixed percentage) every N blocks. Bitcoin halves every 210,000 blocks (~4 years). This front-loads rewards to early miners and progressively tapers inflation. After many halvings, emission approaches zero.

**Step-wise:** A series of announced reductions at fixed intervals (e.g., "Year 1: 100M tokens, Year 2: 80M, Year 3: 60M"). Common in early blockchain projects and ICO allocations.

**Curved (e.g., Ethereum Proof-of-Stake):** A formula adjusting rewards based on total staked capital. More stakers = lower per-unit rewards; fewer stakers = higher. Encourages participation without oversupplying.

**Capped vs. uncapped:** Some protocols (Bitcoin, Litecoin) define a hard max total supply. Others (Ethereum, Cosmos) have no cap, only a rate limit. A cap signals scarcity; no cap signals perpetual inflation management.

## Reading a Real Schedule: Bitcoin Example

Bitcoin emits 6.25 BTC per block (as of 2024) and halves every 210,000 blocks (~4 years):

| Period | Reward (BTC) | Halving event |
|--------|------------|--|
| 2009–2012 | 50 | Genesis |
| 2012–2016 | 25 | First halving |
| 2016–2020 | 12.5 | Second halving |
| 2020–2024 | 6.25 | Third halving |
| 2024–2028 | 3.125 | Fourth halving (2024) |
| 2140+ | ~0 | Tail emission negligible |

Over 210,000 blocks at an average 10-minute interval per block, approximately 4 years elapse. The schedule guarantees no more than ~21 million BTC will ever exist. In practice, transaction fees replace block rewards as inflation tapers.

An investor reading this sees: "Early miners earned 50 BTC per block; I'm entering when reward is 6.25 BTC; in four years it drops to 3.125 BTC. By 2140, new coin creation is nearly zero, and network security depends on transaction fees."

## Forecasting Long-Term Dilution

To estimate how much your stake will be diluted, calculate the cumulative new supply and compare it to current circulating supply.

**Example:** A protocol issues 100M tokens in Year 1, 80M in Year 2, 60M in Year 3 (linear decay). If 500M tokens are already in circulation:

- Year 1 inflation: 100M / 500M = 20%
- Year 2 inflation: 80M / (500M + 100M) = 13.3%
- Year 3 inflation: 60M / (500M + 100M + 80M) = 8.7%

A holder of 1% of supply in Year 1 will own less than 1% by Year 3, purely from dilution, unless they acquire new tokens to maintain their share. This is why investors care deeply about emission schedules—they quantify the risk of being "diluted out."

## Emission Schedules in Different Consensus Models

**Proof of Work:** Miners compete to solve puzzles and earn block rewards. High early emission attracts hash power; tapering emission later tests whether transaction fees sustain security.

**Proof of Stake:** Validators earn staking rewards (often 3–10% annually). The schedule typically caps total staked yield; rewards are lower if more capital stakes, to avoid infinite inflation.

**Delegated Proof of Stake (Cosmos, Solana):** Validators earn a fixed percentage of total stake. Emission adjusts to maintain a target staking ratio. If 30% of supply is staked and the target is 50%, emission rises to incentivize more delegators.

**Hybrid or variable:** Some protocols adjust emission dynamically based on network conditions—higher when security is weak, lower when decentralization is sufficient.

## How Emission Schedules Influence Price

Markets often price in the emission schedule's dilution. If a large emission cliff is approaching (e.g., a token unlock), prices can fall in anticipation. Conversely, if emission is scheduled to halve or disappear, price sometimes rises as scarcity rhetoric builds.

This is not always rational—price depends on demand, not supply alone. But a transparent schedule removes surprises and allows traders to model dilution into valuations.

## See also

<div class="wiki-seealso">

### Closely related

- [LP Token Impermanent Loss](/lp-token-impermanent-loss/) — how emission schedules fund liquidity mining that attracts LPs
- [Proof of Stake](/proof-of-stake/) — validation method that uses emission schedules to reward stakers
- [Proof of Work](/proof-of-work/) — mining reward structure tied to emission curves
- Staking Rewards — how emission is distributed to validators and delegators
- Token Vesting — related concept: when team and investor tokens unlock

### Wider context

- Inflation — monetary inflation in blockchain ecosystems
- Monetary Policy — how protocols govern supply and demand
- [Tokenomics](/tokenomics/) — broader analysis of token economic design
- [Initial Coin Offering](/initial-coin-offering/) — early token allocation that precedes emissions

</div>

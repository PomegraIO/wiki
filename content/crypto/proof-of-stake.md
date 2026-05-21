---
title: "Proof-of-Stake"
description: "Proof-of-stake is a consensus mechanism where validators lock up collateral (cryptocurrency) to earn the right to propose blocks. Validators who misbehave lose their collateral (are slashed), making attacks economically irrational."
keywords:
  - proof-of-stake
  - pos
  - validator
  - staking
  - consensus
  - ethereum
  - slashing
image: "/svg/crypto.svg"
---

*A **proof-of-stake** is a consensus mechanism where [validators](/validator/) lock up cryptocurrency as collateral and are selected to propose blocks in proportion to their stake. Validators earn rewards for honest participation but lose their collateral (are "slashed") if they misbehave, making attacks economically irrational. Proof-of-stake is far more energy-efficient than [proof-of-work](/proof-of-work/).*

<div class="wiki-hatnote">

This entry covers proof-of-stake as a mechanism. For its implementation in Ethereum, see [Ethereum](/ethereum/); for variations, see [delegated proof-of-stake](/delegated-proof-of-stake/); for alternatives, see [proof-of-work](/proof-of-work/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proof-of-Stake — key characteristics</div>

<img src="/svg/crypto.svg" alt="Validators staking collateral to secure the network" />

<div class="wiki-infobox-caption">Proof-of-stake: security through economic incentives.</div>

|   |   |
|---|---|
| **How it works** | Validators lock collateral and earn rewards for honest participation |
| **Security model** | Misbehaviour results in financial penalties (slashing) |
| **Who validates** | Token holders (after [staking](/staking/)) |
| **Reward** | Interest on staked tokens + transaction fees |
| **Energy cost** | Minimal (~99.95% less than [proof-of-work](/proof-of-work/)) |
| **Decentralisation** | Can be high, though wealth concentrates stake |
| **Time to finality** | Fast (seconds to minutes) |
| **Used by** | [Ethereum](/ethereum/) (since 2022), [Cardano](/cardano/), [Polkadot](/polkadot/) |

</aside>

## The staking mechanism

In proof-of-stake, validators deposit cryptocurrency into the protocol as collateral. The network periodically selects validators to propose the next block, usually with selection weighted by the amount staked.

For example, on [Ethereum](/ethereum/):

1. A validator deposits 32 ETH.
2. The validator's stake enters a queue.
3. Every 12 seconds (on average), the protocol selects a validator weighted by stake to propose a block.
4. If the validator is honest and the block is valid, they receive a reward.

The reward is not newly minted coin (or minimally so) but rather transaction fees or a fixed issuance. [Ethereum](/ethereum/) reduces its token supply as block rewards fall relative to fees.

## Slashing: the penalty mechanism

The key to proof-of-stake security is **slashing** — losing collateral for misbehaviour. If a validator:

- Proposes two conflicting blocks.
- Votes for conflicting chains.
- Fails to participate when selected.

The protocol automatically removes ("slashes") part or all of their staked collateral. A validator caught double-signing might lose their entire 32 ETH deposit.

This makes attacks economically irrational. If attacking the network would result in losing more money than you could gain, no rational actor would attack.

## Economic security

Proof-of-stake security is based on **economic finality** — reversing a transaction would cost more than the value stolen. On [Ethereum](/ethereum/), roughly 16 million ETH is staked (~$40+ billion as of 2025). Attacking the network would mean risking destruction of this capital.

This differs from [proof-of-work](/proof-of-work/), where security is based on **physical scarcity** — controlling 51% of the hash rate requires spending billions on electricity and hardware.

Both models work, but they make different trade-offs:

- **Proof-of-work:** Security relies on external resource costs (electricity), making it more resilient to attacks funded by cryptocurrencies gained from compromising the chain.
- **Proof-of-stake:** Security relies on crypto-economic penalties, which are strong but depend on slashing mechanisms working correctly.

## Energy efficiency

Proof-of-stake uses roughly 99.95% less energy than [proof-of-work](/proof-of-work/). The network does not need vast mining operations running 24/7; validators run on standard computers.

This makes proof-of-stake more environmentally sustainable and appeals to institutions concerned about energy consumption.

## Validator selection and centralisation risks

Validators are selected to propose blocks, typically weighted by their stake. A validator with 1% of staked tokens is roughly 1% likely to be selected.

This creates a potential wealth concentration risk: if rich entities accumulate large stakes, they have disproportionate power. To mitigate this, some networks implement:

- **Minimum stake.** Validators must stake at least X tokens, reducing concentration.
- **Slashing incentives.** Larger stakes face larger penalties, making concentration riskier.
- **Delegation.** Token holders delegate their votes to validators without locking up tokens.

## Liquid staking and derivatives

On [Ethereum](/ethereum/), [liquid staking](/liquid-staking/) services like Lido allow users to stake coins without locking them up. The service batches stakes and distributes staking rewards, while users receive a liquid token they can trade.

This increases accessibility but introduces new risks: if the liquid staking service fails, users might lose funds.

## Criticisms

Some argue that proof-of-stake is less proven than proof-of-work; [Ethereum](/ethereum/) only moved to proof-of-stake in September 2022. Edge cases in slashing or validator selection might emerge under unusual conditions.

Others argue that proof-of-stake is inherently plutocratic — wealth determines voting power, and the rich get richer from staking rewards. [Bitcoin](/bitcoin/) developers argue that proof-of-work's reliance on external resources (electricity) provides more equitable distribution of security power.

Proponents counter that plutocracy exists on proof-of-work too (large mining operators dominate) and that proof-of-stake's energy efficiency and sustainability are vital advantages.

## Proof-of-stake variants

- **[Delegated proof-of-stake](/delegated-proof-of-stake/)** — token holders vote for a small number of validators.
- **Liquid proof-of-stake** — users stake through intermediaries.
- **Nominated proof-of-stake** — validators self-nominate and are voted on.

## See also

<div class="wiki-seealso">

### Closely related

- [Validator](/validator/) — who validates proof-of-stake networks
- [Staking](/staking/) — how to earn rewards
- [Slashing](/slashing/) — penalties for misbehaviour
- [Liquid staking](/liquid-staking/) — staking without locking tokens
- [Delegated proof-of-stake](/delegated-proof-of-stake/) — a variation

### Wider context

- [Proof-of-work](/proof-of-work/) — alternative consensus mechanism
- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Ethereum](/ethereum/) — uses proof-of-stake
- [Cardano](/cardano/), [Polkadot](/polkadot/) — other proof-of-stake networks

</div>

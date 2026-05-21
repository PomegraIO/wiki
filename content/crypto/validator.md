---
title: "Validator"
description: "A validator is a network participant in a proof-of-stake blockchain who locks cryptocurrency collateral and earns the right to propose and attest to blocks. Validators are penalised if they misbehave."
keywords:
  - validator
  - proof-of-stake
  - staking
  - block proposal
  - consensus participant
  - slashing
image: "/svg/crypto.svg"
---

*A **validator** is a participant in a [proof-of-stake](/proof-of-stake) [blockchain](/blockchain-fundamentals) who locks cryptocurrency as collateral and participates in consensus by proposing and attesting to blocks. Validators are selected to propose blocks (often randomly or weighted by stake), earn rewards for honest participation, and lose collateral (are "slashed") if they misbehave.*

<div class="wiki-hatnote">

This entry covers validators in proof-of-stake systems. For miners in proof-of-work systems, see [mining Bitcoin](/mining-bitcoin); for staking mechanisms, see [staking](/staking).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Validator — key facts</div>

<img src="/svg/crypto.svg" alt="Validators securing a proof-of-stake network" />

<div class="wiki-infobox-caption">A validator: securing the network through stake and participation.</div>

|   |   |
|---|---|
| **What it is** | A participant in proof-of-stake consensus |
| **Collateral** | Locked cryptocurrency (stake) |
| **Selection** | Random (weighted by stake) or rotation-based |
| **Reward** | Interest on staked coins + transaction fees |
| **Penalty** | Slashing for misbehaviour |
| **Hardware** | Standard computer (unlike ASIC miners) |
| **Energy cost** | Negligible |
| **Example networks** | [Ethereum](/ethereum), [Cardano](/cardano), [Polkadot](/polkadot) |

</aside>

## Role in consensus

A validator's role is to:

1. **Propose blocks.** Periodically, a validator is selected to propose the next block in the chain.
2. **Attest to blocks.** Validators vote on the validity of blocks proposed by other validators.
3. **Follow rules.** Validators must follow the protocol rules (e.g., only vote for one chain at a time, include valid transactions).

## Selection and randomisation

Validators are selected to propose blocks using various mechanisms:

- **[Ethereum](/ethereum):** Uses a pseudo-random selection weighted by stake. A validator with 2% of staked ETH is roughly 2% likely to be selected to propose a block.
- **[Cardano](/cardano):** Uses verifiable random function (VRF) to select validators.
- **[Delegated proof-of-stake](/delegated-proof-of-stake):** Token holders vote for a small number of delegates who become validators.

Randomisation prevents validators from knowing in advance when they will be selected, reducing opportunities for coordination or attacks.

## Staking and collateral

To become a validator on [Ethereum](/ethereum), you must lock 32 ETH in a contract. This collateral:

- Gives you "skin in the game" — if you attack the network, you lose your own money.
- Makes attacks expensive — attacking requires controlling enough validators' collateral to offset gains.
- Serves as a bond that can be seized if you misbehave.

On other networks, minimum stake requirements vary ([Cardano](/cardano) has no minimum; [Polkadot](/polkadot) has a lower minimum).

## Rewards

Validators earn rewards for honest participation:

- **Block proposal rewards.** When a validator proposes a block, they earn a small reward (newly minted coins or transaction fees).
- **Attestation rewards.** When a validator votes to attest a block, they earn a small reward (proportional to how quickly they vote).

On [Ethereum](/ethereum), annual staking yield is typically 3–6%, depending on total amount staked (more staking = lower yield for each validator).

## Slashing and penalties

If a validator misbehaves (e.g., proposes two conflicting blocks or votes for two different chains), they are slashed:

- **Minor slashing.** Losing a small percentage of stake (e.g., 1% if you fail to participate when selected).
- **Major slashing.** Losing significant stake (e.g., 50% if you double-sign, greatly threatening network security).

Slashing is automatic and enforced by the protocol. A validator's collateral is cryptographically seized if they misbehave.

## Hardware requirements

Unlike [ASIC miners](/asic-mining) (which cost millions for large operations), validators require only standard computers:

- A modern laptop or desktop computer.
- Stable internet connection.
- 32 ETH stake (on [Ethereum](/ethereum)).

This lower barrier to entry means validators can be more geographically distributed and diverse than miners, theoretically improving decentralisation.

## Operator centralisation risk

Despite lower hardware requirements, validator operations have concentrated in:

- **Large institutional validators.** Crypto exchanges (like Kraken, Lido) run validators on behalf of customers.
- **[Liquid staking](/liquid-staking) services.** Services like Lido run validators and distribute rewards to token holders.

This centralisation creates risk: if a large validator operator is compromised or misbehaves, a significant portion of the network is affected.

[Ethereum](/ethereum) and other networks have tried to mitigate this by limiting rewards if a single entity controls too much stake and encouraging validator diversity.

## Active validators

[Ethereum](/ethereum) (as of 2024) has roughly 1 million active validators, with ~16 million ETH staked. This is a large and distributed validator set, improving decentralisation relative to proof-of-work mining (which is concentrated in pools).

[Cardano](/cardano) has ~3,000 active validators. [Polkadot](/polkadot) has ~300.

## Comparison with miners

| Aspect | Miner | Validator |
|--------|---|---|
| **Hardware** | Specialised (ASIC) | Standard computer |
| **Cost of entry** | High (ASIC + electricity) | Medium (stake) |
| **Ongoing cost** | High (electricity) | Low (internet) |
| **Penalty for misbehaviour** | None (can't misbehave in PoW) | Slashing (lose stake) |
| **Decentralisation** | Lower (concentrated in pools) | Higher (more distributed) |
| **Environmental cost** | High (energy) | Negligible |

Validators are generally more accessible than miners, though decentralisation is still threatened by institutional operators.

## Running a validator

To run a validator on [Ethereum](/ethereum):

1. Deposit 32 ETH into the staking contract.
2. Run validator software (Prysm, Lighthouse, etc.) on a computer.
3. Connect to the network and participate in consensus.
4. Earn ~4–6% annual yield on your staked ETH.

Withdrawals are possible and relatively quick (~few days), though operators must initiate them.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake) — the consensus mechanism
- [Staking](/staking) — how to become a validator
- [Slashing](/slashing) — penalties for misbehaviour
- [Liquid staking](/liquid-staking) — services for staking without running a validator
- [Delegated proof-of-stake](/delegated-proof-of-stake) — a validator selection mechanism

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals) — the underlying technology
- [Ethereum](/ethereum) — has ~1 million validators
- [Mining Bitcoin](/mining-bitcoin) — the proof-of-work equivalent
- Smart contract — validator deposits are contracts

</div>

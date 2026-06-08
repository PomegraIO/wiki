---
title: "How Staking Rewards Are Calculated in Proof-of-Stake Networks"
description: "The formulas networks use to derive per-validator rewards from total stake, issuance rate, and participation rate."
keywords:
  - staking rewards calculation
  - proof of stake rewards
  - validator rewards
  - stake-based incentives
  - epoch rewards
image: "/svg/crypto.svg"
---

*Networks calculate **staking rewards** using a formula that ties reward size to three key inputs: the validator's own stake, the total stake in the system, and the validator's participation rate. Most systems also target a specific total reward pool per epoch, meaning individual rewards scale down if more validators join.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Staking Rewards — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Incentive payments that reward validators for securing the network, sized by stake, participation, and network issuance.</div>

|   |   |
|---|---|
| **Reward pool** | Fixed per epoch or proportional to total stake |
| **Key factors** | Individual stake, total stake, participation rate |
| **Distribution model** | Proportional to stake (larger validators earn more) |
| **Participation requirement** | Typically 50%–67% of duties to qualify for full rewards |
| **Penalty mechanics** | Inactivity leak, slashing for rule violations |
| **Time to earn rewards** | One to two epochs, depending on finality rules |
| **Variability** | Rewards increase with fewer active validators; decrease as more join |

</aside>

## The base reward rate and the issuance cap

Most [proof-of-stake](/proof-of-stake/) systems define a target **issuance rate**: the total amount of new tokens minted per epoch as rewards. This rate is typically set as a fraction of total stake, rather than a fixed number of tokens.

For example, a network might target 2% annual issuance. If the total staked amount is 10 million tokens, the network will mint approximately 200,000 tokens per year as rewards (ignoring slashing and other adjustments).

The **base reward** for an epoch is derived from the issuance target divided by the number of validators (or effective validators, in systems that cap the maximum vote weight per validator). If the annual issuance is 200,000 tokens and there are 100 [epochs](/epoch-based-consensus-how-epochs-work/) per year (which is roughly true if each epoch is ~6 minutes), the per-epoch issuance is ~2,000 tokens.

This per-epoch pool is then divided among all participating validators, weighted by their stake and participation. The formula is typically:

```
Base Reward = (Total Issuance per Epoch) / (Total Effective Stake)
```

If the total effective stake is 10 million tokens, the base reward rate is 0.0002 tokens per token of stake per epoch. A validator with 32 tokens of stake would earn approximately 0.0064 tokens per epoch at full participation.

## Participation rate and performance adjustments

A validator earns the full base reward only if it completes all its assigned duties in an epoch. Most networks define "full participation" as the validator being online at its designated slot(s) and casting a valid vote.

The **participation rate** is the fraction of expected duties a validator actually completed. If a validator was supposed to attest in 32 slots and only attested in 28, its participation rate is 28/32 = 87.5%.

Rewards are then proportional to participation:

```
Validator Reward = Base Reward × Validator Stake × Participation Rate
```

If a validator with 32 tokens participates at 87.5%, it earns approximately 0.0064 × 0.875 = 0.0056 tokens for that epoch.

Some systems introduce additional adjustments based on vote timeliness. An attestation can be on-time (received early in the slot, counts toward full reward), or late (received after the slot deadline, counts toward a reduced reward). This incentivizes validators to optimize their network latency and honest behavior.

## The economic incentive: more stake, more reward in absolute terms

An important nuance: while the reward *rate* (percentage return) is the same for all validators regardless of size, the absolute reward grows with stake. A validator with 100 tokens earns roughly 3.1 times more tokens per epoch than one with 32 tokens (all else equal), because 100 × base reward > 32 × base reward.

This alignment is intentional. Larger validators have more capital at risk, so they should earn more in absolute terms. But they do not earn a higher *percentage* return, which would create a positive-feedback spiral where wealth accumulates indefinitely in the largest validators.

The typical target is that reward rates range from 3% to 5% annually in percent terms, depending on network security assumptions and the total staked amount. These rates assume a stable validator set and full participation; in practice, validators earn less if they miss duties or the network experiences congestion.

## Inactivity leaks: the penalty for offline validators

If a validator misses duties consistently (e.g., goes offline for hours or days), most networks impose an **inactivity leak**: a penalty that increases quadratically with the duration of the validator's absence.

The inactivity leak serves two purposes: it reduces the stake of absent validators (thereby reducing their voting power) and it creates a pressure for them to come back online or exit. Without this mechanism, a large offline validator could block consensus indefinitely while still claiming proportional rewards upon return.

The formula is typically:

```
Penalty per Epoch = (Validator Stake) × (Target Participation - Actual Participation) × (Leak Slope)
```

The leak slope is a small constant (e.g., 0.002 per epoch). If a validator does not participate for one epoch when it should, it loses roughly 0.2% of its stake. If it remains offline for 10 epochs, the cumulative loss is greater due to the quadratic effect.

Inactivity leaks are particularly harsh in networks that use them for finality enforcement. Ethereum 2.0, for instance, uses the leak to eventually reduce the offline validators' stake so much that the remaining online validators can reach 2/3 quorum and resume finality, even if one-third of the network is offline.

## Slashing: penalties for malicious behavior

Slashing is distinct from inactivity leaks. While leaks penalize offline validators, slashing penalizes validators that break consensus rules—for example, by signing two conflicting block proposals or by voting for two different chains.

Slashing penalties are typically harsh, removing a significant fraction of a validator's stake (often 10% to 50%) in a single incident. Slashing is also coordinated: if many validators are slashed in the same epoch due to a mass slashing event, the penalty increases (the "slashing multiplier"), discouraging coordinated attacks.

A slashed validator is removed from the active validator set immediately and must go through a re-entry delay before it can stake again. This deters deliberate misbehavior and makes consensus-breaking attacks economically expensive.

## Scaling rewards with network size

As more validators join a network, the total stake grows, but the issuance rate is often held constant (or scaled slowly). This means the reward *rate* per token decreases.

For example, if a network targets 2% annual issuance and total stake is 10 million tokens, the rate is 2% annually. But if total stake grows to 20 million tokens with the same issuance target, the rate drops to 1% annually.

This scaling mechanism aligns incentives: early validators earn higher returns because the network is small and capital is scarce. As the network matures and becomes capital-abundant, returns normalize to a sustainable long-term level. This discourages excessive staking (which would dilute returns) and encourages diversity in how capital is deployed.

Some networks experiment with variable issuance: if total stake is below a target, issuance increases; if above, it decreases. This keeps reward rates roughly stable even as the validator set grows. However, variable issuance introduces complexity and must be carefully calibrated to avoid either over-rewarding early stakers or failing to attract sufficient stake.

## Real-world examples: Ethereum 2.0 and Cosmos

Ethereum 2.0 uses an issuance rate proportional to the square root of total stake. The formula is:

```
Epoch Issuance = Base Issuance Rate × sqrt(Total Effective Balance)
```

This means that as more validators join, per-validator rewards decrease, but not linearly. A 100x increase in stake results in a ~10x decrease in per-validator reward rate. This encourages participation without creating a runaway positive feedback loop.

Cosmos's rewards use a simpler model: a fixed inflation target (e.g., 7% annually) is minted per year, and validator rewards are proportional to their stake. If more validators join, the total reward pool grows with inflation, so per-validator rates remain stable. However, this can lead to higher inflation if adoption is slower than expected.

Both approaches are valid; the choice reflects different philosophies about capital scarcity and network maturity.

## Calculating your expected rewards as a validator

To estimate personal staking rewards, a validator can use:

```
Annual Reward = Stake × Annual Reward Rate × Participation Rate
```

If you stake 32 tokens and the network's current annual reward rate is 4% with 95% participation, you would earn approximately 32 × 0.04 × 0.95 = 1.216 tokens per year.

Actual rewards vary with network conditions, participation rates, slashing events, and issuance adjustments. Most validators use on-chain reward analytics or their staking provider's dashboards to track real-time rates.

## See also

<div class="wiki-seealso">

### Closely related

- [Epoch-Based Consensus: How Epochs Structure Validator Duties](/epoch-based-consensus-how-epochs-work/) — How reward settlement times are determined by epoch boundaries
- [Tendermint BFT Consensus Explained](/tendermint-bft-consensus-explained/) — An alternative consensus design with different reward mechanics
- [Casper FFG: Ethereum's Finality Gadget Explained](/casper-ffg-finality-gadget/) — The finality layer that determines when rewards are locked
- [Proof-of-Stake](/proof-of-stake/) — The broader framework for staking and validator incentives

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — How token incentives align validators' behavior
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Where validators convert staking rewards to other assets

</div>
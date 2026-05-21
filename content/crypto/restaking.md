---
title: "Restaking"
description: "Restaking is a mechanism where cryptocurrency already staked in a proof-of-stake network is used to secure additional applications or sidechains. It increases yield but introduces additional slashing risks."
keywords:
  - restaking
  - eigenlayer
  - double-staking
  - dual-slashing
  - middleware
  - yield
image: "/svg/crypto.svg"
---

*A **restaking** mechanism allows users to use cryptocurrency already staked in a [proof-of-stake](/proof-of-stake/) network (like [Ethereum](/ethereum/)) to also secure other applications, sidechains, or services. Restaking increases yield but introduces additional slashing risks: if the restaked application is compromised, the original stake could be slashed.*

<div class="wiki-hatnote">

This entry covers restaking as a concept. For the underlying staking, see [staking](/staking/); for Ethereum's staking, see [Ethereum](/ethereum/); for slashing risks, see [slashing](/slashing/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Restaking — key facts</div>

<img src="/svg/crypto.svg" alt="Restaking architecture with multiple layers" />

<div class="wiki-infobox-caption">Restaking: earning yield on staking by securing multiple applications.</div>

|   |   |
|---|---|
| **What it is** | Using staked coins to secure multiple applications |
| **Primary use** | Eigenlayer (Ethereum-based) |
| **Yield increase** | Additional yield on top of base staking |
| **Risks** | Multi-layer slashing, application risk |
| **Lock-up** | Same as base staking (Ethereum: ~27 hours) |
| **Participants** | Ethereum validators and [liquid staking](/liquid-staking/) token holders |
| **Status** | Emerging (mainnet launched 2024) |

</aside>

## How restaking works

On a traditional blockchain like [Ethereum](/ethereum/), validators stake coins and earn rewards for securing the single network. Their stake is at risk only if they misbehave on [Ethereum](/ethereum/).

With restaking, validators can "restake" their [Ethereum](/ethereum/) stake (or [liquid staking](/liquid-staking/) tokens like stETH) to a separate application (called a middleware or AVS — actively validated service). For example:

1. **Base layer:** A validator stakes 32 ETH on [Ethereum](/ethereum/), earning ~4% staking rewards.
2. **Restaking:** The validator also commits their 32 ETH to an AVS (e.g., a data availability network).
3. **Dual yield:** The validator earns ~4% from [Ethereum](/ethereum/) + additional yield from the AVS (e.g., 5% more).
4. **Multi-layer risk:** If the AVS is compromised, the validator's 32 ETH could be slashed on both layers.

## Eigenlayer: the primary implementation

**Eigenlayer** is the most prominent restaking protocol, deployed on [Ethereum](/ethereum/). It allows validators and [liquid staking](/liquid-staking/) token holders to restake on applications built on top of [Ethereum](/ethereum/).

Applications built on Eigenlayer (called AVSs) can offer their own security to [Ethereum](/ethereum/) users while being secured by [Ethereum](/ethereum/)'s validator set.

## Yield composition

With restaking, yield consists of:

- **Base staking yield:** ~4–6% from [Ethereum](/ethereum/).
- **Application yield:** Variable, depending on the AVS (could be 5–20% or higher).
- **Fees:** Protocols take cuts of yields.

Total yield could reach 10–20%+ but introduces proportional risk.

## Risks: multi-layer slashing

The primary risk is multi-layer slashing. A validator could be slashed on:

1. **[Ethereum](/ethereum/) layer:** For misbehaving as an [Ethereum](/ethereum/) validator.
2. **Application layer:** For failing to properly secure the AVS.

If an AVS is compromised and validators are slashed there, their [Ethereum](/ethereum/) stake is also at risk.

Example: A validator restakes on a data availability AVS. The AVS is hacked, and the attacker causes the AVS to slash all validators. The validator's entire 32 ETH is at risk on both [Ethereum](/ethereum/) and the AVS.

## Opportunity costs and diversification

Restaking forces validators to choose between:

- **Diversification:** Restake on multiple AVSs, earning from multiple sources.
- **Concentration:** Restake heavily on high-yield AVSs, earning more but with greater risk.

Balancing these is a key challenge for restakers.

## Security assumptions

Restaking works only if:

1. **AVS security is high.** The application must not be trivially compromised.
2. **Slashing is properly enforced.** If validators are slashed on the AVS but not on [Ethereum](/ethereum/), the system fails.
3. **Validator incentives align.** Validators must not collude to perform attacks on the AVS.

Meeting all three is challenging, especially for newer AVSs with unproven security.

## Regulatory considerations

Restaking introduces complexity for tax and regulatory purposes:

- **Multiple yield sources.** Are they all taxed the same way?
- **Slashing treatment.** Is slashing a capital loss?
- **Securities regulation.** Are AVSs securities?

These questions remain largely unsettled.

## Comparison with traditional delegation

Restaking differs from traditional [delegated proof-of-stake](/delegated-proof-of-stake/):

- **Traditional delegation:** Token holders delegate votes to validators. Slashing is limited to the validator (delegators are not harmed).
- **Restaking:** Validators' stake is directly at risk on multiple layers.

Restaking gives validators stronger incentives to properly validate AVSs but also creates greater risk.

## Risks of application failure

If an AVS (e.g., a new data availability layer) fails or is compromised, restakers lose funds. This is similar to the risk of a [cryptocurrency exchange](/cryptocurrency-exchange/) failure — you lose what you deposited.

To mitigate this, restakers should:

- Research AVS security thoroughly.
- Diversify across multiple AVSs.
- Limit restaking to amounts they can afford to lose.

## Outlook

Restaking is emerging as a mechanism for funding new blockchain infrastructure. Instead of requiring its own validator set and security model, a new blockchain can plug into [Ethereum](/ethereum/)'s validator set via restaking.

This could accelerate blockchain innovation but introduces systemic risks if validators over-restake and multiple applications are compromised.

## See also

<div class="wiki-seealso">

### Closely related

- [Staking](/staking/) — the base mechanism
- [Slashing](/slashing/) — multi-layer slashing risks
- [Liquid staking](/liquid-staking/) — can be restaked
- [Ethereum](/ethereum/) — the base staking network
- [Validator](/validator/) — who restakes

### Wider context

- [Proof-of-stake](/proof-of-stake/) — the consensus mechanism
- Smart contract — restaking protocols use contracts
- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology

</div>

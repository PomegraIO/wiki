---
title: "Staking"
description: "Staking is the process of locking cryptocurrency as collateral in a proof-of-stake network to participate in consensus and earn rewards. Stakers receive interest on their staked coins but risk losing them if they misbehave."
keywords:
  - staking
  - proof-of-stake
  - validator
  - yield
  - collateral
  - rewards
image: "/svg/crypto.svg"
---

*A **staking** is the process of locking cryptocurrency (called a "stake") in a [proof-of-stake](/proof-of-stake/) [blockchain](/blockchain-fundamentals/) to participate in consensus and earn rewards. Stakers become [validators](/validator/) and propose or attest to blocks. In return, they earn interest on their staked coins, typically 3–10% annually.*

<div class="wiki-hatnote">

This entry covers staking as a mechanism. For proof-of-stake consensus, see [proof-of-stake](/proof-of-stake/); for liquid staking, see [liquid staking](/liquid-staking/); for the risks, see [slashing](/slashing/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Staking — key facts</div>

<img src="/svg/crypto.svg" alt="Staking rewards accumulation" />

<div class="wiki-infobox-caption">Staking: earning rewards by securing the network.</div>

|   |   |
|---|---|
| **What it is** | Locking cryptocurrency for consensus participation |
| **Collateral** | Cryptocurrency (e.g., 32 ETH on Ethereum) |
| **Reward** | Annual yield (typically 3–10%) |
| **Lock-up period** | Variable (days to years, depending on network) |
| **Risk** | Slashing if validator misbehaves |
| **Environmental cost** | Negligible (compared to mining) |
| **Accessibility** | Medium (requires some capital) |
| **Networks** | [Ethereum](/ethereum/), [Cardano](/cardano/), [Polkadot](/polkadot/) |

</aside>

## How staking works

1. **Deposit collateral.** A user deposits cryptocurrency (e.g., 32 ETH) into a smart contract.
2. **Become a validator.** The network registers the user as a [validator](/validator/), eligible to propose or attest to blocks.
3. **Earn rewards.** For honest participation, the validator earns rewards (newly issued coins + transaction fees).
4. **Risk slashing.** If the validator misbehaves, part or all of their stake is "slashed" (removed).
5. **Withdraw.** After an unbonding period, the validator can withdraw their stake plus accumulated rewards.

## Staking yield

Staking yields vary by network and total staked amount:

- **[Ethereum](/ethereum/):** ~4–6% annually (2024), declining as more stake joins.
- **[Cardano](/cardano/):** ~3–4% annually.
- **[Polkadot](/polkadot/):** ~10–15% annually.

Higher yields typically occur on networks with lower total stake (less competition for rewards). As staking becomes more popular, yields decline.

## Comparison with traditional investments

Staking yield resembles traditional interest or bond yields, offering a passive income stream. However:

- **No principal guarantee.** Your stake can be slashed, unlike FDIC-insured deposits.
- **Tax implications.** Staking rewards are typically taxable income.
- **Volatility.** The underlying asset (e.g., ETH) can drop in price, offsetting staking rewards.

## Risks: slashing

The key risk in staking is **slashing** — losing part or all of your collateral. This occurs if you:

- Propose two conflicting blocks.
- Vote for multiple incompatible chains simultaneously.
- Fail to participate when selected (minor penalty).

Slashing is automatic and enforced by the protocol. The risk of slashing keeps stakers honest and is what gives proof-of-stake its security guarantees.

## Unbonding and withdrawal timing

When a staker wants to exit, they trigger an unbonding period:

- **[Ethereum](/ethereum/):** ~1 day to exit the validator set + ~27 hours to receive your withdrawal.
- **[Cardano](/cardano/):** 1–3 epochs (~5–15 days).
- **[Polkadot](/polkadot/):** 28 days.

During this period, your stake remains at risk of slashing if you misbehave. Once withdrawn, you no longer earn rewards.

## Liquid staking

[Liquid staking](/liquid-staking/) services (like Lido, Rocket Pool) allow stakers to stake without running a validator and without locking funds. Users deposit cryptocurrency and receive a token (e.g., stETH) that:

- Earns staking rewards automatically.
- Can be traded, lent, or used in DeFi.

However, liquid staking introduces:

- **Service risk.** The staking service could fail or get hacked.
- **Centralisation risk.** Large liquid staking providers (Lido controls ~30% of Ethereum stake) concentrate staking power.
- **Fees.** Services take 5–10% of rewards.

## Solo staking versus pooled staking

**Solo staking:** Running your own validator node. Requires technical skill, hardware, and ~32 ETH (on Ethereum). Benefits: full control, full rewards. Risks: responsible for your own security.

**Pooled staking:** Joining a [liquid staking](/liquid-staking/) service. Benefits: no technical skill required, no lump capital requirement (can stake any amount), easier. Risks: service risk, centralisation, lower net rewards (after fees).

## Staking as monetary policy

Some view staking as a form of monetary policy: validators are incentivised to participate, expanding the money supply through rewards. This differs from proof-of-work, where new coins are mined at a fixed rate regardless of participation.

## Tax and regulatory considerations

In many jurisdictions, staking rewards are taxable income, even if they are not withdrawn. This can complicate tax reporting for stakers.

Some regulators treat staking as a security, raising questions about whether staking services are subject to securities regulations. This remains unsettled in many jurisdictions.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake/) — the underlying mechanism
- [Validator](/validator/) — who participates in staking
- [Slashing](/slashing/) — the penalty for misbehaviour
- [Liquid staking](/liquid-staking/) — services for staking without running a node
- [Ethereum](/ethereum/) — the primary staking network

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Restaking](/restaking/) — advanced staking on top of staking
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where staking tokens trade

</div>

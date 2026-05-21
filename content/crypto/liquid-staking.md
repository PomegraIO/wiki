---
title: "Liquid Staking"
description: "Liquid staking is a service that allows users to stake cryptocurrency and receive a liquid token representing their stake. Users earn staking rewards while retaining the ability to trade or use the token in other applications."
keywords:
  - liquid staking
  - staking derivative
  - lido
  - steth
  - yield farming
  - delegated staking
image: "/svg/crypto.svg"
---

*A **liquid staking** service allows users to stake cryptocurrency without locking it up. Users deposit coins and receive a liquid token (e.g., stETH) that automatically accumulates staking rewards. The token can be traded, lent, or used in [decentralised applications](/decentralized-exchange), providing liquidity while earning yield.*

<div class="wiki-hatnote">

This entry covers liquid staking services. For regular staking, see [staking](/staking); for yield farming, see yield-farming; for the risks, see [restaking](/restaking).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquid Staking — key facts</div>

<img src="/svg/crypto.svg" alt="Liquid staking token and derivative flows" />

<div class="wiki-infobox-caption">Liquid staking: earn rewards while maintaining liquidity.</div>

|   |   |
|---|---|
| **What it is** | Service providing staking without lock-up |
| **User receives** | Liquid derivative token (e.g., stETH) |
| **Staking yield** | Same as solo staking (~4–6% on Ethereum) |
| **Service fee** | 5–10% of staking rewards |
| **Lock-up period** | None (can withdraw anytime) |
| **Liquidity** | Token can be traded or used in DeFi |
| **Risks** | Service risk, smart contract risk, collateral risk |
| **Major providers** | Lido, Rocket Pool, Coinbase Staking |

</aside>

## How liquid staking works

1. **User deposits.** A user deposits cryptocurrency (e.g., ETH) to a liquid staking service.
2. **Service stakes.** The service pools users' deposits and runs validators.
3. **Service issues token.** The user receives a liquid token (e.g., stETH representing their stake).
4. **Token appreciates.** The token's value increases as staking rewards accumulate. 1 stETH might be worth 1.02 ETH after a year.
5. **User can trade.** The user can trade stETH for other assets, lend it, or use it in DeFi applications.
6. **User redeems.** To withdraw their original ETH + rewards, the user exchanges stETH back to the service.

## Major providers

**Lido Finance:** The largest liquid staking provider, managing ~30% of Ethereum stake (~$10+ billion). Users deposit ETH and receive stETH.

**Rocket Pool:** A decentralised liquid staking protocol. Users can become node operators (running validators for Rocket Pool) or deposit directly and receive rETH.

**Coinbase Staking:** Coinbase's staking service (also liquid) for exchange users.

## Advantages

**Liquidity.** Unlike solo staking (where funds are locked for weeks to exit), liquid staking tokens can be traded immediately. If you need cash, you can sell stETH.

**Accessibility.** No minimum amount required (unlike [Ethereum](/ethereum) solo staking, which requires 32 ETH).

**Simplicity.** No need to run validator software; the service handles it.

**Composability.** stETH can be lent, collateralised, or used in smart contracts, creating additional yield opportunities.

## Disadvantages

**Fee.** Liquid staking services take 5–10% of rewards, reducing net yield from ~4–6% to ~3.6–5.4%.

**Service risk.** If the staking service gets hacked or mismanages funds, you could lose deposits.

**Centralisation risk.** Large providers like Lido control significant portions of network validation, potentially threatening decentralisation.

**Smart contract risk.** If the liquid staking contract has a bug, staked funds could be locked or lost.

## The Ethereum Shanghai impact

Before [Ethereum Shanghai](/ethereum-shanghai) (April 2023), staking rewards were locked — validators could earn rewards but not withdraw them. Liquid staking emerged as a workaround.

After Shanghai, staking withdrawals became possible, reducing the advantage of liquid staking. However, liquidity benefits remain: you can trade stETH without waiting for a withdrawal.

## Centralisation and protocol risk

Lido's dominance (>30% of Ethereum stake) has sparked concerns:

1. **Single point of failure.** If Lido is compromised, a significant portion of Ethereum is affected.
2. **Governance risk.** Lido's governance decisions affect the entire network.
3. **Slashing risk.** If Lido makes a mistake that results in slashing, depositors lose funds.

To address this, some have proposed capping Lido's share or encouraging competition from other providers.

## Restaking on liquid staking

Advanced protocols (like Eigenlayer) enable **restaking** — using staked coins (or liquid staking tokens) to secure multiple networks simultaneously. This increases yield but introduces new risks:

- If a restaked application is compromised, your Ethereum stake could be slashed.
- Multiple layers of slashing risk compound the danger.

## Comparison with solo staking

| Aspect | Solo Staking | Liquid Staking |
|--------|---|---|
| **Yield** | Full rewards | Reduced (after fees) |
| **Lock-up** | Yes (~27 hours exit) | No |
| **Minimum** | 32 ETH | Any amount |
| **Complexity** | High (run validator) | Low (simple deposit) |
| **Risk** | Low (self-custody) | Medium (service risk) |
| **Liquidity** | Low | High |

Solo staking is better if you want maximum rewards and can tolerate lock-up. Liquid staking is better if you want immediate liquidity or have small amounts to stake.

## DeFi opportunities

stETH is used in numerous [decentralised applications](/decentralized-exchange):

- **Lending.** Lend stETH to earn interest.
- **Collateral.** Use stETH as collateral to borrow other assets.
- **Liquidity pools.** Provide stETH/ETH liquidity and earn trading fees.

These opportunities create additional yield but introduce smart contract risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Staking](/staking) — the underlying mechanism
- [Ethereum](/ethereum) — the primary staking asset
- [Ethereum Shanghai](/ethereum-shanghai) — enabled staking withdrawals
- [Validator](/validator) — who receives deposits
- [Restaking](/restaking) — advanced liquid staking application

### Wider context

- [Proof-of-stake](/proof-of-stake) — the consensus mechanism
- Smart contract — liquid staking uses contracts
- Yield farming — earning yield on staking derivatives
- [Decentralized exchange](/decentralized-exchange) — where liquid staking tokens trade

</div>

---
title: "Ethereum Shanghai"
description: "Ethereum Shanghai was an upgrade in April 2023 that enabled staking withdrawals. Users could finally unstake their ETH and receive staking rewards, completing the transition to proof-of-stake."
keywords:
  - ethereum shanghai
  - staking withdrawal
  - upgrade
  - eip-4895
  - validator
image: "/svg/crypto.svg"
---

*An **Ethereum Shanghai** (also called the "Shapella" upgrade) was a network upgrade deployed on 12 April 2023 that enabled staking withdrawals. Before Shanghai, [validators](/validator/) who staked ETH could not withdraw or access their staking rewards. Shanghai completed the transition to [proof-of-stake](/proof-of-stake/) by finally allowing withdrawal of staked funds.*

<div class="wiki-hatnote">

This entry covers Ethereum Shanghai as an upgrade. For Ethereum's broader history, see [Ethereum](/ethereum/); for staking, see [staking](/staking/); for liquid staking, see [liquid staking](/liquid-staking/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Ethereum Shanghai — key facts</div>

<img src="/svg/crypto.svg" alt="Staking withdrawal visualization" />

<div class="wiki-infobox-caption">Shanghai: unlocking staked ETH and earned rewards.</div>

|   |   |
|---|---|
| **Deployed** | 12 April 2023 |
| **Key feature** | Staking withdrawals enabled |
| **EIP** | EIP-4895 (Beacon Chain Deposit Contract) |
| **Impact** | Validators can now withdraw staked ETH |
| **Withdrawal queue** | Validators can withdraw in batches every ~5 days |
| **Prior state** | Staking rewards accumulated but could not be withdrawn |
| **Following upgrade** | [Ethereum Dencun](/ethereum-dencun/) (March 2024) |

</aside>

## The staking withdrawal problem

When the [Beacon Chain](/ethereum-merge/) launched in December 2020, users could stake ETH to become [validators](/validator/). However, the protocol did not support withdrawals — staked ETH and earned rewards were locked indefinitely.

This was intentional: during the testing phase of proof-of-stake, the Ethereum Foundation wanted to prevent mass exit if something went wrong. Once the mechanism was proven secure, withdrawals would be enabled.

However, this created a problem: validators had no way to access their rewards or exit staking. Some validators had staked ETH for over two years without being able to withdraw anything. This limited adoption of staking and frustrated existing validators.

## The withdrawal mechanism

Shanghai implemented withdrawal infrastructure. Validators could now:

1. **Partial withdrawals.** Automatically receive staking rewards (the interest earned) without unstaking the full 32 ETH.
2. **Full withdrawals.** Exit staking and receive the full staked amount plus all accumulated rewards.

Withdrawals are processed in batches every ~5 days, to avoid network congestion from mass exits.

## Economic impact

Shanghai's deployment had immediate economic effects:

- **Unlock of capital.** Tens of millions of ETH in staking became mobile. Some feared this would trigger a sell-off, but largely did not occur.
- **Staking reward clarity.** With rewards finally accessible, staking became more attractive. Participation in staking actually increased post-Shanghai.
- **Liquid staking expansion.** Services like Lido (which already operated via workarounds) could now offer cleaner withdrawal mechanics.

## Prior workarounds: liquid staking

Before Shanghai, [liquid staking](/liquid-staking/) services emerged as workarounds. These services:

1. Accepted ETH from users.
2. Staked the ETH themselves.
3. Issued users a receipt token (e.g., stETH on Lido).
4. Users could trade the receipt token, effectively unlocking their liquidity.

Liquid staking services enabled staking rewards before Shanghai, but at the cost of:

- **Service risk.** The staking service could fail, and users might lose funds.
- **Fee.** Services took a cut of staking rewards (typically 10%).
- **Complexity.** Trading a derivative token is more complex than simply unstaking.

Shanghai made liquid staking less necessary for basic withdrawal access, though liquid staking remains popular because it provides liquidity (you can trade stETH) while still earning staking rewards.

## Technical details

Shanghai introduced **EIP-4895**, which specifies how withdrawal credentials work. Validators can set an Ethereum address (called a withdrawal address) where their staking rewards and exited stake are sent.

The Beacon Chain (the [proof-of-stake](/proof-of-stake/) component) communicates with the execution layer (the smart contract layer) to process withdrawals.

## Transition to full proof-of-stake

Shanghai represented the final piece of [Ethereum](/ethereum/)'s transition to [proof-of-stake](/proof-of-stake/). With staking rewards now accessible, [proof-of-stake](/proof-of-stake/) became a complete, functional system:

1. **[Ethereum Merge](/ethereum-merge/)** (September 2022) — transition to PoS consensus.
2. **Ethereum Shanghai** (April 2023) — enable withdrawals, complete the transition.
3. **[Ethereum Dencun](/ethereum-dencun/)** (March 2024) — optimise for layer-2 scaling.

## Staking adoption post-Shanghai

After Shanghai, [validator](/validator/) participation increased:

- Staking yield became clear and accessible.
- Services built on staking (e.g., [liquid staking](/liquid-staking/) derivatives) matured.
- Retail and institutional interest in staking grew.

As of 2024, roughly 16–18 million ETH are staked (on the order of 40% of total supply), earning roughly 3–5% annual yield.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum/) — the network upgraded
- [Ethereum Merge](/ethereum-merge/) — prior upgrade enabling PoS
- [Ethereum Dencun](/ethereum-dencun/) — subsequent upgrade
- [Proof-of-stake](/proof-of-stake/) — the consensus mechanism
- [Validator](/validator/) — who can now withdraw
- [Staking](/staking/) — the mechanism enabled by Shanghai
- [Liquid staking](/liquid-staking/) — related staking service

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- Smart contract — the withdrawal mechanism is implemented here

</div>

---
title: "Proof of Stake Variants"
description: "Different mechanisms for securing blockchains through staking, including liquid staking, solo staking, and pool staking."
keywords:
  - proof of stake
  - liquid staking
  - solo staking
  - pool staking
  - proof-of-stake-variants
---

*A **proof of stake variants** refers to different ways validators can participate in blockchain consensus and earn staking rewards. The main variants—liquid staking, solo staking, and pool staking—offer different tradeoffs between simplicity, decentralization, and accessibility.*

<aside class="wiki-infobox">

| Variant | Minimum Stake | Accessibility | Reward Share | Complexity |
|---------|---------------|---------------|--------------|-----------|
| **Solo Staking** | Full validator (32 ETH) | High skill required | 100% of rewards | High |
| **Pool Staking** | Any amount | Easy | Shared equally | Low |
| **Liquid Staking** | Any amount | Easy; liquid token | Reduced by protocol | Low |
| **Staking-as-a-Service** | Any amount | Very easy; delegated | Share of rewards | Minimal |

</aside>

## Solo staking: the decentralization ideal

Solo staking means running your own [validator](/wiki/validator/) node independently. On Ethereum (post-[Merge](/wiki/ethereum-merge/)), you need 32 ETH (roughly $100K+ at current prices) to become a validator. You run the validator client software on your own hardware (or rented cloud server), it validates transactions and proposes blocks, and you earn staking rewards proportional to your stake and network participation.

Solo staking is the most decentralized option—you control your keys, your node, and your rewards with no intermediary. But it carries risks and burdens. You must maintain uptime (network penalties apply if your validator is offline and misses attestations). You must handle slashing risk—if your validator signs conflicting blocks (a serious protocol violation), your stake is slashed (penalized), losing up to your entire 32 ETH. You are responsible for security (key management, hardware uptime, software updates). This is why solo staking appeals mainly to technical enthusiasts and security-conscious institutions.

## Pool staking: shared infrastructure and rewards

In pool staking, many validators combine their stakes into a shared pool managed by a pool operator. A retail investor can contribute 0.1 ETH, 1 ETH, or any amount, and earn a proportional share of the pool's staking rewards, minus operator fees. The pool operator runs the validator infrastructure, ensures uptime, handles key management (or uses a secure custody solution), and distributes rewards regularly to all pool members.

Lido is the dominant [liquid staking](/wiki/liquid-staking/) pool on Ethereum, controlling ~30% of all staked ETH as of 2024. Participants deposit ETH into Lido, receive stETH (a liquid staking token), and earn staking rewards as stETH accrues value. They can trade or transfer stETH freely, while the underlying ETH generates yield. The tradeoff: Lido takes a ~10% fee (split between node operators and protocol), and participants are exposed to Lido's smart-contract risk (if the protocol has a bug, funds could be lost).

## Liquid staking: the composite solution

Liquid staking is pool staking with an added layer: the protocol issues a liquid token (like stETH, rETH, or cbETH) representing the staked ETH plus accrued rewards. This token can be traded, used as collateral, or staked again (called [restaking](/wiki/restaking/)), offering yield-generation opportunities that solo staking does not provide.

The appeal is clear: you deposit ETH into a liquid staking protocol, get a liquid token back, earn yield passively, and maintain liquidity (you can sell or transfer the token anytime). The tradeoffs: you pay operator fees, you incur smart-contract risk (if the protocol fails, your staked ETH might be locked or lost), and the liquid token may trade at a discount to the underlying ETH (creating slippage if you need to exit during stress).

## Staking-as-a-service (SaaS): outsourced validation

For non-technical or passive investors, staking-as-a-service providers (like Stakewise, Kraken, or Coinbase) handle all validator infrastructure. You deposit your cryptocurrency, they validate on your behalf, and you receive staking rewards minus their fee (typically 5–15%). This is the easiest path to staking rewards, but you are trusting a custodian with your private keys and bearing custodial and operational risk.

## Validator economics and reward distribution

Validators earn rewards in two forms: *block proposal rewards* (when your validator is selected to propose a block, you earn a portion of transaction fees and a base reward) and *attestation rewards* (for validating other blocks, a small daily reward). The total staking reward rate varies by network participation. On Ethereum, when 50% of ETH is staked, annual yield is roughly 3–4%; when only 10% is staked, annual yield can exceed 10% (because there are fewer validators sharing the rewards).

Pool staking operators typically distribute rewards after deducting their fee. Some pools charge percentage fees (Lido at ~10%), others charge fixed fees or have multiple fee tiers. Liquid staking protocols auto-compound rewards by increasing the token balance daily, so users need not claim rewards manually.

## Restaking and yield layering

[Restaking](/wiki/restaking/) protocols (like Eigenlayer) introduce another layer: validators can stake their staked position (or liquid staking token) again, securing additional services (oracles, bridges, sidechains) and earning additional rewards. A validator on Ethereum earning 3% base yield can deposit their stETH into Eigenlayer and earn an additional 5–10% yield on that stake, for a total yield near 8–13%.

But restaking adds complexity and risk. If the restaked protocol has a slashing event, the validator's Ethereum staked position can be slashed. If the restaking smart contract has a vulnerability, funds could be lost. This is why restaking is for sophisticated investors; the yield layering comes with compounded risk.

## Decentralization concerns with dominant protocols

Liquid staking protocols have grown so large that they pose centralization risk to networks. Lido on Ethereum controls >30% of staked ETH—if Lido's operator made decisions favoring some validators or censoring certain transactions, it could influence the network. Ethereum Foundation and community stakeholders have expressed concern that liquid staking concentration could undermine decentralization. Some validators deliberately choose solo staking or alternative pools to reduce concentration.

## Comparing the variants: a decision matrix

For a retail investor asking "how do I earn staking rewards?":
- **Want maximum rewards and can handle technical risk?** Solo staking.
- **Want simplicity and passive income?** Liquid staking (Lido, Rocket Pool) or SaaS.
- **Want decentralization and medium complexity?** Self-run node or alternative pool (Rocketpool, Stakefish).
- **Want maximum ease?** Exchange staking (Kraken, Coinbase) or SaaS provider.

For institutions and large holders, the calculus includes custody requirements, operational burden, slashing risk tolerance, and regulatory treatment (some regulators view staking rewards as income or interest, with tax implications).

<div class="wiki-seealso">

### Closely related
- [Proof of Stake](/wiki/proof-of-stake/) — Consensus mechanism using validator staking
- [Liquid Staking](/wiki/liquid-staking/) — Staking with liquid derivative tokens
- [Validator](/wiki/validator/) — Network participant securing the blockchain

### Wider context
- [Ethereum Merge](/wiki/ethereum-merge/) — Ethereum's transition to Proof of Stake
- [Restaking](/wiki/restaking/) — Staking staked positions for additional yield
- [Delegated Proof of Stake](/wiki/delegated-proof-of-stake/) — Variant where delegators choose validators

</div>

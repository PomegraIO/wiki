---
title: "Liquid Staking Token"
description: "Derivative tokens that represent staked cryptocurrency, enabling holders to earn staking rewards while maintaining transferable liquidity and participation in DeFi."
keywords:
  - liquid staking
  - staking derivative
  - proof of stake
  - ethereum
  - defi
  - yield token
image: "/svg/crypto.svg"
---

*When you [stake](/proof-of-stake/) cryptocurrency to secure a [blockchain](/blockchain-fundamentals/), your coins are locked and unavailable for trading or other uses. A **liquid staking token** solves that friction: you deposit coins into a staking service, receive a transferable derivative token (stETH, rETH, etc.), and keep earning staking rewards while the underlying coins remain staked. The derivative unlocks liquidity and opens DeFi opportunities, but introduces custodial and smart-contract risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquid Staking Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract mark representing digital assets and token mechanisms." />

<div class="wiki-infobox-caption">Tokens representing staked assets, enabling earn and transfer simultaneously.</div>

|   |   |
|---|---|
| **What it is** | A token issued in exchange for deposited coins, representing a claim on staked assets plus accrued rewards |
| **How earned** | Staking provider locks your deposit, earns [proof-of-stake](/proof-of-stake/) rewards, and grows your token's underlying value |
| **How liquid** | The derivative token is tradeable, composable in DeFi protocols, and swappable back for base coins |
| **Rebase or transfer** | Some liquid staking tokens rebase (balance grows daily); others accrue value through price appreciation |
| **Key providers** | Lido (stETH for Ethereum), Rocket Pool (rETH), Coinbase (cbETH), Kraken (staked ETH), various chains |
| **Primary use case** | Earning staking returns without sacrificing liquidity or DeFi participation |
| **Key risk** | Smart contract vulnerability, slashing of validator penalties, staking provider insolvency |

</aside>

## The staking problem liquid derivatives solve

[Proof-of-stake](/proof-of-stake/) blockchains like Ethereum require validators to lock up coins as collateral. In exchange, they earn new coins as rewards—currently around 3–5% annually on Ethereum, varying with network conditions. But locked coins can't be sold, traded, or deployed in DeFi protocols. You must choose: earn staking rewards (capital locked) or keep liquidity (no rewards).

Liquid staking tokens (LSTs) remove the choice. You deposit your coins into a staking provider, receive a derivative token immediately, and keep earning rewards on the staked balance. The derivative token is fully liquid—you can trade it, send it, or plug it into yield farms and lending protocols. You have staked security plus liquid flexibility.

This unlocked a massive flow of capital. Before liquid staking, perhaps 5–10% of stakeable coins participated; now, over 30% of Ethereum's staked base uses liquid derivative tokens. The mechanism proved so valuable that nearly every [proof-of-stake](/proof-of-stake/) chain developed its own versions.

## How rewards accrue to the token holder

When you deposit 1 ETH into Lido, you receive roughly 1 stETH. The Lido protocol combines your deposit with thousands of others into a large staking pool and runs validators. Each day, those validators earn ~0.0008 ETH per ETH staked. The protocol distributes those rewards by increasing your stETH balance—if you held 1.0 stETH yesterday, you now hold 1.0008 stETH, or approximately so.

This is a **rebase model**: your balance grows daily as rewards accrue. Every holder's balance expands proportionally. Alternatively, some protocols like Rocket Pool use a **price-appreciation model**: your rETH balance stays the same (1.0), but the price in ETH rises (now worth 1.0008 ETH). Both mechanisms deliver the same economic result—rewards flow to holders—but the mechanics differ.

Either way, you're earning without locking. Your stETH can be traded for ETH on an exchange, deposited into a lending protocol to earn additional yield, or used as collateral for loans. The derivative enables what a locked asset cannot: productive deployment in the broader ecosystem.

## The custodial and smart-contract risks

Using a liquid staking token introduces dependencies. You're no longer custody of your own staked coins; the staking provider controls them. If Lido's validators misbehave or are slashed (penalized for breaking protocol rules), your stETH value could drop. If Lido's smart contract has a vulnerability, your deposit could be lost entirely.

Lido is large and battle-tested, but it's not risk-free. Several smaller staking protocols have suffered exploits or governance attacks. And as long as a custodian holds your coins, there's counterparty risk: what if the provider is hacked, goes insolvent, or regulatory pressure forces it to freeze accounts?

This is a fundamental tradeoff. You gain liquidity and composability by delegating staking to a third party. You accept custodial risk in return. Traditional investors understand this via exchanges and brokers; crypto users often find it less obvious because the [blockchain](/blockchain-fundamentals/) promises to remove custodians.

## Slashing and validator penalties

A more subtle risk is **slashing**. If a validator misbehaves—attesting to the wrong block, double-signing, or going offline repeatedly—the [proof-of-stake](/proof-of-stake/) protocol penalizes it by destroying part of its staked balance. This penalty flows through to LST holders proportionally. A validator's ETH might be slashed by 1% or, in severe cases, 100%.

Lido and other large pools run professional validators and implement redundancy, so slashing is rare. But it's not zero. A single major exploit or coordinated attack could slash billions of dollars across the network. LST holders would absorb that loss directly, regardless of size.

## The secondary market and arbitrage

Because LSTs trade separately from the underlying asset, they can drift in price. If market sentiment sours on a staking provider, stETH might trade at a discount to ETH (say, 0.98 ETH per stETH). This creates arbitrage: buy stETH at a discount and redeem it for the staked ETH plus accrued rewards once the discount narrows or expires.

Most protocols allow redemption—you can always convert stETH back to ETH—but redemptions may have delays or fees. Early in Ethereum's history, Lido imposed a withdrawal queue that sometimes took weeks to clear. This meant a discounted stETH holder couldn't immediately recover the underlying, preventing the arbitrage from working smoothly.

These frictions make LSTs not truly interchangeable with the base asset, even though they're economically equivalent. Traders account for redemption risk, liquidity, and time delays when pricing the derivative.

## Diversification across protocols

Some sophisticated holders run staking across multiple protocols—some on Lido, some on Rocket Pool, some on a centralized exchange—to reduce single-provider risk. Rocket Pool emphasizes decentralization (any home user can run a validator), so it appeals to risk-averse holders. Lido emphasizes scale and institutional backing.

This fragmentation creates its own challenge: each derivative trades at slightly different spreads, complicating portfolio management. But it also reflects a healthy ecosystem in which no single provider dominates absolutely.

## The broader DeFi integration

The real power of LSTs lies in their DeFi composability. Once you hold stETH, you can use it in Aave to borrow stablecoins, or in Curve to provide liquidity and earn trading fees on top of your staking yield. A farmer might stack 4–5% staking rewards plus lending fees plus liquidity fees, creating a 7–10% blended yield.

This recursive yield-farming creates risk, too. Each layer of leverage or borrowed capital increases the odds of liquidation if prices move sharply. But for patient, risk-aware holders, LSTs have become foundational pieces of DeFi infrastructure.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of stake](/proof-of-stake/) — the consensus mechanism underlying staking
- [Rebasing token](/rebasing-token/) — tokens that adjust supply algorithmically
- DeFi — decentralized finance protocols and composable lending/trading
- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger systems and validation
- Token — digital assets on a blockchain
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — platforms for trading tokens and derivatives

### Wider context

- [Distributed ledger](/distributed-ledger/) — decentralized record-keeping systems
- [Ethereum](/ethereum/) — the largest proof-of-stake network using liquid staking
- [Hash rate](/hash-rate/) — measuring network security and mining power
- Yield — returns earned on capital
- Leverage — borrowing to amplify returns and risks

</div>

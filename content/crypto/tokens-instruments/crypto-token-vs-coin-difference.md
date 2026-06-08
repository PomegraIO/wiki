---
title: "Crypto Token vs Coin: Key Differences"
description: "Learn the difference between crypto tokens and coins: coins run on their own blockchains, tokens live on host chains. What this means for custody, fees, and security."
keywords:
  - difference between crypto token and coin
  - crypto token vs coin
  - what is a crypto coin
  - what is a crypto token
  - blockchain tokens vs coins
---

*The fundamental difference between crypto tokens and coins is simple: a **coin** has its own blockchain, while a **token** runs on an existing blockchain. Bitcoin is a coin. Ethereum is a coin. But the vast majority of digital assets—from Uniswap (UNI) to Shiba Inu (SHIB)—are tokens built on top of Ethereum or another chain. This distinction shapes how you custody them, what fees you pay, and which risks you face.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Coins vs Tokens — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">The distinction determines blockchain architecture, fee structure, and custody requirements.</div>

|   |   |
|---|---|
| **Coin** | Has its own blockchain; mined or minted at protocol level |
| **Token** | Lives on a host blockchain; created via smart contract |
| **Native currency** | Coins pay network fees; tokens typically cannot |
| **Independence** | Coins exist standalone; tokens depend on host chain uptime |
| **Examples** | Bitcoin, Ethereum, Monero | Uniswap, Chainlink, Tether |
| **Custody** | Coin wallets interact directly with blockchain | Token wallets are smart-contract addresses on the host chain |

</aside>

## What Makes a Coin Independent

A **coin** has its own independent blockchain. Bitcoin runs the Bitcoin network. Ethereum runs the Ethereum network. Monero runs the Monero network. Each maintains a full ledger of transactions, enforced by its own set of validators or miners. When you send Bitcoin to someone, you are transacting on the Bitcoin blockchain itself—no intermediary, no host chain required.

Because coins have independent blockchains, they serve as the native fuel of their networks. Bitcoin pays miners in newly minted Bitcoin and transaction fees in Bitcoin. This creates a direct economic incentive: the coin itself is what secures the network. You cannot build on Bitcoin or send Bitcoin transactions without using Bitcoin for those fees.

Coins are harder to create because they require launching and securing an entire blockchain. This is why relatively few coins exist—Bitcoin, Ethereum, Litecoin, Monero, Solana, and a few dozen others dominate by market cap.

## What Makes a Token Dependent

A **token** is a digital asset created and managed by a [smart contract](/smart-contract/) on an existing blockchain. When you hold a token, you do not own a separate ledger entry; instead, a smart contract on the host chain records that you own a balance of that token.

The vast majority of crypto assets are tokens. When you buy Uniswap (UNI), Chainlink (LINK), or Tether (USDT), you are acquiring a token that exists on Ethereum, Polygon, or another host chain. The token does not have its own blockchain—it is a line of code on someone else's.

Tokens are cheap to create. Anyone with basic Solidity knowledge can deploy a simple token contract in minutes. This is why thousands of tokens exist, and why most of them have zero value.

Because tokens live on a host chain, they inherit that chain's security and architecture. A token on Ethereum is only as secure as the Ethereum network. If Ethereum is under attack or experiences a major outage, your tokens go down with it.

## Custody and Wallet Mechanics

When you own a coin, your wallet software interfaces directly with that coin's blockchain. A Bitcoin wallet generates a private key that controls outputs on the Bitcoin ledger. An Ethereum wallet generates a private key that controls accounts on the Ethereum ledger.

When you own a token, your wallet still holds a private key, but that key controls a smart-contract address on the host chain. When you send Uniswap tokens to someone, Ethereum's network processes the transaction; your key authorizes it, but Ethereum's blockchain executes it. You are not transacting on a "Uniswap blockchain"—you are calling a function on a smart contract that Uniswap deployed on Ethereum.

This has a practical consequence: if the Uniswap contract is buggy or malicious, your tokens could be stolen or frozen. Coins cannot be frozen by code—only by the protocol itself, which requires network-wide consensus. Tokens can be frozen or altered by the contract developer, though reputable tokens typically use immutable or governance-controlled code.

## Fee Structures

Coins pay for network security through their own fees. When you send Bitcoin, you pay Bitcoin as a transaction fee—that Bitcoin goes to miners. When you send Ethereum, you pay Ethereum ([ether](/ethereum/)) as the gas fee. The fee is denominated in the coin itself.

Tokens do not directly pay for network security. When you send a Uniswap token on Ethereum, you pay Ethereum for the gas fee. The token contract itself does not mint new coins to pay validators. This creates an asymmetry: a token has value only because people assign it value through markets, not because it secures its own ledger.

Some tokens attempt to mimic coins by creating their own blockchains. If Uniswap deployed a separate "Uniswap chain," the UNI token on that chain would function more like a coin. A handful of tokens have done this, but the investment required is substantial.

## When Token Swaps Require Migration

Occasionally, a token project will announce a "swap" or "migration"—a process where token holders exchange old tokens for new ones, often when the project launches its own blockchain. When this happens, old tokens become worthless unless the project continues to support them.

For example, if Uniswap announced tomorrow that UNI would move to its own blockchain, holders would have a deadline to swap their Ethereum-based UNI for the new UNI coin. Tokens not swapped by the deadline would typically become unspendable, though this depends on the project's migration contract.

Coins, by definition, do not face this risk. Bitcoin cannot be migrated to another blockchain; there is only one Bitcoin blockchain, and you either own Bitcoin on it or you do not.

## Regulatory Implications

Coins and tokens face different regulatory scrutiny. Coins like Bitcoin and Ethereum are generally treated as property or commodities. Tokens often trigger securities concerns because they may entitle holders to future profits or governance rights, making them resemble stocks.

A coin is harder to label as a security because it is not backed by a corporation promising future returns. A token, especially one with a centralized issuer who retains control of its smart contract, can more easily be viewed as a security offering. This is why token projects often include legal disclaimers and geographic restrictions.

## Key Reasons the Distinction Matters

The token-vs-coin distinction is not merely academic. It determines whether an asset can be frozen, whether it can be migrated away from you, how it is taxed, whether you can custody it directly or must use an exchange, and whether it carries counterparty risk beyond the blockchain itself.

Coins are standalone; tokens are embedded in another system. For everyday usage, this matters less—your wallet hides most of the complexity. But for custody, for understanding your exposure to smart-contract bugs, and for predicting regulatory treatment, the distinction is fundamental.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart contract](/smart-contract/) — code running on-chain that defines token behavior and rules
- [Token migration in crypto](/token-migration-crypto/) — how protocols swap old tokens for new ones, and what happens to unmigrated holdings
- [Proof of work](/proof-of-work/) — the mining mechanism that secures coins like Bitcoin
- [Proof of stake](/proof-of-stake/) — the validation mechanism used by coins like Ethereum
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where token and coin trades happen
- [Revenue-sharing token](/revenue-sharing-token/) — a type of token that distributes protocol fees to holders
- [Distributed ledger](/distributed-ledger/) — the underlying technology powering coins

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — how distributed ledgers record and verify transactions
- [Initial public offering](/initial-public-offering/) — how traditional corporations raise capital; tokens sometimes mimic this structure
- Security — what regulators use to classify tokens versus coins

</div>
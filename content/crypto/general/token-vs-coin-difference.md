---
title: "Token vs Coin: Key Differences"
description: "The difference between crypto tokens and coins: coins have their own blockchain, tokens run on existing ones. Examples and why it matters for trading and security."
keywords:
  - token vs coin
  - difference between crypto token and coin
  - cryptocurrency tokens
  - native coins blockchain
  - erc-20 tokens
---

*A **coin** is a cryptocurrency with its own independent blockchain; a **token** is a digital asset issued and run on top of an existing blockchain. [Bitcoin](/bitcoin/) and [Ethereum](/ethereum/) are coins. USDC (USD Coin) and most other assets trading on Ethereum are tokens. The distinction matters for security, divisibility, and how they move on the network.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Coins vs Tokens — what sets them apart</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Coins are independent; tokens are passengers on someone else's blockchain.</div>

|   |   |
|---|---|
| **Blockchain** | Coin: owns its own network. Token: runs on another network |
| **Examples of coins** | Bitcoin, Ethereum, Solana, Cardano |
| **Examples of tokens** | USDC (on Ethereum), Chainlink (on Ethereum), USDT (multichain) |
| **Speed and fees** | Token: inherit host blockchain's speed and cost |
| **Smart contract** | Token: requires smart contract code to function |
| **Security model** | Coin: independent consensus; Token: depends on host chain |
| **Transferability** | Both can move between wallets, but tokens follow host rules |

</aside>

## Coins: blockchains with native currencies

A **coin** is the native currency of a blockchain network. When developers build a [blockchain](/blockchain-fundamentals/), they define a primary currency—the coin—that powers the network. That coin is used to pay transaction fees, incentivize miners or validators, and secure the network through [proof-of-work](/proof-of-work/) or [proof-of-stake](/proof-of-stake/) mechanisms.

Bitcoin is the canonical example. It has its own network of thousands of nodes validating transactions and maintaining the blockchain. Ethereum is another: it has its own network, and ether (ETH) is its native coin.

Coins are issued directly by the blockchain's consensus rules. You can only send and receive a coin on its own network. A Bitcoin wallet communicates with the Bitcoin network; you cannot send Bitcoin through the Ethereum network.

## Tokens: contracts on existing chains

A **token** is a digital asset created and managed by a [smart contract](/smart-contract/) running on an existing blockchain. The token is not independent; it lives inside the blockchain it's deployed on. The most common standard is the ERC-20 token on Ethereum, which defines how a token can be transferred, approved for spending, and tracked.

USDC (the stablecoin pegged to the US dollar) is an ERC-20 token deployed on the Ethereum network. When you transfer USDC, you're really executing a transaction on the Ethereum blockchain. You pay Ethereum transaction fees (in ETH), and the Ethereum network validates the transfer.

Tokens can be created by anyone—a company, a startup, a community. You write smart contract code, deploy it to a blockchain, and launch your token. This accessibility is why thousands of tokens exist across Ethereum, Solana, Polygon, and other chains.

## Why the distinction matters

**Security and decentralization**: A coin like Bitcoin or Ethereum is only as secure as its network's consensus. If the network is attacked, the coin's security is at risk. A token's security depends not just on the smart contract code but also on the host blockchain. If Ethereum is compromised, all ERC-20 tokens on it are vulnerable.

**Speed and cost**: Tokens inherit the transaction speed and fees of their host blockchain. Sending USDC on Ethereum costs an Ethereum gas fee and takes time according to Ethereum's block time. If you send USDC on Solana (the same token, deployed on a different chain), the fee and speed reflect Solana's network. Some tokens, like USDT, exist on multiple blockchains—each version is a separate token, even though they represent the same underlying value.

**Standardization**: ERC-20 tokens follow a common standard, so wallets and exchanges can easily support them. Bitcoin and Ethereum each have their own rules, so supporting a new coin requires more custom work.

**Utility and governance**: Coins usually have a clear role—securing the network, paying fees, or incentivizing participation. Tokens can be pure value transfers (like USDC), governance tokens (allowing holders to vote on protocol changes), or rewards for participation in a platform.

## Examples side by side

**Native coins** (own blockchains):
- [Bitcoin](/bitcoin/) — the Bitcoin network
- [Ethereum](/ethereum/) — the Ethereum network
- Solana — the Solana network
- Cardano — the Cardano network

**Tokens** (on Ethereum):
- USDC — stablecoin pegged to the US dollar
- Chainlink (LINK) — oracle network utility token
- Aave (AAVE) — governance token for the Aave lending protocol
- Uniswap (UNI) — governance token for the Uniswap [decentralized exchange](/decentralized-exchange/)

**Tokens** (on other chains):
- Wrapped Bitcoin (wBTC) — representation of Bitcoin as an ERC-20 token
- USDC on Solana — same stablecoin, different blockchain

## How tokens are created and issued

A token launch typically involves:

1. Writing smart contract code that defines the token's rules (maximum supply, minting, burning, transfer restrictions, etc.).
2. Deploying the contract to a blockchain (Ethereum, Solana, Polygon, etc.).
3. Assigning initial balances to addresses (the token creator, investors, or a community fund).
4. Listing the token on a [cryptocurrency exchange](/cryptocurrency-exchange/) so others can buy it.

Some tokens are centralized (issued and controlled by a company, like USDC from Circle). Others are decentralized (issued through a protocol, with rules enforced by code rather than a single issuer).

## Why people sometimes confuse the terms

The term "token" is sometimes used loosely to mean any cryptocurrency, including coins. But in precise usage, the distinction is important. A news headline might say "Bitcoin token," but technically Bitcoin is a coin. Understanding the difference helps you evaluate security, transaction costs, and how an asset actually moves.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — how blockchains work and why coins need their own networks
- [Proof-of-Work](/proof-of-work/) — the consensus mechanism securing coins like Bitcoin
- [Proof-of-Stake](/proof-of-stake/) — the consensus mechanism securing Ethereum and other modern chains
- [Smart Contract](/smart-contract/) — the code that powers tokens on existing blockchains
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where both coins and tokens are traded
- [Ethereum](/ethereum/) — the leading blockchain for token issuance

### Wider context

- [Bitcoin](/bitcoin/) — the first and most recognized coin
- [Distributed Ledger](/distributed-ledger/) — the category of technology underlying both coins and tokens
- [Decentralized Exchange](/decentralized-exchange/) — where tokens can trade without a central issuer

</div>

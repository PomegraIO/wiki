---
title: "Token Standard"
description: "Open specifications like ERC-20 and ERC-721 that define how tokens function and interoperate within a blockchain ecosystem."
keywords:
  - token standard
  - ERC-20
  - ERC-721
  - NFT standard
  - blockchain interface
  - smart contract specification
image: /svg/crypto.svg
---

*A **token standard** is a set of rules and function specifications that define how a [token](/stock/) on a particular [blockchain](/stock/) behaves—what methods smart contracts must implement, how transfers work, what data is stored—ensuring interoperability across exchanges, wallets, and applications. ERC-20 and ERC-721 are the dominant standards on [Ethereum](/stock/), and similar frameworks exist on other chains.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Token Standard — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and tokens." />

<div class="wiki-infobox-caption">The common language that lets tokens work across wallets and exchanges.</div>

|   |   |
|---|---|
| **What it is** | A published specification that mandates which smart-contract functions a token must expose and how they behave |
| **Purpose** | Ensure tokens can be transferred, traded, and integrated without custom code for each token |
| **Common examples** | ERC-20 (fungible tokens), ERC-721 (NFTs), ERC-1155 (multi-token contracts) |
| **Adoption layer** | Wallets, exchanges, DeFi protocols all recognize standard tokens natively |
| **Evolution** | New standards emerge to address limitations of predecessors (e.g., ERC-1155 combines multiple token types in one contract) |

</aside>

## Why standards are necessary

Before standards, each token was a bespoke smart contract with its own transfer logic, approval mechanisms, and data structures. If you created a token on [Ethereum](/stock/), every exchange had to write custom code to support it. Wallets couldn't generically display balances. Decentralized protocols couldn't reliably interact with tokens because the interface was unpredictable.

Standards solved this by establishing a contract. Any project that implements ERC-20, for instance, promises to provide specific functions—`transfer()`, `balanceOf()`, `approve()`—with defined behaviour. The moment a token meets the ERC-20 spec, thousands of existing tools (MetaMask wallet, Uniswap DEX, Compound lending protocol) immediately understand it and can interact with it.

This dramatically lowered the friction to creating and trading new [tokens](/stock/).

## ERC-20: the fungible token standard

ERC-20 is the foundational standard on [Ethereum](/stock/) for fungible tokens (interchangeable units, like currency). All ERC-20 tokens have the same basic methods:

- `transfer(address recipient, uint amount)` — move tokens from the caller to another account
- `balanceOf(address account)` — check how many tokens an account holds
- `approve(address spender, uint amount)` and `transferFrom(address from, address to, uint amount)` — authorize another contract or account to spend tokens on your behalf

The `approve` / `transferFrom` pattern is crucial: it allows DeFi protocols to move your tokens without you handing over private keys. When you interact with a [lending protocol](/stock/) or a DEX, you first approve the contract to spend a certain amount, then the contract calls `transferFrom` to execute trades or borrowing.

Most [cryptocurrencies](/stock/) built on [Ethereum](/stock/)—stablecoins, utility tokens, [governance tokens](/stock/)—are ERC-20 compliant. Millions of tokens have launched using this standard.

## ERC-721: the non-fungible token standard

ERC-721 defines how non-fungible tokens (NFTs) work. Unlike ERC-20, where each token unit is identical, every ERC-721 token has a unique identifier and metadata. The standard mandates:

- `ownerOf(uint tokenId)` — retrieve who owns a specific NFT
- `transferFrom()` and `safeTransferFrom()` — move ownership of an NFT
- `approve()` — authorize someone else to transfer the NFT
- Metadata hooks that point to JSON files describing the NFT's properties

ERC-721 is less concerned with quantity (you don't "send 5 NFTs" in the way you send 5 tokens) and more with identity and provenance. Every NFT has a distinct owner, history, and data.

Most blockchain-based art, collectibles, and in-game items use ERC-721 or its successors.

## ERC-1155: the multi-token standard

ERC-1155 is a newer, more flexible standard that can represent both fungible and non-fungible tokens in a single contract. Instead of deploying separate contracts for currency and collectibles, a game developer can use one ERC-1155 contract to manage potions (fungible), unique swords (non-fungible), and batches of crafting materials (semi-fungible) all at once.

ERC-1155 is more gas-efficient than managing hundreds of separate ERC-20 and ERC-721 contracts, especially for games or projects with large token ecosystems.

## Standards beyond Ethereum

Other blockchains have adopted similar frameworks:

- **Solana** uses the SPL (Solana Program Library) standard for tokens
- **Bitcoin** has layer-2 token protocols like Stacks (for smart contracts) and the Ordinals framework (for NFTs)
- **Polygon**, **Arbitrum**, and other [Ethereum](/stock/) Layer 2s typically reuse ERC-20, ERC-721, and ERC-1155 directly
- **Tron**, **Binance Smart Chain**, and other EVM-compatible chains adopt ERC standards wholesale

This allows tokens to be bridged across chains or recognized by cross-chain tools.

## How standards enable DeFi

The liquidity and composability of modern [decentralized finance](/stock/) depends on standards. Because every token follows ERC-20, a [DEX](/stock/) can list any new token with zero custom integration. A [lending protocol](/stock/) can immediately accept any ERC-20 as collateral. A cross-chain bridge can transport tokens knowing they'll behave the same on the destination chain.

Without standards, each token would be an island. With them, new tokens can plug into an entire ecosystem of existing applications the moment they launch.

## Evolution and governance

Standards are proposed, debated, and ratified by the developer community, often via formalized Ethereum Improvement Proposals (EIPs). ERC-20 was proposed in 2015; ERC-721 in 2018; ERC-1155 in 2018. The process is open but conservative—changing a standard retroactively could break millions of tokens and applications.

New standards emerge when limitations are discovered or new use cases arise. Fungible tokens with metadata, wrapped versions of other tokens, and tokens with built-in burn or staking mechanisms have spawned variations. But ERC-20 and ERC-721 remain the overwhelming default, partly due to network effects and partly because they are sufficient for most use cases.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — how the underlying chains enable token standards
- [Smart Contract](/stock/) — the code that implements token standards
- [Ethereum](/ethereum/) — the chain where ERC standards originated
- [Meme Coin](/meme-coin/) — tokens that use ERC-20 but add no utility beyond community
- [Initial DEX Offering](/initial-dex-offering/) — a launch method that relies on ERC-20 compatibility
- [Distributed Ledger](/distributed-ledger/) — the shared record-keeping layer tokens operate on

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where standard tokens are traded
- [Decentralized Finance](/stock/) — enabled by token interoperability via standards
- [Smart Contract](/stock/) — the code layer that implements standards
- [Proof of Stake](/proof-of-stake/) — how some [tokens](/token-standard/) provide governance or staking rights
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — increasingly scrutinizing tokens as potential securities

</div>

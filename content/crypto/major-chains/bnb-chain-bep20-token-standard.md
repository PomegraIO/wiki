---
title: "BNB Chain BEP-20 Token Standard"
description: "BEP-20 is the token standard for BNB Smart Chain; it mirrors ERC-20 and defines how fungible tokens are created and transferred."
keywords:
  - bnb chain bep20 token standard
  - bep20 specification
  - binance smart chain tokens
  - fungible token implementation
image: "/svg/crypto.svg"
---

*The **BEP-20 token standard** is the specification that governs fungible tokens on BNB Smart Chain (formerly Binance Smart Chain). It is functionally identical to Ethereum's ERC-20 standard—defining required functions for transfer, balance tracking, and allowance delegation—but deployed on a separate blockchain with different gas economics and settlement speed. Developers implement BEP-20 to create tokens that wallets, exchanges, and on-chain protocols can interoperate with.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">BEP-20 Token Standard — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">A technical specification that ensures fungible tokens on BNB Smart Chain are interoperable and predictable.</div>

|   |   |
|---|---|
| **Blockchain** | BNB Smart Chain (BSC) |
| **Token type** | Fungible (each unit is identical) |
| **Parallel standard** | ERC-20 on Ethereum |
| **Required functions** | Transfer, approve, allowance, balanceOf, totalSupply, decimals, symbol, name |
| **Optional extensions** | Burn, mint, pause, access control |
| **Governance** | BEP standards maintained by Binance and the community |
| **Primary use** | Stablecoins, governance tokens, wrapped assets, DeFi tokens |

</aside>

## The BEP-20 Specification

BEP-20 is a technical standard that defines the behavior all fungible tokens on BNB Smart Chain must exhibit. When a developer writes a smart contract to create a token, the contract must implement specific functions and events so that wallets, decentralized exchanges ([DEXes](/decentralized-exchange/)), and other on-chain applications know how to interact with it.

The core required functions are:

| Function | Purpose |
|---|---|
| `balanceOf(address)` | Returns the token balance of an account |
| `transfer(to, amount)` | Sends tokens from caller's account to another |
| `approve(spender, amount)` | Allows a third party (spender) to withdraw tokens on your behalf, up to a limit |
| `allowance(owner, spender)` | Returns the amount a spender is permitted to withdraw |
| `transferFrom(from, to, amount)` | Moves tokens on behalf of another account (used by spenders with an allowance) |
| `totalSupply()` | Returns the total number of tokens in circulation |

Additionally, tokens expose metadata:

- **name**: The token's human-readable name (e.g., "Binance USD")
- **symbol**: A short ticker, usually 3–6 uppercase letters (e.g., "BUSD")
- **decimals**: How many decimal places the token supports (typically 18, allowing for tiny fractional amounts)

For example, if a token has 18 decimals and a balance is stored as 1,000,000,000,000,000,000 (in the smallest unit), it displays as 1.0 to the user.

## How BEP-20 Mirrors ERC-20

The BEP-20 standard was modeled directly on Ethereum's ERC-20 standard because Binance and the broader Ethereum ecosystem recognized that a consistent token interface was essential for ecosystem composability. If every token had its own unique interface, wallets and exchanges would need custom code for each one—a maintenance nightmare.

By making BEP-20 functionally identical to ERC-20, developers familiar with Ethereum can deploy tokens on BNB Smart Chain with minimal changes. Libraries and development tools (Solidity, OpenZeppelin) provide standard BEP-20 implementations that are audited and battle-tested.

The chief difference between ERC-20 and BEP-20 is not the standard itself but the underlying blockchain: BNB Smart Chain uses Proof of Stake Authority (PoSA) consensus, finality in ~3 seconds, and dramatically lower gas fees (often cents per transaction versus dollars on Ethereum).

## Required Events

The standard also defines three required events that smart contracts must emit (log) when state changes:

- **Transfer(from, to, value)**: Logged whenever tokens are moved from one account to another
- **Approval(owner, spender, value)**: Logged when an account approves a spender
- **Burn(amount)** (optional but common): Logged when tokens are permanently removed from circulation

These events are not strictly required by the BEP-20 spec but are a de facto standard. Wallets and block explorers monitor these events to show users transaction histories and balance changes.

## Optional Extensions

Many tokens build on the basic BEP-20 interface with additional features:

- **Mint**: A function to create new tokens (usually restricted to an owner or governance contract)
- **Burn**: A function to permanently remove tokens from circulation
- **Pause**: An emergency function to freeze all transfers (used during security incidents)
- **Access Control**: Role-based permissions (e.g., only an admin can mint; only a timelock can update parameters)
- **Snapshot**: A function to record token balances at a specific block height (useful for voting or governance snapshots)

These extensions do not violate BEP-20 compliance; they add functionality on top.

## Interoperability and Ecosystem

Because BEP-20 is standardized, a token automatically becomes usable in:

- **Wallets**: MetaMask, Trust Wallet, and others recognize BEP-20 tokens and can display balances, handle transfers, and approve allowances.
- **Decentralized exchanges**: PancakeSwap and other DEXes have standard pools and routing logic for any BEP-20 token.
- **DeFi protocols**: Lending platforms, yield farms, and derivatives protocols can integrate BEP-20 tokens via standard smart contract interfaces.
- **Bridges**: Cross-chain bridges (e.g., from Ethereum to BSC) wrap ERC-20 tokens as BEP-20 equivalents, allowing tokens to move between blockchains.

A new token that adheres to BEP-20 gains this entire ecosystem immediately, with no special integration required from each protocol. This dramatically lowers the barrier to token adoption.

## Creating a BEP-20 Token

A developer creates a BEP-20 token by writing a [smart contract](/smart-contract/) in Solidity that inherits from or implements the BEP-20 interface. The simplest approach is to use OpenZeppelin's audited ERC20 contract (which works identically for BNB Smart Chain):

```solidity
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }
}
```

The developer then compiles the contract (using Solidity compiler), deploys it to BNB Smart Chain via a transaction (paying gas in BNB), and the token is live. The contract address becomes the token's identity; users and applications refer to it by that address.

## Gas Costs and Economics

A BEP-20 token transfer typically costs 25,000–65,000 gas on BNB Smart Chain. With a gas price of 1 gwei (gigawei), that is roughly 0.000025–0.000065 BNB, or a fraction of a cent USD (BNB trading in double digits). This is 50–100× cheaper than equivalent Ethereum ERC-20 transfers, making BNB Smart Chain attractive for high-volume retail use and gaming tokens.

However, the lower cost also attracts spam tokens and rug-pull schemes. BNB Smart Chain has seen thousands of low-quality or fraudulent tokens. Wallets and users must be cautious about which tokens they interact with.

## See also

<div class="wiki-seealso">

### Closely related

- ERC-20 Token Standard — the Ethereum equivalent; identical specification
- [Smart Contract](/smart-contract/) — programs that define and enforce token behavior on-chain
- Solidity Programming — the language used to write BEP-20 tokens
- [Proof of Stake](/proof-of-stake/) — BNB Smart Chain's consensus mechanism
- [Decentralized Exchange](/decentralized-exchange/) — where BEP-20 tokens trade

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — distributed ledger and consensus
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — centralized trading venues for tokens
- [Distributed Ledger](/distributed-ledger/) — the underlying technology
- [BNB Chain](/bnb-chain/) — the ecosystem and BNB token governance

</div>

---
title: "Atomic Swap"
description: "A peer-to-peer exchange of cryptocurrencies across different blockchains without intermediaries, using cryptographic commitment locks to ensure trustless settlement."
keywords:
  - atomic swap
  - cross-chain trade
  - cryptocurrency exchange
  - trustless settlement
---

*An **atomic swap** is a trustless, peer-to-peer exchange of cryptocurrencies across different blockchains—for example, trading Bitcoin for Litecoin or Ethereum without using a centralized exchange. Both parties lock funds using cryptographic commitments ([hash time-locked contracts](/wiki/atomic-swap/), HTLCs), ensuring that either both transactions complete or both revert, eliminating counterparty risk.*

<aside class="wiki-infobox">

| Key Fact | Value |
|---|---|
| **Mechanism** | Hash time-locked contracts (HTLCs) |
| **Blockchains** | Bitcoin, Litecoin, Ethereum, and many others |
| **Counterparty Risk** | Zero—settlement is atomic |
| **Privacy** | High (no exchange account required) |
| **Speed** | Minutes to hours (block confirmation times) |
| **Cost** | Network fees for two on-chain transactions |
| **Availability** | Decentralized exchanges, experimental DEXes |
| **Adoption** | Growing but still niche |

</aside>

## How atomic swaps work

Atomic swaps use **Hash Time-Locked Contracts (HTLCs)** to enforce simultaneous settlement:

**Step 1: Setup**
- Alice wants to trade 1 Bitcoin (on Bitcoin blockchain) for 20 Ethereum (on Ethereum blockchain) from Bob.
- Alice generates a random secret (hash preimage).
- Alice hashes it: `hash = SHA256(secret)`.

**Step 2: Locking Funds (Bitcoin Side)**
- Alice creates a Bitcoin transaction: "Lock 1 BTC in a contract that releases to Bob if he provides the secret by [Block X]. Otherwise, the BTC returns to Alice."
- Bob can claim the Bitcoin only by revealing the secret.

**Step 3: Locking Funds (Ethereum Side)**
- Bob creates an Ethereum smart contract: "Lock 20 ETH in a contract that releases to Alice if she provides the secret by [Block Y]. Otherwise, the ETH returns to Bob."
- The secret is the same hash Alice used—Bob must provide it to claim the ETH.

**Step 4: Revelation and Settlement**
- Bob sees Alice's Bitcoin transaction locked, knows the secret will let him claim it.
- Bob locks his 20 ETH and reveals the secret to claim Alice's Bitcoin.
- Alice sees Bob revealed the secret on the Bitcoin chain.
- Alice uses that secret to claim Bob's 20 ETH on the Ethereum chain.
- **Result:** Both transactions are atomic—both complete or both fail.

## Why atomic swaps eliminate counterparty risk

Traditional cryptocurrency exchanges (Coinbase, Binance) hold users' funds, creating [counterparty risk](/wiki/counterparty-risk/). The exchange could:
- Get hacked and lose user funds.
- Freeze accounts arbitrarily.
- Face [liquidation](/wiki/liquidation/) (e.g., FTX collapse).

Atomic swaps remove the middleman. Neither Alice nor Bob trusts the other; they trust the blockchain. The smart contract enforces the exchange atomically—no human intervention, no custodian, no single point of failure.

## Time locks and the safety window

The time lock (Block X and Block Y) is critical. If Bob claims the Bitcoin using the secret but then Alice refuses to use it to claim the ETH:

- Bob has Alice's Bitcoin and the secret.
- Alice still has her ETH and could manually release the funds to Bob using the secret.
- But what if Alice delays or goes offline?

The time lock ensures Alice's Bitcoin returns to her automatically if Bob doesn't use the secret within the window. This forces Alice to act—she knows that if Bob got the Bitcoin, he'll rush to claim her ETH before the lock expires. She has ample time to complete her side.

## Challenges and limitations

### Block Confirmation Times
Bitcoin blocks take ~10 minutes on average; Ethereum ~13 seconds. An atomic swap to Bitcoin might take 30–60 minutes to confirm, during which time the market price moves. This makes atomic swaps poor for rapid trades.

### Chain Interoperability
Both blockchains must support HTLCs or equivalent mechanisms. Bitcoin and Litecoin do (they support the same HTLC script). Ethereum supports them via smart contracts. But some blockchains (Cardano, earlier versions) do not natively support HTLCs, making swaps difficult or impossible.

### Liquidity and Matching
Alice needs to find Bob willing to trade at her desired price and quantity. Centralized exchanges solve this via order books and market makers. Atomic swaps require peer-to-peer matching, which is less efficient. The market for peer-to-peer atomic swaps is thin.

### User Experience
Creating HTLCs and managing secrets manually is non-trivial. Most users employ UI tools (e.g., Chainflip, Thorchain) that abstract away the complexity but reintroduce some counterparty risk.

## Atomic swaps vs. stablecoins and wrapped tokens

Atomic swaps serve the same function—cross-chain value exchange—as:

- **Stablecoins** (USDC, USDT): Issued on multiple blockchains; transfers between chains via [bridge protocols](/wiki/bridge-protocols/).
- **Wrapped tokens** (Wrapped Bitcoin, WETH): A Bitcoin-backed token on Ethereum; trades like an ERC-20 token, then can be unwrapped back to native Bitcoin via a custodian.

Atomic swaps differ:
- No trusted intermediary (no issuer, no custodian).
- No protocol risk (rely on blockchain security, not smart contract bugs).
- But: slower, less liquid, more complex for users.

## Adoption and future directions

Atomic swaps remain niche. Why?

1. **Poor user experience:** Most users prefer centralized exchanges for simplicity.
2. **Regulatory arbitrage:** Exchanges provide compliance (KYC, AML) that atomic swaps avoid—a bug or feature, depending on context.
3. **Liquidity fragmentation:** Peer-to-peer markets are fragmented; centralized exchanges offer consolidated order books.

However, growth areas:

- **Privacy swaps:** Monero and other privacy coins are exploring atomic swaps to avoid exchanges that delist privacy tokens.
- **Decentralized finance (DeFi):** Some [decentralized exchanges](/wiki/decentralized-exchange/) use atomic swap principles to settle cross-chain trades.
- **Layer 2 scaling:** As [sidechains](/wiki/sidechain-bridge/) and [rollups](/wiki/zero-knowledge-rollup/) proliferate, atomic swaps across scaling layers may become common.

## Practical example: Swapping Bitcoin for Monero

A trader wanting to swap Bitcoin for Monero without using an exchange could:

1. Initiate an atomic swap proposal on Atomic Swap marketplaces (e.g., XMR/BTC atomic swaps are active).
2. Find a peer (often an MM or liquidity provider).
3. Execute the HTLC exchange.
4. Both parties end up with their desired cryptocurrencies.

This avoids any exchange, but it's slower and requires more technical understanding than clicking "Trade" on Binance.

<div class="wiki-seealso">

### Closely related
- [Hash Time-Locked Contracts](/wiki/atomic-swap/) — The cryptographic mechanism
- [Decentralized Exchange](/wiki/decentralized-exchange/) — Alternative trading venues for cross-chain swaps
- [Bridge Protocols](/wiki/bridge-protocols/) — Alternative cross-chain communication
- [Smart Contracts](/wiki/atomic-swap/) — The code that enforces swaps

### Wider context
- [Cryptocurrency Exchange](/wiki/cryptocurrency-exchange/) — Centralized trading alternatives
- [Blockchain Fundamentals](/wiki/blockchain-fundamentals/) — How blockchains enable swaps
- [Trustless Settlement](/wiki/crypto-settlement-finality/) — The core principle enabling atomic swaps

</div>

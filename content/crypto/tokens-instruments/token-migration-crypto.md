---
title: "Token Migration in Crypto"
description: "Token migration (swap) explained: what happens when a protocol moves to a new blockchain, deadlines for swapping old tokens, and what occurs if you miss the deadline."
keywords:
  - token migration crypto
  - token migration what happens
  - crypto token swap migration
  - token swap deadline crypto
  - what is token migration
---

*A **token migration** (or "token swap") occurs when a blockchain protocol transitions a token from one blockchain or contract to another—typically when the project launches its own blockchain or upgrades its underlying infrastructure. Holders are given a deadline to exchange old tokens for new ones, either automatically or through a swap contract. Tokens not migrated by the deadline become worthless or locked. Historical examples include Cosmos (ATOM), dYdX (DYDX), and many smaller projects. Understanding the mechanics and your rights during a migration is critical, because timing errors or missed instructions can result in permanent loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Token Migration — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A one-time exchange of old tokens for new ones when a protocol upgrades or relocates to a new blockchain.</div>

|   |   |
|---|---|
| **Trigger** | New blockchain launch, major upgrade, or contract redeployment |
| **Deadline** | Usually 1–2 years; varies by project |
| **Swap mechanism** | Manual swap contract, automatic airdrop, or exchange-assisted swap |
| **Old token fate** | Becomes worthless or non-transferable after deadline |
| **Risk if missed** | Permanent loss of access to new token; old token becomes non-tradeable |
| **Custody** | Matters: self-custody requires manual action; exchange-held tokens swap automatically |
| **Tax event** | May be taxable as a [capital gain](/long-term-capital-gain-tax/) or [1099](/tax-bracket-investor/) event at fair market value |
| **Historical examples** | Cosmos (ATOM), dYdX (DYDX), Chainlink (LINK) on some chains |

</aside>

## Why Migrations Happen

A token migration occurs for several reasons:

- **Mainnet launch**: The project was initially built on Ethereum as an ERC-20 token, but now has its own blockchain (Mainnet). The Ethereum token becomes obsolete; holders must migrate to the native coin on Mainnet.
- **Technical upgrade**: The project discovered a flaw or inefficiency in the original token contract and deployed a new, improved version. The old contract is abandoned.
- **Blockchain migration**: A token on one chain (say Ethereum) is moved to a different chain (Polygon) for lower fees or faster transactions. Holders must swap from one chain to another.
- **Consolidation**: Multiple token contracts are unified into a single, canonical one.
- **Governance change**: The old contract was controlled by a centralized entity; the new one is fully decentralized via on-chain governance.

In most cases, the migration is announced months in advance, with a clear deadline and instructions. However, the bar for clarity varies wildly. Some projects publish detailed how-to guides on multiple channels; others issue a single blog post and expect everyone to know what to do.

## The Swap Mechanism: How Migrations Actually Work

Token migrations typically use one of three mechanisms:

**Manual swap via smart contract:**
The project deploys a "migration contract" on the blockchain. Holders initiate a transaction, sending their old tokens to the contract. The contract checks that the tokens are valid, then mints new tokens and sends them to the sender's address. This requires active participation—you must find the contract, approve it to spend your tokens, and call the swap function.

**Automatic airdrop:**
The project takes a snapshot of all old token holders at a specific block height. Then, automatically and without action required, new tokens are airdropped to every address that held old tokens. This is the smoothest experience but is rarer, because airdropping to thousands of addresses can be gas-intensive and logistically complex.

**Exchange-mediated swap:**
If you hold the token on a centralized exchange (Coinbase, Kraken, etc.), the exchange handles the migration for you. You do not need to do anything—the exchange swaps your tokens automatically and updates your balance. This is why exchange-listed tokens experience fewer migration disasters: the exchange does the work.

## Deadlines and Penalties

Migrations usually have two dates:

- **Swap deadline**: The last day you can exchange old tokens for new ones. After this date, the migration contract stops accepting old tokens.
- **Burn or lock deadline**: The old token contract is disabled. After this, the old token cannot be transferred or spent.

The gap between these dates is often 12–24 months. Projects build in generous timelines because the goal is to get everyone across before the old chain/contract is shut down.

However, generous deadlines do not always prevent disasters. Many token holders:

- Forget about the migration entirely and assume the old token is still valid.
- Leave tokens on exchanges that shut down or lose them in security breaches before the deadline.
- Store tokens on hardware wallets and lose the backup seed, making them unable to approve the swap.
- Miss announcements due to poor communication from the project.

In nearly all cases, tokens not swapped by the deadline become permanently worthless. The project does not offer an extension, does not swap them retroactively, and does not compensate holders. The burden is entirely on the individual.

## What Happens to Unmigrated Tokens

Once the deadline passes, an old token typically becomes:

- **Non-tradeable**: Exchanges delist it; peer-to-peer trades are possible but worthless—no one wants a token with no redemption path.
- **Non-transferable**: The project may disable the token contract entirely, making it impossible to send even to yourself.
- **Held by locked addresses**: If the tokens were in a smart contract, a vault, or an exchange that shut down, they are stuck there permanently.

In rare cases, projects offer a grace period or allow holders to swap many years later. But this is not standard and should not be assumed. The rule is: miss the deadline, lose the tokens.

## Historical Examples

**Cosmos (ATOM)**: When Cosmos launched its mainnet in 2019, holders of Cosmos (ATOM) tokens on Ethereum had to swap them for native ATOM coins on the Cosmos blockchain. The deadline was about 1 year. This was a major migration affecting thousands of holders.

**dYdX (DYDX)**: dYdX moved its token from Ethereum to its own blockchain (dYdX Chain). Holders had a deadline to swap their Ethereum-based DYDX for the native DYDX coin. Some centralized exchanges handled this automatically; others did not, and some users missed the deadline.

**Ethereum classic (ETC)**: When Ethereum split into Ethereum and Ethereum Classic in 2016, holders were not technically asked to "migrate"—instead, the old chain continued as ETC, and the new fork became ETH. However, holders had to choose which token to support and often had to move their holdings across exchanges to settle in the new ecosystem.

Smaller projects have fared worse. Countless low-cap tokens have issued migrations with poor communication, leading to widespread loss. The less reputable the project, the higher the likelihood that the migration deadline is disregarded by most holders.

## Custody Matters Greatly

Your custody method determines whether a migration is painless or risky:

**Exchange-held tokens**: If your tokens sit on Coinbase, Kraken, or another major exchange, the exchange typically handles the migration automatically. You wake up with new tokens in your account. Zero risk if the exchange is solvent and reputable.

**Self-custody (hardware wallet, metamask)**: You must actively participate in the swap. You need to understand how to approve a smart contract, call a swap function, and pay gas fees. If you make a mistake—send tokens to the wrong address, use the wrong contract, or miss the deadline—you lose everything. The risk is entirely on you.

**Decentralized finance (DeFi) contracts**: If your tokens are locked in a yield-farming contract, a liquidity pool, or a staking vault, you must first withdraw them from that contract before you can migrate. If the contract is broken or abandoned, you may be unable to access your tokens in time. This has happened to holders caught in scams or failed projects.

**Offline/lost access**: If you stored your tokens on a wallet and lost the private key or recovery seed, a migration is a non-starter. You cannot participate, and your tokens are lost forever.

## Tax Implications

Depending on your jurisdiction, a token migration may trigger a [taxable event](/long-term-capital-gain-tax/). The IRS and most tax authorities treat a swap of one token for another as a disposal of the old token and an acquisition of the new one.

You owe tax on any gain at the time of the swap:

- **Gain = fair market value of new tokens received − cost basis of old tokens given up**
- **Tax rate = your [marginal tax rate](/marginal-tax-rate-investor/) (ordinary income) or long-term capital gains rate, depending on holding period**

If you bought ATOM at $0.10 and it was worth $10 at the time of the migration, you owe capital gains tax on a $9.90 gain per token. The fact that you did not sell anything is irrelevant in most tax codes.

Some jurisdictions treat token-for-token swaps differently, and a few have issued guidance treating certain migrations as non-taxable (e.g., if the migration is a 1:1 exchange). But in the US and most OECD countries, assume it is taxable.

Keeping records of the exact time and price of every migration is critical for compliance.

## How to Prepare for a Migration

If a migration is announced for a token you hold:

1. **Find official sources**: Locate the migration announcement from the project's official website, Twitter account, or GitHub. Avoid third-party guides; they are often wrong.
2. **Note the deadline**: Write it down. Set a phone reminder 1 month before. Then set another for 1 week before.
3. **Understand your custody**: Are your tokens on an exchange, in a hardware wallet, or in a DeFi contract? Each path requires different action.
4. **If self-custody**: Find the official migration contract address, test the swap with a small amount, then migrate the rest.
5. **If on an exchange**: Check if the exchange will handle the migration automatically. If not, withdraw your tokens and do the swap yourself.
6. **Budget for gas fees**: Swaps cost transaction fees. Estimate this cost and ensure you have enough of the host blockchain's native asset (ether, SOL, etc.) to pay for the swap.
7. **Verify the result**: After swapping, confirm you received the new tokens in your wallet. Do not assume success; check the blockchain.

## See also

<div class="wiki-seealso">

### Closely related

- [Crypto token vs coin: key differences](/crypto-token-vs-coin-difference/) — why coins and tokens differ, and why migrations often happen when tokens become coins
- [Revenue-sharing token](/revenue-sharing-token/) — tokens that distribute protocol fees; these may also migrate
- [Initial public offering](/initial-public-offering/) — how traditional companies raise capital; token launches sometimes parallel IPOs
- [Smart contract](/smart-contract/) — the code that governs token swaps and migrations

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — how different blockchains work, context for cross-chain migrations
- [Decentralized exchange](/decentralized-exchange/) — peer-to-peer trading, sometimes used for over-the-counter swaps during migration windows
- [Tax loss harvesting](/tax-loss-harvesting/) — strategy to offset gains from migrations
- [Long-term capital gain tax](/long-term-capital-gain-tax/) — tax treatment of token swaps

</div>
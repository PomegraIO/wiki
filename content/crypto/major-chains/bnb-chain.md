---
title: "BNB Chain"
description: "Binance's EVM-compatible blockchain achieving high throughput through a delegated proof-of-stake model with a small validator set."
keywords:
  - bnb-chain
  - binance-smart-chain
  - delegated-proof-of-stake
  - evm-compatible
  - smart-contract-blockchain
  - validator-set
image: "/svg/crypto.svg"
---

*[BNB Chain](/bnb-chain/) (formerly Binance Smart Chain) is an [Ethereum](/)-compatible smart-contract network operated by a small set of validators that process transactions and secure the chain through delegated proof-of-stake. By limiting the validator set to around 20 active nodes, BNB Chain achieves transaction throughput 100+ times higher than Ethereum while remaining fundamentally centralised.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">BNB Chain — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain networks and cryptocurrency." />

<div class="wiki-infobox-caption">The dominant centralised-validator chain after Ethereum, built for capital efficiency and transaction speed.</div>

|   |   |
|---|---|
| **Launched** | 2020 (as Binance Smart Chain) |
| **Consensus** | Delegated Proof-of-Stake (DPoS) with ~20 active validators |
| **Transaction finality** | ~5 seconds (vs. Ethereum ~13 seconds) |
| **Block time** | 3 seconds |
| **Smart contracts** | EVM-compatible; runs Solidity, Truffle, Hardhat tooling |
| **Native token** | BNB; used for gas fees and validator staking |
| **TVL and market position** | Second-largest chain ecosystem after Ethereum by total value locked |

</aside>

## The centralisation-speed trade-off

When Ethereum launched, it was the only [smart-contract](/)-capable blockchain. But its [proof-of-work](/)-based security model and global validator network meant blocks took 12+ seconds to finalise and gas fees could exceed $100 per transaction during congestion. By 2020, countless projects were paying hundreds of thousands in fees to deploy simple contracts.

Binance's approach was pragmatic: keep Ethereum's smart-contract language and tooling, but replace global consensus with a small cabal of trusted operators. This is what [delegated proof-of-stake](/delegated-proof-of-stake/) means — token holders vote for a small number of validators to represent them, rather than running validation themselves. With only 20 validators producing blocks, BNB Chain can commit new blocks every 3 seconds and confirm them within 15 seconds. More importantly, a developer pays 1/100th the gas.

This design choice sacrifices decentralisation for speed. The 20 active validators are mostly Binance-affiliated entities or large stakeholders with aligned incentives. There is no meaningful censorship resistance: Binance could persuade or coerce validators to exclude transactions. But for application developers, the trade-off is obvious: build on Ethereum and go bankrupt on gas fees, or build on BNB Chain and reach users affordably.

## EVM compatibility and developer onboarding

BNB Chain is fully Ethereum Virtual Machine (EVM) compatible. This means:

- Contracts written in Solidity compile and run identically on both chains.
- Wallets like MetaMask recognise BNB Chain as a network with the same address format as Ethereum.
- Developers use Hardhat, Truffle, and other Ethereum tooling without modification.
- A project can "fork" or copy an Ethereum contract to BNB Chain by changing a single RPC endpoint.

This compatibility was not inevitable. The early altcoins and other smart-contract chains (EOS, Tezos) created custom virtual machines, requiring developers to learn new languages and tooling. By choosing EVM compatibility, Binance eliminated the developer's learning curve. Any Ethereum developer could have a BNB contract live in minutes. This network effect was decisive: capital flooded in, and BNB Chain became the obvious second-choice chain for new projects.

## Token economics and validator incentives

BNB is the native token of the chain. Every transaction requires a gas fee paid in BNB, which is distributed to validators as block rewards. Validators also accept delegations of BNB from token holders, earning a yield in return for maintaining infrastructure and signing blocks.

This creates a profitable business for large operators. A validator with millions in staked BNB earns tens of thousands of dollars daily in block rewards and gas fees. Smaller holders can delegate to validators in exchange for yield, though delegation typically requires a custodian or staking pool (Lido, Stader) because most users lack the technical sophistication to run validator software.

The tight validator set means BNB Chain is a closed club. New validators do not appear because Binance does not invite them. This is the inverse of Ethereum's [proof-of-stake](/proof-of-stake/) model, where anyone can deposit 32 ETH and become a validator. It is also why BNB Chain is sometimes called "Binance's blockchain" — the chain serves Binance's interests first, the broader ecosystem second.

## Market dominance in retail DeFi

BNB Chain exploded in 2021–2022 as the destination for yield farming, meme tokens, and high-leverage trading. PancakeSwap, the leading decentralised exchange on BNB Chain, rivalled Uniswap in trading volume at the peak. Protocols like Venus and Alpaca Finance offered yields that would have been impossible on Ethereum given the gas costs.

By 2023–2024, BNB Chain had settled into its ecological role: it hosts retail-focused DeFi, low-capital NFT trading, and emerging-market use cases (where users cannot afford $100 transaction fees). Ethereum retained the premium, institutional-grade infrastructure; Arbitrum and Optimism (Ethereum's scaling layers) captured much of the high-volume trading. BNB Chain became the choice of price-sensitive users and projects that could not raise capital on Ethereum's ecosystem.

## The bridge problem and cross-chain security

Most assets on BNB Chain are wrapped versions of Ethereum tokens. A user bridge USDC from Ethereum to BNB Chain by locking it on Ethereum and receiving a wrapped version (USDC.e or similar) on BNB Chain. These bridges — including Binance's own cross-chain router and third-party bridges like Stargate — are centralised operations that custodise the locked funds. If the bridge operator is hacked or misconfigures its smart contract, bridges can lose millions (as happened repeatedly in 2023).

This created a structural weakness: BNB Chain can never be more secure than the bridges that connect it to Ethereum. A developer building on BNB Chain is, in effect, trusting both BNB's validator set and Binance's bridge infrastructure.

## Regulatory status and Binance dependency

BNB Chain is wholly dependent on Binance's continued operation and willingness to maintain the validator set. This is not true of Ethereum or Cosmos, which were designed to survive the withdrawal of any single operator. It is also unclear whether BNB Chain's validators would continue operating if Binance faced regulatory action or went bankrupt.

Several national regulators have scrutinised BNB Chain as an extension of Binance's business, not a truly autonomous network. This distinction matters because Binance has faced enforcement actions in multiple jurisdictions, including the USA. A developer deploying to BNB Chain faces the risk that the chain itself becomes subject to seizure or shutdown, though this is unlikely in practice because Binance's token, BNB, trades on dozens of exchanges and the validator set is internationally distributed.

## See also

<div class="wiki-seealso">

### Closely related

- Ethereum Virtual Machine — the compatibility standard BNB Chain implements
- [Delegated proof-of-stake](/delegated-proof-of-stake/) — the consensus mechanism enabling BNB Chain's high throughput
- Binance — the exchange operator that created and maintains the chain
- [Proof-of-stake](/proof-of-stake/) — the broader consensus category of which DPoS is a variant
- Solidity — the smart-contract language used on BNB Chain

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — core concepts underlying smart-contract networks
- Decentralised exchange — trading protocols that run on BNB Chain
- [Smart contracts](/smart-contract/) — programmable logic that BNB Chain executes
- [Ethereum](/ethereum/) — the parent architecture and primary competitor

</div>

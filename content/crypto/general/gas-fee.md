---
title: "Gas Fee"
description: "How Ethereum prices computation to allocate block space and deter spam through a fee mechanism."
keywords:
  - gas fee
  - ethereum transaction cost
  - block space pricing
  - transaction fee market
  - computational cost
  - ethereum network
image: "/svg/crypto.svg"
---

*A **gas fee** is a transaction cost on blockchain networks—particularly Ethereum—that charges users based on the computational work required to execute their transaction. By pricing block space, gas fees allocate scarce validation resources, prevent spam, and allow the network to operate without central gatekeepers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gas Fee — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and blockchain topics." />

<div class="wiki-infobox-caption">Ethereum's fee mechanism ties cost to computational complexity rather than transaction size.</div>

|   |   |
|---|---|
| **What it is** | A per-operation cost, measured in gas units, that users pay to execute transactions on a blockchain |
| **Measured in** | Gwei (billionths of a [cryptocurrency](/bitcoin/) unit) or wei (smallest unit) |
| **Paid to** | Validators and the protocol (burn mechanism varies by chain) |
| **Varies by** | Network congestion, operation complexity, and prioritization preference |
| **Primary function** | Allocate limited block space and deter malicious or frivolous activity |

</aside>

## The economics of computational scarcity

Every transaction on Ethereum requires computational work: validating signatures, updating account balances, executing smart contract code. Block space is finite—a validator can process only so much computation per block. Rather than ration access by lottery or central authority, Ethereum introduced a price mechanism: users bid for the right to have their transaction included and executed.

This mirrors any market for a scarce resource. Just as concert tickets command higher prices when demand is high and capacity is fixed, Ethereum transactions cost more when the network is congested. During peak trading or NFT mint events, gas fees spike because many users are competing for the same limited block space. During quiet periods, fees fall.

The cost varies not just by congestion but by *type* of operation. A simple transfer of funds between two accounts might cost 21,000 gas units; a complex smart contract interaction could cost ten times more, reflecting the greater computational burden. This granular pricing encourages developers to write efficient code and discourages wasteful operations.

## How gas is calculated and paid

Users specify a gas limit—the maximum amount of gas they're willing to consume—and a gas price (in gwei). Miners or validators order transactions by price and fill each block with the highest-paying ones first until capacity is reached.

When a transaction executes:
- If it completes without error, the user pays (actual gas used) × (gas price).
- If it fails partway through, the user still pays for gas consumed up to the failure point—a design that prevents attackers from running expensive computations "for free."
- Any unused gas is refunded.

From 2015 to mid-2021, this first-price auction meant all users paid the same gas price (the market rate). Ethereum's London hard fork in August 2021 introduced **EIP-1559**, which split the gas price into a base fee (burned by the protocol) and a miner tip (paid to validators). This mechanism reduced gas price volatility and made fee prediction more reliable, though it did not eliminate congestion pricing itself.

## Spam prevention and resource fairness

Without gas fees, an attacker could flood the network with millions of trivial transactions, consuming block space and slowing the network for honest users—a denial-of-service attack. Gas fees create a material cost per operation, making such attacks expensive and economically irrational for most attackers.

Gas fees also align incentives: users who value their transaction more (willing to pay higher fees) get priority; those with less urgent needs can wait for cheaper periods or use [layer-2-scaling](/layer-2-scaling/) solutions.

The mechanism is not perfect. During extreme congestion, even ordinary users face prohibitive costs. Very small transactions may cost more in fees than their value warrants. This has driven migration to [layer-2-scaling](/layer-2-scaling/) systems, which bundle many off-chain transactions into a single on-chain settlement, dramatically reducing per-transaction costs.

## Gas versus network utility

A common misconception is that high gas fees represent a broken network. In fact, high fees typically signal high demand—more people find Ethereum valuable enough to pay for. Conversely, a network with perpetually low fees may simply lack utility. The fee market is doing its job: pricing the use of scarce resources.

That said, gas fees are a legitimate barrier to retail adoption and to small transactions. Alternatives such as [layer-2-scaling](/layer-2-scaling/) solutions and competing blockchains with lower fee structures have emerged precisely to address this tradeoff.

Different blockchains take different approaches. Some (Solana, newer Ethereum-compatible chains) prioritize speed and low fees at the cost of decentralization. Others (Bitcoin, original Ethereum) accept higher fees as a byproduct of security and decentralization. Neither is categorically "better"—the choice reflects different values.

## Gas fees and protocol incentives

Gas revenue funds the validators who maintain the network. Higher fees mean validators earn more, which can attract more hardware and security resources. When Ethereum transitioned to [proof-of-stake](/proof-of-stake/), transaction fees became the primary ongoing revenue for validators, replacing block rewards (subsidies). This shift tightened the link between network utility and validator profitability.

The long-term sustainability of Ethereum hinges partly on fee revenue staying adequate. If adoption stalls or users migrate to [layer-2-scaling](/layer-2-scaling/) solutions, base layer fee revenue shrinks, potentially reducing validator security incentives. Protocol designers must balance low fees (which encourage use) against sustainable validator returns (which ensure security).

## See also

<div class="wiki-seealso">

### Closely related

- [Layer 2 Scaling](/layer-2-scaling/) — off-chain execution systems that bundle transactions to reduce per-transaction gas costs
- [Proof of Stake](/proof-of-stake/) — Ethereum's validator mechanism, for which gas revenue provides ongoing income
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the ledger and consensus architecture underlying gas mechanics
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — venues where transaction volumes spike, driving gas fees higher

### Wider context

- [Bitcoin](/bitcoin/) — uses a different fee model, not a gas mechanism, reflecting its simpler transaction model
- [Ethereum](/ethereum/) — the primary network where gas fees originated and remain most complex
- [Distributed Ledger](/distributed-ledger/) — the broader concept of decentralized transaction settlement

</div>

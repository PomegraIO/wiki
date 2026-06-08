---
title: "Smart Contract"
description: "Self-executing code deployed on a blockchain that automatically enforces agreement terms without intermediaries or manual intervention."
keywords:
  - smart contract
  - blockchain
  - automated execution
  - decentralized
  - ethereum
  - code enforcement
image: "/svg/crypto.svg"
---

*A **smart contract** is a piece of code written and deployed on a [blockchain](/blockchain-fundamentals/) that automatically executes predefined actions when specified conditions are met. Unlike traditional contracts enforced by courts or intermediaries, smart contracts are enforced by the underlying network's consensus mechanism—the code itself *is* the law.*

<div class="wiki-hatnote">

For legal frameworks and real-world applications, see [cryptocurrency-exchange](/cryptocurrency-exchange/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Smart Contract — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain and cryptocurrency topics." />

<div class="wiki-infobox-caption">Agreement and enforcement merged into code.</div>

|   |   |
|---|---|
| **What it is** | Executable code on a distributed ledger that triggers actions when conditions are met |
| **Also called** | Automated contract; blockchain-based agreement; decentralized application logic |
| **Key platform** | [Ethereum](/ethereum/); also Solidity, Vyper, Rust-based chains |
| **Key feature** | Immutable once deployed; execution is deterministic and verifiable |
| **Trade-off** | No human discretion; code bugs or edge cases cannot be patched without consent |
| **Related concepts** | [Blockchain fundamentals](/blockchain-fundamentals/), [Ethereum](/ethereum/), [Distributed ledger](/distributed-ledger/) |

</aside>

## How a smart contract works

A traditional contract is a written agreement. Two parties sign it, and a court or arbitrator enforces it if one party breaches. A smart contract skips the middleman.

Instead of prose, the terms are written in code. If the code is deployed to [Ethereum](/ethereum/) (or another smart-contract-enabled blockchain), the network's nodes will *automatically* execute the code's instructions the moment the specified conditions are true.

A simple example: a payment contract. Traditional version—you lend money, sign a note, and sue if the borrower doesn't repay. Smart contract version—you transfer crypto to a contract address with a rule: *"Release the funds to the borrower's address on January 1, 2027, and if not repaid by January 1, 2028, transfer the collateral to the lender's address."* No judge needed. When January 1, 2028 arrives, the network automatically executes the instruction.

The blockchain's consensus mechanism—proof-of-work or [proof-of-stake](/proof-of-stake/)—ensures that once the code is deployed, it cannot be altered, and its execution cannot be censored or reversed. The code is the arbiter, not a person.

## Why smart contracts exist

Smart contracts solve a specific problem: *trust without intermediaries*. In the traditional financial system, you trust a bank, broker, or clearinghouse to hold your money and execute trades on your behalf. That intermediary takes a cut, can be hacked, and may collude with the other party against you.

A smart contract is written in plain code that anyone can read. You don't trust a person; you trust the code, the blockchain's security (its [hash rate](/hash-rate/) and [consensus mechanism](/proof-of-work/)), and the economic incentives that prevent network participants from attacking it.

This is why smart contracts are foundational to [decentralized finance (DeFi)](/distributed-ledger/). An automated lending protocol, token swap, or derivatives market can operate 24/7 without employees, without a CEO, without a licence from a regulator (though regulators are now paying attention). The code enforces the rules for everyone equally.

## Key platforms and languages

[Ethereum](/ethereum/) is the primary smart-contract platform. Contracts are written in Solidity, a language designed to resemble JavaScript. When you deploy a contract to Ethereum, it lives at a specific address. Calling that address with certain inputs triggers the code.

Other platforms exist. Solana, Cardano, and Polkadot each have smart-contract environments. Solidity is Ethereum-specific; Cardano uses Plutus; Solana uses Rust. The conceptual idea is the same: code on a blockchain, executed deterministically, enforced by consensus.

## The immutability problem

Once deployed, a smart contract *cannot be modified* by the creator. This is a feature and a bug.

It's a feature because it guarantees that the code the users saw *before* they sent their funds is the code that will execute. No secret backdoor can be added later.

It's a bug because *code has bugs*. The famous DAO hack of 2016 exploited a flaw in a smart contract that held millions in Ethereum. The creator couldn't patch it; the only solution was a controversial "hard fork" of the Ethereum network itself, which some in the community rejected as a betrayal of immutability.

Later, the Solidity team introduced design patterns like the "upgrade proxy," which allows a smart contract to call a *different* version of code. But this reintroduces trust: you're trusting that the upgrade proxy's administrator won't change the underlying code in a malicious way.

## Use cases: from trivial to complex

The simplest smart contracts are escrow agreements. Alice wants to sell a digital asset to Bob, but neither trusts the other. They deploy a contract: *"Hold Bob's payment in escrow; if Alice proves she delivered the asset (by calling this function), release the payment to Alice."*

More complex: automated market makers (AMMs). A contract pool holds two tokens and allows users to swap between them. The contract enforces pricing rules, collects fees, and distributes them to [liquidity providers](/liquidity-risk/) who funded the pool. Uniswap, the largest DEX, is a smart contract.

Even more complex: collateralized debt positions (CDPs). A user locks crypto as collateral and borrows stablecoins against it. The contract monitors the collateral price, allows borrowing and repayment, and automatically liquidates the collateral if its value falls below a threshold. Maker DAO runs on smart contracts.

## Limitations and real-world friction

Despite the promise, smart contracts are not frictionless.

*Oracle problem*: A smart contract running on the blockchain can only see data that's *on* the blockchain. If your contract needs to know the price of Bitcoin or whether a real-world event occurred (e.g., a plane landed), you need an external data source called an "oracle." Oracles are centralized or semi-centralized, reintroducing trust and failure points.

*Finite state machine*: A smart contract can only execute code that was written in advance. It has no agency or judgment. If unexpected circumstances arise—an edge case, a disaster, a legal change—the code cannot adapt.

*Regulatory ambiguity*: A contract written in code may or may not be legally enforceable depending on jurisdiction. If the contract's terms conflict with law, which wins? Courts are still deciding.

*Composability risk*: Smart contracts often call other smart contracts. If the underlying contract changes or is hacked, your contract is affected, even if your code is correct. Cascading failures are common in DeFi.

## See also

<div class="wiki-seealso">

### Closely related

- [Ethereum](/ethereum/) — primary platform for smart contracts
- [Blockchain fundamentals](/blockchain-fundamentals/) — underlying technology
- [Distributed ledger](/distributed-ledger/) — the ledger that hosts smart contracts
- [Proof of work](/proof-of-work/) — consensus mechanism that secures smart-contract execution
- [Proof of stake](/proof-of-stake/) — alternative consensus mechanism

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — platforms where smart-contract-based tokens trade
- [Bitcoin](/bitcoin/) — lacks native smart contracts; Ethereum was built to support them
- [Decentralized finance](/distributed-ledger/) — primary use case for smart contracts
- [Hash rate](/hash-rate/) — computational power that secures the blockchain

</div>

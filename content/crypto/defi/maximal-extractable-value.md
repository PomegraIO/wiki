---
title: "Maximal Extractable Value"
description: "The profit validators and searchers capture by reordering, inserting, or censoring transactions within a blockchain block."
keywords:
  - MEV
  - transaction ordering
  - front-running
  - sandwich attack
  - validator profit
  - block building
image: "/svg/crypto.svg"
---

*[Maximal Extractable Value](/maximal-extractable-value/), or MEV, is the excess profit a validator or block builder earns by strategically reordering, inserting, or excluding transactions within a block. Originally understood as "Miner Extractable Value" under [Proof of Work](/proof-of-work/), it has evolved into a broader phenomenon affecting every blockchain where transaction ordering matters—which is almost all of them.*

## The mechanics of transaction ordering

On a blockchain, transactions enter a mempool (a waiting room) before being bundled into blocks. In Bitcoin, miners select transactions; in [Ethereum](/ethereum/) after the 2022 Merge, validators do. Whoever controls block building also controls the order in which transactions execute.

This ordering power is profitable when two conditions align: a profitable trade opportunity is visible in the mempool, and no single transaction can capture it alone. A classic example: a large swap on Uniswap that will move the price of an asset. A searcher or validator who sees this swap before it hits the block can frontrun it—include their own swap first to move the price favourably, then execute the original swap at a worse rate, capturing the difference.

The original swap's user still completes the trade, but at a degraded price. They pay the cost of MEV invisibly, as slippage. The validator captures the gain.

## Where MEV comes from

MEV opportunities emerge wherever [smart contracts](/smart-contract/) perform complex calculations and transaction order affects the outcome. In DeFi, the sources are numerous.

**Liquidation cascades**: When a borrower's collateral falls below a threshold on a lending protocol, anyone can liquidate them—seizing their collateral and selling it. The first person to submit a liquidation transaction in a block wins the liquidation reward. Searchers watch for near-liquidations and prepare transactions. Validators can insert their own liquidations ahead of searchers' transactions.

**Automated market makers (AMMs)**: Protocols like Uniswap execute swaps using a mathematical formula. A large swap within a block moves the price; any transaction placed after it trades at that worse price. A searcher inserting a swap before a large public swap (frontrun), then selling after it (backrun), captures the price movement.

**Auctions and settlement**: When an auction ends on-chain, the validator decides which bids arrive before the deadline and which arrive after. A validator could theoretically exclude a competing bid to help their preferred bidder win.

**MEV is *maximal***: The term "maximal" is telling. We count the largest extractable profit in any single block, not the average. During periods of high congestion and volatile markets, individual MEV events can be worth millions of dollars.

## The shift from miners to validators

Under Proof of Work, miners performed the work to produce blocks and earned transaction fees and block rewards. They could also extract MEV, but they had to do it themselves—solo miners had full visibility and control. Large mining pools delegated work to mining nodes but maintained some MEV awareness.

The transition to [Proof of Stake](/proof-of-stake/) fractured this arrangement. A validator chosen to propose a block doesn't necessarily build it themselves. Specialised block builders—companies and individuals running sophisticated [MEV](/maximal-extractable-value/) search algorithms—prepare blocks and sell them to validators. Validators earn a base reward for proposing blocks but outsource the MEV extraction.

This created a market: Flashbots, a research collective, began running an "MEV Relay" that gathered blocks from builders and auctioned them to validators. Validators bid on blocks, paying the builder for the MEV-rich blocks while keeping the base reward and tips. The flow of MEV shifted from direct validator extraction to a centralised relay system.

## The social cost

MEV itself is not illegal or fraudulent—it follows the rules. But it imposes a cost on users.

When you submit a transaction to swap tokens on an AMM, you set a slippage tolerance (usually 1–3%), accepting up to that price movement. But if a searcher sandwiches your transaction—inserting a swap before yours and another after—your actual price movement can far exceed your tolerance. Your transaction goes through, but you paid invisible MEV tax.

In lending protocols, MEV creates a "liquidation tax": borrowers forced into liquidation often lose more than the protocol's intended penalty, because liquidators and validators extract additional MEV from their collateral sales.

On aggregate, studies estimate that users pay billions annually in MEV—a hidden tax on decentralized finance. This runs counter to DeFi's foundational promise: transparent, censorship-resistant finance. The promise holds (transactions are censorship-resistant), but the pricing is worse than users expect.

## Attempts to reduce MEV harm

Because MEV is mathematically inevitable wherever transaction ordering matters, the focus has shifted to containing it.

**Private mempools and encrypted transactions**: Some protocols allow users to submit transactions in encrypted form, visible only to builders. The Threshold Encryption approach tries to hide transaction content until it's been ordered, eliminating frontrunning opportunities. But encrypted mempools centralize on a small number of providers and introduce their own trust assumptions.

**MEV-resistant consensus**: Some newer blockchains (Solana's MEV-resistant features, for instance) attempt to randomize or obscure block production, making it harder for validators to reorder transactions profitably. The tradeoff is slightly reduced throughput or finality.

**Application-level protections**: DeFi protocols can build in protections. Batch auctions, where all transactions in a block execute at the same price, eliminate MEV from that operation. Intent-based architectures, where users express what they want rather than how to get it, allow solvers to find the optimal path without exposing ordering to MEV.

**MEV redistribution**: Rather than eliminate MEV, some systems try to redirect it toward validators or the protocol itself. [MEV Auction](/miner-extractable-value-auction/) systems let validators claim more of the MEV that searchers generate, creating at least a fairer distribution of gains.

## MEV and protocol governance

Importantly, MEV is not purely a technical problem—it's also a [governance](/defi-governance/) problem. Protocols must decide how much MEV leakage is acceptable and what constraints to place on block builders.

Ethereum's roadmap includes Proposer-Builder Separation (PBS) and more recent proposals for encrypted mempools. These represent fundamental choices about centralization (isolated builders) versus opacity (encrypted transactions)—neither ideal.

Some argue MEV is the inevitable rent on transaction ordering in any system where users don't see each other's intent. Others contend that MEV represents pure waste—value extracted without adding utility—and should be minimized aggressively, even at the cost of speed or decentralization.

Most protocols have settled on a pragmatic middle ground: acknowledge MEV as a real phenomenon, build systems to contain it where possible, and let markets find equilibrium. Users who want MEV protection can use encrypted mempools or batch auctions, accepting slightly higher fees or latency. Others accept MEV as a cost of low-friction, high-speed trading.

## See also

<div class="wiki-seealso">

### Closely related

- [MEV Auction](/miner-extractable-value-auction/) — markets such as Flashbots that sell the right to build blocks and capture MEV
- [DeFi Governance](/defi-governance/) — protocols use governance to set rules constraining MEV extraction
- [Proof of Stake](/proof-of-stake/) — the consensus mechanism enabling separated block proposal and building
- [Smart Contract](/smart-contract/) — the code that makes reordering profitable
- [DeFi Oracle](/defi-oracle/) — price feeds can themselves be vulnerable to MEV manipulation

### Wider context

- [Ethereum](/ethereum/) — the primary blockchain where MEV research and tools were developed
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the underlying transaction ordering logic
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — market infrastructure where MEV concepts originated
- [Market Maker Trading](/market-maker-trading/) — the traditional finance analogue to MEV extraction

</div>

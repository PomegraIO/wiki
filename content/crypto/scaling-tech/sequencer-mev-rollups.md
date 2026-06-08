---
title: "Sequencer MEV in Rollups"
description: "How rollup sequencers extract maximal extractable value and what mechanisms aim to prevent it or redistribute it fairly."
keywords:
  - sequencer mev in rollups
  - maximal extractable value sequencer
  - rollup centralization mev
  - mev prevention mechanisms
  - fair ordering services
---

*A **sequencer** in a rollup is responsible for ordering transactions, batching them, and posting them on chain. Because it controls transaction order, the sequencer can extract maximal extractable value (MEV)—profiting from reordering transactions to front-run trades, sandwich attacks, or liquidations. This centralization of MEV in one entity is a core concern in rollup design.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sequencer MEV in Rollups — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Centralized sequencers can capture all MEV in the rollup.</div>

|   |   |
|---|---|
| **What it is** | Profit a sequencer earns by reordering or manipulating the inclusion of transactions in a batch |
| **Typical forms** | Front-running swaps, sandwich attacks on DEX trades, liquidation ordering, stealing arbitrage |
| **Who benefits** | The sequencer operator; users see worse execution prices and higher slippage |
| **Why it happens** | Sequencer has monopoly over transaction ordering in the rollup |
| **Mitigation approaches** | Decentralized sequencing, private mempools, encrypted transactions, MEV auctions, fair-ordering protocols |
| **Current state** | Most rollups are centralized sequencers; mitigation is in early / experimental stages |

</aside>

## How Sequencer Ordering Creates MEV

In a rollup, users submit transactions to a mempool. A sequencer (a single node or small set of nodes) chooses which transactions to include, in what order, and when. Unlike a public blockchain where any participant can participate in consensus, most rollups today rely on a **centralized sequencer** operated by the rollup company.

This sequencer has complete visibility into the mempool and can see pending transactions before they're ordered. When it sees a large swap transaction that will move a price, the sequencer can insert its own transaction before it (front-running), execute the swap first at a better price, and sell at a profit after the user's transaction moves the market.

The user's transaction still executes, but at worse terms: higher slippage, worse price. The sequencer pockets the difference.

This is MEV—the value the sequencer extracts by reordering or manipulating transactions. In Ethereum, MEV is distributed among miners, validators, and MEV searchers who bid for block space. In a centralized rollup, the sequencer captures it all unilaterally.

## Forms of Sequencer MEV

**Front-running**: Sequencer sees a swap, inserts its own swap first, and profits from the resulting price movement.

**Sandwich attacks**: Sequencer places a user's transaction between two of its own transactions—one that buys before the user's trade, one that sells after—extracting the profit from price movement.

**Liquidation ordering**: In a lending protocol, when a user's collateral falls below a threshold, anyone can liquidate their position and earn a liquidation fee. A sequencer can delay liquidations to maximize the fee or front-run them to capture the fee itself.

**Arbitrage stealing**: If a user initiates a cross-rollup or cross-DEX arbitrage, the sequencer can see it and execute the same arbitrage first, capturing the profit before the user's transaction clears.

**Censorship**: The sequencer can delay or exclude transactions entirely, censoring users or manipulating market conditions.

All these forms of MEV reduce user experience and create moral hazard: users can't trust fair execution if a single entity controls ordering.

## Why Centralized Sequencers Exist

Early rollups adopted centralized sequencers for simplicity and speed. Decentralizing sequencing requires solving consensus among multiple sequencers—a hard problem. A single, trusted sequencer was faster to deploy and allowed the rollup team to ensure liveness (transactions always get included within a predictable time).

Over time, sequencer centralization became a dependency risk. If the sequencer goes down, the rollup halts. If the sequencer is malicious, users face extraction and censorship. But replacing it required either:

- Building a decentralized sequencer protocol, which is complex and introduces latency.
- Moving to a shared sequencer (like Ethereum's), which introduces dependencies and may require new trust assumptions.

Most rollups today remain centralized, though they have published commitments to decentralize in the future.

## Mitigation Strategies

### Private Mempools and Encrypted Transactions

If transactions are encrypted until they're sequenced, the sequencer cannot see pending transactions and cannot reorder them to extract MEV. Protocols like Shutter Network and Threshold Encryption hide transaction content until a threshold of parties decrypt it.

The trade-off is added complexity and latency. Decryption requires coordination among multiple parties, and encryption adds computational overhead.

### MEV Auctions (Proposer-Builder Separation)

Rather than letting the sequencer take all MEV, some rollups use MEV auctions. The sequencer becomes a "proposer" that decides the canonical order, and competitive "builders" submit bids for the right to fill in the transactions. The highest bidder's transactions are included, and fees are shared between sequencer and rollup.

This doesn't eliminate MEV but redistributes it. Builders still extract it; some revenue flows back to the rollup or users.

### Fair-Ordering Services and Sequencer Committees

**Encrypted mempools** (also called threshold encryption or timelock puzzles) allow transactions to be ordered fairly without the sequencer knowing their content until commitment time.

**Sequencer committees** distribute sequencing across multiple independent nodes. No single node controls transaction order; instead, a consensus mechanism (e.g., Practical Byzantine Fault Tolerance) determines the ordering. This is slower than a centralized sequencer but more robust. Arbitrum's Anytrust uses this approach with a small committee.

### Intent-Based Architectures

Newer designs like Uniswap's MEV-prevention proposals and protocols like MEV-Burn attempt to separate transaction ordering from execution. Users express intents (goals, like "swap 100 USDC for USDT at the best available price") rather than hardcoding transaction parameters. A solver network competes to fulfill intents optimally, and the sequencer cannot reorder to extract MEV because it never sees the raw transaction content.

This is still experimental and requires a significant shift in how users interact with applications.

## The Economic Reality of Sequencer MEV

Empirically, sequencer MEV in rollups is substantial. Studies of Arbitrum, Optimism, and Polygon (an Ethereum sidechain with similar sequencing dynamics) show that sequencers extract millions of dollars per month through front-running and reordering.

For small users, MEV per transaction is often negligible—a few cents. For large traders, swaps, and liquidations, MEV can be thousands or millions of dollars per transaction.

This creates a perverse incentive: the sequencer has every reason to maximize MEV extraction, even if it harms users. Users cannot opt out; they must use the rollup if they want its benefits.

## Toward Decentralized Sequencing

The Ethereum roadmap includes a future state where rollups use a shared, decentralized sequencer—potentially Ethereum itself via sharding, or a separate protocol like Cosmos or a sequencer network. Arbitrum, Optimism, and others have publicly committed to decentralizing sequencing, though timelines are uncertain.

Decentralized sequencing would spread MEV among many participants and make front-running difficult or impossible. The drawback is latency and complexity. Including a transaction in a rollup using Ethereum consensus might take 12 seconds instead of 2 seconds.

Until rollups are decentralized, users should expect sequencer MEV to be a feature—not a bug—of centralized rollup design. This is a key reason many users prefer layer-2 scaling solutions with more mature MEV infrastructure (like Ethereum's own Lido validator network, which distributes MEV proposing rewards).

## See also

<div class="wiki-seealso">

### Closely related

- Maximal Extractable Value (MEV) — general concept of value extracted through transaction reordering
- Front-Running — specific MEV technique of inserting a transaction before another's
- Sandwich Attack — form of MEV where an attacker surrounds a victim's transaction
- [Optimistic Rollup](/optimistic-rollup/) — rollup design that includes sequencer choice and risks
- ZK Rollup — alternative rollup design that also relies on centralized sequencers today
- [Arbitrum](/arbitrum/) — rollup with sequencer committee design to mitigate MEV

### Wider context

- Ethereum Layer 2 — category of solutions building on Ethereum
- Decentralized Sequencing — emerging designs for removing sequencer centralization
- Proposer-Builder Separation — technique to mitigate MEV by separating roles

</div>

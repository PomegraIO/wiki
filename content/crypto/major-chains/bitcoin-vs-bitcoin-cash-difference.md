---
title: "Bitcoin vs Bitcoin Cash: Key Differences"
description: "Understand the difference between Bitcoin and Bitcoin Cash: block size, fees, forking history, and divergent use cases."
keywords:
  - difference between bitcoin and bitcoin cash
  - bitcoin vs bitcoin cash
  - bitcoin cash block size
  - bitcoin hard fork
  - cryptocurrency fork
image: /svg/crypto.svg
---

*The difference between **Bitcoin and Bitcoin Cash** stems from a 2017 hard fork over block size and fee policy: Bitcoin Cash increased the maximum block size from 1 MB to 8 MB (later 32 MB), aiming to lower fees and increase transaction throughput, while Bitcoin kept the 1 MB limit and developed Layer 2 scaling solutions instead. This philosophical split shaped two distinct networks with different use cases, communities, and price trajectories.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bitcoin vs Bitcoin Cash — Key Differences</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A fundamental disagreement about scaling strategy created two separate blockchains.</div>

|   |   |
|---|---|
| **Block size limit** | Bitcoin: 1 MB; Bitcoin Cash: 32 MB |
| **Fork date** | August 1, 2017 |
| **Average transaction fee (typical)** | Bitcoin: $1–$100+ (variable); Bitcoin Cash: <$0.01 |
| **Transaction speed (base layer)** | Both ~10 minutes per block |
| **Scaling approach** | Bitcoin: Layer 2 rollups; Bitcoin Cash: on-chain |
| **Market capitalization** | Bitcoin: ~10–20x larger |
| **Ticker symbol** | BTC (Bitcoin); BCH (Bitcoin Cash) |

</aside>

## The 2017 Fork: Why It Happened

By 2016, Bitcoin's 1 MB block size limit was creating a genuine problem. The network could only process roughly 7 transactions per second. As adoption grew, transactions began competing for limited block space, driving up fees. During peaks, sending a Bitcoin payment could cost $10 or more, and users had to wait days if they didn't pay a premium.

Two competing visions emerged. One camp—backed by much of Bitcoin's core development community—argued that raising the block size was a dead end. More data per block meant higher storage and bandwidth requirements, which would make running a full node expensive and push the network toward centralization. Their solution: keep Bitcoin itself lean and minimal, and build "Layer 2" solutions (like the Lightning Network) on top to handle payments.

The other camp—including major miners and some early Bitcoin developers—saw the block size limit as an artificial constraint. They argued that hardware was improving fast enough to handle larger blocks; keeping the limit was crippling Bitcoin's usefulness as digital cash. Their solution: increase the block size and let Bitcoin scale directly on-chain.

After years of contentious debate, the two sides could not reach consensus. In August 2017, a group of Bitcoin Cash proponents implemented a hard fork (a change so fundamental that non-upgraded nodes cannot follow the new chain), increasing the block size to 8 MB. Bitcoin Cash was born. Those who held Bitcoin before the fork suddenly held both BTC (Bitcoin) and BCH (Bitcoin Cash) in equal amounts.

## Block Size and Fee Economics

Bitcoin's 1 MB block limit means roughly 3,000–4,000 transactions fit in each block, processed every ~10 minutes. In quiet periods, this capacity is more than enough, and fees drop to cents. During network congestion—when everyone is transacting—fees can spike to dollars or tens of dollars per transaction. The fee market is real: users bidding for limited block space.

Bitcoin Cash's 8 MB block size (and later 32 MB upgrade path) holds far more transactions per block. On most days, Bitcoin Cash blocks are not full, so fees are negligible (a fraction of a cent). Users paying lower fees enjoy a genuine advantage for simple payments. But Bitcoin Cash's block size increase also has a cost: each block takes more storage and bandwidth to process and relay. Running a full Bitcoin Cash node requires more disk and faster internet than Bitcoin.

For the average user, Bitcoin's $1–$50 fee per transaction (depending on network load) is acceptable for larger transfers and savings but painful for everyday payments. Bitcoin Cash's sub-cent fees make it viable for small purchases—a coffee, a tip, a small transfer—without fees eroding the amount sent.

## Transaction Speed and Scalability Philosophy

Both Bitcoin and Bitcoin Cash produce blocks every ~10 minutes on average. This is a deliberate constraint designed into the protocol for security and decentralization, not a technical limitation. Neither network is slow because of block time; they're slow because blocks fill up and new ones arrive at intervals.

Bitcoin's approach to scaling beyond 1 MB is Layer 2 networks. The [Lightning Network](/lightning-network/), for example, allows two parties to open a channel, transact off-chain as many times as they wish, and settle the final balance on-chain later. This way, millions of payments can occur in the time it takes Bitcoin to process one on-chain transaction. Layer 2 solutions move complexity off the blockchain while preserving Bitcoin's security guarantees.

Bitcoin Cash's approach is to increase block size directly. The reasoning is straightforward: if the bottleneck is block space, add more space. This makes Bitcoin Cash feel lighter and faster for simple payments but does not address the trade-off between throughput and the cost of running a full node.

## Adoption and Market Position

Bitcoin remains the dominant cryptocurrency by far: market capitalization, trading volume, institutional adoption, and mindshare. Bitcoin's brand is strong; most people saying "crypto" or "Bitcoin" are referring to BTC specifically.

Bitcoin Cash has a much smaller but dedicated ecosystem. It has merchants, exchanges, and even some retail use in countries with unreliable fiat currencies or high remittance costs (where low transaction fees matter more). However, Bitcoin Cash never achieved mainstream payment adoption. Its actual utility as a payment system remains niche compared to BTC's store-of-value narrative and BTC's ecosystem of financial products.

## Use Cases Today

**Bitcoin (BTC)** is primarily used as a store of value and a hedge against inflation or currency debasement. Its high fees make it economical for large transfers and long-term holding. Institutional investors, governments, and inflation-conscious savers use Bitcoin. For everyday payments, most Bitcoiners route transactions through Lightning Network or centralized exchanges rather than on-chain.

**Bitcoin Cash (BCH)** markets itself as "peer-to-peer electronic cash"—a direct payment system. It suits remittances in countries with weak banking infrastructure, tips and donations, and small retail purchases where fees must be minimal. Bitcoin Cash communities in Africa, Southeast Asia, and some Latin American countries use BCH for this purpose.

## Mining and Network Security

Both Bitcoin and Bitcoin Cash use [Proof of Work](/proof-of-work/) with SHA-256 hashing, the same fundamental algorithm. Initially, the same miners could mine both coins by choosing which pool to send their work to. Over time, they've developed somewhat different mining ecosystems. Bitcoin, as the more valuable chain, attracts the majority of hash power and mining investment. Bitcoin Cash has seen hash power fluctuate as miners weigh profitability.

Both networks remain secure via proof of work. Bitcoin's network is far larger; attacking Bitcoin requires more computational power than attacking Bitcoin Cash. This is a real security difference: Bitcoin Cash's smaller mining base means lower absolute cost to a hypothetical attacker, though the threshold is still astronomically high.

## The Philosophical Divide

The split between Bitcoin and Bitcoin Cash reflects a deeper disagreement about what blockchain technology is for. Bitcoin's philosophy emphasizes security, decentralization, and immutability—even at the cost of throughput and fees. Bitcoin Cash's philosophy prioritizes practical utility as a medium of exchange—even if it requires larger blocks and somewhat higher node-running costs.

Neither approach is objectively wrong. Bitcoin's Layer 2 scaling keeps the base layer lean and lets users choose their speed/cost trade-off. Bitcoin Cash's on-chain scaling makes the base layer more usable for payments but concentrates on-chain activity. The market has chosen Bitcoin as the more valuable and trusted asset, but Bitcoin Cash remains a functional alternative with genuine use cases.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Work](/proof-of-work/) — consensus mechanism used by both Bitcoin and Bitcoin Cash
- [Lightning Network](/lightning-network/) — Layer 2 payment channel for Bitcoin
- Block — fundamental unit of blockchain data
- [Ethereum vs Solana Transaction Speed](/ethereum-vs-solana-transaction-speed/) — another throughput vs. decentralization comparison
- Hard Fork — the mechanism that created Bitcoin Cash

### Wider context

- Cryptocurrency — digital assets and blockchain overview
- [Bitcoin](/bitcoin/) — Bitcoin network fundamentals
- [Blockchain Fundamentals](/blockchain-fundamentals/) — consensus, decentralization, and scalability concepts
- [Distributed Ledger](/distributed-ledger/) — distributed network technology

</div>

---
title: "MEV Auction"
description: "Block-building markets where validators sell the right to order transactions, channeling MEV revenue to protocol participants."
keywords:
  - MEV market
  - block auction
  - Flashbots
  - block builder
  - validator revenue
  - MEV relay
image: "/svg/crypto.svg"
---

*An [MEV Auction](/miner-extractable-value-auction/) is a market structure in which block builders—entities that assemble transactions into blocks—compete to sell those blocks to validators. The winning builder claims the [Maximal Extractable Value](/maximal-extractable-value/) (MEV) available in the block, paying validators for the right to order transactions. This system emerged on Ethereum after the 2022 transition to [Proof of Stake](/proof-of-stake/), reshaping how validators earn revenue.*

## Why auctions became necessary

Before Proof of Stake, Ethereum miners built blocks themselves. A miner saw the mempool, identified profitable reordering opportunities, and kept the MEV. Revenue was simple: block reward plus transaction fees plus MEV extracted.

After Proof of Stake, validators no longer do the computational work to produce blocks—they just propose them. A validator randomly selected to propose a block has seconds to decide which transactions to include. For most validators, building a competitive block with careful transaction ordering is impractical. They lack the infrastructure, data connections, and algorithms to do sophisticated MEV extraction.

This created a vacuum. Specialized entities—companies and teams running expensive hardware and mathematical models—began building blocks and approaching validators with an offer: "Use our block; we'll pay you a premium." This was the birth of the MEV market.

## How MEV auctions work

The canonical MEV auction system is **Flashbots Relay**, launched in 2021 and formally integrated into Ethereum's validator ecosystem in 2023.

Block builders submit candidate blocks to the relay. Each block contains an ordered sequence of transactions and a bid—the amount the builder will pay the validator for the right to use that block. The relay selects the block with the highest bid (or some variant of the highest bid) and forwards it to the validator. The validator signs and broadcasts the block, receiving the builder's payment in addition to the base reward and transaction tips.

The builder profits if the MEV captured in the block exceeds the payment made to the validator. For example, if a builder constructs a block containing a large swap that they can sandwich, and the sandwich profit is $500,000, they might pay the validator $250,000 and keep $250,000 for themselves. The validator earns more than they would have by building a block independently; the builder captures the MEV that would have otherwise been lost or extracted less efficiently.

This auction mechanism has become the norm. In 2024, the majority of Ethereum blocks are built through Flashbots Relay or similar auction-based systems.

## Who are the block builders?

Early MEV extraction was dominated by specialist teams and research entities. Flashbots itself began as a research organization, publishing papers on MEV before building commercial tools. Companies like Lido, a major stake pooling service, eventually launched their own builders.

Over time, builders consolidated. A block-building operation requires:
- Fast connections to mempools and other builders
- Access to high-quality transaction data
- Sophisticated algorithms for transaction reordering
- Relationships with major validators and relays

These barriers to entry mean the builder market is concentrated. In 2024, a small number of builders (Flashbots MEV-Boost, Lido's LVR Builder, and a handful of others) construct the majority of Ethereum blocks.

This concentration has raised concerns about centralization. If a small number of builders control block content, they wield enormous influence. A builder could, in theory, censor transactions they dislike, favour certain users, or refuse to build blocks that harm their commercial interests.

## Validator incentives and competition

From a validator's perspective, MEV auctions create a straightforward economic decision: accept a builder's bid or build a block independently. In almost all cases, the builder's bid is higher than any MEV the validator could extract alone. A solo validator accepting $10,000 from a builder earns more than the $2,000 they might capture by trying to extract MEV themselves.

This creates a prisoner's dilemma at scale. Individually, validators are better off accepting builder bids. But collectively, if all validators outsource to a small set of builders, the protocol loses decentralization and the validators lose direct control over transaction ordering.

Some validators resist this pressure. Solo stakers sometimes build blocks directly, rejecting builder bids. Staking pools, which aggregate capital from many small holders, typically outsource to builders, since the economics favour it and most participants lack MEV expertise.

## Concerns: Centralization and transparency

The most serious criticism of MEV auctions is that they concentrate power. When Flashbots Relay processes 90%+ of Ethereum blocks (a level sometimes reached), a single relay operator has extraordinary influence.

Several risks emerge. First, **censorship**: if Flashbots or a builder dislikes certain transactions, they can simply exclude them. In 2023, concerns about sanctions and OFAC compliance led some builders to voluntarily exclude transactions from sanctioned addresses. This happened without formal governance or validator consent—builders simply did it.

Second, **information asymmetry**: builders see all pending transactions before ordering them. They can therefore extract MEV more efficiently than anyone else. While this efficiency is not inherently wrong, it means builders have privileged information and profit from it.

Third, **auction instability**: if a large validator or validator pool is unhappy with a builder's practices, they can't easily switch. The builder market is concentrated enough that alternatives may be limited or require negotiation.

## Alternative designs

To reduce centralization, several alternatives have been proposed.

**Encrypted mempools** would hide transaction content from builders until they're included in a block, preventing frontrunning. But encryption adds latency and requires new infrastructure (threshold cryptography or trusted hardware).

**Threshold encryption (TEC)** lets users encrypt their transactions such that only a threshold of validators together can decrypt and order them. This eliminates individual validator or builder power over ordering.

**Intent-based architectures** are gaining traction. Instead of submitting transactions, users submit "intents"—descriptions of what they want to happen. Solvers compete to fulfil those intents optimally. This separates intent from execution and allows protocols to control ordering, not builders.

**Proposer-builder separation (PBS)** with enhanced transparency is another direction. Rather than a single relay, PBS could operate through multiple competing relays, and validators could select from multiple builders more easily.

## Revenue implications

MEV auctions have substantially increased validator revenue. In Ethereum, block rewards are modest (currently a few ETH per block), but MEV bids often exceed that. For a validator, the effective yield from MEV can be 5–20% annually, depending on market conditions and builder competition.

This has had subtle effects. Higher validator revenue makes staking more attractive, increasing the total amount staked and therefore the protocol's security. But it also concentrates wealth—validators who outsource to builders pocket the validator tips, while the builders capture the MEV. For most users, this is invisible; they just experience worse prices (the MEV cost embedded in transaction execution).

## Future evolution

The trend is toward more sophisticated mechanisms. Some builders now implement "PBS-lite" systems where they commit to certain transaction orderings before seeing all transactions. Others experiment with "encrypted blocks," where transactions remain encrypted until finality.

Ethereum's long-term roadmap includes Proposer-Builder Separation (PBS) as a protocol-level feature, formalizing the relationship between proposers (validators) and builders. This could improve transparency and reduce the power of relays.

Competition among builders is also increasing. As the MEV market matures, more operators (protocols, exchanges, hedge funds) are launching builders, hoping to capture a share of MEV. This competition could eventually reduce builder margins and increase the payments to validators.

Whether MEV auctions represent a permanent feature of proof-of-stake blockchains or a transitional phase remains open. For now, they are the dominant mechanism, restructuring how validators earn revenue and who controls transaction ordering.

## See also

<div class="wiki-seealso">

### Closely related

- [Maximal Extractable Value](/maximal-extractable-value/) — the underlying profit being auctioned
- [DeFi Governance](/defi-governance/) — protocols use governance to regulate builder behaviour
- [Proof of Stake](/proof-of-stake/) — the consensus mechanism that enabled separated block building
- [Smart Contract](/smart-contract/) — the infrastructure where most MEV opportunities originate
- [DeFi Oracle](/defi-oracle/) — price feeds can be manipulated or informed by MEV data

### Wider context

- [Ethereum](/ethereum/) — the blockchain where MEV auctions are most developed
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the technical structure enabling auction systems
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — traditional market infrastructure analogues
- [Market Maker Trading](/market-maker-trading/) — the traditional finance basis for MEV concepts

</div>

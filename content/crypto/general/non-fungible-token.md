---
title: "Non-Fungible Token"
description: "Unique on-chain ownership records that distinguish digital assets from interchangeable coins and tokens."
keywords:
  - NFT
  - non-fungible token
  - digital ownership
  - blockchain token
  - unique asset
  - cryptocurrency
image: "/svg/crypto.svg"
---

*A **non-fungible token (NFT)** is a unit of data on a blockchain that represents something unique and irreplaceable. Unlike [bitcoin](/bitcoin/) or other [cryptocurrencies](/cryptocurrency-exchange/), which are fungible (one unit is identical to another), each NFT has distinct properties and provenance. NFTs establish on-chain ownership of digital and physical assets without requiring a central intermediary.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Non-Fungible Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and blockchain topics." />

<div class="wiki-infobox-caption">NFTs prove ownership and uniqueness on-chain, without requiring a central issuer or custodian.</div>

|   |   |
|---|---|
| **What it is** | A blockchain token representing a unique, irreplaceable item or asset |
| **Key property** | Non-interchangeable; each token has distinct metadata and history |
| **Issued on** | Ethereum (via ERC-721 standard), Bitcoin, Solana, and other blockchains |
| **Recorded** | On a distributed ledger, with ownership transferred by transaction |
| **Ownership proof** | Cryptographic signature; the blockchain serves as a public registry |
| **Use cases** | Digital art, collectibles, in-game items, domain names, real-world asset registration |

</aside>

## Fungibility versus uniqueness

Fungible goods are interchangeable: one dollar bill is equivalent to another; one unit of a [mutual fund](/mutual-fund/) is equivalent to another. Fungible assets are ideal for currency and financial instruments because users care only about quantity, not identity.

Non-fungible goods are unique: a Picasso painting is not interchangeable with another painting; a specific piece of land is not interchangeable with another parcel. For unique goods, ownership history and provenance matter. A painting's value depends partly on its documented history.

For centuries, proving unique ownership required centralised registries. A government maintains a land registry; a museum maintains provenance documentation for an artwork; a corporation maintains records of which person owns which seat at a stadium event. These registries are slow, expensive, and require trust in the institution.

A blockchain is a decentralised, permanently immutable registry. When an NFT is created and assigned to a wallet, the transaction is recorded. When the NFT is transferred, the new owner's wallet address is recorded. Anyone can query the blockchain to verify who currently owns a specific NFT and trace its full ownership history. The proof is cryptographic, not bureaucratic.

## Technical standards and minting

The most common standard for NFTs on Ethereum is **ERC-721**, introduced in 2017. Each ERC-721 token has a unique integer ID; metadata (name, image URL, attributes) is stored separately, either on-chain or off-chain. A wallet can hold multiple ERC-721 tokens; ownership is proven by the wallet's private key.

A newer standard, **ERC-1155**, allows a single contract to issue both fungible and non-fungible tokens, useful for games or mixed collections.

Creating an NFT is called "minting." A creator deploys a smart contract, specifies metadata, and mints tokens. The creator often retains a royalty right—each time the NFT is resold, the creator receives a percentage. This is encoded in the contract and settled automatically.

## Use cases and speculation

NFTs exploded in popularity around 2021, initially for digital art and collectibles. Artists could sell digital works directly to collectors, with the blockchain proving authenticity and ownership. Unlike a jpg file, which can be copied freely, an NFT is a scarce, uniquely owned record.

Beyond art, NFTs have been used for:
- **In-game items**: weapons, skins, and other game assets that a player truly owns (not rented from a game publisher)
- **Domain names**: ENS (Ethereum Name Service) allows users to register human-readable names (.eth) as NFTs
- **Event tickets**: concert and sports tickets as NFTs, resaleable on secondary markets
- **Deeds and titles**: companies exploring NFT-based registration for real-world property

The NFT market has been volatile. Hype drove prices to unsustainable levels; many projects collapsed. Rug pulls (where creators abandon a project after raising funds) and fraud were common. However, the underlying technology—using a blockchain to prove unique ownership—is sound, and niche use cases (game items, domain names) have shown genuine utility.

## Custody and bridging with physical assets

A critical distinction: an NFT proves ownership of a digital asset *on-chain*. For a digital image or virtual item, this is straightforward. But for a physical asset (a painting, a house, a diamond), the NFT is only a claim. Someone must bridge the physical and digital worlds.

If you own an NFT representing a painting, you still need a trusted custodian (a museum, a vault service) to actually hold and insure the physical work. The NFT proves your claim, but custody is a separate contract. Similarly, an NFT representing a house is only as good as the government's land registry; the blockchain is a parallel record, not a replacement.

This gap has slowed adoption for high-value real-world assets. NFTs work best for purely digital goods (where the blockchain is the only registry) or for communities where the NFT itself is the entire asset (like a profile picture).

## Scalability and environmental concerns

Early NFT minting was expensive, often costing $50–500 per transaction due to [gas fees](/gas-fee/). High fees made the format impractical for low-value items and discouraged experimental use. [Layer 2 scaling](/layer-2-scaling/) solutions have dramatically reduced costs, enabling NFT ecosystems on Arbitrum, Optimism, and other systems.

Environmental concerns were raised about NFT energy use, particularly on proof-of-work blockchains. Ethereum's transition to [proof-of-stake](/proof-of-stake/) in 2022 reduced its energy consumption by ~99%, mitigating the issue for Ethereum-based NFTs. Newer blockchains like Solana use far less energy per transaction than proof-of-work.

## The broader implication

The deeper significance of NFTs is not speculative art markets but the principle: a blockchain can serve as a public, immutable registry of unique ownership without a central authority. This applies to digital art, in-game items, domain names, and potentially to real-world assets. The technology is durable even if current hype cycles fade.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — the ledger and smart contract infrastructure enabling NFTs
- [Distributed Ledger](/distributed-ledger/) — the decentralised registry concept that NFTs embody
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — markets where NFTs are bought and sold
- [Gas Fee](/gas-fee/) — the cost of minting and transferring NFTs on Ethereum

### Wider context

- [Bitcoin](/bitcoin/) — predates NFTs but inspired the concept of decentralised ownership
- [Ethereum](/ethereum/) — the primary platform for NFT creation and trade
- [Proof of Stake](/proof-of-stake/) — reduced the environmental cost of blockchains hosting NFTs
- [Layer 2 Scaling](/layer-2-scaling/) — makes NFT transactions cheap enough for mass adoption
- [Distributed Ledger](/distributed-ledger/) — the broader architecture of decentralised asset ownership

</div>

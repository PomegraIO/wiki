---
title: "Semi-Fungible Token"
description: "ERC-1155 tokens that are mutually exchangeable within a class but retain unique identity across different classes."
keywords:
  - semi-fungible token
  - ERC-1155
  - hybrid token
  - multi-class fungibility
  - batch tokens
image: "/svg/crypto.svg"
---

*A semi-fungible token (SFT) is a token that behaves as fungible within one category but as non-fungible across different categories. The ERC-1155 standard on Ethereum exemplifies this: 1,000 tickets to a concert are interchangeable with each other, but a concert ticket is distinct from a parking pass or a merchandise voucher, even though all three live on the same contract.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Semi-Fungible Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for hybrid token standards." />

<div class="wiki-infobox-caption">Fungible in class, unique across classes.</div>

|   |   |
|---|---|
| **What it is** | Token standard (e.g., ERC-1155) supporting multiple token classes within a single contract; each class is fungible internally, non-fungible externally |
| **Also called** | Batch tokens, hybrid tokens, multi-token standard |
| **Key innovation** | Merges fungible (ERC-20) and non-fungible (ERC-721) logic into one contract |
| **Primary use** | Gaming, event ticketing, loyalty programs, metadata-heavy collections |
| **Fungible within** | A specific ID or class (all ID #42 tokens are identical) |
| **Non-fungible across** | Different IDs (token ID #42 differs from token ID #43) |
| **Gas efficiency** | Batch transfers and operations reduce transaction costs versus separate contracts |

</aside>

## The fungibility spectrum

Most blockchain tokens live at one extreme or the other. A [stablecoin](/stablecoin/) like USDC is fully fungible—any unit is identical and interchangeable. A [non-fungible token](/nft/) (like an NFT art piece) is completely unique and non-interchangeable. Semi-fungible tokens occupy the middle ground: they are fungible *in some respects* and non-fungible *in others*.

Consider an event. A concert venue issues 10,000 tickets. All tickets to the main floor are interchangeable—they seat you in the same section, cost the same, and entitle you to the same experience. In that sense, they are fungible. But a ticket to the concert is fundamentally different from a parking pass or a merchandise voucher, both of which might also be issued by the same venue. That is where non-fungibility emerges: across categories.

## The ERC-1155 standard

The ERC-1155 standard, created by Enjin and now widely adopted on Ethereum and other blockchains, codifies semi-fungibility. Instead of deploying separate contracts for concert tickets (ERC-721), parking passes (ERC-20), and merchandise (ERC-721), a venue can issue all three from a single ERC-1155 contract.

Each token type is assigned a unique ID. ID 1 might represent a main-floor ticket; ID 2, a VIP ticket; ID 3, a parking pass; ID 4, a merchandise voucher. Within each ID, tokens are fungible—you can trade your main-floor ticket for someone else's main-floor ticket without loss. Across IDs, tokens are distinct—a main-floor ticket is not a parking pass, even though both come from the same contract.

## Why this matters: efficiency and flexibility

The innovation is not just logical elegance—it is practical efficiency. In ERC-20 and ERC-721, each token type requires its own smart contract. An event operator managing tickets, parking, merchandise, and food vouchers would deploy four separate contracts, each with its own storage, transfer logic, and security audit surface.

With ERC-1155, one contract handles all four. This drastically reduces gas costs for batch operations. If you want to transfer 100 concert tickets and 50 parking passes to 50 different friends, ERC-1155 lets you do it in a single transaction; ERC-20 and ERC-721 would require dozens.

## Use cases where semi-fungibility shines

**Gaming**: A game studio issues swords (ID 1), shields (ID 2), and potions (ID 3) from one contract. All swords are interchangeable with each other (fungible), but a sword is not a shield (non-fungible across types). Players can trade swords freely and sell potions to collectors.

**Event ticketing**: Tickets by section or class are fungible internally; different event dates or venues are non-fungible across classes. A buyer can swap their ticket for another seat in the same section, but swapping for a different event requires a different token type.

**Loyalty programs**: A retailer issues loyalty points (fungible), exclusive perks (semi-fungible by tier), and collectible badges (non-fungible by achievement). All points are the same, but a Gold tier perk is distinct from a Platinum tier perk.

**Digital collectibles**: A trading card platform issues common cards, rare cards, and limited editions from one contract. Commons are fungible; rares are non-fungible across tiers.

**Fractional ownership**: [Fractional NFTs](/fractional-nft/) can use ERC-1155 to represent fractional shards of different underlying assets. All shards of Asset A are fungible; shards of Asset B are distinct.

## Semi-fungible versus [Fractional NFT](/fractional-nft/)

The distinction is architectural. A fractional NFT takes one non-fungible asset, locks it, and mints fungible shards from it. Semi-fungible tokens are a token standard designed to natively support multiple classes of tokens. A fractional NFT is an application of fungible tokens; an ERC-1155 is the underlying standard that may *contain* fractional NFTs alongside other token types.

## Metadata and enrichment

Because ERC-1155 is flexible, each token ID can carry rich metadata—images, descriptions, attributes, and properties. A sword in a game might have a rarity level, a forging date, and special bonuses. This metadata makes each token class recognizable and tradeable. Marketplaces can filter by metadata (show me all legendary swords), and collectors can value tokens based on attributes.

## Interoperability and trading

ERC-1155 tokens trade on decentralized exchanges and marketplaces that support the standard. OpenSea, for instance, handles both ERC-721 (pure NFTs) and ERC-1155 (semi-fungible) collections. A buyer can swap fungible tokens within a class or across classes using atomic swaps on [decentralized exchanges](/decentralized-exchange/).

## Scalability and the multi-token future

As blockchains support more complex applications—games with 100,000 item types, loyalty programs spanning retailers, cross-platform digital assets—ERC-1155 becomes increasingly valuable. It allows developers to scale without deploying hundreds of contracts.

Layer-2 solutions (like Polygon or Arbitrum) support ERC-1155 natively and inherit its efficiency. This accelerates adoption in high-frequency applications like gaming.

## Limitations and design trade-offs

ERC-1155 is more complex than ERC-20 or ERC-721, which can introduce security risks if the contract is poorly audited. The flexibility to support many token types also means metadata management becomes a responsibility of the issuer—if metadata servers go offline, token attributes may become unreadable.

## The path forward: standardization

ERC-1155 is now a de facto standard, but newer proposals (like ERC-3525 for semi-fungible tokens with variable amounts) suggest the ecosystem will continue evolving. Future standards may support more granular control over fungibility or better interoperability with cross-chain protocols.

## See also

<div class="wiki-seealso">

### Closely related

- [Fractional NFT](/fractional-nft/) — fungible shards of a single non-fungible asset
- [Real-World Asset Tokenization](/real-world-asset-tokenization/) — tokenizing off-chain assets into fungible or semi-fungible classes
- [NFT](/nft/) — fully non-fungible tokens representing unique ownership
- [Smart Contract](/smart-contract/) — code that defines token behavior and metadata
- [Decentralized Exchange](/decentralized-exchange/) — platforms for trading semi-fungible tokens across classes

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — how blockchains execute token standards
- [Ethereum](/ethereum/) — primary blockchain supporting ERC-1155
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — centralized markets for SFT trading
- [Distributed Ledger](/distributed-ledger/) — underlying technology storing token balances and metadata

</div>

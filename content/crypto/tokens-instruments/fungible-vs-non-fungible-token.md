---
title: "Fungible vs Non-Fungible Token"
description: "Fungible tokens like ETH are interchangeable and divisible; NFTs are unique digital assets tied to ownership. Learn when each instrument is appropriate and why the distinction matters."
keywords:
  - fungible vs non-fungible token
  - fungible token explained
  - nft vs token difference
  - erc-20 erc-721
image: "/svg/crypto.svg"
---

*A **fungible token** is interchangeable, divisible, and identical to every other token of the same type—like dollar bills or shares of stock. A **non-fungible token** (NFT) is unique, indivisible, and tied to a specific digital asset (art, collectible, deed, identity)—like a painting or deed to land. Fungible tokens are appropriate for currency, utility, and governance; NFTs are appropriate for scarce digital assets where authenticity and ownership matter.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fungible vs Non-Fungible — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two token types serving fundamentally different purposes on a blockchain.</div>

|   |   |
|---|---|
| **Fungible tokens** | Interchangeable, divisible, standard (ERC-20) |
| **Examples** | ETH, USDC, governance tokens, stablecoins |
| **Appropriate for** | Currency, utility, rewards, governance voting |
| **Non-fungible tokens** | Unique, indivisible, non-standard (ERC-721, ERC-1155) |
| **Examples** | Digital art, collectibles, deeds, identity certificates |
| **Appropriate for** | Scarce assets, provenance, ownership records |

</aside>

## Fungibility: the core principle

In economics, a **fungible** asset is one unit that is perfectly equivalent to every other unit of the same type. A dollar bill is fungible—your $1 is identical to my $1, and we can exchange them without loss. A barrel of crude oil is fungible—one barrel is interchangeable with another. An acre of wheat field is not fungible; one acre's location, soil, and drainage differ from another's.

Fungible tokens follow this logic. One unit of Ether (ETH) is identical to every other ETH. One token of a governance coin is identical to another. They are divisible (you can own 0.5 ETH) and interchangeable (I send you 1 ETH, you send me 1 ETH, we are square). When you buy 100 tokens on an exchange, you do not care *which* 100 tokens you receive; all 100 are the same.

Non-fungible tokens do the opposite. An NFT is a unique digital object, often tied to a contract containing metadata: an image hash, a creator identity, a certificate of authenticity. Token #1234 is different from token #1235, and you cannot exchange them 1:1 because they represent different assets. If I own an NFT tied to a digital artwork, you cannot swap me "any NFT" as payment—you must pay in something fungible (like ETH or USD) or offer a specific NFT that I want.

## Blockchain standards for each type

The Ethereum blockchain defines standards (called ERC) for how tokens behave. The two most common are:

**ERC-20** is the standard for fungible tokens. It specifies a contract interface: the token tracks balances, allows transfers, and specifies a total supply. Every ERC-20 token—whether ETH, USDC, Uniswap (UNI), or a new meme coin—follows this template. Wallets, exchanges, and protocols can handle any ERC-20 token the same way, which makes it trivial to add new tokens to an exchange or to build DeFi applications that support any ERC-20.

**ERC-721** is the standard for NFTs. It also tracks ownership and transfers, but each token has a unique identifier and can carry custom metadata. An ERC-721 contract might point to an image hosted on a server or distributed storage, bind the token to a legal document, or record authorship and creation date. Each token is distinct.

Ethereum also supports **ERC-1155**, a "semi-fungible" standard that allows a single contract to manage both fungible and non-fungible tokens. A game might use ERC-1155 to issue 1,000 interchangeable in-game coins (fungible) and also unique player avatars (non-fungible) from the same contract.

## When to use fungible tokens

Fungible tokens work whenever you need:

**Currency or store of value.** You need a medium of exchange. Paying for goods with unique NFTs makes no sense; paying with fungible ETH or a stablecoin does. The vendor receives something they can immediately spend, lend, or exchange.

**Utility within a protocol.** A decentralized exchange might issue a governance token that users stake to earn fees or governance rights. Hundreds of thousands of users hold this token; each token holder is interchangeable in the voting system. You do not care if your specific token unit is "token #500,000 minted by the protocol" versus "token #999,999"—you only care about the count.

**Rewards and incentives.** A blockchain network issues tokens to validators or liquidity providers as rewards. These are fungible—reward payouts are fungible amounts, and recipients merge them into pools of identical tokens.

**Governance voting.** A DAO issues tokens where each holder votes on proposals. Tokens are fungible because each token grants one vote (or proportional voting weight), and the voting mechanism does not distinguish between "token from founder wallet" versus "token from community purchase."

## When to use non-fungible tokens

Non-fungible tokens work whenever you need to establish uniqueness, prove ownership, or create scarcity:

**Digital art and collectibles.** An artist creates an artwork and mints it as an ERC-721. The token's metadata points to the artwork image and includes the creator's signature. A collector buys the token, proving they own the canonical version. The artwork is unique; no two buyers can both own "the original."

**Deeds and property records.** Real-world property (a house, a piece of land, a vehicle) has a unique deed proving ownership. An NFT can encode this deed on-chain. A buyer purchases the NFT, and the blockchain record becomes the authoritative proof of ownership—transparent, transferable, and immutable.

**Identity and credentials.** A university might issue an NFT diploma. The token includes the recipient's name, degree, graduation date, and the university's digital signature. The recipient owns the token and can prove their credential without relying on the university's servers; the credential is portable and cryptographically verified.

**Membership and access.** A private club might issue an NFT membership card. The token grants the holder access to a gated portal or physical venue. Each token is tied to a specific member identity and is non-transferable (or transferable only with the organization's consent).

**Licensing and intellectual property.** A software company might issue NFTs as licenses to use proprietary code or data. Each license is unique, tied to a specific company, and traceable on-chain—protecting both the licensor's ability to prove ownership and the licensee's proof of a legal right to use the asset.

## Fungible tokens dominate by volume and utility

On most blockchains, fungible tokens vastly outnumber non-fungible ones by trading volume and utility. A single fungible token (like USDC, a stablecoin) might trade tens of billions daily. The largest NFT collections trade millions or billions, but still a fraction of major fungible token volume.

This reflects their respective purposes. Fungible tokens are the workhorses of blockchain finance—users need stable, divisible, exchangeable units to conduct commerce and participate in DeFi. NFTs are specialized instruments for specific use cases where uniqueness and provenance matter: art, rare collectibles, identity, and property records.

The conflation of NFTs with "digital art as investment" has obscured their broader utility. Most NFT volume is speculative trading in visual collectibles, but the underlying technology is ideal for any scenario requiring a unique, ownership-bearing record on a public ledger.

## Fungibility and privacy

One underappreciated distinction: fungible tokens can be mixed and obscured; non-fungible tokens cannot. If you own one Ether, I cannot tell which specific Ether you hold—all Ethers are identical on the ledger. This privacy-by-default makes fungible tokens suitable for everyday use. An NFT, by contrast, is traceable forever—the blockchain ledger preserves a complete history of who held the token and when. This transparency is a feature for legal deeds and credentials, but a drawback for privacy-sensitive transactions.

## See also

<div class="wiki-seealso">

### Closely related

- [Fan Token Explained](/fan-token-explained/) — fungible tokens issued by sports properties that grant holders voting rights
- [Token Unlock Schedule](/token-unlock-schedule/) — how fungible tokens are scheduled for release to investors and teams
- [Wrapped Token vs Synthetic Asset in DeFi](/wrapped-token-vs-synthetic-asset/) — fungible tokens that represent other assets or currencies
- [Ethereum](/ethereum/) — the blockchain hosting both ERC-20 and ERC-721 standards

### Wider context

- [Distributed Ledger](/distributed-ledger/) — the foundational technology enabling unique token identification
- [Initial Public Offering](/initial-public-offering/) — the traditional precedent for fungible equity shares
- Cryptocurrency Fundamentals — broader blockchain and token concepts
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator scrutinizing token classification

</div>

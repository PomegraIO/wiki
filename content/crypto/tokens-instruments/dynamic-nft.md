---
title: "Dynamic NFT"
description: "Non-fungible tokens whose metadata or visual appearance changes on-chain based on external data or protocol conditions."
keywords:
  - dynamic nft
  - programmable nft
  - oracle integration
  - on-chain metadata
  - conditional tokens
  - generative nft
image: "/svg/crypto.svg"
---

*A **Dynamic NFT** is a non-fungible token whose metadata, image, or attributes update automatically in response to external data feeds or on-chain conditions. Unlike a static NFT (which displays the same image and traits forever), a Dynamic NFT can evolve — its appearance might change based on price feeds, time passing, user interactions, or data from an external API — creating a token that feels alive rather than fixed in time.*

## Static NFTs and their limitations

The first wave of NFTs — CryptoPunks, Bored Ape Yacht Club, Art Blocks — were static. Once minted, a token's image and metadata never changed. This immutability was part of the appeal: proof of uniqueness and permanence on the blockchain. But it was also limiting. A digital art piece could not respond to the world around it. A gaming item could not gain experience or level up. A financial instrument couldn't update its terms based on market conditions.

A Dynamic NFT removes that constraint. The image and metadata live off-chain (usually on a server or IPFS) and can be refreshed whenever conditions change. The NFT itself — the smart contract — points to a metadata URL. When that URL's content updates, the NFT's appearance updates across all wallets and marketplaces that fetch and display it.

## How the mechanics work

A Dynamic NFT requires a few components:

**A smart contract:** The contract mints the NFT and stores a pointer to where its metadata lives (usually a URL). It can also store simple on-chain data (health points, level, ownership history).

**A metadata server or IPFS gateway:** Hosts the JSON file describing the NFT (name, image URL, attributes, etc.). This server can update the JSON file based on triggers.

**A trigger mechanism:** Usually an oracle or API call. A chainlink oracle might feed real-time Bitcoin prices into the blockchain. A backend server might check a game's status and update an in-game item's stats. A user might click a smart contract function that unlocks new traits or visuals.

**Off-chain computation:** A backend (owned by the NFT creator or a service provider) watches for trigger conditions and updates the metadata URL's content when conditions change.

When a wallet or marketplace displays the NFT, they query the metadata URL. If the underlying data has changed, the displayed image and traits reflect the current state.

## Use cases: where Dynamic NFTs make sense

**Gaming items:** An in-game sword can grow stronger as it's used, showing wear or enhancement visually. A character NFT can gain experience and level up, with new abilities or appearance traits unlocking at milestones.

**Real-world asset tracking:** A tokenized diamond or fine art piece can display authenticity certificates, auction history, or insurance status that updates on-chain.

**Financial instruments:** A debt instrument (bond NFT) can update its maturity date, coupon rate, or current yield as conditions change.

**Time-based collectibles:** An NFT might evolve based on the date — a "seasonal" NFT that looks different in spring, summer, fall, and winter. Or one that changes every day, rewarding holders who check back.

**Generative art:** An artist can create NFTs whose image is generated programmatically from on-chain data (price feeds, block numbers, holder wallet address). Each time the underlying data shifts, the image regenerates.

**Sports or fantasy:** A player card NFT whose stats update weekly based on real-world performance. A fantasy token that changes rarity based on game outcomes.

## The oracle and data problem

A Dynamic NFT's integrity depends entirely on the reliability of its data source. If the NFT's appearance is supposed to track the price of Ethereum, the system needs an oracle (a service that feeds blockchain-verified price data into smart contracts). Chainlink and other oracle networks provide this, but oracles introduce a new dependency and a potential point of failure.

Some Dynamic NFTs rely on centralized APIs — a creator's server fetches data from an exchange and updates the metadata. This is simpler but reintroduces trust: if the server goes down, the NFT's metadata cannot update. If the creator abandons the project, Dynamic NFTs stop updating.

Others rely on on-chain data only — Ethereum block numbers, transaction counts, DeFi protocol states. These are trustless but limited in scope.

## The display problem

A fundamental challenge: most NFT marketplaces and wallets don't know how to handle Dynamic NFTs. OpenSea and other markets cache the image and metadata when an NFT is first listed. If the underlying metadata changes, the marketplace might not refresh for hours or days, if ever.

A user viewing the NFT on their wallet might see an outdated image. The true state of the NFT (on the metadata server) and the displayed state (in marketplaces) can diverge significantly.

Some projects work around this by building custom galleries or frontends where Dynamic NFTs display correctly. Others push metadata updates to IPFS (where the content hash changes, making history transparent) or use standards like EIP-4906 which signal to wallets that metadata has changed.

## Dynamic NFTs vs. soulbound tokens

Soulbound tokens (non-transferable NFTs) sometimes update based on holder achievements or time passed. A soulbound diploma might unlock new traits when the holder completes a course. Soulbound tokens are a subset of Dynamic NFTs — they update, but they also can't be traded.

Most Dynamic NFTs remain transferable. The updating mechanic is separate from the trading restriction.

## Why Dynamic NFTs haven't dominated

Despite the conceptual appeal, Dynamic NFTs remain niche. Reasons:

**Complexity:** Creating reliable Dynamic NFTs requires coordination between smart contracts, oracles, and off-chain servers. Most projects can't maintain this infrastructure long-term.

**Display issues:** As noted, marketplace support is spotty. Users often see stale images.

**Regulatory uncertainty:** A Dynamic NFT whose appearance changes based on external data might be deemed a security (if it tracks asset prices or yields). Regulators have not made clear rulings.

**User confusion:** A collectible whose image changes unexpectedly can feel unsettling to owners. Static NFTs feel more like ownership of a fixed thing.

**Cost:** Keeping a metadata server or IPFS gateway live costs money. Projects that halt funding often abandon Dynamic NFTs.

That said, Dynamic NFTs work well in specific contexts — in-game items (where the game developer controls the update mechanism) and real-world asset tracking (where transparency is valuable). They're not likely to replace static collectibles, but they fill a design niche.

## See also

<div class="wiki-seealso">

### Closely related

- Soulbound Token — non-transferable NFTs, sometimes Dynamic
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the infrastructure enabling NFTs
- [Smart Contract](/smart-contract/) — the code that mints and manages Dynamic NFTs
- [Distributed Ledger](/distributed-ledger/) — the underlying ledger technology
- [Initial Coin Offering](/initial-coin-offering/) — earlier tokenization model

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — marketplaces where Dynamic NFTs trade
- [Ethereum](/ethereum/) — the primary blockchain for Dynamic NFT projects
- Decentralized Finance — ecosystem that uses Dynamic tokens as collateral
- [Price Discovery](/price-discovery/) — the mechanism that feeds data into Dynamic NFTs

</div>

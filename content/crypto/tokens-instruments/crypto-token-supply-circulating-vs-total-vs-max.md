---
title: "Circulating Supply vs Total Supply vs Max Supply in Crypto"
description: "The difference between circulating, total, and max supply in crypto; how each affects market cap calculations and price discovery."
keywords:
  - circulating supply
  - total supply
  - max supply
  - crypto supply
  - cryptocurrency metrics
  - market capitalization crypto
---

*Cryptocurrency markets quote three supply figures—**circulating supply**, **total supply**, and **max supply**—each measuring a different point in the token's lifecycle and lifecycle cap.* Circulating supply is the number of tokens currently in active use; total supply includes locked, unvested, or reserved tokens not yet released; max supply is the permanent cap hard-coded into the protocol (or absent entirely if a token has unbounded inflation). The distinction matters because market capitalization calculations use circulating supply, yet future dilution depends on total and max.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Token Supply Types — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Circulating supply drives price; max supply sets the ceiling; total supply fills the gap.</div>

|   |   |
|---|---|
| **Circulating supply** | Tokens actually in wallets and tradeable now |
| **Total supply** | Circulating + locked, vested, reserved, not yet distributed |
| **Max supply** | Hard cap if one exists; absent for many protocols |
| **Market cap formula** | Price × Circulating supply (not total) |
| **Dilution risk** | Future = Total − Circulating; Ultimate = Max − Total |
| **Common issue** | Competing definitions; community distrust of supply figures |

</aside>

## Circulating Supply: What's Actively Traded

**Circulating supply** is the simplest conceptually: tokens that exist and are not locked. A user holding Bitcoin in a wallet, a staking pool holding Ethereum, a liquidity provider's token balance—all count toward circulating supply. When a crypto exchange publishes "Bitcoin's circulating supply is 21 million," it means roughly 21 million BTC are expected to be mined across all time; as of today, ~21 million have been released (the last will come in ~2140).

The figure is used to calculate **market capitalization**:
$$\text{Market Cap} = \text{Price} \times \text{Circulating Supply}$$

If Ether trades at $2,000 per coin and 120 million ETH are in circulation, the market cap is $240 billion. This metric helps investors compare the total dollar value locked in each token and estimate a "cost to flip" (how much capital would move the price if all circulating tokens were acquired).

The challenge: **no central registry tracks which tokens are truly tradeable**. Exchanges, data providers (CoinMarketCap, CoinGecko), and blockchain explorers use slightly different definitions. An Ethereum token locked in a [smart contract](/smart-contract/) may be unspendable but still show on the blockchain; some counters exclude it, others don't. Disagreement creates confusion and occasional manipulation.

## Total Supply: The Next Layer of Dilution

**Total supply** includes circulating plus all tokens that have been minted but not yet distributed to the public. Common examples:

- **Vesting schedules**: Team tokens locked in a vesting contract, released monthly or yearly over multiple years.
- **Treasury reserves**: Tokens held by the foundation or DAO, reserved for future grants or incentives.
- **Staking rewards**: In Proof of Stake systems (like Ethereum), validators earn new tokens. Some protocols pre-mint them; others print on demand. If pre-minted and locked, they count toward total supply.
- **Ecosystem allocations**: Tokens allocated to developers, advisors, or early backers but not yet distributed.

Consider a fictional token with:
- Circulating: 100 million
- Team vesting (3 years remaining): 20 million
- Treasury reserve: 15 million
- Staking rewards (not yet released): 10 million
- **Total supply**: 145 million

If all vesting schedules run to completion and all reserves are released, circulating supply expands to 145 million. If price stays constant, market cap stays constant but per-token value is diluted: the pie stays the same size but is cut into more slices.

Total supply is published on block explorers (Etherscan, Solscan, etc.) and aggregated by data sites. However, **not all locked tokens are disclosed equally**. A team that holds tokens in a multisig wallet may not register on public vesting contracts; circulating supply may undercount their eventual dilution. This opacity is why some investors distrust supply claims.

## Max Supply: The Protocol Ceiling

**Max supply** is the hard limit built into the consensus rules—if one exists. Bitcoin has a max of exactly 21 million; Ethereum has no max (inflation is capped at a rate, not a sum). Dogecoin has no max; Litecoin caps at 84 million.

Max supply represents the ultimate supply after all inflation has completed. It is **often absent** in newer tokens that operate with unbounded inflation (like traditional currencies) or periodic governance votes on emission policy. In those cases, data sites show total supply but no max.

When a max exists, it sets a **theoretical lower bound on dilution**:
- If max = 100 million, total = 60 million, and circulating = 40 million, then future dilution is capped at 40 million additional tokens.
- If the price remains constant and all 100 million are eventually minted, circulating supply would 2.5× and per-token value would fall by 60% (from $1 to $0.40, keeping dollar market cap constant).

## Market Cap Implications

The three supply figures matter for valuation because they define different time horizons:

| Supply Type | When | Market Cap Interpretation |
|---|---|---|
| Circulating | Now | "Today's stock-like market value" |
| Total | Next 1–3 years | "Diluted cap if all locked tokens enter circulation" |
| Max | Long term | "Ultimate cap if inflation runs to the end" |

A token might have a $50 billion circulating market cap but a $200 billion fully-diluted cap if substantial vesting remains. Institutional investors often compare **fully diluted valuation** (using total supply) to understand the true long-term capital structure.

Conversely, a token with high max supply but low total minted might appear cheap by market cap (small dollar value) but have enormous future dilution ahead. A protocol that has only minted 5% of its max so far is at risk of 20× future dilution, depending on governance and emission policy.

## Supply Disagreements and Data Quality

Supply figures vary across data providers because:

1. **Different treatment of locked tokens**: Is a smart contract holding 10 million tokens locked until 2027 included in circulating supply? Different counters decide differently.
2. **Burn events**: Some tokens burn (permanently remove) circulating supply through fee mechanisms or intentional destruction. If a token burned 1 million last week, circulating supply fell 1 million, but some data sources lag.
3. **Token splits and migrations**: When a protocol upgrades (Ethereum 1.0 → 2.0, Ethereum Classic after the fork), supply resets or branches; legacy counters may still reference old figures.
4. **Governance changes**: A DAO might vote to increase max supply or halt inflation. Community consensus on whether the chain "actually did" that varies.

To verify supply, read the blockchain directly (Etherscan, Solscan, block explorers) or the protocol's published whitepaper and emission schedule. CoinMarketCap and CoinGecko are widely used but not infallible.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart contract](/smart-contract/) — Vesting contracts often lock and release tokens on schedule
- [Proof of stake](/proof-of-stake/) — Consensus mechanism that determines how new tokens are minted as rewards
- [Distributed ledger](/distributed-ledger/) — Blockchain records all supply changes and holdings
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Platforms report circulating supply, though definitions vary

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — Underlying technology defining token supply rules
- [Ethereum](/ethereum/) — Major token with no hard max supply; uses supply cap on [base reward rate](/proof-of-stake/) instead
- [Bitcoin](/bitcoin/) — First token with a hard 21 million cap, embedded in the protocol

</div>

---
title: "Decentralised Exchange"
description: "A decentralised exchange (DEX) is a peer-to-peer platform where users trade cryptocurrencies directly from their own wallets using smart contracts. DEXs eliminate custodial risk but may have lower liquidity than centralised exchanges."
keywords:
  - decentralised exchange
  - dex
  - peer-to-peer trading
  - smart contract
  - amm
  - uniswap
image: "/svg/crypto.svg"
---

*A **decentralised exchange** (**DEX**) is a peer-to-peer cryptocurrency trading platform where users trade directly from their own wallets using smart contracts. DEXs eliminate custodial risk and censorship, but trading speed and liquidity depend on the underlying blockchain. The most common DEX model is the [automated market maker](/automated-market-maker/) (AMM).*

<div class="wiki-hatnote">

This entry covers decentralised exchanges. For centralised exchanges, see [centralised exchange](/centralized-exchange/); for the AMM mechanism, see [automated market maker](/automated-market-maker/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Decentralised Exchange — key facts</div>

<img src="/svg/crypto.svg" alt="DEX smart contract interface" />

<div class="wiki-infobox-caption">A DEX: peer-to-peer, trustless, on-chain.</div>

|   |   |
|---|---|
| **Operator** | None (protocol/smart contracts) |
| **Custody** | User-custodial (you hold your keys) |
| **Speed** | Blockchain speed (~12 seconds on Ethereum) |
| **Liquidity** | Variable (depends on [liquidity pools](/liquidity-pool/)) |
| **Fee** | 0.01–0.3% (goes to [liquidity providers](/liquidity-provider/)) |
| **Regulation** | Minimal (protocol is decentralised) |
| **Risks** | Smart contract bugs, slippage, complexity |
| **Major examples** | [Uniswap](/automated-market-maker/), Curve, SushiSwap |

</aside>

## How a DEX works

1. **[Liquidity pool](/liquidity-pool/) exists.** Users deposit pairs of tokens (e.g., ETH and USDC) into a smart contract.
2. **User initiates trade.** A trader specifies a token pair and amount they want to trade.
3. **Smart contract executes.** The contract automatically swaps tokens from the pool, adjusting price based on supply/demand.
4. **Tokens transferred.** Trader receives the swapped tokens in their wallet; they retain custody throughout.

The entire process is on-chain; the trader never hands over private keys to an intermediary.

## AMM versus order book

**AMM (automated market maker):** [Liquidity providers](/liquidity-provider/) deposit tokens in pools. Trades execute against the pool at algorithmically determined prices. This is how [Uniswap](/automated-market-maker/) works.

**Order book:** Users place limit orders; trades occur when orders match. This is more similar to CEXs but still decentralised.

AMM DEXs are more common because they are simpler to implement.

## Advantages of DEX

**No custody risk.** You retain control of your private keys throughout. The exchange cannot steal your funds or go bankrupt and lock them away.

**No censorship.** A decentralised protocol cannot prevent you from trading. No exchange can freeze your account.

**Transparency.** All trades are on-chain and verifiable. No hidden fees, no market manipulation hidden in dark pools.

**Composability.** DEX smart contracts can be combined with other smart contracts, enabling complex strategies and yield farming.

## Disadvantages of DEX

**Speed.** Trades are as fast as the blockchain. On [Ethereum](/ethereum/), that's ~12 seconds; on [Bitcoin](/bitcoin/), ~10 minutes.

**Complexity.** Requires a web3 wallet, gas fees, understanding of [slippage](/impermanent-loss/).

**Slippage.** Large trades against a pool move the price unfavourably. A big market order might pay significantly more than the initial quoted price.

**[Impermanent loss.](/impermanent-loss/)** [Liquidity providers](/liquidity-provider/) face losses if token prices diverge significantly.

## Major DEX platforms

**[Uniswap](/automated-market-maker/):** The largest DEX by trading volume. Uses AMM model. Available on [Ethereum](/ethereum/) and many layer-2 solutions.

**Curve Finance:** Specialises in stablecoin trading (low slippage). Dominant for stablecoin pairs.

**SushiSwap:** A Uniswap fork with community governance and additional features.

**Balancer:** A flexible AMM allowing pools of 2–8 assets.

## Gas fees

Trading on a DEX costs gas (transaction fees). On [Ethereum](/ethereum/), a simple trade might cost $5–$50 depending on network congestion. This makes very small trades uneconomical.

Layer-2 DEXs (like [Uniswap](/automated-market-maker/) on [Arbitrum](/arbitrum/)) reduce gas costs 10–100x, making small trades feasible.

## Liquidity and trading pairs

A DEX is only useful if it has liquidity in the pairs users want. A DEX with no [liquidity pools](/liquidity-pool/) cannot facilitate trades.

[Liquidity providers](/liquidity-provider/) earn trading fees but face [impermanent loss](/impermanent-loss/) risks. Balancing incentives to attract liquidity is crucial for a DEX's success.

## Smart contract risk

DEX smart contracts are immutable; if there is a bug, users' funds can be lost. For example:

- A DEX contract with a bug might allow anyone to withdraw any token without payment.
- A contract might accidentally transfer tokens incorrectly.

This is why security audits are critical for DEXs.

## Comparison with CEX

| Aspect | DEX | [CEX](/centralized-exchange/) |
|--------|---|---|
| **Custody** | Non-custodial | Custodial |
| **Speed** | Slow | Fast |
| **Liquidity** | Variable | Deep |
| **Complexity** | High | Low |
| **Risk** | Smart contract | Counterparty |
| **Censorship** | Impossible | Possible |

DEXs are best for security-conscious users who value censorship resistance. CEXs are best for speed and ease of use.

## Regulatory status

Decentralised exchanges exist in a regulatory grey zone. Because the protocol is decentralised (no company operates it), it is unclear who is responsible for regulatory compliance.

Some jurisdictions try to regulate DEX interfaces (front-ends), but the underlying protocol remains difficult to regulate.

## Future of DEX

DEX volume has grown substantially. As layer-2 solutions reduce gas costs and as UI/UX improve, DEX adoption is accelerating.

The future likely involves hybrid approaches: decentralised execution with some centralised services (better UX, fiat on/off-ramps) layered on top.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — general exchanges
- [Centralised exchange](/centralized-exchange/) — custodial alternative
- [Automated market maker](/automated-market-maker/) — the AMM mechanism
- [Liquidity pool](/liquidity-pool/) — provides DEX liquidity
- [Liquidity provider](/liquidity-provider/) — who supplies pools

### Wider context

- Smart contract — DEX implementation
- [Impermanent loss](/impermanent-loss/) — risk for liquidity providers
- [Ethereum](/ethereum/), [Arbitrum](/arbitrum/), Layer-2 — DEX deployment chains

</div>

---
title: "Automated Market Maker"
description: "An automated market maker (AMM) is a smart contract that enables peer-to-peer trading by maintaining token pools. Prices are determined algorithmically based on the ratio of tokens in the pool, rather than through an order book."
keywords:
  - automated market maker
  - amm
  - liquidity pool
  - uniswap
  - price formula
  - decentralised exchange
image: "/svg/crypto.svg"
---

*An **automated market maker** (**AMM**) is a smart contract mechanism that enables peer-to-peer token trading using [liquidity pools](/liquidity-pool). Instead of matching buyers and sellers through an order book, AMMs use an algorithmic price formula (typically $x \times y = k$) where prices adjust based on the ratio of tokens in the pool.*

<div class="wiki-hatnote">

This entry covers the AMM mechanism. For decentralised exchanges that use AMMs, see [decentralised exchange](/decentralized-exchange); for liquidity pools, see [liquidity pool](/liquidity-pool).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Automated Market Maker — key facts</div>

<img src="/svg/crypto.svg" alt="Liquidity pool with price formula" />

<div class="wiki-infobox-caption">An AMM: algorithmic pricing through liquidity pools.</div>

|   |   |
|---|---|
| **Mechanism** | Pool-based pricing |
| **Price formula** | $x \times y = k$ (Uniswap v2) or variants |
| **Liquidity source** | [Liquidity providers](/liquidity-provider) depositing token pairs |
| **Slippage** | Higher for larger trades (moves price) |
| **Fee** | 0.01–0.3% goes to liquidity providers |
| **Speed** | One blockchain transaction |
| **Custody** | User-custodial (smart contract only) |
| **Major example** | [Uniswap](/automated-market-maker) |

</aside>

## The constant product formula

[Uniswap](/automated-market-maker) v2 uses the constant product formula:

$$x \times y = k$$

Where:

- $x$ = amount of token A in the pool
- $y$ = amount of token B in the pool
- $k$ = a constant

When a trader swaps token A for token B:

1. They deposit some amount $\Delta x$ of token A.
2. The pool must maintain $x \times y = k$, so $y$ decreases by $\Delta y$.
3. The trader receives $\Delta y$ of token B.

The price is determined by the current ratio ($x / y$) and adjusts as the pool composition changes.

## Example

Imagine a [liquidity pool](/liquidity-pool) with 1,000 ETH and 1,000,000 USDC. The constant is $k = 1,000 \times 1,000,000 = 1,000,000,000$.

A trader wants to swap 100 USDC for ETH. After the trade:

- Pool USDC: $1,000,000 + 100 = 1,000,100$
- Pool ETH: $x \times 1,000,100 = 1,000,000,000$, so $x = 999.9$ ETH
- Trader receives: $1,000 - 999.9 = 0.1$ ETH

But wait — at the current price (1 ETH = 1,000 USDC), 100 USDC should be 0.1 ETH. So the trader gets exactly the expected amount!

However, larger trades cause slippage. If a trader swaps 100,000 USDC:

- Pool USDC: $1,000,000 + 100,000 = 1,100,000$
- Pool ETH: $x \times 1,100,000 = 1,000,000,000$, so $x = 909.09$ ETH
- Trader receives: $1,000 - 909.09 = 90.91$ ETH

The trader received 90.91 ETH, but at 1,000 USDC/ETH, 100,000 USDC should be 100 ETH. The trader lost 9.09 ETH to slippage.

This is why large trades on AMMs are expensive — they move the price.

## Advantages of AMM

**Permissionless.** Anyone can deposit liquidity and become a [liquidity provider](/liquidity-provider).

**Automatic pricing.** No order book needed; prices adjust continuously based on supply/demand.

**Capital efficient (somewhat).** Even small pools can facilitate trades, though with slippage.

**Composable.** AMM smart contracts can be combined with other contracts, enabling complex strategies.

## Disadvantages of AMM

**Slippage.** Large trades face high slippage because prices adjust as the pool composition changes.

**Impermanent loss.** [Liquidity providers](/liquidity-provider) face losses if token prices diverge, even if they earn trading fees.

**Inefficiency.** The constant product formula is not the most capital-efficient pricing mechanism.

## Variations

**Uniswap v3:** Introduced concentrated liquidity, allowing LPs to specify a price range. This reduces slippage and improves capital efficiency but adds complexity.

**Curve Finance:** Optimised for stablecoins using a different formula (less slippage for similar-priced tokens).

**Balancer:** Allows pools with arbitrary token ratios (not just 50/50).

## Liquidity provider economics

[Liquidity providers](/liquidity-provider) earn trading fees (e.g., 0.3% on Uniswap) but face [impermanent loss](/impermanent-loss) if token prices diverge significantly.

To incentivise liquidity, AMMs sometimes offer additional rewards (governance tokens, yield farming) on top of trading fees.

## Security considerations

AMM smart contracts are immutable. A bug in the price formula or token transfer logic could result in lost funds.

For example, if the code accidentally divides instead of multiplies ($x / y = k$ instead of $x \times y = k$), prices would be completely wrong, and traders would be arbitraged out.

## See also

<div class="wiki-seealso">

### Closely related

- [Decentralised exchange](/decentralized-exchange) — platforms using AMMs
- [Liquidity pool](/liquidity-pool) — the underlying mechanism
- [Liquidity provider](/liquidity-provider) — who supplies pools
- [Impermanent loss](/impermanent-loss) — risk for LPs

### Wider context

- Smart contract — AMMs are smart contracts
- [Ethereum](/ethereum) — primary platform for AMMs
- [Uniswap](/automated-market-maker) — the largest AMM
- Yield farming — earning on liquidity provision

</div>

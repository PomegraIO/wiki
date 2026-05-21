---
title: "Liquidity Pool"
description: "A liquidity pool is a smart contract containing paired tokens that enables decentralised trading. Users deposit token pairs and earn fees from trades executed against the pool, but face impermanent loss if prices diverge."
keywords:
  - liquidity pool
  - amm
  - decentralised exchange
  - liquidity provider
  - trading fee
  - impermanent loss
image: "/svg/crypto.svg"
---

*A **liquidity pool** is a smart contract that holds paired cryptocurrency tokens and enables peer-to-peer trading through an [automated market maker](/automated-market-maker/) mechanism. Users (called [liquidity providers](/liquidity-provider/)) deposit equal values of two tokens and earn trading fees. Pool prices adjust automatically based on the ratio of tokens in the pool.*

<div class="wiki-hatnote">

This entry covers liquidity pools. For the AMM mechanism, see [automated market maker](/automated-market-maker/); for liquidity providers, see [liquidity provider](/liquidity-provider/); for the associated risks, see [impermanent loss](/impermanent-loss/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidity Pool — key facts</div>

<img src="/svg/crypto.svg" alt="Liquidity pool with token deposit and withdrawal" />

<div class="wiki-infobox-caption">A liquidity pool: earn fees by providing liquidity.</div>

|   |   |
|---|---|
| **What it is** | Smart contract holding paired tokens |
| **Tokens** | Any pair (e.g., ETH/USDC) |
| **Fee** | 0.01–0.3% per trade (paid by traders) |
| **Who earns fees** | [Liquidity providers](/liquidity-provider/) |
| **Minimum deposit** | Usually none (any amount) |
| **Risk** | [Impermanent loss](/impermanent-loss/) if prices diverge |
| **LP token** | Represents your share of the pool |
| **Major pools** | Uniswap ETH/USDC, Curve 3Pool |

</aside>

## Structure

A liquidity pool holds two (or more) tokens in specific ratios. Users deposit equal values of both tokens and receive LP tokens (liquidity provider tokens) representing their share.

For example, in a 100 ETH + 100,000 USDC pool (ratio 1:1,000):

- An LP deposits 1 ETH + 1,000 USDC.
- The LP receives tokens representing 1% of the pool.
- If the pool earns 10 USDC in fees, the LP receives 0.1 USDC.

## Trading against the pool

When a trader wants to swap ETH for USDC:

1. The trader sends ETH to the pool.
2. The pool's smart contract calculates how much USDC to send back (using the [AMM](/automated-market-maker/) formula).
3. The USDC is transferred to the trader.
4. A small fee (e.g., 0.3%) is allocated to LPs.

The pool ratio changes (more ETH, less USDC), which increases the price of ETH relative to USDC in the pool.

## Fee structure

Typical fees:

- **Uniswap:** 0.01%, 0.05%, 0.3%, 1% depending on the pool.
- **Curve:** 0.04% (lower for stablecoins).

Fees are taken from the trader and distributed to LPs proportionally to their share of the pool. If the pool earns 100 USDC in fees and you own 1% of the pool, you receive 1 USDC.

## Impermanent loss

When a [liquidity provider](/liquidity-provider/) deposits into a pool, their tokens are exposed to price movements. If one token increases in value relative to the other, the LP suffers **[impermanent loss](/impermanent-loss/)**.

Example: An LP deposits 1 ETH + 1,000 USDC in a pool. If ETH price increases to 2,000 USDC:

- The pool auto-balances, reducing ETH and increasing USDC to maintain the constant product.
- The LP now owns ~0.7 ETH + 1,400 USDC (roughly).
- If the LP had simply held, they would own 1 ETH + 1,000 USDC (worth ~3,000 USDC).
- The LP lost money compared to holding, despite earning fees.

This is [impermanent loss](/impermanent-loss/) — the difference between the LP's actual value and their hypothetical value if they had simply held.

However, if trading fees are sufficient, they can offset [impermanent loss](/impermanent-loss/).

## LP tokens

When an LP deposits into a pool, they receive **LP tokens** (or pool tokens) representing their share. These can be:

- **Held** to continue earning fees.
- **Traded** on decentralised exchanges.
- **Staked** in yield farming to earn additional rewards.
- **Withdrawn** by burning the LP token, which releases the underlying tokens.

## Concentrated liquidity (Uniswap v3)

Modern AMMs like Uniswap v3 allow LPs to specify a price range. Instead of providing liquidity across all prices, an LP might provide liquidity only between 1,500 and 2,500 USDC per ETH.

This allows:

- **Better capital efficiency.** The same capital earns more fees if prices stay in the specified range.
- **Higher risk.** If prices move outside the range, the LP earns no fees and faces worse [impermanent loss](/impermanent-loss/).

## Risk management for LPs

LPs can mitigate risks by:

- **Choosing stable pairs.** Pools of similar-priced assets (e.g., USDC/USDT) have minimal [impermanent loss](/impermanent-loss/).
- **Diversifying.** Contributing to multiple pools reduces exposure to any single pair.
- **Monitoring prices.** Withdrawing if prices diverge significantly (to limit losses).
- **Seeking high fees.** Pools with higher fees are more attractive if [impermanent loss](/impermanent-loss/) is similar.

## Historical context

[Uniswap](/automated-market-maker/) v1 (2018) pioneered the [AMM](/automated-market-maker/) model and made liquidity pools accessible to anyone. Prior to this, liquidity was provided by centralised market makers; now, anyone can earn fees by providing liquidity.

## See also

<div class="wiki-seealso">

### Closely related

- [Automated market maker](/automated-market-maker/) — the pricing mechanism
- [Liquidity provider](/liquidity-provider/) — who supplies pools
- [Impermanent loss](/impermanent-loss/) — the main risk for LPs
- [Decentralised exchange](/decentralized-exchange/) — platforms using pools

### Wider context

- Smart contract — pools are contracts
- Yield farming — earning on liquidity provision
- [Ethereum](/ethereum/) — primary platform for pools
- [Uniswap](/automated-market-maker/) — the largest AMM

</div>

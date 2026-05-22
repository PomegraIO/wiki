---
title: "Decentralized Exchange Mechanics"
description: "Peer-to-peer trading systems using automated market makers and liquidity pools to enable cryptocurrency trading without a central counterparty."
keywords:
  - decentralized exchange
  - dex
  - automated market maker
  - amm
  - liquidity pool
  - peer-to-peer trading
---

*A decentralized exchange (DEX) is a peer-to-peer trading system that uses [automated market makers](/wiki/automated-market-maker/) (AMMs) and [liquidity pools](/wiki/liquidity-pool/) to enable [cryptocurrency](/wiki/bitcoin/) trading without a central [counterparty](/wiki/counterparty-credit-risk/).*

<aside class="wiki-infobox">

| Feature | Detail |
|---------|--------|
| **Market Model** | Automated market maker with [liquidity pools](/wiki/liquidity-pool/), not order books |
| **Custody** | Non-custodial; traders hold private keys |
| **Price Discovery** | Set by [arbitrage](/wiki/arbitrage-defi/) between pools and external markets |
| **Governance** | Typically decentralized via [governance tokens](/wiki/governance-token/) |
| **Liquidity Providers** | Earn fees proportional to pool share; subject to [impermanent loss](/wiki/impermanent-loss/) |

</aside>

## How automated market makers work

Instead of matching buy and sell orders from a central [order book](/wiki/order-book-depth/), a DEX uses a mathematical formula to set prices based on the ratio of two assets in a [liquidity pool](/wiki/liquidity-pool/). The most common model—introduced by Uniswap in 2018—is the constant product formula: `x * y = k`, where `x` and `y` are the quantities of two tokens and `k` is a constant. If a trader wants to buy ETH by selling USDC, they deposit USDC into the pool, the pool's ratio shifts, and the formula determines how much ETH they receive. The price they pay rises slightly with the size of the [trade](/wiki/pairs-trading/), preventing arbitrage—this is called "slippage." A $100 trade might move price 0.1%; a $1 million trade might move it 5% or more, making large orders inefficient.

## Liquidity providers and yield farming

Traders cannot execute without liquidity, so DEXes incentivize **liquidity providers** (LPs) to deposit equal values of both tokens into the pool. An LP earns a fraction of every [trade fee](/wiki/payment-for-order-flow/) (typically 0.01%–0.5% per trade) proportional to their share of the pool. A provider who deposits $10,000 into a $1 million pool owns 1% and earns 1% of fees. However, LPs face **[impermanent loss](/wiki/impermanent-loss/)**: if the price of one asset rises or falls sharply, the LP's share of the pool ends up worth less than if they had simply held both tokens unchanged. This asymmetric risk is the price of earning fees.

To bootstrap liquidity, DEXes distribute governance tokens (like UNI from Uniswap, or AAVE) to LPs as rewards—a practice called "[yield farming](/wiki/yield-farming/)." Early LPs could earn 100%+ annual returns in governance tokens, creating a speculative frenzy in 2020–2021. Over time, as governance token prices decline and more capital floods pools, yields compress toward single digits.

## No central order book, no [clearing](/wiki/central-counterparty-clearing/)

Unlike a [centralized exchange](/wiki/centralized-exchange/) (which owns the [order book](/wiki/order-book-depth/) and [clears](/wiki/clearing-firm/) every trade), a DEX is non-custodial: traders retain control of their private keys throughout. When you swap tokens on Uniswap, the transaction is atomic—your USDC leaves your wallet, the pool executes instantly, and your ETH arrives in your wallet, all in a single on-chain transaction. If the transaction fails (e.g., insufficient liquidity, price moved beyond your "slippage limit"), the whole thing reverts and your USDC returns. There is no [settlement risk](/wiki/settlement-risk/), no [counterparty risk](/wiki/counterparty-credit-risk/), and no central entity can freeze your funds—as long as you control your private key.

## Price discovery via arbitrage

DEXes do not determine prices in isolation. If Uniswap's ETH/USDC pool shows a price of $2,100 per ETH but Coinbase (a [centralized exchange](/wiki/centralized-exchange/)) shows $2,000, [arbitrageurs](/wiki/arbitrage-defi/) will buy on Coinbase and sell on Uniswap until the gap disappears. This [arbitrage](/wiki/arbitrage-defi/) between DEXes and centralized venues ensures that DEX prices track real market value. The flip side: DEX prices are "lazy"—they only move when someone actually [trades](/wiki/trade-reporting/); in thin markets with low [liquidity](/wiki/liquidity-risk/), prices can lag by minutes or hours.

## Governance and [impermanent loss](/wiki/impermanent-loss/)

Most successful DEXes (Uniswap, Aave, Curve) issue governance tokens to distribute control among users rather than concentrating it in a company. Token holders vote on parameters: trading fees, new token listings, treasury allocation. This decentralization is a philosophical win but operationally messy—governance moves slowly and is subject to [flash loan](/wiki/flash-loan/) attacks (malicious voters can borrow huge sums, vote, and return the funds before their loan is repaid).

The core problem for LPs is [impermanent loss](/wiki/impermanent-loss/). If ETH doubles from $2,000 to $4,000 while you are an LP, you own proportionally more stables (USDC) and fewer ETH than if you had simply held both unchanged. You still earn fees, but the fees often don't compensate for the divergence—especially on highly volatile pairs. This is a contested phenomenon: some argue it is the cost of providing liquidity; others argue it is a design flaw and have proposed "constant-mean-market makers" and other formulas to reduce it.

## Types of DEXes and variants

**Constant-product AMMs** (Uniswap, SushiSwap) are the market standard. **Constant-mean AMMs** (Balancer) allow pools with more than two assets and custom weights (e.g., 60% DAI, 40% ETH). **Curve** specializes in stablecoin swaps with a custom formula that reduces slippage for stable-to-stable trades. **Concentrated liquidity DEXes** (Uniswap v3) let LPs specify a price range where they want their capital to work, increasing capital efficiency but requiring active rebalancing. **Intent-based DEXes** (emerging in 2024–2025) allow users to specify what they want without revealing their strategy, reducing [MEV](/wiki/mev-maximal-extractable-value/).

<div class="wiki-seealso">

### Closely related
- [Automated market maker](/wiki/automated-market-maker/) — Mathematical model powering DEX pricing
- [Liquidity pool](/wiki/liquidity-pool/) — Reserve of two assets enabling peer-to-peer trading
- [Impermanent loss](/wiki/impermanent-loss/) — Asymmetric risk faced by liquidity providers
- [Flash loan](/wiki/flash-loan/) — Uncollateralized loans repaid within a single block

### Wider context
- [Centralized exchange](/wiki/centralized-exchange/) — Order-book-based trading with custody
- [Arbitrage](/wiki/arbitrage-defi/) — Profit-taking across venues to equalize prices
- [Governance token](/wiki/governance-token/) — Token granting voting rights over protocol
- [Yield farming](/wiki/yield-farming/) — Earning rewards for providing liquidity

</div>

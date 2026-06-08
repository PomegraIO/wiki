---
title: "Concentrated Liquidity"
description: "How Uniswap v3 lets liquidity providers concentrate capital within custom price ranges to maximize fee revenue."
keywords:
  - uniswap v3
  - concentrated liquidity
  - liquidity ranges
  - capital efficiency
  - automated market maker
  - lp strategy
image: "/svg/crypto.svg"
---

*Concentrated liquidity is the mechanism that lets liquidity providers (LPs) allocate their capital to a specific price range rather than spreading it across the entire trading curve. Introduced by **Uniswap v3**, this model trades ease for efficiency—LPs must actively choose their exposure, but in return their capital works harder and generates more fees.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Concentrated Liquidity — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for decentralized finance." />

<div class="wiki-infobox-caption">LPs concentrate capital in custom ranges to boost fee yield at the cost of position management.</div>

|   |   |
|---|---|
| **What it is** | Capital allocated to a specific price range rather than uniformly across all prices |
| **Introduced by** | Uniswap v3 (2021) |
| **Capital efficiency gain** | Often 4,000x or higher vs. uniform distribution, depending on range width |
| **Trade-off** | Higher fees offset by [impermanent loss](/loss-aversion/) and rebalancing work |
| **Typical use** | Pairs with tight correlations or stable assets; widened ranges in volatile pairs |
| **Smart contract risk** | Concentrated positions are more sensitive to smart-contract exploits |

</aside>

## Why uniform liquidity was inefficient

Early [automated market makers](/etf/) like Uniswap v1 and v2 forced all liquidity into a single formula curve: the product of the two token reserves stays constant (x × y = k). If you deposited $10,000 worth of ETH and USDC, your capital was spread across every price from zero to infinity. In practice, most trades happen in a narrow band around the current price—but your capital was locked uselessly at extreme prices where almost no trading occurred. You earned fees only on the fraction of your capital that actually matched against swaps.

Concentrated liquidity inverts this. Instead of spreading $10,000 uniformly, you deposit it in, say, the price range between $1,500 and $2,500 per ETH. Now all your capital is where the action is. The fee-generating trades happen in that range, and you capture a larger share of the volume. The capital multiplier can be 5x, 20x, or even 4,000x higher, depending on how narrow your range and how much the price actually moves within it.

## How price ranges work in practice

In Uniswap v3, you select a lower and upper tick (Uniswap uses discrete price ticks rather than continuous prices). Your liquidity is "active" only when the current price sits between those bounds. When the price rises above your upper tick, your position is fully converted to the higher-denomination asset (e.g., all USDC). When it falls below your lower tick, you're fully in the lower asset (all ETH). In both cases, your liquidity earns zero fees until the price returns to your range.

This mechanism creates two opposing forces. The narrower your range, the higher your capital efficiency and fee yield—but the greater the risk that price moves outside your range, leaving you stranded. A range of $1,800 to $2,200 around a $2,000 price is much more efficient than $0 to $10,000, but it also means you stop earning fees if ETH moves to $2,500. Traders with strong convictions about where a pair will trade choose tight ranges; risk-averse LPs choose wide ones.

## The fee advantage and the cost

The fee-collection mechanism matters enormously. In a concentrated position, every swap that passes through your range swaps against a much smaller liquidity pool, increasing slippage. Traders pay more in fees to execute their transactions. LPs capture that fee volume proportional to their share of the liquidity in that range.

A typical ETH/USDC v3 position earns meaningful fees even at 0.01% annual returns or lower because the fee multiplier from concentration often exceeds the trading volume multiplier. Someone concentrating $10,000 in a tight range might earn the same fees a v2 LP would earn on $500,000 deployed across all prices—a 20x capital efficiency gain. But this comes with costs: rebalancing costs (gas fees to update your position), [impermanent loss](/loss-aversion/) (the divergence loss you face if the price drifts far from your range), and operational risk.

## Active management and risk

Concentrated liquidity is not passive. The moment price moves beyond your intended range, you stop earning fees and crystallize impermanent loss. Some LPs rebalance frequently—daily or weekly—harvesting accrued fees and shifting their ranges to track price movement. Others leave positions static and accept being out-of-range. The choice depends on gas costs, volatility, and the LP's time horizon.

Volatile assets (like most altcoins) make tight ranges dangerous; the price could spike 50% in an hour, rendering your concentrated position entirely out-of-range. Stable or tightly correlated pairs (like USDC/USDT, or ETH/stETH) allow much tighter ranges and correspondingly higher fee yields. This is why stablecoin pools on Uniswap v3 often offer extraordinarily high yield for minimal impermanent loss.

## Broader ecosystem adoption

Since Uniswap v3's release, concentrated liquidity has become the standard for modern AMMs. [Curve](https://curve.fi/), Balancer, and newer protocols have implemented concentrated mechanisms. Some projects like Camelot and the Arbitrum DeFi ecosystem have layered governance and rebasing tokens on top of concentrated liquidity to incentivize LPs to lock ranges in specific buckets, directing capital flow strategically.

The model also intersected with [protocol-owned-liquidity](/protocol-owned-liquidity/) strategies—protocols use concentrated positions to own their own trading pairs at tight spreads, capturing fees that would otherwise go to external LPs. This created a new economic dynamic where protocols compete on capital efficiency as much as on token utility.

## See also

<div class="wiki-seealso">

### Closely related

- [Automated market maker](/etf/) — the core mechanic that concentrated liquidity optimizes
- [Protocol-owned liquidity](/protocol-owned-liquidity/) — how protocols accumulate their own concentrated positions
- [Impermanent loss](/loss-aversion/) — the convergence risk LPs face when price moves
- [Liquidity mining](/etf/) — incentive programs that compensate LPs for concentrated risk
- [Yield farming](/etf/) — strategies that layer concentrated liquidity with token rewards

### Wider context

- [Decentralized exchange](/secondary-market/) — the broader DEX ecosystem where concentrated liquidity trades
- [Ethereum](/ethereum/) — the primary chain where Uniswap v3 and concentrated AMMs run
- [Smart contract risk](/operational-risk/) — the execution and economic risks of on-chain positions

</div>

---
title: "How to Calculate Fee Income from Liquidity Provision"
description: "Calculate fee income from liquidity provision in DeFi: understand volume, fee tiers, share of pool, and impermanent loss interaction."
keywords:
  - how to calculate fee income liquidity provision
  - liquidity provider fees
  - defi fee calculation
  - trading fee income
  - liquidity pool earnings
image: "/svg/crypto.svg"
---

*Liquidity providers earn fee income by depositing assets into a [pool](/smart-contract/), and estimating and measuring that income is a straightforward calculation—once you understand how volume, the fee tier charged by the protocol, and your fractional ownership of the pool interact. **How to calculate fee income from liquidity provision** requires tracking three numbers: the pool's trading volume, the fee percentage, and your share of the pool's assets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidity Provision Fee Income — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Fee income = (pool volume × fee tier × your share) — but your share changes as the pool's value fluctuates and other LPs join or exit.</div>

|   |   |
|---|---|
| **Basic formula** | Pool trading volume × fee tier % × (your liquidity ÷ total pool liquidity) = fee income |
| **Fee tiers** | Uniswap typically offers 0.01%, 0.05%, 0.30%, and 1.00%; other protocols vary |
| **Your share** | Amount of LP tokens you hold ÷ total LP tokens outstanding; or your assets ÷ total pool assets |
| **Impermanent loss** | The cost of holding both assets in a pool; net fee income must exceed it to profit |
| **Slippage impact** | Price movement within the pool reduces effective volume and fee capture per trade |
| **Accrual method** | Most protocols compound fees back into the pool; you see realized income only upon withdrawal |
| **Gas costs** | Transaction fees for deposit, withdrawal, and rebalancing reduce net fee income |

</aside>

## The Core Calculation

The fundamental equation for fee income from liquidity provision is straightforward:

**Fee income = Pool trading volume × Fee tier % × (Your liquidity ÷ Total pool liquidity)**

To work through this in concrete terms: suppose you deposit $10,000 into a Uniswap v3 ETH/USDC pool that charges a 0.30% fee. The pool has $1 million in total liquidity. Over a month, the pool processes $50 million in trading volume.

Your share of the pool is $10,000 ÷ $1,000,000 = 1%.

Pool fees collected = $50,000,000 × 0.30% = $150,000.

Your share of fees = $150,000 × 1% = $1,500.

Your fee income for the month is $1,500—before any costs or adjustment for impermanent loss.

## Fee Tiers and Protocol Design

Different decentralized exchanges offer different fee tiers to match market conditions and asset pairs. Uniswap v3, the most widely used DEX, offers four standard tiers: 0.01%, 0.05%, 0.30%, and 1.00%.

The lowest tier (0.01%) is typically used for stablecoin pairs (USDC/USDT) where traders expect minimal slippage and are price-sensitive. The highest tier (1.00%) is reserved for highly volatile or illiquid pairs where traders demand steeper compensation for risk. Mainstream pairs like ETH/USDC typically use 0.30%.

The fee tier you choose is crucial. A 1.00% fee tier on the same volume will generate ten times the fee income of a 0.01% tier—but a 1.00% tier also attracts less volume, because traders avoid it when lower-cost alternatives exist. Lower fees attract more volume; higher fees repel it. An LP must choose a tier that balances fee percentage against expected volume.

Some protocols, like Curve, specialize in stablecoin swaps and charge a flat 0.04% fee because the lower volatility supports thinner margins. Other AMMs allow fees to be set dynamically or by governance. The key is that you earn only on the tier you choose.

## Your Share of the Pool

Your share of the pool is not fixed. It evolves as:

1. **Other LPs deposit or withdraw**: If new liquidity enters, your fractional ownership declines even if your absolute token count stays the same. If others exit, your share rises.

2. **Fees accrue and compound**: In most protocols, trading fees are reinvested into the LP's position automatically, increasing their share over time.

3. **Asset prices move**: This is subtle. In Uniswap v3, you're providing liquidity within a price range you select. If prices drift outside that range, you may hold only one asset instead of both, and your share calculation changes.

To track your actual share at any moment, divide your LP token balance by the total supply of LP tokens for that pool, or divide your assets in the pool by the pool's total assets. Most DEXs and analytics platforms calculate this for you in real time.

## Measuring Realized vs. Accrued Income

In most protocols, fees do not arrive in a separate account. Instead, they compound back into your LP position. This means your share of the pool grows automatically as fees accumulate. The math is elegant but requires discipline to track:

- **Accrued income** is the fee accumulation in the pool since you last checked.
- **Realized income** is the fee you extract when you withdraw (some or all of) your position.

If you deposit $10,000, earn $1,500 in fees, and then withdraw $11,500, your realized fee income is $1,500. If you don't withdraw, the fees remain in the pool, and you've earned accrued income—but you haven't cashed it out.

Some LPs reinvest realized fees into additional LP positions; others take the income and redeploy elsewhere. The timing of withdrawal matters for tax purposes in most jurisdictions.

## Impermanent Loss and Net Income

Fee income is only meaningful if it exceeds impermanent loss. Impermanent loss occurs when the price of one asset in a pool moves significantly relative to the other, forcing you to hold a worse ratio of assets than if you'd simply held them outside the pool.

Here's a simplified example: you deposit equal dollar amounts of ETH and USDC into a pool at a 1:1 price ratio. Prices move such that ETH doubles. If you'd held both assets outside the pool, you'd have the same ETH amount but more USDC value. Inside the pool, the protocol forces you to have rebalanced to maintain the correct ratio, locking in a loss.

Impermanent loss is *impermanent* because it reverses if prices move back. But for many positions, especially in volatile pairs, the loss is permanent (you exit before prices recover).

To evaluate whether liquidity provision is worth it, compare your expected fee income to your expected impermanent loss. If you earn $1,500 in fees but suffer $2,000 in impermanent loss, your net is negative. This is why high fee tiers matter: they attract volatile pairs where impermanent loss is larger but fee compensation must be larger too.

## Volume, Concentration, and Fee Capture

Not all trading volume generates the same fee income for an LP. The volume that matters is the volume that flows through *your* specific price range (in protocols like Uniswap v3 that allow concentrated liquidity).

If you place liquidity in a tight band around the current price, most volume touches your liquidity and you capture fees efficiently. If you place liquidity far from the current price, fewer trades happen in your range, and your fee income drops.

Additionally, slippage—the price movement within the pool caused by a single large trade—can reduce the effective fee collected. A trader executing a $1 million swap in a $100 million pool will move the price during the swap, and part of the traded volume will occur at worse prices. This reduces the fee per dollar of notional volume.

Analytics platforms like Uniswap's own info site and third-party tools display historical volume and fee distribution, allowing you to model income before committing capital.

## Gas Costs and Net Returns

Every deposit, withdrawal, and rebalancing incurs gas costs (transaction fees). On Ethereum mainnet, these can be substantial—$50 to $500+ per transaction depending on network congestion. On cheaper chains like Arbitrum or Polygon, gas is negligible.

If you deploy $10,000 into a pool and plan to collect fees for a month before withdrawing, gas costs of $200–$400 (for deposit + withdrawal) will reduce your net return by 2–4%. For smaller positions or shorter holding periods, gas can outweigh fees entirely. This is why many LPs operate on sidechains with lower fees, or batch their rebalancing to amortize gas costs across multiple transactions.

## Tracking and Taxation

Recording fee income for tax purposes requires detailed transaction-level data: date, amount, price, volume, and your share. Most DEXs and wallet tools export this data, but formatting and aggregation across pools and chains is labor-intensive.

Many jurisdictions treat LP fee income as ordinary income (not capital gains), so accrual-basis reporting may be required even if you don't withdraw. This is evolving; tax treatment is still unsettled in many countries. Consult a tax professional if you're operating substantial positions.

## See also

<div class="wiki-seealso">

### Closely related

- [Decentralized Ledger](/distributed-ledger/) — the foundational technology powering liquidity pools and DEXs
- [Smart Contract](/smart-contract/) — how AMM pools execute swaps and accrue fees automatically
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — centralized and decentralized trading venues
- [Volatility Smile](/volatility-smile/) — price volatility dynamics that affect LP returns
- [Financial Ratios for Retail Industry](/financial-ratios-for-retail-industry/) — how traditional inventory-based earnings compare to algorithmic earning models
- [Slow-Moving Inventory Ratio](/slow-moving-inventory-ratio/) — parallel concept: capital deployed without generating return

### Wider context

- [Hedging with Derivatives](/derivatives-hedging/) — risk management strategies that LPs use to offset impermanent loss
- [Option Premium](/option-premium/) — fee and time-value concepts parallel to LP fee accrual
- [Execution Risk](/execution-risk/) — slippage and volume concentration risks in DEX trading
- [Market Maker Trading](/market-maker-trading/) — traditional market-making economics and the parallels to automated liquidity provision
- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — how risk and return are balanced in asset allocation

</div>

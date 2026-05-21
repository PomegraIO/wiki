---
title: "Liquidity Provider"
description: "A liquidity provider is a user who deposits paired tokens into a smart contract pool and earns trading fees. LPs are essential to decentralised exchanges but face impermanent loss if token prices diverge significantly."
keywords:
  - liquidity provider
  - lp
  - amm
  - yield farming
  - trading fees
  - impermanent loss
image: "https://picsum.photos/seed/liquidity-provider/900/600"
---

*A **liquidity provider** (**LP**) is a user who deposits cryptocurrency into a [liquidity pool](/liquidity-pool) and earns a portion of trading fees. LPs are essential to decentralised exchanges, supplying the capital that allows trades to occur. In return, LPs earn fees but face [impermanent loss](/impermanent-loss) if token prices diverge.*

<div class="wiki-hatnote">

This entry covers liquidity providers. For the pools they contribute to, see [liquidity pool](/liquidity-pool); for the AMM mechanism, see [automated market maker](/automated-market-maker); for the risks, see [impermanent loss](/impermanent-loss).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidity Provider — key facts</div>

<img src="https://picsum.photos/seed/liquidity-provider/900/600" alt="LP earning trading fees from pool" />

<div class="wiki-infobox-caption">A liquidity provider: earning fees from decentralised trading.</div>

|   |   |
|---|---|
| **What they do** | Deposit token pairs into pools |
| **Income source** | Trading fees (0.01–0.3% per trade) |
| **Minimum capital** | Usually none (any amount) |
| **Payout frequency** | Continuous (fees accumulate in pool) |
| **Duration** | Flexible (can withdraw anytime) |
| **Risk** | [Impermanent loss](/impermanent-loss) |
| **Additional incentives** | Yield farming rewards, governance tokens |

</aside>

## How liquidity providers earn

1. **Deposit:** An LP deposits equal values of two tokens (e.g., 1 ETH + 1,000 USDC) into a [liquidity pool](/liquidity-pool).
2. **Receive LP tokens:** The LP receives tokens representing their ownership share.
3. **Earn fees:** Every trade in the pool incurs a fee (e.g., 0.3% on [Uniswap](/automated-market-maker)). Fees are proportionally distributed to LPs.
4. **Withdraw:** At any time, the LP can burn their LP token and withdraw their share of the pool (plus accumulated fees, minus [impermanent loss](/impermanent-loss)).

## Fee structure

Different pools have different fee tiers:

- **0.01% fee:** Ultra-low fee for very similar assets (e.g., stablecoins).
- **0.05% fee:** Low fee for correlated assets.
- **0.3% fee:** Standard fee for most pairs.
- **1% fee:** High fee for volatile or newly launched pairs.

Higher fees incentivise LPs to provide liquidity in riskier pools.

## Economics

An LP's return depends on:

1. **Trading volume.** Higher volume = more fees earned.
2. **Pool size.** Larger pools dilute each LP's fee share, but attract more volume.
3. **Fee tier.** Higher fees = more income per trade, but might attract less volume.
4. **Price volatility.** Higher volatility = worse [impermanent loss](/impermanent-loss).

A successful LP strategy involves finding pools with high volume, reasonable fee tier, and low volatility.

## Impermanent loss in detail

[Impermanent loss](/impermanent-loss) is the key risk for LPs. If you deposit 1 ETH + 1,000 USDC and ETH price increases to 2,000 USDC:

- **If you held:** 1 ETH + 1,000 USDC = 3,000 USDC value.
- **As an LP:** The pool auto-balances; you own ~0.7 ETH + 1,400 USDC = 2,800 USDC value.
- **Loss:** 200 USDC (6.7%).

The loss is "impermanent" because it disappears if prices revert. But if prices stay divergent, the loss becomes permanent.

## Mitigation strategies

**Stable pair pools:** Pools of similar-priced tokens (USDC/USDT) have minimal [impermanent loss](/impermanent-loss). LPs in these pools earn fees with low risk.

**Concentrated liquidity:** Uniswap v3 allows LPs to specify a price range. If prices stay in range, capital is more efficient and earns more fees. If prices diverge, [impermanent loss](/impermanent-loss) is worse.

**Fee incentives:** Pools with higher trading volumes or additional rewards (yield farming) might offset [impermanent loss](/impermanent-loss).

## Yield farming

Yield farming combines liquidity provision with additional rewards. An LP deposits into a pool and additionally stakes the LP token to earn governance tokens or additional yields.

For example:

- Earn 0.3% trading fee from providing liquidity.
- Earn additional 50% APY in the protocol's token by staking the LP token.
- Total yield: ~50.3%.

However, yields vary widely and may not be sustainable. Always research the underlying protocol.

## Types of LPs

**Retail LPs:** Individuals providing capital to earn fees.

**Institutional LPs:** Funds or companies providing substantial capital for returns.

**Arbitrageurs:** LPs who simultaneously arbitrage different pools to extract value.

**Yield farmers:** LPs focusing on maximising incentive rewards, not just trading fees.

## Capital requirements

Unlike traditional market making (which requires millions), DEX liquidity provision has no minimum. An LP can deposit $100 or $100 million.

However, smaller deposits have worse economics (higher slippage for their own trades, smaller fee earnings).

## Regulatory considerations

In most jurisdictions, LPs are not regulated as securities traders or financial advisors. However, tax treatment varies:

- Some jurisdictions tax LPs like traders (capital gains).
- Others treat pools as business income.
- Some allow deducting [impermanent loss](/impermanent-loss).

Tax treatment is unsettled; consult a professional.

## Risks summary

- **[Impermanent loss](/impermanent-loss).** Prices diverge, you lose relative value.
- **Smart contract bugs.** Funds could be lost if the contract has a vulnerability.
- **Slippage.** Your own trades have slippage, reducing returns.
- **Regulatory risk.** Tax or legal treatment could change.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidity pool](/liquidity-pool) — where LPs deposit
- [Automated market maker](/automated-market-maker) — the mechanism
- [Impermanent loss](/impermanent-loss) — the main risk
- [Decentralised exchange](/decentralized-exchange) — platforms using LPs

### Wider context

- Smart contract — LPs use contracts
- Yield farming — additional incentives for LPs
- [Ethereum](/ethereum) — primary platform for LP activity

</div>

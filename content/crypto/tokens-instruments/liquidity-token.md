---
title: "Liquidity Token"
description: "A token that represents a share of a liquidity pool, held by a liquidity provider and redeemable for a pro-rata share of the underlying assets."
---

*A liquidity token (often called an LP token) is a receipt issued to a liquidity provider who deposits assets into a decentralized exchange or other liquidity-providing protocol. If you deposit 1 Bitcoin and 50 Ethereum into an automated market maker, you receive liquidity tokens representing your share of the pool. The liquidity token can be traded, lent, or held for future redemption. When you redeem the liquidity token, you receive your pro-rata share of the pool's assets plus any trading fees accumulated.*

## How liquidity tokens work

An automated market maker (AMM) maintains a pool of two assets. To provide liquidity, you must deposit both assets in a 1:1 value ratio (on Uniswap v2) or within a specific price range (on Uniswap v3). The protocol issues you liquidity tokens equivalent to your ownership stake in the pool.

These tokens are fungible—one liquidity token is worth the same as another liquidity token in the same pool. But they are not interchangeable with the underlying assets. A UNI-USDC liquidity token is not the same as UNI or USDC; it represents a claim on a share of both.

When you redeem your liquidity token, the protocol burns it and transfers your share of the pool's assets back to you. If the pool has generated trading fees, you receive a pro-rata share of those fees in addition to your original assets.

## Liquidity tokens as composable assets

One advantage of liquidity tokens is that they are themselves tradeable assets. You can provide liquidity to Uniswap, receive UNI-USDC liquidity tokens, and then:

- Sell the liquidity tokens on a secondary market.
- Deposit them as collateral into a lending protocol.
- Stake them in a yield-farming contract to earn additional rewards.
- Swap them for other assets.

This composability is powerful in decentralized finance. A single liquidity token can be simultaneously earning trading fees, serving as collateral for a loan, and earning staking rewards from a farming program. Traditional finance rarely allows this—a stock certificate cannot simultaneously be a loan collateral and earn dividend payments and grant voting rights on multiple things at once.

## Liquidity tokens and [impermanent-loss](/wiki/impermanent-loss/)

Holding a liquidity token exposes you to [impermanent-loss](/wiki/impermanent-loss/). If the prices of the underlying assets diverge significantly, the pool automatically rebalances by selling the appreciating asset and buying the depreciating one. When you redeem your liquidity token, you may receive less of the appreciating asset than you deposited, costing you the opportunity gain.

This cost is offset by trading fees. If the pool generates enough fees to exceed the impermanent loss, liquidity provision is profitable. For stable pairs (USDC-DAI), fees often exceed impermanent loss because prices barely diverge. For volatile pairs (ETH-ALT tokens), impermanent loss can exceed fee income, creating a net loss for liquidity providers.

## Liquidity tokens in concentrated liquidity

Uniswap v3 introduced concentrated liquidity, allowing liquidity providers to provide assets only in a specific price range rather than across the entire price spectrum. This increases capital efficiency (you earn more fees per dollar of capital) but also increases impermanent loss if the price moves outside your specified range.

Concentrated liquidity tokens are more complex than uniform liquidity tokens. They must encode the price range, and their redemption value depends on the current price. If the current price is within your range, redemption is straightforward; if it is outside your range, you may receive only one of the two assets (the one whose price fell).

## Liquidity tokens and protocol risk

A liquidity token represents a claim on the protocol's ability to function. If the protocol is exploited or experiences a bug, the underlying assets might be stolen or lost, and the liquidity token becomes worthless. This risk is not fully priced into most liquidity tokens. Users often provide liquidity to unaudited or untested protocols, accepting substantial risk.

Major protocols (Uniswap, Curve) with audited smart contracts and long track records have lower risk. But newer protocols, even with audits, can experience novel attacks that no one anticipated. Liquidity providers in these protocols are exposing themselves to significant [smart-contract](/wiki/ethereum/) risk.

## Liquidity tokens as leverage

When a liquidity token is deposited as collateral in a lending protocol, the lender can use the capital to take a leveraged position. They can borrow stablecoins against the liquidity token, use those stablecoins to provide more liquidity elsewhere, and capture the interest spread. This amplifies returns but also amplifies risk. If the price of the underlying assets diverges unfavorably, the leveraged position can be liquidated, and the user can lose money.

## The market for liquidity tokens

Liquidity tokens are less commonly traded on secondary markets than the underlying assets because:

1. **Impermanent loss complexity.** Buyers must evaluate not just current pool composition but price-divergence risk, which is complex.
2. **Redemption friction.** It is often cheaper to provide liquidity yourself than to buy a liquidity token from someone else (due to transaction fees and bid-ask spreads).
3. **Staking and farming.** Liquidity providers often immediately stake their liquidity tokens in farming contracts to earn additional rewards, removing them from the secondary market.

However, some liquidity tokens do trade. Balancer and other AMM protocols have active secondary markets for their LP tokens. And some yield-aggregation protocols (Yearn, Aave) issue synthetic versions of liquidity tokens that bundle the underlying asset with staking or farming, making them more attractive to hold.

<div class="wiki-seealso">
<h2>See also</h3>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/liquidity-pool/">Liquidity Pool</a> — the underlying mechanism where liquidity tokens originate.</li>
<li><a href="/wiki/impermanent-loss/">Impermanent Loss</a> — the main risk of holding liquidity tokens.</li>
<li><a href="/wiki/yield-farming/">Yield Farming</a> — liquidity tokens are often staked to earn additional rewards.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/automated-market-maker/">Automated Market Maker</a> — the protocol underlying liquidity token issuance.</li>
<li><a href="/wiki/decentralized-exchange/">Decentralized Exchange</a> — platforms where liquidity tokens are created and traded.</li>
<li><a href="/wiki/token-swap/">Token Swap</a> — users provide liquidity to enable swaps.</li>
</ul>
</div>

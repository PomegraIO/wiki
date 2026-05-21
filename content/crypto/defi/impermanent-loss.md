---
title: "Impermanent Loss"
description: "Impermanent loss is the reduction in value a liquidity provider experiences when token prices diverge. It is the difference between holding tokens separately versus pooling them in an AMM."
keywords:
  - impermanent loss
  - il
  - liquidity provider
  - amm
  - divergence loss
  - price impact
image: "/svg/crypto.svg"
---

*An **impermanent loss** is a reduction in the value held by a [liquidity provider](/liquidity-provider/) in an [AMM](/automated-market-maker/) [liquidity pool](/liquidity-pool/) compared to simply holding the tokens separately. It occurs when token prices diverge, forcing the pool to auto-balance and LPs to own less of the appreciated asset.*

<div class="wiki-hatnote">

This entry covers impermanent loss as a concept. For liquidity provision generally, see [liquidity provider](/liquidity-provider/); for liquidity pools, see [liquidity pool](/liquidity-pool/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Impermanent Loss — key facts</div>

<img src="/svg/crypto.svg" alt="Impermanent loss graph showing loss by price change" />

<div class="wiki-infobox-caption">Impermanent loss: the cost of providing liquidity to price-moving assets.</div>

|   |   |
|---|---|
| **What it is** | Value loss from holding in pool vs. separately |
| **Trigger** | Price divergence between pooled tokens |
| **Magnitude** | Higher with greater price changes |
| **Example** | 1x price change = ~0.5% loss; 2x = ~5.7% loss |
| **"Impermanent"** | Reverts if prices return to original ratio |
| **Mitigated by** | Trading fees, stable pairs, concentrated liquidity |
| **Permanent if** | Prices never revert to original ratio |

</aside>

## The mechanism

When a [liquidity provider](/liquidity-provider/) deposits into an [AMM](/automated-market-maker/), they deposit equal values of two tokens. The pool maintains a constant product ($x \times y = k$) as trades occur.

If token A's price increases relative to token B, the pool auto-balances: it sells A and buys B. This rebalancing leaves the LP with less of the appreciated asset (A) and more of the depreciated asset (B).

## Example calculation

Imagine an LP deposits:

- 1 ETH (at 1,000 USDC each) = 1,000 USDC value
- 1,000 USDC

Total: 2,000 USDC value.

**Scenario 1: Hold separately**
ETH increases to 2,000 USDC. LP would own:

- 1 ETH (at 2,000 USDC each) = 2,000 USDC
- 1,000 USDC

Total: 3,000 USDC value.

**Scenario 2: In AMM pool**
With 1 ETH + 1,000 USDC in the pool ($x \times y = 1,000 \times 1,000 = 1,000,000$ constant):

As ETH price increases to 2,000 USDC, traders sell ETH for USDC. The pool equilibrates:

- Let the new pool be $x$ ETH + $y$ USDC, with $x \times y = 1,000,000$.
- At 2,000 USDC per ETH, the pool should have $y / x \approx 2,000$.
- Solving: $x \times 2,000x = 1,000,000$, so $x \approx 22.4$ and $y \approx 44,721$ USDC.

Wait, that doesn't seem right. Let me recalculate more carefully. If the LP owns a share of the pool and initially deposited 1 ETH + 1,000 USDC:

The LP's share is 1 out of the total. If the pool value increased, the LP's share also increased, but less than if they had held.

More precisely, the LP's impermanent loss is:

$$IL = \frac{2 \sqrt{P_1 / P_0}}{1 + P_1 / P_0} - 1$$

Where $P_1 / P_0$ is the price ratio change.

For a 2x price increase ($P_1 / P_0 = 2$):

$$IL = \frac{2\sqrt{2}}{3} - 1 \approx 0.886 - 1 = -0.114 \text{ or } -11.4\%$$

So the LP loses ~11.4% compared to holding.

However, if they earned trading fees of 1–5% during this period, the fees might offset the loss.

## Common scenarios

| Price change | Impermanent loss |
|---|---|
| 1.1x (10%) | ~0.1% |
| 1.5x (50%) | ~1.6% |
| 2x (100%) | ~5.7% |
| 3x (200%) | ~13.4% |
| 4x (300%) | ~20.1% |

Larger price moves cause larger impermanent losses.

## "Impermanent" versus "permanent"

The loss is called "impermanent" because it reverts if prices return to their original ratio. If ETH increases to 2,000 USDC then drops back to 1,000 USDC, the LP's impermanent loss disappears.

However, if prices never revert, the loss becomes permanent. An LP who deposited at the peak and held as prices collapsed would permanently lose value.

## Mitigation

**Stable pair pools:** USDC/USDT pools have minimal price divergence, so impermanent loss is negligible.

**High fee tiers:** Pools with higher trading volume and higher fee percentages might earn enough fees to offset losses.

**Concentrated liquidity:** Uniswap v3 allows LPs to concentrate liquidity in a narrow range. This increases fee earnings if prices stay in range but worsens loss if they don't.

**Diversification:** Providing liquidity across multiple pairs reduces exposure to any single pair's divergence.

## Is impermanent loss a tax?

Some view impermanent loss as the "price" of providing liquidity. LPs are essentially selling volatility (paying to hedge risks) and earning fees as compensation.

If fees exceed impermanent loss, the LP makes money. If not, the LP loses overall.

## Research

Academic research shows that most LPs experience net losses due to impermanent loss outweighing trading fees. Only sophisticated LPs or those in very high-volume, low-volatility pools consistently profit.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidity provider](/liquidity-provider/) — who experiences IL
- [Liquidity pool](/liquidity-pool/) — where IL occurs
- [Automated market maker](/automated-market-maker/) — the mechanism causing IL
- [Decentralised exchange](/decentralized-exchange/) — DEX using pools

### Wider context

- Smart contract — pools are contracts
- Yield farming — earning despite IL
- [Ethereum](/ethereum/) — primary platform for AMMs

</div>

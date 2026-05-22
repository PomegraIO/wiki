---
title: "Curve Wars"
description: "Competition among projects for liquidity incentives and voting control on Curve Finance's stablecoin decentralized exchange."
keywords:
  - curve wars
  - curve finance
  - liquidity mining
  - governance token
---

*The **Curve Wars** refers to the intense competition among cryptocurrency projects (including DAOs and protocols) for influence over [Curve Finance](/wiki/decentralized-exchange/), a dominant stablecoin [decentralized exchange (DEX)](/wiki/decentralized-exchange-mechanics/). Projects accumulate the CRV governance token and vote to direct liquidity incentives (rewards) to their own trading pairs, creating an "arms race" where protocols spend substantial capital to win governance votes and capture trading volume and fees on Curve.*

<aside class="wiki-infobox">

| Element | Description |
|--------|--------|
| **Central asset** | CRV token; controls Curve governance and reward allocation |
| **Mechanism** | Vote-escrowed model: lock CRV for veToken (voting power) |
| **Competitors** | StETH, USDT, Frax, and other stablecoin protocols |
| **Prize** | Gauge votes → liquidity incentives → trading volume → fees |
| **Timeline** | Intensive 2021–2023; ongoing but less heated as of 2024 |
| **Cost to win** | Protocols spent $100M+ on CRV to secure gauge votes |

</aside>

## Curve's dominance and governance structure

Curve Finance is the largest [automated market maker (AMM)](/wiki/automated-market-maker/) specialized in stablecoin trading. Because it uses a specialized curve formula (rather than the generic x*y=k of Uniswap), it offers lower slippage for stablecoin pairs, attracting high trading volume. Curve's native token, CRV, is used to govern the protocol: holders vote on which trading pairs (called "gauges") receive liquidity incentives. The incentives are substantial; Curve distributes millions of dollars in CRV tokens weekly to high-voted gauges, and protocols flush with capital realized that controlling those votes was valuable. High incentives = high liquidity = high trading volume = high fees for the protocol.

## The vote-escrowing mechanism and veToken

Curve uses a "vote-escrowing" (ve) model, popularized by Balancer. Instead of voting with plain CRV tokens, holders lock CRV for a period (up to four years) to receive veToken (voting escrow CRV, or veCRV). Longer locks receive more voting power; locking 1 CRV for 4 years yields 1 veCRV, while locking 1 CRV for 1 week yields ~0.05 veCRV. This mechanism incentivizes long-term governance commitment and discourages flash-loan attacks. However, it also means accumulating veCRV is expensive; accumulating 1 million veCRV required locking 1 million CRV for four years, or significantly more if locking for shorter periods. As CRV prices rose, that cost became staggering.

## The war and capital expenditure

Beginning in late 2021 and intensifying in 2022, major protocols realized the value of controlling Curve gauges. Lido Finance (dominant Ethereum staking protocol) wanted high incentives for its stETH/ETH pair to ensure liquidity and capture trading fees. Frax (fractional-reserve stablecoin protocol) wanted to boost Frax/USDC liquidity. Convex Finance (derivative protocol built on top of Curve) began accumulating veToken to sell voting power to other projects. The competition was fierce: protocols spent tens of millions of dollars buying CRV, locking it for four years, and voting for their gauges. A single gauge vote in 2022 was worth ~$1–2 million per week in incentives; controlling 20% of gauges was worth tens of millions annually.

## Convex Finance and voting delegation

Convex Finance emerged as a meta-layer on Curve. Convex accumulated massive amounts of veCRV by offering Curve LPs a deal: lock your CRV with Convex and earn additional CVX rewards (Convex's native token) plus delegated voting power, all without sacrificing liquidity. Convex pooled these votes and then auctioned the voting power to projects. Projects would pay CVX or other tokens to Convex in exchange for gauge votes. This created an efficient market for voting power and incentivized Convex accumulation of veToken. By mid-2022, Convex controlled ~50% of all veCRV, making it the de facto arbiter of Curve incentive allocation.

## Capital intensity and excess spending

The Curve Wars became a cautionary tale in capital allocation. Protocols routinely spent $2–3 in CRV purchases to win $1 in annual incentive value, making no sense on a pure return basis. But in 2021–2022, protocols were flush with venture capital and speculative trading gains; burning capital on governance seemed acceptable. Additionally, the narrative was powerful: "If we don't control Curve, our competitors will." This fear drove herd behavior and overspending. Once some protocols bought CRV aggressively, others felt compelled to follow, even if the return was poor.

## Cooling and maturing market

By late 2023, the intensity of the Curve Wars had declined. CRV token price fell sharply from its 2023 peak, making accumulation more expensive. Many early war participants (Frax, Lido) had already secured substantial voting power and reduced spending. Market participants became more price-conscious. The venture capital boom ended, and protocols faced pressure to show financial discipline. Additionally, the DEX market matured; while Curve remains dominant for stablecoins, alternative protocols and cross-chain DEXs offered competition. The wars persist in attenuated form, but the feverish spending of 2022 was unsustainable.

## Lessons and systemic implications

The Curve Wars highlighted the risks of vote-escrowing governance for protocols. Voting power concentrates among the richest players; smaller protocols cannot compete. Additionally, the wars revealed how governance can become detached from value creation; protocols were burning capital not to earn economics, but to prevent competitors from controlling incentives. Some observers argue this dynamic is inherent to ve-governance, while others contend better incentive design or governance structures (e.g., [quadratic voting](/wiki/voting-rights/)) could mitigate it. The wars also demonstrated that [decentralized governance](/wiki/governance-token/) is not immune to rent-seeking and capital misallocation.

<div class="wiki-seealso">

### Closely related
- [Decentralized Exchange](/wiki/decentralized-exchange/) — Curve's market type and function
- [Automated Market Maker](/wiki/automated-market-maker/) — Curve's mechanism (especially constant-product vs. stable-swap)
- [Governance Token](/wiki/governance-token/) — CRV's role in Curve governance
- [Liquidity Pool](/wiki/liquidity-pool/) — How Curve LPs earn fees and incentives

### Wider context
- [DeFi Composability](/wiki/defi-composability/) — Curve as infrastructure, Convex as meta-layer
- [Cryptocurrency Bubble](/wiki/cryptocurrency-bubble-2017/) — Broader crypto valuation cycles
- [Stablecoin](/wiki/stablecoin/) — Asset class underlying Curve's focus

</div>

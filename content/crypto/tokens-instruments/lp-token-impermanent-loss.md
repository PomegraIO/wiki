---
title: "LP Token Impermanent Loss Explained"
description: "Learn how LP token impermanent loss reduces liquidity-provider returns when prices diverge, with a worked example showing the arithmetic."
keywords:
  - lp token impermanent loss
  - impermanent loss amm
  - liquidity provider loss
  - automated market maker risks
image: /svg/crypto.svg
---

*An **LP token impermanent loss** is the shortfall in value a liquidity provider faces when token prices in an automated market maker diverge significantly from entry price, relative to simply holding the underlying pair. It arises because the protocol rebalances the pool's inventory as traders swap, forcing the LP to sell appreciating assets and buy depreciating ones—locking in a loss if prices don't recover.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LP Token Impermanent Loss — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and tokens." />

<div class="wiki-infobox-caption">The cost of providing liquidity when prices move, illustrated with real numbers.</div>

|   |   |
|---|---|
| **What causes it** | Pool rebalancing as traders swap; LP holds a fixed ratio of two assets, not a fixed quantity |
| **When it's worst** | Large price divergence (2x, 5x, 10x moves) between paired tokens |
| **When it's best** | Narrow price range; high trading fees offset the loss |
| **Is it "impermanent"?** | Only if prices revert; if they stay diverged, the loss becomes permanent |
| **How to measure it** | Compare LP token exit value to "hodl" value of same capital allocated 50/50 at entry |
| **Typical AMM design** | Constant product (Uniswap): x × y = k; depth of loss depends on the curve |

</aside>

## How the Pool Rebalancing Works

To understand impermanent loss, first understand how an AMM pool operates. A liquidity provider deposits two assets in equal value—say, 1 ETH and $3,000 in USDC, totaling $6,000. The pool enforces a ratio: if someone swaps USDC for ETH, they pull ETH out and push USDC in, automatically shifting the LP's holdings toward whichever asset buyers are dumping into the pool.

When ETH rises to $4,000, traders dump ETH to buy the now-cheaper USDC. The pool absorbs that ETH, and the LP's inventory drifts. Instead of still holding 1 ETH and $3,000 USDC, the LP now holds perhaps 0.75 ETH and $4,500 USDC. The LP has been forced to sell ETH into strength and hold more stablecoin—the opposite of buying low and selling high.

If ETH then crashes back to $3,000, the pool rebalances again, and the LP's loss becomes permanent. They exit with less than the $6,000 they put in, even after accounting for trading fees they earned.

## A Worked Example

Assume a Uniswap-style constant product pool with a 50/50 split at entry:

**Entry state (both assets at $1 each):**
- LP deposits 3,000 Token A + 3,000 Token B = $6,000 total value
- Pool constant: k = 3,000 × 3,000 = 9,000,000

**Price movement (Token A rises to $2; Token B stays at $1):**
- Traders buy Token A aggressively, so they sell Token B into the pool and pull Token A out
- Pool rebalances to maintain k = 9,000,000
- New state: approximately 2,121 Token A + 4,243 Token B (the product holds: 2,121 × 4,243 ≈ 9,000,000)

**LP value if they exit now:**
- 2,121 Token A @ $2 = $4,242
- 4,243 Token B @ $1 = $4,243
- Total = $8,485 + trading fees earned (roughly $85–200 depending on volume)
- Let's say total = $8,600

**Hodl comparison (if LP had just held their original coins):**
- 3,000 Token A @ $2 = $6,000
- 3,000 Token B @ $1 = $3,000
- Total = $9,000

**The loss:** $9,000 − $8,600 = $400, or roughly 4.4% impermanent loss before fees. Fees might recover half or all of this over time.

## How Price Magnitude Matters

Impermanent loss scales with divergence. A small move (±10%) causes minimal loss; a large move (2x, 5x, 10x) causes severe loss.

At a 2x ratio between the two assets, impermanent loss is roughly 5.4%. At 5x, it jumps to 25%. At 10x, it exceeds 50%. The relationship is not linear; larger moves compound the rebalancing damage.

This is why volatile pairs are risky for LPs. A stablecoin/ETH pool sees modest divergence because stablecoins don't move much; a meme-token/ETH pool can see 10x swings, inflicting catastrophic impermanent loss.

## When Fees Offset the Loss

The flip side: every swap through the pool generates a fee (typically 0.01% to 1%, depending on tier). High-volume pools earn fees that can offset impermanent loss if prices don't move too wildly or recover relatively quickly.

A tight range—say Token A fluctuates between $1.80 and $2.20—allows the LP to earn fees without suffering large rebalancing losses. An AMM pair with deep liquidity and moderate volatility can be profitable for LPs even if prices drift moderately.

Conversely, a thin, highly volatile pair may generate so little fee volume that the impermanent loss dominates.

## Why It's Called "Impermanent"

The name suggests the loss is reversible—if prices revert to entry, the loss evaporates. This is technically true: if Token A sinks back to $1, the pool rebalances again, and the LP recovers their original position (minus any slippage leakage).

But if prices never recover, the loss is permanent. The term is somewhat misleading; it's more accurate to say the loss is *conditionally permanent*, depending on price paths.

## How to Measure Your Own Exposure

To calculate impermanent loss on a position:

1. Record entry capital and the price of each token at deposit.
2. Record exit capital and prices at withdrawal.
3. Calculate what your capital would be worth if you had simply held the original coins (50/50 split) at exit prices.
4. Compare exit value to hodl value; the gap is impermanent loss.
5. Add trading fees earned to the impermanent loss figure; if fees exceed loss, the LP was profitable overall.

Many AMM dashboards and trackers now display this calculation automatically.

## See also

<div class="wiki-seealso">

### Closely related

- Automated Market Maker — how pools work and rebalance in response to trades
- Constant Product Market Maker — the x × y = k formula that drives impermanent loss magnitude
- [Liquidity Mining](/liquidity-mining/) — how protocols incentivize LPs to accept impermanent loss risk
- Slippage — related loss mechanism for individual traders, not LPs
- [Token Emission Schedule](/token-emission-schedule/) — how AMM incentive tokens are distributed to offset IL

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — centralized alternatives to DEXs and their trade-offs
- Volatility — what drives price swings and thus impermanent loss severity
- Hedging — techniques to reduce exposure to divergent pairs
- Diversification — broader risk management in decentralized finance

</div>

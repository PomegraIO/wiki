---
title: "Single-Sided Liquidity Provision in DeFi"
description: "How single-sided liquidity provision in DeFi lets you deposit one token instead of equal parts of a pair, and the trade-offs involved."
keywords:
  - single-sided liquidity provision defi
  - unimbalanced liquidity pools
  - asymmetric liquidity defi
  - one-sided lp tokens
---

*In standard AMMs, **single-sided liquidity provision** allows you to deposit only one token from a trading pair instead of both tokens in equal value. This feature reduces the friction of entering a pool but introduces new risks—mainly the exposure to one side of a swap and potential impermanent loss from price moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Single-Sided Liquidity Provision — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Deposit one token; the protocol routes the other half of your capital through a swap.</div>

|   |   |
|---|---|
| **Standard requirement** | Equal value in both tokens (50/50) |
| **Single-sided model** | Deposit only one token; protocol handles the swap |
| **Common protocols** | Uniswap v3, Balancer, Curve, Bancor |
| **Key advantage** | Simpler entry; no need for both tokens upfront |
| **Main risk** | Impermanent loss from internal swap slippage |
| **Entry fee impact** | Often higher due to embedded swap cost |

</aside>

## How Single-Sided Deposits Work

When you provide liquidity to a traditional AMM, you must supply both tokens in precise ratio. If you want to add $1,000 to an ETH–USDC pool, you deposit roughly $500 ETH and $500 USDC. This requirement creates friction: you need access to both assets, and if you only hold one, you must swap it first.

Single-sided provision flips the workflow. You deposit, say, $1,000 of only ETH. The protocol internally swaps approximately half that ETH for USDC, then deposits the resulting 50/50 pair into the pool. From your perspective, one transaction yields LP tokens backed by both assets.

Protocols achieve this through different mechanisms. Uniswap v3 introduced direct single-sided deposits for concentrated liquidity positions. Balancer uses metastable pools and swap routers. Curve and Bancor each handle it via wrapped versions or protocol-native routing.

## The Hidden Cost: Slippage and Spread Loss

Single-sided deposits are not free. When the protocol swaps your first 50% of deposited tokens into the second token, that swap incurs price impact—the "slippage" paid within your own transaction.

**Example:** You deposit 1 ETH (worth $2,000) into a pool where the swap from ETH to USDC normally has 0.3% slippage. The protocol swaps ~0.5 ETH at that slippage cost, losing roughly $3 to inefficient pricing. That loss is embedded in your LP position before you start earning fees. In illiquid pools, slippage can be 1–5%, making single-sided entry expensive relative to two-sided.

This spread loss is particularly harsh in:
- Small or newly launched pools with low liquidity
- Volatile token pairs where price moves mid-transaction
- Periods of high network congestion, delaying block inclusion

For large deposits, even a "small" slippage percent translates to thousands of dollars lost upfront.

## Impermanent Loss and Price Volatility

Every liquidity provider faces impermanent loss when token prices diverge from the deposit ratio. Single-sided deposits expose you to an additional form of it: the difference between your deposit price and the swap price embedded in the protocol.

If you deposit ETH and the protocol swaps your ETH for USDC at a price slightly worse than the current market rate, you immediately own a position biased toward the cheaper asset at the moment of deposit. If prices move further, that asymmetry can amplify losses.

Consider a concentrated liquidity position (common in modern AMMs). You deposit 1 ETH at $2,000 and the protocol swaps 0.5 ETH for 1,000 USDC at a rate of $2,000/ETH. If ETH falls to $1,800, your position—which now holds less ETH and more USDC—realizes losses twice over: the impermanent loss of a standard LP, plus the cost of having entered with an unfavorable internal swap rate.

## When Single-Sided Deposits Make Sense

The friction savings justify single-sided entry in specific scenarios:

- **Simplicity:** You hold only one token and want immediate exposure to a pool without executing a pre-swap.
- **Minimal slippage:** Highly liquid pools (major stablecoin or major asset pairs) with tight spreads. Slippage in a $100M+ USDC–USDT pool is negligible.
- **Automated strategies:** Protocols or smart contract bots that systematically add liquidity and cannot easily coordinate two-token deposits.
- **Incentives:** A pool offering temporary boosted rewards may outweigh the single-sided entry cost if you're eligible.

Single-sided provision also enables new users or those unfamiliar with the asset pair to participate without fully understanding two-token balancing.

## Comparison to Standard Two-Sided Deposits

| Factor | Two-Sided | Single-Sided |
|--------|-----------|--------------|
| **Setup** | Must source both tokens | Need only one token |
| **Upfront cost** | Only network fees | Network fee + swap slippage |
| **Impermanent loss** | Standard LP risk | Standard + swap price risk |
| **Best for** | Liquidity providers with balanced holdings | Newcomers or single-token holders |

Two-sided deposits remain the default in most protocols because they avoid the embedded swap cost. Many experienced LPs source both tokens separately or use flash loans to optimize entry, treating the cost-saving as a competitive edge.

## Risks Beyond Slippage

**Flashloan sandwiching:** If single-sided deposits process as a visible swap, the transaction may be visible in the mempool, inviting MEV (maximal extractable value) attacks where attackers front-run or back-run your deposit with larger swaps.

**Multi-hop routing:** Some single-sided wrappers route through multiple pools to source the second token. Each hop adds a tiny spread loss; the total can exceed direct two-token deposits if routing is inefficient.

**Liquidity fragmentation:** Concentrating single-sided deposits in a small number of protocols can fragment overall liquidity, leading to worse slippage for everyone.

## The Trade-Off

Single-sided liquidity provision trades simplicity for cost. It works best for trivial entry into highly liquid pools and worst for illiquid or volatile pairs where every basis point of slippage matters. Users should calculate the all-in entry cost—network fees plus swap slippage—and compare it against the time and complexity saved by avoiding a separate token swap.

## See also

<div class="wiki-seealso">

### Closely related

- Impermanent Loss in DeFi — how concentrated and standard LP positions lose value from token price divergence
- Automated Market Maker — how constant-product and other AMM designs execute trades
- Uniswap v3 Concentrated Liquidity — narrow range positions that enable range order strategies
- Slippage and Price Impact — how large trades move prices
- Liquidity Pool Design — multi-token pools and fee structures
- Flash Loans and MEV — sandwich attacks and mempool visibility risks

### Wider context

- DeFi Fundamentals — core AMM and LP concepts
- Token Economics — how new tokens incentivize liquidity
- Decentralized Finance — overview of the DeFi ecosystem

</div>

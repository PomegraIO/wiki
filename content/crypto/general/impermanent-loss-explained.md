---
title: "Impermanent Loss Explained with an Example"
description: "Impermanent loss explained: how price divergence between pooled assets causes losses for liquidity providers in automated market makers."
keywords:
  - impermanent loss explained
  - liquidity provider
  - automated market maker
  - uniswap
  - cryptocurrency trading
  - decentralized finance
---

*Impermanent loss is the loss that liquidity providers suffer when the price of two pooled assets diverge significantly. When you deposit two tokens into a liquidity pool on an automated market maker, the pool's algorithm forces you to maintain a constant ratio of both assets. As price moves, you're forced to hold more of the asset that has fallen and less of the asset that has risen—the opposite of what a passive holder would own. If you had simply held both tokens without providing liquidity, you'd have more value. **Impermanent loss explained** is the difference between that lost potential and what you actually earned in fees.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Impermanent Loss — liquidity provider economics</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The core problem: price divergence forces the liquidity provider into an unfavorable rebalance.</div>

|   |   |
|---|---|
| **Pool composition** | Two assets in a 50/50 value ratio (e.g., ETH and USDC) |
| **Liquidity provider role** | Deposit both; earn trading fees; maintain constant product formula |
| **Price movement scenario** | ETH doubles while USDC stays flat |
| **Forced rebalance** | Sell ETH for USDC to maintain constant product |
| **Result** | LP now holds more USDC and less ETH than a passive holder would |
| **Loss source** | Missed upside on the ETH that was sold automatically |
| **Fee recovery** | Trading fees can offset or eliminate impermanent loss if high enough |

</aside>

## How automated market makers work

A decentralized exchange like Uniswap uses an automated market maker (AMM) instead of an order book. Instead of waiting for a buyer and seller to agree on a price, an AMM pools liquidity and users trade against the pool.

A typical pool holds two assets—say, Ethereum (ETH) and USD Coin (USDC). A liquidity provider (LP) deposits both assets in equal value (e.g., $10,000 of ETH and $10,000 of USDC). In return, the LP earns a fraction of every trade fee (typically 0.25%, 0.3%, or 1%) that flows through the pool.

The AMM uses a simple formula to determine the price: **x * y = k**, where x is the amount of one asset, y is the amount of the other, and k is a constant. When a trader swaps one asset for another, the AMM adjusts the pool amounts so that x * y stays equal to k. This automatic rebalancing is what sets the exchange rate.

**Simple example:**
- LP deposits 10 ETH and 20,000 USDC
- k = 10 * 20,000 = 200,000
- Trader swaps 2,000 USDC for ETH
- New USDC in pool: 22,000
- To keep k constant: 10 ETH * x = 200,000, so x must be ~9.09 ETH
- Trader receives ~0.91 ETH for their 2,000 USDC
- Pool fees (0.3%): 6 USDC goes to LP

The LP earns fees on every trade. As long as there's no impermanent loss or it's small, the fees are profit.

## The impermanent loss problem: a worked example

Now imagine the price of ETH rises sharply. Let's walk through what happens:

**Initial state (LP's position):**
- Deposits: 10 ETH + 20,000 USDC
- Price of ETH: $2,000 per coin
- LP's total value: (10 × $2,000) + $20,000 = $40,000

**Price moves: ETH rises to $4,000**

If the LP just held the tokens (no pool, no trading), they'd now own:
- 10 ETH × $4,000 = $40,000
- 20,000 USDC = $20,000
- Total: $60,000 (a $20,000 gain)

But the LP is in a pool. As ETH's price rises, traders see the pool's price is stale (too cheap) relative to the market. They buy ETH from the pool using USDC. The pool algorithm automatically rebalances.

To keep x * y = k:
- As traders buy ETH, the pool's ETH amount shrinks and USDC amount grows
- The pool is forced to give up ETH and accumulate USDC
- Eventually, the pool reaches a new equilibrium

**Pool state after ETH rises to $4,000:**
- Original constant k = 10 * 20,000 = 200,000
- New ETH amount in pool: ~7.07 ETH (approximate)
- New USDC amount: ~28,284 USDC (approximate)
- (Verify: 7.07 * 28,284 ≈ 200,000)

**LP's share of the pool:**
Assuming the LP owns 100% of this pool (simplified), they now hold:
- 7.07 ETH × $4,000 = $28,280
- 28,284 USDC = $28,284
- Total: $56,564

**Compare to holding:**
- Hold scenario: $60,000
- Pool scenario: $56,564
- **Impermanent loss: $3,436**

The LP missed out on $3,436 in value because they were forced to sell ETH as its price rose. They held more USDC (which didn't appreciate) and less ETH (which did).

## Why it's called "impermanent"

The loss is called impermanent because it can be recovered if prices revert. If ETH falls back to $2,000:
- The pool rebalances again
- ETH amounts increase, USDC amounts decrease
- LP's position returns to roughly the original composition
- The loss disappears (minus any fee impact)

If the LP had entered at the $2,000 price, price had risen to $4,000, and then fell back to $2,000, they would have:
1. Realized the impermanent loss at the peak ($3,436)
2. Recovered the loss when price fell back
3. Kept all the trading fees earned along the way
4. Net result: profit from fees, zero impermanent loss

However, if price stays at $4,000 indefinitely (or continues to rise), the loss becomes permanent—it's never recovered.

## The fee offset

The saving grace for liquidity providers is trading fees. In the example above, as the price of ETH rose and traders bought the pool's ETH, the pool earned 0.3% on each swap.

If the pool generated, say, $3,500 in fees by the time ETH hit $4,000, the LP would have:
- Pool value: $56,564
- Plus accumulated fees: $3,500
- Total: $60,064
- vs. hold scenario: $60,000
- **Net gain: $64**

So the fees can offset or exceed the impermanent loss. The outcome depends on:
- How much the prices diverge (bigger divergence = bigger loss)
- How many trades occur (more trades = more fees)

For volatile asset pairs, the impermanent loss can be enormous, sometimes outweighing fees entirely. For stable coin pairs (e.g., USDC to DAI), prices don't diverge much, so impermanent loss is minimal, and fees are pure profit.

## The impact on pool composition

As price diverges, the LP's position shifts. In our ETH/USDC example:
- Original 50/50 split: 10 ETH + 20,000 USDC
- After ETH rises: 7.07 ETH + 28,284 USDC

The LP is now overweight in USDC (the asset that didn't appreciate) and underweight in ETH (the asset that did). They're holding more of the loser and less of the winner—the opposite of an optimal strategy.

This dynamic is why LPs in volatile pairs often suffer significant impermanent loss. High volatility means large price divergences, which means the algorithm forces larger rebalances.

## Strategies to mitigate impermanent loss

LPs who understand impermanent loss can reduce it:

**Choose stable pairs.** Deposit USDC and DAI (both stablecoins). Price divergence is minimal, impermanent loss is negligible, and fees are mostly profit.

**Choose concentrated liquidity.** New AMMs (like Uniswap v3) let LPs specify a price range. If they deposit liquidity only in the range $1,500–$2,500 ETH/USD and the price moves outside that range, the liquidity is no longer used—no impermanent loss. But the tradeoff is zero fees while the price is outside the range.

**Hold only while fees exceed loss.** Some sophisticated LPs monitor their position's impermanent loss in real time. If loss exceeds expected fees, they withdraw liquidity.

**Use pairs with high trading volume.** More trades = more fees. High volume is necessary but not sufficient to offset high volatility.

## Who bears impermanent loss?

Liquidity providers bear it. Traders do not. Traders are indifferent to impermanent loss because they're not holding the position; they're taking a trade and moving on.

The impermanent loss is essentially a cost of the liquidity-providing service. LPs accept it in exchange for earning fees. It's the price of being on both sides of every trade.

## Impermanent loss in complex strategies

In advanced DeFi strategies (yield farming, leveraged liquidity, single-sided liquidity), impermanent loss can be partially hedged or hidden, but it never disappears completely. Some protocols pay LPs extra rewards to compensate for expected impermanent loss in volatile pairs.

The fundamental problem remains: when two assets in a pool diverge in price, whoever is holding both (the LP) is forced into a position where they hold too much of the loser and too little of the winner. That's the essence of impermanent loss.

## See also

<div class="wiki-seealso">

### Closely related

- [Automated Market Maker](/automated-market-maker/) — The mechanism that causes impermanent loss
- [Liquidity Provider](/liquidity-provider/) — The role and rewards of AMM participants
- [Proof of Stake](/proof-of-stake/) — Contrasting economic model: validators, not liquidity providers
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — How centralized exchanges avoid this problem
- [Yield Farming](/yield-farming/) — Farming strategies that are exposed to impermanent loss
- Uniswap — The largest AMM and where impermanent loss is most commonly experienced

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — Core concepts behind decentralized finance
- [Distributed Ledger](/distributed-ledger/) — Technology underlying AMMs
- [Volatility Smile](/volatility-smile/) — Options concept related to divergent price moves
- Arbitrage — How traders profit from price divergences that cause LP losses

</div>

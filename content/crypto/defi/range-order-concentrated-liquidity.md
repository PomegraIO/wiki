---
title: "Range Orders in Concentrated Liquidity Pools"
description: "How range orders in concentrated liquidity work by placing capital in a narrow price range, effectively mimicking a limit order."
keywords:
  - range order concentrated liquidity
  - limit order amm defi
  - concentrated liquidity range
  - price range limit order
---

*A **range order** in a concentrated liquidity pool is a position placed within a single, narrow price band—typically one or two percentage points wide. As the trading price moves through that range, your liquidity gets swapped for the other token. This mechanism effectively mimics a traditional [limit order](/limit-order/), allowing you to execute trades at a specified price without relying on an order book or centralized exchange.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Range Orders in Concentrated Liquidity — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">Capital placed in a narrow band executes a swap when price crosses the range.</div>

|   |   |
|---|---|
| **Mechanism** | Deposit liquidity into a single tight price range |
| **Width** | 0.01% to 2% typical; customizable per protocol |
| **Execution** | Automatic when market price reaches your range |
| **Comparison** | Behaves like a limit order in traditional markets |
| **Capital efficiency** | Very high; all capital used within the range |
| **Execution certainty** | Near-certain if range is hit; no cancellation risk |
| **Gas cost** | Two transactions (deploy and remove) required |

</aside>

## How Range Orders Differ From Traditional Limit Orders

A traditional [limit order](/limit-order/) sits on an order book. You specify a price, and the exchange matches you with a counterparty at that price or better. If the price never reaches your bid, the order remains unfilled indefinitely.

A range order in an AMM works differently. You deposit liquidity into a pool within a narrow price band. As the market price fluctuates, traders swap against your liquidity. Once your capital is exhausted (all converted to the other token), the order is "filled." If the price never enters your range, your liquidity remains untouched and earns no fees.

**Key difference:** Traditional limit orders wait for a price; range orders are *waiting in that price region*, earning fees from every trade that crosses it.

## Mechanics: Placing and Executing a Range Order

Using Uniswap v3 as the example protocol:

1. **Define your range.** You specify a lower bound and upper bound price. For example, if ETH trades at $2,000 and you want to sell ETH for USDC only if the price rises, you might set a range from $2,000 to $2,020.

2. **Deposit one or both tokens.** If your range is above the current price, you deposit the token you want to sell (ETH). If your range is below, you deposit the token you want to buy (USDC). The protocol calculates how much liquidity that capital buys.

3. **Liquidity becomes active.** As traders swap in the pool, if the price moves into your range, your liquidity gets used to fill those trades. Each trade partially converts your tokens.

4. **Gradual execution.** Unlike a single-fill limit order, a range order can be filled piecemeal. If traders execute $500 in volume through your range, you receive the counterparty tokens. If $1,000 passes through, you receive more. Execution is proportional to how much of your liquidity gets consumed.

5. **Range exhausted or price exits.** When all your capital is converted (liquidity fully used) or the price moves away from your range, execution stops. You can then remove your position.

## Why Traders Use Range Orders

**Goal: Execute a large sell without slippage.** Suppose you hold 100 ETH and want to sell it all for USDC, but a single $4M market order would cause devastating slippage. Instead, you place a range order from the current price upward, across a $100,000 range. As the price rises naturally, your ETH is sold gradually, minimizing slippage on each micro-transaction.

**Goal: Harvest a specific price.** You believe ETH will rise to $2,100 but want to cap your exposure at that price. You deposit ETH and set a range from $2,100 to $2,120, allowing it to sell into strength without forcing an immediate sale at current prices.

**Goal: Dollar-cost averaging the buy side.** You want to accumulate stETH (staked Ethereum) but prefer buying in increments as price declines. You place a range order below the current price, ready to buy if the market drops into your range. As it does, your capital is gradually converted into stETH.

## Capital Efficiency and Fee Accrual

Range orders concentrate capital into a tight band, making them extremely capital-efficient. A $1 million range order across a 0.5% price band uses far more liquidity depth than $1 million spread across a 10% band. This efficiency means:

1. **Your liquidity handles more volume.** If traders execute $5 million in swaps within your range, more of that volume passes through your capital, generating more fees.

2. **Slippage for you is minimal.** Because your range is narrow, the incremental price movement within it is tiny, and you're effectively the "best" counterparty for most trades in that band.

3. **You earn more fees per dollar deployed.** Assuming the price stays in your range, concentrated capital generates higher returns than spread-out capital.

However, if the price never touches your range, you earn zero fees and may have wasted gas on the transaction.

## Comparison to Passive Liquidity Provision

| Factor | Passive (Wide Range) LP | Range Order |
|--------|--------------------------|-------------|
| **Price expectation** | Price stays in range | Price moves through your band |
| **Capital deployment** | 10–100% range possible | 0.01–2% typical |
| **Fee generation** | Continuous if price stays | Only during execution |
| **Impermanent loss** | Possible | Eliminated once fully converted |
| **Use case** | Market-neutral provision | Directional trading |
| **Gas cost** | Two transactions | Two transactions (same) |
| **Rebalancing** | May be needed | Not needed if filled |

Range orders blur the line between trading and liquidity provision. You're simultaneously providing liquidity (earning fees while in the range) and executing a directional bet (selling at a specified price band).

## Price Execution Certainty and Path Dependency

Range orders are nearly certain to execute **if the market price reaches the range**, but they're subject to **path dependency**. The same execution fills differently depending on whether the price rises smoothly or crashes through your range.

**Smooth rise through your range:** Traders gradually swap into your liquidity, filling your order methodically. You receive a fair distribution of fill prices across the range.

**Flash crash through your range:** If the market price crashes from $2,100 to $1,800 in a single candle, your range order (e.g., $1,950–$2,000) is entirely consumed at the worst prices within the range. You received the intended outcome—conversion of your tokens—but at worse-than-expected execution prices.

In volatile markets, range orders can end up partially filled at extremes, exposing you to execution risk despite being "automatic."

## Transaction Costs and Profitability

Range orders require two on-chain transactions: one to deploy and one to remove. In Ethereum, this can cost $50–$500+ in gas, depending on network congestion. On cheaper chains (Arbitrum, Polygon), gas is negligible.

**Profitability threshold:** If you earn 0.1% in fees while your range is active, you need at least $50,000 in volume to offset a $50 gas cost. For small positions, the gas may exceed earned fees, making range orders uneconomical.

## Variations: One-Sided vs. Two-Sided

Most range orders place capital on one side. You deposit ETH and specify an upper range where it converts to USDC. This is **one-sided liquidity**.

Some protocols allow two-sided ranges: deposit both tokens and specify a range where they swap both directions. This is less common and more niche, typically used for stablecoin pairs where the price should stay in a tight band.

## Range Orders on Major Protocols

- **Uniswap v3:** Native support; users specify lower and upper tick (price) bounds.
- **Balancer:** Supports ranges via asymmetric liquidity, though less user-friendly than Uniswap.
- **Curve:** Primarily designed for stablecoins; ranges less relevant.
- **Liquity:** Troves can be thought of as range orders for collateral management.

Higher-level protocols (aggregators, intent-based routers) sometimes abstract range orders into simpler UIs, allowing users to specify "sell 10 ETH above $2,100" without manually calculating ticks.

## Risks and Gotchas

**Range not hit.** If price never reaches your specified band, you earn no fees and have wasted gas.

**Partial fill at volatility.** Volatile markets can fill your range unevenly, leaving you with a worse-than-expected execution price.

**Liquidity fragmentation.** If many users place overlapping ranges, each gets a smaller share of fees, potentially making execution uneconomical.

**No slippage protection.** Unlike limit orders on centralized exchanges, there's no option to cancel or modify after deployment. You must remove the position to exit.

## Strategic Uses

Range orders excel in:
- **Selling strength.** Hold a coin and sell as it rises, harvesting higher prices without a single large dump.
- **Buying weakness.** Place a range below current price, ready to buy if the market dips.
- **Hedging leverage.** Sell upside while holding downside, creating a synthetic short call.
- **Protocol arbitrage.** Execute price discovery between two pools or chains by placing ranges that route capital to better prices.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — traditional order book execution at a specified price
- Uniswap v3 Concentrated Liquidity — how V3 enables ultra-precise position management
- Automated Market Maker — how pools execute trades without order books
- Impermanent Loss in DeFi — risks of holding both tokens across a range
- Slippage and Price Impact — how large trades move prices
- Liquidity Provision Strategies — passive and active LP approaches

### Wider context

- Decentralized Exchange — non-custodial trading venues
- Order Types and Trading — market, limit, and advanced orders
- Decentralized Finance — overview of the DeFi ecosystem

</div>

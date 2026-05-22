---
title: "Arbitrage in DeFi"
description: "Exploiting price discrepancies across decentralized finance protocols and exchanges to capture risk-free or near-risk-free returns."
keywords:
  - arbitrage
  - defi
  - price discrepancy
  - decentralized finance
  - liquidity pools
---

*[Arbitrage in DeFi](/wiki/arbitrage-defi/) exploits price differences for the same asset across [decentralized exchanges](/wiki/decentralized-exchange/), [liquidity pools](/wiki/liquidity-pools/), or lending platforms. An arbitrageur might buy ETH at $2,000 on one venue and sell at $2,010 on another, capturing the spread minus [gas fees](/wiki/arbitrage-defi/). Unlike traditional markets with central order books and tight [bid-ask spreads](/wiki/bid-ask-spread/), DeFi fragmentation creates persistent mispricings, attracting sophisticated traders and bots.*

<aside class="wiki-infobox">

| Factor | Details |
|--------|---------|
| **Spread Size** | 0.1–2% typical; wider during volatility |
| **Execution Speed** | Milliseconds (bots via [MEV](/wiki/mev-maximal-extractable-value/)) |
| **Costs** | [Gas fees](/wiki/arbitrage-defi/) 5–50% of profit depending on network |
| **Venue Pairs** | Uniswap-SushiSwap, Curve-Balancer, dYdX-Aave |
| **Risk** | [Slippage](/wiki/slippage/), smart contract vulnerabilities |
| **Strategy** | Statistical arbitrage, flash loans, sandwich attacks |

</aside>

## Statistical arbitrage across AMMs

Automated Market Makers ([AMMs](/wiki/automated-market-maker/)) like Uniswap use [liquidity pools](/wiki/liquidity-pools/) with constant-product formulas: price adjusts based on token ratio. During volatile periods, [AMM](/wiki/automated-market-maker/) prices lag [order books](/wiki/order-book-depth/), creating arbitrage. If Uniswap quotes ETH at $2,000 but Coinbase spot trades at $2,005, an arbitrageur buys ETH on Uniswap and sells on Coinbase, pocketing $5 per coin minus [gas fees](/wiki/arbitrage-defi/). High [gas costs](/wiki/arbitrage-defi/) on Ethereum make this profitable only for large trades; lower-fee chains ([Polygon](/wiki/polygon/), [Arbitrum](/wiki/arbitrum/)) enable smaller margins.

## Flash loans and atomic arbitrage

[Flash loans](/wiki/flash-loan/) enable uncollateralized borrowing if repaid within the same [transaction](/wiki/atomic-swap/). An arbitrageur borrows 1,000 ETH via Aave, buys low on one [DEX](/wiki/decentralized-exchange/), sells high on another, repays the loan, and keeps profit—all in one atomic transaction with no net capital requirement. This removes the need to hold capital overnight, amplifying arbitrage activity. If profit margins exceed flash loan interest (typically 0.05% of borrowed amount), the trade executes. Flash loans have enabled both legitimate arbitrage and [exploits](/wiki/flash-loan/)—attackers borrow massive sums to manipulate prices, extract value, then repay.

## Cross-protocol arbitrage and bridge risk

Assets often exist on multiple chains: USDC on [Ethereum](/wiki/ethereum/), [Solana](/wiki/solana/), [Polygon](/wiki/polygon/). If USDC trades at $0.995 on Ethereum and $1.01 on Solana, an arbitrageur can bridge USDC, execute the trade, and profit if bridge fees and [slippage](/wiki/slippage/) stay below the spread. [Bridge protocols](/wiki/bridge-protocols/) carry smart contract risk; if a bridge is hacked, bridged assets become worthless. This risk compounds returns, pushing arbitrage spreads tighter but adding execution hazards.

## MEV and transaction ordering

Miners and validators extract [Maximal Extractable Value (MEV)](/wiki/mev-maximal-extractable-value/) by front-running transactions. An arbitrageur submits a profitable trade; a validator inserts their own trade first (front-running) and a losing trade after (sandwich attack), capturing the arbitrage profit. Sophisticated DeFi traders use [private mempools](/wiki/dark-pool/) and encrypted order relays to hide trades and reduce MEV theft, but this comes at cost.

## Funding rate and perpetual futures arbitrage

On decentralized perpetuals ([dYdX](/wiki/decentralized-exchange/), [Hyperliquid](/wiki/futures-contract/)), the [funding rate](/wiki/carry-trade/) is the interest paid between long and short positions. If perpetuals trade rich (higher than spot), longs pay shorts via funding. An arbitrageur buys spot, short perps, and earns the funding rate spread minus costs—a [carry trade](/wiki/carry-trade/) variant. [Liquidations](/wiki/liquidation/) on the short leg add risk: if spot crashes and perps rally, the short position may liquidate before the hedge rebalances.

## Sandwich attacks and vulnerability

Arbitrageurs submit profitable transactions; miners can observe pending transactions, include their own trade ahead (front-running), and another trade behind (back-running), siphoning profit. A user executing a large swap on Uniswap observes impact costs; a bot can front-run, intensifying the user's slippage, then back-run to exit profitably. Defense mechanisms include private order flow, [order routers](/wiki/smart-order-router/), and MEV-resistant protocols.

## Arbitrage bot sophistication and infrastructure

Professional arbitrage requires high-speed execution, [latency](/wiki/latency-tier/) optimization, and capital efficiency. Bots monitor dozens of venues simultaneously, calculate profitable paths instantly, and execute. Infrastructure costs—dedicated hardware, direct RPC nodes, MEV protection—create barriers. Smaller traders face competition from well-capitalized bots with millisecond latency advantages; the market has structurally compressed [bid-ask spreads](/wiki/bid-ask-spread/), reducing retail arbitrage profits.

<div class="wiki-seealso">

### Closely related
- [Arbitrage Pricing Theory](/wiki/arbitrage-pricing-theory/) — Theoretical framework
- [Decentralized Exchange](/wiki/decentralized-exchange/) — Venue for DeFi arbitrage
- [Flash Loan](/wiki/flash-loan/) — Uncollateralized borrowing mechanism
- [Liquidity Pool](/wiki/liquidity-pools/) — AMM source of mispricings

### Wider context
- [Automated Market Maker](/wiki/automated-market-maker/) — DeFi market structure
- [MEV](/wiki/mev-maximal-extractable-value/) — Extraction risk
- [Slippage](/wiki/slippage/) — Execution cost
- [Statistical Arbitrage](/wiki/statistical-arbitrage/) — Quantitative approach

</div>

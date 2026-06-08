---
title: "Perpetual Protocol (DeFi)"
description: "Decentralized futures contracts with no expiry date, settled via automatic funding rates in AMM or order-book environments."
keywords:
  - perpetual futures
  - decentralized derivatives
  - funding rate
  - virtual amm
  - leveraged trading
  - dex derivatives
image: "/svg/crypto.svg"
---

*A **perpetual protocol** (or perpetual DEX) is a decentralized trading venue for futures contracts that never expire—allowing traders to hold long or short positions indefinitely, as long as they manage their collateral and margin. Unlike traditional derivatives exchanges, these protocols use [cryptocurrency-exchange](/cryptocurrency-exchange/) mechanics powered either by automated market makers (AMMs) or on-chain order books, with funding rates rather than daily settlement to keep contract prices tethered to spot markets.*

<div class="wiki-hatnote">

For the broader category, see Decentralized Finance (DeFi). For the price-discovery mechanism, see [Funding rate](#funding-mechanism).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Perpetual Protocol — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for decentralized finance and crypto derivatives." />

<div class="wiki-infobox-caption">Perpetuals replaced traditional expiring contracts with perpetual structures, funded by trader-to-trader payments.</div>

|   |   |
|---|---|
| **What it is** | Decentralized derivatives market for leveraged spot-like trading without expiry dates |
| **Settlement method** | Automatic funding-rate transfers, not marked-to-market liquidation |
| **Common design** | Virtual AMM (e.g. Perpetual Protocol v2) or on-chain order book (e.g. dYdX v4) |
| **Leverage range** | Typically 1–20×, capped by protocol risk parameters |
| **Core advantage** | No counterparty; no expiry; transparent on-chain pricing |
| **Core risk** | Slippage on entry/exit; liquidation if margin falls below maintenance |
| **Governance** | Most use DAO tokens for fee-switch and risk control votes |

</aside>

## Why perpetuals displaced traditional expiring futures

In traditional finance, futures expire monthly or quarterly. Traders roll positions forward to keep exposure, paying the bid–ask cost each time. Decentralized perpetuals remove this friction: a trader opens a 10× long Bitcoin position and holds it forever, paying only a funding rate to short traders who keep the market balanced.

The funding rate is the protocol's elegant answer to keeping perpetual prices aligned with spot. When longs outnumber shorts and the perpetual trades above spot, longs pay shorts an hourly or 8-hourly fee. This payment incentivises new shorts to enter and existing longs to close, pushing price back toward spot without needing an expiry or cash-settlement window. The rate adjusts mechanically—usually based on a formula tying it to open-interest imbalance and utilisation—so the market self-corrects.

## Virtual AMM vs. order-book designs

Early perpetual DEXs (Perpetual Protocol v1, Synthetix) used a **virtual AMM** approach: they simulated an order book without storing matched orders on-chain. A trader buys a perpetual the same way they'd swap tokens on Uniswap, with slippage proportional to position size. All positions sit in one liquidity pool. The AMM automatically prices the contract based on a formula (usually a constant product variant), and the protocol's price oracle feeds in the spot rate. If a trader leaves a 1,000× leveraged long unhedged, the entire pool bears that risk—leading to designs like capped leverage or insurance funds to absorb tail losses.

Newer protocols (dYdX v4, Hyperliquid) adopted **on-chain order books**: traders post limit orders or take available liquidity from the book. Matching happens on-chain (though sometimes batch-matched off-chain and verified). Order books reduce slippage and offer tighter spreads for market-makers, but they increase on-chain computation and latency compared to AMMs. Most still use funding rates to tether price to spot, but settlement logic can differ.

## Funding-rate mechanics

The funding rate is typically calculated every 8 hours (or 1 hour, depending on the protocol). At settlement, the protocol measures the premium: if the perpetual is trading 0.5% above spot, longs owe shorts 0.5% of notional position value, divided into 8-hourly chunks.

Some protocols tie the rate to maximum of spot premium and open-interest imbalance. Others use proportional interest: longs pay when leverage is imbalanced toward long side, rates shift fractionally each block or epoch. The exact formula varies, but the principle remains: continuous, automatic rebalancing without expiry auctions.

Traders often describe perpetuals as "cash-settled spot trading"—you get the leverage and continuous exposure of a futures position, but no T+0 or T+2 settlement headache. You only care about marking your position to market and managing collateral.

## Liquidation and margin mechanics

When a trader's collateral falls below the maintenance margin requirement (typically 5–10% of position notional), liquidation bots or the protocol's auto-deleveraging system steps in. If a position is liquidated, its collateral is seized and the position is closed at market price. Loss above collateral is usually absorbed by an insurance fund or socialised across remaining users (depends on protocol design).

Some protocols allow partial liquidation: if you're 20× long and hit maintenance, only 10× gets force-closed, letting you keep some upside. Others liquidate entirely in one go. Traders must monitor maintenance margin closely; a sudden spot move of 5–10% can easily trigger liquidation on levered positions.

## Why liquidity depth and oracle risk matter

A perpetual protocol is only as reliable as its oracle feed for spot price. If the oracle is delayed or attacked, traders can game the funding rate: buy cheap on spot, sell expensive on the perpetual, wait for a forced settlement, and pocket the arbitrage. Most protocols use multiple oracle sources ([Chainlink](/blockchain-fundamentals/), price aggregators, decentralized oracles) and have circuit-breakers to halt trading if one source deviates wildly.

Liquidity depth determines slippage. A thin AMM or order book can make it painful to enter or exit large positions. If you want to close a 100,000 USD position on a small perpetual DEX and the book only has 10,000 USD in bids, you'll bleed value. [Liquidity mining](/liquidity-mining/) programs and market-maker rebates are common ways protocols bootstrap depth.

## Governance and fee capture

Most perpetual DEXs are governed by a DAO token. Token holders vote on trading fees (typically 0.05–0.1%), funding-rate multipliers, leverage caps, and new asset listings. Fees accumulate in a treasury; some protocols burn them, others distribute to stakers. This aligns incentives: traders want low fees, but the DAO wants fees high enough to fund development and insurance.

## Risk and outlook

Perpetual DEXs have proven durable—they capture real trading demand and offer genuine liquidity. But concentration risk is real: if one perpetual DEX grows too large and its oracle is compromised or its smart contract is exploited, losses cascade. The space continues to innovate: merging AMM and order-book mechanics, improving oracle designs, exploring layer-2 solutions for lower latency and cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Funding rate settlement](/liquidity-mining/) — the mechanism that keeps perpetual prices aligned with spot
- Decentralized Finance — the broader ecosystem that perpetuals serve
- [Leverage and margin](/leverage-ratio-forex/) — how traders amplify exposure and face liquidation risk
- [Order book mechanics](/market-maker-trading/) — matching systems underlying order-book perpetual DEXs
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — centralized and decentralized spot trading foundations
- [Liquidity mining](/liquidity-mining/) — how protocols incentivise market depth on perpetual pairs

### Wider context

- [Bitcoin](/bitcoin/) — a major perpetual trading pair on most DEXs
- [Ethereum](/ethereum/) — another dominant perpetual trading asset
- [Crypto volatility](/cryptocurrency-exchange/) — perpetuals are tools for volatility traders
- [Blockchain fundamentals](/blockchain-fundamentals/) — the infrastructure underneath on-chain derivatives

</div>

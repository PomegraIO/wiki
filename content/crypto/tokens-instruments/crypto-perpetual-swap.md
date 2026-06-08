---
title: "Crypto Perpetual Swap"
description: "Leverage derivatives that track spot price indefinitely without expiration, maintained near market via periodic funding-rate settlements."
keywords:
  - perpetual swap
  - perpetual futures
  - crypto derivatives
  - funding rate
  - leveraged trading
  - perpetual contract
image: /svg/crypto.svg
---

*A **crypto perpetual swap** (or perpetual futures contract) is a leveraged derivative that mimics ownership of a [cryptocurrency](/stock/) without an expiration date, maintained at or near [spot price](/stock/) through periodic funding-rate payments between longs and shorts. Unlike standard [futures contracts](/stock/) that settle on a fixed date, perpetuals can be held indefinitely—making them the primary vehicle for leveraged crypto speculation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Perpetual Swap — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and tokens." />

<div class="wiki-infobox-caption">No-expiry derivatives that let traders lever up on spot price moves.</div>

|   |   |
|---|---|
| **What it is** | A [derivative](/stock/) contract that tracks the price of a [cryptocurrency](/stock/) with no maturity date and automatic funding rebalancing |
| **Leverage available** | Typically 2× to 100× depending on the exchange and [counterparty risk](/stock/) appetite |
| **Settlement** | Mark price, with no mandatory expiration (only liquidation) |
| **Funding mechanism** | Periodic payments from longs to shorts (or vice versa) keep the contract price anchored to spot |
| **Exchange type** | Centralized exchanges (Binance, Bybit, FTX before collapse); decentralized protocols (Hyperliquid, dYdX) |

</aside>

## Why perpetuals dominate crypto leverage trading

In traditional [futures markets](/stock/), a contract expires on a set date—three months later, say—and holders must close or roll to a new contract. This creates [roll costs](/stock/) and forces decisions. Crypto perpetuals eliminate this friction. Because the [funding rate](/stock/) continuously adjusts the price toward spot, traders can hold their positions indefinitely, paying (or receiving) only the small periodic funding settlement.

This is far cheaper and simpler than rolling [futures contracts](/stock/) in equities or commodities. The result: perpetuals have become the dominant way retail (and professional) traders access leverage on [cryptocurrencies](/stock/). Daily [trading volume](/stock/) in Bitcoin and Ethereum perpetuals often exceeds spot-market volume.

## The funding-rate mechanism

The core innovation that keeps a perpetual contract tethered to spot price is the **funding rate**—a small percentage fee paid periodically (typically every 8 hours) from traders on the winning side to the losing side.

When the perpetual is trading above spot price, longs are profitable relative to spot, so they pay shorts. This incentive encourages traders to short, driving the perpetual price down toward spot. When the perpetual trades below spot, shorts pay longs, encouraging long positions. The rate adjusts continuously or periodically depending on the exchange.

The funding rate is rarely large enough to guarantee a return, but it does anchor the perpetual to reality. If it broke free entirely, arbitrageurs could exploit the gap by holding a perpetual and a [spot position](/stock/) in opposite directions. The funding mechanism prevents this.

## Leverage and liquidation

Most perpetual exchanges allow traders to use 2× to 100× leverage, though higher multiples are rarer. A 10× long position means the trader controls \$1,000 notional value with \$100 of [margin](/stock/). If the underlying price falls 10%, the position loses 100% and is liquidated—the exchange closes it and keeps the margin (or takes it out of the trader's account).

Liquidation is automatic and often brutal. In volatile markets, a \$500 million position can be liquidated in seconds, triggering a cascade of forced sales that drive prices further down. Traders who are leverage-heavy often lose far more than they invested.

Most exchanges also employ a **maintenance margin** requirement—a smaller percentage, perhaps 5%, that traders must hold at all times. If margin falls below this, liquidation begins. Some exchanges use dynamic leverage or risk-management systems that reduce a trader's maximum leverage automatically if [volatility](/stock/) spikes.

## Centralized versus decentralized perpetuals

The earliest and still-largest perpetual swaps trade on centralized crypto exchanges: Binance, Bybit, OKX, and others. These platforms offer high [liquidity](/stock/), deep order books, and fast execution. The tradeoff: they hold trader funds, present [counterparty risk](/stock/), and can be hacked, regulated, or shut down (as FTX discovered in 2022).

Decentralized perpetual protocols (such as Hyperliquid and dYdX v4) settle on-chain, eliminating the middleman but introducing latency, higher fees, and sometimes less reliable [price discovery](/stock/). They also spread [liquidation risk](/stock/) across liquidity providers rather than centralizing it on the exchange. Some traders view decentralized perpetuals as more resilient; others find them slower and less forgiving for active trading.

## The speculation problem

Perpetuals are powerful for hedging and market-making. A fund that holds Bitcoin [spot](/stock/) can short perpetuals to lock in a price. An options [market maker](/stock/) can use perpetuals to delta-hedge. But the ease of access and high leverage have made perpetuals a retail speculation machine. A retail trader with \$1,000 can deploy \$100,000 notional exposure—enough to wipe out their account in minutes if wrong.

The most volatile episodes in crypto price action often correlate with mass liquidations in perpetual markets. When a flash crash liquidates thousands of leveraged longs or shorts simultaneously, the forced selling or buying accelerates the move, sometimes creating local market dislocations.

## Funding-rate arbitrage and basis trading

Professional traders often trade the **basis**—the difference between the perpetual price and the spot price. If perpetuals are trading 1% above spot and the funding rate is 0.05% per cycle, a trader with capital can:

1. Buy spot Bitcoin.
2. Short the perpetual.
3. Collect the funding rate until the prices converge.

This is low-risk but capital-intensive. It also makes the perpetual markets more efficient, tightening the basis and keeping them closer to spot.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/stock/) — the traditional derivatives that perpetuals resemble
- [Leverage Ratio Forex](/stock/) — similar leverage mechanics in currency markets
- [Margin Call Forex](/stock/) — the mechanism that triggers liquidation
- [Mark Price](/stock/) — how perpetuals value positions independent of the last trade
- [Volatility Smile](/stock/) — volatility dynamics that affect leverage-heavy trading
- [Meme Coin](/meme-coin/) — often the asset underlying highly leveraged perpetual trades
- [Token Standard](/token-standard/) — the basis of the assets being traded perpetually

### Wider context

- [Bitcoin](/stock/) — the most-traded perpetual underlying
- [Ethereum](/stock/) — the second-largest perpetual market
- [Cryptocurrency Exchange](/stock/) — where centralized perpetuals execute
- [Distributed Ledger](/stock/) — the tech enabling decentralized perpetuals
- [Counterparty Risk](/stock/) — the hazard of centralized exchange collapse
- [Systemic Risk](/stock/) — how large perpetual crashes can shake markets

</div>

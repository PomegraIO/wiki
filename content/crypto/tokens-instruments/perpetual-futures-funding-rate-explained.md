---
title: "Perpetual Futures Funding Rate Explained"
description: "How perpetual futures funding rates anchor derivative prices to spot, who pays whom, and how traders use funding as a sentiment indicator."
keywords:
  - perpetual futures funding rate
  - funding rate explained
  - crypto derivatives
  - perpetual contracts
  - basis trades
---

*The **perpetual futures funding rate** is a periodic payment between long and short traders that keeps the price of a perpetual futures contract anchored to the spot price of the underlying asset. When perpetual prices rise above spot, longs pay shorts to incentivize shorts to enter and cool the market; when perpetuals trade below spot, shorts pay longs. The funding rate is also a barometer of trader sentiment and leverage.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Perpetual funding — price anchor</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Funding rates force perpetual contracts back toward real-world prices.</div>

|   |   |
|---|---|
| **What it is** | Periodic payments between long and short perpetual futures traders |
| **Purpose** | Keeps contract price anchored to spot price |
| **Frequency** | Typically every 8 hours; varies by exchange |
| **Positive rate** | Longs pay shorts (perpetual is overpriced) |
| **Negative rate** | Shorts pay longs (perpetual is underpriced) |
| **Use by traders** | Sentiment indicator; arbitrage signal |

</aside>

## Why perpetual contracts need a funding mechanism

A perpetual futures contract is a derivative that has no expiration date, unlike a standard [futures contract](/futures-contract/) which settles on a specific date. Without an expiration, perpetuals are at risk of drifting away from the underlying asset's spot price indefinitely. If Bitcoin spot is trading at $45,000 but Bitcoin perpetual futures are trading at $50,000 on Binance, arbitrage opportunities become uneconomical—the basis (the difference between futures and spot) has grown too large.

The funding rate solves this. It is a mechanism that periodically transfers money between long and short perpetual traders. By making one side pay the other, the mechanism creates an economic incentive to close out profitable positions or open offsetting ones, pulling the perpetual price back toward spot.

## How the funding rate works

Most perpetual exchanges calculate and settle the funding rate every eight hours (Binance, Bybit, Deribit). Some use hourly or daily intervals. At settlement, the exchange compares the perpetual futures price to an index price (a fair-value estimate of spot, usually an average across multiple spot exchanges).

If the perpetual is trading above the index price, the market is overbought. The funding rate is set to a positive value. All traders with long positions pay all traders with short positions a fee proportional to their position size. For example, if the funding rate is 0.05% and you hold a long position worth $100,000, you pay $50 every eight hours.

Conversely, if the perpetual is trading below the index price, the funding rate is negative. Shorts pay longs. A trader holding $100,000 short at a −0.05% rate receives $50.

The funding rate formula varies by exchange, but a common approach is:

> Funding Rate = (Perpetual Price − Index Price) / Funding Interval

The more the perpetual deviates from spot, the larger the funding payment and the greater the incentive to rebalance. High positive funding can incentivize shorts to enter or longs to close, which pushes perpetual prices down. High negative funding has the opposite effect.

## Who pays whom: a simple example

Let's say Bitcoin spot is $50,000, but the perpetual futures contract is trading at $51,000 on a given exchange. The market is overbought; more traders are long perpetuals than short. The funding rate calculates to +0.10% per eight-hour period.

You hold a long perpetual position of 1 BTC (worth $51,000 notional). Every eight hours, you owe the shorts 0.10% of $51,000, which is $51. Over a day (three funding periods), you pay $153.

A trader who is short 1 BTC receives $51 every eight hours. This payment compensates the short for holding an underwater position in an overbought market.

For the short, this is attractive: they are making yield just by holding their short. Over time, shorts are attracted to the market, and more traders close long positions because they are bleeding funding. The perpetual price gradually falls back toward $50,000.

## The mechanics: premium index and index price

To calculate funding fairly, exchanges publish two reference prices:

1. **Perpetual mark price** or **spot price**: The actual traded price of the perpetual contract.
2. **Index price**: A fair-value estimate of the underlying asset, usually a weighted average of spot prices from major spot exchanges. Binance uses a median of prices from several spot markets; Deribit uses its own methodology.

The funding rate is derived from the difference between mark and index. Some exchanges also include an "interest rate component" reflecting the cost of borrowing (margin interest) in the calculation. A trader holding a leveraged long position is effectively borrowing collateral from the exchange or other traders; the interest rate component captures that cost.

## Funding rates as a sentiment indicator

Persistent positive funding rates signal that traders are aggressively long. Funding is positive when perpetuals are priced above spot because there is excess demand from longs. Traders who are contrarian or expect a pullback often view high positive funding as a sell signal: "The market is overheated; longs are overpaying; I should fade this."

Conversely, highly negative funding signals excess shorting and desperation among shorts. This can be a bullish signal for contrarians.

Some traders also use funding rates as a leading indicator of volatility. When funding rates are extreme (very positive or very negative), it often precedes a sharp reversal. The reason: funding accruals eventually force position holders to close or face unsustainable bleed.

Funds and institutions track funding rates across all major exchanges and use them to:
- Gauge retail sentiment (positive funding = retail is long).
- Identify basis trade opportunities (buy spot, short perpetual futures, collect negative funding).
- Assess tail risk (extreme funding can precede a cascade of liquidations).

## Basis trades and arbitrage

A professional trader might exploit a large gap between perpetual and spot by executing a basis trade:

1. **Buy spot** Bitcoin at $50,000.
2. **Short perpetual futures** at $51,000.
3. **Hold both** and collect the positive funding payments every eight hours.
4. **Close both** when the perpetual price converges toward spot.

The profit is the initial basis ($51,000 − $50,000 = $1,000) minus trading fees and borrowing costs. The perpetual trader also collects funding payments along the way. This is a low-risk arbitrage trade because the directional exposure is hedged.

Large traders and hedge funds run basis trades systematically, especially when funding is persistently positive. Their activity drives the perpetual price down over time, pulling it back toward spot.

## Liquidations and funding cascades

When funding rates are extremely positive (say, 1% per period), leverage traders holding longs are increasingly stretched. The funding bleed accelerates position erosion. If the price also drops slightly, margin calls trigger liquidations, which causes further selling and more liquidations—a cascade.

Similarly, extremely negative funding can force shorts into a cascade if the price rallies. The funding mechanism is designed to prevent persistent divergence, but periods of market stress can see large funding swings that trigger cascades before equilibrium is restored.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — Standard derivatives with expiration; perpetuals have no expiration
- [Basis](/basis/) — The difference between futures (or perpetual) price and spot price
- [Leverage](/leverage-ratio-forex/) — How traders use margin to amplify perpetual position size
- [Liquidation](/liquidation/) — Forced closure of positions when collateral falls below a threshold
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Venues where perpetual futures are traded
- [Volatility](/historical-volatility/) — Funding spikes often precede sharp price moves

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — Perpetuals are one tool for hedging or speculating
- [Market cycle](/market-cycle/) — Funding rates often signal late-cycle overbought conditions
- [Arbitrage](/forward-contract/) — Basis trades are arbitrage between perpetual and spot markets
- [Blockchain fundamentals](/blockchain-fundamentals/) — The underlying technology securing perpetual exchanges

</div>

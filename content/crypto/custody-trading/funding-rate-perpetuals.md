---
title: "Funding Rate in Perpetual Futures"
description: "The periodic cash flows that anchor perpetual contract prices to spot markets and equalize long and short leverage on exchanges."
keywords:
  - funding rate
  - perpetual futures
  - futures contracts
  - leverage trading
  - cryptocurrency derivatives
image: /svg/crypto.svg
---

*A **funding rate** is a periodic payment between long and short holders of a [perpetual futures](/futures-contract/) contract, designed to keep the contract price aligned with the spot market price. When longs outnumber shorts (bullish bias), longs pay shorts; when shorts dominate, shorts pay longs. This self-balancing mechanism replaces the fixed expiration of traditional [futures](/futures-contract/) and allows contracts to trade indefinitely without a delivery date.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Funding Rate — Perpetual Futures Self-Balance</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency derivatives trading." />

<div class="wiki-infobox-caption">A cost to holding imbalanced positions; a subsidy for balanced ones.</div>

|   |   |
|---|---|
| **What it is** | Periodic payment (8-hour intervals, typically) between long and short futures holders |
| **Who pays** | The side (long or short) that dominates the open interest |
| **Amount** | Varies: 0.01% to 0.1% per funding period, or higher in extreme markets |
| **Purpose** | Anchors perpetual price to spot market; incentivizes balance |
| **Key mechanic** | Positive funding (longs pay): price above spot; negative funding (shorts pay): price below spot |

</aside>

## Why perpetuals need anchoring

Traditional [futures contracts](/futures-contract/) have an expiration date. A March wheat future expires on a specific day, after which physical delivery or cash settlement resolves the contract. Until that date, the future's price can diverge from the spot price, but once expiration arrives, they converge by force.

Perpetual futures, created in crypto to serve 24/7 trading, have no expiration. A Bitcoin perpetual that you buy today can stay open indefinitely. Without an expiration to force convergence, the contract price could drift away from the spot price indefinitely. Imagine Bitcoin spots at USD 65,000, but the perpetual trades at USD 64,000 and stays there for weeks. Arbitrage would be perfect (buy cheap perpetual, short spot, lock a risk-free profit) but liquidity and fees make it slow.

The funding rate is the solution. Rather than waiting for an expiration date to enforce convergence, the exchange builds in a periodic payment that incentivizes traders to close imbalanced positions or add to underweighted sides.

## How it works: payment mechanics

Most cryptocurrency exchanges calculate a funding rate every 8 hours and settle it on the same schedule. The formula varies, but the logic is consistent: if the perpetual price is above the spot price (a "premium"), the funding rate is positive; if below spot (a "discount"), it's negative.

A positive funding rate of 0.05% means longs pay shorts 0.05% of their position notional value. A trader holding 10 Bitcoin (notional value 650,000 USD) long pays 325 USD to the shorts. This payment is made via the exchange's clearing mechanism, not peer-to-peer; the exchange pools payments from the side that pays and distributes them to the side that receives.

The magnitude of the funding rate depends on how far the perpetual has drifted from spot. If perpetual is 2% above spot, the funding rate might be 0.1% per 8-hour period. If it's 1% above, funding might be 0.05%. The exact calculation is set by the exchange, but the principle is: the bigger the drift, the higher the cost to the imbalanced side, and thus the stronger the incentive to correct it.

## The incentive to balance

When funding is positive (longs paying), short holders are profiting just by holding their position. This attracts new shorts or encourages longs to exit or switch sides. Eventually, the open interest evens out, shorts decrease relative to longs, and the perpetual price drops back toward spot. Funding rate then falls, and the incentive weakens. Equilibrium is restored, not by force, but by profit-seeking.

Conversely, when funding is negative (shorts paying), longs are subsidized, and shorts must pay. New longs enter, seeking free money. Shorts exit or reduce size. The perpetual price rises back toward spot. Again, the mechanic is elegant: the market balances itself via profit incentives.

This is different from traditional futures, where such imbalances are usually small because traders know the contract expires soon. In perpetuals, without an expiration, the funding rate is the only mechanism keeping price and spot tethered.

## Extreme funding rates and leverage feedback loops

In abnormally volatile markets, funding rates can spike dramatically. During a euphoric rally, everyone is long, and funding might hit 1% or more per 8-hour period (3% annualized or higher on a single interval). This sounds like a subsidy to shorts, but it's actually a warning sign: the market is extremely one-sided.

In such moments, leverage bets are exaggerated. Retail and some institutional traders are borrowed-up, holding massive long positions at high [leverage](/leverage-ratio-forex/). If volatility spivers upward and prices drop, these longs get liquidated (forced closed at a loss by the exchange because their margin is exhausted). This triggers a cascade: liquidations sell into the market, pushing price down further, forcing more liquidations. The high funding rate that should attract shorts instead amplifies the crash.

Responsible exchanges have safeguards: circuit breakers, position limits, and [liquidation](/liquidation/) buffers. But in extreme moves, funding rates reveal the fragility of a market built largely on leverage.

## Arbitrage and funding

A savvy trader can profit from funding rates without directional bets. Suppose Bitcoin perpetual is trading at a 0.2% premium to spot (meaning funding is positive), and the funding rate is 0.05% per 8 hours. A trader buys spot Bitcoin and shorts the perpetual for the same notional amount. They lock in the 0.2% premium minus trading fees and financing costs. Over the next 8 hours, they collect 0.05% funding on the short position while holding the spot. If they unwind at the same prices, they profit the funding rate minus fees.

This is called "funding arbitrage" and is a core activity of crypto market makers and algorithmic firms. It requires capital (to hold both spot and margin), low fees (most traders pay 0.1% per trade or less), and tight management (to avoid being caught if prices move before funding is paid). But it is relatively low-risk profit.

The presence of arbitrage traders keeps funding rates from exploding too high and keeps perpetual prices honest. If funding gets too expensive, arbitrage becomes profitable, capital flows in, and the spread narrows.

## Structural biases: longs typically dominant

Over time, cryptocurrency funding rates tend to be positive more often than negative, meaning longs pay shorts on average. This reflects a structural reality: in bull markets, longs accumulate and dominate open interest. During bear markets, shorts do dominate, but for shorter durations. The asymmetry is cultural—cryptocurrency has a community narrative of long-term bullishness—but also rational: long-term hodling is simpler than short-selling in crypto (shorting requires borrowing, is riskier, and is restricted or unavailable on many exchanges).

This means that shorts, on average, collect more funding than longs pay. Some strategies are built around this: collecting funding by holding short positions in a sideways market. But it also means bullish rallies tend to be steeper (longs are paying to hold, so they hold more comfortably) and bearish drops tend to be sharper (shorts unwind faster when stops are hit).

## Funding rates as a sentiment gauge

Traders watch funding rates as a sentiment indicator. Extremely high positive funding (longs paying heavily) suggests the market is extremely bullish and possibly overleveraged. Extremely negative funding (shorts paying) is rare but suggests pessimism. Many trading strategies include a filter: avoid selling/shorting when funding is extreme positive, or avoid buying/going long when it's extreme negative, because mean reversion tends to follow.

For institutions managing large holdings, funding rates are a trading cost but also an asset. A [hedge fund](/hedge-fund/) holding a long spot position can short perpetuals to hedge, earning funding in the process. A [business development company](/business-development-company/) or treasury holding Bitcoin might do the same for yield enhancement (though this is contentious from a risk perspective; the yield subsidizes unwind risk).

## Variations across exchanges

Not all exchanges use the same funding formula. Some use the premium index (the difference between perpetual and spot prices) as the primary input. Others incorporate a "interest rate" component reflecting the cost of borrowing margin. Some have variable settlement intervals (1 hour, 4 hours, 8 hours, 24 hours). The specific mechanics can affect whether funding is stable or volatile.

Traders often compare funding rates across exchanges and migrate volume to venues with more favorable rates. An arbitrageur might hold spot on a low-funding-rate exchange and short on a high-funding exchange, collecting the spread. This capital flow between venues tends to equalize funding rates over time, though lags and differences in leverage availability keep them from converging perfectly.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — The traditional contract with expiration, of which perpetuals are a variant.
- [Perpetual Futures](/futures-contract/) — Contracts without expiration date, core to crypto derivatives.
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Venues where perpetuals trade.
- [Crypto Market Microstructure](/crypto-market-microstructure/) — How fragmented crypto venues shape pricing.
- [Leverage (Forex)](/leverage-ratio-forex/) — The borrowed capital that amplifies gains and losses.

### Wider context

- [Price Discovery](/price-discovery/) — How market mechanisms anchor prices to fundamentals.
- [Market Maker (Trading)](/market-maker-trading/) — Liquidity providers who exploit funding inefficiencies.
- [Liquidation](/liquidation/) — The forced closure of overleveraged positions.
- [Arbitrage](/price-discovery/) — Risk-free profit from price discrepancies.

</div>

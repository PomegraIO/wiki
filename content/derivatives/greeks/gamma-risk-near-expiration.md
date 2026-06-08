---
title: "Gamma Risk Near Expiration"
description: "Gamma risk in options accelerates near expiration as delta becomes more volatile. Learn why gamma spikes in final days and what it means for hedging."
keywords:
  - gamma risk options near expiration
  - gamma spike expiration
  - delta sensitivity options
  - options gamma decay
image: "/svg/derivatives.svg"
---

*As expiration approaches, **gamma risk** — the rate at which delta changes — can multiply ten-fold or more in just days. For traders holding positions near expiration, this amplified sensitivity to underlying price moves forces constant rehedging and inflicts real P&L swings even in quiet markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma Risk — the acceleration factor</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Gamma magnifies with time decay; expiration turns it into a daily bleed.</div>

|   |   |
|---|---|
| **What it is** | Rate of change of [delta](/delta/) per 1-point move in the underlying |
| **Why it matters** | Forces rehedging and creates P&L surprises as expiration nears |
| **Peak timing** | Last 7–14 days, most acute on expiration day |
| **Risk direction** | Short gamma means you lose on big moves; long gamma profits on volatility |
| **Hedging cost** | Buying [options](/option/) to hedge gamma costs [vega](/vega/) exposure and [theta](/theta/) bleed |

</aside>

## How gamma accelerates as time runs out

Gamma is always positive for the buyer and negative for the seller. For most of an option's life, gamma rises modestly as the underlying drifts near the strike; it peaks when the option lands at-the-money, then falls symmetrically as it moves out-of-the-money.

But time compresses gamma in the final month. An at-the-money call with 60 days to go might have gamma of 0.01 — meaning each 1-point move in the underlying changes delta by 0.01. With 30 days left, gamma on the same position doubles to 0.02. With 7 days, it triples again to 0.06. On expiration day itself, gamma can spike to 0.20 or higher for near-the-money strikes.

The mathematics is unforgiving: as calendar days drain away, the same percentage change in the underlying translates to a larger percentage change in delta. An option with ten days to expiration is hyper-sensitive; a 2% move in the stock becomes a sharp delta revaluation.

## Why this forces constant rehedging

Suppose you sold a call ten days before expiration. You delta-hedge it by buying stock at a 1:1 ratio. The next day, the stock drops 1%. Your call's delta might swing from −0.60 to −0.45. Your hedge is now 15% overweight — you own too much stock relative to your short call exposure. You must sell part of the hedge to rebalance.

But here is the trap: if the stock falls another 1% the following day, your delta drops again, forcing you to sell more. Yet if the stock rises even 1%, delta surges, and you must buy back. In the last days before expiration, near-the-money options often see gamma-driven hedge rebalancing every single trading session — and sometimes multiple times per day if the underlying is volatile.

Each rebalancing incurs [bid-ask spreads](/bid-ask-spread/) and transaction costs. Over ten days, those micro-losses accumulate. A trader short gamma near expiration is grinding money into the bid-ask spread with every hedge transaction.

## The asymmetry between buyers and sellers

Long options (the buyer) benefits from gamma near expiration because positive gamma means delta adjusts in the position's favor. If you own a call and the stock surges 2%, your delta increases from 0.60 to 0.85 — your payoff amplifies without you lifting a finger. Gamma is your ally; it is a free convexity.

Short options (the seller) suffers the inverse. Each unexpected move forces you to rebalance at an unfavorable price. The more volatile the underlying in the final week, the more you are forced to buy high and sell low. Short gamma positions near expiration are short volatility in the most concrete sense: you lose money on big moves and gain only the [theta](/theta/) decay if the underlying stays put.

This is why [implied volatility](/implied-volatility/) often spikes into expiration — short gamma holders demand compensation for the bleed, driving up the price of options themselves.

## Expiration day: when gamma becomes infinite

On the last trading day, gamma reaches an extreme. An out-of-the-money option has gamma approaching zero — a tiny move in the underlying won't change delta from 0.0 (worthless). But an at-the-money option has gamma effectively infinite: a 1-point move determines whether you finish in-the-money or out. Delta jumps from near 0.5 to near 1.0 or vice versa.

At this point, option pricing is almost pure intrinsic value. Trading volume can collapse as liquidity dries up. Market makers pull bids and asks wider because the gamma risk is too acute. A trader caught in a large position expiring at-the-money may find that a market order creates a slippage cost far exceeding the spread that was quoted moments earlier.

For index options or equity options with official expiration settlement, the final hour can witness erratic price discovery as market participants sort out their gamma exposure and cash settlement mechanics.

## Gamma risk in position sizing and strategy

A trader managing gamma risk near expiration must ask: how much can the underlying move before my hedge breaks? If you are short 100 calls on a $100 stock with two weeks left, a 5% move (to $105) might push delta from −0.60 to −0.80, creating a $20 loss per share on your short call position and requiring $2,000 in new hedge trades. Multiply that across several expiration series, and gamma risk becomes a significant P&L drag.

Many sophisticated traders reduce exposure in the final week explicitly to avoid gamma bleed. A long calendar spread — selling a near-term option and buying a further-dated one — is a classic way to profit from theta while limiting gamma risk; the short leg's gamma is offset somewhat by the long leg's positive gamma.

Conversely, volatility-focused traders sometimes add long positions specifically to harvest gamma near expiration, betting that realized volatility will exceed the implied volatility they paid for the option.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — rate of change of option value per 1-point move in the underlying
- [Theta](/theta/) — time decay; accelerates in final 30 days
- [Vega Exposure: Long vs Short Options](/vega-exposure-long-vs-short-options/) — how implied volatility affects positions
- [Options](/option/) — contract to buy or sell at a fixed strike
- [Implied Volatility](/implied-volatility/) — market's expectation of future price swings

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — framework for managing option risk
- [Time Decay Rate by Days to Expiry](/theta-decay-rate-by-days-to-expiry/) — theta accelerates alongside gamma
- [Option Premium](/option-premium/) — what you pay for gamma and theta
- [Volatility Smile](/volatility-smile/) — how gamma varies across strikes

</div>
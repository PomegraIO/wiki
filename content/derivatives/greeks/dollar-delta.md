---
title: "Dollar Delta"
description: "Delta scaled by the spot price to express the option's directional exposure in notional dollars rather than as a rate of change per dollar of spot movement."
keywords:
  - dollar delta
  - notional exposure
  - delta scaling
  - option greeks
  - derivatives hedging
image: "/svg/derivatives.svg"
---

*Dollar delta transforms [delta](/delta/) from a fractional sensitivity into an absolute dollar amount. It is the [delta](/delta/) multiplied by the spot price—the notional directional exposure of the position. For a trader managing a portfolio in dollar terms, dollar delta answers the question: "How many dollars do I gain or lose per dollar move in the underlying?"—directly translating greek sensitivity into P&L intuition.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dollar Delta — notional directional exposure</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and pricing mechanics." />

<div class="wiki-infobox-caption">Delta scaled to dollars, the most intuitive measure of position risk in absolute terms.</div>

|   |   |
|---|---|
| **What it is** | Δ × S, delta multiplied by the spot price |
| **Units** | Dollars (or local currency) per unit move in spot |
| **Also called** | Notional delta, position delta, buck delta |
| **Relation to delta** | Dollar delta = Delta × Spot Price × [Shares per contract]/[Shares per contract] |
| **Key use** | Portfolio hedging; risk reporting; multi-asset comparisons |
| **Sign** | Positive for long calls/short puts; negative for short calls/long puts |

</aside>

## From rate of change to notional exposure

[Delta](/delta/) is a rate of change: a call option with delta 0.6 gains $0.60 for every dollar the underlying spot price rises. But managing a trading desk or risk book in practice requires thinking in absolute dollars, not fractional rates. If a trader owns 100 call contracts, each with delta 0.6, on a spot price of $100, the portfolio's [delta](/delta/) is 60, but what does that number actually mean for P&L?

Dollar delta answers the question by making the calculation concrete. The 100 contracts have a total notional directional exposure of 60 × $100 = $6,000. If the spot rises $1, the position gains $6,000. This is dollar delta in its simplest form: the notional amount of the underlying asset that the position effectively mimics.

## Calculating dollar delta

The formula is deceptively simple:

Dollar Delta = Delta × Spot Price

For a single option contract:

DD = Δ × S

where Δ is the option's [delta](/delta/) (a number between −1 and 1 for European options, between −1 and 0 for puts and 0 and 1 for calls) and S is the current spot price of the underlying.

For a portfolio of multiple positions across strikes and expirations:

Portfolio Dollar Delta = Σ(Δ_i × S_i × Contracts_i)

where the sum runs over all option contracts. This aggregation is straightforward and is a standard output in any institutional risk system.

## Why dollar delta matters more than delta alone

A [delta](/delta/) of 0.4 sounds like a weak directional exposure—40% of a pure long position. But if the underlying is a stock trading at $500 per share, that 0.4 delta on 1,000 contracts represents 400 × 1,000 shares = 400,000 shares worth of directional exposure, or $200 million notional—a massive position that would require enormous hedging.

Conversely, a single deep-in-the-money call option on a $2 stock with delta 0.99 sounds almost like a pure long stock position, but its dollar delta is only $0.99 per contract—negligible if only one contract is held.

Dollar delta is therefore the preferred metric for:

- **Cross-asset comparisons**: A trader managing both equity options and commodity futures needs a common language. Dollar delta on the equity book and dollar delta on the commodity book can be directly summed and compared.
- **Hedging calculations**: If a trader has a long dollar delta position of $10 million and wants to flatten it, she knows she needs to short $10 million notional of the underlying (or enter short futures/forwards of equivalent notional).
- **Risk limits**: Portfolio managers and risk officers typically set limits not on [delta](/delta/) but on notional directional exposure. A desk might be authorized to carry up to $50 million long dollar delta at any time; dollar delta provides immediate visibility into that limit.

## Dollar delta across underlyings of different scales

The power of dollar delta shines in heterogeneous portfolios. Consider a desk holding:

- 100 call option contracts on Apple stock (spot $150, each contract delta 0.5): dollar delta = 0.5 × 150 × 100 = $7,500.
- 10 call contracts on the S&P 500 index futures (spot 4,500, each contract delta 0.7): dollar delta = 0.7 × 4,500 × 10 = $31,500.
- 50 call contracts on crude oil (spot $80/barrel, each contract delta 0.3): dollar delta = 0.3 × 80 × 50 = $1,200.

The portfolio's total dollar delta is $7,500 + $31,500 + $1,200 = $40,200. The desk is net long $40,200 notional across all three asset classes. If the trader wants to reduce directional risk, she knows precisely how much notional to short: $40,200. [Delta](/delta/) alone would have given three separate, hard-to-compare numbers (0.5, 0.7, 0.3); dollar delta unifies them in economic terms.

## Dollar delta and hedging efficiency

When a portfolio manager wants to hedge directional exposure, dollar delta guides the sizing. If a trader holds $50 million notional of long equity risk (positive dollar delta) and wants to hedge it with SPY put options, she first computes the dollar delta of each put contract, then sizes the position such that the put's negative dollar delta offsets the $50 million long exposure.

More broadly, dollar delta is the currency of [hedge fund](/hedge-fund/) and [mutual fund](/mutual-fund/) rebalancing. A fund's dollar delta across all holdings (equities, options, futures, bonds) is its net directional exposure. When markets move, the fund's dollar delta drifts; rebalancing typically targets a dollar-delta band (e.g., maintain net long exposure between $0 and $5 million).

## Dollar delta versus notional and contract multipliers

Dollar delta is not identical to notional exposure when the contract structure involves multipliers. For a single stock option contract in the US, the standard multiplier is 100 shares. A call option with [delta](/delta/) 0.5 on a $100 stock has dollar delta of 0.5 × $100 = $50 per contract, but the notional exposure of the position is $50 × 100 = $5,000 (one contract controls 100 shares).

Most trading systems account for this distinction by tracking both dollar delta (the greeks-derived measure) and notional (the actual underlying quantity controlled). The two are related by the contract multiplier, but they answer different questions: dollar delta measures spot-price risk; notional measures the quantity of underlying you can buy or sell with the capital freed up if you closed the option position.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the foundational greek, expressed as a rate of change per dollar of spot
- [Gamma](/gamma/) — convexity in delta itself, the rate of change of dollar delta
- [Vega](/vega/) — volatility sensitivity, another key greek for options
- [Dual Delta](/dual-delta/) — sensitivity to strike price shifts in the Black-Scholes framework
- Hedge — the core application of dollar delta in risk management

### Wider context

- [Option](/option/) — the fundamental derivative whose risk dollar delta measures
- Greeks — the broader family of option sensitivities
- Portfolio Risk — how dollar delta aggregates across a book
- Notional Exposure — the quantity of underlying at risk

</div>
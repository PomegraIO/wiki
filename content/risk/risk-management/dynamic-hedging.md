---
title: "Dynamic Hedging"
description: "Continuously rebalancing hedges as underlying prices shift to maintain delta neutrality and lock in option profit."
keywords:
  - delta hedging
  - rebalancing
  - options hedge
  - delta neutral
  - portfolio rebalancing
  - derivatives risk
image: /svg/risk.svg
---

*A **dynamic hedge** is a strategy in which a portfolio manager continuously rebalances a derivative position or its underlying to maintain [delta](/delta/) neutrality as prices move. Rather than set a hedge once and forget it, dynamic hedging requires active adjustment—selling when the underlying rises, buying when it falls—to keep net exposure flat and lock in the option's profit.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dynamic Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management topics." />

<div class="wiki-infobox-caption">The art of staying delta-neutral as markets move.</div>

|   |   |
|---|---|
| **What it is** | Continuous rebalancing of a hedge to maintain a target exposure (usually zero delta) |
| **Why it matters** | Locks in option [fair value](/fair-value/) and isolates [gamma](/gamma/) profit from directional moves |
| **When it's hard** | Near [expiry](/expiration-date/), in gaps, with large [gamma](/gamma/) positions, or when [bid-ask spreads](/bid-ask-spread/) are wide |
| **Cost source** | Transaction costs, [bid-ask spread](/bid-ask-spread/) slippage, and the cost of covering realized vs. unrealized hedging losses |
| **Historical note** | Formalized by Black, Scholes, and Merton; central to modern options trading since the 1970s |

</aside>

## How dynamic hedging isolates gamma profit

An [option](/option/) holder benefits from [volatility](/historical-volatility/) through [gamma](/gamma/)—the profit from buying low and selling high as prices bounce. Static hedging (buy once, hold) forces the portfolio to carry directional risk; dynamic hedging neutralises that risk through constant rebalancing, allowing the trader to harvest gamma without betting on direction. If you sell an option, dynamic hedging lets you lock in your selling price by buying the moves you're short of.

The math is clean: if you sell an option, you are short [vega](/vega/) (volatility), but you have positive [gamma](/gamma/). By selling the underlying when it rises and buying when it falls, you realise the gains from that gamma—turning it into cash—without ever admitting to a view on where prices are headed. The profit comes purely from the gap between realised [volatility](/historical-volatility/) and the [implied volatility](/implied-volatility/) you sold.

## The practical reality: continuous costs

In theory, hedging infinitely often costs nothing (you scalp infinitesimal moves). In practice, hedging is lumpy and expensive. Every trade incurs a [bid-ask spread](/bid-ask-spread/), commissions, or (in a large portfolio) market impact. A high-frequency trader in S&P 500 futures might hedge a 10,000-contract option book dozens of times per hour; a hedge fund selling a multi-year volatility product might hedge daily or weekly. The less frequently you rebalance, the more your [gamma](/gamma/) profit is eaten by realised moves; the more often you rebalance, the more you pay in transaction costs.

This trade-off sits at the heart of derivatives profitability. Major banks price options by assuming a rebalancing cadence—daily, hourly, or continuous—and charge a spread that covers their estimated hedging costs plus their [risk](/operational-risk/) of being unable to hedge (in a gap or market crash). When you buy a widely-quoted option, you are implicitly paying the dealer's hedging cost.

## Gamma risk and rebalancing near expiry

[Gamma](/gamma/) explodes as [expiration](/expiration-date/) approaches, especially at-the-money. A tiny price move changes delta dramatically, forcing outsized hedging trades. Imagine you have sold an at-the-money call with one day to expiry and positive [gamma](/gamma/). The underlying bounces 1%. Your delta has swung by 50 contracts. You now owe a [hedge](/dynamic-hedging/) that is large relative to what the option is worth; you're forced to pick between accepting [gamma](/gamma/) losses or paying dearly to rebalance.

This is why [option](/option/) traders fear gamma the most on the final days before [expiry](/expiration-date/). Large [gamma risk](/gamma-risk/) can turn a profitable trade into a loss if price moves are large and the trader is slow or forced to execute at bad prices. In 1987 and again in 2008, when markets gapped across trading halts, dynamic hedgers found themselves holding massive unhedged positions—a lesson in the fragility of continuous assumptions.

## Funding and liquidity constraints

Dynamic hedging assumes you can trade whenever you want. If the underlying is illiquid, or if your position is large relative to typical market depth, you face a dilemma: the cost of hedging grows, and you may be forced to hedge at poor prices or accept unhedged [gamma](/gamma/) risk. This is especially acute for firms with [leverage](/leverage-ratio-forex/) and tight funding—they may be forced to abandon hedging during stress (see [funding liquidity risk](/funding-liquidity-risk/)).

A classic example: a dealer shorts volatility on an emerging-market currency. As the currency falls, [gamma](/gamma/) eats the position, and the dealer needs to sell the currency to hedge. But in a crisis, the currency is illiquid and the dealer has no funding to post collateral. The hedge that should have kept them safe never happens.

## When static hedging is preferable

Not every derivative position needs dynamic hedging. If you hold a long-dated, out-of-the-money [put option](/put-option/) for true catastrophic [risk](/tail-risk/), rebalancing constantly to maintain delta neutrality defeats the purpose—you own the hedge for direction, not gamma. Similarly, if [bid-ask spreads](/bid-ask-spread/) are very wide (in a crisis), the cost of rebalancing may exceed the value you're protecting.

Many corporate treasurers and smaller hedge funds use static hedging instead: buy a [put](/put-option/) or [put spread](/put-option/), hold it, and accept the directional risk. The trade-off is simplicity and low turnover against a higher hedge cost upfront. For large derivatives books, though, where [leverage](/leverage-ratio-forex/) and capital efficiency matter, dynamic hedging is the standard—it saves the firm money and keeps it delta-neutral.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma Risk](/gamma-risk/) — the acceleration of delta change that makes hedging harder
- [Delta](/delta/) — the rate of change of an option price with respect to the underlying
- [Vega](/vega/) — sensitivity to volatility, the other key option greek
- [Option Premium](/option-premium/) — what you pay to buy protection or receive for selling it
- [Volatility Smile](/volatility-smile/) — why implied volatility varies by strike, complicating hedges
- [Fair Value](/fair-value/) — the theoretical price a dealer locks in through hedging
- [Bid-Ask Spread](/bid-ask-spread/) — transaction costs that erode hedging profit
- [Leverage Ratio](/leverage-ratio-forex/) — how much borrowed capital constrains hedging ability

### Wider context

- Derivatives Risk — the full landscape of risks in options and futures
- [Options](/option/) — the instrument being hedged
- [Hedge Fund](/hedge-fund/) — institutions that often run sophisticated hedging programs
- [Black-Scholes Model](/black-scholes-model/) — the mathematical foundation for option pricing and hedging

</div>

---
title: "Delta (Option Greeks)"
description: "The sensitivity of an option's price to changes in the underlying asset's price, expressed as a ratio between 0 and 1."
keywords:
  - option greeks
  - delta hedging
  - option pricing
  - price sensitivity
---

*The **Delta** of an [option](/wiki/option/) measures how much its price will move for every dollar the underlying asset moves—and it is the first line of defense for anyone managing [option](/wiki/option/) portfolios or running hedges.*

<aside class="wiki-infobox">

| Metric | Value |
|---|---|
| Formula | Change in option price ÷ Change in asset price |
| Range | 0 to 1 (calls); -1 to 0 (puts) |
| Practical range | 0.01 to 0.99 |
| Interpretation | Shares of underlying held equivalent |
| Time decay impact | Increases as expiration nears (ITM) |

</aside>

## Delta as a hedge ratio

Delta is the most practical of the [option Greeks](/wiki/options-greeks/). It answers a deceptively simple question: if the stock moves up $1, how much will the option gain or lose? For a [call option](/wiki/call-option/) with a delta of 0.60, each $1 rise in the underlying generates a $0.60 gain in the option's value. For a [put option](/wiki/put-option/) with a delta of -0.60, that same $1 rise triggers a $0.60 loss.

This is why delta is often called the "hedge ratio." If you own 100 shares of a stock trading at $50 and you sell a call with a delta of 0.50, you have effectively reduced your upside exposure. The 100 shares are +1.0 delta (100% sensitivity), and the short call is -0.50 delta, netting to +0.50 delta—equivalent to owning only 50 shares of outright exposure.

## Delta across the strike prices

At-the-money (ATM) options have a delta near 0.50, meaning they are equally likely to expire in or out of the money (under the [Black-Scholes](/wiki/black-scholes-model/) framework). Deep in-the-money (ITM) [calls](/wiki/call-option-equity/) approach a delta of 1.0—they move nearly dollar-for-dollar with the stock because exercise is almost certain. Far out-of-the-money (OTM) options approach zero delta; a $1 move in the underlying barely affects their value.

This non-linearity is crucial. A call at strike $40 when the stock trades at $60 has a delta near 1.0 and behaves like stock. A call at strike $80 has a delta near 0.05 and behaves like a lottery ticket. The same $5 stock move affects each very differently.

## Volatility and time to expiration drive delta

Delta is not fixed. It shifts with [volatility](/wiki/volatility-index-option/) and time. Higher volatility pushes OTM option deltas up (more probability mass in the tails), while lower volatility pushes them down. As expiration approaches, time decay ([theta](/wiki/theta-option-greeks/)) accelerates. An ATM option with one day to expiration has a delta closer to 0.50, but as expiration nears, it converges sharply to either 0 or 1 depending on whether it is above or below the strike. A $0.01 move in the stock can swing the delta from 0.49 to 0.95 in the final hours.

## Delta in portfolio hedging

Institutional traders use delta to manage overall portfolio direction. A long stock position (positive delta) can be partially hedged with [put options](/wiki/protective-put/) (negative delta) or short calls (negative delta) to reduce net exposure. An arbitrageur running [merger arbitrage](/wiki/merger-arbitrage/) might be long the acquisition target (positive delta) and short the acquirer (negative delta), betting on deal closure while keeping directional risk near zero.

[Dynamic hedging](/wiki/dynamic-hedging-algorithm/) means rebalancing the hedge continuously as delta changes—buying and selling the underlying to keep net delta constant. This is how [market makers](/wiki/market-makers/) stay flat; they are delta-neutral on average and profit from [bid-ask spreads](/wiki/bid-ask-spread/) and volatility rather than direction.

## Gamma: the delta of delta

Delta itself changes—that change is measured by [gamma](/wiki/gamma-option-greeks/). A call with a gamma of 0.05 means for every $1 the stock moves, the delta itself rises (or falls) by 0.05. Gamma is highest for ATM options and near expiration, where delta is most sensitive. When gamma is high, your hedge ratio becomes unstable; you must rebalance frequently to stay hedged. When gamma is low, delta is steady and hedging is less urgent.

## Practical uses in trading

Short-dated options (weeklies, monthlies) have high gamma and unstable deltas, making them hard to hedge dynamically—each $0.50 move in the stock can swing the delta 0.10 or more. Long-dated options (LEAPS) have stable deltas that shift gradually, making them easier to use as directional hedges. Traders who sell premium ([short calls](/wiki/covered-call/), [iron condors](/wiki/iron-condor/)) keep close watch on delta because it tells them their maximum gain (if delta goes to zero) and maximum loss (if delta goes to -1.0).

## Myth: delta equals probability

A common misconception is that a delta of 0.60 means "60% probability the option expires in the money." This is almost true under certain models but not exact in reality. Delta is the hedge ratio first; the probability interpretation is secondary and assumes particular distributional assumptions that may not hold in the market. Different volatility surfaces and jump-risk models yield different probabilities for the same delta. Use delta as a hedge ratio, not as a substitute for [implied volatility](/wiki/implied-volatility/) analysis.

<div class="wiki-seealso">

### Closely related
- [Options Greeks](/wiki/options-greeks/) — the full suite of sensitivities (gamma, theta, vega, rho).
- [Gamma (Option Greeks)](/wiki/gamma-option-greeks/) — the rate of change of delta.
- [Call Option](/wiki/call-option-equity/) — a long-delta instrument.

### Wider context
- [Black-Scholes Model](/wiki/black-scholes-model/) — theoretical foundation for delta and option pricing.
- [Implied Volatility](/wiki/implied-volatility/) — shifts affect delta across all strikes.
- [Dynamic Hedging Algorithm](/wiki/dynamic-hedging-algorithm/) — continuous rebalancing to maintain delta neutrality.

</div>

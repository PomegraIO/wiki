---
title: "Risk-Neutral Pricing"
description: "The foundational theorem that derivatives are priced by discounting expected payoffs under a risk-neutral probability measure, not real-world probabilities."
keywords:
  - risk-neutral measure
  - martingale pricing
  - no-arbitrage principle
  - derivative valuation
  - discount factor
image: /svg/derivatives.svg
---

*The **risk-neutral pricing** principle states that a derivative's fair value equals the discounted expectation of its payoff, where expectations are computed under a risk-neutral (or equivalent martingale) measure, not the actual real-world distribution of outcomes. This theorem decouples valuation from investor risk preferences and forms the bedrock of modern derivatives mathematics.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk-Neutral Pricing — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">The no-arbitrage argument that bypasses investor preferences entirely.</div>

|   |   |
|---|---|
| **What it is** | A valuation principle using risk-neutral probabilities rather than real probabilities |
| **Also called** | Martingale pricing, equivalent martingale measure, risk-neutral measure |
| **Core insight** | Investor risk aversion doesn't directly affect derivative prices |
| **Key theorem** | Fundamental Theorem of Asset Pricing: no arbitrage ↔ equivalent martingale measure exists |
| **Standard application** | [Option](/option/) pricing, [interest-rate](/interest-rate/) derivatives, [futures](/futures-contract/) |
| **Contrast** | Real-world pricing uses actual probabilities; risk-neutral pricing uses "synthetic" adjusted probabilities |

</aside>

## The intuition: why investor risk appetite drops out

Most people assume that if you believe a stock is equally likely to rise or fall tomorrow, you should pay an expected-value price for a [call option](/call-option/) on it. But that logic misses a crucial fact: the option holder can hedge away risk. If you own a call and short some amount of the underlying stock, you create a riskless position—one that should earn only the [interest-rate](/interest-rate/) (the risk-free rate). That arbitrage-free constraint forces the option price to a specific level *regardless of whether you personally fear or love risk*. The risk-neutral measure is simply the probability distribution that makes the risky asset's expected return equal to the risk-free rate, ensuring that the [discount-rate](/discount-rate/) always matches the risk-free rate.

## The Fundamental Theorem and the measure

The **Fundamental Theorem of Asset Pricing** (proved rigorously by Harrison and Pliska in 1981) establishes that a market is free of arbitrage if and only if at least one **equivalent martingale measure** exists. Under this measure, the discounted price of every traded asset is a martingale—meaning its expected value tomorrow (discounted to today) equals its price today. When such a measure exists, you can price any derivative by taking the expected payoff under that measure and discounting at the risk-free rate.

Here's the power: you don't need to know an investor's actual beliefs about future prices, and you don't need to estimate a [risk-premium](/), because the martingale measure is *not* the real-world distribution. It's an adjusted probability that makes the math work: mathematically, it inflates the odds of down moves just enough that the expected return matches the risk-free rate. This synthetic weighting sidesteps the need to estimate the historical equity [premium](/), which is notoriously hard to pin down.

## Applications in practice

For [equity options](/call-option/), the standard tool is the **Black-Scholes-Merton formula**, derived by computing expected payoffs under the risk-neutral measure (in that case, log-normal). For **[bond options](/option/)** and [interest-rate](/interest-rate/) derivatives, practitioners move to different numeraires—for example, a **[forward measure](/forward-measure/)** using a zero-coupon bond as the base unit—and recompute under the corresponding martingale measure for that choice.

The same principle applies to [credit derivatives](/), [commodity](/crude-oil/) futures, and [currency](/canadian-dollar/) swaps: once you identify the right martingale measure for each asset class, you can price any contingent claim by integration and discounting. This universality is why risk-neutral pricing is sometimes called the "trick that made derivatives pricing possible."

## Why this isn't just mathematical sleight of hand

A common objection: "If risk-neutral probabilities aren't real, how can they give correct prices?" The answer is that the market itself enforces the correspondence. If you try to sell a derivative cheaper than its risk-neutral price, a trader can buy it, hedge it with spot and forward contracts, and pocket an arbitrage profit. Conversely, if you try to buy cheaper than risk-neutral, you'd leave money on the table by selling and hedging. Over time, market competition drives prices to the risk-neutral level *because that's where hedging breaks even and no arbitrage exists*.

The real-world probabilities matter for *forecasting* the asset's performance and understanding tail risk—they inform [value-at-risk](/value-at-risk/) models and risk management. But for valuation of liquid derivatives that can be hedged, real-world beliefs are irrelevant; only the risk-free rate, [volatility](/historical-volatility/), and the no-arbitrage condition matter.

## Limitations and when it breaks down

Risk-neutral pricing assumes you can trade continuously and frictionlessly, that markets are complete (every claim is replicable), and that there is a single [interest-rate](/interest-rate/). Real markets have [bid-ask spreads](/bid-ask-spread/), jump gaps, margin requirements, and funding constraints. When the market is incomplete or illiquid—say, a long-dated [interest-rate](/interest-rate/) swaption with few counterparties—multiple martingale measures may coexist, and prices depend on [counterparty-risk](/counterparty-risk/), funding costs, and dealer constraints.

Additionally, the risk-neutral measure is *not* the statistical measure. Over decades, equities have earned a risk premium above the [interest-rate](/interest-rate/), driven by real economic risk. Confusing the two—using risk-neutral probabilities for long-term forecasting, or assuming that implied volatilities from options represent investors' true forecast uncertainty—is a frequent source of error.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — financial contract priced via risk-neutral expectation
- [Forward Measure](/forward-measure/) — adapted numeraire for interest-rate derivatives
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — applies the same discount-rate logic to corporate equity
- [Interest-Rate Risk](/interest-rate-risk/) — the volatility parameter essential to derivative pricing
- [Black-Scholes Model](/black-scholes-model/) — canonical application of risk-neutral pricing to equity options
- [Volatility Smile](/volatility-smile/) — empirical deviation from risk-neutral model predictions
- [Counterparty Risk](/counterparty-risk/) — real-world friction that violates the model's assumptions

### Wider context

- [Bond](/bond/) — fixed-income security whose options are priced using risk-neutral methods
- [Interest-Rate](/interest-rate/) — the risk-free rate that anchors all discounting
- [Derivative](/option/) — broad class of securities whose valuation rests on this theorem
- [Market Maker Trading](/market-maker-trading/) — practitioners who enforce arbitrage-free pricing

</div>

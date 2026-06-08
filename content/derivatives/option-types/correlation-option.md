---
title: "Correlation Option"
description: "An exotic option whose payoff depends on the realised correlation between two or more underlying assets."
keywords:
  - correlation option
  - multivariate option
  - exotic derivatives
  - correlation trading
  - basket options
image: /svg/derivatives.svg
---

*A **correlation option** is an exotic [derivative](/option/) whose payoff hinges on how closely two or more assets move together—that is, their realised [correlation](/volatility-option/). A correlation [call](/option/) profits if the correlation between, say, a [stock](/stock/) and a [bond](/bond/) is high; a correlation [put](/option/) profits if correlation is low. These instruments allow traders to express views on co-movement and help portfolio managers [hedge](/over-the-counter-market/) against tail-risk scenarios where historically uncorrelated assets suddenly spike together.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Correlation Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and exotic options." />

<div class="wiki-infobox-caption">A derivative that profits from predicting how closely assets will move together.</div>

|   |   |
|---|---|
| **What it is** | An [option](/option/) whose payoff = f(realised correlation between 2+ assets), not individual asset prices |
| **Underlying** | Correlation coefficient (ρ) between asset pairs; typically 0 to 1 (or –1 to +1 for negatively correlated pairs) |
| **Correlation call** | Profits if realised correlation > strike; zeros out if below |
| **Correlation put** | Profits if realised correlation < strike; zeros out if above |
| **Asset pairs** | Stocks, currencies, commodities, [indices](/sp-500-index/); often cross-asset (equity–bond, crude–gold) |
| **Main users** | [Hedge funds](/hedge-fund/), [pension funds](/), asset managers, market makers, systematic traders |

</aside>

## Why correlation matters

In a diversified portfolio, correlation is destiny. Two [stocks](/stock/) with zero correlation reduce [portfolio risk](/diversification/); two [stocks](/stock/) that move in lockstep offer no diversification benefit. During calm periods, equity–[bond](/bond/) correlation is near zero, making a 60/40 portfolio sensible. During crises, correlation spikes to +0.8 or higher, and [bonds](/bond/) no longer cushion [equity](/stock/) losses—the diversification [hedge](/over-the-counter-market/) fails precisely when needed.

Correlation [options](/option/) let traders exploit and hedge this dynamic. If a manager believes that equity–[bond](/bond/) correlation will stay low, she buys a correlation [put](/option/) with a low strike. If correlation spikes above that strike (the [put](/option/) expires in-the-money), she profits—compensating for the larger portfolio losses from rising correlations. Conversely, a [hedge fund](/hedge-fund/) betting that stock-picker [alpha](/alpha/) will persist despite sector consolidation might sell correlation [calls](/option/), profiting if stock correlations remain fragmented.

## Pricing and the curse of dimension

Correlation [options](/option/) are devilishly hard to price. Vanilla [options](/option/) on a single underlying can be priced with the [Black-Scholes](/black-scholes-model/) model, which has a clean closed-form solution. Correlation [options](/option/) depend on the joint distribution of returns across multiple assets—a much richer problem.

Most dealers price correlation [options](/option/) using Monte Carlo simulation: they assume each underlying follows a stochastic process (typically geometric Brownian motion with fixed or time-varying correlation), simulate thousands of paths forward to [expiration](/expiration-date/), and average the discounted payoffs. The accuracy depends on model assumptions. If true correlation is stochastic (changes unpredictably over time), a model assuming fixed correlation will misprice. Equally, if returns are fat-tailed (prone to large jumps), standard models underestimate tail risk.

The difficulty is why correlation [options](/option/) are less standardised than vanilla [options](/option/) and trade primarily [over-the-counter](/over-the-counter-market/). Each trade requires fresh negotiation and pricing, and dealers must reserve significant capital for the [model risk](/operational-risk/) inherent in pricing.

## Basket options and their cousins

Correlation [options](/option/) are closely related to **basket [options](/option/)**, which are [options](/option/) on a weighted portfolio (basket) of assets. A basket [call](/option/) on the "tech basket" might consist of Apple, Microsoft, and Nvidia with weights 40%, 35%, and 25%. The payoff depends on the basket's total return.

Basket [options](/option/) also depend on correlation, but implicitly. If the constituents move in lockstep, the basket [volatility](/volatility-option/) is high, making basket [options](/option/) expensive. If constituents are uncorrelated, basket [volatility](/volatility-option/) is low, making basket [options](/option/) cheaper. A correlation [option](/option/) makes this dependence explicit.

Another cousin is the **[covariance](/correlation-option/) [swap](/option/)**, which directly exchanges fixed and floating [covariance](/correlation-option/) values. These are even less liquid than correlation [options](/option/) but are used by [hedge funds](/hedge-fund/) and [asset managers](/stock-market/) to fine-tune portfolio risk.

## Realised vs. implied correlation

Like [volatility](/volatility-option/), correlation has both realised and implied flavours. **Realised correlation** is the historical correlation coefficient between two assets over a trailing window (e.g., 20 trading days). **Implied correlation** can be inferred from basket [option](/option/) prices: given individual [option](/option/) prices on each constituent and a basket [option](/option/) price, one can back out the implied correlation.

Most standardised correlation [options](/option/) settle on realised correlation. [Over-the-counter](/over-the-counter-market/) structures sometimes reference implied correlation.

Traders exploit mispricings between the two. If implied correlation (baked into basket [option](/option/) prices) is 0.60 but the trader expects realised correlation to drop to 0.40, she buys a correlation [put](/option/) and sells the basket [option](/option/) to lock in the spread. This is correlation arbitrage—a sophisticated strategy requiring real-time pricing and [risk](/credit-risk/) management.

## Tail risk and crisis dynamics

Correlation [options](/option/) are particularly valuable for hedging tail risks. During benign market conditions, equity–[bond](/bond/) correlation is near zero, so a 60/40 portfolio is well-diversified. But in a true crisis—a geopolitical shock, a financial panic, a pandemic—correlation can spike to 0.7 or 0.8 in minutes. [Bonds](/bond/) sell off alongside [equities](/stock/), the [diversification](/diversification/) [hedge](/over-the-counter-market/) evaporates, and losses compound.

A [pension fund](/traditional-ira/) or endowment that buys correlation [puts](/option/) on equity–[bond](/bond/) correlation is effectively buying insurance against this tail outcome. The premium is expensive—most months, the [put](/option/) expires worthless—but when correlation spikes, the [put](/option/) profits enormously, offsetting portfolio losses.

The 2008 financial crisis and the March 2020 COVID crash were textbook examples. Correlations spiked to near +1.0, [diversification](/diversification/) failed, and portfolios suffered sharp losses. Investors who had bought correlation [puts](/option/) (or equivalently, long volatility [insurance](/homeowners-insurance/)) were cushioned.

## Practical limitations and model risk

Correlation [options](/option/) are illiquid. Unlike [equity](/stock/) [options](/option/) or [Treasury](/treasury-bill/) [options](/option/), which trade in deep, liquid markets, correlation [options](/option/) are typically bespoke, [over-the-counter](/over-the-counter-market/) structures with wide [bid-ask spreads](/bid-ask-spread/). A trader wanting to exit a position before [expiration](/expiration-date/) may face substantial costs.

[Model risk](/operational-risk/) is also material. Different pricing models (Gaussian, Student-t, copula-based) can produce widely different fair values for the same correlation [option](/option/). Dealers must disclose model assumptions to clients, but in illiquid markets, prices are often whatever the dealer's model says—and the dealer has every incentive to use conservative (favourable-to-dealer) assumptions.

Correlations are also notoriously unstable. A correlation of 0.3 observed over a quiet summer can jump to 0.7 during a [market](/stock-market/) dislocation, invalidating historical estimates. Models struggle to capture this regime-shifting. As a result, correlation [options](/option/) are best viewed as bets on medium-term co-movement patterns, not as precise insurance contracts.

## Real-world applications

**Multi-asset [hedge funds](/hedge-fund/)**: A fund running a [commodity](/crude-oil/) and [currency](/currency-risk/) portfolio buys correlation [puts](/option/) to hedge against spikes in [commodity](/crude-oil/)–[currency](/currency-risk/) correlation, which occur during inflationary shocks.

**Pension fund [risk management](/counterparty-risk/)**: A [pension fund](/traditional-ira/) with a liability-driven investment mandate buys correlation [puts](/option/) on [equity](/stock/)–[interest rate](/interest-rate/) correlation to protect against scenarios where [equities](/stock/) and [yields](/interest-rate/) both rise, eroding the [pension](/traditional-ira/)'s funded status.

**Quantitative [arbitrage](/volatility-option/)**: A quant [hedge fund](/hedge-fund/) models implied correlations from basket [option](/option/) prices and trades against realised correlation, earning small [spreads](/bid-ask-spread/) on hundreds of trades.

**Structured products**: A bank bundles correlation [options](/option/) into a retail structured note promising yields tied to the correlation between [oil](/crude-oil/) and the [dollar](/us-dollar/)—a bet on [economic cycles](/business-cycle/).

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative contract
- [Volatility option](/volatility-option/) — an exotic option written on realised [volatility](/volatility-option/); shares pricing complexity
- [Basket option](/option/) — an [option](/option/) on a portfolio of assets; depends implicitly on correlation
- [Covariance](/correlation-option/) — the mathematical measure of co-movement
- [Diversification](/diversification/) — portfolio principle that relies on low correlation
- [Over-the-counter market](/over-the-counter-market/) — where correlation [options](/option/) trade bespoke
- [Black-Scholes model](/black-scholes-model/) — the foundational [option](/option/) pricing framework

### Wider context

- [Hedge fund](/hedge-fund/) — major users of correlation [options](/option/)
- [Tail risk](/tail-risk/) — hedging tail risk is a key use case
- [Risk management](/counterparty-risk/) — portfolio protection via correlation [options](/option/)
- [Market dislocation](/market-risk/) — when correlation assumptions break down
- [Pension fund](/traditional-ira/) — institutional user of correlation [insurance](/homeowners-insurance/)

</div>

---
title: "Cross-Gamma"
description: "The second-order price sensitivity of a portfolio to simultaneous moves in two different underlying assets."
keywords:
  - gamma
  - greeks
  - multi-asset portfolios
  - derivatives
  - correlation
  - options pricing
  - portfolio risk
image: /svg/derivatives.svg
---

*Cross-gamma measures how a portfolio's [gamma](/gamma/) in one asset changes in response to moves in a different asset. It captures the risk that correlations between assets may shift or that moves in one market trigger moves in another, amplifying or dampening portfolio convexity in unpredictable ways.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Gamma — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options pricing." />

<div class="wiki-infobox-caption">The hidden second-order risk in multi-asset books.</div>

|   |   |
|---|---|
| **What it is** | The second-order sensitivity of gamma in one asset to price changes in a different asset |
| **Mathematical form** | The mixed partial derivative of portfolio value with respect to two different underlying prices |
| **When it appears** | Multi-leg strategies, cross-asset hedges, [calendar spreads](/spread/) between correlated assets |
| **Related to** | [Correlation risk](/correlation-risk/), [delta](/delta/), [gamma](/gamma/) |
| **Amplified by** | Structural changes in asset linkages, volatility clustering, regime shifts |
| **Monitoring challenge** | Easy to miss; hidden in portfolio aggregation systems |

</aside>

## Moving beyond single-asset gamma

Traditional [gamma](/gamma/) measures how an option's [delta](/delta/) changes when a single underlying moves. A [call option](/call-option/) on an oil company stock has gamma in oil prices and gamma in the stock price separately. But what happens to the stock's gamma if oil prices move? That is cross-gamma: how gamma in one direction of the portfolio interacts with moves in a different asset.

Consider a [hedge fund](/hedge-fund/) with a large long position in European bank stocks and a short position in [euro](/euro/) currency futures. If bank stocks rise, the portfolio's [delta](/delta/) exposure to the euro increases (the European exposure becomes more valuable). But if the euro rises simultaneously, the short euro position loses value, and the relationship between bank stock moves and euro moves becomes critical to understanding the portfolio's true convexity. That interaction is cross-gamma.

## Why correlation matters

Cross-gamma is fundamentally about correlation. If two assets always move together perfectly, cross-gamma is straightforward: compute gamma in each separately and aggregate. But real correlations are unstable. In calm markets, European stocks and the euro might have a low correlation; during a crisis, they correlate perfectly as eurozone contagion spreads. A portfolio designed with low cross-gamma under calm correlations can suddenly develop very high cross-gamma under stress correlations, creating a hidden tail risk.

This instability is especially dangerous in derivatives strategies. A desk might run a [calendar spread](/spread/) — long European bank calls with a nearby expiration and short European bank calls with a far expiration — while simultaneously hedging with short euro futures. The gamma of the call spread changes not only with the bank stock price but also with currency moves, because the currency hedge changes the effective payoff structure. If the euro weakens, the gamma of the call spread might actually increase (as the international exposure becomes more attractive), even though gamma typically decays with time.

## Multi-asset option strategies

Cross-gamma is most pronounced in [options](/option/) that explicitly link two assets. A [spread option](/spread/) — paying off on the difference between two underlyings, like the price gap between WTI crude and Brent crude — has gamma in each crude market and cross-gamma measuring how gamma in one market changes if the other rallies. If both crude markets rally together, the spread widens and gamma shifts. If they decouple, gamma behaves differently.

Similarly, [basket options](/option/) (options on a weighted average of multiple stocks) have cross-gamma in every pair of components. A [call option](/call-option/) on a basket of energy stocks has gamma that depends not only on each stock's move but on how the stocks move together. A trader short this basket option is implicitly short cross-gamma: if correlations between basket components collapse and individual stocks move in opposite directions, the basket option becomes cheaper (lower implied volatility) and the short position profits. If correlations tighten and all stocks move together, volatility expands and the short position loses.

## Correlation risk as cross-gamma

In fixed income and currency markets, cross-gamma appears as [correlation risk](/correlation-risk/). A portfolio holding long [bonds](/bond/) in multiple countries faces gamma in each country's yield curve but also cross-gamma from the correlation between yields. If yields are normally uncorrelated (each country's economy moves independently), gamma is straightforward. But during a crisis, yields converge and [spreads](/spread/) compress. The portfolio's gamma suddenly changes shape as diversification collapses. This change in the diversification benefit is cross-gamma in action.

Equity volatility has similar dynamics. A portfolio long [call options](/call-option/) on individual stocks has gamma in each stock separately. But if stock correlations are high, the portfolio acts like a concentrated bet on the sector; a sector move drives all options' gamma together. If correlations collapse, each stock's gamma becomes independent, and the portfolio's overall gamma is lower (because gains and losses offset). A trader expecting correlation to rise must account for cross-gamma: as correlations rise, individual-stock gamma matters less and sector gamma matters more.

## Hedging cross-gamma exposure

Unlike [delta](/delta/) and standard [gamma](/gamma/), which are relatively easy to hedge (by buying or selling the underlying or offsetting options), cross-gamma is harder to manage. There is no simple instrument called "cross-gamma hedge." Instead, traders must identify which pairs of assets are driving cross-gamma and adjust positions in both.

A desk might find that its portfolio has high positive cross-gamma between the euro and European equities: if both rally together, the portfolio makes money from convexity; if they decouple, it loses that benefit. To reduce this exposure, the desk could reduce the notional size of one leg, or introduce options that profit from correlation breakdown (such as [dispersion trades](/option/), which are long individual stock volatility and short index volatility). Dispersion trades are essentially bets that correlations will fall, which is effectively short correlation or short cross-gamma.

## Detection and measurement challenges

Cross-gamma is dangerous because it is invisible in most risk systems. A platform that measures [delta](/delta/), [gamma](/gamma/), [vega](/vega/), and [theta](/theta/) separately may report that portfolio gamma is low, when in fact high positive cross-gamma across different legs is creating undetected tail risk. Only when correlations shift or multiple assets move simultaneously is the hidden exposure revealed, often too late.

Professional firms use correlation stress testing to unearth cross-gamma. They run scenarios where correlations move — market correlations rise, interest rate correlations fall, equity-commodity correlations reverse — and observe how gamma changes. A sharp change in gamma under these scenarios indicates high cross-gamma exposure. Similarly, historical simulations that replay past periods when correlations shifted can reveal whether the portfolio would have been hurt by that shift.

## The role of regime shifts

Cross-gamma becomes acute during regime shifts — moments when the structure of the market changes. The March 2020 volatility spike saw correlations across asset classes collapse, then tighten. Portfolios designed with cross-gamma exposure optimized for one regime faced severe losses in another. A long [straddle](/option/) on a currency pair (betting on volatility) combined with short correlation trades (betting that correlations would remain high) faced a squeeze: volatility spiked and correlations dropped simultaneously, the worst combination for that book.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — single-asset convexity; cross-gamma extends this concept
- [Delta](/delta/) — first-order sensitivity in one asset
- [Vega](/vega/) — sensitivity to volatility; related to correlation through stochastic vol models
- [Theta-Gamma Tradeoff](/theta-gamma-tradeoff/) — extends to multiple assets
- [Correlation Risk](/correlation-risk/) — the underlying dynamic

### Wider context

- [Spread](/spread/) — strategy that concentrates cross-gamma
- Greeks — the full toolkit of sensitivities
- Derivatives — instruments that create cross-gamma
- Portfolio Risk — how cross-gamma fits into broader management
- [Volatility Smile](/volatility-smile/) — related multi-dimensional pricing phenomenon

</div>

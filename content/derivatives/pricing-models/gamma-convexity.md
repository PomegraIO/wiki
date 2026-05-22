---
title: "Gamma Convexity"
description: "The rate of change in delta as the underlying asset price moves, measuring an option's non-linearity and sensitivity to volatility changes."
keywords:
  - gamma option greek
  - delta convexity
  - option non-linearity
  - gamma hedging
---

*A **gamma** (γ) is an [option Greek](/wiki/options-greeks/) measuring the rate of change in [delta](/wiki/delta-option-greeks/) as the underlying asset price moves. It quantifies an option's **convexity**—how much [delta](/wiki/delta-option-greeks/) accelerates as the underlying rises or falls. An option with high gamma is more responsive to price moves; an option with low gamma has stable [delta](/wiki/delta-option-greeks/).* 

[Delta](/wiki/delta-option-greeks/) tells you an option's current price sensitivity; gamma tells you how that sensitivity changes. Traders use gamma to measure [leverage](/wiki/leverage-ratio-forex/), manage [volatility](/wiki/volatility-index-futures/) exposure, and size positions. Long options have positive gamma (delta increases as price rises), while short options have negative gamma (delta decreases as price rises). Understanding gamma is essential for [option](/wiki/option/) hedging and risk management.

<aside class="wiki-infobox">

| Item | Detail |
|---|---|
| **Definition** | ∂delta / ∂underlying price |
| **Sign (long call/put)** | Positive |
| **Sign (short call/put)** | Negative |
| **Units** | Delta per dollar of underlying (or per 1% move) |
| **Highest gamma** | At-the-money options |
| **Lowest gamma** | Deep in/out-of-the-money options |
| **Payoff of gamma** | Long gamma profits from realized [volatility](/wiki/volatility-index-futures/); short gamma loses |
| **Relationship to vega** | Both positive for long options; gamma relates to realized [volatility](/wiki/volatility-index-futures/), vega to implied [volatility](/wiki/implied-volatility/) |

</aside>

## Delta and gamma: the relationship

**[Delta](/wiki/delta-option-greeks/)** answers: "If the underlying price moves $1, how much does the option price change?"

**Gamma** answers: "If the underlying price moves $1, how much does [delta](/wiki/delta-option-greeks/) change?"

Example with a 3-month at-the-money (ATM) [call option](/wiki/call-option/):
- Current underlying price: $100
- Current [delta](/wiki/delta-option-greeks/): 0.50
- Current gamma: 0.03

If the underlying rises to $101:
- New [delta](/wiki/delta-option-greeks/) ≈ 0.50 + 0.03 = 0.53

If the underlying falls to $99:
- New [delta](/wiki/delta-option-greeks/) ≈ 0.50 − 0.03 = 0.47

Gamma quantifies this curvature. The [option](/wiki/option/) price curve is not linear; it is convex. Gamma measures the degree of convexity.

## Positive and negative gamma

**Positive gamma (long [call](/wiki/call-option/) or [put](/wiki/put-option/))**: 
- You own the [option](/wiki/option/).
- If the underlying rises, [delta](/wiki/delta-option-greeks/) increases, making your position more bullish—you have increasing leverage.
- If the underlying falls, [delta](/wiki/delta-option-greeks/) decreases, making your position less bearish—you have decreasing leverage.
- **Benefit**: You benefit from large moves (realized [volatility](/wiki/volatility-index-futures/)).
- **Cost**: You lose money to [theta decay](/wiki/theta-option-greeks/) (time decay) if the underlying is static.

**Negative gamma (short [call](/wiki/call-option/) or [put](/wiki/put-option/))**:
- You have sold the [option](/wiki/option/).
- If the underlying rises, [delta](/wiki/delta-option-greeks/) increases (the [call](/wiki/call-option/) you sold is more deeply in-the-money), your short position becomes worse—you have increasing negative [delta](/wiki/delta-option-greeks/).
- If the underlying falls, [delta](/wiki/delta-option-greeks/) decreases (the [call](/wiki/call-option/) you sold is less in-the-money), your short position becomes better.
- **Benefit**: You profit from low realized [volatility](/wiki/volatility-index-futures/) and [theta decay](/wiki/theta-option-greeks/).
- **Cost**: You lose money if realized [volatility](/wiki/volatility-index-futures/) is high and the underlying makes large moves.

## Gamma across [moneyness](/wiki/moneyness/): ATM vs. OTM

**At-the-money (ATM) [options](/wiki/option/)**: Highest gamma. A one-dollar move in the underlying creates the largest change in [delta](/wiki/delta-option-greeks/).

**Out-of-the-money (OTM) [options](/wiki/option/)**: Lower gamma. The [option](/wiki/option/) is less sensitive to price changes because it is less likely to be exercised.

**In-the-money (ITM) [options](/wiki/option/)**: Lower gamma. The [option](/wiki/option/) behaves more like the underlying stock; [delta](/wiki/delta-option-greeks/) is already close to 1.0 and does not change much with further price moves.

This is why ATM options are more sensitive to realized [volatility](/wiki/volatility-index-futures//) and why traders use ATM straddles (long [call](/wiki/call-option/) + long [put](/wiki/put-option/)) to express a view on [volatility](/wiki/volatility-index-futures/).

## Gamma and time decay: the trader's dilemma

Gamma and [theta](/wiki/theta-option-greeks/) (time decay) are inversely related:

- **Long [options](/wiki/option/)**: Positive gamma, negative [theta](/wiki/theta-option-greeks/). You gain from realized [volatility](/wiki/volatility-index-futures/), lose from time decay.
- **Short [options](/wiki/option/)**: Negative gamma, positive [theta](/wiki/theta-option-greeks/). You gain from time decay and low [volatility](/wiki/volatility-index-futures/), lose from realized [volatility](/wiki/volatility-index-futures/).

A trader buying [options](/wiki/option/) as a [volatility](/wiki/volatility-index-futures/) hedge pays [premium](/wiki/option-premium/) (cost of [theta](/wiki/theta-option-greeks/)) to own gamma (profit from large moves).

## Gamma hedging: dynamic rebalancing

A **gamma hedge** is a strategy where a trader dynamically adjusts the underlying position to remain [delta](/wiki/delta-option-greeks/)-neutral while profiting from realized [volatility](/wiki/volatility-index-futures/).

**Example**: A market maker has sold a large [call option](/wiki/call-option/) (short gamma, short [vega](/wiki/vega-option-greeks/)). They hedge by buying the underlying:

- Stock is at $100, [delta](/wiki/delta-option-greeks/) = 0.50 on the short [call](/wiki/call-option/). The market maker buys 50 shares to be [delta](/wiki/delta-option-greeks/)-neutral.
- Stock rises to $101. The [call](/wiki/call-option/) [delta](/wiki/delta-option-greeks/) increases to 0.53. The market maker now has negative [delta](/wiki/delta-option-greeks/) (short 0.03 on the call, long 50 shares on underlying). They sell some shares to rebalance.

By continuously rebalancing to stay [delta](/wiki/delta-option-greeks/)-neutral, the market maker locks in profits from **realized [volatility](/wiki/volatility-index-futures/)** exceeding **implied [volatility](/wiki/implied-volatility/)** when they sold the [call](/wiki/call-option/).

Realized [volatility](/wiki/volatility-index-futures/) (actual price movements) versus implied [volatility](/wiki/implied-volatility/) (market's expectation of future [volatility](/wiki/volatility-index-futures/)) is the arbitrage.

## Gamma in portfolio context

A large long equity position is short gamma. The [delta](/wiki/delta-option-greeks/) is fixed at 1.0; it does not change as the stock price changes. The position is linear, not convex. In a violent sell-off, the portfolio loses linearly on the equity and has no gamma cushion.

Adding long [puts](/wiki/put-option/) (protective [puts](/wiki/protective-put/)) adds positive gamma. If the stock crashes, the [put](/wiki/put-option/) gains value (negative [delta](/wiki/delta-option-greeks/) becomes more negative, hedging the long stock). The portfolio is now convex: losses are cushioned.

This is why tail-risk hedging programs specifically buy [puts](/wiki/put-option/); the positive gamma provides a cushion in extreme moves.

## Gamma and [volatility](/wiki/volatility-index-futures/): the vega-gamma blend

Gamma measures exposure to realized [volatility](/wiki/volatility-index-futures/). [Vega](/wiki/vega-option-greeks/) measures exposure to implied [volatility](/wiki/implied-volatility/). 

A trader believing realized [volatility](/wiki/volatility-index-futures/) will exceed implied [volatility](/wiki/implied-volatility/) wants **long gamma, neutral [vega](/wiki/vega-option-greeks/)**. This is achieved by buying [options](/wiki/option/) at low implied [volatility](/wiki/implied-volatility/), betting that realized [volatility](/wiki/volatility-index-futures/) will be high.

Conversely, a trader believing realized [volatility](/wiki/volatility-index-futures/) will fall below implied [volatility](/wiki/implied-volatility/) wants **short gamma, neutral [vega](/wiki/vega-option-greeks/)**. They sell [options](/wiki/option/) at high implied [volatility](/wiki/implied-volatility/).

## Gamma in the tails: realized vs. implied [volatility](/wiki/volatility-index-futures/)

During market crashes, realized [volatility](/wiki/volatility-index-futures/) often exceeds implied [volatility](/wiki/implied-volatility/) (the market did not expect the crash). Traders long gamma profit from this gap. Traders short gamma lose.

After a crash, implied [volatility](/wiki/implied-volatility/) often remains elevated even as realized [volatility](/wiki/volatility-index-futures/) subsides (traders are nervous). Here, short-gamma traders start to profit as realized [volatility](/wiki/volatility-index-futures/) declines and implied [volatility](/wiki/implied-volatility/) remains high.

This is the risk-reward of gamma positions: they profit from realized [volatility](/wiki/volatility-index-futures/), but losses can accelerate if the underlying gaps (jumps instantaneously), because [gamma](/wiki/gamma-option-greeks/) models small continuous moves, not discrete jumps.

## Gamma and convexity: the bond analogy

In fixed income, **convexity** refers to the curvature of the price-yield relationship. A [bond](/wiki/bond/) with high convexity gains more value when yields fall and loses less when yields rise. This is analogous to positive gamma: the position is convex, benefiting from large moves.

A [callable bond](/wiki/callable-bond/) is short convexity (the issuer has a [call option](/wiki/call-option/)). When yields fall, the bond's upside is capped (the issuer calls it), so convexity is negative. This is the "convexity trap" that hurt many bond portfolios in the 2021–2022 rising-rate environment.

The term "gamma convexity" unifies these concepts: gamma for [options](/wiki/option/), convexity for [bonds](/wiki/bond/), both describe non-linearity and the cost of owning protection in tails.

## Practical note: gamma decay

Gamma itself decays as expiration approaches (assuming the [option](/wiki/option/) remains ATM). Longer-dated [options](/wiki/option/) have lower gamma but last longer; shorter-dated [options](/wiki/option/) have higher gamma but die faster.

A trader managing a [volatility](/wiki/volatility-index-futures/) position must roll short-gamma positions to avoid the acceleration of gamma loss as expiration nears.

<div class="wiki-seealso">

### Closely related
- [Delta Option Greeks](/wiki/delta-option-greeks/) — Rate of change in option price with underlying price
- [Vega Option Greeks](/wiki/vega-option-greeks/) — Sensitivity to changes in implied volatility
- [Theta Option Greeks](/wiki/theta-option-greeks/) — Time decay; daily loss from passage of time
- [Options Greeks](/wiki/options-greeks/) — Complete set of option sensitivities (delta, gamma, vega, theta, rho)

### Wider context
- [Option](/wiki/option/) — Derivative contract with the right (not obligation) to buy or sell an asset
- [Implied Volatility](/wiki/implied-volatility/) — Market's expectation of future price volatility
- [Protective Put](/wiki/protective-put/) — Buying a put to hedge downside on an existing position
- [Volatility Hedging](/wiki/volatility-hedging/) — Using derivatives to manage exposure to price swings

</div>

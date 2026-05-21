---
title: "Volatility Smile"
description: "The volatility smile is the empirical observation that implied volatility varies across different strike prices, typically rising for out-of-the-money options in both directions."
keywords:
  - volatility smile
  - volatility skew
  - implied volatility
  - strike price
  - option pricing anomaly
image: "/svg/derivatives.svg"
---

*The **volatility smile** is an empirical pattern where [implied volatility](/implied-volatility) varies across different [strike price](/strike-price)s for options with the same [expiration date](/expiration-date) on the same underlying. In many markets, the IV is lowest for [at-the-money](/at-the-money) options and rises for [in-the-money](/in-the-money) and [out-of-the-money](/out-of-the-money) options, creating a U-shaped curve that resembles a smile. Related patterns—**volatility skew** and **volatility term structure**—describe IV varying across moneyness and expiration.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Smile — key facts</div>

<img src="/svg/derivatives.svg" alt="U-shaped implied volatility curve across strikes" />

<div class="wiki-infobox-caption">Volatility smile: IV rises away from the strike.</div>

|   |   |
|---|---|
| **Pattern** | U-shaped IV curve across strikes |
| **Skew alternative** | Lopsided curve; higher on one side |
| **Pre-1987** | Relatively flat IV (Black-Scholes assumption) |
| **Post-1987** | Clear smile/skew in most markets |
| **OTM puts** | Often have higher IV (crash fear) |
| **ATM options** | Lowest IV |
| **OTM calls** | Higher IV than ATM, lower than OTM puts |
| **Explains** | Why Black-Scholes misprices OTM options |
| **Driven by** | Jump risk, leverage effects, demand imbalances |
| **Opportunity** | Volatility arbitrage and smile trades |

</aside>

## The smile pattern

In a perfect [Black-Scholes model](/black-scholes-model) world with constant volatility, all options on the same underlying and expiration should have the same [implied volatility](/implied-volatility), regardless of strike.

In practice, this does not happen. The plot of [implied volatility](/implied-volatility) vs. strike price looks like a smile (U-shaped) or a skew (lopsided). For example:

- ATM $100 call/put: IV = 18%
- $95 OTM put: IV = 22%
- $105 OTM call: IV = 21%

The OTM options have higher [implied volatility](/implied-volatility) than the ATM options. The market is pricing in a higher probability of large moves at the extremes.

## Volatility skew vs. smile

**Smile:** Symmetric; IV rises on both sides of the strike equally. More common in indices and currencies.

**Skew:** Asymmetric; IV rises more on one side. Most common in single stocks, where OTM puts have much higher IV than OTM calls (fear of crashes, not rallies).

## Why the smile exists

Several factors contribute:

1. **Jump risk:** Stock prices can gap overnight (earnings, news). Jumps are non-log-normal. Options priced under jump models have higher IV for OTM options, which are sensitive to jumps.

2. **Leverage effect:** As stock prices fall, [equity volatility](/historical-volatility) rises (companies become riskier). This creates skew: OTM puts are more valuable because falls are more volatile.

3. **Demand imbalances:** After a crash (e.g., 2008), demand for OTM puts surges, pushing their IV higher. Supply-demand creates skew.

4. **Model limitations:** Black-Scholes assumes log-normal prices and constant volatility. Real markets have fatter tails (more extreme moves) and stochastic volatility, both of which create smile.

## Trading the smile

Volatility smile traders:

1. **Identify mispricings:** If a model predicts IV should be flat but the smile is steep, they identify where the market is over- or under-pricing moves.

2. **Sell overpriced volatility:** Buy ATM options, sell OTM options (higher IV), betting the smile flattens.

3. **Buy underpriced volatility:** The reverse; buy OTM options, sell ATM, betting the smile steepens or the OTM options become more expensive.

4. **Skew trades:** Buy OTM puts, sell OTM calls (or vice versa) to express a view on skew changes.

## Volatility term structure

Related to the smile is the **volatility term structure**—how IV varies across [expiration date](/expiration-date)s. Near-term options might have IV of 20%; 6-month options might have 25%. This reflects different volatility expectations for the near vs. far future.

The term structure shifts with regime changes. Before earnings, the near-term IV spikes; after earnings (once uncertainty resolves), it may fall faster than longer-term IV.

## Stochastic volatility models

To model the smile properly, quants use **stochastic volatility models** (e.g., Heston, SABR, local volatility) that allow volatility to change over time and vary by price level. These models fit the smile better than Black-Scholes and improve hedging.

## See also

<div class="wiki-seealso">

### Closely related

- [Implied volatility](/implied-volatility/) — what varies across strikes
- [Volatility skew](/volatility-smile/) — asymmetric smile
- [Black-Scholes model](/black-scholes-model/) — assumes flat volatility
- [At-the-money](/at-the-money/) — lowest IV in smile
- [Out-of-the-money](/out-of-the-money/) — higher IV
- [Strike price](/strike-price/) — determines smile position

### Trading and hedging

- [Vega](/vega/) — sensitivity to overall volatility level
- [Volatility arbitrage](/alpha/) — exploiting smile mispricings
- Options strategy — smile trades
- Gamma scalping — interacts with smile shifts

### Advanced models

- [Stochastic volatility](/volatility-smile/) — models smile behavior
- [Local volatility](/volatility-smile/) — alternative smile model
- [Jump diffusion](/volatility-smile/) — models jumps causing smile
- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — handles smile

### Deeper context

- [Option](/option/) — the underlying instrument
- [Derivatives pricing](/black-scholes-model/) — smile is pricing anomaly
- [Risk management](/hedge-fund/) — smile affects hedging

</div>

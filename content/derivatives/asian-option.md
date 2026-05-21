---
title: "Asian Option"
description: "An Asian option's payoff depends on the average price of the underlying asset over a set period, rather than just the final price, reducing the impact of price spikes."
keywords:
  - asian option
  - exotic option
  - average price option
  - path-dependent
  - derivative
image: "/svg/derivatives.svg"
---

*An **Asian option** is an exotic derivative whose payoff is based on the average price of the underlying asset over a specified period, rather than its price on the [expiration date](/expiration-date). This averaging smooths out short-term price spikes and makes the option cheaper and less sensitive to manipulation than a standard [call option](/call-option) or [put option](/put-option) struck on the spot price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Asian Option — key facts</div>

<img src="/svg/derivatives.svg" alt="A chart showing average price calculation over time" />

<div class="wiki-infobox-caption">Asian options smooth volatility by averaging price over a period.</div>

|   |   |
|---|---|
| **Payoff basis** | Average price over period, not final price |
| **Average type** | Arithmetic mean (common) or geometric mean |
| **Monitoring dates** | Daily, weekly, monthly, or fixed dates |
| **Strike type** | Fixed strike or floating (based on average) |
| **Price vs. vanilla** | Much cheaper (lower volatility) |
| **Volatility factor** | Lower implied volatility due to averaging |
| **Primary use** | Commodity and currency hedging |
| **Settlement** | Cash or physical |
| **Path-dependent** | Yes; full price history matters |

</aside>

## How averaging works

A standard [call option](/call-option) on a [stock](/stock) at a $100 strike is worth $X if the stock is at $105 on expiration; its payoff is $5. Now suppose the stock jumped to $120 on day 47 of a 90-day option, then fell back to $105 by expiration. The vanilla option payoff is unchanged (still $5), but the Asian option recalculates.

The Asian call averages the stock price over the entire 90 days. If the average came to $107, the Asian call payoff is $7 rather than $5. If the average is $102, the payoff is $2. The averaging *dampens* volatility. A dramatic spike or crash partway through affects the payoff, but not as directly as a final-spot-price option.

This is why Asian options are cheaper. Lower [historical volatility](/historical-volatility) in the underlying price path (relative to a vanilla option's sensitivity to the final price) means lower option [premium](/option-premium). An Asian call is always worth less than a vanilla call struck at the same [strike price](/strike-price) on the same underlying.

## Two averaging approaches

**Arithmetic mean** is the most common. The option pays based on the average of closing prices (or intra-day prices) over the monitoring period. If you average 90 daily closing prices and the average is $107 against a $100 strike, the payoff is $7.

**Geometric mean** is sometimes used, particularly in academic pricing models, because it yields more tractable mathematics. The geometric average of a set of prices is always less than the arithmetic average, so a geometric-mean Asian option is cheaper still. In practice, arithmetic means dominate because they match market conventions.

## Fixed strike vs. floating strike

Most Asian options use a **fixed [strike price](/strike-price)**—a [strike](/strike-price) of $100, just like a vanilla option. The average price is compared to this fixed strike.

Some Asian options, called **floating-strike Asians**, use the average price itself as the strike. The call holder is paid if the final price exceeds the average; the put holder is paid if the final price falls below the average. These are even cheaper because they remove the strike risk entirely. The payoff to a floating-strike Asian call is always max(final price – average price, 0), which is almost always less in-the-money than a fixed-strike version.

## Primary use cases

Asian options are heavily used in commodity hedging. An oil refinery knows it will buy oil monthly for the next year. Rather than buying 12 separate [call option](/call-option) contracts, one for each month, it can buy a single Asian call that averages across all 12 months. The refinery saves on [premium](/option-premium) and avoids the risk of being hedged only on one spike day.

Currency traders use Asian options when they have ongoing exposure. An exporter receives revenue monthly in foreign currency. A 12-month Asian option on the currency pair provides downside protection without paying the full [premium](/option-premium) of a monthly vanilla option ladder.

Airlines have historically used Asian options to hedge jet fuel costs, because their fuel consumption is continuous and they benefit from averaging.

## Pricing Asian options

Valuing Asian options analytically is harder than [vanilla option](/call-option) pricing because the payoff depends on the entire price path, not just the starting and ending prices. [Black-Scholes model](/black-scholes-model) does not apply directly.

[Monte-carlo-options-pricing](/monte-carlo-options-pricing) is the standard approach. The model simulates thousands of possible price paths from now to expiration, calculates the average for each path, computes the payoff, and takes the expected value. Geometric-average Asian options can sometimes be closed-form priced using Black-Scholes variants, but arithmetic-average Asians typically require simulation.

The key insight is that the [volatility](/historical-volatility) input to the model must reflect the volatility of the average price, not the spot price. This is materially lower, which is why Asian options are cheaper.

## Greeks and risks

[Delta](/delta) for an Asian option depends on where in the monitoring period you are. Early in the period, the delta is low because the final average is still uncertain. As you approach expiration, the [delta](/delta) drifts closer to a vanilla option's delta because the unknown future prices become fewer.

[Theta](/theta) (time decay) is less aggressive for Asian options than vanilla options, because the averaging mutes the edge. [Vega](/vega) (sensitivity to [volatility](/historical-volatility)) is also lower, which helps the buyer—falling volatility hurts a vanilla option more than an Asian.

## Path dependency and monitoring

The value of an Asian option depends on every price observation during the monitoring period. Once a price is locked in (observed), it cannot change; the future average is now a weighted sum of locked prices plus unknown future prices. This path-dependent nature means you cannot price an Asian option by knowing just today's price and historical [volatility](/historical-volatility)—you must track the running average as monitoring dates pass.

Some Asian options use continuous monitoring (every trading day), while others use fixed dates (monthly, quarterly). Continuous monitoring is cheaper because it captures more price detail and reduces the chance of a discrete spike.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — vanilla right to buy
- [Put option](/put-option/) — vanilla right to sell
- [Barrier option](/barrier-option/) — another exotic with path-dependent payoff
- [Basket option](/basket-option/) — payoff based on multiple underlyings
- [Expiration date](/expiration-date/) — when the average period ends

### Pricing & Greeks

- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — standard valuation method
- [Black-Scholes model](/black-scholes-model/) — vanilla pricing; not directly applicable
- [Implied volatility](/implied-volatility/) — of the average, not the spot
- [Historical volatility](/historical-volatility/) — affects option premium

### Deeper context

- [Option](/option/) — the family of derivatives
- Commodity — common underlying
- [Currency](/currency-option) — another common underlying
- [Volatility smile](/volatility-smile/) — exotic options display distinct smile patterns

</div>

---
title: "Implied Volatility vs Historical Volatility in Options"
description: "How implied volatility reflects forward-looking market expectations of price swings while historical volatility measures realized past moves, and why the gap between them drives trading opportunity."
keywords:
  - implied volatility vs historical volatility options
  - implied volatility
  - historical volatility
  - options pricing
  - volatility trading
image: /svg/derivatives.svg
---

*In options trading, **implied volatility** is the market's forward-looking forecast of price swings (backed into the [option](/option/) price), while **historical volatility** measures the realized swings in the underlying asset's past price. The gap between them signals whether options are expensive or cheap and drives much of options traders' decision-making.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Measures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Implied is forward-looking and market-priced; historical is backward-looking and objective. The spread between them reveals relative value.</div>

|   |   |
|---|---|
| **Implied volatility (IV)** | Market's consensus forecast of future price swings embedded in option price |
| **Historical volatility (HV)** | The standard deviation of realized daily/weekly returns over a past period |
| **IV data source** | Options prices observed in the market, backed into the [Black-Scholes model](/black-scholes-model/) |
| **HV data source** | Historical price data; computed mechanically |
| **Key use** | IV–HV gap reveals whether options are relatively expensive or cheap |
| **Time horizon** | IV is forward-looking (to expiration); HV looks backward (last 20, 60, or 252 trading days) |

</aside>

## What Implied Volatility Measures

An [option](/option/) is more valuable the more volatile the underlying asset is expected to be. A call option on a stock that traders expect to swing wildly is worth more than a call on a stock expected to move little. But the market does not directly observe "expected volatility"—instead, traders observe option prices and back out the implied volatility.

The [Black-Scholes model](/black-scholes-model/) (and other pricing models) map volatility into option prices. If you know the stock price, the strike, the time to expiration, interest rates, and the volatility, you can compute a fair option price. But traders often invert this: given the observed option price, strike, and other terms, they solve for the volatility that makes the model price equal the market price. That solved volatility is the **implied volatility (IV)**.

IV is the market's consensus expectation of how much the underlying will move before the option expires. A 20% annual IV means traders expect the annualized standard deviation of returns to be 20%. If IV is 50%, traders expect much larger swings.

IV is forward-looking. It reflects the market's collective belief about future uncertainty and risk—shaped by economic conditions, earnings announcements, geopolitical shocks, or technical patterns.

## What Historical Volatility Measures

**Historical volatility (HV)** is straightforward: the standard deviation of the underlying's realized returns over a recent period—often the past 20, 60, or 252 trading days (roughly 1 month, 3 months, or 1 year).

HV is objective and mechanical. You pull the price data, compute daily log returns, and take the standard deviation. A stock's HV over the past 60 days is a fact, not a forecast.

HV answers a simple question: "How much has this asset actually moved recently?" It reflects the past, not the future.

## Why the Gap Matters: Relative Valuation

The spread between IV and HV is the trader's window into relative value.

**Case 1: IV > HV (Options are expensive)**

Suppose a stock's 60-day HV is 18%, but the current IV on its 60-day options is 28%. The market is pricing in much higher future volatility than the asset has exhibited recently. This might happen if:

- An earnings announcement is imminent, and traders expect a large swing
- The company has announced a strategic event (acquisition, restructuring) that creates uncertainty
- Broader market volatility has spiked, and contagion to this stock is priced in

An options seller (short a call or short a put) views high IV as attractive—they receive a premium that is generous relative to recent realized volatility. They are betting that future realized volatility will be lower than IV, pocketing the difference as profit.

An options buyer (long a call or long a put) is skeptical of high IV—they are buying expensive insurance or leverage, betting that realized volatility will surprise to the upside and justify the premium paid.

**Case 2: IV < HV (Options are cheap)**

A stock's 60-day HV is 35%, but IV on 60-day options is 20%. The market is underpricing volatility. This might happen if:

- The stock has experienced a recent shock (earnings miss, lawsuit) that inflated HV temporarily, but the market believes volatility will normalize
- A central bank intervention or policy announcement is expected to reduce uncertainty
- The asset's recent volatility is viewed as a one-off, not representative of forward prospects

An options buyer views low IV as attractive—they can buy options cheaply, betting realized volatility will be higher. An options seller avoids selling, viewing the premium as inadequate compensation for the true risk.

## The Role of Historical Volatility in Forecasting

While IV is the market's official forecast, HV still matters. Different lookback windows reveal different patterns:

- **20-day HV** reflects very recent turbulence; useful for high-frequency traders and short-dated options
- **60-day HV** captures medium-term trends; useful for monthly and quarterly options
- **252-day (annual) HV** captures long-term volatility regime; useful for long-dated options and strategic hedging

Traders often compare IV to multiple HV windows. If 20-day HV is 18% but 60-day and 252-day HV are both 25%, the recent calm may be temporary. IV around 22% is then viewed as underpriced (the market expects calm to persist, but the longer-term regime is higher). Conversely, if recent HV has spiked temporarily, IV might be pricing in mean reversion to a lower long-term level.

## Volatility Surface and Smile: IV Is Not Uniform

IV is not a single number; it varies across strikes and maturities. The **volatility surface** (or **volatility smile**) maps IV across different option strikes.

For equity index options, IV is typically higher on out-of-the-money puts than on at-the-money or call options. This is because downside crashes command a premium; buyers pay more for protection against tail risks. HV, by contrast, is a single value per lookback window—it does not vary by strike.

This means the IV–HV comparison becomes more nuanced:

- An equity index's HV might be 15%, but IV on far out-of-the-money puts might be 25% (tail risk premium), while IV on calls is 18%
- A trader buying tail-risk protection (puts) is paying a much higher premium than HV justifies, but is explicitly paying for protection against rare, large crashes
- A trader selling call options at 18% IV is better compensated than at-the-money puts at 25% IV (in volatility terms), though in absolute dollar terms depends on the strike and time value

## Time Decay and Volatility Prediction

As an option approaches expiration, its [time value](/time-value/) decays. An option's realized volatility over its remaining life becomes more relevant to the option's P&L than the IV at inception.

If a trader buys a 3-month call when IV is high, intending to hold it for 1 month and sell it, the trade profits if realized volatility exceeds IV (the option value rises as realized moves justify the high IV premise) or if IV rises further (the option becomes more valuable regardless of realized moves).

This highlights the relationship:

- IV tells you the option market's view of future volatility
- Realized volatility (the actual moves that occur) determines whether an IV bet was correct
- HV provides a baseline for expected volatility, but it lags market repricing around news and shocks

## Volatility Regimes and Trading Cycles

Volatility follows regimes. High-volatility periods (market corrections, crises) often see IV spike faster than it can be justified by realized moves alone—traders panic and bid up option premiums. Low-volatility periods (steady bull markets) see IV and HV both decline, and options become cheap.

A classic trading opportunity emerges when IV falls too far below HV (or median historical levels). Traders sell expensive assets and buy cheap options, betting on mean reversion. Conversely, when IV spikes far above recent HV, options buyers fade the spike, assuming it is transient.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — The derivative contract priced using volatility measures
- [Black-Scholes Model](/black-scholes-model/) — The pricing framework that maps volatility to option value
- [Implied Volatility](/implied-volatility/) — Forward-looking market forecast of price swings
- [Time Decay](/time-decay-theta/) — How option value erodes as expiration approaches
- [Time Value](/time-value/) — The component of option price driven by volatility and time

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Using options and volatility to manage risk
- [Option Premium](/option-premium/) — The price paid for an option, driven by volatility
- [Volatility Smile](/volatility-smile/) — The non-uniform IV surface across strikes
- [Strike Price](/strike-price/) — The reference price that determines option payoff

</div>

---
title: "Volatility Option"
description: "An option contract written directly on the realised or implied volatility of an underlying asset, rather than its price."
keywords:
  - volatility option
  - volatility derivatives
  - implied volatility
  - realized volatility
  - exotic options
image: /svg/derivatives.svg
---

*A **volatility option** is a [derivative](/option/) whose payoff depends on the actual (realised) or expected (implied) [volatility](/historical-volatility/) of an underlying asset, not the asset's price itself. A volatility [call option](/option/) pays off if actual [volatility](/historical-volatility/) exceeds a strike level; a volatility [put option](/option/) pays off if [volatility](/historical-volatility/) falls below the strike. These contracts allow traders to bet directly on market turbulence and are fundamental instruments in systematic [hedge fund](/hedge-fund/) strategies and volatility arbitrage.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and exotic options." />

<div class="wiki-infobox-caption">A derivative whose payoff is determined by turbulence, not price movement.</div>

|   |   |
|---|---|
| **What it is** | An [option](/option/) with payoff = f(realised or implied [volatility](/historical-volatility/)) rather than f(price) |
| **Underlying** | Volatility itself ([volatility](/historical-volatility/) of a stock, [index](/sp-500-index/), currency, or commodity) |
| **Volatility call** | Pays off if realised [volatility](/historical-volatility/) > strike; zeros out if below |
| **Volatility put** | Pays off if realised [volatility](/historical-volatility/) < strike; zeros out if above |
| **Strike** | Expressed as a [volatility](/historical-volatility/) level (%, annualised) rather than a price |
| **Main users** | Volatility traders, [hedge funds](/hedge-fund/), systematic strategies, market makers |

</aside>

## A bet on turbulence, not direction

Most [options](/option/) are bets on the direction and magnitude of price movement. A [call](/option/) profits if the underlying rises; a [put](/option/) profits if it falls. A volatility [option](/option/) is indifferent to direction. Instead, it profits from *how much* the underlying moves, regardless of which way.

Consider a volatility [call](/option/) on the [S&P 500](/sp-500-index/) with a 15% [volatility](/historical-volatility/) strike. If the index's realised [volatility](/historical-volatility/) over the [option's](/option/) life turns out to be 18%—whether the index rose or fell—the [call](/option/) is in-the-money. If realised [volatility](/historical-volatility/) lands at 12%, the [call](/option/) expires worthless. The trader profits purely from the market's turbulence, not from being right on direction.

This is powerful. It decouples the trader's bet from bullish or bearish views. A systematist who expects an earnings season to be chaotic but has no conviction on price direction can buy volatility [calls](/option/). A [hedge fund](/hedge-fund/) bracing for geopolitical shocks that could roil [currency markets](/currency-risk/) can purchase volatility [puts](/option/) on the [dollar](/us-dollar/) to hedge tail risk. A volatility arbitrageur can construct [spreads](/bid-ask-spread/) between implied and realised [volatility](/historical-volatility/) to scalp mispricings.

## Implied versus realised

The distinction is crucial. **Implied [volatility](/historical-volatility/)** is the [market](/stock-market/)'s forward-looking expectation, extracted from vanilla [option](/option/) prices via the [Black-Scholes](/black-scholes-model/) model or similar frameworks. **Realised [volatility](/historical-volatility/)** is the actual standard deviation of returns over the [option's](/option/) life, calculated retroactively.

A volatility [option](/option/) can settle on either. Most standardised volatility [options](/option/) (e.g., those trading on [exchanges](/stock-exchange/)) settle on realised [volatility](/historical-volatility/) calculated over the final 30 days before [expiration](/expiration-date/). Bespoke [over-the-counter](/over-the-counter-market/) volatility [options](/option/) may reference implied [volatility](/historical-volatility/) indices such as the VIX (implied [volatility](/historical-volatility/) of S&P 500 [options](/option/)).

This distinction creates trading opportunities. If a trader expects [implied volatility](/historical-volatility/) to rise sharply—perhaps because the [Federal Reserve](/federal-reserve/) is signalling an aggressive policy shift—she can buy a volatility [call](/option/) on the VIX or similar index. If she expects realised [volatility](/historical-volatility/) to stay subdued while implied [volatility](/historical-volatility/) is elevated, she can sell implied volatility and buy realised, pocketing the difference.

## Pricing and the volatility surface

Vanilla [options](/option/) are priced using the [Black-Scholes](/black-scholes-model/) model or related methods, which assume that all [options](/option/) on the same underlying with the same expiry have the same implied [volatility](/historical-volatility/). In reality, shorter-dated [options](/option/) and those further out-of-the-money often have different implied [volatilities](/historical-volatility/), creating a "[volatility smile](/volatility-smile/)" or skew.

Volatility [options](/option/) are priced using stochastic [volatility](/historical-volatility/) models—typically ones that assume [volatility](/historical-volatility/) itself follows a random process. A common model is the Heston model, which allows [volatility](/historical-volatility/) to mean-revert and jump. These models are complex and sensitive to calibration; two traders using different assumptions can price the same volatility [option](/option/) quite differently.

The intuition is straightforward: volatility [options](/option/) are [calls](/option/) or [puts](/option/) on a random variable ([volatility](/historical-volatility/)). Pricing them requires forecasting the distribution of future [volatility](/historical-volatility/), which in turn depends on historical mean-reversion rates, jump probabilities, and correlation with the underlying asset's returns.

## Why volatility deserves its own derivatives market

Volatility is an asset class unto itself. Large institutions [hedge](/over-the-counter-market/) volatility risk separately from price risk. A portfolio manager might be neutral on stock prices but exposed to volatility: if the market crashes, prices fall *and* implied [volatility](/historical-volatility/) spikes, compounding losses. Volatility [options](/option/) allow that manager to buy [volatility](/historical-volatility/) [insurance](/homeowners-insurance/) without necessarily shorting [stocks](/stock/).

Moreover, volatility [options](/option/) are far more liquid than the underlying vanilla [options](/option/) market in some cases. A trader can more easily adjust [volatility](/historical-volatility/) [exposure](/leverage-ratio-forex/) using volatility [swaps](/option/) or volatility [options](/option/) than by rebalancing hundreds of individual vanilla [calls](/option/) and [puts](/option/).

Historical returns on volatility [trading](/option/) strategies have been attractive—at least until recent years. Markets tend to overprice realised [volatility](/historical-volatility/) relative to actual outcomes (buyers overpay for "[volatility](/historical-volatility/) insurance"), creating systematic profits for sellers. However, tail events—flash crashes, pandemics, bank failures—have occasionally blown up volatility-selling strategies, underscoring the risks.

## Greeks and risk management

Volatility [options](/option/) have greeks analogous to vanilla [options](/option/), but reinterpreted. **[Vega](/vega/)** is the sensitivity of a vanilla [option](/option/) price to changes in implied [volatility](/historical-volatility/). For a volatility [option](/option/), the closest analogue is **[gamma](/gamma/)** on [volatility](/historical-volatility/)—the convexity of the [option's](/option/) payoff with respect to realised [volatility](/historical-volatility/).

[Theta](/theta/) (time decay) works against volatility [option](/option/) buyers. As [expiration](/expiration-date/) approaches, the [option](/option/) loses time value, especially if realised [volatility](/historical-volatility/) is near the strike. Volatility [option](/option/) sellers exploit this decay, selling and holding short [volatility](/historical-volatility/) [exposure](/leverage-ratio-forex/) in the hope that realised [volatility](/historical-volatility/) stays low.

## Real-world applications

**Volatility arbitrage**: A desk notices that the VIX is elevated (implied [volatility](/historical-volatility/) is high) while historical [volatility](/historical-volatility/) is subdued. They sell a volatility [call](/option/) and buy vanilla [puts](/option/) to hedge, profiting if the mismatch corrects.

**Tail risk hedging**: A [hedge fund](/hedge-fund/) buys volatility [calls](/option/) as [insurance](/homeowners-insurance/) against market dislocations. These are expensive but have saved many funds during crises.

**Systematic rebalancing**: A [volatility](/historical-volatility/) targeting fund adjusts [leverage](/leverage-ratio-forex/) inversely to market [volatility](/historical-volatility/). Volatility [options](/option/) help them hedge against the [volatility](/historical-volatility/) of their own [volatility](/historical-volatility/) measures.

**Speculation**: A trader convinced that a central bank announcement will trigger a [volatility](/historical-volatility/) spike buys a volatility [call](/option/) to express the view cheaply and with defined [risk](/credit-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative contract
- [Implied volatility](/historical-volatility/) — the market's expectation of future [volatility](/historical-volatility/), embedded in vanilla [option](/option/) prices
- [Historical volatility](/historical-volatility/) — realised [volatility](/historical-volatility/) observed in past price movements
- [Volatility smile](/volatility-smile/) — the curve of implied [volatility](/historical-volatility/) across different strikes
- [Vega](/vega/) — sensitivity of an [option](/option/) price to changes in implied [volatility](/historical-volatility/)
- [Black-Scholes model](/black-scholes-model/) — the standard tool for [option](/option/) pricing
- [Over-the-counter market](/over-the-counter-market/) — where most volatility [options](/option/) trade

### Wider context

- [Hedge fund](/hedge-fund/) — primary traders of volatility [options](/option/)
- [Theta](/theta/) — time decay, a key greek in volatility [options](/option/)
- [Gamma](/gamma/) — convexity; important for volatility [option](/option/) payoffs
- [Speculation](/stock-market/) — a common use of volatility [options](/option/)
- [Risk management](/counterparty-risk/) — hedging via volatility [options](/option/)

</div>

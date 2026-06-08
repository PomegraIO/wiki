---
title: "Realized Volatility vs Implied Volatility: What the Gap Means for Risk"
description: "Realized volatility measures past price swings; implied volatility forecasts future moves from option prices. The gap between them signals market mispricing and sentiment."
keywords:
  - realized volatility vs implied volatility difference
  - implied volatility interpretation
  - volatility smile trading
  - realized vs expected volatility
  - option pricing volatility
image: /svg/risk.svg
---

*Volatility comes in two flavors. **Realized volatility** measures what already happened—the actual price swings an asset experienced over a past period. **Implied volatility** is what traders expect: the level of future price movement embedded in [option](/option/) prices today. When implied volatility sits well above realized, the market is pricing in surprise. When it falls below, traders are complacent. Understanding the gap is essential to gauging whether options are expensive, whether risk is being properly priced, and where market sentiment may be misaligned with reality.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Realized vs Implied Volatility — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">Realized is backward-looking; implied is forward-looking. The gap reveals whether the market is overestimating or underestimating future risk.</div>

|   |   |
|---|---|
| **Realized volatility** | Historical measure; standard deviation of past returns over a fixed window (10, 20, 60 days) |
| **Implied volatility** | Forward-looking; extracted from [option](/option/) prices using [Black-Scholes](/black-scholes-model/) or similar models |
| **Gap meaning** | Implied > Realized: market fears upcoming shock; Implied < Realized: complacency; market may be underpricing risk |
| **Why it matters** | Options are expensive when implied is high; cheap when low. The gap signals whether hedging is worth its cost |
| **Volatility smile** | Implied volatility varies by strike price; typically rises for out-of-the-money [puts](/put-option/), signaling tail-risk fears |
| **Term structure** | Near-term and far-term implied volatility can diverge; reveals whether shock is expected soon or later |
| **Market timing signal** | Historically, spikes in implied volatility often mark short-term bottoms for price; low implied often precedes volatility jumps |

</aside>

## Realized Volatility: The Rearview Mirror

Realized volatility is simple and mechanical. Take an asset's daily returns over the past 20 trading days, calculate the standard deviation, and annualize it (multiply by the square root of 252 trading days per year). The result is a number—say, 18%—that tells you how much, on average, the asset bounced around.

Realized volatility is observable and backward-looking. It cannot lie (though it can be calculated different ways: closing-to-closing, high-to-low, Parkinson, Garman-Klass estimators). A stock that rose and fell 2% daily has 20-day realized volatility around 28% annualized. One that moved 0.5% daily has volatility around 7%.

The key insight: realized volatility is history. It tells you what has already occurred and is useful as a baseline for understanding an asset's typical behavior. But it says nothing about what comes next. A stock can have 10% realized volatility and then gap 15% on earnings. The past volatility was calm; the future was not.

## Implied Volatility: The Market's Forecast

[Option](/option/) prices contain a forecast. A [call option](/call-option/) on Apple stock expiring in 30 days, struck at-the-money, trades at a certain price. Using the [Black-Scholes](/black-scholes-model/) model or other pricing frameworks, traders reverse-engineer what future volatility the market is implying. If Apple is trading at $150, a $150 call is worth more if traders expect large moves in the next month than if they expect small moves.

That implied volatility is the market's collective bet on future swings. It is forward-looking, but it is also subjective—a consensus of traders' opinions, not a hard fact. Two traders can disagree on what volatility will be; they will demand different option prices. The market price settles somewhere in between.

Implied volatility is extracted from traded option prices, not calculated from past returns. It depends on current supply and demand for options, fear levels, positioning, and expected catalysts (earnings, central bank decisions, geopolitical events). High demand for [put options](/put-option/) (insurance against declines) drives implied volatility up, even if past volatility was low.

## The Gap: When Forecasts Diverge from History

The real insight lies in comparing the two. When implied volatility is much higher than realized volatility—say, realized is 15% but implied is 30%—the market is pricing in a significant shift. Traders expect larger moves ahead. Reasons could include:

- **Earnings uncertainty.** A stock is about to announce results; options get expensive.
- **Central bank decision.** A [Federal Reserve](/federal-reserve/) meeting is coming; FX options spike in implied volatility.
- **Geopolitical event.** Tensions rise; volatility options rise in price.
- **Tail-risk hedging demand.** Investors are rushing to buy [protective puts](/protective-put/); demand drives implied volatility up even if history does not justify it.

When implied is lower than realized—say, realized is 25% but implied is 12%—the market may be complacent. History shows turbulence; the options market is pricing calm. This often precedes volatility spikes; it is a warning that hedging is cheap and often a good time to buy [put options](/put-option/).

## The Volatility Smile and Tail Risk

Implied volatility is not constant across all [strike prices](/strike-price/). A [call option](/call-option/) deep out-of-the-money (struck far above the current price) sometimes has higher implied volatility than an at-the-money call, even though both expire on the same day. Similarly, [put options](/put-option/) struck far below the current price often have much higher implied volatility.

This pattern, called the **volatility smile** (or skew), reveals that traders fear extreme outcomes more than the [Black-Scholes](/black-scholes-model/) model, which assumes constant volatility, would suggest. The smile is a sign of tail-risk awareness: traders are willing to pay more for protection against 10–20% declines than a simple model would indicate.

The smile flattens when fear subsides. It steepens when tail risk is top-of-mind. Monitoring the smile is a way to gauge fear without looking at absolute implied volatility levels—it is the shape of the fear that matters.

## Volatility Term Structure

Implied volatility also varies by expiration date. A 30-day implied volatility might be 20%, while 180-day implied is 16%. Or the reverse: near-term spiking, far-term calm (suggesting traders expect a near-term shock to dissipate). This term structure reveals when the market expects risk.

A steep upward term structure (30-day implied high, far-term low) suggests an imminent catalyst—earnings, a policy decision—after which calm returns. A flat or inverted structure (near-term calm, far-term high) suggests diffuse risk: not an immediate shock, but instability expected to build.

## Trading the Gap: Signals and Risks

Many traders use the gap between realized and implied to time entries and exits:

- **Implied >> Realized:** Options are expensive. Consider selling [call options](/call-option/) ([covered call](/covered-call/)) or buying stock if fundamentals support it (selling "volatility" when it spikes is often profitable, though risky).

- **Implied << Realized:** Options are cheap. Buy [put options](/put-option/) as insurance or sell stock if momentum is weak.

The catch: implied volatility spikes often precede market bottoms. The worst time to buy hedging is after the market has already declined—but that is when implied volatility is highest. Conversely, the market tends to crater when implied is very low, just after hedging got cheap.

There is no free lunch. High implied volatility means protection is expensive (good time to sell insurance, bad time to buy it). Low implied means protection is cheap (good time to buy, but the market is often about to decline, so hedging is urgently needed).

## Real-World Patterns

Historical data shows persistent patterns in the realized–implied gap:

- **VIX spikes precede lows.** The [VIX](/volatility-smile/) (implied volatility index for S&P 500 [options](/option/)) has spiked to 40–80 during crashes. Within weeks, markets often recover, and the VIX drops back to 15–20. Traders who bought hedging at the peak often regret it; those who bought near the peak and held are vindicated.

- **Realized volatility is mean-reverting.** A stock with 50% realized volatility is unlikely to maintain that forever. It tends to revert to its long-term average (say, 25%). Implied volatility often overestimates the duration of spikes.

- **Positive correlation with returns.** In equity markets, implied volatility usually rises when prices fall (and vice versa). A decline of 5% is often accompanied by a jump in implied volatility. This relationship is asymmetric: declines come with higher volatility jumps than gains.

## The Takeaway: Assessing Risk Pricing

A trader or risk manager comparing realized and implied volatility is asking: is the market pricing in the right amount of future risk? If history (realized) is stormy but the options market (implied) is pricing calm, either traders are not paying attention, or they believe the storm will pass. If implied is sky-high and realized is tame, traders are either braced for a shock or overestimating the odds.

Neither is automatically wrong. The market's forecast can be poorly calibrated. But the gap is a signal worth reading. It tells you whether hedging is expensive, whether the crowd is fearful or complacent, and whether positioned bets are likely to age well or blow up.

## See also

<div class="wiki-seealso">

### Closely related

- [Implied volatility](/realized-volatility-vs-implied-volatility/) — extracted from option prices; forward-looking expectation of future risk
- [Black-Scholes model](/black-scholes-model/) — theoretical framework for option pricing; yields implied volatility
- [Option](/option/) — derivative contract whose price embeds volatility expectations
- [Volatility smile](/volatility-smile/) — pattern in implied volatility across strikes; signals tail-risk fears
- [Put option](/put-option/) — commonly bought for hedging; expensive when implied volatility is high

### Wider context

- [Historical volatility](/historical-volatility/) — another name for realized volatility; backward-looking measure
- Risk — core concept; volatility is one measure of it
- [Time decay (theta)](/time-decay-theta/) — option value deteriorates; realized vs implied volatility determines whether decay helps or hurts the holder
- [Protective put](/protective-put/) — strategy that buys insurance; expensive when implied volatility is high
- [Covered call](/covered-call/) — strategy that sells insurance; profitable when implied is high vs realized

</div>

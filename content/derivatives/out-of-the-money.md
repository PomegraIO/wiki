---
title: "Out-of-the-Money"
description: "Out-of-the-money describes an option with no intrinsic value because exercising it would be immediately unprofitable."
keywords:
  - out-of-the-money
  - otm
  - option value
  - time value
  - moneyness
image: "https://picsum.photos/seed/out-of-the-money/900/600"
---

*An option is **out-of-the-money (OTM)** when exercising it would not be immediately profitable. For a [call option](/call-option), this means the [stock](/stock) price is below the [strike price](/strike-price). For a [put option](/put-option), this means the stock price is above the strike. Out-of-the-money options have zero [intrinsic value](/intrinsic-value) and are worth only their [time value](/time-value), reflecting the probability and magnitude of becoming [in-the-money](/in-the-money) before [expiration date](/expiration-date).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Out-of-the-Money — key facts</div>

<img src="https://picsum.photos/seed/out-of-the-money/900/600" alt="A stock price line below a strike level" />

<div class="wiki-infobox-caption">Out-of-the-money options have zero intrinsic value.</div>

|   |   |
|---|---|
| **Call OTM condition** | Stock price < strike price |
| **Put OTM condition** | Stock price > strike price |
| **Intrinsic value** | Zero |
| **Time value** | All of the option's value |
| **Price decays to** | Zero at expiration (if OTM) |
| **Delta** | Lower; for OTM calls, typically 0.1 to 0.5 |
| **Probability of profit** | Lower than ITM, depends on time and volatility |
| **Leverage** | High; small stock move = large % return |
| **Risk** | Capped at premium paid |
| **Time decay impact** | Accelerates as expiration nears |

</aside>

## OTM for calls and puts

A [call option](/call-option) is out-of-the-money if the underlying [stock](/stock) price is below the [strike price](/strike-price). A $100 strike call is OTM if the stock trades at $95, $80, $50, or any price below $100.

A [put option](/put-option) is out-of-the-money if the underlying stock price is above the strike. A $100 strike put is OTM if the stock is at $105, $120, $200, or any price above $100.

The logic mirrors calls: a call holder wants to buy at the strike, so OTM means the market price is lower (you would not want to exercise). A put holder wants to sell at the strike, so OTM means the market price is higher (you would not want to exercise).

## All value is time value

An out-of-the-money option has zero [intrinsic value](/intrinsic-value) and all of its value comes from [time value](/time-value). This [time value](/time-value) represents the market's bet that the option will become [in-the-money](/in-the-money) before expiration.

An OTM [call option](/call-option) is worth something only if there is a chance the stock will rise above the strike before expiration. An OTM [put option](/put-option) is worth something only if there is a chance the stock will fall below the strike. The longer the time to [expiration date](/expiration-date) and the higher the [volatility](/historical-volatility), the more likely that outcome is, and the higher the [time value](/time-value).

At expiration, any remaining OTM option expires worthless. The entire [time value](/time-value) evaporates. This is why [theta](/theta) (time decay) is the dominant risk for OTM option buyers—the option loses value daily as expiration nears and the chance of reversal shrinks.

## Cheap but risky

Out-of-the-money options are cheap because they have no intrinsic value and lower probability of finishing [in-the-money](/in-the-money). A call struck at $120 on a $100 stock is much cheaper than a call struck at $100, because the stock must rise 20% to make the $120 call profitable.

This cheapness creates leverage for buyers. You can control more stock exposure with less capital. An OTM call bought at $0.50 that finishes $5 in-the-money at expiration returns 1000%—a spectacular return on the premium paid.

But the flip side is frequent total loss. Most OTM options expire worthless. If you buy ten OTM calls betting on 10% moves, and the stock does not move enough, you lose money on all ten. The returns are binary: either the big win or the small loss.

## Delta and movement sensitivity

Out-of-the-money options have low [delta](/delta), meaning they do not move much with the underlying stock's price. An OTM call deep out of the money might have a [delta](/delta) of 0.1, meaning a $1 move in the stock translates to $0.10 movement in the option price.

This low [delta](/delta) is why small account traders sometimes avoid OTM options for hedging; they require the stock to move a lot before the option price responds significantly. But it is also why OTM options are cheap to buy and useful for leverage plays.

## Volatility's outsized impact

[Implied volatility](/implied-volatility) has a much larger percentage impact on OTM options than on [in-the-money](/in-the-money) options. An OTM call's entire value is [time value](/time-value), which depends directly on the market's estimate of volatility. If [volatility](/historical-volatility) spikes from 20% to 40%, an OTM call might double in value even if the stock price does not move.

This makes OTM options useful for pure [volatility](/historical-volatility) plays, independent of direction. An investor bullish on volatility but neutral on direction might buy OTM calls and puts together—if volatility spikes, both gain.

## Use cases and strategies

OTM options are the core of leverage strategies. Traders with a small amount of capital buy OTM calls or puts to capture large moves without the capital to own stock or buy ATM options.

They are also used in spreads: a bull-call-spread buys an ATM call and sells an OTM call, capping upside to reduce cost. A bear-put-spread buys an OTM put and sells an ATM put, capping downside while reducing premium paid.

Portfolio managers buy OTM puts on indices as tail-risk hedges—cheap insurance for catastrophic market crashes that would otherwise wipe out significant portfolio value.

## Time decay acceleration

OTM options suffer the most from [theta](/theta) decay as expiration nears. Early in an option's life, a far-OTM option loses [time value](/time-value) slowly. But in the final week, decay accelerates. An OTM option with 1 day to expiration might lose 20–30% of its remaining value in hours, as the probability of finishing [in-the-money](/in-the-money) plummets.

This is why timing is critical for OTM option buyers. Buying a far-OTM option with high [time value](/time-value) and selling it after [volatility](/historical-volatility) spikes (which increases [time value](/time-value)) can be profitable, independent of the stock's direction.

## See also

<div class="wiki-seealso">

### Closely related

- [In-the-money](/in-the-money/) — opposite; profit built in
- [At-the-money](/at-the-money/) — stock exactly at strike
- [Call option](/call-option/) — OTM when stock < strike
- [Put option](/put-option/) — OTM when stock > strike
- [Strike price](/strike-price/) — the reference level
- [Time value](/time-value/) — entire value for OTM options

### Greeks and valuation

- [Delta](/delta/) — lower for OTM options
- [Gamma](/gamma/) — significant for near-OTM options
- [Theta](/theta/) — rapid decay for OTM as expiration nears
- [Vega](/vega/) — outsized impact for OTM
- [Implied volatility](/implied-volatility/) — critical for OTM pricing

### Strategies

- Bull call spread — sells OTM call to cap upside
- Bear put spread — buys OTM put for downside
- Iron condor — sells both OTM calls and puts
- Straddle — buys OTM call and put

### Deeper context

- [Option](/option/) — the family of derivatives
- Leverage — OTM options provide high leverage
- [Volatility plays](/volatility-smile/) — OTM options sensitive to volatility changes

</div>

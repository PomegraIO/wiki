---
title: "Moneyness"
description: "The relationship between an option's strike price and the current price of the underlying, measured as a ratio or percentage difference."
---

*Moneyness describes whether an option is [in-the-money](/wiki/in-the-money/), [at-the-money](/wiki/at-the-money/), or [out-of-the-money](/wiki/out-of-the-money/) by comparing the [strike price](/wiki/strike-price/) to the spot price. More formally, moneyness is often expressed as a ratio: for a call, moneyness = spot ÷ strike; for a put, moneyness = strike ÷ spot. A ratio above 1.0 means in-the-money for calls. This simple lens helps traders quickly assess whether an option has [intrinsic value](/wiki/intrinsic-value/) or is entirely dependent on [time value](/wiki/time-value/).*

## The three states of moneyness

For a [call option](/wiki/call-option/): in-the-money if spot > strike (you'd profit exercising now); at-the-money if spot ≈ strike; out-of-the-money if spot < strike (exercising would lock in a loss). For a [put option](/wiki/put-option/): in-the-money if spot < strike; at-the-money if spot ≈ strike; out-of-the-money if spot > strike. This is the foundation of all options thinking. An option's value consists of intrinsic value (how far in-the-money it is) plus time value (the probability and magnitude of further movement before expiration).

## Moneyness drives option behavior

Deep in-the-money options behave like the underlying stock—[delta](/wiki/delta/) near 1.0, moving dollar-for-dollar with spot. Out-of-the-money options are speculative—delta near zero, their value driven purely by [gamma](/wiki/gamma/) and [theta](/wiki/theta/)—and are sensitive to [implied volatility](/wiki/implied-volatility/) swings. At-the-money options strike a balance, experiencing both intrinsic value changes and volatility changes. Knowing moneyness tells you what drives the option's price behavior.

## Moneyness and break-even at expiration

A call holder's break-even at expiration is the strike plus the [premium](/wiki/option-premium/) paid. A $100 call purchased for $3 breaks even at $103—the stock must rise that far just to recover the cost. Similarly, a put holder's break-even is the strike minus the premium. The further out-of-the-money the option, the more room the underlying must move just to break even. This is why out-of-the-money options are cheaper but also less likely to profit.

## Moneyness and probability

Market prices embed rough probability estimates. An at-the-money option has roughly 50% probability of finishing in-the-money at expiration (this varies with volatility, time, and interest rates). Deep in-the-money options have high probability of expiring in-the-money. Deep out-of-the-money options have very low probability. The further out-of-the-money, the cheaper the option but also the lower the odds of profit. This creates a risk-reward spectrum that traders exploit: buying cheap out-of-the-money calls (lottery tickets) vs. selling expensive in-the-money calls (high probability income).

## Moneyness affects Greeks

[Delta](/wiki/delta/) scales with moneyness: in-the-money calls have delta closer to 1.0; out-of-the-money calls have delta closer to 0.0. [Gamma](/wiki/gamma/) is highest at-the-money and decays away for deep moneyness extremes. [Vega](/wiki/vega/) (sensitivity to volatility) is also highest at-the-money. [Theta](/wiki/theta/) (time decay) is concentrated in at-the-money and slightly in-the-money options. Understanding moneyness helps predict how Greeks will behave as the underlying moves.

## Moneyness in multi-leg strategies

Constructing [vertical spreads](/wiki/vertical-spread/), [straddles](/wiki/straddle/), and other strategies requires choosing strikes and thus moneyness. A [bull call spread](/wiki/bull-call-spread/) might buy an at-the-money call (high delta, expensive) and sell an out-of-the-money call (low delta, cheap), balancing upside potential with cost. Understanding moneyness makes strike selection intuitive.

## Spot-strike ratio vs. percentage difference

Some traders use spot ÷ strike (the moneyness ratio); others use (spot − strike) ÷ strike (the percentage difference). Both are useful. A ratio of 1.10 means 10% in-the-money; a percentage of 10% means the same. The ratio approach is cleaner for lognormal models used in pricing; the percentage approach is more intuitive for casual traders.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/in-the-money/">In-the-money</a> — option with intrinsic value.</li>
<li><a href="/wiki/out-of-the-money/">Out-of-the-money</a> — option with no intrinsic value.</li>
<li><a href="/wiki/at-the-money/">At-the-money</a> — strike equal to spot.</li>
<li><a href="/wiki/intrinsic-value/">Intrinsic value</a> — value from moneyness alone.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/strike-price/">Strike price</a> — the strike component of moneyness.</li>
<li><a href="/wiki/delta/">Delta</a> — the Greek most affected by moneyness.</li>
<li><a href="/wiki/option/">Option</a> — the contract being evaluated.</li>
</ul>
</div>

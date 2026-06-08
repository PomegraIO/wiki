---
title: "Charm: How Delta Changes as Expiration Approaches"
description: "The charm Greek measures how fast an option's delta decays as expiration nears, crucial for traders rehedging delta-neutral positions overnight."
keywords:
  - charm greek delta decay
  - delta decay rate expiration
  - charm rate option greeks
  - delta drift time decay
  - gamma vs charm
image: /svg/derivatives.svg
---

*Charm, also called **delta decay rate**, measures how quickly an option's [delta](/delta/) changes over a single day (or infinitesimal time increment) purely from the passage of time, independent of any price move in the underlying. As expiration approaches, charm becomes larger and more volatile—especially for at-the-money options—forcing delta hedgers to rebalance their [hedging](/derivatives-hedging/) positions more frequently or accept larger unhedged gaps.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Charm (Delta Decay) — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The rate at which delta erodes or grows purely from the ticking clock.</div>

|   |   |
|---|---|
| **What it measures** | Daily change in delta due to time decay alone |
| **Sign convention** | Positive charm = delta grows, negative = delta shrinks |
| **Highest magnitude** | At-the-money options, especially close to expiry |
| **Time dependence** | Grows (in absolute value) as expiration approaches |
| **Relation to gamma** | Charm = ∂delta/∂time; gamma = ∂delta/∂price |
| **Practical horizon** | Hours to days; crucial for overnight hedges |
| **Common nickname** | "DvegaDtime" when tracking vega's time decay |

</aside>

## What charm measures and why it matters

An option's [delta](/delta/) tells you how many shares of stock you must own to offset a short call (or how many to short to offset a long call) to stay neutral to price moves. But delta is not static. Even if the stock price never budges, the delta shifts overnight because time decay affects the probability landscape.

Charm quantifies this shift. It is the **partial derivative of delta with respect to time**: how many basis points of delta you lose (or gain) per day, holding all other inputs constant. For a delta hedger, charm is essential. If you were delta-neutral yesterday but held the position through the night, you are likely not delta-neutral anymore because charm has nudged your delta. Depending on option type, moneyness, and time to expiry, that shift could be tiny or significant.

Near expiration, charm explodes. An at-the-money call with one week to go might have charm of −0.15 (losing 15 basis points of delta per day). The same call with one day to go could have charm of −0.50 or worse. This is why option traders focus intensely on intraday rebalancing in the final days before expiry: a 50-basis-point delta drift is material enough that even a small portfolio can swing from hedged to unhedged in hours.

## The relationship between charm and gamma

[Gamma](/gamma/) measures how much delta changes per 1% move in the underlying stock price. Charm measures how much delta changes per unit of time. They are related: gamma and theta (time decay) combine to determine charm.

The intuition: as an option decays toward expiration with an unchanged stock price, the probability distribution tightens. If a call is out-of-the-money with one month left, time decay gradually lowers the probability it ends in-the-money, shrinking delta. If a call is in-the-money with one month left, time decay shrinks the probability it expires out-of-the-money, but the effect on delta is smaller. At-the-money calls experience the *largest* probability shift per unit time, so charm is highest there.

## How charm changes by moneyness

An out-of-the-money call has low delta (close to zero). As expiration approaches, that delta continues toward zero, so charm is negative—delta is decaying. The magnitude of charm grows as expiry nears.

An in-the-money call has high delta (close to one). As expiration approaches, delta gravitates toward one, so charm is positive—delta is growing. Again, the magnitude is highest very close to expiry.

At-the-money calls sit on the knife's edge. With weeks to expiry, delta hovers near 0.50 and charm is small. But in the final days, gamma and theta compress the outcome space violently. The delta can swing 0.05 or more in a single session with no price move, meaning charm jumps to large negative or positive values depending on the moment and which path the underlying takes.

## Charm near expiration: the danger zone

This is where charm bites traders. Suppose a hedge fund is short an at-the-money call on Apple stock (or a basket of options) with two days to expiration. The portfolio is delta-neutral because it owns shares to offset the short call. That overnight, time decay compresses the outcome probabilities. The short call's delta might swing from 0.50 to 0.48 or 0.52 just from the calendar turning. Multiply by millions of dollars of notional exposure, and a "small" charm shift becomes a six- or seven-figure unhedged gap.

Professional market makers handle this by rehedging continuously—sometimes intraday—as expiration nears. Retail traders or less-liquid portfolios may accept the risk or hedge more conservatively (for example, selling some of the short call rather than trying to stay perfectly delta-neutral).

## Charm's sign and interpretation

Charm is usually expressed as:
- **Negative for out-of-the-money calls and in-the-money puts**: these lose delta as expiration approaches (probability of finishing in-the-money decays).
- **Positive for in-the-money calls and out-of-the-money puts**: these gain delta as expiration approaches.
- **Largest magnitude at-the-money**, where the probability landscape is flattest and most sensitive to time compression.

The sign tells you the direction of delta drift; the magnitude tells you how fast. A charm of −0.20 on a call means the delta drops 0.20 (20 basis points) per day, all else equal.

## Practical example: rehedging a short call

Assume you are short one at-the-money call on a $100 stock with delta 0.50 and charm −0.15. You are hedged with 50 shares long.

Next day, the stock is still at $100. But the delta has decayed to 0.485 (you sold 0.015 of delta just from time passing). You are now long 50 shares against a short call that has delta 0.485—you are over-hedged by 0.015, or about $1.50 per share of notional exposure. 

If you manage a $100 million portfolio of options, that $1.50 of drift per share becomes material. You would sell a small amount of the stock to re-neutralize. Multiply this across thousands of daily adjustments, and transaction costs and slippage accumulate. This is why charm matters most to high-frequency traders and large institutional hedgers: they have the scale and technology to rebalance cheaply.

## Charm in a rising or falling rate environment

Charm also interacts with interest rates. As risk-free rates rise, the cost of carry on the underlying increases, shifting the probability distribution slightly and affecting charm. This secondary effect is usually small compared to the direct time-decay component, but it matters for precision hedging and for traders holding positions through central bank meetings or economic data releases.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the primary Greek charm measures; the rate of change of option value with respect to underlying price
- [Gamma](/gamma/) — the rate at which delta changes with underlying price; complements charm as a measure of portfolio sensitivity
- [Theta](/theta/) — the pure time-decay component; closely related to charm but measures total value loss, not just delta shift
- [Option](/option/) — the fundamental derivative contract whose Greeks are being analyzed
- [Volatility Smile](/volatility-smile/) — how implied volatility varies across strikes, affecting charm indirectly

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why traders track and rebalance charm to stay neutral
- [Time Decay Theta](/time-decay-theta/) — the broader time effect on option prices
- [Time Value](/time-value/) — the portion of an option's premium reflecting remaining life
- [Vega](/vega/) — the Greek measuring sensitivity to volatility changes

</div>

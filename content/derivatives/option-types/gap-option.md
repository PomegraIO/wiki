---
title: "Gap Option"
description: "An option contract where the strike determining exercise differs from the strike setting the payoff, creating a payout cliff."
keywords:
  - gap option
  - binary option
  - exercise strike
  - payoff strike
  - exotic option
  - forward contract
image: "/svg/derivatives.svg"
---

*A **gap option** is an [option](/option/) where the strike price that triggers exercise differs from the strike price used to calculate the payoff. Rather than exercising and receiving the intrinsic value at a single strike, the holder waits for one price level to activate the option, then collects profit based on a second, higher (for calls) or lower (for puts) level.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gap Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A bifurcated strike structure that creates a payoff discontinuity.</div>

|   |   |
|---|---|
| **What it is** | An [option](/option/) with separate exercise and payoff strikes |
| **Exercise strike** | Triggers automatic or mandatory exercise |
| **Payoff strike** | Determines the settlement amount once triggered |
| **Also called** | Binary option, trigger option |
| **Payoff shape** | Flat below exercise strike, then steps up (calls) or down (puts) |
| **Primary use** | Speculating on gap moves; hedging discrete price risk |
| **Trader advantage** | Customizable sensitivity to crossing specific price barriers |

</aside>

## How the payoff structure works

A standard [call option](/option/) at strike K pays max(S − K, 0) at expiry, where S is the spot price. A gap call divides this into two strikes: an exercise trigger E and a payoff strike P, where typically P > E (for calls). Once the stock closes at or above E, exercise occurs automatically or the holder exercises. Payoff is then max(S − P, 0).

The effect is striking: if the stock rallies from 95 to 105, a standard call struck at 100 pays 5. A gap call with exercise strike 100 but payoff strike 108 pays nothing until the stock climbs past 108—a cliff drop at the boundary. Cross it, and the payoff accelerates sharply. This creates a non-linear [time decay](/time-decay-theta/) and [gamma](/gamma/) profile that pure vanilla options cannot replicate.

## Why traders use gap options

Speculators deploy gap calls ahead of earnings or macroeconomic announcements when they expect a large, directional move. If you believe a stock will jump 8% through a round-number barrier, a gap option lets you concentrate risk: you collect nothing until that level, but payoff explodes once breached. It's cheaper than buying further out-of-the-money vanilla calls because the probability of touching E is higher than touching P.

Hedgers use gap puts in reverse. A corporate treasurer worried that a foreign currency might depreciate only to a certain floor—say, a 4% loss before support—can buy a gap put with exercise at that floor and payoff at a lower strike. Below the support, large adverse moves are covered; above, the company self-insures the smaller swing.

## The pricing mechanics

A gap option's [premium](/option-premium/) reflects two competing forces. First, the gap shrinks the probability of profitable payoff, pushing price down versus a vanilla option at strike P. Second, the exercise trigger at E is easier to reach, pulling price up. The net effect depends on the gap size, [volatility](/historical-volatility/), and time to [expiration](/expiration-date/). Wider gaps are cheaper; narrower ones approach vanilla pricing.

[Black-Scholes](/black-scholes-model/) models compute gap option value by splitting the calculation: probability of touching E times conditional payoff given that S ≥ E. In practice, traders adjust [vega](/vega/) (volatility sensitivity) upward because gap options embed a discrete binary element—a small move in [implied volatility](/implied-volatility/) can shift the gap's value sharply if the spot price sits near the exercise barrier.

## Relationship to other exotic structures

Gap options sit on a spectrum between vanilla calls and [binary options](/option/). A binary pays a fixed amount if triggered; a gap pays the difference between spot and a lower payoff strike, blending binary and vanilla logic. They also resemble [forward contracts](/forward-contract/) dressed as options: once the exercise strike is hit, payoff is predetermined by the payoff strike, reducing the exercise decision to a mechanical trigger.

This design makes them attractive to institutions that want leverage without holding outright [futures](/futures-contract/). A hedge fund can buy a gap call and capture a large directional move with a small premium outlay, then exit or roll the position before expiry if market conditions shift.

## Risks and practical limits

The discontinuity creates [gamma](/gamma/) risk: spot price hovering near the exercise strike is explosive. A small adverse move wipes the option near-worthless; a small favourable move can double its value. [Vega](/vega/) spikes similarly; a volatility crush late in the option's life can collapse payoff even if the stock remains above E but below P.

Liquidity is a second constraint. Gap options are rare in retail markets and typically trade over-the-counter or only on select exchanges for index options. Bid-ask spreads are wide, and pricing models assume assumptions about [volatility surfaces](/volatility-smile/) that may not hold in stressed markets. Exiting early is difficult.

Finally, exercise mechanics matter. Some gap options exercise automatically upon hitting the trigger; others require the holder to choose. Automatic exercise can force the holder into a forward position at an unfavourable time. Manual exercise gives optionality but requires active monitoring.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational definition of calls, puts, and premiums
- [Option Premium](/option-premium/) — pricing and factors driving cost
- [Implied Volatility](/implied-volatility/) — market expectation of future price swings
- [Black-Scholes Model](/black-scholes-model/) — mathematical framework for option valuation
- [FLEX Option](/flex-option/) — exchange-listed customizable option contracts
- [Strike Price](/strike-price/) — the reference price for option payoff

### Wider context

- [Forward Contract](/forward-contract/) — similar payoff structure but binding obligation
- [Futures Contract](/futures-contract/) — leveraged price exposure with daily settlement
- [Volatility Smile](/volatility-smile/) — non-flat implied volatility surface at different strikes
- [Time Decay Theta](/time-decay-theta/) — erosion of option value as expiry approaches

</div>

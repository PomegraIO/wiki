---
title: "Vega Bucketing"
description: "The practice of decomposing a portfolio's volatility exposure by expiry tenor to reveal term-structure risk."
keywords:
  - vega bucketing
  - vega risk
  - term structure
  - volatility curve
  - portfolio Greeks
image: "/svg/derivatives.svg"
---

*A **vega bucket** is a grouping of options positions by their time-to-expiry (tenor), allowing a trader to see which parts of the volatility curve they are long or short. Rather than managing total [vega](/vega/) as a single number, bucketing reveals that a portfolio might be long 3-month volatility but short 12-month volatility—a critical distinction for risk management and hedging.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vega Bucketing — term-structure risk visibility</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and volatility curves." />

<div class="wiki-infobox-caption">Decomposing volatility exposure by expiry reveals hidden mismatches.</div>

|   |   |
|---|---|
| **What it is** | Segmenting a portfolio's [vega](/vega/) exposure by time-to-expiry |
| **Also called** | Vega ladder, tenor bucketing, volatility bucketing |
| **Typical buckets** | 1-week, 1-month, 3-month, 6-month, 1-year, 2-year+ |
| **Primary use** | Risk monitoring, hedging decisions, greeks analysis |
| **Key insight** | The same total vega can hide very different term-structure bets |

</aside>

## Why total vega is misleading

Suppose a trader's options book shows a total [vega](/vega/) of £0. Sounds hedged, right? Not necessarily. The trader could be long 100 contracts of 1-month calls (vega +50) and short 100 contracts of 12-month calls (vega −50). Aggregate [vega](/vega/) is zero, but the positions are exposed to completely different risks.

If the volatility curve steepens—short-term volatility rises sharply while long-term volatility is stable—the book loses money: the long 1-month vega gains value as [implied volatility](/implied-volatility/) rises, but the 12-month shorts do not. Conversely, if the curve flattens, the 12-month shorts gain while 1-month shorts lose. This is **curve risk**, and it's invisible to an aggregate vega number.

## Constructing vega buckets

A trader (or risk manager) divides the portfolio's positions into time buckets. Common ones are 1-week, 1-month, 3-month, 6-month, 1-year, and 2-year-or-longer. For each bucket, they sum the [vega](/vega/) of all options expiring or closest to that tenor.

For example:
- 1M bucket: vega of all 1-month options, weighted by distance from expiry
- 3M bucket: vega of all 3-month-ish options
- 1Y bucket: vega of all ~1-year options
- And so on

Each bucket might show positive or negative vega. If the 3M bucket reads +1000 and 1Y reads −800, the trader is long 3-month volatility and short 1-year volatility—a [curve risk](/credit-spread/) bet. This structure makes curve exposure explicit.

## The volatility curve and term structure

The volatility curve plots [implied volatility](/implied-volatility/) on the y-axis against time-to-expiry on the x-axis. In normal markets, short-term and long-term volatility move together, but not always. During earnings seasons, 1-month volatility might spike while 6-month volatility drifts higher more gently. During geopolitical crises, the opposite can happen: long-dated options reprice as uncertainty spreads.

Vega bucketing lets traders quantify exposure to these term-structure shifts. If a portfolio has +2000 1M vega and −1000 6M vega, and the 1M volatility falls 2 points while 6M rises 1 point, the net profit or loss depends on scaling and the specific portfolio weights, but the P&L is no longer a mystery.

## Curve hedging and decisions

Once vega is bucketed, hedging the curve becomes tractable. A trader long near-term volatility can hedge by selling shorter-term options or buying longer-term options (selling vega on a different part of the curve). This trades [vega](/vega/) exposure across tenors.

Many professional traders and market makers use vega bucketing as a decision framework: "Our 3M bucket is overweight. If we win on 3M volatility, great—but we're concentration-heavy there. Let's rebalance and push some of that exposure to 6M or 1M to diversify."

## Interaction with other Greeks

Vega bucketing exists alongside [delta-hedging](/delta-hedging/), [gamma](/gamma/) tracking, and [theta](/theta/) monitoring. A position might have zero delta (because it's [delta-hedged](/delta-hedging/)), positive [gamma](/gamma/) (so it profits from moves), and a vega bucketing profile that shows short near-term and long far-term volatility. These are independent lenses on the same book—each reveals different risk.

[Greeks aggregation](/greek-aggregation/) often includes a vega-bucketing report. A trader reviews total delta, total [gamma](/gamma/), total [vega](/vega/), total [theta](/theta/), and then digs into vega by bucket (and sometimes [gamma](/gamma/) by bucket too) to make sure no single tenor or curve segment is a hidden time bomb.

## Practical risks vega bucketing uncovers

1. **Concentrated curve bets**: A trader might accumulate vega on one tenor without realizing it, then be blindsided by a volatility move that only affects that part of the curve.

2. **Roll risk**: As options approach expiry, a trader usually rolls (sells the near-term, buys a longer-term contract). If done carelessly, this can flip vega from long to short or create unexpected curve exposure.

3. **Volatility surface changes**: The curve doesn't just shift in parallel; sometimes it twists or bends. A vega-bucketed view reveals these non-parallel moves in a way a single total-vega number never can.

4. **Event risk**: Earnings, central bank decisions, or other time-stamped events often roil volatility at specific tenors. Bucketing surfaces which parts of the curve are most at risk.

## Limits of bucketing

Vega bucketing is a simplification. It treats options expiring in a 3-month window as equivalent, when a 2.5-month option and a 3.5-month option might behave very differently. Some traders use finer buckets (weekly) or nonlinear interpolation methods to address this.

Bucketing also assumes that volatility moves independently across tenors, which is unrealistic. In crises, correlations spike and the entire curve can repruce in seconds. Bucketing helps you see where you're exposed, but it doesn't make the exposure disappear.

## See also

<div class="wiki-seealso">

### Closely related

- [Vega](/vega/) — the greek measuring sensitivity to implied volatility
- [Implied Volatility](/implied-volatility/) — the volatility priced into options; what vega bets on
- [Yield Curve](/yield-curve/) — the analogous term-structure for interest rates
- [Greek Aggregation](/greek-aggregation/) — the portfolio-level summary that includes vega bucketing
- [Credit Spread](/credit-spread/) — another term-structure hedge commonly used alongside vega bucketing

### Wider context

- Greeks — the sensitivities that drive options and derivatives trading
- [Option](/option/) — the contract whose [vega](/vega/) is being bucketed
- [Black-Scholes Model](/black-scholes-model/) — the framework for calculating [vega](/vega/)
- [Volatility Smile](/volatility-smile/) — non-uniform pricing across strikes that complicates bucketing

</div>

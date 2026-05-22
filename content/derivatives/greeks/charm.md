---
title: "Charm"
description: "The rate of change of gamma with respect to time, measuring how an option's gamma decays as expiration approaches."
keywords:
  - charm greek
  - gamma decay
  - time decay
  - option greeks
---

*Charm is a second-order derivative of an option's price — specifically, the rate at which [gamma](/gamma-option-greeks/) changes as time passes. Because gamma itself changes as an option moves closer to expiration, charm quantifies this decay. In options parlance, charm is sometimes called "gamma decay" or "gamma theta," and it is most important for traders managing large [gamma](/gamma/) positions near expiration.*

<div class="wiki-hatnote">Charm is less commonly cited than the first-order Greeks ([delta](/delta-option-greeks/), [gamma](/gamma-option-greeks/), [theta](/theta-option-greeks/), [vega](/vega-option-greeks/), [rho](/rho-option-greeks/)). It appears in some models of option price dynamics.</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Definition** | d(Gamma) / d(Time); also d(Theta) / d(Delta) |
| **Sign convention** | Positive for out-of-the-money (OTM) options, negative for in-the-money (ITM) |
| **Time decay relation** | Charm accelerates gamma decay near expiration |
| **Practical relevance** | High for short-gamma positions held through expiration |
| **Calculation** | Derived from option pricing models (Black-Scholes, binomial) |
| **Comparable to** | Gamma's counterpart in time dimension |

</aside>

## Charm as the time derivative of gamma

To understand charm, start with [gamma](/gamma-option-greeks/). Gamma measures how much [delta](/delta-option-greeks/) changes when the underlying asset's price moves by one unit. As expiration approaches, gamma increases for at-the-money (ATM) options — the option becomes more sensitive to price moves. Charm quantifies how rapidly this gamma is increasing (or decreasing, depending on moneyness) as time elapses.

For an out-of-the-money (OTM) option near expiration, charm is typically positive: as time passes, gamma is rising. For an in-the-money (ITM) option, charm is typically negative: gamma is falling. This asymmetry reflects the fact that ITM options become more certain to finish ITM as expiration nears, so their delta approaches 1 (or -1 for puts), and gamma correspondingly shrinks.

## The relationship between charm, gamma, and theta

Charm is connected to both [gamma](/gamma-option-greeks/) and [theta](/theta-option-greeks/) in a non-obvious way. Theta measures how much option value decays per unit of time; gamma measures delta sensitivity to price. Charm bridges them: it shows how gamma's sensitivity to time interacts with delta's sensitivity to price.

In fact, charm is sometimes approximated as d(Theta) / d(Delta) — the rate at which theta changes per unit of delta movement. A trader holding a long gamma position (which profits from price volatility) also faces [theta decay](/theta-option-greeks/) (which costs money each day). Charm helps explain why these two P&L sources are coupled: as the underlying moves, not only does delta shift (gamma profit), but also the amount of daily theta decay may shift (charm effect).

## Practical significance for gamma traders

For options traders managing [gamma](/gamma-option-greeks/) hedges, charm matters primarily near expiration. A trader short gamma (selling volatility) faces a dilemma: if the underlying rallies sharply, delta increases and the position must be rehedged by buying stock. But as expiration approaches, the amount of gamma in the trade is increasing (for OTM strikes). Charm quantifies how aggressively gamma is accelerating.

In the final days or hours before expiration, charm can be large. An OTM put option might have low gamma early, but as expiration approaches and the strike remains OTM, gamma accelerates sharply. A trader short this put must rehedge more frequently, increasing transaction costs and slippage. Charm helps model this cost.

## Charm asymmetry and volatility structure

Charm is asymmetric between puts and calls at the same strike, and between ITM and OTM options. This asymmetry reflects option convexity. Deep ITM options (calls with spot far above strike) have gamma approaching zero; charm is near zero too. ATM options have the highest gamma and (in absolute value) the highest charm. OTM options have moderate gamma and positive charm (as time passes, they gain gamma).

Understanding charm asymmetry is useful for structuring volatility trades. A [straddle](/straddle/) (long call and long put at the same strike) has gamma that is high and symmetric. But charm is asymmetric: if the underlying is slightly below the strike, the ITM put has negative charm while the OTM call has positive charm. This asymmetry means the straddle's gamma profile will shift as time elapses — not just shrink uniformly.

## Charm in multi-leg strategies

In complex [options positions](/option-chain/), charm becomes non-trivial. A trader managing a large [calendar spread](/calendar-spread/) (long-dated options against short-dated options) or a [ratio spread](/ratio-spread/) must track how gamma profiles change over time. Charm is one of the tools to model this evolution.

For example, a [reverse calendar spread](/calendar-spread/) (short long-dated, long short-dated) benefits if near-term gamma decays faster than far-term gamma. Charm helps quantify whether this actually happens, or whether the benefit will materialize as expected.

## Computational aspects and limitations

Charm is rarely quoted by market makers or options platforms alongside the standard Greeks. Calculating charm requires second derivatives of the option pricing model with respect to time and price. In Black-Scholes models, charm has a closed form, but it is computationally fiddly. Many practitioners use numerical approximations or don't track it explicitly.

Modern options analytics platforms can compute charm if requested, but it is less liquid in the data ecosystem than delta, gamma, or vega. Traders who care about charm typically compute it in-house using their preferred option model.

## Charm and exotic options

Charm becomes more relevant for [exotic options](/option/) that have complex P&L dynamics near expiration. A [barrier option](/barrier-option/) that knocks in as expiration approaches has rapidly shifting gamma; charm is essential for understanding the rehedging cost. A [lookback option](/lookback-option/) or [Asian option](/asian-option/) may also have charm effects that matter for hedging.

For vanilla [calls](/call-option/) and [puts](/put-option/), charm is a second-order consideration. For structured products and exotic derivatives, it is increasingly important.

<div class="wiki-seealso">

### Closely related

- [Gamma (Option Greeks)](/gamma-option-greeks/) — delta's sensitivity to price moves
- [Theta (Option Greeks)](/theta-option-greeks/) — option time decay
- [Delta (Option Greeks)](/delta-option-greeks/) — option price sensitivity to underlying price

### Wider context

- [Options Greeks](/options-greeks/) — complete family of option risk measures
- [Black-Scholes Model](/black-scholes-model/) — framework for option pricing and Greeks
- [Gamma Hedging](/dynamic-hedging-algorithm/) — managing gamma risk via continuous rebalancing

</div>

---
title: "Epsilon"
description: "An option Greek measuring the sensitivity of an option's value to changes in dividend yield of the underlying asset."
keywords:
  - epsilon
  - option greeks
  - dividend sensitivity
  - derivatives sensitivity
---

*Epsilon is one of the lesser-known [option Greeks](/wiki/options-greeks/), measuring how much an option's price changes when the dividend yield of the underlying asset changes. Also called **psi** in some contexts, epsilon is most relevant for dividend-paying stocks and in dividend futures pricing.*

<aside class="wiki-infobox">

| Attribute | Details |
|-----------|---------|
| **Symbol** | ψ (psi) or sometimes ε (epsilon) |
| **Measure** | Change in option value per 1% change in dividend yield |
| **Formula** | ∂C/∂q (European call); depends on time to expiration and strike |
| **Direction** | Negative for calls; positive for puts (opposite relationship to underlying dividend yield) |
| **Practical relevance** | High when dividend yield is high or expiration is far |
| **Time decay** | Epsilon effect increases as expiration approaches for in-the-money calls |
| **Related Greeks** | Delta, theta, rho; all measure sensitivity to different market variables |

</aside>

## Why dividend yield matters for options

The value of an [option](/wiki/option/) depends on several factors: the underlying stock price, volatility, time to expiration, interest rates, and *dividend yield*.

When a company pays a dividend, the stock price drops by approximately the dividend amount on the ex-dividend date. Options pricing models (like Black-Scholes) account for this. A higher dividend yield reduces the value of [call options](/wiki/call-option/) (fewer dollars of appreciation) and increases the value of [put options](/wiki/put-option/) (more downside potential).

Epsilon quantifies this sensitivity.

## The mechanics: calls vs. puts

For a European [call option](/wiki/call-option/):
- Higher dividend yield → lower call value.
- Epsilon is negative.
- If dividend yield rises from 2% to 3% and epsilon is −0.50, the call value drops by roughly $0.50.

For a European [put option](/wiki/put-option/):
- Higher dividend yield → higher put value.
- Epsilon is positive.
- If dividend yield rises and epsilon is +0.30, the put value rises by roughly $0.30.

**Intuition:** When a stock yields 5% annually, the expected appreciation of the stock is lower (part of returns come via dividends, not price appreciation). Call buyers want price appreciation; they are disadvantaged by high yields. Put holders benefit because the stock's upside is dampened.

## When epsilon matters most

**High-dividend-yield stocks:** Utilities, REITs, and dividend aristocrats often yield 3–5%. Option prices are sensitive to dividend changes.

**Before dividend announcements:** If a company is expected to raise its dividend, option prices adjust. Call values drop; put values rise.

**Long expirations:** For far-dated options (6–12 months), multiple dividend payments are expected. Epsilon impact accumulates.

**Deep in-the-money calls:** An ITM call will likely be exercised. If dividends rise, the stock may still be above strike, but the call holder forgoes future dividends. The option is less attractive.

**Dividend futures:** Financial contracts on dividend indices (e.g., the [S&P 500](/wiki/sp-500-index/) dividend index) explicitly price dividend yield. Options on dividend futures have large epsilon components.

## Contrast with other Greeks

| Greek | Sensitivity |
|-------|-------------|
| **[Delta](/wiki/delta-option-greeks/)** | Price of underlying stock |
| **[Gamma](/wiki/gamma-option-greeks/)** | Rate of change of delta (curvature) |
| **[Theta](/wiki/theta-option-greeks/)** | Time to expiration (time decay) |
| **[Rho](/wiki/rho-option-greeks/)** | Interest rates |
| **Epsilon** | Dividend yield |
| **[Vega](/wiki/vega-option-greeks/)** | [Volatility](/wiki/implied-volatility/) |

All six Greeks work together. An option's price is sensitive to all six variables simultaneously.

## Calculating epsilon

The closed-form formula for epsilon depends on the option pricing model. Under Black-Scholes:

For a European call:
ε = −S × e^(−q×T) × N'(d1)

Where:
- S = stock price
- q = continuous dividend yield
- T = time to expiration
- N'(d1) = the standard normal probability density at d1

The formula is complex, but key insights:
- Epsilon decays as time passes (T decreases).
- Epsilon is largest for at-the-money options (maximum convexity).
- Higher dividend yields increase the magnitude of epsilon.

**Numerical example:**
- Stock: $100, dividend yield 3%, 6 months to expiration.
- Call option with strike $100.
- Epsilon ≈ −0.35 (per percentage point change in yield).
- If yield changes to 4%, the call value drops ~$0.35.

## Practical uses

**Traders hedge dividend risk:** A trader short a call with epsilon of −0.40 faces losses if the dividend yield drops (call value rises). To hedge, the trader might buy an OTC dividend swap or position in related derivatives.

**Arbitrageurs exploit mispricing:** If the market prices in a 2% dividend yield but the actual announced yield is 2.5%, call options are overpriced. Arbitrageurs sell calls and buy stock.

**Portfolio managers manage tax timing:** High-dividend-yielding positions have tax implications. Options can be used to defer or accelerate dividend capture, adjusting for epsilon effects.

## Dividend-stripping and epsilon dynamics

In some markets, companies declare special dividends or engage in [dividend stripping](/wiki/dividend-stripping/) (deliberately raising or timing dividends for tax advantage). These events create epsilon surprises.

A special dividend announcement can cause calls to drop sharply in value (epsilon realizes). Traders who failed to account for announced or rumored dividends face unexpected losses.

## Limitations and real-world complications

**Discrete vs. continuous dividends:** Black-Scholes assumes continuous dividend yield. Real dividends arrive on discrete ex-dates. American options, which can be exercised early, may behave differently from the model around ex-dates.

**Uncertain dividend growth:** Epsilon assumes the dividend yield is known. If future dividends are uncertain, the effective yield is ambiguous, and epsilon becomes noisy.

**Interest rate correlation:** Dividend yields and interest rates can be correlated (both rise in strong economies). The interaction complicates hedging.

**Market microstructure:** Real option prices incorporate bid-ask spreads and trading costs that dwarf epsilon effects on small moves.

## Epsilon in dividend futures and indices

The [CBOE](/wiki/cboe-options-exchange/) and other exchanges offer options on dividend indices (e.g., the S&P 500 Dividend Index, which tracks cumulative dividends). These options have large epsilon components because the underlying is inherently dividend-focused.

Dividend futures contracts also exist, allowing traders to speculate on future dividend payments. Options on dividend futures have purely dividend-driven values.

## Relation to ex-dividend date

The ex-dividend date (when the stock price is adjusted down by the dividend amount) creates discrete jumps in option value. Epsilon models smooth, continuous changes in yield. Around ex-dates, discrete effects dominate epsilon.

A [call option](/wiki/call-option/) holder does not receive the dividend (the stock price drops, reducing the call's value). This is captured by the negative epsilon. But the discrete drop on ex-date is the mechanism.

## Summary and takeaway

Epsilon is a second-order consideration for most retail traders. Most option traders focus on delta (direction), [gamma](/wiki/gamma-option-greeks/) (convexity), [theta](/wiki/theta-option-greeks/) (time decay), and [vega](/wiki/vega-option-greeks/) (volatility).

But for anyone trading dividend-rich stocks, writing covered calls, or engaging in dividend arbitrage, epsilon is essential. A call seller holding a high-yield stock faces large negative epsilon; if the company announces a dividend increase, the short call loses value sharply.

<div class="wiki-seealso">

### Closely related
- [Options Greeks](/wiki/options-greeks/) — Category of sensitivities
- [Delta](/wiki/delta-option-greeks/) — Price sensitivity
- [Rho](/wiki/rho-option-greeks/) — Interest-rate sensitivity
- [Vega](/wiki/vega-option-greeks/) — Volatility sensitivity
- [Theta](/wiki/theta-option-greeks/) — Time-decay sensitivity

### Wider context
- [Call Option](/wiki/call-option/) — Primary use case
- [Put Option](/wiki/put-option/) — Inverse relationship
- [Dividend Yield](/wiki/dividend-yield/) — Core variable epsilon measures
- [Black-Scholes Model](/wiki/black-scholes-model/) — Pricing foundation
- [Implied Volatility](/wiki/implied-volatility/) — Related option input

</div>

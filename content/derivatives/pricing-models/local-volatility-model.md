---
title: "Local Volatility Model"
description: "Dupire's framework that calibrates a deterministic volatility surface to fit all observed option prices exactly."
keywords:
  - volatility surface
  - Dupire framework
  - option pricing
  - deterministic volatility
  - calibration
image: "/svg/derivatives.svg"
---

*The **local volatility model** is an option pricing framework where volatility is a deterministic function of both the underlying asset price and time. Unlike Black-Scholes, which assumes a single constant volatility, local volatility allows the model to be "calibrated" so it reproduces every observed option price in the market—a feature that makes it indispensable for pricing exotic derivatives and managing volatility risk in real trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Local Volatility Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">A volatility surface that moves with price and time, fit precisely to market data.</div>

|   |   |
|---|---|
| **What it is** | A model where volatility σ(S, t) depends on stock price and time, not constant |
| **Key insight** | Can exactly match a [Black-Scholes-model](/black-scholes-model/) price at any (S, t) by construction |
| **Calibration** | Uses [implied volatility](/implied-volatility/) data from traded options to back out σ(S, t) across the surface |
| **Main use** | Pricing exotic derivatives ([call-option](/call-option/), [put-option](/put-option/), barriers, etc.) and delta-hedging |
| **Also called** | Dupire model (after Bruno Dupire), deterministic volatility, state-dependent volatility |
| **Limitation** | Does not capture volatility clustering or stochastic changes in volatility smile |

</aside>

## How Dupire's formula inverts option prices into a volatility surface

The local volatility model's practical power comes from **Dupire's formula**, derived in 1994. Given a continuum of observed call option prices C(K, T) across all strikes K and maturities T, Dupire's formula lets you solve directly for σ(S, t):

The formula is constructive: if you have a fine grid of [market-maker](/market-maker-trading/) quotes for calls at various strikes and expirations, you can numerically interpolate them, apply Dupire's equation, and recover a smooth volatility surface σ(S, t). That surface then embeds all of the market's [implied volatility](/implied-volatility/) information—the [volatility smile](/volatility-smile/) and skew—into a single, deterministic object.

This contrasts sharply with the [Black-Scholes-model](/black-scholes-model/), where you pick one volatility σ and apply it everywhere. Local volatility says: the market is telling you a different σ for a stock at $100 than for a stock at $80, and a different σ three months from now than six months from now.

## The model assumes volatility is deterministic, not random

A critical assumption underlying local volatility is that σ(S, t) is **deterministic**: it is a smooth, known function once calibrated. This differs fundamentally from stochastic volatility models, which treat volatility itself as a random process evolving over time.

The deterministic assumption has two consequences:

**Advantage:** Once you've fit the surface to today's market prices, you have a complete, parsimonious description of the market's option prices. You can price any exotic derivative—barriers, lookbacks, [leverage](/leverage-ratio-forex/), you name it—by Monte Carlo or PDE methods, without estimating extra stochastic parameters. It integrates cleanly with [delta](/delta/) hedging: your hedge ratio at any price level is pinned down by the surface.

**Disadvantage:** Local volatility cannot capture volatility clustering or mean reversion. If you observe that realized volatility tends to spike in clusters (as real markets do), a deterministic surface fit to today's prices will badly misprice the path-dependent payoffs of exotic derivatives whose value depends on the sequence of volatility realizations, not just the distribution. This is why traders often prefer stochastic volatility models for longer-dated exotics.

## Calibration: fitting the surface to market quotes

In practice, calibrating a local volatility model involves:

1. **Gather market data.** Collect bid–ask quotes for liquid calls and puts across strikes and expirations.

2. **Interpolate call prices.** Use spline fitting or similar techniques to construct a smooth price surface C(K, T) from the discrete market quotes.

3. **Differentiate and apply Dupire's formula.** Compute the necessary partial derivatives (price with respect to strike, price with respect to time) and apply Dupiere's formula to recover σ(K, T).

4. **Transform to price space.** If desired, express the surface in terms of stock price S rather than strike K, giving σ(S, t).

5. **Validate and smooth.** Check that the recovered volatility surface is smooth and economically sensible (e.g., no negative volatilities). Use regularization or additional constraints if needed.

The result is a 2D surface: along the horizontal axes you have the stock price and time; on the vertical axis, volatility. Practitioners visualize this as a mesh or contour plot, with the familiar shape often showing higher volatility for out-of-the-money puts (the [volatility smile](/volatility-smile/)) flattening as time increases.

## Why local volatility alone cannot capture all of the market's dynamics

Despite its calibration perfection on today's prices, local volatility has a well-known failing: it is **path-independent**. Once the surface is fit, the model gives a single, deterministic vol for a stock at price S at time t, regardless of the path by which the stock reached S.

In reality, option prices (especially for exotic derivatives) often depend on the volatility of the path. If a stock jumps to $100 via a smooth climb, traders might price a barrier option differently than if it spiked to $100 instantaneously. Local volatility cannot distinguish these scenarios.

This is why traders often layer local volatility with other tools:

- **Stochastic volatility extensions.** Models like SABR or Heston add a second random process for volatility, allowing correlation between returns and volatility changes (the "leverage effect").
- **Jump-diffusion models.** If markets show sudden discontinuous moves, [jump-diffusion-model](/jump-diffusion-model/) frameworks capture fat tails and gap risk.
- **Regime-switching models.** For long-dated exotics, some traders fit separate local volatility surfaces for different market regimes.

## Local volatility in daily hedging and exotics pricing

For vanilla options on stocks, local volatility is largely a theoretical curiosity—traders just use [Black-Scholes-model](/black-scholes-model/) with a single [implied volatility](/implied-volatility/) and plug in [market-maker](/market-maker-trading/) deltas. But for exotic derivatives, it is essential.

Consider a barrier option—a call that knocks out if the stock touches a lower barrier level. The payoff depends critically on the distribution of paths that avoid the barrier. Local volatility automatically supplies the vol at each price and time, so you can simulate thousands of paths using the calibrated surface and compute the expected payoff.

Similarly, for a variance swap or a cliquet (a strip of consecutive [call-option](/call-option/) resets), local volatility lets you price the portfolio consistently with the vanilla market, since it is calibrated to fit all vanilla prices exactly.

In practice, traders maintain local volatility surfaces for major stock indices and currencies, updating them intraday as market prices shift. The surface is then plugged into production systems for risk management and exotic pricing.

## The volatility surface and its shape tell a story

The fitted local volatility surface encodes several market narratives:

- **The smile.** Higher volatility for out-of-the-money [put-option](/put-option/) reflects investors' fear of crashes; higher volatility for far out-of-the-money calls reflects tail-risk premium.
- **The term structure.** Near-term volatility often exceeds far-term volatility (a "downward-sloping" term structure) if the market expects imminent news; the reverse signals complacency.
- **Asymmetry.** For equities, the smile is usually skewed—calls are less expensive (lower vol) than puts at the same distance from the money—because of [loss-aversion](/loss-aversion/) and leverage constraints.

Traders read these shapes to infer where the market sees risk. A flattening smile might signal that tail risk is pricing out; a steepening term structure warns of expected volatility spikes.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes-model](/black-scholes-model/) — The foundational constant-volatility option pricing framework that local volatility extends
- [Implied volatility](/implied-volatility/) — The volatility input that makes a Black-Scholes price match a market quote; local volatility inverts these to build a surface
- [Volatility smile](/volatility-smile/) — The empirical observation that implied vol varies with strike; local vol captures this deterministically
- [Black-76-model](/black-76-model/) — Another extension of Black-Scholes for futures and interest rates that can also employ local volatility methods
- [Jump-diffusion-model](/jump-diffusion-model/) — A competing framework that adds discontinuous price jumps rather than a smoothly varying volatility
- [Bachelier-model](/bachelier-model/) — An alternative pricing framework using normal (rather than lognormal) distributions, also extensible to local volatility

### Wider context

- [Option](/option/) — The fundamental derivative that local volatility models price
- [Delta](/delta/) — The hedge ratio for options; local volatility supplies delta consistently across all prices
- [Volatility-smile](/volatility-smile/) — The empirical pattern that motivated local volatility models
- Derivative — The broader class of instruments priced using local volatility
- Risk-management — How traders use local vol surfaces to hedge exotic portfolios

</div>

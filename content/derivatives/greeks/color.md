---
title: "Color"
seo_title: "Color (Options Greek): Gamma of Gamma Explained"
description: "Color is a third-order option Greek measuring how gamma changes as the underlying price moves. What it means for hedging and when traders track it."
keywords:
  - color greek
  - gamma sensitivity
  - option greeks
  - third-order greek
  - option risk
---

*The **color** (also called "gamma of gamma") is a third-order option Greek that measures how quickly an option's [gamma](/wiki/gamma-option-greeks/) changes as the underlying asset price moves. Where [delta](/wiki/delta-option-greeks/) measures price sensitivity and gamma measures how delta changes, color measures how gamma's rate of change varies — a meta-level view of the option's curvature dynamic.*

<div class="wiki-hatnote">
For the foundational Greeks, see <a href="/wiki/options-greeks/">/wiki/options-greeks/</a>. For gamma itself, see <a href="/wiki/gamma-option-greeks/">/wiki/gamma-option-greeks/</a>. For related higher-order Greeks, see <a href="/wiki/charm/">/wiki/charm/</a> (gamma sensitivity to time decay).
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Definition** | ∂Gamma / ∂S (or Γ′ in partial derivatives notation) |
| **Order** | Third-order Greek (third derivative of option price with respect to underlying) |
| **Sign** | Typically positive for ATM options, negative for deep ITM/OTM |
| **Maximum** | Largest magnitude near-at-the-money, decaying as moneyness increases |
| **Units** | Per dollar of underlying price move (dimension: 1 / underlying²) |
| **Traders Use** | Exotic option hedging, volatility trading, portfolio rebalancing schedules |
| **Opposite Sign to Charm** | Color (price-based) and charm (time-based) have opposite effects; sum to zero under no-drift |
| **Market Relevance** | Most important in illiquid markets where rehedging is infrequent |

</aside>

## Understanding color through the Greek hierarchy

The [option Greeks](/wiki/options-greeks/) form a hierarchy of sensitivities:

- **Delta** (first-order): sensitivity of option price to underlying price. How much does the option's value change if the stock moves $1?
- **Gamma** (second-order): sensitivity of delta to underlying price. How much does delta change if the stock moves $1?
- **Color** (third-order): sensitivity of gamma to underlying price. How much does gamma change if the stock moves $1?

In mathematical terms, if C is the option price and S is the underlying price:
- Delta = ∂C / ∂S
- Gamma = ∂Delta / ∂S = ∂²C / ∂S²
- Color = ∂Gamma / ∂S = ∂³C / ∂S³

Color quantifies the convexity of gamma itself. For an at-the-money (ATM) call option, gamma is at its maximum, but color is zero (gamma is at an extremum, not changing). Just below the strike, gamma is high and increasing, so color is positive. Deep out-of-the-money (OTM), gamma is very low and decreasing, so color is negative.

## The intuition: gamma's gamma

Imagine an ATM call option on Apple stock. As Apple's price rises slightly from $150 to $151, gamma tells you how much delta increases. If gamma is 0.05, delta might increase by approximately 0.05 (though the exact change depends on gamma's shape).

Color measures how gamma itself changes with the next move. If Apple rises from $151 to $152, does gamma increase at the same rate as it did from $150 to $151? If gamma is still increasing (color is positive), then the delta-acceleration is speeding up. If gamma is starting to decrease (color is negative), delta-acceleration is slowing.

This is relevant for dynamic hedging. A trader who [rehedges](/wiki/rebalancing-discipline/) by adjusting delta daily encounters changing gamma; color tells them whether gamma is becoming more or less influential in their hedging costs.

## Color, charm, and third-order effects

Two related third-order Greeks are **charm** (the rate of gamma decay over time) and **color** (the rate of gamma change over price). Charm measures ∂Gamma / ∂t (gamma sensitivity to time); color measures ∂Gamma / ∂S (gamma sensitivity to price).

Together, they determine how gamma evolves. An ATM option loses gamma as time passes (charm is negative); it also reshapes as the underlying price moves (color), affecting how much gamma is available for rehedging. The gamma of a $150 call increases when the underlying moves toward $150, but decreases when the underlying moves away (color transitions from positive to negative).

## Relevance for exotic and structured options

Color is most important for traders managing **exotic options** with complex gamma structures. A barrier option or a volatility-dependent option has gamma that varies rapidly with price; understanding color helps the trader anticipate hedging costs.

For standard vanilla options (listed calls and puts), color is academically interesting but less practically important, because liquidity allows frequent rehedging and gamma-related costs are directly hedged by [vega](/wiki/vega-option-greeks/) trades (vega captures the volatility sensitivity that drives gamma variation).

For **illiquid underlying assets** or **concentrated positions** where rehedging is infrequent, color becomes more relevant. If a trader must rebalance gamma only weekly or monthly, knowing color helps them predict how their gamma exposure will shift between rehedges, informing decisions about interim volatility trades.

## Calculation and sign conventions

Color is calculated using partial derivatives of the option-pricing model (Black-Scholes, binomial, Monte Carlo):

For a European call option under Black-Scholes:
- Color = ∂³C / ∂S³ = (1 / (σ * S² * sqrt(T))) * φ(d₁) * [2 * σ * S * sqrt(T) * d₂ - 1]

where φ is the standard normal PDF and d₁, d₂ are the Black-Scholes parameters.

The sign of color:
- **Positive** near ATM (gamma is increasing as price moves toward ATM).
- **Negative** deep ITM or OTM (gamma is decreasing as price moves away from ATM).
- **Zero** exactly at ATM (gamma is at a local maximum).

## Practical applications

**Gamma scalping** (profiting from selling volatility and rehedging delta) is affected by color. A trader selling a call and rehedging delta daily expects gamma to decay, generating profits. But color determines how gamma decays as the underlying price moves. If color is positive (gamma increasing), the trader's rehedging costs are accelerating; if negative (gamma decreasing), rehedging costs are slowing.

**Volatility trading** uses color indirectly. Traders who buy straddles or strangles (long gamma positions) benefit from price moves that push the option toward ATM (positive color) and suffer from moves away from ATM (negative color). Understanding color informs decisions about whether the underlying volatility is likely to generate profitable rehedging opportunities.

**Portfolio rebalancing** schedules can be informed by color. A portfolio manager with a fixed rebalancing schedule (monthly, quarterly) can use color to estimate how gamma will drift between rebalance dates, adjusting hedges accordingly.

## Color versus other Greeks in comparative importance

In terms of practical trading, the hierarchy of Greek importance is typically:
1. **Delta** (first-order): dominates risk; must be hedged immediately.
2. **Gamma** (second-order): significant for dynamic strategies and illiquid markets.
3. **Vega** (second-order): critical in volatility-rich environments; traders actively manage volatility exposure.
4. **Theta** (second-order): governs time decay; crucial for evaluating time-sensitive positions.
5. **Color** (third-order): notable for exotics and infrequent rehedging; secondary for vanilla.

Most retail and even institutional traders focus on the first four; color is used primarily by options specialists and quants managing large, complex books.

## Limitations and model dependence

Color, like all Greeks, depends on the assumptions embedded in the option-pricing model. Under Black-Scholes, color has a specific formula. But if the underlying asset's volatility is not constant (violating Black-Scholes' assumptions), true color may differ from the model's prediction.

In real markets, color is less stable than delta or gamma because it depends on the shape of the entire gamma curve, which is affected by second-order effects (volatility smile, term structure, dividend expectations).

<div class="wiki-seealso">

### Closely related
- <a href="/wiki/gamma-option-greeks/">/wiki/gamma-option-greeks/</a> — The second-order Greek that color measures
- <a href="/wiki/charm/">/wiki/charm/</a> — Time decay of gamma; the temporal companion to color
- <a href="/wiki/delta-option-greeks/">/wiki/delta-option-greeks/</a> — The first-order Greek
- <a href="/wiki/vega-option-greeks/">/wiki/vega-option-greeks/</a> — Volatility sensitivity
- <a href="/wiki/options-greeks/">/wiki/options-greeks/</a> — Complete Greek taxonomy

### Wider context
- <a href="/wiki/option-pricing/">/wiki/black-scholes-model/</a> — The model that computes color
- <a href="/wiki/gamma-scalping/">/wiki/gamma-scalping/">/wiki/gamma-scalping/</a> — Strategy most affected by color
- <a href="/wiki/dynamic-hedging-algorithm/">/wiki/dynamic-hedging-algorithm/</a> — Rehedging approach where color matters
- <a href="/wiki/volatility-smile/">/wiki/volatility-smile/</a> — Price-dependent volatility that affects color
- <a href="/wiki/exotic-option/">/wiki/exotic-option/</a> — Complex instruments where color is material

</div>
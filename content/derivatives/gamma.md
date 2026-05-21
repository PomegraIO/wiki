---
title: "Gamma"
description: "Gamma measures the rate at which an option's delta changes as the underlying asset price moves, quantifying the convexity and instability of option hedges."
keywords:
  - gamma
  - option greeks
  - delta change
  - convexity
  - hedging risk
image: "/svg/derivatives.svg"
---

*The **gamma** of an option is the second derivative—the rate of change of [delta](/delta) with respect to the underlying asset's price. Gamma is always positive for long options (you own them) and always negative for short options (you sold them). Gamma is highest for [at-the-money](/at-the-money) options and falls to near-zero for deep [in-the-money](/in-the-money) or [out-of-the-money](/out-of-the-money) options. Gamma quantifies the instability and rehedging cost of [delta-hedged](/call-option) positions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma — key facts</div>

<img src="/svg/derivatives.svg" alt="Convex delta curve showing acceleration" />

<div class="wiki-infobox-caption">Gamma measures how delta itself changes.</div>

|   |   |
|---|---|
| **Measures** | Rate of change of delta |
| **Sign** | Always positive for long, negative for short |
| **Highest at** | At-the-money options |
| **Lowest at** | Deep in/out-of-the-money |
| **Time to expiration** | Higher gamma closer to expiration (at ATM) |
| **Volatility impact** | Lower volatility = higher gamma (at ATM) |
| **Interpretation** | Delta increases/decreases per $1 stock move |
| **Hedging cost** | Gamma cost = loss from rehedging |
| **Long gamma** | Profit from large moves (convexity benefit) |
| **Short gamma** | Lose from large moves (convexity cost) |

</aside>

## Gamma as delta acceleration

If a [call option](/call-option) has a [delta](/delta) of 0.5 and a gamma of 0.05, then a $1 move in the stock increases the delta to 0.55 (for upward moves) or decreases it to 0.45 (for downward moves).

This acceleration of [delta](/delta) is gamma. It quantifies how quickly your directional sensitivity changes as the stock moves. High gamma means [delta](/delta) is unstable and requires frequent rehedging. Low gamma means [delta](/delta) is stable.

## Gamma is always positive for owned options

Whether you own a [call](/call-option) or [put](/put-option), gamma is positive. This is because option value is convex—the option benefits from large moves in either direction. A $100 strike call is worth more if the stock rises to $110 OR falls to $90 (no benefit from the fall, but lower time value) relative to just staying at $100.

For short options (sold/written), gamma is negative. You lose from large moves in either direction; you want the stock to stay near the strike.

## Gamma and the Greeks' relationship

Gamma is related to [theta](/theta) through a key equation: for a delta-neutral portfolio, [theta](/theta) + ½ × [volatility](/historical-volatility)² × [gamma](/gamma) ≈ 0.

This says: if you are [theta](/theta)-positive (profiting from time decay), you are [gamma](/gamma)-negative (losing from large moves). If you are [gamma](/gamma)-positive (long volatility), you are [theta](/theta)-negative (losing to time decay). This trade-off is fundamental in options markets.

## Gamma and rehedging costs

When you delta-hedge by buying/selling shares to neutralize [delta](/delta), you are betting the stock will not move much. But when the stock does move, [delta](/delta) changes (due to gamma), and you must rehedge. This rehedging locks in losses.

Suppose you short a [call](/call-option) and delta-hedge by buying shares. If the stock rises:
1. The call delta increases (you are now long-gamma-exposed).
2. You must sell shares to restore delta neutrality.
3. You sell those shares at a higher price than you bought them.
4. But now the stock falls back to the original level.
5. The call delta decreases (back toward the original).
6. You must buy shares again, now at the original (higher) price.

You have locked in a loss. The size of this loss is roughly: realized [volatility](/historical-volatility)² × gamma × time. This is the "gamma cost" of hedging.

## Gamma concentration near the strike

[At-the-money](/at-the-money) options have maximum gamma. An [at-the-money](/at-the-money) [call](/call-option) with 90 days to expiration might have a gamma of 0.02 (meaning delta increases by 0.02 per $1 move). A deep [out-of-the-money](/out-of-the-money) call on the same stock might have a gamma of 0.001.

This concentration of gamma at the strike is why near-the-money options are riskier to hedge and why traders focus gamma management effort on contracts near the strike.

## Gamma and time to expiration

For [at-the-money](/at-the-money) options, gamma increases as [expiration date](/expiration-date) nears. A call with 1 day to expiration has much higher gamma than the same call with 60 days to expiration (assuming same [volatility](/historical-volatility)). The delta is forced to swing from 0.5 (if out-of-the-money) to 1.0 (if in-the-money) over the final day, creating extreme gamma.

This is why near-expiration options are volatile and difficult to hedge.

## Gamma scalping

**Gamma scalping** is a strategy where you hold a long gamma position (own options) and delta-hedge it. As the stock moves, [delta](/delta) changes, you rehedge, and you pocket the rehedging profit. This requires significant transaction costs and is typically profitable only when realized [volatility](/historical-volatility) exceeds [implied volatility](/implied-volatility).

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the metric gamma measures change in
- [Theta](/theta/) — gamma-theta trade-off
- [Options Greeks](/options-greeks/) — gamma is one of the five
- [Call option](/call-option/) — positive gamma when long
- [Put option](/put-option/) — positive gamma when long

### Hedging concepts

- [Delta hedging](/call-option) — gamma creates rehedging costs
- [Rebalancing](/alpha) — required due to gamma
- [Convexity](/call-option) — gamma is the option's convexity
- [Volatility](/historical-volatility) — gamma profits from realized volatility

### Valuation

- [Black-Scholes model](/black-scholes-model/) — computes gamma
- [Implied volatility](/implied-volatility/) — affects gamma calculation
- [At-the-money](/at-the-money/) — maximum gamma
- [Out-of-the-money](/out-of-the-money/) — low gamma

### Deeper context

- [Option](/option/) — the family of derivatives
- [Risk management](/hedge-fund/) — gamma is central to hedging
- [Trading](/stock-market) — gamma scalping exploits gamma

</div>

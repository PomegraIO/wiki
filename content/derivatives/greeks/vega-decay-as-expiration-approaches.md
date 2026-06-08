---
title: "Vega Decay as Expiration Approaches"
description: "Why option vega shrinks as time to expiration decreases, making implied volatility exposure nearly zero at maturity."
keywords:
  - vega decay expiration
  - vega option greek
  - implied volatility sensitivity
  - option time decay
  - vega near expiration
  - derivatives trading greeks
  - option vega calculation
image: /svg/derivatives.svg
---

*[Vega](/vega/) measures how much an [option](/option/) price changes when [implied volatility](/implied-volatility/) shifts by 1%. An option with vega of 0.05 gains $5 in value if implied volatility jumps from 25% to 26%. But vega is not constant. As an **option approaches expiration**, its vega *collapses* toward zero—sometimes in days. A call option with 180 days to expiration might have vega of 0.15; the same call at 5 days to expiration might have vega of 0.01. This decay happens because implied volatility becomes irrelevant when there is almost no time left for price movement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vega Decay — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">As expiration nears, volatility sensitivity collapses to zero.</div>

|   |   |
|---|---|
| **Vega peak** | At-the-money, 20–60 days to expiration |
| **90+ days** | Vega is substantial; volatility moves matter |
| **30 days** | Vega declines noticeably; decay accelerates |
| **5 days** | Vega is minimal; volatility has little effect |
| **At expiration** | Vega = 0; only intrinsic value remains |
| **Decay pattern** | Non-linear; accelerates into expiration |
| **Portfolio effect** | Long volatility positions bleed value if volatility is flat |

</aside>

## The Math Behind Vega Decay

Vega decay is an inevitable consequence of the [Black-Scholes model](/black-scholes-model/) and market pricing logic. The value of an [option](/option/) consists of two components:

**Intrinsic value** — the amount by which the option is [in the money](/in-the-money/). A call with strike $100 on a stock trading at $105 has intrinsic value of $5. This portion is deterministic and unaffected by volatility.

**Time value** — the premium above intrinsic value that traders pay for optionality—the right, not the obligation, to buy or sell. Time value depends on two things: time remaining and implied volatility. More time = more premium. Higher volatility = more premium.

Now, implied volatility only matters when there is time for price movement. If an option expires in 180 days, there are 180 days for volatility to occur—the stock could swing 10%, 20%, or more. A volatility estimate matters. But if the option expires in 3 days, there is almost no time for volatility to manifest. The stock is unlikely to swing 10% in 3 days. Volatility becomes theoretical.

As time decreases, the "leverage" of volatility diminishes. A 1% change in implied volatility has a large effect on an option with 6 months to go but a negligible effect on an option with 3 days to go. This is why vega shrinks.

## Numerical Example: Vega Over Time

Consider an at-the-money call option on a $100 stock with various times to expiration. Assume constant [interest rates](/interest-rate/) and dividends.

| Days to Expiration | Call Price | Vega | Change in Call if IV +1% |
|---|---|---|---|
| 180 | $8.50 | 0.095 | $8.50 → $8.60 (+$0.10) |
| 90 | $6.20 | 0.068 | $6.20 → $6.27 (+$0.07) |
| 30 | $3.80 | 0.032 | $3.80 → $3.83 (+$0.03) |
| 10 | $1.95 | 0.010 | $1.95 → $1.96 (+$0.01) |
| 5 | $1.25 | 0.004 | $1.25 → $1.25 (no material change) |
| 1 | $0.50 | 0.000 | $0.50 → $0.50 (vega ≈ 0) |

The decay accelerates near expiration. The drop from 180 to 90 days cuts vega by 28%; the drop from 30 to 10 days cuts vega by 69%; the drop from 10 to 5 days cuts vega by 60%. In the final days, vega is essentially zero.

Why? Because the option's remaining time value is minimal. At 5 days to expiration, an at-the-money call is worth barely more than the [time decay](/time-decay-theta/) warrant. A 1% change in implied volatility affects a pool of remaining premium that is already tiny.

## The Non-Linear Decay Pattern

Vega decay is **not linear**. It accelerates, especially in the last 2–4 weeks. This is a critical insight for [derivatives](/derivatives-hedging/) traders.

- **Weeks 26–20:** Vega declines slowly; a long vega position loses value gradually.
- **Weeks 10–5:** Vega decay steepens; daily losses accelerate.
- **Days 7–0:** Vega approaches zero sharply; the position is almost entirely time decay.

A trader who buys a [call option](/call-option/) to profit from a volatility spike faces accelerating headwinds if volatility does not spike soon. If the stock remains flat and implied volatility is stable, [theta (time decay)](/time-decay-theta/) erodes the call's value *every single day*, but theta's effect grows as vega shrinks.

## Vega and the Greeks Over Time

Vega decay is intertwined with other Greeks. As vega falls, [theta](/time-decay-theta/) (time decay) accelerates. A long option position that bleeds theta every day will lose more money per day near expiration than weeks earlier, even if the stock and volatility are unchanged.

[Delta](/delta/) (directional sensitivity) also changes near expiration. An at-the-money call has a delta of roughly 0.50; as expiration approaches, it will approach either 0 or 1, depending on whether the stock is below or above the strike. Vega decay and delta acceleration happen simultaneously.

[Gamma](/gamma/) (the rate of change of delta) also rises near expiration as the option's directional sensitivity becomes binary.

Together, these dynamics make near-the-money options near expiration highly kinetic—one tick in the stock's price causes a large swing in delta, and time decay pounds the position daily.

## Implications for Traders

**Long volatility positions decay.** If you buy calls or puts to express a volatility view, you are short theta and long vega. If volatility does not change, your position loses money every day, and the rate of loss accelerates as expiration nears. You *need* volatility to move, and you need it soon, to overcome time decay.

**Short volatility positions bleed optionality.** If you sell calls or puts (or sell a straddle), you are long theta and short vega. If volatility does not move—if the stock stays flat and implied volatility remains flat—you profit from time decay. But that profit shrinks as vega approaches zero, because there is less volatility left to sell.

**Rolling or exiting before expiration is often cheaper.** If you hold a position into the last 5 days, vega becomes worthless, and you are fighting pure time decay. Many traders exit positions one month before expiration precisely to avoid this zone. You also avoid the [liquidity](/liquidity-risk/) risk of closing a near-expired option, which often trades in wide bid-ask spreads.

**Near-the-money options are vulnerable.** An at-the-money option 5 days to expiration has almost no intrinsic value and almost no time value (because vega is near zero). A tiny move against you can wipe it out.

> Vega decay is relentless: do not fight it unless you have a sharp, near-term volatility forecast.

## The Final Week

In the last 7 days, an [option](/option/) is essentially a binary bet on intrinsic value at expiration. If you own a call and the stock is trading below the strike, the vega is so close to zero that no amount of volatility will save you. The only path to profit is an immediate rally above the strike. If you own a call and the stock is already above the strike but close to it, a small dip could [expire worthless](/expiration-date/).

This is why experienced traders often close positions a week or more before expiration. The probability of the expected move is baked in; vega is worthless; theta is your only enemy. Why stay and fight?

## See also

<div class="wiki-seealso">

### Closely related

- [Vega](/vega/) — The Greek measuring volatility sensitivity
- [Implied Volatility](/implied-volatility/) — The input to vega; what vega measures sensitivity to
- [Time Decay (Theta)](/time-decay-theta/) — The competing Greek that accelerates as vega falls
- [Delta](/delta/) — Directional exposure that shifts as expiration nears
- [Gamma](/gamma/) — The rate of delta change, which accelerates near expiration

### Wider context

- [Option](/option/) — The instrument whose vega decays
- [Black-Scholes Model](/black-scholes-model/) — The framework that formalizes vega decay
- [Derivatives Hedging](/derivatives-hedging/) — The use of vega in risk management
- [Call Option](/call-option/) — Specific instrument affected by vega decay
- [Put Option](/put-option/) — The inverse instrument, equally subject to vega decay

</div>

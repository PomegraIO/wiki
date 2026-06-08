---
title: "Realised Volatility vs Implied Volatility"
description: "Understand the difference between realised volatility (actual past price swings) and implied volatility (market's forward-looking forecast), and what the spread signals."
keywords:
  - realised volatility vs implied volatility
  - historical volatility
  - volatility pricing options
  - volatility term structure
  - vix index
image: /svg/ratios.svg
---

*The **realised volatility vs implied volatility** gap reveals whether the market is over- or under-pricing future price swings. Realised volatility measures the actual percentage swings that occurred; implied volatility is the market's consensus forecast embedded in option prices. A wide spread between them often signals rich or cheap options, shifts in risk appetite, or regime changes ahead.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Realised vs Implied Volatility — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two measures of volatility shape option pricing and portfolio hedging decisions.</div>

|   |   |
|---|---|
| **Realised volatility** | Calculated from actual historical price returns; backward-looking |
| **Implied volatility** | Extracted from option market prices; forward-looking consensus |
| **Common measure** | Realised: annualised standard deviation; Implied: indexed in the VIX for the S&P 500 |
| **Calculation timing** | Realised: computed after the fact; Implied: observed in real time |
| **Typical spread** | IV often exceeds RV in calm markets; narrows or reverses in crises |
| **Trading signal** | IV ≫ RV can suggest overpriced hedges; IV ≪ RV may signal undervalued options |

</aside>

## Realised Volatility: What Actually Happened

Realised volatility is a statistic. It measures the *annualised* standard deviation of returns that *already* occurred over a past window—typically 20, 60, or 252 trading days. The math is straightforward: calculate daily returns, find the standard deviation of those returns, annualise it (usually by multiplying by √252), and you have realised volatility.

A stock trading between $95 and $105 over a month has low realised volatility; one that swings from $80 to $120 has high realised volatility. The figure is objective and historical. Traders compute it in spreadsheets; it never guesses. The choice of lookback window matters—a 20-day realised volatility is noisier and more responsive to recent shocks than a 252-day one.

## Implied Volatility: The Market's Forecast

Implied volatility is the *reverse-engineered* forecast. When a market maker quotes an option price, that price contains an assumption about how volatile the underlying will be *over the option's life*. By plugging an option's market price into the [Black-Scholes model](/black-scholes-model/) and solving for volatility, traders extract implied volatility. It is the volatility assumption that makes the observed price "correct" under the model.

Implied volatility is not a single number for an asset. It varies by strike price (the "volatility smile") and by expiration date (the "term structure"). Near-term options often have higher IV than longer-dated ones in turbulent periods. IV moves continuously as market sentiment shifts; it reflects **collective opinion**, not past fact.

## Why the Two Diverge

Realised and implied volatility are often unequal because they answer different questions. Realised volatility answers "what happened?" Implied volatility answers "what does the market think will happen?" The gap widens when:

**Risk appetite shifts.** In calm markets, investors are complacent and accept low hedging prices. IV sinks relative to the realised volatility you'd measure over the same window. When fear spikes—earnings shock, geopolitical event, rate shock—investors bid up option prices immediately, and IV can surge well above realised volatility.

**Earnings or events approach.** An earnings announcement in two weeks is certain to move a stock, but you don't know the *direction*. IV for short-dated options reflects the *magnitude* of that event, even if realised volatility in the run-up is calm. Once the event occurs and the stock settles, realised volatility for that period may exceed the IV that priced it.

**Volatility of volatility.** Some periods are inherently more choppy. High-IV regimes tend to spike suddenly and stay elevated; low-IV regimes are stable but brittle. Options pricing reflects this regime uncertainty, so IV can remain elevated even as recent realised volatility is low.

## Reading the Spread: What It Signals

A wide gap between IV and realised volatility is rarely random. It usually means one of three things:

**IV ≫ RV (implied well above realised):** Hedging is expensive. Options are priced for volatility that hasn't been realised yet. This often occurs just before major announcements or in periods of geopolitical uncertainty. Sellers of options profit if volatility remains low; buyers pay a steep premium for safety.

**IV ≪ RV (implied well below realised):** Hedging is cheap, but options prices have not caught up to recent chaos. This can happen if realised volatility spiked suddenly (a one-day shock) and IV hasn't fully repriced yet, or if the market believes the spike is temporary and volatility will normalise.

**Converging IV and RV:** As an option nears expiration, IV must converge toward realised volatility, because there's less future time to surprise. In the final days before expiration, IV and RV are almost identical—the option's intrinsic value is known.

## Practical Uses: Trading and Hedging

Option traders exploit the IV–RV gap. A strategy called **volatility arbitrage** buys or sells options depending on whether IV is too high or low relative to expected realised volatility. If you believe realised volatility over the next month will be 20% but IV is priced at 30%, you short (sell) options and hedge with the underlying stock, profiting if realised stays low.

Portfolio managers use implied volatility as a forward-looking risk gauge. A spike in the VIX—the "fear index," derived from S&P 500 option prices—signals that hedging costs have soared. That often precedes equity weakness, though the relationship is not mechanical. Realised volatility, being backward-looking, is less useful for predicting tomorrow but is precise for measuring risk *that already occurred*.

## Volatility Regimes and the Term Structure

Implied volatility also organises itself across time. Short-dated options are often priced with higher IV than long-dated ones (an inverted term structure) during crises, because near-term uncertainty is acute. Once the crisis passes, the curve normalises. Conversely, in calm markets, the IV term structure can be flat or slightly upward-sloping.

Realised volatility does not have a term structure—it is computed over a fixed lookback window. But traders do compute rolling realised volatility (20-day, 60-day) to see if volatility is stable or trending.

## Inflation, Rates, and Volatility Expectations

In high-inflation environments, realised volatility often rises because central banks tighten policy, rate shocks are larger, and earnings forecasts swing wide. Implied volatility, however, can react faster—options prices snap up before realised volatility has fully climbed. The initial IV spike may exceed the eventual realised swing, especially if the inflation scare fades.

The reverse can happen in deflation scares: markets price catastrophic risk into IV, but realised volatility stays modest because central banks flood the market with liquidity.

## See also

<div class="wiki-seealso">

### Closely related

- VIX Index — the "fear gauge" of option-implied volatility for the S&P 500
- [Historical Volatility](/historical-volatility/) — standard measure of realised price swings
- [Implied Volatility](/implied-volatility/) — forward-looking market forecast baked into option prices
- [Option Premium](/option-premium/) — price paid for an option, shaped by both IV and time decay
- [Black-Scholes Model](/black-scholes-model/) — the framework used to extract IV from observed option prices
- [Volatility Smile](/volatility-smile/) — the pattern that IV varies by strike, hinting at tail risk fears

### Wider context

- [Option](/option/) — call and put contracts whose prices embed volatility forecasts
- [Time Decay (Theta)](/time-decay-theta/) — how options lose value as expiration nears, separate from volatility
- [Market Risk](/market-risk/) — broader framework for measuring portfolio volatility and hedging
- [Sharpe Ratio](/sharpe-ratio/) — risk-adjusted return metric that uses volatility as the denominator

</div>

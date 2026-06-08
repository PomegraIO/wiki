---
title: "Implied Volatility vs Historical Volatility: Key Differences"
description: "Implied volatility is what the market prices into options now; historical volatility is what the stock actually did. The gap reveals fear, opportunity, and model risk."
keywords:
  - implied volatility vs historical volatility
  - forward-looking volatility
  - realized volatility
  - volatility forecast
  - option pricing risk
  - vega exposure
---

*Implied volatility is the forward-looking volatility the option market is pricing in right now; historical volatility is the backward-looking realized volatility the stock actually experienced. When implied exceeds realized, the market expects more turbulence ahead; when it lags, the market underestimates upcoming swings.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Implied Volatility vs Historical Volatility — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">One looks forward; one looks back. The gap predicts whether option buyers or sellers are better positioned.</div>

|   |   |
|---|---|
| **Implied volatility** | What option prices imply about expected volatility |
| **Historical volatility** | Realized vol over the past 20, 60, or 252 trading days |
| **Implied > Realized** | Market is nervous; option premiums are expensive |
| **Implied < Realized** | Market is complacent; option premiums are cheap |
| **Measurement** | IV from option market; HV from daily or intra-day returns |
| **Use** | IV prices options; HV forecasts realized moves |

</aside>

## What is historical volatility?

**Historical volatility** measures how much the stock price actually moved over a past period. The most common calculation is:

1. Collect daily closing prices over N days (typically 20, 60, or 252 trading days).
2. Calculate log returns: ln(Price_today / Price_yesterday).
3. Compute the standard deviation of those returns.
4. Annualize: multiply by √252 (the number of trading days in a year).

A stock with 20-day realized volatility of 2% annualizes to roughly 32% annualized vol (2% × √252 ≈ 32%). This is a backward-looking, mechanical calculation based purely on observed price swings.

Different lookback windows tell different stories:
- **20-day vol** captures recent choppiness and is sensitive to the last few trading days.
- **60-day vol** smooths out daily noise and reflects a quarter's worth of movement.
- **252-day vol** (one full year) is the "true" long-term realized vol for that year, but you only know it at year-end, making it less useful for daily trading decisions.

## What is implied volatility?

**Implied volatility** is the volatility number that, when plugged into an option pricing model like [Black-Scholes](/black-scholes-model/), produces the observed market price of the option.

For example:
- An at-the-money call on Stock XYZ is trading at $2.50.
- Using Black-Scholes with spot $100, strike $100, 30 days to expiration, and risk-free rate 5%, you solve for the volatility that gives a $2.50 price.
- That vol is the **implied volatility**—typically 35% annualized.

Implied volatility is **forward-looking** because it reflects the collective consensus of option traders about how much the stock will move between now and expiration. Traders bid up call and put prices when they expect turbulence; they bid them down when they expect calm.

Implied vol is also **market-price-derived**: it's not a forecast you make yourself, but an inference you extract from what options are actually trading for. If you see a call trade at a price that implies 40% vol, you know the buyer and seller agreed that 40% was the right bet on future volatility.

## Historical vol is easier to measure; implied vol is harder to interpret

Historical vol is purely mechanical. Look at past prices, calculate returns, compute standard deviation. No judgment required. But it has a fatal flaw: it's always outdated. By the time you observe realized volatility, the opportunity has passed.

Implied vol is harder to extract (you need to invert an option pricing formula), but it points forward. It embeds the market's consensus about what's coming. However, that consensus can be wrong: market participants are sometimes too fearful (IV too high) or too complacent (IV too low).

## The gap between implied and realized

The trading opportunity lies in the gap. When **implied volatility > realized volatility**, option premiums are expensive. An option buyer paying $2.50 for a call that turns out to require only 30% vol to replicate is overpaying. A seller of that call, on the other hand, is receiving more premium than realized risk warrants.

When **implied volatility < realized volatility**, option premiums are cheap. An option buyer gets a bargain; a seller is undercompensated for the risk they're taking.

### Why the gap exists

1. **Uncertainty about future events.** Before earnings, an option's implied volatility spikes because traders don't know if the company will beat or miss. If the stock ends up moving a modest 2% but IV was 40%, realized volatility fell far short of implied. The opposite happens if the stock crashes 10%—realized vol exceeds implied, and option buyers win.

2. **Tail risk and skew.** Traders are willing to pay a premium for protection, similar to insurance. Out-of-the-money puts on equity indices are consistently more expensive (higher implied vol) than calls, even if historical returns are symmetric. This "insurance premium" means IV exceeds realized vol more often than not for puts.

3. **Sentiment and fear cycles.** Panic drives IV up even when nothing new has happened. In 2020, the VIX (the equity market's implied volatility index) hit 80 in March, though realized vol that month was perhaps 50. The discrepancy reflected extreme fear and a scramble for protection.

4. **Model assumptions breaking.** Realized volatility is calculated assuming returns are independent (each day's move doesn't predict the next day's). But returns actually [cluster](/volatility-clustering/): calm days tend to follow calm days, and volatile days follow volatile days. This autocorrelation in volatility can cause realized moves to be larger in clusters than a constant-volatility model predicts, even if the average volatility is stable.

## When each measure is more useful

**Use implied volatility to:**
- **Price options.** IV is the standard input for every option pricing model. Buy or sell options by comparing market IV to your own vol forecast.
- **Assess relative value.** Is the 30-day IV higher or lower than the 60-day IV? Are puts more expensive than calls? These comparisons reveal market sentiment and skew.
- **Forecast realized volatility.** High implied vol is a weak predictor of realized vol, but it's better than historical vol alone. Sophisticated models blend the two.
- **Evaluate option strategies.** A [covered call](/covered-call/) seller wants implied vol to be high (to earn more premium) but realized vol to be low (to avoid assignment). Comparing the two shapes strategy choices.

**Use historical volatility to:**
- **Estimate trend and mean reversion.** If 20-day vol is 50% but 252-day vol is 20%, the stock is in an unusual spike. This might signal mean reversion coming (vol reverts to 20%) or signal that a new regime is starting.
- **Hedge portfolio Greeks.** When you don't have option prices (e.g., for illiquid OTC derivatives), historical vol gives you a volatility estimate for Greeks like [delta](/delta/) and [gamma](/gamma/).
- **Backtest strategies.** Historical vol is the input you plug into models when testing what would have happened in the past under different trading rules.
- **Communicate realized risk.** "This stock moved 3% per day on average last month" is immediately interpretable. It describes what actually happened.

## The relationship between implied and realized

Over long periods, implied and realized volatility converge on average. A stock's 252-day realized vol tends to cluster around its average level of prior implied vols. But on any single 30-day period, they can diverge significantly:

- **Low IV, high realized:** The market was too complacent. Option sellers got hurt; option buyers benefited.
- **High IV, low realized:** The market was too fearful. Option buyers overpaid; option sellers were protected by a large premium.
- **Both low:** A calm period confirmed by both past and expected future moves.
- **Both high:** Turbulence now and expected to continue.

Savvy option traders constantly compare the two. If implied vol is 30% but historical vol is 20%, and there's no obvious event coming, they might sell options (collecting premium for vol they believe will revert lower). If implied is 20% but historical is 40%, and the event that caused the spike hasn't fully played out, they might buy options.

## Measuring implied volatility across strikes and dates

Implied volatility is not uniform. A stock might have 30-day implied vol of 25% at-the-money but 35% out-of-the-money on puts and 20% out-of-the-money on calls—the [volatility skew](/volatility-skew-explained/). The 60-day IV might be 22%, reflecting mean reversion expectations.

Option traders track not just a single "implied vol" but an entire **volatility surface**: implied vol as a function of both strike and time to expiration. Pricing and hedging require this full map.

Historical volatility, by contrast, is simpler: one number per lookback period, the same for all strikes and dates. This simplicity is both a strength (easy to compute and explain) and a weakness (ignores the market's richer information about where turbulence is concentrated).

## See also

<div class="wiki-seealso">

### Closely related

- [Implied volatility](/implied-volatility/) — definition and how traders observe it
- [Historical volatility](/historical-volatility/) — realized past movements
- [Volatility skew explained](/volatility-skew-explained/) — why IV varies across strikes
- [Black-Scholes assumptions limitations](/black-scholes-assumptions-limitations/) — how constant-volatility assumption breaks
- [Vega](/vega/) — option sensitivity to IV changes

### Wider context

- [Option](/option/) — fundamental derivative contract
- Options — pricing and hedging framework
- [Volatility smile](/volatility-smile/) — empirical pattern of IV across strikes
- [Derivatives hedging](/derivatives-hedging/) — use of implied vol in risk management

</div>

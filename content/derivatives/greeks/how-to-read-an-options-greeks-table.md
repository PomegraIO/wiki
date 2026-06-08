---
title: "How to Read an Options Greeks Table"
description: "Guide to interpreting delta, gamma, theta, vega, and rho columns in an options chain, sign conventions, and practical use."
keywords:
  - options greeks table
  - delta gamma theta vega rho
  - options chain interpretation
  - greeks sign convention
  - option sensitivity metrics
---

*An **options greeks table** shows the sensitivity of [option](/option/) prices to changes in underlying price, volatility, time, and interest rates. The columns—[delta](/delta/), [gamma](/gamma/), [theta](/theta/), [vega](/vega/), and [rho](/rho/)—are numerical derivatives that summarize how much an option's value will move if its market inputs shift. Reading the table correctly requires understanding sign conventions (positive or negative), typical ranges, and what each greek reveals about risk. Traders and portfolio managers use these metrics to monitor hedge ratios, decay, and directional exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Options Greeks — sign conventions and ranges</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Five sensitivity metrics that quantify option price movements.</div>

|   |   |   |
|---|---|---|
| **Greek** | **Measures** | **Sign & Range** |
| **Delta** | Price sensitivity to 1-point move in underlying | +1.0 to 0 (calls); 0 to –1.0 (puts) |
| **Gamma** | Rate of change of delta | Always positive (both calls and puts) |
| **Theta** | Daily time decay (value loss per day) | Usually negative (calls & puts lose value) |
| **Vega** | Price sensitivity to 1% change in volatility | Positive for both calls and puts |
| **Rho** | Price sensitivity to 1% change in interest rates | Positive for calls; negative for puts |

</aside>

## The Purpose of a Greeks Table

Before diving into the table itself, understand what you are looking at. A broker's [options chain](/option/) display shows strike prices, bid-ask prices, and implied volatility. The greeks overlay a layer of mathematical analysis: they quantify how sensitive each option is to different market moves.

A trader might see an option priced at $2.50 with a delta of 0.40. That delta tells you: if the underlying stock rises by $1, this option's price should rise by approximately $0.40. Without the greek, you have only the price; with it, you understand the option's behavior.

The greeks are partial derivatives from the [Black-Scholes model](/black-scholes-model/) or other pricing models. They are not predictions—they are snapshots of how the option reacts to tiny moves in each input. As market conditions change, the greeks themselves change.

## Delta: Direction and Probability

**Delta** is the most widely used greek. It has two interpretations:

**Hedge ratio:** Delta tells you how many shares of the underlying you would need to short to neutralize price movement. A call with delta 0.60 behaves like owning 0.60 shares—if the stock rises $1, the call gains $0.60. To hedge that call, you would short 0.60 shares.

**Probability of finishing in the money:** Delta approximates the risk-neutral probability that the option will finish [in-the-money](/in-the-money/) at expiration. A call with delta 0.70 has about a 70% chance of expiration value. (This is not a real-world probability; it is a model-derived measure useful for rough intuition.)

**Sign conventions:**
- **Call options:** Delta ranges from 0 (far out-of-the-money) to +1.0 (deep in-the-money). Positive delta means the call gains value when the underlying rises.
- **Put options:** Delta ranges from 0 (far out-of-the-money) to –1.0 (deep in-the-money). Negative delta means the put gains value when the underlying falls. An [at-the-money](/at-the-money/) put has delta around –0.50.

**At-the-money options** have deltas near +0.50 (calls) and –0.50 (puts), indicating roughly equal probability of finishing in or out of the money.

## Gamma: Delta Sensitivity

**Gamma** measures how fast delta itself changes as the underlying price moves. It is the second derivative of price.

If an option has low gamma, its delta stays relatively stable even if the underlying swings. If gamma is high, delta changes rapidly with small price moves.

**Sign conventions:**
- **Gamma is always positive** for both calls and puts. This means delta becomes less negative (for puts) or more positive (for calls) as the underlying rises. Gamma is always "helpful" to the option holder—it amplifies gains as they move in your direction.
- Gamma is highest for **at-the-money options** and falls as you move far in-the-money or out-of-the-money.
- Shorter time to expiration means higher gamma (for a given moneyness). A one-week at-the-money option has much higher gamma than a six-month one.

**Practical use:** Gamma is the hidden cost of being wrong. If you buy a call and the stock falls, your delta loss accelerates (gamma works against you). If you sell an option, you are short gamma—you profit from the option's delta staying stable, but you lose if the underlying whipsaws.

## Theta: Time Decay

**Theta** measures the daily loss in option value due to the passage of time, assuming all other inputs (price, volatility) stay constant. It is the time decay greek.

**Sign conventions:**
- **Theta is usually negative** for long calls and long puts—the option loses value as expiration approaches.
- **Theta is usually positive** for short calls and short puts—you profit from time decay.
- Theta is typically expressed as a daily figure (e.g., –0.05 means the option loses $0.05 per day).

**Magnitude and expiration:**
- At-the-money options have the most theta (largest absolute value).
- Theta accelerates sharply in the final week before expiration.
- Far out-of-the-money and deep in-the-money options have low theta.

**Practical use:** Theta is the engine of option selling strategies. A [covered call](/covered-call/) writer earns income from theta decay. A buyer of options fights against theta; they need the underlying to move fast enough to offset daily theta losses.

## Vega: Volatility Sensitivity

**Vega** measures the option's price change for a 1 percentage-point change in [implied volatility](/implied-volatility/).

If an option has vega of 0.15, a 1-point rise in implied volatility (say, from 20% to 21%) increases the option's price by $0.15.

**Sign conventions:**
- **Vega is positive for both calls and puts.** Higher volatility increases both call and put values because it increases the odds of larger moves, expanding the payoff tail.
- Vega is largest for at-the-money options and falls as you move far in-the-money or out-of-the-money.
- Longer-dated options have higher vega; short-term options have low vega.

**Practical use:** Vega exposure matters if you believe volatility will change. A long position in options (long call or long put) is long vega—you profit if volatility rises. A short straddle or strangle is short vega—you profit if volatility falls. Many traders monitor vega separately from delta to understand whether their profit or loss is coming from directional moves or volatility changes.

## Rho: Interest-Rate Sensitivity

**Rho** measures the option's price change for a 1 percentage-point change in interest rates (e.g., from 4% to 5%).

In most markets, rho is the least impactful greek because interest rates change slowly and their effect on near-term options is tiny.

**Sign conventions:**
- **Call options have positive rho.** Rising interest rates increase call values slightly because they reduce the present value of the strike price (which you pay in the future).
- **Put options have negative rho.** Rising interest rates decrease put values because they reduce the present value of the strike, which the put holder receives.
- Rho is larger for longer-dated options and deep in-the-money options.

**Practical use:** For stock options expiring within a few months, rho is often negligible. For long-dated options or options on bonds, rho becomes more significant.

## Reading a Real Options Table

Imagine you are looking at a call option table for a stock trading at $100:

| Strike | Price | Delta | Gamma | Theta | Vega | Rho |
|--------|-------|-------|-------|-------|-------|-----|
| 95     | $6.20 | 0.75  | 0.025 | –0.02 | 0.18  | 0.08 |
| 100    | $3.10 | 0.50  | 0.040 | –0.05 | 0.25  | 0.07 |
| 105    | $1.45 | 0.28  | 0.035 | –0.04 | 0.22  | 0.05 |

**The in-the-money call (95 strike):**
- Delta of 0.75 means the option moves $0.75 for every $1 move in the stock. It behaves much like owning 75 shares.
- Gamma of 0.025 is relatively low; delta is stable.
- Theta of –0.02 means it loses $0.02 per day—slow decay because it is already in-the-money.
- Vega of 0.18 means a 1-point rise in volatility adds $0.18 of value.

**The at-the-money call (100 strike):**
- Delta of 0.50 is textbook at-the-money behavior.
- Gamma of 0.040 is the highest—delta will change fastest here.
- Theta of –0.05 is the steepest (fastest decay) because this option is time-sensitive.
- Vega of 0.25 is the highest—volatility changes matter most here.

**The out-of-the-money call (105 strike):**
- Delta of 0.28 means the option moves only $0.28 per $1 move in stock—less sensitive to price.
- Gamma of 0.035 is still elevated (between the in-the-money and at-the-money).
- Theta of –0.04 is moderate; the option decays daily but slower than the at-the-money.
- Vega of 0.22 is high because volatility matters to long-shot payoffs.

## Key Behaviors to Remember

1. **Delta and gamma track each other.** As delta gets very high (deep in-the-money) or very low (far out), gamma shrinks. Gamma peaks at-the-money.

2. **Theta accelerates at expiration.** A one-month option decays steadily; a one-week option decays fast. Check the expiration date to interpret theta magnitude.

3. **Volatility and time interact.** If implied volatility is high, vega is larger. If time to expiration is short, vega is smaller.

4. **Greeks change every day.** The table is a snapshot. As the underlying price moves, all greeks update. A delta of 0.50 one day may be 0.55 or 0.45 the next.

5. **Gamma is your risk.** If you are short an option, gamma decay forces you to rehedge frequently in a volatile market. If you are long, gamma helps you if you are right about direction, but hurts if the underlying whipsaws.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — option price sensitivity to underlying price movement
- [Gamma](/gamma/) — rate of change of delta
- [Theta](/theta/) — time decay rate of an option
- [Vega](/vega/) — option price sensitivity to volatility changes
- [Rho](/rho/) — option price sensitivity to interest rate changes
- [Option](/option/) — financial contract granting the right to buy or sell at a fixed price
- [Implied Volatility](/implied-volatility/) — market's expectation of future stock-price moves
- [Black-Scholes Model](/black-scholes-model/) — foundational option pricing formula

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — using options to manage market risk
- [Covered Call](/covered-call/) — sell call options against held stock for income
- [In-the-Money](/in-the-money/) — option with immediate intrinsic value
- [Strike Price](/strike-price/) — fixed price at which option can be exercised

</div>

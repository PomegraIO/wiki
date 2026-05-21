---
title: "Options Greeks"
description: "The Greeks are five key metrics that measure how an option's price changes in response to different market factors: delta, gamma, theta, vega, and rho."
keywords:
  - options greeks
  - delta
  - gamma
  - theta
  - vega
  - rho
  - option greeks
  - risk metrics
image: "https://picsum.photos/seed/options-greeks/900/600"
---

*The **Greeks** are a set of partial derivatives—mathematical measures of sensitivity—that quantify how an option's price responds to changes in five key factors: the underlying asset price ([delta](/delta)), the rate of delta change ([gamma](/gamma)), time passage ([theta](/theta)), [volatility](/historical-volatility) ([vega](/vega)), and interest rates ([rho](/rho)). Together, the Greeks provide traders and risk managers with a complete toolkit for understanding option behavior, hedging positions, and pricing derivatives.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Options Greeks — key facts</div>

<img src="https://picsum.photos/seed/options-greeks/900/600" alt="The five Greek letters representing risk metrics" />

<div class="wiki-infobox-caption">The Greeks quantify option price sensitivities.</div>

|   |   |
|---|---|
| **What they measure** | Price sensitivity to five factors |
| **Number of primary Greeks** | Five: delta, gamma, theta, vega, rho |
| **Second-order Greeks** | Charm, vanna, volga (less common) |
| **Computed from** | Black-Scholes or other pricing models |
| **Used for** | Hedging, risk management, position monitoring |
| **Updated frequency** | Continuously throughout trading day |
| **Sign interpretation** | Positive/negative tells you direction of sensitivity |
| **Sum across portfolio** | Allows net Greeks for entire position |
| **Delta-hedging** | Using delta to neutralize directional risk |
| **Gamma risk** | Cost of delta-hedging; edge of knife |

</aside>

## The five Greeks

**Delta:** Measures how much the option's price changes for each $1 move in the underlying asset. A delta of 0.5 means the option moves $0.50 for every $1 move in the stock. [Call option](/call-option) deltas range from 0 to 1; [put option](/put-option) deltas range from -1 to 0.

**Gamma:** Measures how much delta itself changes for each $1 move in the underlying. Gamma is highest for [at-the-money](/at-the-money) options and lowest for deep [in-the-money](/in-the-money) or [out-of-the-money](/out-of-the-money) options. Gamma risk is the cost of hedging; as the stock moves, you must rehedge, locking in losses.

**Theta:** Measures daily [time value](/time-value) decay. Also called "time decay," theta is negative for option buyers (you lose money daily) and positive for option sellers (you profit daily). Theta accelerates as [expiration date](/expiration-date) nears.

**Vega:** Measures how much the option's price changes for each 1% change in [implied volatility](/implied-volatility). Higher [volatility](/historical-volatility) increases option prices (both calls and puts); lower [volatility](/historical-volatility) decreases them. Vega is highest [at-the-money](/at-the-money) and zero for deep in/out-of-the-money.

**Rho:** Measures sensitivity to interest rate changes. [Call options](/call-option) gain value when rates rise (rho is positive); [put options](/put-option) lose value when rates rise (rho is negative). Rho's impact is usually small unless the option has many months to expiration.

## Why traders use the Greeks

The Greeks turn abstract option theory into actionable risk management. A trader managing a portfolio of 100 option positions can sum up the [delta](/delta) across all positions to know the portfolio's directional exposure. A [delta](/delta) of +500 means the portfolio moves like owning 5 shares of the underlying (per share basis).

Similarly, summing [vega](/vega) tells you the portfolio's total sensitivity to [volatility](/historical-volatility) changes. If total vega is +1000, a 1% volatility rise profits the portfolio $1000 (all else equal).

## Delta hedging and rebalancing

A key use of [delta](/delta) is **delta hedging**—maintaining a net-zero [delta](/delta) by balancing long and short positions. A trader long 100 [call options](/call-option) with a delta of 0.5 each (total delta +50) can hedge by short-selling 50 shares. If the stock rises $1, the calls gain $50 but the short shares lose $50, netting zero.

But [gamma](/gamma) creates a problem: as the stock rises, the [delta](/delta) of the calls increases (becomes more positive), so the hedge becomes imperfect. The trader must rehedge. When rehedging into a rising market (buying stock as the stock rises), you lock in losses. This is gamma risk—the cost of dynamic hedging.

## Greeks and the Black-Scholes model

The [Black-Scholes model](/black-scholes-model) not only prices options but also provides closed-form formulas for all five Greeks. For [european-option](/european-option) calls and puts, the Greeks can be computed exactly. For exotic or [american-option](/american-option) options, the Greeks must be approximated numerically.

In practice, every broker, trading desk, and options pricing service provides Greeks automatically, updated continuously during the trading day.

## Second-order Greeks

Beyond the five primary Greeks, traders sometimes reference second-order Greeks:

- **Charm:** The rate of change of [delta](/delta) with time. Charm tells you how your hedge becomes stale as time passes.
- **Vanna:** The rate of change of [delta](/delta) with [volatility](/historical-volatility). Tells you how hedges become imperfect when volatility shifts.
- **Volga:** The rate of change of [vega](/vega) with [volatility](/historical-volatility). Tells you how volatility sensitivity changes when volatility spikes.

These are less commonly quoted but important for precise hedging.

## Sign conventions

- **Delta:** Positive for calls (higher stock = higher option value); negative for puts.
- **Gamma:** Always positive (option value is convex).
- **Theta:** Negative for long options (decay works against you); positive for short options.
- **Vega:** Positive for both calls and puts (higher volatility = higher value for both).
- **Rho:** Positive for calls; negative for puts.

## Practical example

Suppose you own 100 [call options](/call-option) struck at $100 with the stock at $105, 30 days to expiration:
- Total delta might be +4500 (you have directional exposure equivalent to 45 shares).
- Total gamma might be +300 (for each $1 stock move, delta increases/decreases by 300, or 3 deltas per share).
- Total theta might be -500 (you lose $500 per day to time decay).
- Total vega might be +3000 (a 1% volatility spike gains you $3000).

These four numbers tell you everything about your position's risk.

## See also

<div class="wiki-seealso">

### The five Greeks

- [Delta](/delta/) — stock price sensitivity
- [Gamma](/gamma/) — delta change rate
- [Theta](/theta/) — time decay
- [Vega](/vega/) — volatility sensitivity
- [Rho](/rho/) — interest rate sensitivity

### Related concepts

- [Black-Scholes model](/black-scholes-model/) — derives the Greeks
- [Option premium](/option-premium/) — Greeks measure premium sensitivity
- [Implied volatility](/implied-volatility/) — vega input and output
- [Historical volatility](/historical-volatility/) — realized vs. expected moves

### Strategies

- [Delta hedging](/call-option) — using delta to neutralize risk
- Gamma scalping — profiting from gamma while hedging delta
- [Volatility trading](/volatility-smile/) — using vega to bet on volatility changes
- Calendar spread — exploiting theta decay

### Deeper context

- [Option](/option/) — the family of derivatives
- [Risk management](/hedge-fund/) — using Greeks for portfolio hedging
- [Derivatives pricing](/black-scholes-model/) — Greeks quantify pricing sensitivities

</div>

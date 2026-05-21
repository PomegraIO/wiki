---
title: "Barrier Option"
description: "A barrier option becomes active or worthless when the underlying asset's price crosses a predetermined level, making it cheaper and more exotic than vanilla options."
keywords:
  - barrier option
  - knock-in option
  - knock-out option
  - exotic option
  - path-dependent derivative
image: "/svg/derivatives.svg"
---

*A **barrier option** is an exotic derivative whose existence or payoff is contingent on the underlying asset's price reaching (or not reaching) a specified level—the "barrier"—at any point before [expiration](/expiration-date). If the barrier is crossed, a knock-in option activates; a knock-out option expires worthless. This path-dependent structure makes barrier options cheaper and more tailored to specific hedging needs than [vanilla option](/call-option) alternatives.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Barrier Option — key facts</div>

<img src="/svg/derivatives.svg" alt="Price chart with a horizontal barrier level marked" />

<div class="wiki-infobox-caption">A barrier level (line) determines whether the option lives or dies.</div>

|   |   |
|---|---|
| **Barrier types** | Up-and-in, up-and-out, down-and-in, down-and-out |
| **Activation** | Knock-in: barrier crossed; knock-out: barrier avoided |
| **Strike price** | Usually set independently of barrier |
| **Price vs. vanilla** | Cheaper (lower payoff probability) |
| **Monitoring** | Continuous throughout holding period |
| **Path-dependent** | Yes; full history matters |
| **Typical use** | Cheap hedges, binary outcomes |
| **Settlement** | Cash or physical |
| **Liquidity** | Lower than vanilla options |

</aside>

## The four barrier types

A barrier option can be one of four combinations:

1. **Up-and-in (UIO) call:** The option is worthless until the asset price rises to the barrier level; once crossed, the option comes to life. Useful if you want downside protection only if the price rallies first (e.g., a takeover rumor scenario).

2. **Down-and-in (DIO) put:** The option is worthless until the asset price falls to the barrier; then it activates. Useful if you want downside insurance only if the price crashes hard (e.g., a tail-hedge scenario).

3. **Up-and-out (UOO) call:** The option is active until the price rises to the barrier, at which point it expires worthless. Useful if you want bullish exposure that cancels if the stock soars past a certain level (e.g., to cap risk before a company event).

4. **Down-and-out (DOO) put:** The option is active until the price falls to the barrier, then expires worthless. Useful if you want downside protection that cancels if the crash is severe (reducing cost by eliminating worst-case hedging).

## Why barrier options are cheaper

A [knock-out](/knock-out-option) option is cheaper than a vanilla [call option](/call-option) because it can disappear if the stock makes a big move. A [knock-in](/knock-in-option) option is cheaper because it starts worthless; you pay for the *chance* it will activate, not the certainty that it exists.

An up-and-out call struck at $100 with a barrier at $120 is much cheaper than a vanilla call at $100, because if the stock rockets past $120, the option vanishes and you get nothing. The buyer is implicitly betting that the stock will rise to his profit level ($105–$119) without crossing the barrier at $120.

Similarly, a down-and-in put struck at $90 with a barrier at $70 is much cheaper than a vanilla put at $90, because the put is dormant unless the stock crashes below $70. The buyer is hedging only catastrophic downside, not everyday volatility.

## Risk transfer and hedging

Barrier options let companies hedge selectively. Suppose a stock is trading at $100 and you own shares. A vanilla [put option](/put-option) struck at $90 protects you below $90, costing (say) $2 per share. But a down-and-in put struck at $90 with a barrier at $70 costs only $0.50 per share, because it activates only if the crash is severe.

This trade-off makes sense if you are willing to accept losses between $90 and $70 (which are rare in normal markets) to save [premium](/option-premium) on routine downside. You keep the tail-hedge cheaply.

Similarly, a corporate treasurer wanting to hedge currency exposure for a deal that may or may not close can use a knock-in option. The option is dormant until the deal is announced (the "barrier" is the news), at which point the hedge activates. This saves [premium](/option-premium) for a contingent liability.

## Monitoring and activation

Barrier options are monitored continuously throughout their life, typically at the settlement price or high/low of each trading day, depending on the contract. The barrier level is fixed at inception.

Once the barrier is crossed, it cannot be uncrossed for a knock-out (the option is gone) or a knock-in (the option remains active forever after). The crossing is binary and irreversible. Some exotic structures allow the barrier to be reset or include a "rebate" (a small payment) if a knock-out is triggered.

## Pricing barrier options

Valuing barrier options requires accounting for the probability that the barrier is hit. [Black-Scholes model](/black-scholes-model) extensions exist for vanilla barrier options, particularly in currency and interest-rate markets. The key input is the probability of hitting the barrier level given the current price, the barrier level, [volatility](/historical-volatility), and time to [expiration](/expiration-date).

Higher [volatility](/historical-volatility) increases the probability of hitting any barrier, so it increases the value of knock-in options and decreases the value of knock-out options. A knock-out becomes cheaper when volatility rises (more likely to be knocked out). A knock-in becomes more expensive (more likely to activate).

## Greeks and path dependency

[Delta](/delta) for a barrier option depends on distance to the barrier. A call deep in-the-money but also near a knock-out barrier has lower [delta](/delta) than an otherwise similar vanilla call, because crossing the barrier kills the option. [Gamma](/gamma) can spike near the barrier level, where small price moves drastically change the payoff probability.

[Vega](/vega) (sensitivity to [volatility](/historical-volatility)) is negative for knock-out options and positive for knock-in options, the reverse of a vanilla option's vega in some regimes. This makes hedging barrier options more complex.

## Common variations

Some barrier options include a **rebate**—if the barrier is touched, the holder receives a fixed payment (e.g., 5% of the premium paid). This reduces the cost relative to a vanilla option but not as much as a barrier option without a rebate.

**Double-barrier options** have both an upper and lower barrier. The option is active until either barrier is crossed. These are even cheaper and more exotic, used primarily in fixed-income and FX products.

## See also

<div class="wiki-seealso">

### Closely related

- [Knock-in option](/knock-in-option/) — activates when barrier is crossed
- [Knock-out option](/knock-out-option/) — terminates when barrier is crossed
- [Call option](/call-option/) — vanilla right to buy
- [Put option](/put-option/) — vanilla right to sell
- [Exotic option](/binary-option/) — non-standard payoff structure
- [Expiration date](/expiration-date/) — monitoring period end

### Pricing & Greeks

- [Black-Scholes model](/black-scholes-model/) — extended for barrier options
- [Implied volatility](/implied-volatility/) — affects barrier-crossing probability
- [Historical volatility](/historical-volatility/) — drives option value
- [Delta](/delta/) — path-dependent due to barrier proximity
- [Vega](/vega/) — reversed sign vs. vanilla options

### Deeper context

- [Option](/option/) — the family of derivatives
- [Path-dependent option](/asian-option/) — barrier options are also path-dependent
- [Volatility smile](/volatility-smile/) — exotic options show distinct volatility patterns

</div>

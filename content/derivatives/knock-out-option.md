---
title: "Knock-Out Option"
description: "A knock-out option terminates and becomes worthless if the underlying asset's price crosses a barrier level, making it cheaper than vanilla options."
keywords:
  - knock-out option
  - barrier option
  - termination
  - cancellation
  - exotic option
image: "/svg/derivatives.svg"
---

*A **knock-out option** (also **out-option**) is a [barrier option](/barrier-option) that terminates (expires worthless) if the underlying asset's price crosses a predetermined barrier level at any point before [expiration date](/expiration-date). Before the barrier is touched, it behaves like a vanilla [call](/call-option) or [put](/put-option). Once crossed, it is instantly worthless regardless of the underlying price at expiration. There are two types: **up-and-out** (terminates if price rises above the barrier) and **down-and-out** (terminates if price falls below the barrier). Knock-out options are cheaper than vanilla options because the payoff probability is reduced.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Knock-Out Option — key facts</div>

<img src="/svg/derivatives.svg" alt="Option terminating when barrier is breached" />

<div class="wiki-infobox-caption">Option dies if barrier is crossed.</div>

|   |   |
|---|---|
| **Types** | Up-and-out (UOC/UOP), down-and-out (DOC/DOP) |
| **Termination** | When spot price crosses barrier |
| **Pre-termination** | Behaves as vanilla option |
| **Post-termination** | Worthless; no recovery |
| **Barrier monitoring** | Continuous throughout option life |
| **Price vs. vanilla** | Cheaper (lower payoff probability) |
| **Moneyness** | Can be at, in, or out of the money |
| **Strike** | Independent of barrier level |
| **Primary use** | Cheap directional bets with risk cap |
| **Rebate option** | Some have payoff if barrier is hit |

</aside>

## How knock-out options work

A trader is bullish on a stock at $100 but worries about a sharp rally above $120 (which might trigger profit-taking). The trader buys an **up-and-out call**:

- Strike: $110
- Barrier: $120
- Premium: $1.00 (cheap vs. $1.50 for vanilla)

**Scenario 1:** Stock rises to $115 (below the barrier). The call is still alive and profitable ($115 − $110 = $5 profit).

**Scenario 2:** Stock rises to $130 (barrier crossed). The option is instantly knocked out and becomes worthless, regardless of the stock's final price being $130 (well above the $110 strike).

The trader has sacrificed the upside above $120 (capped gain) to pay less premium.

## Down-and-out options

A **down-and-out put** is eliminated if the stock price falls below the barrier. A shareholder owns stock and wants downside protection (via a put) but only if the decline is modest.

Example:
- Stock at $100; strike $90; barrier $70
- Premium: $0.40

If stock falls to $80 (between barrier and strike), the put protects. If stock crashes to $60 (below barrier at $70), the put is knocked out and provides no protection—exactly when you need it most!

This is why down-and-out puts are cheaper but riskier.

## Use cases

**Cheap directional bets:** An investor bullish on a stock buys an up-and-out call at low cost. The barrier is set at an unrealistic level; if hit, the rally has been so strong that losing the option is acceptable.

**Risk capping:** A trader wants directional exposure but is willing to sacrifice tail upside if the move is extreme (above barrier). Up-and-out lets them hedge the extreme tail cheaply.

**Income generation:** A seller of calls can cap downside risk by writing up-and-out calls (knocked out if price soars), accepting lower premium for limited liability.

## Rebate options

Some knock-out options include a **rebate**: if the barrier is hit, the buyer receives a fixed payment (e.g., 10% of the option's original premium). This softens the blow of knock-out and makes the contract more attractive to buyers.

## Path-dependency

Knock-out options are path-dependent: the complete price history matters. A stock that briefly spikes to $121 and falls back to $100 has knocked out your up-and-out call. A stock that rises smoothly to $100 has not.

This sensitivity makes knock-out options riskier during volatile periods and makes them valuable for reducing risk in calm periods.

## Barrier monitoring

Barriers are typically monitored at the settlement (close) price daily. Some contracts allow continuous monitoring, making knock-outs more likely (and cheaper).

A barrier at $120 monitored continuously can be breached by an intra-day spike to $120.01, even if the stock closes at $119.99. This hidden risk is why knock-out pricing is so cheap.

## Pricing knock-outs

Knock-out option pricing requires calculating the probability that the barrier will NOT be crossed before expiration.

Prob(no barrier hit) = 1 − Prob(barrier hit)

Higher [volatility](/historical-volatility) increases the probability of hitting the barrier, reducing knock-out value.

[Monte-carlo-options-pricing](/monte-carlo-options-pricing) simulates paths and checks if any price exceeds the barrier.

## See also

<div class="wiki-seealso">

### Closely related

- [Barrier option](/barrier-option/) — parent category
- [Knock-in option](/knock-in-option/) — opposite mechanism; requires crossing
- [Call option](/call-option/) — vanilla right to buy
- [Put option](/put-option/) — vanilla right to sell
- [Exotic option](/binary-option/) — non-standard structure

### Pricing and valuation

- [Monte Carlo options pricing](/monte-carlo-options-pricing/) — simulation method
- [Binomial option pricing](/binomial-option-pricing/) — tree method
- [Black-Scholes model](/black-scholes-model/) — extended for barriers
- [Implied volatility](/implied-volatility/) — affects barrier-crossing risk

### Related concepts

- [Barrier](/barrier-option) — termination level
- [Path-dependent option](/asian-option/) — full history matters
- [Option premium](/option-premium/) — very low for knock-outs
- [Strike price](/strike-price/) — independent of barrier

### Deeper context

- [Option](/option/) — the family of derivatives
- [Hedging](/hedge-fund/) — cheap bets with capped risk
- [Speculation](/stock-market) — leveraged bets with barriers
- [Risk management](/hedge-fund/) — barrier risk control

</div>

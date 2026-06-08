---
title: "Option Time Decay by Days to Expiration: The Theta Curve"
description: "How option time decay accelerates as expiration nears, with decay rates for 90-, 30-, and 7-day contracts and the non-linear theta curve explained."
keywords:
  - option time decay days to expiration
  - theta decay curve
  - time value option
  - days to expiration
  - option pricing
  - time decay rate
  - theta risk
---

*An **option's time decay**—measured by **theta**—is the daily erosion of the option's value due to the shrinking window until expiration, and this decay accelerates non-linearly as the expiration date approaches, with 7-day options losing value far faster per day than 90-day contracts.*

This is why short-term options can evaporate even if the underlying asset doesn't move. An option with 90 days left might lose $0.05 per day; at 7 days, that same option might shed $0.15 per day, even on a calm market. The closer to expiration, the sharper the curve. Understanding this acceleration is crucial for anyone selling premium (collecting theta decay) or holding long options (fighting it).

## The mechanics of theta decay

Every option has two value components: **intrinsic value** (how far in-the-money it is) and **time value** (what traders will pay for the possibility of further moves before expiration). Time value is pure theta exposure.

As days tick away, that time value shrinks. A call option with 90 days to expiration might be worth $2.50; 89 days later, it's worth $2.45 (if the underlying asset price and volatility stay constant). That $0.05 loss is one day's theta.

But the decay isn't linear. The rate of decay *accelerates*—the option loses value faster and faster as expiration looms. This is because options traders pay less for optionality the less time there is for prices to move dramatically. With 90 days, lots can happen; with 7 days, less likely.

## The theta curve: days versus decay rate

Consider a hypothetical call option on a stock trading near the strike price (at-the-money, or ATM). Here's roughly how daily theta might evolve across different days to expiration:

| Days to Expiration | Daily Theta Decay | Cumulative Loss (5 days) |
|---|---|---|
| 90 days | ~$0.04–0.06 | ~$0.22–0.30 |
| 60 days | ~$0.06–0.08 | ~$0.30–0.40 |
| 30 days | ~$0.10–0.15 | ~$0.50–0.75 |
| 14 days | ~$0.18–0.25 | ~$0.90–1.25 |
| 7 days | ~$0.25–0.40 | ~$1.25–2.00 |
| 1 day | ~$0.40–2.00 | Variable, depends on strike |

The table shows the acceleration: going from 90 days to 60 days nearly doubles daily decay; 60 to 30 nearly doubles it again. The last week is a vertical cliff.

## Why decay accelerates

The mathematical reason lies in option pricing models like [Black-Scholes](/black-scholes-model/). An option's time value depends on two factors:

1. **The time window available for a move.** With 90 days, the stock could swing 20%. With 7 days, it's unlikely to move that much. Traders value that optionality, and it shrinks as time shrinks.

2. **Volatility and probability density.** The further from expiration, the broader the range of possible outcomes. The closer to expiration, outcomes collapse toward a binary: in-the-money or out-of-the-money. Once a path is clear (e.g., the option is deep out-of-the-money), traders know it's worthless. That certainty erodes remaining time value fast.

In technical terms, theta is the negative of the option's time-decay derivative. As time runs out, the second derivative (the acceleration of decay) becomes more negative—meaning the loss per day increases faster and faster.

## Factors that amplify theta decay

**Implied volatility (IV):** High volatility means more time value to begin with. A high-IV option has more to lose per day. But remember: theta decay is about *time*, not volatility. Low-volatility environments can actually feature *higher* theta decay rates per day because the time-value cliff is steeper.

**Moneyness (how far in/out of the money):** At-the-money options have the most time value, so they experience the steepest theta decay. Deep out-of-the-money options lose value more gradually early on, then cliff near expiration (because they're nearly worthless either way). In-the-money options decay more slowly, because intrinsic value masks time decay.

**Interest rates and [dividends](/dividend/):** Minor contributors, but real. Rising rates increase call values slightly (opportunity cost of capital), which flattens theta. Upcoming [dividend distributions](/dividend-distribution/) reduce the value available to call holders, steepening their theta.

## Practical implications

**For long-option holders:** You're fighting theta every day. The closer to expiration, the faster you're losing money to time decay alone, even if you're right about direction. This is why traders often "roll" positions forward—sell the near-term, buy the further-out—to avoid the acceleration cliff.

**For short-option sellers:** You profit from theta decay. A trader who sells a 7-day call collects decay much faster than one who sells a 90-day call on the same strike. The risk is volatility spikes and directional moves, but the daily theta wind is at your back more aggressively.

**For hedging:** Protective puts (insurance) get expensive near expiration because the time value has eroded. It's cheaper to buy a 90-day put and hold it than to wait and buy a 7-day put; the acceleration means you'd pay far more per day in the final week.

## Theta decay across option types

**Call and put options** have similar theta structures, though the magnitude varies by [interest rates](/interest-rate/) and dividends. Calls on dividend-paying stocks experience slower theta decay (dividends reduce their value), while puts experience faster decay.

**Out-of-the-money options** start with slow decay, then accelerate sharply in the final days. An OTM call that's been losing $0.01 per day for weeks might suddenly lose $0.10 in the last three days.

**In-the-money options** decay more slowly because intrinsic value cushions them; the time-value component is smaller to begin with.

## See also

<div class="wiki-seealso">

### Closely related

- [Time value](/time-value/) — the non-intrinsic component of an option's price, subject to theta decay
- [Theta](/theta/) — the Greeks, measuring daily time decay across a portfolio
- [Intrinsic value](/intrinsic-value/) — the in-the-money portion of an option that is not subject to time decay
- [Implied volatility](/implied-volatility/) — the market's estimate of future volatility, which affects time-value magnitude
- [Protective put](/protective-put/) — insurance strategy where theta decay works against the buyer

### Wider context

- [Option](/option/) — foundational primer on calls and puts
- [Black-Scholes model](/black-scholes-model/) — the mathematical framework underlying theta calculation
- [Delta](/delta/) — directional sensitivity, which interacts with theta in a trader's overall [Greeks](/delta/) exposure
- [Derivatives hedging](/derivatives-hedging/) — using options to manage tail risk despite theta drag

</div>

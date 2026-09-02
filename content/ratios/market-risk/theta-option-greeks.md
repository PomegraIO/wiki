---
title: "Theta (Option Greeks)"
description: "Time decay of an option's premium as it approaches expiration; the daily loss an option holder faces simply from the passage of time."
keywords:
  - theta decay
  - option greeks
  - time value
  - option pricing
  - expiration risk
---

*[**Theta**](/wiki/time-decay-theta/) is the rate at which an [option](/wiki/option/) loses value due to the passage of time, all else equal. It measures how much premium evaporates each day as the contract ticks closer to expiration.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Symbol** | θ (theta) |
| **Unit** | Premium change per day (dollars per day) |
| **Sign** | Negative for long options (holder loses), positive for short options (seller gains) |
| **Magnitude** | Accelerates near expiration |
| **Peak decay** | Highest in the last 30 days to expiration |
| **At-the-money** | Theta is highest for ATM options |
| **Deep OTM/ITM** | Theta is lower (less time value) |

</aside>

## Why options decay in value

An [option](/wiki/option/) is worth two things: intrinsic value (how much the option is in-the-money) and time value (the chance the option will move further in-the-money before expiration).

A [call option](/wiki/call-option/) to buy Apple at $150 when Apple trades at $155 has $5 of intrinsic value. But if that call has three months to expiration, the holder paid perhaps $6 because there is a chance Apple rallies to $160, $170, or higher—the option is worth the extra dollar of time value.

As time passes and nothing else changes, that time value shrinks. With one month left, the call might be worth $5.50. With one week left, $5.10. On the expiration day, if Apple is still at $155, the call is worth exactly $5—all time value has evaporated.

Theta quantifies this daily bleed. If an option's theta is –$0.05 per day, the option loses $0.05 every single day due to passage of time alone, regardless of stock price movement.

## How theta accelerates near expiration

Theta is not constant. An option that is far from expiration (say, nine months away) decays slowly. Each day, only a tiny fraction of the time premium vanishes because there is still a vast horizon for the stock to move.

But as expiration approaches, theta accelerates. In the final 30 days, theta is often 2–3 times larger than it was six months prior. In the final week, it can be extreme. On expiration day itself, an out-of-the-money option's theta approaches negative infinity: the option is about to become worthless, and every second counts.

This is why options traders watch the calendar. An out-of-the-money [put](/wiki/put-option/) bought three months ago might have seemed like a cheap insurance policy with high theta (slow decay). But the same put, three weeks before expiration, has extremely high negative theta and is losing value by the hour.

## Theta depends on moneyness

Theta is strongest (in absolute value) for [at-the-money](/wiki/at-the-money/) options. An ATM call is almost all time value; as time passes, that time value erodes fast.

By contrast, a [deep-in-the-money](/wiki/in-the-money/) call or a [deep-out-of-the-money](/wiki/out-of-the-money/) call has little time value to begin with, so theta decay is slower. A deep-ITM call behaves almost like stock; its value is almost entirely intrinsic.

This creates a natural hedge: buying a far-OTM put for disaster insurance has low theta decay (not much time value to lose), while buying an ATM put is more expensive and decays faster.

## The option buyer's enemy, the seller's friend

From the buyer's perspective, theta is the enemy. Every day that passes, the position loses value to decay alone. A buyer of out-of-the-money options (betting on a move) is fighting a constant drag from theta.

From the seller's perspective (the writer of the option), theta is the friend. A short [call](/wiki/call-option/) or short [put](/wiki/put-option/) generates a daily profit from time decay, independent of stock price movement. Sellers of [covered calls](/wiki/covered-call/) and cash-secured [puts](/wiki/cash-secured-put/) can be net profiting from theta while the stock price barely moves.

This is why option selling strategies often work best in calm, range-bound markets: theta compounds daily, but the stock is not moving enough to trigger large losses on the short side.

## Relationship to other Greeks

Theta does not work in isolation. An option's value is also driven by changes in the underlying stock price ([delta](/wiki/delta-option-greeks/)), changes in volatility ([vega](/wiki/vega-option-greeks/)), and changes in interest rates ([rho](/wiki/rho-option-greeks/)).

In real portfolios, theta decay may be offset or amplified by vega exposure. If the stock is not moving but implied volatility (IV) is rising, the option's vega component is making money, offsetting theta losses. A trader long premium (bought calls or puts) benefits from vega but suffers from theta; the net P&L depends on how volatility moves relative to theta decay.

This is why professional options traders manage Greeks in combination. They might sell an option (to capture theta) while simultaneously buying another option to hedge delta or vega risk.

## Theta and volatility

Implied volatility and theta are linked. In high-volatility environments, options have more time value (more chance of a large move), and theta is larger in absolute dollars. When volatility collapses, time value shrinks, and theta is smaller.

A trader holding an option position in a low-volatility market suffers less from daily theta decay than the same position held in a high-volatility market. This is why volatility crush can be devastating for long-premium strategies: not only does the stock fail to move, but implied volatility collapses, eroding time value and accelerating theta decay.

## Practical strategies exploiting theta

The calendar spread or time spread ([calendar spread](/wiki/calendar-spread/)) is a classic theta strategy: sell a near-term option (high theta) and buy a far-term option (low theta) on the same underlying. The position profits from the high theta decay of the short leg, while the long leg limits risk if the stock moves sharply.

[Iron condors](/wiki/iron-condor/) and [strangles](/wiki/strangle/) sold at wide widths benefit from theta while being hedged against large price moves. The seller collects premium and profits if the stock ends up between the strike prices at expiration—a steady, theta-driven profit center.

Long-dated, out-of-the-money hedges (e.g., portfolio insurance puts) are accepted as "negative theta" trades—insurance policies always cost money to hold, and theta is that cost.

## Measuring and monitoring theta

Most options platforms display theta as the estimated daily change in option price due to passage of time. A call option might show θ = –$0.05, meaning the option will lose $0.05 tomorrow if everything else (stock price, volatility, interest rate) stays constant.

More precisely, theta is the **derivative** of option value with respect to time—the instantaneous rate of change. It is not perfectly linear; it accelerates as expiration nears.

<div class="wiki-seealso">

### Closely related
- [Time Decay Theta](/wiki/time-decay-theta/) — Detailed treatment of theta concepts.
- [Delta](/wiki/delta-option-greeks/) — Rate of change of option value with stock price.
- [Vega](/wiki/vega-option-greeks/) — Sensitivity to changes in implied volatility.
- [Gamma](/wiki/gamma-option-greeks/) — Rate of change of delta with stock price.
- [Rho](/wiki/rho-option-greeks/) — Sensitivity to interest-rate changes.

### Wider context
- [Option Greeks](/wiki/options-greeks/) — All five Greeks and their interplay.
- [Option Pricing](/wiki/black-scholes-model/) — Framework for valuing options.
- [Calendar Spread](/wiki/calendar-spread/) — Strategy exploiting theta on different expirations.
- [Iron Condor](/wiki/iron-condor/) — Sold spread that profits from theta and low volatility.
- [Covered Call](/wiki/covered-call/) — Selling calls on owned stock to capture theta.

</div>
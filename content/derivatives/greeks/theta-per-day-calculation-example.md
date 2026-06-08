---
title: "Theta Per Day: Calculation and Example"
description: "Theta per day calculation shows the daily dollar cost of holding an option position due to time decay. Learn to interpret and calculate daily theta."
keywords:
  - theta per day calculation options example
  - daily theta value options
  - time decay dollar amount daily
  - theta calculation single leg spread
  - interpreting theta brokerage platform
image: /svg/derivatives.svg
---

*The **theta per day calculation** translates a Greek into a real dollar amount: how much an option position loses (or gains) per day purely from the passage of time, holding the underlying price and volatility constant. Most brokers display annualized theta; dividing by 365 gives a daily figure, though the nuance of how that daily erosion compounds matters when you stack multiple options.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Theta per day — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The daily cost of time decay on an options position.</div>

|   |   |
|---|---|
| **What it measures** | Dollar loss per day from [time decay](/time-decay-theta/) alone |
| **Formula (simple)** | Annualized theta ÷ 365 |
| **Sign convention** | Positive theta = you gain; negative theta = you lose |
| **Who gains from theta** | [Option sellers](/put-option/), short-duration strategies, [covered calls](/covered-call/) |
| **Who loses from theta** | [Option buyers](/call-option/), especially at-the-money options |
| **Typical range** | Pennies to tens of dollars per day per contract, depending on strike, expiry, and [implied volatility](/implied-volatility/) |
| **Compound effect** | Daily erosion is non-linear; theta accelerates as expiration nears |

</aside>

## Why theta per day matters

When you hold an option, three things can change its value: the underlying price moves (handled by [delta](/delta/)), [volatility](/historical-volatility/) shifts (handled by [vega](/vega/)), and time passes (handled by [theta](/theta/)). Theta is the *silent cost* of holding the position—it costs you money whether the underlying moves or not, simply because you own a decaying asset.

Most brokerage platforms display theta as an annualized figure (e.g., –0.05 for a long call). That's the annual rate of decay. But you don't hold the option for a year; you hold it for hours, days, or weeks. To understand your daily cost, you need to scale it down to a single day.

This is especially critical if you trade short-dated options (weekly expirations) or if you monitor your account daily. Knowing your daily theta exposure tells you how much drift from price and volatility you need to overcome just to break even.

## The basic formula

The simplest theta-per-day calculation:

**Daily theta = Annualized theta ÷ 365**

If a call option has a theta of –0.20 (per share), that's –0.20 ÷ 365 = **–0.00055 per share per day**.

For a full options contract (covering 100 shares), multiply by 100:

**Daily theta (contract) = (–0.00055) × 100 = –$0.055 per day**

So you lose roughly 5.5 cents per day, all else equal, just from time decay.

## Single-leg example: long call

Suppose you buy one call option:
- Underlying stock: trading at $100
- Strike: $100 (at-the-money)
- Days to expiration: 30 days
- [Implied volatility](/implied-volatility/): 30%
- Current theta on your platform: –0.08 per share

**Calculation:**
- Annual theta decay: –0.08 per share
- Daily theta: –0.08 ÷ 365 = –0.000219 per share
- Per contract (100 shares): –0.000219 × 100 = **–$0.0219, or roughly –2.2 cents per day**

**Interpretation:** Holding this call costs you about $2.20 per day in time decay alone. If the stock stays at $100 and volatility doesn't change, your call loses $2.20 in value each day until expiration (when it expires worthless, assuming it's still at-the-money).

To break even, you'd need the stock to move up slightly (gaining [delta](/delta/)) or volatility to rise (gaining [vega](/vega/)) to offset the daily theta drain.

## Multi-leg example: call spread

Theta becomes more nuanced in spreads because you own theta in one leg and are short theta in another.

Suppose you buy a $100 call and sell a $105 call (a bull call spread):
- Long $100 call: theta = –0.10 per share
- Short $105 call: theta = +0.06 per share
- Net theta: –0.04 per share

**Calculation:**
- Net annual theta: –0.04 per share
- Daily theta: –0.04 ÷ 365 = –0.000110 per share
- Per contract: –0.000110 × 100 = **–$0.011 per day, or roughly –1.1 cents per day**

**Interpretation:** Even though you're long an option (which normally decays), the short leg is paying you theta. The spread nets out to a small daily cost compared to the long call alone. This is why credit spreads ([covered calls](/covered-call/), short puts) can show positive theta—the short leg is so far out-of-the-money that its theta decay is rapid, and you pocket that decay as profit.

## The catch: non-linearity of decay

The formula theta ÷ 365 assumes decay is uniform across the day. In reality, theta *accelerates* as expiration approaches. An option with 30 days to go loses theta much more slowly than one with 5 days to go.

The Greeks are snapshots, not guarantees. The theta figure you see in your platform is valid *right now* but will change as time passes. A position with –$0.02 daily theta today will have a larger daily theta loss by tomorrow.

This is why traders watching short-dated options (weekly expiries, or positions with just days to expiration) need to monitor their theta position closely. A $0.02/day cost might seem trivial, but if you hold the option until it has just 2 days left, theta accelerates and you could lose $0.10 per day or more.

## Theta by position type

**Long calls and long puts:** Always negative theta. You pay for the privilege of holding leverage. The longer you hold, the more time decay costs you.

**Short calls and short puts:** Always positive theta. You collect money from decay. Sellers of options profit from theta.

**At-the-money options:** Theta is steepest here. An ATM option decays fastest because all its value is time value; there's no intrinsic value buffer.

**In-the-money and out-of-the-money options:** OTM options have the most time value and decay fastest in absolute terms, but ITM options can still have material theta costs if they're close to the money.

**Near expiration (days left = single digits):** Theta explodes. An option with 5 days left and $0.50 in value might lose $0.05+ per day. The daily theta figure becomes mission-critical for traders.

## How brokers display theta

Most platforms show theta per share. To convert to a dollar figure:
1. Multiply by 100 (one options contract = 100 shares)
2. Divide by 365 (annualized to daily)

Some platforms allow you to view theta as an aggregate across your entire position (all legs, all contracts). This is the most useful view: it tells you, in dollars per day, what your position will cost you in pure time decay.

If your multi-leg position shows a daily theta of +$1.20, you're collecting $1.20 per day from the passage of time alone—a modest but steady income stream, as long as the underlying stays within your target range.

## Practical use: break-even math

Knowing your daily theta helps you set realistic stop-losses and profit targets.

If you buy a call with daily theta of –$0.05 for a premium of $1.50, you need the underlying to move enough (in your favor) to offset both the purchase price and the time decay over however many days you plan to hold it.

If you hold for 10 days, time decay alone will cost you $0.50. So if the underlying moves $0.25 in your favor, you've only netted $0.25 in profit—but you've actually paid $0.50 in theta, leaving you down $0.25 before commissions and bid-ask slippage.

This is why many option traders focus on short-duration, high-probability moves: the less time you're exposed to theta decay, the more of your profit comes from price movement rather than volatility crush.

## See also

<div class="wiki-seealso">

### Closely related

- [Theta](/theta/) — the full Greek, including the nuances of measurement
- [Time decay](/time-decay-theta/) — the underlying mechanism of theta decay
- [Implied volatility](/implied-volatility/) — what theta assumes constant; changes ripple through all Greeks
- [Delta](/delta/) — directional sensitivity; your hedge against theta loss
- [Vega](/vega/) — sensitivity to volatility; can offset or amplify theta
- [Call option](/call-option/) — typical long-theta position (loses to decay)
- [Put option](/put-option/) — typical long-theta position (loses to decay)

### Wider context

- [Options](/option/) — the asset class where theta is primary
- [Covered call](/covered-call/) — a positive-theta trade that collects from decay
- [Option premium](/option-premium/) — what you pay or collect upfront before theta drain
- [Expiration date](/expiration-date/) — the point at which theta goes to zero

</div>
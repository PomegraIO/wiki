---
title: "Average Strike Option"
description: "An average strike option sets its exercise price as the arithmetic mean of the underlying asset's price over a sampling window, reducing pricing uncertainty."
keywords:
  - average strike option
  - exotic option
  - path-dependent option
  - exercise price
  - arithmetic average
  - option pricing
  - derivatives
---

*An **average strike option** fixes the strike price not at inception, but as the arithmetic mean of the underlying's price over a defined observation period. This structure shifts timing risk from the strike level to the spot price path, making it cheaper and more predictable for buyers hedging volatile exposures.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Average Strike Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A path-dependent option whose payoff depends on where the stock traded, not where it trades on expiry.</div>

|   |   |
|---|---|
| **Strike price** | Arithmetic mean of observed prices over the sampling window |
| **Holder's benefit** | Lower premium than vanilla options; reduced vulnerability to single-point surprises |
| **Settlement** | Usually European-style (exercisable only at maturity) |
| **Pricing driver** | Volatility of the underlying *and* the correlation structure of price paths |
| **Common use** | Equity index hedging, commodity forward strategies, long-dated employee equity grants |

</aside>

## How the strike price emerges from averaging

A vanilla [call option](/option/) fixes the strike at a known level on day one. An average strike call, by contrast, has its strike determined by averaging the underlying price at each observation date through the option's life.

If you buy an average strike call with a 60-day observation window:
- Days 1–60: the system records the closing price each day (or weekly; the specification varies).
- At expiry, the strike is set as the average of all recorded prices.
- Payoff: max(0, spot at expiry − average strike).

The buyer pays a lower premium than for a comparable vanilla call, because the strike is set to a smoothed value, not a fixed level. The trade-off is that the payoff depends on the full path the stock took, not just where it lands.

## Average strike versus average price (Asian options)

The terminology can confuse traders new to exotics. An **average price option** (also called an Asian option) fixes the strike at inception and sets the *payoff* using the average price: max(0, average spot − strike).

An average strike option does the opposite: it keeps the payoff deterministic (spot − strike), but lets the *strike itself* be the average.

In a call:
- **Average price call:** max(0, average spot − fixed strike)
- **Average strike call:** max(0, spot at expiry − average strike)

Both are cheaper than vanilla options, but they protect against different risks. If you expect the stock to drift higher steadily, an average price option cushions your cost basis. If you're uncertain about the opening level but confident about the trend, an average strike call lets you lock in downside protection at a price that reflects the whole period, not a single opening.

## Why buyers choose average strike options

### Lower premiums

Because the strike is anchored to a realized average, not a fixed point, the [option premium](/option-premium/) is almost always lower than a vanilla call or put at an equivalent forward level. Traders paying that premium get diversification: the strike can't spike against you after you buy.

### Path smoothing in volatile markets

In sectors prone to gap openings (earnings, Fed announcements, geopolitical shocks), an average strike option is robust. A single bad open doesn't dictate the strike; the full 60 or 90 days do. For a company hedging a known future equity issuance, this matters: you care about the price trend, not the luck of a single trading session.

### Predictability for long-dated structures

Employee stock purchase plans, deferred equity compensation, and long-term forward commitments often use average strike mechanics. Because the strike converges to a realized mean, volatility expectations matter less, making the product easier to price and model over years.

## Valuation and pricing drivers

An average strike option's price depends not just on spot, volatility, and time to expiry (as with vanilla options), but also on **the correlation of price movements over the observation period** and the shape of the volatility surface.

If the stock bounces daily but ends where it started, the strike averages to that starting level—and the average strike call pays off similarly to a vanilla call. But if the stock climbs steadily, the strike ratchets up, and the call finishes out-of-the-money even though spot rallied.

Practitioners use [Monte Carlo simulation](/sensitivity-analysis-valuation/) to price these, accounting for:
- The number and spacing of observation dates.
- Whether observations reset (reset options) or accumulate.
- Dividend and corporate-action adjustments.

## Observation frequency and settlement details

The contract specifies when prices are sampled:
- **Daily:** closes at market.
- **Weekly:** Friday close.
- **Monthly:** the last business day.
- **Discrete vs. continuous:** fewer observation points reduce computational cost but increase model risk if prices gap sharply between sampling dates.

Settlement is typically [European-style](/option/) (exercisable only at expiry), which simplifies valuation. American-style average strike options are rarer and harder to price, since the holder must decide whether to exercise before knowing the full average.

## Real-world example

A fund manager holds 10 million shares of a mid-cap stock over 90 days. Worried about downside but uncertain when the bottom might arrive, she buys 90-day average strike puts with monthly observations (Jan 31, Feb 28, Mar 31 closes).

The put's strike becomes the average of those three closing prices. If the stock trades $45, $42, $48 on those dates, the strike is $45. On April 1, if the stock has fallen to $40, the put pays max(0, 45 − 40) = $5 per share. The [call premium](/call-option/) was 15 cents—much lower than a vanilla $45 put would have cost.

If instead the stock climbed to $50, the put expires worthless, and she kept the $0.15 savings. This makes sense: she was hedging not a worst-case scenario, but a three-month trend.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational contract and its mechanics
- [Option premium](/option-premium/) — what buyers pay for optionality
- [Call option](/call-option/) — the mechanics of upside bets
- [Put option](/put-option/) — downside protection instruments
- [Path-dependent derivatives](/derivatives-hedging/) — options whose payoff depends on the price journey, not just the endpoint
- [Monte Carlo simulation](/sensitivity-analysis-valuation/) — the numerical method used to price average strike options

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — why corporations and investors use options
- [Volatility smile](/volatility-smile/) — how market prices vary across strike and expiration
- [Option pricing](/option/) — theoretical foundations and models
- [European Central Bank](/european-central-bank/) — central banks' derivatives regulation

</div>

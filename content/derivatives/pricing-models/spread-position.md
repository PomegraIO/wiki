---
title: "Spread Position"
description: "A paired long-short options trade that reduces net premium paid and limits both profit and loss."
keywords:
  - spread position
  - options strategy
  - debit spread
  - credit spread
---

*A **spread position** is an options strategy that combines two or more options on the same underlying asset to reduce net premium paid (debit spread) or collect premium (credit spread), trading unlimited profit for defined, reduced risk.*

The simplest spread is a **call spread**: buy a lower-strike call and sell a higher-strike call. Both expire on the same date. If the underlying rises sharply, the long call profits but the short call caps the gain. If the underlying falls, both calls expire worthless and the trader keeps the net credit received. The maximum loss is the debit paid (long premium minus short premium received), and the maximum gain is capped at the strike width minus the net debit. This is the essence of a spread: it trades unlimited payoff for defined, lower-risk payoff.

<aside class="wiki-infobox">

| Type | Payoff | Use case |
|---|---|---|
| **Bull call spread** | Debit; profit if stock rises moderately | Bullish, defined risk |
| **Bear call spread** | Credit; profit if stock falls/stays flat | Neutral, defined risk |
| **Bull put spread** | Credit; profit if stock stays above strike | Bullish income strategy |
| **Bear put spread** | Debit; profit if stock falls moderately | Bearish, limited risk |
| **Butterfly** | Debit; peak profit at middle strike | Neutral bet on [volatility](/wiki/volatility-index-futures/) |
| **Calendar spread** | Debit; profit from time decay asymmetry | [Theta](/wiki/theta-option-greeks/) harvesting |

</aside>

## Risk and reward tradeoffs

A **bull call spread** costs $2 (buy $100 call, sell $110 call, net debit $2). The underlying rises to $115. The long call is worth $15, the short is worth $5, so the spread is worth $10. Profit is $10 – $2 = $8. If the underlying falls to $90, both expire worthless, and the loss is the $2 premium. The trader cannot lose more than $2, but cannot gain more than $8. This defined risk is the entire point: a straightforward long $100 call (no spread) risks $3 or $4 of premium but has unlimited upside to $15, $20, $50. The spread sacrifices unlimited upside for safety.

For **credit spreads** (e.g., a bear call spread), the trader *sells* the higher premium and *buys* the lower premium, receiving a net credit. If the stock falls, the trader keeps the credit. If the stock rises above the long call's strike, the spread reaches max loss. Credit spreads are attractive to investors seeking monthly or quarterly income from options; the [theta decay](/wiki/time-decay-theta/) (premium erosion as expiration nears) works in their favor on both legs.

## Variance and implied volatility sensitivity

Spread positions have more nuanced [Greeks](/wiki/options-greeks/) than outright calls or puts:

- **Delta**: The spread's delta is the difference between the two legs' deltas. A bull call spread has net positive delta (bullish), scaling with the strike separation and time to expiration.
- **Vega**: Short options reduce the spread's [vega](/wiki/vega-option-greeks/). A bull call spread—long one call, short another—has *lower* vega than a pure long call. If [implied volatility](/wiki/implied-volatility/) soars, the long call gains less than it would without the short. This vega drag is why spreads underperform in volatility surges, but outperform when volatility subsides.
- **Theta**: Calendar spreads (long back-month, short front-month) harvest [theta](/wiki/theta-option-greeks/), as the near-term option decays faster. The spread profits as expiration approaches (if the underlying stays flat).

## Strategic uses

**Income traders** use credit spreads to monetize covered positions. A trader holding 100 shares of Apple might sell a monthly 180 call (collecting $3) and buy a 185 call (paying $1), netting $2 per share ($200). If Apple closes below 180, the trader keeps the $200 and still owns the stock, continuing to sell spreads indefinitely. This is similar to a [covered call](/wiki/covered-call/), but with downside [defined](/wiki/spread-position/).

**Directional traders** use spreads to reduce premium when they have a mild view. Bullish but uncertain: buy a 3-month bull call spread instead of an outright call. Less upside, but much lower cost.

**Volatility traders** use diagonal spreads (different expirations and strikes) to isolate [volatility](/wiki/volatility-smile/) exposures. A short calendar spread—short front month, long back month—profits if short-term [implied volatility](/wiki/implied-volatility/) rises relative to long-term (a [volatility smile](/wiki/volatility-smile/)) or if the underlying stays flat (theta works).

## Comparison to collars and straddles

A **collar** (a put spread paired with a call spread) is a defined-risk hedge: sell a call, buy a put lower down, hedge an underlying position. A **straddle** (long call + long put, same strike) is an unhedged bet on [volatility](/wiki/volatility-index-futures/); both legs are long, with unlimited risk but also unlimited profit potential. A spread differs: it *always* involves at least one short leg, capping one side of the profit/loss.

## Execution and tax considerations

Spreads require careful execution. A retail investor on a standard broker platform may face **assignment risk**: if the short call is exercised, the broker may auto-sell the underlying or force a short stock position rather than offset with the long call. Most brokers' platforms handle spreads as single orders ("close the spread" on one click), eliminating this friction.

For **tax purposes**, spreads are treated as two separate options. A [Section 1256 contract](/wiki/mark-to-market/) (equity option spreads on U.S. indices) receives 60/40 long-term/short-term [capital gains](/wiki/capital-gains-tax/) treatment at year-end. A trader closing a spread at a loss can claim the loss against other [Section 1256](/wiki/mark-to-market/) gains. Wash-sale rules apply: if a spread is closed at a loss, buying substantially identical options within 30 days will disallow the loss and add it to the new position's cost basis.

<div class="wiki-seealso">

### Closely related
- [Call Option](/wiki/call-option/) — foundational building block
- [Put Option](/wiki/put-option/) — reciprocal leg in spreads
- [Bull Call Spread](/wiki/bull-call-spread/) — classic directional strategy
- [Collar](/wiki/collar/) — asymmetric protection strategy

### Wider context
- [Options Greeks](/wiki/options-greeks/) — sensitivity measures
- [Implied Volatility](/wiki/implied-volatility/) — pricing and vega driver
- [Time Decay](/wiki/time-decay-theta/) — theta and calendar effects
- [Box Spread](/wiki/box-spread/) — arbitrage-less spread variant

</div>

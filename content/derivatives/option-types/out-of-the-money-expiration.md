---
title: "Out-of-the-Money Expiration"
description: "Option expiring worthless because underlying price doesn't exceed strike price."
keywords:
  - out of the money
  - option expiration
  - worthless option
  - strike price
---

*An **out-of-the-money (OTM) expiration** occurs when an [option](/wiki/option/) expires with zero intrinsic value because the underlying asset's price has not moved beyond the [strike price](/wiki/strike-price/) in the favorable direction. A call option expires OTM if the underlying price is below the strike; a put option expires OTM if the underlying is above the strike. The option holder loses the entire premium paid.*

<aside class="wiki-infobox">

| Scenario | Call | Put |
|---|---|---|
| **OTM at expiration** | Underlying < Strike | Underlying > Strike |
| **Result** | Expires worthless | Expires worthless |
| **Holder loss** | Full premium paid | Full premium paid |
| **Writer profit** | Full premium collected | Full premium collected |
| **Intrinsic value** | $0 | $0 |

</aside>

## Mechanics of OTM expiration

An [option](/wiki/option/) has [intrinsic value](/wiki/intrinsic-value/) only if it's "in the money" (ITM) at expiration:

- A **call option** is ITM if underlying price > strike price. Example: Call struck at $50, underlying at $55 at expiration. Intrinsic value = $5.
- A **put option** is ITM if underlying price < strike price. Example: Put struck at $50, underlying at $45 at expiration. Intrinsic value = $5.

If the underlying price does not exceed the strike (for a call) or fall below the strike (for a put), the option expires [out-of-the-money](/wiki/out-of-the-money/) with zero intrinsic value.

**Example:** A trader buys a $100 call option on stock XYZ, paying $3 premium. At expiration, XYZ is trading at $98. The call is OTM (the underlying never reached the strike). The option expires worthless. The trader's loss is the $3 premium paid; the seller keeps the $3.

## Time decay and OTM options

Out-of-the-money options are sensitive to [time decay (theta)](/wiki/time-decay-theta/). An OTM option has no intrinsic value, so its entire value is time value—the probability that the underlying will move far enough to make the option ITM before expiration.

As expiration approaches, an OTM option's time value decays toward zero. A call option that is $5 OTM with 30 days to expiration might have $0.50 of time value (representing the probability the underlying gains $5+); with 1 day to expiration, that time value might be $0.01. At exactly expiration, time value = zero.

Traders who sell OTM options profit from time decay: they collect the premium upfront and benefit as time value erodes toward expiration.

## Implied volatility and OTM options

[Implied volatility](/wiki/implied-volatility/) (IV) dramatically affects OTM option prices. High IV means markets expect large moves, so even OTM options have valuable time value (high probability of moving ITM). Low IV means markets expect small moves, so OTM options are cheap (low probability of moving ITM).

When IV spikes (e.g., after an earnings announcement), OTM options become more expensive. When IV collapses after the event, OTM options lose value rapidly, even if the underlying price hasn't moved. This [volatility crush](/wiki/volatility-smile/) affects sellers of OTM options (who want low IV at exit) and buyers (who want low IV at entry).

## Strategic uses of OTM options

**Selling OTM options (covered calls, cash-secured puts):** A trader might sell OTM call options above current price, collecting premium and keeping the stock if it's called away. Or sell OTM put options below current price, collecting premium and willing to own the stock if assigned. Both strategies profit from OTM expiration.

**Buying OTM options (cheap leverage):** A speculator buys far-OTM call options cheaply, risking the full premium but gaining leveraged exposure to the underlying. If the underlying doesn't reach the strike, the option expires worthless and the loss is 100%. But if a large move occurs, the percentage gains are magnified.

**Protective puts (insurance):** A stock owner buys OTM put options below the stock price, paying premium for downside protection. If the stock stays above the strike, the put expires OTM and the premium is the cost of insurance (lost). If the stock crashes, the put's value offsets losses.

## Probability of expiration OTM

The probability that an option expires OTM is related to [delta](/wiki/delta-option-greeks/). A call option with a delta of 0.30 has approximately a 30% probability of expiring ITM and a 70% probability of expiring OTM.

Deep OTM options (way out of the money) have very low delta and high probability of expiring OTM. Far-OTM options are cheap because the underlying must make a dramatic move for the option to gain value.

## Comparison: OTM vs. ITM expiration

- **ITM expiration:** Option has intrinsic value; holder exercises or sells, capturing value. Writer must deliver shares (calls) or cash (puts).
- **OTM expiration:** Option expires worthless; holder loses premium; writer keeps full premium as profit.
- **ATM expiration:** Option expires right at the strike; intrinsic value is zero, but close-to-maturity at-the-money options may have bid-ask prices reflecting illiquidity.

## Tax treatment of OTM expiration

When an option expires worthless, the loss is typically treated as a [capital loss](/wiki/capital-gains-tax/). For [covered call](/wiki/covered-call/) writers, the expiration of an OTM call doesn't trigger [short-term capital gains](/wiki/short-term-capital-gain-tax/) on the underlying—the stock is still held. The premium received reduces the cost basis of the stock.

For traders, the situation is more complex; losses can potentially be treated as ordinary losses if the trader qualifies as a professional [Section 1256](/wiki/section-13g/) or [mark-to-market](/wiki/mark-to-market/) trader, but most retail traders report capital losses.

## Psychological impact

OTM expiration can be psychologically painful for option buyers. A trader who bought a call option for $500 and watches it expire worthless has a clean, visible loss. Conversely, sellers of OTM options experience the joy of "free money"—they collected the premium upfront and keep it with zero effort. This psychological asymmetry explains why many traders are biased toward selling options (and taking the risk of rare large moves) versus buying (and accepting the frequent total loss on far-OTM positions).

## OTM expiration in real markets

On the third Friday of each month (US equity option expiration), thousands of OTM options expire worthless. The [open interest](/wiki/open-interest/) in OTM strikes reflects speculative bets on large moves; most expire OTM, enriching sellers and frustrating buyers.

This happens across all [derivatives](/wiki/derivatives-exchange-crypto/) markets: equities, [indices](/wiki/index-fund/), [futures](/wiki/futures-contract/), currencies, and commodities. The volume of worthless expirations is enormous, which is why [options exchanges](/wiki/cboe-options-exchange/) and market makers focus on probabilities and manage gamma risk rather than betting on specific prices.

<div class="wiki-seealso">

### Closely related
- [Out of the Money](/wiki/out-of-the-money/) — OTM definition and general concept
- [Strike Price](/wiki/strike-price/) — Determines OTM status
- [Option](/wiki/option/) — Core instrument expiring
- [Time Decay (Theta)](/wiki/time-decay-theta/) — Helps OTM options expire worthless
- [Delta](/wiki/delta-option-greeks/) — Probability of OTM expiration
- [Implied Volatility](/wiki/implied-volatility/) — Affects OTM option value

### Wider context
- [Call Option](/wiki/call-option/) — OTM calls expire worthless
- [Put Option](/wiki/put-option/) — OTM puts expire worthless
- [Covered Call](/wiki/covered-call/) — Strategy selling OTM calls
- [Capital Gains Tax](/wiki/capital-gains-tax/) — Loss treatment on expiration
- [Volatility Smile](/wiki/volatility-smile/) — IV skew in OTM strikes
- [Open Interest](/wiki/open-interest/) — OTM options often have large open interest

</div>

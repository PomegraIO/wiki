---
title: "Cash-or-Nothing Call Option Explained"
description: "A cash-or-nothing call pays a fixed cash amount if the underlying finishes above the strike at expiration, zero otherwise. Payoff differs sharply from vanilla calls."
keywords:
  - cash or nothing call option
  - binary options call
  - digital options call
  - exotic options payoff
  - cash-or-nothing contracts
image: /svg/derivatives.svg
---

*A **cash-or-nothing call** is an [exotic option](/option/) that pays a fixed cash amount if the underlying asset closes above the strike price at expiration—and zero if it closes at or below. Unlike a vanilla [call option](/call-option/), which pays the intrinsic value (spot price minus strike), the cash-or-nothing call's payoff is binary: all-or-nothing, regardless of how far in-the-money the underlying moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cash-or-Nothing Call — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A fixed payout contingent on crossing a single strike threshold.</div>

|   |   |
|---|---|
| **Payoff at expiration** | Rebate amount (fixed) if spot > strike; $0 if spot ≤ strike |
| **Payoff type** | Binary; no [intrinsic value](/intrinsic-value/) scaling |
| **Premium (cost)** | Lower than vanilla call in same [strike](/strike-price/); bet on direction only |
| **Max gain** | Rebate amount (known upfront) |
| **Max loss** | Premium paid |
| **Used for** | Directional bets with capped risk; hedging on budget |
| **Exchange traded** | Rare; mostly OTC or prop trading platforms |

</aside>

## How the Cash-or-Nothing Call Works: The Binary Payoff

A vanilla call's profit scales with how far the underlying rallies past the strike. If you buy a $100 call on Stock X and it closes at $105, you profit $5 per share. If it closes at $110, you profit $10 per share.

A cash-or-nothing call has no scaling. You set a strike and a fixed cash payout (the "rebate"). If the underlying closes above the strike—$100.01 or $150—you receive the full rebate. If it closes at or below the strike, you receive nothing.

**Example Payoff Comparison:**

| Stock Close | Vanilla $100 Call | Cash-or-Nothing $100 Call (Rebate: $500) |
|---|---|---|
| $95 | $0 | $0 |
| $100 | $0 | $0 |
| $105 | $500 gain | $500 gain |
| $110 | $1,000 gain | $500 gain |
| $115 | $1,500 gain | $500 gain |

In the vanilla case, your profit scales. In the cash-or-nothing case, profit caps at the rebate—but you paid less premium to enter the trade, so the [risk-reward ratio](/bid-ask-spread/) tilts differently.

## Premium and Pricing of Cash-or-Nothing Calls

The **premium** (cost) of a cash-or-nothing call is lower than a vanilla call on the same underlying and strike, because the max payoff is capped. A vanilla call on Stock X at a $100 strike has unlimited upside; a cash-or-nothing call with a $500 rebate caps your return at $500 no matter how high the stock runs.

The premium is driven by:
- **Probability of expiring in-the-money** (spot > strike). Higher probability = higher premium.
- **Rebate amount**. Larger rebate = higher premium.
- **Time to expiration**. More time = higher premium (more opportunity to cross the strike).
- **Volatility**. Higher [volatility](/historical-volatility/) = higher premium (wider range of possible outcomes = higher chance of exceeding strike).

Pricing cash-or-nothing calls uses the [Black-Scholes model](/black-scholes-model/) or similar frameworks, but instead of calculating [intrinsic value](/intrinsic-value/), it solves for the probability that the call finishes in-the-money and multiplies by the rebate, then discounts back to present value. Roughly:

**Premium ≈ Rebate × Probability(spot > strike at expiration)**

If the probability is 50% and the rebate is $500, the fair premium is roughly $250 (ignoring [time decay](/time-decay-theta/) and discounting). In practice, the seller adds a spread, and market makers adjust for volatility and edge.

## Cash-or-Nothing Calls vs. Vanilla Calls: When Each Matters

**Vanilla calls** make sense when:
- You want to profit from *how much* the underlying moves, not just *whether* it moves. A 10% rally is 5× better than a 2% rally.
- You are bullish but price-sensitive—you want upside scaling.

**Cash-or-nothing calls** make sense when:
- You want a directional bet (up or down) without caring how far it moves. You just need the underlying to cross the strike.
- You have a tight budget and want to avoid the larger premium of a vanilla call.
- You are timing a catalyst or event and believe there is a binary outcome (deal closes, earnings surprise, rate decision). You don't need upside beyond "win or lose."

Example: Suppose a stock is at $100 and an earnings announcement is next week. You believe earnings will be strong and the stock will pop above $105. A vanilla $105 call might cost $1.00 (premium) and profits $1.00 if the stock hits exactly $105 (then rallies beyond). A cash-or-nothing $105 call might cost $0.50 and pays $2.00 if the stock exceeds $105—matching your two-for-one risk-reward expectation with lower capital at risk.

## Risk Profile and Breakeven

The max loss on a cash-or-nothing call is the premium you paid. If you buy the call for $0.50 and the stock closes below the strike, you lose $0.50.

The max gain is the rebate. If you bought for $0.50 and the rebate is $2.00, your max profit is $1.50 ($2.00 received minus $0.50 paid).

**Breakeven:** The stock price at which your total payout (rebate or zero) equals your premium.

If the rebate is $2.00 and you paid $0.50, you breakeven if you receive at least $0.50 of value. Since the call pays $2.00 if in-the-money (and $0 if out), the breakeven is simply at the strike price (since any spot > strike triggers the full $2.00 rebate, covering your $0.50 cost).

In practice, brokers and dealers price these contracts so the expected value to the buyer is slightly negative (the [bid-ask spread](/bid-ask-spread/) and dealer margin). You are betting on *mispricing* or a specific catalyst moving the underlying past your strike threshold.

## Where Cash-or-Nothing Calls Are Traded

**Exchange-traded** cash-or-nothing calls are rare. Most equity and index options markets trade vanilla American or European calls, not binary options. However:
- Some futures exchanges (e.g., CME) list binary options on commodities and currency pairs.
- Retail binary-options platforms (often offshore) offer cash-or-nothing calls on forex pairs, stocks, and commodities—though these are highly regulated in the US and prohibited for most retail traders.
- **OTC (over-the-counter)** markets see cash-or-nothing calls traded between institutions and sophisticated traders on a bespoke basis. A bank might customize a cash-or-nothing call on an equity, commodity, or index for a corporate client or hedge fund.

**Availability to retail traders** is limited in the US, as the SEC and CFTC have cracked down on binary-options retail offerings. Most retail traders access these structures through synthetic replication (combining vanilla options) rather than buying them directly.

## Synthetic Replication: Building a Cash-or-Nothing Call from Vanillas

A trader without direct access to cash-or-nothing calls can approximate one using vanilla options. A simple approach:
- Buy a vanilla call at strike K.
- Buy a vanilla put at strike K (same strike, same expiration).
- This is a [straddle](/straddle/); it profits if the underlying moves away from K in either direction.

A more precise replication for a cash-or-nothing call uses a call spread:
- Buy a vanilla call at strike K.
- Sell a vanilla call at strike K + ε (a slightly higher strike).
- Adjust the contract sizes so the payout is approximately fixed.

As ε approaches zero, the spread's payoff approaches a binary payout at the single strike K. In practice, using a tight spread (e.g., $100 call / $101 call) on an equity can closely mimic a $1 cash-or-nothing call.

## Greeks and Hedging Sensitivity

The [Greeks](/delta/) (delta, gamma, vega, theta) of a cash-or-nothing call differ from a vanilla call:
- **Delta** is highest near the strike (the option is most sensitive to spot-price moves right at the boundary).
- **Gamma** is highest at the strike and decays away (curvature is sharpest right at the threshold).
- **Theta** (time decay) accelerates near expiration (the boundary becomes narrower, so remaining time value evaporates faster).
- **Vega** (volatility sensitivity) is also highest at the strike (volatility most affects the probability of crossing it).

For traders hedging or managing a position, these non-linear Greeks mean that delta-hedging a short cash-or-nothing call requires more frequent rebalancing as expiration approaches and the underlying approaches the strike.

## See also

<div class="wiki-seealso">

### Closely related

- [Vanilla call options and intrinsic value](/call-option/) — standard calls with scaling payoff
- [Put options and protective puts](/put-option/) — the downside analog; cash-or-nothing puts exist too
- [Strike price and exercise mechanics](/strike-price/) — how the strike threshold is set and enforced
- [Option Greeks: delta, gamma, vega, theta](/delta/) — sensitivity metrics for hedging and [risk management](/value-at-risk/)
- [Black-Scholes model and option pricing](/black-scholes-model/) — underlying math for valuing binary options

### Wider context

- [Exotic options and structured products](/structured-product/) — broader class of non-vanilla derivatives
- [Over-the-counter (OTC) markets and counterparty risk](/over-the-counter-market/) — where bespoke cash-or-nothing calls trade
- [Hedging and derivatives](/derivatives-hedging/) — risk-management frameworks
- [Synthetic replication and option spreads](/option/) — replicating payoffs from basic building blocks

</div>
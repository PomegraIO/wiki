---
title: "Gamma Risk in Options: Why It Matters Near Expiry"
description: "Gamma risk in options: why delta changes faster near expiration, increasing hedging costs for options sellers and rebalancing risks for hedgers."
keywords:
  - gamma risk options explained
  - gamma options near expiration
  - delta hedging gamma cost
  - gamma decay expiration
  - options rebalancing risk
  - high gamma options
image: /svg/derivatives.svg
---

*[Gamma](/gamma/) is the rate at which [delta](/delta/) changes. Near expiration, gamma spikes—meaning small moves in the underlying asset force massive shifts in the [delta](/delta/) of an option position, requiring frequent and costly rebalancing. For a hedger, this is a tax on the hedging itself. For an option seller, it is the meat of risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma — the hidden cost of hedging</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Gamma measures delta's sensitivity to the underlying; it peaks as expiration nears, driving rebalancing costs.</div>

|   |   |
|---|---|
| **Gamma is** | The second derivative of option price w.r.t. underlying price |
| **Units** | Change in [delta](/delta/) per dollar move in the spot |
| **Peak timing** | At-the-money options nearest to expiration |
| **Implication** | Small moves → large delta shifts → frequent rehedging |
| **Cost** | Transaction costs, bid-ask spreads, slippage |
| **Who pays** | Option sellers (short gamma) and hedgers rebalancing |
| **Who benefits** | Option buyers (long gamma) and mean-reversion traders |

</aside>

## Delta is not constant

An [option](/option/) does not behave like a simple linear bet. When you own a call [option](/option/) deep out-of-the-money (the underlying is far below the strike), a $10 move in the underlying barely moves the option price. The [delta](/delta/) is near zero.

When the underlying is near the strike (at-the-money), that same $10 move swings the option price by a large amount. The [delta](/delta/) is near 0.5.

When the underlying is deep in-the-money, the option tracks the underlying nearly one-for-one. The [delta](/delta/) is near 1.0.

This is where [gamma](/gamma/) enters: gamma measures how much [delta](/delta/) itself changes when the underlying moves. It is the second derivative, or the slope of the [delta](/delta/) curve.

## Gamma spikes near expiration

Gamma is highest for at-the-money options that are close to [expiration](/expiration-contracts/). The closer you get to the expiration date, the more dramatic the change.

Consider a call [option](/option/) with 90 days to expiration, struck at-the-money. The [delta](/delta/) is 0.50. A $1 move up in the underlying might shift [delta](/delta/) to 0.52. Gamma is small.

Now consider the same call with 1 day to expiration, still at-the-money. The [delta](/delta/) is still about 0.50, but a $1 move up in the underlying shifts [delta](/delta/) to 0.90 or higher. The stock is now almost certainly finishing in-the-money, so the option is almost as good as owning the underlying. Gamma is enormous.

On the final day, gamma reaches its extreme. A cent move in the underlying can flip [delta](/delta/) from 0.1 to 0.9. This is the "knife-edge" nature of deep out-of-the-money short-dated options.

The reason is simple: Near expiration, there is no time value left to cushion the option. An [option](/option/) is a bet on where the underlying will be at a specific moment. With days left, that moment is imminent. A tiny move that pushes you from out-of-the-money to in-the-money is a binary event. [Delta](/delta/) lurches.

## The hedging cost: a worked example

Suppose you are a volatility trader. You want to be [delta](/delta/)-neutral—indifferent to direction—but long [volatility](/historical-volatility/). You sell 100 call [options](/option/) (10 contracts) struck at $100, expiring in 10 days. You immediately hedge by buying delta-equivalent shares of the underlying.

The [delta](/delta/) of each short call is −0.50 (since you sold it), so you buy 50 shares at $100 to be neutral. Your [delta](/delta/) is now 0: you have −5,000 (from short calls) + 5,000 (from long shares) = 0 [delta](/delta/).

The next day, the stock jumps to $101. Your short calls now have [delta](/delta/) = −0.65 each. You are now short 6,500 [delta](/delta/) (100 × −0.65). To rebalance to zero, you must sell 1,500 shares at $101.

The day after, the stock falls back to $100.50. Your calls now have [delta](/delta/) = −0.58. You need to buy back shares to re-neutral. You purchase 700 shares at $100.50.

The day after, the stock goes to $100.80. You rebalance again, selling 500 shares at $100.80.

Over four days of hedging, you have done the classic "sell high, buy low" pattern: sold at 101, bought back at 100.50, sold at 100.80. But here is the kicker: You are locked into this pattern because gamma is forcing you to rebalance. You are not choosing to trade; gamma is choosing for you.

Your rebalancing costs include:
- Bid-ask spreads: Each trade eats 1–2 cents per share.
- Market impact: Large rebalances may move the stock.
- Commissions: Less relevant today, but still a factor.
- Slippage: You rarely execute at the midpoint.

Over a 10-day life, you might rebalance 4–6 times. With gamma rising as [expiration](/expiration-contracts/) nears, the number of rebalances accelerates in the final days.

## Gamma, volatility, and options prices

This is critical: The higher the realized volatility (how much the underlying actually moves), the higher the gamma cost to the hedger.

If you sell a call and the stock sits perfectly still, gamma is irrelevant—your [delta](/delta/) hedge is perfect, and you make money from the [theta](/theta/) (time decay) you sold. You harvested [time value](/time-value/) without paying a dime in rehedging costs.

If the stock whipsaw back and forth violently, every move forces a rehedge. You buy high, sell low, again and again. The realized volatility of the stock *costs* you money. That cost is paid to the option buyer, who is long gamma and benefits from high realized volatility.

This is why option prices include a premium for expected volatility. [Implied volatility](/implied-volatility/) prices in the market's expectation of how much gamma cost will be realized. If the market thinks the stock will be choppy, it demands a high [implied volatility](/implied-volatility/), raising the [option premium](/option-premium/). If the stock is dead calm, [implied volatility](/implied-volatility/) is low.

The option seller's profit, then, depends on *selling* high [implied volatility](/implied-volatility/) but *realizing* low actual (realized) volatility. That spread—the gap between implied and realized volatility—is the seller's edge. Gamma cost is the mechanism that determines whether the seller wins.

## At-the-money vs. out-of-the-money gamma

Gamma is highest for at-the-money options and lower for both in-the-money and out-of-the-money options. 

An out-of-the-money [call](/call-option/), far from the strike, has low gamma. The [delta](/delta/) is near zero and changes slowly. The option is likely to expire worthless, so the [delta](/delta/) has a wide range where it can sit without changing much.

An in-the-money [call](/call-option/) deep in-the-money has low gamma. The [delta](/delta/) is near 1.0 and changes slowly as well. The option is very likely to finish in-the-money, so the [delta](/delta/) is already pegged.

An at-the-money call is on the knife-edge. The option could flip in-the-money or out-of-the-money with a small move, so [delta](/delta/) is highly sensitive to the underlying price.

This is why short-dated, at-the-money straddles (long both a call and a put at the same strike) blow up: both the call and the put have enormous gamma. A move in either direction forces a violent rehedge.

## Gamma risk for different positions

**Short gamma positions** (short calls, short puts, or short a straddle):
- Benefit if realized volatility is low (no rehedging, high [theta](/theta/) profit).
- Harmed if realized volatility is high (constant rehedging costs eat the profit).
- Most vulnerable near expiration, when gamma is highest.

**Long gamma positions** (long calls, long puts, or long a straddle):
- Benefit if realized volatility is high (rebalancing profits as you rehedge).
- Harmed if realized volatility is low ([theta](/theta/) decay erodes the position faster than gamma gains).
- Have the best return profile in violent markets.

**[Delta](/delta/)-neutral hedgers** (e.g., a bank hedging client derivatives with spot trades):
- Incur gamma costs whether volatility is high or low.
- Try to minimize rebalancing by trading in larger blocks or using less frequent rehedges (but this introduces directional risk).
- Offset gamma costs by earning the spread between the [option premium](/option-premium/) they charge clients and the underlying cost.

## Gamma decay and time decay

[Gamma](/gamma/) does not decay uniformly. [Theta](/theta/) (time decay) decays steadily—options lose value every day. But [gamma](/gamma/) accelerates as expiration nears.

With 180 days to expiration, gamma is small and changes slowly week to week.

With 30 days to expiration, gamma is higher and changing more noticeably.

With 5 days to expiration, gamma is very high and changing sharply day to day.

With 1 day to expiration (at-the-money), gamma is at its peak and can change minute to minute.

This is why option traders care so much about the "theta/gamma tradeoff" in the final week. You are collecting [theta](/theta/) (daily decay is fat), but you are paying for it with escalating gamma costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the directional sensitivity that gamma measures the change in
- [Theta](/theta/) — time decay, which accelerates as gamma spikes near expiration
- [Implied volatility](/implied-volatility/) — the expected volatility priced into the option premium
- [Option premium](/option-premium/) — the price the option buyer pays, which compensates for gamma risk
- [Volatility smile](/volatility-smile/) — how gamma relates to different strikes
- [Call option](/call-option/) — the derivative position where gamma creates hedging costs
- [Put option](/put-option/) — the other position where gamma scales near expiration

### Wider context

- [Option](/option/) — the underlying instrument whose risks gamma measures
- [Derivatives hedging](/derivatives-hedging/) — the operational practice where gamma costs are incurred
- [Vega](/vega/) — another Greeks that measures exposure to [volatility](/historical-volatility/) changes
- [Time value](/time-value/) — the component of the option price that bleeds away as [theta](/theta/)
- [Black-Scholes model](/black-scholes-model/) — the framework that quantifies gamma and the Greeks

</div>

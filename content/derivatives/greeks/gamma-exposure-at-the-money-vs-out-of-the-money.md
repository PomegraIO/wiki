---
title: "Gamma Exposure: At-the-Money vs Out-of-the-Money Options"
description: "Gamma at the money vs out of the money options: peaks at-the-money and declines sharply for strikes away from spot, creating different hedging burdens."
keywords:
  - gamma at the money vs out of the money options
  - gamma exposure moneyness
  - atm gamma vs otm gamma
  - option gamma profile
image: /svg/derivatives.svg
---

*The gamma of an option—the rate at which its **delta** changes as the underlying price moves—is steeply concentrated at-the-money (ATM) and drops sharply as strikes move away from the current spot price. This concentration means ATM options demand the most frequent re-hedging, while out-of-the-money (OTM) options expose traders to larger, saltier delta jumps per unit price movement but less often.*

<div class="wiki-hatnote">

For context on delta and how options respond to price changes, see **[delta](/delta/)** and **[in the money](/in-the-money/)**. This article focuses on how gamma varies across different strike prices relative to the spot price.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma Exposure — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Gamma is highest at-the-money and declines as you move away from spot, forcing different hedging regimes.</div>

|   |   |
|---|---|
| **Peak gamma location** | At-the-money (spot ≈ strike) |
| **Gamma as moneyness widens** | Falls sharply for in-the-money or out-of-the-money strikes |
| **ATM gamma implication** | More frequent [delta](/delta/) adjustments needed |
| **OTM/ITM gamma implication** | Large delta changes per price move; less frequent adjustment |
| **Hedging cost driver** | ATM options incur more transaction costs from re-hedging |
| **Gamma volatility sensitivity** | Higher [implied volatility](/implied-volatility/) flattens the gamma profile |

</aside>

## The gamma curve across strikes

For a given underlying, time to expiration, and [implied volatility](/implied-volatility/), the gamma of ATM options is substantially higher than that of options struck away from spot. The difference is not marginal: an ATM call's gamma might be 0.08 per dollar of spot price movement, while a call struck 10% OTM has gamma around 0.02. This creates a curve that peaks sharply at the money and tapers on both sides.

The intuition is straightforward. An ATM option sits at the knife's edge—it is nearly equally likely to end in or out of the money, so small moves in the underlying produce material changes in its delta. A deep OTM call with a strike far above spot has already "decided" it will likely expire worthless, so its delta hovers near zero and responds sluggishly to price bumps. By contrast, an ITM call with a strike far below spot is already behaving almost like a forward: its delta is close to 1.0, and moves to higher prices do not change that much further.

## Why ATM options demand constant re-hedging

A [delta-neutral](/delta/) trader—one who holds an option position offset by a spot position or futures—must constantly adjust the hedge as the underlying price changes. The [gamma](/gamma/) of the position tells you how much your delta will shift given a price move.

With an ATM option, gamma is large. If you are long an ATM call and delta-neutral (short the underlying), a 1% jump in the stock means your delta increases sharply—your long gamma has cost you money on the move, but your delta is now far too positive. You must sell more of the underlying to re-hedge. This cycle repeats many times over the option's life, especially as volatility contracts near expiration.

OTM and ITM options have lower gamma, so their delta changes more slowly. You re-hedge less often, but each hedge adjustment is a larger shift in delta when it does happen. For a scalping operation seeking to profit from frequent small moves, ATM gamma is a curse: you are forced to buy high and sell low, realizing losses on the moves themselves. For a large rebalancing trade, OTM gamma is acceptable because you can wait longer between adjustments.

## Transaction costs and the gamma drag

Every time you re-hedge, you pay the [bid-ask spread](/bid-ask-spread/), fees, and possibly market impact. ATM options, with their high gamma, force you to re-hedge more often. Over the life of an option position, these cumulative costs represent a real drag on P&L—sometimes called gamma drag or [theta](/theta/) bleed (though technically theta is the time decay cost, and gamma drag is the cost of re-hedging volatility).

Consider a strangle (long OTM call and put): its gamma is low at inception, so you hedge infrequently. The position profits when volatility spikes, because the [straddle](/straddle/)-like nature of long gamma allows you to capture volatility moves with fewer adjustments. But with an ATM straddle (long ATM call and put), you are constantly re-hedging, burning the spread on every turn.

## How implied volatility shapes the gamma curve

A subtle but important factor: higher [implied volatility](/implied-volatility/) flattens the gamma curve. When volatility is high, even OTM options have material probability of expiring in the money, so their delta is less extreme and gamma is higher. When volatility is low, the gamma curve is more concentrated at ATM—the probability of an OTM option reaching the strike is small, so its gamma is negligible.

This matters operationally. In a low-vol environment, running a hedge on an OTM option is cheaper (you move it less often), but you are vulnerable to larger delta steps if volatility jumps. In a high-vol environment, the gamma curve is flatter, so there is less incentive to focus all hedging effort on ATM options.

## Strike selection in a hedging program

Portfolio managers choosing which strikes to hedge with in a tail-risk program will naturally favor OTM options: they are cheaper and require less active re-hedging. A protective put deep OTM protects against catastrophic loss but does not bleed money on small daily moves. But if volatility expectations change or the market exhibits rare large moves, that OTM position's delta can jump materially, leaving the portfolio exposed until re-hedging occurs.

Conversely, a bank offering put options to clients faces the highest hedging cost when those puts are ATM. When spot is near the strike, any small move shifts the delta, forcing constant adjustments. This is why dealers often widen their bid-ask spreads most on ATM options: they are compensating for the expected re-hedging burden.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — rate of change of delta as the underlying moves
- [Delta](/delta/) — the rate at which an option price changes with the underlying
- [Theta](/theta/) — time decay cost of holding an option
- [Implied volatility](/implied-volatility/) — market consensus forward volatility
- [Straddle](/straddle/) — long ATM call and put
- [Option](/option/) — definition and mechanics
- [Vega](/vega/) — sensitivity to changes in volatility
- [Strike price](/strike-price/) — the contractual exercise price

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — overview of hedging strategies
- [Market maker trading](/market-maker-trading/) — role of dealers and spread management
- [Capital adequacy](/capital-adequacy/) — regulatory capital charges for option positions

</div>

---
title: "Basis Risk in Hedging"
description: "Why hedges fail to fully offset a position when the hedging instrument's price does not move in lockstep with the underlying exposure."
keywords:
  - basis risk
  - basis risk hedging
  - imperfect hedge
  - hedge failure
  - cross-hedge
image: "/svg/risk.svg"
---

*When you hedge a position, you assume the hedging instrument will move in tandem with your exposure—but it often doesn't. **Basis risk** is the danger that the hedge and the underlying exposure move at different speeds or in different directions, leaving you partially unprotected. A perfect hedge is rare; basis risk is the usual cost of protection.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Arises when the hedge and exposure do not move in perfect lockstep.</div>

|   |   |
|---|---|
| **Definition** | Imperfect correlation between hedge and position |
| **Root cause** | Different maturities, grades, or markets |
| **Common form** | Cross-hedge using a correlated but imperfect instrument |
| **Measurement** | Correlation; beta; historical price spreads |
| **Cannot be eliminated** | Only minimized through careful design |
| **Trade-off** | Hedging cost vs. basis risk tolerance |

</aside>

## The ideal that never exists

A perfect hedge would mean: you own 10,000 barrels of crude oil; you sell 10,000 barrels of crude futures. Oil rises; your physical barrels gain $50,000 and your short futures loses $50,000—net zero. Reality rarely cooperates.

Suppose you own crude oil but the only futures contract available has a different grade (lighter, more volatile), a different delivery date (three months out instead of immediate), or trades on a different exchange with different liquidity. When your crude moves 3%, the futures might move 2.8% or 3.2%. That difference—the **basis**—is the gap between what you wanted to happen and what actually did.

More broadly, basis risk materializes whenever:

- **Grade or quality differs** — You hold Brent crude; you hedge with West Texas Intermediate futures. The two don't move dollar-for-dollar.
- **Geography matters** — You own natural gas delivered to Houston; the futures contract settles in Henry Hub, Louisiana. Transport and supply differences create basis.
- **Maturity mismatch** — You own bonds due in 18 months but hedge with a 10-year Treasury contract. Different duration means different interest-rate sensitivity.
- **Counterparty differs** — You're exposed to Bank A's credit risk but hedge with Bank B's credit default swap. Bank A and B's credit spreads don't move together.

## The cross-hedge problem

A **cross-hedge** occurs when no perfect instrument exists, so you hedge with something correlated but imperfect. An airline exposed to jet fuel prices might hedge with crude oil futures—the best proxy available. But jet fuel has its own supply chain and price movements; correlations with crude slip during refinery problems or geopolitical shocks.

The effectiveness of a cross-hedge depends on **correlation** and **relative volatility**. If jet fuel and crude oil have a correlation of 0.85 (fairly high) and jet fuel is 20% less volatile than crude, a $1 million exposure needs roughly $833,000 notional hedged in crude to stay flat if both move by their historical standard deviations. But that's a historical approximation; the relationship can break in real market stress.

During 2020, when oil prices collapsed and refineries shut in, the correlation between crude and jet fuel broke down sharply. Airlines found their hedges performed worse than historical data suggested—a harsh lesson in basis risk.

## Measuring and quantifying basis

Risk managers estimate basis risk by examining the historical relationship between the position and hedge:

1. **Calculate the correlation** — How often do they move together? Perfect = 1.0; independent = 0.
2. **Compute beta** — For each 1% move in the hedge, how much does the position move? If beta = 0.92, the position moves 92% as much.
3. **Observe basis spreads** — Track the actual price gap over time. Wider and more volatile spreads signal higher basis risk.

A hedged portfolio with 0.95 correlation and 0.95 beta might still endure basis risk during tail events. The 2008 crisis saw relationships that looked stable for decades suddenly diverge as correlations collapsed and liquidity vanished.

## Maturity and convexity basis

A subtler form arises with bonds and interest-rate derivatives. A portfolio manager with $100 million in 5-year bonds might hedge with 10-year Treasury futures because they're more liquid. But a 1% rate rise affects a 5-year bond and a 10-year bond differently—the 10-year loses more because of its longer [duration](/duration/). The manager has locked in an implicit basis bet on the slope of the [yield curve](/yield-curve/).

Similarly, options create convexity basis: a short call option in a stock isn't perfectly hedged by holding the stock, because the option's [gamma](/gamma/) (curvature) means the delta hedge needs constant rebalancing. Transaction costs and price impact create slippage—another flavor of basis risk.

## Basis risk in credit derivatives

A company's bond traders hold a $50 million position in unsecured debt. They hedge with a [credit default swap](/credit-default-swap/) on the same company. If the company's creditworthiness deteriorates 2%, the bond loses value—say $500,000—but the CDS spread only widens 150 basis points instead of 200, netting only $375,000 on the hedge. The bond is senior; the CDS protects all debt equally, creating a basis mismatch in recovery value and seniority.

Corporate-bonds-to-CDS basis fluctuates with funding conditions and dealer supply. In 2008 and again in 2020, this basis blew out as hedges became unreliable; protection that looked cheap became unavailable or only accessible at distressed prices.

## Accepting and pricing basis risk

Basis risk cannot be eliminated entirely—only accepted, measured, and priced. A farmer hedging next year's wheat crop with futures accepts that the harvest will occur at a location and time when the futures contract does not—creating basis. The farmer calculates the expected basis based on historical spreads and accepts this as a cost of certainty. Without it, commodity farming would be uninsurable.

Large institutions use basis-risk dashboards, stress tests, and scenario analysis. "If our position moves 2% and the hedge moves 1.8%, we lose 0.2% × position notional—is that acceptable?" If not, they adjust the hedge ratio, shift to a better-correlated instrument, or accept tighter risk limits.

## See also

<div class="wiki-seealso">

### Closely related

- [Derivatives hedging](/derivatives-hedging/) — strategies to protect against price moves
- [Duration](/duration/) — how bond prices respond to rate changes; a key source of maturity basis
- [Correlation](/beta/) — measuring the relationship between two prices
- [Counterparty risk](/counterparty-risk/) — another form of hedge failure when the counterparty defaults
- [Interest-rate risk](/interest-rate-risk/) — a major driver of basis in fixed-income hedges

### Wider context

- [Tail risk](/tail-risk/) — basis often breaks down precisely when you need it most
- [Stress testing](/stress-testing/) — how firms validate hedge effectiveness under extreme moves
- [Hedge fund](/hedge-fund/) — strategies that explicitly manage basis risk in relative-value trades
- [Futures contract](/futures-contract/) — the primary tool for hedging, though imperfect
- [Forward contract](/forward-contract/) — custom hedges with other basis trade-offs

</div>

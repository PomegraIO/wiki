---
title: "Volatility Skew vs Volatility Smile: What the Difference Means for Pricing"
description: "Understand volatility skew vs smile and how these asymmetric and symmetric patterns in implied volatility affect option pricing across different strike prices."
keywords:
  - volatility skew vs smile difference
  - implied volatility surface patterns
  - option pricing strike sensitivity
  - volatility smile asymmetry
  - derivatives pricing skew effect
---

*The **volatility skew vs smile difference** is a pattern in how implied volatility varies across strike prices. Some underlyings show a skew—where out-of-the-money puts trade at markedly higher implied volatility than out-of-the-money calls, tilting the curve one-sided. Others display a smile—a symmetric pattern where volatility rises equally as you move away from the at-the-money strike in either direction. These shapes emerge from market pricing pressures and have real consequences for how options are valued.*

<div class="wiki-hatnote">

This article covers implied volatility surface shapes. For the Greeks that measure sensitivity to volatility changes, see [vega](/vega/). For the fundamental volatility model that treats it as constant, see [Black-Scholes model](/black-scholes-model/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Skew vs Smile — key patterns</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Surface shape drives option valuation and hedging costs.</div>

|   |   |
|---|---|
| **Skew** | One-sided tilt; OTM puts higher than OTM calls (equity) or opposite (FX) |
| **Smile** | Symmetric U-shape; volatility rises equally on both sides of ATM |
| **Typical in equities** | Skew (post-1987) dominates; calls cheaper, puts more expensive |
| **Typical in currencies** | Smile or reverse-skew; risk priced symmetrically across wings |
| **Pricing impact** | OTM options worth more than Black-Scholes predicts; wider spreads |
| **Hedge cost** | Skew = unequal cost to protect downside vs upside |

</aside>

## Why Black-Scholes predicts a flat surface

The original [Black-Scholes model](/black-scholes-model/) assumes constant volatility across all strikes and maturities. In that frictionless world, implied volatility—the volatility figure that makes a model price match market price—should be identical for every option on the same underlying and maturity. Plug in the same σ whether you price a 5% OTM call or a 10% OTM put; the model gives a consistent answer.

But markets don't behave that way. When traders calibrate the model backwards from actual option quotes, implied volatility varies dramatically with strike. This variation is not noise; it reflects real constraints, demands, and fears that the constant-volatility assumption ignores.

## The equity volatility skew

Equity markets almost universally exhibit a **volatility skew**: out-of-the-money puts have significantly higher implied volatility than out-of-the-money calls on the same maturity. This pattern intensified after the 1987 crash and has persisted through subsequent corrections.

The mechanism is intuitive. A portfolio manager holding a large equity position fears sudden downside drops far more than gradual upside drifts. Downside tail risk—a gap down in the market—is the nightmare scenario. Demand for put protection overwhelms supply, bidding up put prices. To value those puts consistently using the model, traders back out a higher implied volatility.

This skew shapes option prices concretely. A 10% OTM put on a blue-chip equity may trade at 25% implied volatility while the at-the-money option sits at 20% IV and a 10% OTM call only 18%. A trader pricing a 15% OTM put using the 20% ATM volatility would systematically misprice it—it would come in too cheap.

The skew is also asymmetric by direction. Puts further out-of-the-money can trade at even higher IV, creating a tilt or ramp. A 20% OTM put might hit 30% IV. This reflects a belief that tail risk is concentrated in the deep downside rather than linearly distributed.

## The volatility smile in other markets

Currency and index derivatives often display a **volatility smile** instead: volatility rises as you move away from the at-the-money strike in *either* direction, creating a symmetric U-shape. A 10% OTM call and a 10% OTM put both trade at 24% IV, while the ATM option sits at 20%.

The smile is less about directional fear and more about the risk of large moves in *either* tail. Foreign exchange markets, for instance, fear both currency appreciation and depreciation symmetrically—political shocks, interest rate divergence, or trade surprises can push either direction. Neither side has a monopoly on tail risk.

Volatility smiles also appear in equity indices, especially after major corrections when options traders have been burned in both directions and price protection symmetrically. Commodity derivatives frequently smile as well, reflecting physical supply and demand that can shift either way.

## Why the smile is thinner for single-name equities

Individual stocks almost never display a perfect smile. The equity skew dominates because single companies lack the two-way tail risk of markets or currencies. A technology stock can go up 300% or down to zero, but the zero scenario is what traders fear and pay for. A negative earnings surprise compounds the downside; an upside surprise just lifts the stock higher. This creates fundamental asymmetry.

An index, by contrast, can crash hard *or* rally hard on broad macroeconomic swings, currency moves, or policy surprises. The upside and downside tail risks feel more balanced, pushing towards a smile.

## Practical consequences for pricing

The difference between skew and smile directly affects how traders mark option prices and hedge portfolios:

- **Wider bid-ask spreads in deep OTM options.** Because volatility varies so much by strike, dealers cannot hedge a deep OTM put using a simple position in the underlying. They must dynamically adjust. That friction shows up in wider bid-ask spreads, especially for skewed tails.

- **Calibration and model choice.** A trader using a flat constant-volatility model will misprice options across the surface. Many practitioners use local volatility models or stochastic volatility models to fit the surface and reprice accurately.

- **Vega hedging becomes multi-strike.** A trader long a 15% OTM put has vega exposure, but hedging it with an at-the-money volatility position leaves them unhedged if the skew flattens (IV drops faster at the 15% strike than ATM). Effective hedging requires monitoring vega across multiple strikes—a multidimensional problem.

- **Bid risk in corporate actions.** A put buyer at one strike may face an mispriced short call at a different strike if the skew shifts. M&A announcements, earnings misses, or changes in market regime can alter the skew shape dramatically, turning a seeming arbitrage into a one-sided loss.

## How regime and data shape the surface

The implied volatility surface is not fixed. It evolves as market fears and structural conditions change. A market crash will steepen the equity skew as downside hedging demand spikes. A period of calm can flatten it. Currency volatility can shift from a smile to a skew and back as geopolitical risk waxes and wanes.

Historical volatility—the realized volatility of past returns—feeds the surface but does not determine it. Options prices reflect *expected* volatility and tail risk. During a quiet market with high realized volatility trending downward, implied volatility often falls faster than realized, leaving options "cheap" by historical measures but expensive by forward-looking risk assessment.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes model](/black-scholes-model/) — Foundation model; assumes constant volatility across strikes
- [Vega](/vega/) — Sensitivity of option price to changes in implied volatility
- [Delta](/delta/) — Sensitivity to underlying price; varies with implied volatility assumptions
- [Implied volatility](/implied-volatility/) — The volatility figure backed out from market prices
- Local volatility — Models volatility as a deterministic function of price and time
- [Option premium](/option-premium/) — Price paid; affected by surface shape and strike selection
- [Strike price](/strike-price/) — Reference level; skew and smile create different moneyness risks

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — Risk management using options; surface shape affects hedging cost
- [Option](/option/) — Foundational; rights to buy or sell at set price
- [Volatility smile](/volatility-smile/) — Symmetric pattern specific to some markets
- [Historical volatility](/historical-volatility/) — Realized past volatility; distinct from implied
- [In the money](/in-the-money/) — Moneyness definition; determines distance to skew/smile tilt

</div>

---
title: "Convexity Adjustment: Why Futures Prices Differ From Forward Prices"
description: "Convexity adjustment explains why futures contracts command a price premium or discount relative to economically identical forwards due to daily settlement cash flows."
keywords:
  - convexity adjustment
  - futures vs forwards pricing
  - daily margining effect
  - futures price premium
  - interest rate derivatives
image: /svg/derivatives.svg
---

*The **convexity adjustment** is the price correction needed to align a [futures contract](/futures-contract/) with an economically identical [forward contract](/forward-contract/), arising because futures settlement happens daily while forwards settle at maturity. When rates are volatile, this daily cash-flow cycling creates a systematic bias that derivative traders must account for.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity Adjustment — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The price gap between futures and forwards stems from the [interest-rate](/interest-rate/) optionality built into daily settlement.</div>

|   |   |
|---|---|
| **Root cause** | Daily margin adjustments on futures; forwards settled only at maturity |
| **Direction** | Typically positive (futures > forwards) when [volatility](/historical-volatility/) rises |
| **Formula magnitude** | ~0.5 × (volatility)² × convexity × time-remaining |
| **Matters most for** | Long-dated [fixed-income](/bond/) and currency derivatives |
| **When negligible** | Short maturities, low rates, low volatility |
| **Who cares** | Dealers, traders, risk managers comparing synthetic [forward rates](/forward-guidance/) |

</aside>

## Why futures and forwards are not the same price

On the surface, a futures contract and a forward contract on the same underlying asset and settlement date should have identical values. Both are agreements to exchange the asset at a locked-in price on a known date. But they differ in one crucial way: **futures are marked to market daily, with gains and losses settled immediately; forwards are not.**

When you hold a long futures position and rates fall (or the underlying appreciates), you collect a margin deposit today. You can reinvest it. If rates subsequently rise, you pay margin tomorrow, forcing you to borrow at a higher rate. A forward holder faces neither of these intermediate cash flows—they settle when the contract matures.

This difference matters because in a volatile market, daily settlement creates an embedded optionality. A long futures holder gets to reinvest favorable margin at the then-current rate; a forward holder cannot. That asymmetry translates into a price premium. The **convexity adjustment** quantifies this bias.

## The intuition: right-way and wrong-way risk

Under typical conditions, interest-rate movements correlate with the futures payoff in a favorable way. When rates fall and the underlying asset increases in value (or the forward rate climbs), the long futures holder receives margin and can reinvest at the lower prevailing rate—locking in a gain. Conversely, when rates rise and the contract loses value, margin is posted, but it is borrowed at the higher rate—amplifying the loss.

Over many cycles, the reinvestment side skews profitable relative to the borrowing side, because the trader can reinvest gains at the lower rates that correspond to favorable price moves. This is the **convexity benefit** to the futures holder; it is why futures prices typically exceed their forward counterparts.

The effect is most pronounced when:
- Volatility is high (wider swings mean bigger interim margin moves)
- Rates are positively correlated with the underlying (common in bond and currency markets)
- The contract is long-dated (more cycles for the bias to accumulate)
- Interest rates themselves are volatile (reinvestment rates fluctuate widely)

## The formula and its moving parts

The standard approximation for convexity adjustment is:

**Convexity Adjustment ≈ 0.5 × (σ²) × C × T**

where:
- **σ** = annualized volatility of the underlying (or forward rate)
- **C** = convexity of the payoff (the second derivative of price with respect to yield)
- **T** = time to maturity in years
- The coefficient 0.5 arises from the second-order Taylor expansion of the reinvestment term

For a [bond futures](/bond/) contract, convexity is positive and substantial—a 20-year bond has convexity around 6.0. For a 10% volatility, 2-year contract:

Adjustment ≈ 0.5 × (0.10)² × 6.0 × 2 = 0.006 or about 60 basis points.

This is material: it means the futures quote will typically run 60bp above the synthetic forward price derived from spot-and-rate.

## When convexity adjustment is negligible

For short-dated contracts, the adjustment shrinks rapidly. A 3-month futures contract with the same volatility and convexity:

Adjustment ≈ 0.5 × (0.10)² × 6.0 × 0.25 ≈ 7.5 basis points

—worth tracking for precise dealers, but often invisible in trading.

In low-volatility regimes (e.g., when [central banks](/central-bank/) have anchored [inflation expectations](/inflation-expectations/)), the adjustment also flattens. And for assets with negative or very low convexity (like certain options or short-dated instruments), the term vanishes.

## Practical applications: Eurodollars and bonds

The [eurodollar futures](/libor/) contract is the classic arena for convexity vigilance. Eurodollars are 3-month [LIBOR](/libor/) futures; when traded far out the [curve](/yield-curve/)—say 5 or 10 years—convexity adjustments can reach 50bp to 100bp.

Traders comparing a eurodollar futures strip (a sequence of quarterly contracts) to a synthetic forward curve built from spot and [interest-rate swaps](/interest-rate-swap/) must subtract the accumulated convexity adjustment from the futures quotes to get apples-to-apples forward rates.

U.S. Treasury bond futures (contracts on 10-year or 30-year bonds) exhibit smaller adjustments because the convexity is lower and the [duration](/duration/) is not extreme, but the effect is still priced. Conversely, in markets with very steep [yield curves](/yield-curve/) or high [rate volatility](/volatility-smile/), the adjustment can exceed 100bp.

## Measurement and estimation challenges

The formula above is a standard approximation but assumes constant rates and volatility. Real markets deviate:

1. **Path dependence**: The exact timing of margin flows matters if reinvestment rates change daily. A simplified model may miss second-order effects.

2. **Rate distribution**: If rates are non-normally distributed (fat tails), extreme moves create larger margin swings, and the adjustment can be underestimated.

3. **Correlation**: The adjustment assumes rates and the underlying price are positively correlated. If they move together, the effect is amplified; if they move apart, it shrinks.

Practitioners often fit convexity adjustments empirically, comparing actuals futures-forward pairs over rolling periods and backing out the implied volatility or convexity parameter.

## When the adjustment flips negative

In rare cases—typically in deflationary environments or when rates are sufficiently negative—the correlation between rates and asset prices can invert. A short futures position might then enjoy the reinvestment advantage, causing the futures price to fall *below* the forward price. This reversal is uncommon in developed markets but has been observed in some emerging-market currency and commodity futures during sharp disinflationary episodes.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate Swap](/interest-rate-swap/) — the OTC forward instrument that embeds the same rate optionality
- [Duration](/duration/) — measures the sensitivity of bond prices to rate changes, a key input to convexity
- [Volatility Smile](/volatility-smile/) — non-constant volatility across strikes; relevant for nonlinear payoffs
- [Futures Contract](/futures-contract/) — the daily-settled sibling of the forward
- [Forward Contract](/forward-contract/) — the bilateral, unsettled-until-maturity equivalent

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why traders build synthetic forwards and must adjust for convexity
- [Bond](/bond/) — the typical underlying, and its convexity is central to the adjustment
- [Yield Curve](/yield-curve/) — the shape and [steepness](/yield-curve/) drive reinvestment rate expectations
- [Interest Rate](/interest-rate/) — the driver of daily margin flows and reinvestment opportunities
- [Central Bank](/central-bank/) — influences rate volatility and inflation expectations, key inputs to the model

</div>

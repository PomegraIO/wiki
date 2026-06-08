---
title: "Vanna: The Cross-Greek Between Delta and Vega Explained"
description: "Vanna measures how delta changes as implied volatility shifts—a critical Greek for hedging barrier options and volatility-sensitive positions."
keywords:
  - vanna option greek explained
  - delta vega cross greek
  - option greeks sensitivity
  - barrier option hedging
  - volatility surface
image: /svg/derivatives.svg
---

*The **vanna option greek** measures the sensitivity of delta to changes in implied volatility, or equivalently, the sensitivity of vega to spot price movements. For traders hedging positions sensitive to both price and volatility, vanna captures a cross-risk that pure delta and vega hedges miss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vanna — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The overlooked Greek that tracks how volatility exposure shifts with price.</div>

|   |   |
|---|---|
| **What it measures** | Rate of change of delta with respect to volatility (∂Δ/∂σ) |
| **Alternative view** | Rate of change of vega with respect to spot price (∂ν/∂S) |
| **Sign convention** | Positive vanna: delta increases when volatility rises; negative vanna: delta decreases when volatility rises |
| **Units** | Delta per 1% volatility point (approximate) |
| **When it matters most** | Barrier options, deep out-of-the-money positions, skew-hedged portfolios |
| **Hedging method** | Adjust option ratios or rebalance volatility exposure as prices move |

</aside>

## The Two-Sided Interpretation of Vanna

Vanna's power lies in its dual nature. It can be understood in two equivalent ways:

1. **Delta's volatility sensitivity**: As implied volatility climbs, what happens to your delta hedge? For many positions, an increase in volatility tilts the delta in one direction or the other. Vanna quantifies that tilt.

2. **Vega's price sensitivity**: As the spot price moves, does your vega exposure (long or short gamma vol) grow or shrink? Vanna measures exactly this cross-derivative.

For traders, this equivalence matters because you can hedge vanna with either spot moves (which shift your delta) or volatility moves (which shift your vega). Most often, you adjust the relative quantities of long and short options as market conditions change.

## Why Vanna Is Largest for At-the-Money and Near-the-Money Options

The size of vanna follows a predictable pattern:

- **At-the-money (ATM) options** have the largest vanna magnitude. Here, delta is most sensitive to volatility changes because the option straddles the payoff boundary.
- **Deep out-of-the-money (OTM) or in-the-money (ITM) options** have small vanna. Their deltas are already close to zero or one, leaving little room to shift.
- **Expiration effects**: Vanna decays as expiration approaches, especially for OTM options that fall further out of reach.

This is why vanna hedging is often concentrated in and around the ATM strike: that's where the Greek has economic meaning and hedging is most active.

## Vanna and the Volatility Smile

In real markets, implied volatility is not flat across strikes—it forms a smile, smirk, or term structure. This curvature means vanna is not uniform across your book.

When you hold a portfolio of options at different strikes:
- Your OTM puts may have negative vanna (negative delta when vol rises).
- Your ATM calls may have positive vanna (positive delta when vol rises).
- The net effect depends on the mix.

A [volatility-smile](/volatility-smile/) environment magnifies vanna's practical importance because small spot moves can materially change how much of the vol curve your hedge covers.

## Barrier Options and Vanna Risk

Barrier options—which activate or knock out at a specified level—are notoriously vanna-heavy. 

Consider an up-and-out call that will be knocked out if the stock reaches a barrier above the current spot. As volatility rises:
- The probability of hitting the barrier increases.
- The effective delta of the position changes, sometimes dramatically.

A trader who hedges only delta and vega without accounting for vanna can be caught off-guard when a jump in implied volatility forces the position to re-hedge across a very different delta. This is vanna tail risk.

## Practical Hedging Implications

Because vanna connects two Greeks—delta and vega—hedging it requires a combination approach:

**Method 1: Ratio adjustment**
Rebalance your long and short option positions as the spot price changes, targeting a consistent net vega exposure. Each rebalance implicitly hedges vanna.

**Method 2: Spot-volatility correlation**
If spot and volatility are inversely correlated (as they often are in equity indices), movements in spot will naturally hedge part of your vanna. A static [delta-hedging](/delta-hedging/) routine captures this automatically.

**Method 3: Explicit vanna trades**
Use lower-liquid strikes or calendar spreads (longer-dated vs. nearer-dated) to isolate and adjust vanna exposure without overwhelming other Greeks.

The practical choice depends on liquidity, transaction costs, and how sensitive the overall position is to spot-volatility moves.

## Vanna and Gamma Scalping

Gamma scalping—rapidly rehedging delta to profit from realized volatility—generates costs that are partly captured by vanna. When you delta-hedge and the market moves, you rehedge at a different delta. If vanna is positive, the rehedge is "easier" (delta moves in your favor); if vanna is negative, it is "harder" (delta moves against you).

For a [gamma-scalping](/algorithmic-trading/) trader running tight hedges, accounting for vanna can mean the difference between collecting realized vol efficiently and being whipsawed by volatility surface moves.

## When to Ignore Vanna

For short-dated options, deep OTM, or very small portfolios, vanna often falls below the noise floor of other risks. A trader managing a portfolio of long-dated options with substantial deltas, however, cannot afford to skip it.

Similarly, in hedging regimes where spot and volatility are uncorrelated (rare, but it happens), vanna's impact weakens because the two sources of rehedging pressure work against each other.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — The first Greek; vanna measures how it shifts with volatility
- [Vega](/vega/) — Volatility sensitivity; vanna is its price-sensitivity counterpart
- [Gamma](/gamma/) — Convexity in delta; necessary for understanding vanna decay near expiry
- [Option premium](/option-premium/) — What funds the Greeks you're hedging
- [Barrier option](/option/) — The derivatives where vanna risk is most acute
- [Volatility smile](/volatility-smile/) — The skew landscape that makes vanna non-uniform

### Wider context

- [Black-Scholes model](/black-scholes-model/) — The framework underlying all Greek calculations
- [Implied volatility](/implied-volatility/) — The vol input that drives vanna moves
- [Options](/option/) — Foundation for understanding derivatives and hedging
- [Derivatives hedging](/derivatives-hedging/) — The practical reason vanna matters

</div>
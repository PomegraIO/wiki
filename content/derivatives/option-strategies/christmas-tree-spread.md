---
title: "Christmas Tree Spread"
description: "A multi-leg option strategy that extends a butterfly across three strikes, balancing limited risk with defined profit zones."
keywords:
  - option strategies
  - butter spread variants
  - vertical spreads
  - debit spreads
  - premium selling
image: "/svg/derivatives.svg"
---

*A **Christmas tree spread** is an asymmetric butterfly variant that uses three strike prices instead of the usual two, creating a lopsided profile that catches price movement in a wider range. Traders use it to reduce cost and shift risk tolerance, accepting larger potential losses on one side in exchange for better odds on the other.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Christmas Tree Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A three-strike extension of the butterfly, skewing payoff in one direction.</div>

|   |   |
|---|---|
| **What it is** | A multi-leg [option](/option/) spread using four options across three strikes |
| **Also called** | Skewed butterfly, unbalanced butterfly, call tree (bullish) or put tree (bearish) |
| **Setup** | Buy 1 call, sell 2 calls, buy 1 call at four different strikes (or puts, inverted) |
| **Max loss** | Defined; occurs when underlying moves sharply beyond the outer strikes |
| **Max profit** | Defined; highest between the middle and the wider wing strike |
| **Trade-off** | Asymmetric risk; larger loss potential on one side funds lower net cost |
| **Common use** | Directional bias with reduced upfront debit |

</aside>

## How the structure differs from a standard butterfly

A traditional [butterfly spread](/option/) uses three strikes (buy, sell, sell, buy) in equal spacing. The Christmas tree variant splits one wing unevenly, adding a fourth leg across three rather than two strike widths. If you're bullish, you might buy calls at 100, sell calls at 105 and 110, then buy a call at 120. The result is a payoff diagram that looks lopsided—hence the name—with a wider profit zone on one side and steeper loss on the other.

The asymmetry is intentional. By abandoning the butterfly's symmetry, you reduce the net debit (or increase the net credit, if run as a put tree) and accept unequal downside and upside risk. Traders favour this when they have a directional lean or want cheaper access to the underlying's expected range.

## Why the cost structure appeals to traders

A standard butterfly nets zero or a small credit because you are buying and selling equal quantities at the extremes. The Christmas tree sacrifices this balance to change the economics. If you build it as a call tree with more space on the upside, you pay less initially—sometimes just a few cents per share—because the wider short calls fund most of the long call purchases.

This lower entry cost broadens the practical range of strikes you can use. In choppy or tight margin environments, that efficiency matters. You are also naturally long gamma in the narrow middle zone, meaning you profit from volatility compression near the body strikes once the position is placed.

## Profit zones and typical scenarios

Suppose the stock trades at 50, and you structure a bullish call tree: buy the 50 call, sell two 52 calls, buy the 55 call. If the stock stays between 52 and 55 at expiration, you capture maximum profit—say, $1.50 per share. If it rallies past 55, losses start to mount, capped when the short 52 calls lose more than the long 50 call gains. If it crashes below 50, your loss is the net debit paid upfront, but that loss is smaller than a standard butterfly's, leaving room for tighter stops.

The inflection points shift based on which wing you widen. A bullish tree with the upper wing wider profits most if the stock stays in a band and then drifts higher, but tolerates a deeper loss below the lower short strike. A bearish version (using puts, or inverting calls) flips this: bigger profit zone lower, steeper loss above.

## Volatility and time decay effects

Christmas tree spreads benefit moderately from [time decay](/option/) working in your favour—the short calls erode faster than the long ones initially—but this advantage diminishes as expiration nears and the position approaches the flat zones. [Implied volatility](/implied-volatility/) increases benefit the long calls and harm the short calls, so you are roughly neutral to a volatility spike; you don't gain the pure vega long of a call spread, nor the pure short vega of a naked short.

Traders often enter these when they expect low volatility. The wider wing also gives you some breathing room if you want to roll the position into the next month without locking in an immediate loss, though the asymmetry complicates adjustments.

## Adjustments and practical management

Because one wing is larger, the risk is not symmetrical. If the underlying shoots through the wide wing, you can't simply let the spread expire for max profit; you will take losses. Many traders monitor the wider side more carefully and are ready to close or roll that wing if the underlying threatens the long strike.

A common adjustment is to roll the untested wing further out, extending the profit zone, though this extends time and introduces new [counterparty risk](/counterparty-risk/). Some traders simply accept the defined max loss and focus on hitting the profit zone; others use it as a hedge component in a larger portfolio.

## When to use this instead of simpler spreads

The Christmas tree is more complex than a [call spread](/option/) or standard butterfly, so it suits traders who understand [option Greeks](/option/) and want fine-grained control over their risk shape. It is particularly useful when you are slightly directional but want to keep upfront cost minimal—perhaps you have a bias that the stock stays flat or drifts one way, but you don't want to outlay much capital. The asymmetry also works well in low-volatility periods when you expect the stock to stay in a defined range.

It is less useful if you are highly directional; a simple call or put spread is clearer and requires fewer moving parts. It is also less suitable in high-volatility environments where the short calls and puts can get challenged quickly, turning your defined loss into a real and painful one.

## See also

<div class="wiki-seealso">

### Closely related

- [Butterfly Spread](/butterfly-spread/) — the three-strike symmetrical parent strategy
- [Condor Spread](/condor-spread/) — a four-strike variant with wider middle band
- [Broken Wing Butterfly](/broken-wing-butterfly/) — asymmetric butterfly using unequal wing widths
- [Skip-Strike Butterfly](/skip-strike-butterfly/) — butterfly variant with a gap between body and wing
- [Call Option](/call-option/) — long call used in the structure
- [Covered Call](/covered-call/) — simple two-leg short call strategy for comparison
- [Spread](/option/) — overview of multi-leg option strategies
- [Time Decay](/time-decay-theta/) — how extrinsic value erodes, aiding short legs

### Wider context

- [Option](/option/) — foundational instrument
- [Strike Price](/strike-price/) — the price levels that define each leg
- [Option Greeks](/option/) — delta, gamma, theta, vega guide position behaviour
- [Implied Volatility](/implied-volatility/) — affects option pricing and spread payoff

</div>

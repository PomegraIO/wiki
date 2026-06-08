---
title: "Skip-Strike Butterfly"
description: "A butterfly variant where one wing skips a strike between the body and the long option, creating directional bias and altered payoff characteristics."
keywords:
  - option strategies
  - butterfly variants
  - directional spreads
  - skip strikes
  - gap-strike trading
image: "/svg/derivatives.svg"
---

*A **skip-strike butterfly** is a [butterfly spread](/butterfly-spread/) variant where the long option in one wing is placed one or more strikes further out, creating a gap between the short and long strike. This gap produces directional bias and shifts the profit zone, allowing traders to reduce cost while accepting asymmetric risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Skip-Strike Butterfly — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A butterfly with a gap in one wing, creating directional tilt and altered economics.</div>

|   |   |
|---|---|
| **What it is** | A three-leg [option](/option/) spread with one wing featuring a skipped strike |
| **Also called** | Gap butterfly, skipped butterfly, skip-strike spread |
| **Setup** | Buy 1 call/put, sell 2 calls/puts, buy 1 call/put with a gap in the upper or lower wing |
| **Max profit** | Defined; typically at or near the short strike |
| **Max loss** | Defined but often larger on the gapped side |
| **Net cost** | Lower than standard butterfly due to reduced long-call value |
| **Common use** | Directional bias, reduced entry cost, defined risk with skew |

</aside>

## The structure: introducing the gap

A standard [butterfly spread](/butterfly-spread/) uses three consecutive strike intervals—say, 100 call, 105 call, 110 call. A skip-strike butterfly inserts a gap in one wing. Instead of buying the 110 call, you buy the 115 call, leaving the 110 strike untraded. This gap is where the directional bias comes in: you are no longer neutral between two sides; you are betting that the underlying won't end up in the skipped zone.

The gap can be a single skip (one strike omitted) or multiple skips, though single skips are most common. The gap can also be in the lower wing (buying the 95 instead of the 100) or the upper wing; the direction of the gap determines whether you are biased up or down.

## Why traders skip strikes: the cost benefit

Skipping a strike lowers the cost of the long option. If the 110 call costs $1.50 but the 115 call costs $0.50, swapping one for the other saves you $1 per share. This saving flows straight to your net cost (debit) or, in a credit structure, increases your net credit. You are essentially buying less protection in the outer wing—you are unhedged between 110 and 115—in exchange for lower upfront cost.

This cost efficiency is the core appeal. A standard butterfly might cost you $2 to set up; a skip-strike variant might cost only $0.50 or even earn you a credit. The tradeoff is that your max loss on the gapped side rises by the amount you saved.

## Directional positioning and profit zones

If you build a bullish skip-strike butterfly with a gap in the upper wing (buy 100, sell 105, sell 105 again, buy 115), you are implicitly betting that the stock won't settle between 110 and 115. If it does, you are underwater. The profit zone is now shifted: max profit is no longer at the short strike (105) but somewhere between 105 and 110, since the 115 call is still worthless there. If the stock rallies past 110, you start losing money because the 115 long call doesn't kick in until 115.

A bearish version flips this: gap in the lower wing (buy 115, sell 110, sell 110, buy 105) bets the stock won't settle between 105 and 110. Your profit zone shifts lower, and losses accelerate if the stock rallies into the gap.

## Greeks and volatility interaction

The skip-strike butterfly is short [gamma](/option/) across the entire position (like a standard butterfly), but the gamma is not evenly distributed. Near the gap, gamma is steeper because you have less long optionality to cushion sharp moves. This means the position is more sensitive to volatility spikes in the gap zone.

[Theta](/option/) decay still favors you, since the short calls erode faster than the long calls overall. However, the savings from the lower long-call cost means your theta is also smaller in dollar terms. You are trading theta payoff for cost efficiency and directional bias.

[Implied volatility](/implied-volatility/) effects are asymmetric. If the underlying approaches the gap from the unfavourable side, a volatility spike can accelerate your losses because the skipped strikes have no offsetting long options to appreciate. This makes skip-strike butterflies riskier in volatile markets or around earnings announcements.

## Practical payoff scenarios

Suppose the stock is at 100 and you build a bullish skip-strike call butterfly: buy 100 call ($3), sell 105 call ($1.50 each), buy 115 call ($0.25). Your net cost is $3 − $1.50 − $1.50 + $0.25 = $0.25 per share.

If the stock closes at 105, both calls expire worthless and you profit $0.25 (your max profit). If it closes at 110, the 100 and 105 calls are in the money, but the 115 call is still out of the money, so your profit is $5 (100–105 spread gain) + $0 (105–115 spread loss) − $0.25 (cost) = $4.75. If it closes at 115, you break even: $5 from the lower spread, −$0 from the upper spread (now 115, not the gap), and −$0.25 cost. If it closes at 120, you lose: $5 gain on lower spread, −$5 loss on upper spread, −$0.25 cost = −$0.25 total loss.

The gap zone (110–115) is where you suffer most. If the stock closes at 112, you have $5 from the lower spread and lose $0 from the upper spread (115 long is still out of the money), so you make $5 − $0.25 = $4.75 profit. Actually, you make profit nearly all the way up to the gap. But once in the gap, losses are capped at the width of the gapped strike distance.

## Adjustments and management

Many traders don't hold skip-strike butterflies to expiration, especially once the underlying approaches the gap. If the underlying nears the gap, the position is often closed to lock in profit and avoid the sharp loss that the gap can deliver.

Some traders use the skip-strike as a semi-directional hedge: they hold the narrow-wing side to expiration for max profit odds, but close the wide-wing side early if the underlying threatens it. This converts the strategy into a managed position rather than a fire-and-forget one.

## When skip-strikes make sense

Skip-strike butterflies suit traders with moderate directional conviction and tight budgets. They are useful when you want the defined-risk profile of a butterfly but don't want to outlay much capital. They also suit environments where volatility is expected to be low and the underlying is expected to stay out of the gap zone.

They are risky if you are wrong about the underlying's direction or if volatility spikes sharply, since the gap leaves you with no long option hedge. They are also less suitable for neutral traders, since the directional asymmetry means you are betting against one outcome. Finally, they demand careful attention to the likely settlement zone; a gap that seems safe in backtest can feel dangerous in real time when the stock approaches it.

## See also

<div class="wiki-seealso">

### Closely related

- [Butterfly Spread](/butterfly-spread/) — the standard three-strike parent
- [Christmas Tree Spread](/christmas-tree-spread/) — asymmetric three-strike variant
- [Broken Wing Butterfly](/broken-wing-butterfly/) — unequal-width butterfly
- [Condor Spread](/condor-spread/) — four-strike wide-band version
- [Call Option](/call-option/) — component of the spread
- [Vertical Spread](/option/) — simpler two-strike reference point
- [Strike Price](/strike-price/) — why gaps between them matter
- [Bid-Ask Spread](/bid-ask-spread/) — affects entry/exit economics

### Wider context

- [Option](/option/) — foundational instrument
- [Option Greeks](/option/) — delta, gamma, theta, vega guide position behaviour
- [Implied Volatility](/implied-volatility/) — affects risk profile and entry timing
- [Time Decay](/time-decay-theta/) — benefits short legs
- [Market Volatility](/historical-volatility/) — affects payoff realization

</div>

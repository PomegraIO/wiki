---
title: "Broken Wing Butterfly"
description: "An asymmetric butterfly spread with unequal wing widths that shifts risk to one side and reduces or eliminates upfront cost."
keywords:
  - option strategies
  - butterfly variants
  - asymmetric spreads
  - credit spreads
  - directional bias
image: "/svg/derivatives.svg"
---

*A **broken wing butterfly** is a [butterfly spread](/butterfly-spread/) variant where the two wings have different widths, creating an asymmetric profit-and-loss profile. By narrowing one wing and widening the other, traders can reduce the net cost (or earn a credit) while accepting larger risk on the expanded side in exchange for more profit potential on the narrow side.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Broken Wing Butterfly — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">An asymmetric butterfly using unequal wing widths to shift risk and reduce cost.</div>

|   |   |
|---|---|
| **What it is** | A three-strike [option](/option/) spread with unequal distance from body to wings |
| **Also called** | Unequal butterfly, skewed butterfly, call/put ratio spread |
| **Setup** | Buy 1 call/put, sell 2 calls/puts, buy 1 call/put at strikes with unequal spacing |
| **Max profit** | Defined; located at the body strike |
| **Max loss** | Defined but asymmetric; larger on the wide-wing side |
| **Net cost** | Often zero or a small credit; efficiency gained by abandoning symmetry |
| **Common use** | Directional bias with defined risk; premium selling with cost reduction |

</aside>

## How the broken wing differs from a standard butterfly

A traditional [butterfly spread](/butterfly-spread/) uses three strikes equally spaced—say, 100, 105, 110—and buys at the outer strikes while selling at the inner strikes (or vice versa). The profit zone is a narrow peak at the middle strike, and losses are identical on both sides.

A broken wing butterfly breaks that symmetry. You might buy at 100, sell at 105, and buy at 115 instead of 110. The lower wing (100 to 105) is only 5 points wide, while the upper wing (105 to 115) is 10 points wide. This asymmetry is the whole point: the narrow wing keeps cost low, while the wide wing reduces the net debit (or even generates a credit) and shifts risk.

## The economics: cost reduction through asymmetry

The standard butterfly requires equal capital outlay on both sides. The broken wing rearranges this. If you buy the 100 call for $2, sell the 105 call for $4, sell the 105 call (second one) for $4, and buy the 115 call for $1, your net cost is $2 + $1 − $4 − $4 = −$5, meaning you *receive* $5 per share as a credit.

This credit is the payoff for accepting unequal risk. In a broken wing, if the stock falls sharply, you lose money on the wide wing (you collect only $10 of the maximum $10 width, but you paid $1, a profit of $9). If the stock rallies sharply, you can lose much more on the wide wing (up to $10 in loss) while only gaining $5 on the narrow wing. The asymmetry favours the direction you are *not* betting on heavily, so you must choose your bias carefully.

## Directional bias in practice

Traders typically use broken wings when they are slightly directional but want the credit and defined risk that a butterfly offers. A bullish broken wing might narrow the downside wing and widen the upside wing. This setup earns a credit if the stock stays flat and profits modestly if it rises slightly. If it crashes, you lose on the narrow wing quickly, but the crash risk is capped. If it soars, losses mount on the wide wing, but you've already pocketed a credit that offsets some of that loss.

Conversely, a bearish broken wing (using puts, or inverted calls) reverses this: you narrow the upside wing and widen the downside wing, setting yourself up to profit if the stock falls or stays flat, with large losses only if it rallies sharply.

## Profit zones and maximum risk

Unlike a standard butterfly, which has a narrow profit peak and then symmetric losses on both sides, a broken wing has lopsided profit and loss zones. The max profit is still located at the middle (short) strike, but the profit zone is wider on one side and narrower on the other. The max loss is also asymmetric: smaller on the narrow-wing side and larger on the wide-wing side.

Calculating the exact max loss requires careful attention to the widths. If the lower wing is 5 points and the upper wing is 10 points, and you received a net credit of $5, then your max loss on the downside is $5 (the width of the narrow wing) minus the credit, and your max loss on the upside is $10 (the width of the wide wing) minus the credit. The two are not equal, so you must manage the position differently on each side.

## Volatility and time decay

Like a standard butterfly, a broken wing benefits from [time decay](/time-decay-theta/); the short calls (or puts) erode faster than the long ones, handing you profit as days pass. Your [theta](/option/) is positive if you entered the position as a net debit; if you entered as a net credit, your theta is negative (time works against you), but the credit you pocketed upfront provides a buffer.

[Implied volatility](/implied-volatility/) effects are roughly neutral in the body, but skewed toward the wide wing. If volatility spikes, the wide wing's long option appreciates more than the narrow wing's long option, which can either help or hurt depending on where the underlying is trading and your directional bias.

## Adjustments and risk management

The asymmetric risk demands careful monitoring. Many traders don't let a broken wing run all the way to expiration; they close it early if it hits max profit or if the underlying threatens the wide wing. Early exit preserves time value and reduces the chance that a gap move will turn a defined loss into a catastrophic one.

If the underlying moves toward the wide wing, some traders will roll that wing further out, extending protection but also committing more time and capital to the trade. Others simply close the position and take the loss, accepting that the broken wing didn't work as expected for that particular market environment.

## When to use broken wings

Broken wings are attractive when you have a moderate directional bias and want to harvest premium without paying upfront. They suit traders who are comfortable with asymmetric risk profiles and understand that the wide wing can be a real source of loss if the underlying moves sharply that direction. They are also useful in low-volatility periods, where the credit you collect upfront and the daily theta decay give you a cushion.

They are less suitable for neutral traders, since the directional asymmetry means you are implicitly betting against one side. They are also risky in high-volatility environments or around events like earnings announcements, since a gap move can skip right through your wing strikes and leave you at max loss with no time to adjust.

## See also

<div class="wiki-seealso">

### Closely related

- [Butterfly Spread](/butterfly-spread/) — the symmetric parent strategy
- [Christmas Tree Spread](/christmas-tree-spread/) — another three-strike asymmetric variant
- [Condor Spread](/condor-spread/) — four-strike wide-band version
- [Skip-Strike Butterfly](/skip-strike-butterfly/) — butterfly with a gap between body and wing
- [Call Option](/call-option/) — component of the spread
- [Put Option](/put-option/) — used in bearish variant
- [Vertical Spread](/option/) — simpler two-strike reference point
- [Time Decay](/time-decay-theta/) — benefits short legs over time

### Wider context

- [Option](/option/) — foundational instrument
- [Strike Price](/strike-price/) — the three strikes that define payoff
- [Implied Volatility](/implied-volatility/) — affects edge on entry and exit
- [Option Greeks](/option/) — delta, gamma, theta, vega guide position behaviour
- [Bid-Ask Spread](/bid-ask-spread/) — affects entry/exit cost and slippage

</div>

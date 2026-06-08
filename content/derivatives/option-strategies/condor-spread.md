---
title: "Condor Spread"
description: "A four-strike option strategy that profits when the underlying stays within a wide middle band, combining elements of vertical spreads and butterflies."
keywords:
  - option strategies
  - four-strike spreads
  - range-bound trading
  - vertical spreads
  - credit spreads
image: "/svg/derivatives.svg"
---

*A **condor spread** is a four-strike [option](/option/) strategy that profits when the underlying asset stays within a broad target range. It combines two vertical spreads into a single position, creating a flatter profit zone than a [butterfly](/butterfly-spread/) and lower upfront cost in exchange for more capital at risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Condor Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A four-strike spread with a wide, profitable middle band between inner and outer strikes.</div>

|   |   |
|---|---|
| **What it is** | A multi-leg [option](/option/) spread using four options at four different strikes |
| **Also called** | Iron condor (when mixing puts and calls), call condor, put condor |
| **Setup** | Buy 1 call (or put), sell 1 call, sell 1 call, buy 1 call (or equivalent put structure) |
| **Max profit** | Defined; earned if underlying stays between the two inner short strikes |
| **Max loss** | Defined; occurs if underlying moves beyond either outer strike |
| **Profit zone** | Wide band between the sold strikes; flatter than butterfly |
| **Common use** | Range-bound markets, low-volatility periods, income generation |

</aside>

## The structure: two vertical spreads merged

A condor spread is built by stacking two [vertical spreads](/option/) together. If bullish, you might sell a call spread at strikes 100–105, then buy a call spread at 110–115. The result: buy the 100 call, sell the 105 call, sell the 110 call, buy the 115 call. Your profit zone sits in the middle—between 105 and 110—where all four legs expire worthless (or finish in-the-money with specific payoffs that net to max profit).

Unlike a butterfly, which uses three strikes and has a narrow peak, the condor uses four strikes and creates a wide, flat-topped profit band. This is the core appeal: there is more room for the underlying to move and still land you near maximum profit. A [butterfly spread](/butterfly-spread/) might be profitable only in a $2 range; a condor might be profitable across a $5 range.

## Why the wider middle band matters

The flatter profit zone reduces the precision demanded of your timing and directional sense. If you sell a butterfly and the stock moves just 0.5% beyond your intended zone, losses mount quickly. With a condor, that same move leaves you still in profit or close to it. This makes condors popular in markets where the underlying is choppy or where historical volatility is moderate—you aren't betting on pinpoint accuracy.

The wider band also lowers margin requirements, since you are holding two separate defined-loss vertical spreads rather than a tightly wound butterfly. Brokers often treat the inner short strikes as the risk measure, freeing up margin compared to the full max-loss width that a butterfly consumes.

## The iron condor variant

A common form is the **iron condor**, which uses calls above the current [strike price](/strike-price/) and puts below, capturing premium from both sides. If the stock is at 100, you might sell the 95 put, buy the 90 put, sell the 105 call, and buy the 110 call. If the stock stays between 95 and 105, both spreads expire worthless and you pocket the net credit received upfront.

Iron condors are popular for income strategies because they generate a cash inflow on initiation, rather than requiring a debit. You profit immediately if volatility contracts and the stock stays calm, making them appealing in low-volatility periods or when you are slightly bullish to neutral.

## Profit and loss mechanics

Suppose you sell a call condor with strikes at 100, 105, 110, 115, each one month to expiration. You collect a net credit of $1 per share ($2 from the 100–105 spread minus $1 cost of the 110–115 spread). Max profit is $1 per share if the stock closes between 105 and 110. Max loss is also defined: if the stock soars past 115, both calls are deep in the money and the position loses $4 (the width of the outer spread) minus the $1 credit you pocketed, for a net loss of $3.

The symmetry is convenient: max profit and max loss are both locked in at initiation. You can calculate your return on risk and make a quick go-no-go decision. This clarity is partly why condors appeal to retail traders; you don't have to guess the Greeks or imagine tail scenarios.

## Greeks and volatility interactions

A long condor (where you pay a debit) benefits from [time decay](/time-decay-theta/); the sold calls and puts erode faster than the long calls and puts you own. Your theta is positive, meaning each day that passes with the stock in range hands you small profit. You are roughly [delta](/option/)-neutral near the centre of the range, so directional moves hurt you; you are short [gamma](/option/), meaning you lose if the stock swings sharply in either direction.

An iron condor flips some of these dynamics. You collect theta immediately as a credit, but you are also short [vega](/option/), meaning a spike in [implied volatility](/implied-volatility/) works against you—the sold options become more expensive, cutting into your profit. This is why iron condors are favoured when volatility is expected to fall or stay low.

## Adjustments and management

Because the profit zone is wide but defined, many traders manage their position early. If the underlying approaches one of the outer strikes, you might buy back the threatened spread to lock in profit and reduce exposure. This often costs less than waiting for expiration, especially if implied volatility spiked in response to the underlying's move.

Some traders use the condor as a baseline and then leg into adjustments. If the underlying threatens the call side, you close the call spread and keep the put spread running, converting it into a partial position. This flexibility is another reason condors are popular: they break neatly into sub-positions, allowing granular adjustments.

## When condors win and lose

Condors excel in quiet, range-bound markets where you correctly predict the upper and lower boundaries. They are ideal for mildly bullish or bearish views that don't require a big directional move. They also suit traders who want steady theta income without the complexity of managing a full straddle or strangle.

Condors struggle in trending or highly volatile markets. A sharp move in either direction can quickly turn a small loss into max loss. They also suffer if implied volatility spikes sharply; credit spreads particularly feel the pain. For this reason, many traders avoid condors during earnings announcements or macroeconomic data releases when tail risk is elevated.

## See also

<div class="wiki-seealso">

### Closely related

- [Butterfly Spread](/butterfly-spread/) — three-strike parent with narrower profit zone
- [Christmas Tree Spread](/christmas-tree-spread/) — asymmetric three-strike variant
- [Broken Wing Butterfly](/broken-wing-butterfly/) — unequal-width butterfly
- [Skip-Strike Butterfly](/skip-strike-butterfly/) — butterfly with strike gap
- [Call Option](/call-option/) — component of the spread
- [Put Option](/put-option/) — component in iron condor version
- [Vertical Spread](/option/) — the two spreads that make up a condor
- [Time Decay](/time-decay-theta/) — benefits the sold legs

### Wider context

- [Option](/option/) — foundational instrument
- [Strike Price](/strike-price/) — the four prices that define profit and loss
- [Implied Volatility](/implied-volatility/) — affects setup and adjustments
- [Option Greeks](/option/) — delta, gamma, theta, vega guide position behaviour
- [Margin Call](/margin-call-forex/) — capital required to hold the position

</div>

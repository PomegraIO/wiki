---
title: "Jade Lizard"
description: "An option strategy combining a short put with a short call spread such that the total premium collected exceeds the width of the call spread, eliminating downside risk."
keywords:
  - jade lizard
  - option spread
  - income strategy
  - limited risk
  - premium collection
image: "/svg/derivatives.svg"
---

*A **jade lizard** merges a short put with a short call spread—typically selling an out-of-the-money put while simultaneously selling an OTM call and buying a further OTM call at a wider strike. The strategy's elegant trick is that the total credit received exceeds the maximum loss from the call spread, effectively converting naked downside risk into a net-credit position with defined risk on both sides.*

## The mathematics of overcoming the call spread

Where a naked [short put](/put-option/) exposes you to theoretically unlimited downside risk (down to zero), and a [short call spread](/call-option/) caps your loss at the difference between the two strikes, a jade lizard combines them to create something more refined.

The arithmetic works like this. On a stock at $100, you might:
- Sell a $95 put for $3
- Sell a $110 call for $2
- Buy a $115 call for $0.50
- Net credit: $3 + $2 − $0.50 = $4.50

Your call spread width (the distance between the $110 call you sold and the $115 call you bought) is $5. Because you collected $4.50, your net risk on the upside is only $0.50 (the $5 width minus the $4.50 credit). On the downside, the short $95 put creates theoretically unlimited loss, but it's offset by the $4.50 you pocketed—your breakeven on the put side is $90.50.

The name "jade lizard" may evoke a tropical reptile, but the strategy is named for the shape of its profit diagram: a wide, flat plateau of profit from the downside breakeven up to the lower call strike, then a sloped decline as the short call moves into-the-money.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Jade Lizard — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A short put paired with a short call spread, where the credit covers the call risk.</div>

|   |   |
|---|---|
| **Max profit** | Total credit collected |
| **Max loss (upside)** | Call spread width − total credit |
| **Max loss (downside)** | Put strike − total credit (capped by stock going to zero) |
| **Breakeven (upside)** | Short call strike + credit |
| **Breakeven (downside)** | Short put strike − credit |
| **Risk ratio** | Asymmetric; downside risk > upside risk in typical setup |
| **Capital requirement** | Margin tied to the larger of the two risks |
| **Implied volatility** | Benefits from IV expansion at entry, hurt by IV collapse |

</aside>

## Why the asymmetry matters

The jade lizard is not a neutral strategy; it has a built-in bullish tilt. The downside loss potential (from the put) is typically much larger than the upside loss (from the capped call spread). This makes it best suited for traders with a mild bullish outlook or for those who simply believe the underlying will not drop below a certain floor.

Conservative traders use jade lizards on quality stocks with strong support levels or companies with predictable earnings. Aggressive traders layer them on volatile assets, accepting higher downside risk in exchange for the generous credit upfront. The key decision point is whether the $95 put strike—the level where you're forced to take assignment if exercised—feels like solid support or like a dangerous assumption.

## Building blocks: choose your strikes carefully

The selection of all three strikes determines the risk-reward shape. A typical jade lizard might use strikes that are all out-of-the-money but spaced to reflect the trader's conviction:

- **Tight setup**: Sell $98 put, $102 call, $105 call. Lower credit but smaller losses.
- **Aggressive setup**: Sell $90 put, $110 call, $115 call. Higher credit but severe downside risk.

The gold standard jade lizard collects enough credit that the call spread is nearly risk-free. If you can sell the put and call spread for a net credit that equals or exceeds the call spread width, you've achieved the ideal: both sides capped at zero loss theoretically (though downside risk remains if the stock tanks).

Some traders adjust the put strike to be closer to the current price (more in-the-money) to collect higher premium, accepting steeper downside risk. Others push the put far out-of-the-money to reduce downside exposure, accepting a thinner credit.

## Comparison to other multi-leg spreads

A [covered call](/covered-call/) sells a call against a long stock, capping upside and generating income but leaving downside naked. A jade lizard caps both sides, though with asymmetric risk. A [short strangle](/short-strangle/) is simpler—just two legs, a short put and a short call—but offers no upside cap.

The jade lizard's advantage is definition: if you can accept the downside risk of the put, the call side is entirely contained. The disadvantage is complexity: you're managing three contracts, each with its own expiration, roll date, and assignment risk.

## Rolling and adjustment in practice

Jade lizards are often rolled before expiration. If the underlying approaches the short call strike, a trader might close both the short call and the bought call, and simultaneously sell a new call spread at higher strikes and a further expiration. This extends the trade while protecting the short call from assignment.

Similarly, if the stock nears the put strike on the downside, the trader faces a choice: take assignment (buy the stock at the put strike), close the put early and keep the call spread active, or roll the entire position. Most professionals close the put and keep the call spread, or close everything and reset.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Strangle](/short-strangle/) — sells put and call without the call spread cap
- Short Call Spread — the upside component of the jade lizard in isolation
- [Short Put](/put-option/) — the downside component in isolation
- [Reverse Jade Lizard](/reverse-jade-lizard/) — inverted structure using a short call and short put spread
- [Option Premium](/option-premium/) — the credit you collect in this three-leg trade

### Wider context

- [Call Option](/call-option/) — foundational to the call spread side
- [Put Option](/put-option/) — foundational to the short put side
- [Implied Volatility](/implied-volatility/) — affects all three legs simultaneously
- [Time Decay Theta](/time-decay-theta/) — works in your favor on all three contracts
- [Assignment](/exercise-price/) — the risk you take on all three strikes simultaneously

</div>

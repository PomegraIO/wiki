---
title: "Reverse Jade Lizard"
description: "An option strategy combining a short call with a short put spread such that the total premium collected eliminates upside risk entirely, creating a defined-risk income trade."
keywords:
  - reverse jade lizard
  - option spread
  - income strategy
  - limited risk
  - neutral to bearish
image: "/svg/derivatives.svg"
---

*A **reverse jade lizard** inverts the standard [jade lizard](/jade-lizard/) by pairing a short call with a short put spread—selling an out-of-the-money call while simultaneously selling an OTM put and buying a further OTM put at a lower strike. The total credit collected is sized so that it exceeds or equals the maximum loss from the put spread, capping both upside and downside risk and creating a neutral-to-bearish income trade.*

## Flipping the risk to the downside

The reverse jade lizard shares the three-leg elegance of its namesake but reverses the conviction. Instead of betting the stock will not fall far below current levels, you're betting it will not rally far above them—a logical choice for traders expecting a pullback or consolidation, or those who believe upside volatility is overpriced.

Consider a stock at $100. A reverse jade lizard might look like:
- Sell a $105 call for $2
- Sell a $95 put for $3
- Buy a $90 put for $0.50
- Net credit: $2 + $3 − $0.50 = $4.50

Your put spread width (the distance between the $95 put you sold and the $90 put you bought) is $5. Since you collected $4.50, your net risk on the downside is only $0.50 (the $5 width minus the $4.50 credit). On the upside, the short call creates theoretically unlimited loss, but it's offset by your $4.50 credit—your breakeven on the call side is $109.50.

The result: a position with capped loss on both sides and pure income decay as time passes. It is the downside-focused twin of the jade lizard.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reverse Jade Lizard — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A short call paired with a short put spread, where the credit covers the put risk.</div>

|   |   |
|---|---|
| **Max profit** | Total credit collected |
| **Max loss (downside)** | Put spread width − total credit |
| **Max loss (upside)** | Call strike − total credit (theoretically unlimited if uncapped) |
| **Breakeven (upside)** | Short call strike + credit |
| **Breakeven (downside)** | Short put strike − credit |
| **Risk ratio** | Asymmetric; upside risk > downside risk in typical setup |
| **Capital requirement** | Margin tied to the larger of the two risks |
| **Volatility exposure** | Benefits from falling IV, hurt by rising IV |

</aside>

## The bearish slant and positioning

Where the jade lizard tilts bullish, the reverse jade lizard tilts bearish or at minimum expects rangebound price action. It works well in markets that have run up sharply and are consolidating, or ahead of events where sentiment is decidedly bullish and implied volatility is elevated. You're betting that any further upside is modest and that the market will pull back rather than crash.

This makes the reverse jade lizard a natural fit for portfolio managers in late-stage bull markets, or for traders short-term bearish but not willing to buy [put spreads](/put-option/) outright. The income stream from the short call and short put can be substantial in high-volatility environments, and the defined risk—capped loss on the downside—provides a safety net that a naked short call never offers.

## Strike selection and risk management

As with the standard jade lizard, the art lies in choosing strikes that reflect your conviction and market conditions. A trader might use:

- **Tight setup**: Sell $103 call, $97 put, $94 put. Lower credit, smaller losses, higher probability of profit.
- **Aggressive setup**: Sell $110 call, $90 put, $85 put. Higher credit, larger losses, more leverage.

The ideal reverse jade lizard collects so much credit from the call and put that the put spread width is nearly covered. If the credit exceeds the put spread width, you achieve a rare feat: both sides of the trade are profitable at maximum loss. This happens when the put spread is far out-of-the-money and the short call is right at the current price or slightly above it.

Most reverse jade lizards in practice do not achieve perfect symmetry. The trader usually accepts larger downside loss potential (the put spread) in exchange for a call strike that is closer to the current price, where selling is more profitable. This asymmetry is a feature, not a bug—it matches the trader's view that downside is less risky than upside.

## Volatility and the timing problem

Reverse jade lizards suffer when implied volatility spikes. Both the short call and the short put lose value to IV expansion, and the position can move against you sharply. Conversely, if IV collapses—which often happens during a strong rally—the position benefits immediately.

This means reverse jade lizards are best entered when IV is at or above the median, not at extremes. Entering one just before a volatility crush (such as a successful earnings announcement on a heavily shorted stock) can mean the short call and short put both lose value faster than anticipated, and you may be forced to roll or close early to capture the decay.

## Rolling and assignment navigation

As expiration nears, both the call and the put spread face assignment. Most professionals close a reverse jade lizard 7–14 days before expiration, taking profit without sweating the final days. Some roll the entire position forward—closing all three legs and immediately selling new ones at wider strikes and a further expiration.

Rolling the call is straightforward: buy it back and sell a new one further out. Rolling the put spread is trickier: you must close both the short and long puts, then immediately sell a new pair at a lower strike and further expiration. Done smoothly, rolling extends the income stream indefinitely.

## Comparison to standard short spreads and naked selling

A naked [short call](/call-option/) generates the most income but exposes you to unlimited upside loss. A short call spread caps that loss at the strike width but requires paying for the long call. A reverse jade lizard uses the short put sale to subsidize the long call, often eliminating its cost entirely.

The tradeoff: you now own downside risk from the short put spread. If the stock crashes, this position suffers. If it rallies modestly and then consolidates, it shines. For traders with strong conviction that a rally has run its course, the reverse jade lizard is one of the sharpest tools in the options arsenal.

## See also

<div class="wiki-seealso">

### Closely related

- [Jade Lizard](/jade-lizard/) — the bullish mirror, pairing a short put with a short call spread
- Short Call Spread — the upside component in isolation
- [Short Put Spread](/put-option/) — the downside component in isolation
- [Short Strangle](/short-strangle/) — simpler two-leg alternative without defined risk on both sides
- [Option Premium](/option-premium/) — the credit from all three legs in this trade

### Wider context

- [Call Option](/call-option/) — foundational to the short call side
- [Put Option](/put-option/) — foundational to the short put spread side
- [Implied Volatility](/implied-volatility/) — simultaneous impact on call and put premiums
- [Time Decay Theta](/time-decay-theta/) — your daily friend as all three legs decay
- [Assignment](/exercise-price/) — looming on all three strikes at expiration

</div>

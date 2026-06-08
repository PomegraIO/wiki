---
title: "Short Strangle"
description: "An option strategy selling out-of-the-money calls and puts at different strikes to collect premium while accepting defined risk if the underlying moves sharply."
keywords:
  - short strangle
  - income strategy
  - premium collection
  - option spread
  - directional neutral
image: "/svg/derivatives.svg"
---

*A **short strangle** pairs a short out-of-the-money call with a short out-of-the-money put at different strikes, collecting premium in exchange for unlimited loss potential if the asset moves far enough in either direction. It is the mirror of the [long strangle](/long-strangle/) and one of the most popular income-generating option trades for investors who believe volatility is overpriced.*

## Selling volatility for cash today

The short strangle inverts the logic of its long cousin. Instead of paying premium to bet on a big move, you pocket premium by betting the underlying will stay within a range. You sell a call above the current price and a put below it, both out-of-the-money, and keep the difference if neither side gets exercised.

On a stock at $100, you might:
- Sell one $110 call for $2
- Sell one $90 put for $1.50
- Total credit: $3.50

Your maximum profit is capped at the $3.50 you collected upfront. Your maximum loss is theoretically unlimited on the upside (the stock could rally to $150 and your short call obligation is unlimited) and technically unlimited on the downside (though limited by the stock going to zero). Breakevens sit at $113.50 on the upside and $86.50 on the downside—the same levels as the long strangle, but with opposite payoffs.

This is why short strangles appeal to portfolio managers and traders with high conviction that markets are fairly or overvalued at the moment. You're essentially saying: "I think this stock will not move more than this much in the next 30–45 days, and I'm willing to get paid for that opinion."

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Short Strangle — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Earn premium by betting the underlying stays within a two-sided range.</div>

|   |   |
|---|---|
| **Max profit** | Total premium collected |
| **Max loss** | Unlimited upside; theoretically unlimited downside |
| **Entry credit** | Narrower range = lower credit; wider range = higher credit |
| **Breakeven (upside)** | Call strike + total premium |
| **Breakeven (downside)** | Put strike − total premium |
| **Directional view** | Neutral; expects low volatility or range-bound price |
| **Time decay effect** | Works in your favour each day |
| **Margin requirement** | Higher than spreads; caps at largest strike gap |

</aside>

## Why margin and risk become front-and-centre

Running a short strangle is not a "free money" trade, despite collecting premium immediately. Brokers require substantial margin—usually the width of your call strike gap (say $10 on a $100/$110 strangle), capped at the width of the widest risk. This margin ties up capital and exposes you if the underlying gaps sharply on earnings or a black swan event.

The true cost emerges on the downside during a market selloff. A short put is often painfully profitable to own. If the market drops 20% overnight, your $90 put becomes deep in-the-money and forces you either to sell cash secured to cover the loss or buy back the short at a much higher price. Similarly, a short call becomes a liability in a sharp rally.

This is why successful short strangle traders focus obsessively on position sizing. A single short strangle on a volatile stock can wipe out weeks or months of premium gains in a single gap move. Professional traders typically lay off strangles on assets with high [realized volatility](/historical-volatility/) but low [implied volatility](/implied-volatility/)—situations where IV is overestimated relative to actual market movement.

## The relationship between width and reward

A tighter strangle (closer strikes) collects less premium but requires a smaller move to hit breakeven and blow up the position. A wider strangle collects more premium because you're accepting larger risk. The trader's job is matching the width to the underlying's typical daily and weekly moves and to the coming catalysts.

Before earnings, implied volatility usually expands, which is bad for a short strangle seller (your shorts become more expensive to close). After earnings, IV collapses, which is excellent for you—even if the stock moved, your short options lose value rapidly and can be closed profitably. Many short strangle traders enter weeks before an event, collect premium in the runup, and close early after the event posts, avoiding the gamma and assignment risk of holding through the final days.

## Comparison to a short straddle and risk management

A [short straddle](/short-straddle/) sells a call and put at the same strike, collecting more premium but demanding less movement on either side to blow up. A short strangle accepts a wider range in exchange for lower cost and slightly lower profit. If you believe volatility is moderately overpriced, the strangle is more forgiving; if you think it's massively overpriced, the straddle pays better—at the cost of higher risk.

Defensive traders often pair short strangles with stop-loss rules or defined spreads. Instead of naked short calls and puts, a trader might sell a $110 call and buy a $115 call, capping upside loss to $5 minus the credit received. This collar transforms the position into a defined-risk spread, trading unlimited profit for certainty.

## Assignment and the last-minute scramble

As expiration approaches, short options that are slightly in-the-money face assignment risk. You might get assigned on the put (forced to buy the stock) or the call (forced to sell it), especially on dividend or ex-date days. Most traders close short strangles by rolling them forward—closing the expiring position and opening a new one a month or two out—rather than sweating out the final day.

Rolling extends the trade indefinitely. Traders will close both the near-term call and put, and simultaneously sell a new pair at wider strikes and a further expiration. This locks in profit or cuts losses without taking assignment, and the income stream becomes semi-permanent.

## See also

<div class="wiki-seealso">

### Closely related

- [Long Strangle](/long-strangle/) — mirrors this trade, buying OTM calls and puts for volatility exposure
- [Short Straddle](/short-straddle/) — sells at-the-money options, higher profit and higher risk
- [Covered Call](/covered-call/) — sells calls against a long stock position; often paired with put sales
- [Protective Put](/protective-put/) — buys downside protection; opposite philosophy to short puts
- [Option Premium](/option-premium/) — what you collect upfront in a short strangle

### Wider context

- [Implied Volatility](/implied-volatility/) — the overpriced vol you're betting against
- [Time Decay Theta](/time-decay-theta/) — your daily friend in this position
- [Gamma Risk](/gamma-risk/) — acceleration of losses if the underlying gaps past your breakeven
- [Margin Call](/margin-call-forex/) — the leverage that can force you to close before you're ready
- [Assignment](/exercise-price/) — what happens if your short options expire in-the-money

</div>

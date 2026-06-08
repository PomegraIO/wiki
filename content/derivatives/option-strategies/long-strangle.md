---
title: "Long Strangle"
description: "An option strategy buying out-of-the-money calls and puts at different strikes to profit from volatility while limiting upfront cost below a straddle."
keywords:
  - long strangle
  - volatility strategy
  - option spread
  - otm options
  - straddle alternative
image: "/svg/derivatives.svg"
---

*A **long strangle** pairs a long out-of-the-money call with a long out-of-the-money put at different strikes, betting that the underlying asset will move far enough in either direction to overcome the combined premium paid. The strategy trades narrower profit zones for cheaper entry than a [straddle](/straddle/), making it a refined bet on [volatility](/volatility-smile/) rather than an all-or-nothing directional play.*

## When the wings are wider, the cost drops

The mechanical appeal of a long strangle lies in its asymmetry. You buy a call above the current price and a put below it—both out-of-the-money. Because these options have less intrinsic value than at-the-money equivalents, you pay less total premium than you would for a [long straddle](/long-straddle/), which uses both legs at-the-money.

The tradeoff: your breakeven points sit further from the current price. With a straddle, you need movement of only the combined premium paid. With a strangle, you need movement plus the gap between strike and current price on whichever side gets tested. That wider margin of safety comes at the cost of needing larger moves to profit.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Long Strangle — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Buy volatility cheaply by placing both legs out-of-the-money.</div>

|   |   |
|---|---|
| **Max profit** | Unlimited upside; large downside |
| **Max loss** | Total premium paid |
| **Entry cost** | Lower than [long straddle](/long-straddle/) |
| **Breakeven (upside)** | Call strike + total premium |
| **Breakeven (downside)** | Put strike − total premium |
| **Directional view** | Neutral; expects volatility surge |
| **Time decay effect** | Works against you until expiration |
| **Implied volatility** | Profits if IV expands |

</aside>

## The setup: strikes, premiums, and ratio trades

A practical long strangle on a stock trading at $100 might look like:
- Buy one $110 call for $2
- Buy one $90 put for $1.50
- Total debit: $3.50

Upside breakeven: $110 + $3.50 = $113.50. You profit if the stock rallies past that level. Downside breakeven: $90 − $3.50 = $86.50. You profit if it falls below that.

The strike selection is the lever. Wider spacing (say $105/$95 calls and puts) costs less but requires larger moves. Tighter spacing narrows the cost difference versus a straddle but demands less room. Sophisticated traders also run ratio strangles—buying multiple calls and puts in unequal quantities—to fine-tune the cost basis or cap risk on one side.

Traders often enter strangles ahead of earnings or macro events expected to trigger sharp moves, banking on implied [volatility](/volatility-smile/) expanding as uncertainty peaks. Once the event passes and IV collapses, the position can turn sour even if the stock moved, because the option premiums have shriveled.

## Time decay is an enemy until you're proven right

A long strangle bleeds value if the underlying drifts sideways. Each day, [theta](/time-decay-theta/) erodes both the call and put. The position is most painful during the final weeks before expiration if the stock has hugged its original level—you've paid premium for a move that hasn't arrived.

This is why strangle buyers typically target known catalysts or anticipate sustained elevated volatility. A trader holding a strangle for weeks on a flat stock is fighting theta; a trader holding it through earnings or a central bank decision is fighting for a big enough price spike to overcome time decay. Closing early—before IV collapses and theta accelerates—is often smarter than holding to expiration.

## Comparing the strangle to its cousins

The long straddle costs more upfront because both legs are at-the-money, but breakevens sit closer to the entry price—you need less movement to profit. The long strangle costs less but demands bigger moves. A [long stradddle](/long-straddle/) shines when you expect volatility to surge around your entry point; a strangle is for traders who can afford to be patient and accept a slower path to profit if the move is large enough.

A protective collar using a put and call for hedging is a different animal altogether: it's designed to cap losses on a long stock position. A strangle is pure speculation on volatility, independent of any underlying holding.

## The psychology: greedy or prudent?

Buying a cheaper strangle instead of a straddle appeals to portfolio managers and speculators with limited capital. You can own more positions on the same margin, or own the same number of strangles instead of straddles and keep cash free.

The flip side: if volatility sinks before it rises—a common market pattern after uncertainty eases—the position loses money faster than you'd lose on a straddle, because you started with less extrinsic value. The strangle is not "cheaper and better"; it's a different risk profile.

## See also

<div class="wiki-seealso">

### Closely related

- [Long Straddle](/long-straddle/) — buys call and put at the same strike for maximum volatility exposure at higher cost
- [Short Strangle](/short-strangle/) — mirrors this trade, selling OTM calls and puts to collect premium
- [Straddle](/straddle/) — foundational at-the-money volatility strategy
- [Option](/option/) — core building block of all volatility spreads
- [Implied Volatility](/implied-volatility/) — the key driver of option prices and strangle profitability

### Wider context

- [Volatility Smile](/volatility-smile/) — why OTM options have different implied volatilities
- [Time Decay Theta](/time-decay-theta/) — the erosion that works against long option positions
- [Strike Price](/strike-price/) — the critical choice that separates strangle legs
- [Expiration Date](/expiration-date/) — when your bet must have paid off or be closed

</div>

---
title: "Strip Strategy"
description: "A volatility options strategy buying two put options and one call at the same strike to profit from large moves with downside bias."
keywords:
  - strip strategy
  - option strategy
  - volatility
  - leverage
  - derivatives
image: "/svg/derivatives.svg"
---

*A **strip strategy** is a bearish [volatility](/implied-volatility/) [options](/option/) position in which an investor buys two at-the-money or slightly out-of-the-money [put options](/put-option/) and one [call option](/call-option/) at the same strike price on the same underlying asset and expiration date. The strategy profits from large price swings in either direction but is skewed toward bearish moves and offers unlimited downside profit potential.*

## The payoff structure: unlimited down, limited up

A strip's payoff mirrors a [strap](/strap-strategy/) but with the bias reversed. If the underlying falls sharply below the strike, both puts gain value and produce unlimited profit. If it rises sharply, the call gains value, but only one call caps that profit.

Consider a strip where you buy two puts and one call, each at a $100 strike. If the stock falls to $90, each put gains $10 of intrinsic value (for $2,000 total profit, minus premium paid). If it rises to $110, the call gains $10 intrinsic value (for $1,000 profit from the call), but you've lost the premium paid for the two puts.

This asymmetry is intentional: the strategy bets that if a large move occurs, it will be downward. The extra long put acts as an amplifier for bearish moves and as a loss limiter for bullish ones.

## When and why traders use strips

Strips are deployed when traders expect an imminent large move but lean toward the downside. Classic catalysts include earnings misses, regulatory setbacks, geopolitical shocks, or moments when market consensus appears overly optimistic on a stock or sector.

In high-volatility environments, the single call sale offsets a substantial fraction of the two-put cost, making the position economical. This is particularly attractive when implied volatility on puts is elevated relative to calls, giving you extra income from selling the call while prices remain suppressed from pessimism.

Traders favour strips when they believe the market has mispriced downside risk—a common view before disappointment or sudden repricing events. The extra put allocation efficiently converts that conviction into leverage.

## Capital efficiency and leverage

Buying two puts outright is capital intensive. A strip reduces net cost by selling one call, which generates income. In volatile or pessimistic markets, the call's premium can reduce or even eliminate the net cost of the position.

This leverage is powerful: for the cost of a cheaper single put, you control two puts' worth of downside profit. However, this leverage inverts if the stock rallies unexpectedly—losses mount because you've committed capital to two puts that are depreciating while the short call is rising against you.

## The breakeven points and profit zones

Maximum profit occurs as the stock approaches zero, with no upper limit in theory. Above the strike, losses are limited. If the net premium paid was small (due to call sale income), the upper breakeven is close to the strike, making upside risk tightly bounded.

If you pay $200 net for the strip, the upper breakeven is at $102. The stock can rise that far before losses exceed the premium. Below $100 (the strike), every dollar of move produces $200 of gross profit (two puts), minus premium paid.

This creates a wide profit zone—any large move profits, but downside moves are far more lucrative.

## Implied volatility and entry timing

Strips are exquisitely sensitive to implied volatility. If vol contracts sharply after entry, all three options (two puts, one call) lose value. The net effect is typically a loss, even if the stock price stays put.

Conversely, vol expansion before the move occurs amplifies the position's value, allowing exit at a premium. This makes strips ideal for trading into periods of elevated vol, such as right before earnings or regulatory announcements when prices are suppressed but volatility is high.

If vol falls after you enter, the vol edge erodes. Many strip traders exit if the expected move doesn't occur within a few days; the position's daily decay from theta and vol contraction destroys value.

## Strip vs. straddle: the directional tilt

A [straddle](/option/) (one call, one put at the same strike) is neutral—it profits equally from moves in either direction. A strip tilts that neutrality sharply downward. If you strongly believe in downside, the strip's extra put is a capital-efficient way to express that conviction without moving the strike.

A straddle suits traders who are genuinely agnostic on direction and simply want to trade volatility. A strip is for traders who expect a move and believe it will favour the downside—such as before dividend disappointments, credit concerns, or cyclical downturns.

## Strike selection and proximity

Most strip traders buy at-the-money (ATM) or slightly out-of-the-money (OTM) options. ATM options are most expensive but offer the broadest profit zone. OTM options are cheaper but demand larger moves to be profitable.

Many practitioners choose slightly OTM strikes to balance cost and range. A $100 stock with an expected move of 5–10% might be well served by $98 or $99 puts (and call).

Some traders also use different strikes to fine-tune the payoff: e.g., buying a $98 put and $102 put while selling a $100 call. This widens the loss-free zone and allocates capital more efficiently, though it complicates position management.

## Early exit and position management

Most strip traders do not hold to expiration. If the stock gaps in the expected direction, closing the position on day one or two locks in the vol premium that evaporates as expiration approaches.

Rolling is also common: if the expected move hasn't occurred by a week before expiration, closing and opening a strip on a later expiration recaptures vol and avoids the final weeks of theta bleed.

Holding a strip into the final days without a move is value-destructive. The position loses on both time decay (theta) and, typically, vol contraction, creating a double headwind.

## Risks and margin considerations

The main risk is vol collapse without a corresponding price move. You pay premium for both puts and the call; if the stock trades flat and vol falls, you lose on all three. This "double vol hit" can quickly erase the intended low-cost advantage.

Assignment risk is minimal for long positions (long puts and call) during holding, but near expiration, assignment becomes possible if the stock is in the money. If assigned on the call while holding the puts, you'll be short 100 shares, which may violate your intended position.

Strips also require sufficient buying power or margin to sustain losses if the stock rallies sharply. If the stock climbs, losses on the two long puts mount and must be funded.

## When strips outperform: the leverage asymmetry

Unlike a simple put purchase (which profits equally from a $5 or $50 decline), a strip amplifies downside moves. A 10% decline produces roughly double the profit of a single put because you own two. This asymmetric leverage is precisely why traders accept the upside cap.

In environments where downside moves are sudden and large—crashes, earnings disasters, sector rotations—strips' leverage amplifies gains. In markets where moves are gradual or ambiguous, the vol decay and premium decay erode value faster than in simpler positions.

## See also

<div class="wiki-seealso">

### Closely related

- [Strap Strategy](/strap-strategy/) — buying two calls and one put at the same strike for upside-biased volatility
- [Long Combo](/long-combo/) — buying an OTM call and selling an OTM put for bullish exposure
- [Short Combo](/short-combo/) — selling an OTM call and buying an OTM put for bearish exposure
- [Put Option](/put-option/) — the right to sell an asset at a set price
- [Call Option](/call-option/) — the right to buy an asset at a set price
- [Implied Volatility](/implied-volatility/) — the market's expectation of future price swings
- [Option Premium](/option-premium/) — the cost of buying or income from selling an option

### Wider context

- Derivatives — financial instruments whose value depends on an underlying asset
- [Option](/option/) — a contract giving the right (not obligation) to buy or sell
- [Protective Put](/protective-put/) — buying a put to hedge downside on a stock position
- [Volatility](/historical-volatility/) — the tendency of prices to fluctuate over time
- [Theta](/theta/) — the decay in option value as expiration approaches

</div>
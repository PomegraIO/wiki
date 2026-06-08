---
title: "Strap Strategy"
description: "A volatility options strategy buying two call options and one put at the same strike to profit from large moves with upside bias."
keywords:
  - strap strategy
  - option strategy
  - volatility
  - leverage
  - derivatives
image: "/svg/derivatives.svg"
---

*A **strap strategy** is a bullish [volatility](/implied-volatility/) [options](/option/) position in which an investor buys two at-the-money or slightly out-of-the-money [call options](/call-option/) and one [put option](/put-option/) at the same strike price on the same underlying asset and expiration date. The strategy profits from large price swings in either direction but is skewed toward bullish moves and offers unlimited upside.*

## The payoff structure: unlimited up, limited down

A strap's payoff is asymmetric. If the underlying rises sharply above the strike, both calls gain value and produce unlimited profit. If it falls sharply, the put gains value, but only one put covers the move—so losses are capped.

Consider a strap where you buy two calls and one put, each at a $100 strike. If the stock climbs to $110, each call gains $10 of intrinsic value (for $2,000 total profit, minus premium paid). If it falls to $90, the put gains $10 intrinsic value (for $1,000 profit from the put), but you've lost the premium paid for the two calls.

This asymmetry is the heart of the strategy: you're betting that if a large move occurs, it will be upward. The extra long call acts as an amplifier for bullish moves and as a brake for bearish ones.

## When and why traders use straps

Straps shine when traders expect an imminent large move but lean toward the upside. Classic triggers include earnings announcements, FDA decisions, central bank meetings, or other binary events where the consensus underprices the likelihood of a headline move.

The strategy is cheaper than buying calls alone if you can sell the put for meaningful premium—which happens when volatility is elevated. In high-vol environments, that single put sale offsets a substantial fraction of the two-call cost, making the position economical.

Traders also favour straps over straddles ([where you buy one call and one put](/option/)) when fundamentals favour upside. A strap allocates more capital to capturing upside, making it a statement of directional conviction.

## Capital efficiency and leverage

Buying two calls outright is capital intensive. A strap reduces net cost by selling one put, which generates income. In volatile markets, the put's premium can reduce or even eliminate the net cost of the position, creating a nearly free trade that profits from large moves.

This leverage appeals to capital-constrained traders: for the price of a cheaper, single call, you can control two calls' worth of upside. However, that leverage inverts if the stock falls—losses mount because you've committed capital to two calls that are depreciating.

## The breakeven points and profit zones

Maximum profit is unlimited above the strike plus the net premium paid. Below the strike, losses are limited. If the net premium paid was small (due to put sale income), the lower breakeven is close to the strike, making downside risk tightly bounded.

For example, if you pay $200 net for the strap, the lower breakeven is at $98. The stock can fall that far before losses exceed the premium. Above $100 (the strike), every dollar of move produces $200 of gross profit (two calls), minus premium paid.

This creates a wide profit zone—any large move, up or down, generates returns, but upside moves are far more lucrative.

## Implied volatility and timing

Straps are exquisitely sensitive to implied volatility. If vol contracts sharply after entry, all three options (two calls, one put) lose value. The net effect is typically a loss, even if the stock price stays put.

Conversely, vol expansion before the move occurs amplifies your position's value, allowing you to exit early at a premium. This makes straps ideal for trading into predictable vol spikes—the day before earnings, for instance—when vol is elevated and the stock typically gaps at open.

If vol falls after you enter, you've lost the vol edge. Many strap traders exit if the expected move doesn't occur within a few days; the position's vol premium deteriorates daily.

## Strap vs. straddle: the directional tilt

A [straddle](/option/) (one call, one put at the same strike) is neutral—it profits equally from moves in either direction. A strap tilts that neutrality sharply upward. If you strongly believe in upside, the strap's extra call is a high-leverage way to express that without moving the strike.

A straddle is suitable for traders who are truly agnostic on direction and simply want to trade volatility. A strap is for traders who expect a move and believe it will favour the upside—such as when earnings typically beat or when consensus has been too pessimistic.

## Strike selection and proximity

Most strap traders buy at-the-money (ATM) or slightly out-of-the-money (OTM) options, depending on capital and the nature of the expected move. ATM options are most expensive but offer the broadest profit zone. OTM options are cheaper but demand larger moves to be profitable.

In practice, many traders choose slightly OTM strikes to balance cost and range. A $100 stock with an expected move of 5–10% might be well served by $102 or $103 calls (and put).

## Early exit and roll management

Most strap traders do not hold to expiration. If the stock gaps in the expected direction, closing the position on day one or two locks in the vol premium that may evaporate as expiration approaches.

Rolling is also common: if the expected move hasn't occurred by a week before expiration, closing the position and opening a strap on a later expiration lets you recapture vol. Holding into the final days of a strap that hasn't moved is value-destructive due to theta decay.

## Risks and margin considerations

The main risk is vol collapse without a corresponding price move. You pay premium for both calls and the put; if the stock trades flat and vol falls, you lose on all three. This "double vol hit" can quickly erase the putative low-cost advantage.

Assignment risk is minimal during the holding period but becomes real near expiration if the stock is in the money. A long position (owning the calls and put) cannot be assigned early on European-style options, but American options may be assigned at any time. If assigned on the put while holding the calls, you'll own 100 shares, which may be contrary to your intent.

Straps also require sufficient margin or buying power to sustain the position if losses mount. If the stock falls sharply, losses on the two long calls create a debit that must be funded.

## See also

<div class="wiki-seealso">

### Closely related

- [Strip Strategy](/strip-strategy/) — buying two puts and one call at the same strike for downside-biased volatility
- [Long Combo](/long-combo/) — buying an OTM call and selling an OTM put for bullish exposure
- [Short Combo](/short-combo/) — selling an OTM call and buying an OTM put for bearish exposure
- [Call Option](/call-option/) — the right to buy an asset at a set price
- [Put Option](/put-option/) — the right to sell an asset at a set price
- [Implied Volatility](/implied-volatility/) — the market's expectation of future price swings
- [Option Premium](/option-premium/) — the cost of buying or income from selling an option

### Wider context

- Derivatives — financial instruments whose value depends on an underlying asset
- [Option](/option/) — a contract giving the right (not obligation) to buy or sell
- [Straddle](/option/) — buying one call and one put at the same strike to bet on volatility
- [Volatility](/historical-volatility/) — the tendency of prices to fluctuate over time
- [Theta](/theta/) — the decay in option value as expiration approaches

</div>
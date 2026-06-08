---
title: "Long Combo"
description: "A bullish options strategy combining a long OTM call with a short OTM put to create leveraged exposure with minimal net premium."
keywords:
  - long combo
  - option strategy
  - bullish position
  - leverage
  - derivatives
image: "/svg/derivatives.svg"
---

*A **long combo** is a bullish [option](/option/) strategy where an investor simultaneously buys an out-of-the-money [call option](/call-option/) and sells an out-of-the-money [put option](/put-option/) at different strike prices on the same underlying asset and expiration date. The trade aims to establish leveraged bullish exposure while keeping the net premium (cost) near zero.*

## What happens at each price level

The mechanics of a long combo depend entirely on where the underlying asset closes relative to the two strikes. Suppose you buy a call at a $105 strike and sell a put at a $95 strike, both expiring in one month.

If the stock climbs above $105, the call gains value while the put expires worthless—you keep the premium collected from selling it as pure profit. This is the ideal outcome: the stock rallies and you pocket both the call's intrinsic value and the put premium.

If the stock remains between the two strikes, the call loses value (it's still out of the money) while the put likewise expires worthless. You absorb a loss on the call but retain the put premium, so the net outcome depends on the premium split.

If the stock falls below $95, you're obligated to buy shares at $95 via the short put while the call expires worthless. Your total loss is capped at the difference between the two strikes, minus the net credit received.

## Why use it: the zero-cost appeal

The defining attraction of a long combo is that selling the OTM put often generates enough premium to offset—sometimes entirely—the cost of buying the OTM call. This creates an economical entry to a bullish leveraged position. Instead of buying stock or a call outright and paying upfront, you can engineer a similar payoff for little or no cash outlay.

This appeals to investors who are confident in an imminent move upward but face capital constraints or prefer not to deploy cash until they must. The strategy also suits traders expecting volatility to decline after earnings or another event; the put sale profits from falling implied volatility, regardless of direction.

## The tradeoff: capped upside and assignment risk

A long combo's upside is unlimited—or nearly so, depending on how wide the strikes are. But there's a floor. If assigned on the short put, you own shares at $95; if you're forced to hold them and they fall further, losses accumulate. Many traders pair a long combo with a predetermined exit rule or stop-loss to avoid open-ended downside.

Assignment on the short put is also a practical headache. Many retail platforms require you to have enough cash or buying power on reserve to cover the purchase of 100 shares (or more) at the put strike. If you lack that buffer, your broker may close the position involuntarily or refuse to let you sell the put in the first place.

Implied volatility can also work against you. If [volatility](/implied-volatility/) contracts sharply after you enter, both the call (which you own) and the put (which you're short) lose value. The call's decline will hurt more than the put's gain helps, leaving you underwater even if the stock moves sideways.

## Long combo vs. long call: when to choose each

Buying a call outright is simpler and offers defined risk (you lose at most the call premium) but requires upfront cash. A long combo transfers some of that cost to a counterparty and leverages your conviction; if you're right, returns per dollar invested are higher.

However, a long combo also creates an obligation to buy shares if the put is exercised—a risk a simple call avoids. The choice comes down to capital availability, risk tolerance, and how strongly you believe in the move. Conservative traders often prefer a straightforward call; aggressive capital-efficient traders favour the combo.

## Setting up the strikes

The distance between the call and put strikes affects both payoff and probability. A wide combo (e.g., call at $110, put at $90) requires larger moves to be profitable and limits your loss if the stock falls sharply. A narrow combo (call at $102, put at $98) demands smaller moves and increases assignment risk.

Most traders choose strikes roughly equidistant from the current price and aim for strikes where each option trades at similar premiums. This naturally minimizes net cash outlay. Some traders deliberately skew the strikes—buying a cheaper call and selling an expensive put—to engineer a net credit, though this increases downside risk.

## When volatility changes the game

Implied volatility significantly impacts combo profitability. A surge in [volatility](/historical-volatility/) raises both the call and put values, but the put—which you're short—gains more in premium than your long call. This scenario can erode profits. Conversely, volatility collapse benefits you, especially if both options expire worthless.

This makes the long combo attractive in periods of suppressed volatility (e.g., after a major event has passed) when you expect prices to move but not volatility to spike further. Selling the put in a low-vol environment locks in premium that may not be recoverable if vol surges later.

## Early exit and rolling

Many combo traders don't hold to expiration. If the stock rallies sharply, closing the position early locks in the profit before the put expires worthless. Similarly, if the stock falls, you might buy back the put to limit losses before assignment hits.

Rolling is also common: closing both legs and opening a new combo at later-dated strikes. This lets you extend the position without taking assignment and adjust strikes based on new price levels.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Combo](/short-combo/) — the opposite bet, selling a call and buying a put for bearish exposure
- [Strap Strategy](/strap-strategy/) — buying two calls and one put at the same strike for bullish volatility
- [Strip Strategy](/strip-strategy/) — buying two puts and one call at the same strike for bearish volatility
- [Call Option](/call-option/) — the right to buy an asset at a set price
- [Put Option](/put-option/) — the right to sell an asset at a set price
- [Implied Volatility](/implied-volatility/) — the market's expectation of future price swings
- [Option Premium](/option-premium/) — the cost of buying or income from selling an option

### Wider context

- Derivatives — financial instruments whose value depends on an underlying asset
- [Option](/option/) — a contract giving the right (not obligation) to buy or sell
- Leverage — using borrowed capital or derivatives to amplify exposure
- [Volatility Smile](/volatility-smile/) — non-uniform implied volatility across strikes

</div>
---
title: "Short Combo"
description: "A bearish options strategy combining a short OTM call with a long OTM put to create leveraged exposure with minimal net premium."
keywords:
  - short combo
  - option strategy
  - bearish position
  - leverage
  - derivatives
image: "/svg/derivatives.svg"
---

*A **short combo** is a bearish [option](/option/) strategy where an investor simultaneously sells an out-of-the-money [call option](/call-option/) and buys an out-of-the-money [put option](/put-option/) at different strike prices on the same underlying asset and expiration date. The trade aims to establish leveraged bearish exposure while keeping net premium (cost) near zero.*

## What happens at each price level

The payoff of a short combo is precisely inverse to a [long combo](/long-combo/). Suppose you sell a call at a $105 strike and buy a put at a $95 strike, both expiring in one month.

If the stock falls below $95, the put gains value while the call expires worthless—you pocket the call premium as profit and exercise (or benefit from the value of) the put, locking in gains. This is the ideal outcome: the stock declines and you profit from both the call premium and put intrinsic value.

If the stock stays between the two strikes, the call expires worthless (premium pocketed) but the put loses value as it remains out of the money. Your net profit depends on the premium split; if you collected more from selling the call than you paid for the put, you come out ahead.

If the stock climbs above $105, you're assigned on the short call and must sell shares at $105, while the put expires worthless. Your maximum profit is capped at the premium spread plus the difference between strikes. Your loss is unlimited in theory, but the put you own acts as a hedge, capping loss at the gap between strike prices.

## Why use it: the zero-cost hedge against rallies

The short combo's appeal lies in its economics: selling an OTM call often generates premium sufficient to offset or eliminate the cost of buying an OTM put. This creates a bearish position for little or no capital. Traders use it when they expect a pullback or consolidation but want protection against a surprise rally—the short call premium funds the put insurance.

The strategy suits investors who hold assets and wish to protect downside without committing much cash. A short combo is cheaper than buying a put alone, since selling the call offsets most or all of the put's cost.

This is particularly appealing in markets where implied [volatility](/implied-volatility/) is elevated. High call premiums make the sale lucrative, and the premium collected can comfortably pay for downside protection.

## The tradeoff: profit ceiling and assignment obligation

The defining constraint of a short combo is capped profit. Your maximum gain is the premium spread plus the strike width. If the stock falls to zero, you still cannot profit beyond this cap—the profit materialises at expiration and never grows.

Assignment on the short call is also a practical burden. If shares surge above the call strike and the option is exercised, you're forced to sell shares at that price. For owners of appreciated securities, this can trigger unexpected tax consequences. For traders with margin accounts, assignment typically requires settlement within a day.

Delta risk is also asymmetric. The short call has negative delta (you lose if the stock rises), while the long put has negative delta too (you profit if the stock falls). This sounds aligned, but if the stock rallies sharply, the call's losses far exceed the put's limited downside protection. Your loss is theoretically unlimited unless you close the position.

## Short combo vs. protective put: when to choose each

Buying a put outright caps downside but costs cash upfront and offers no income. A short combo offsets that cost by selling a call; you get cheaper insurance but accept a profit ceiling and call assignment risk.

The short combo favours traders who believe the stock will decline modestly or trade sideways and are willing to cap gains in exchange for lower insurance cost. A protective put suits investors who simply want downside insurance without opinion on upside.

## Choosing and calibrating strikes

Strike selection is crucial. A wide combo (call at $110, put at $90) limits maximum profit but protects you across a broad range. A narrow combo (call at $102, put at $98) demands the stock move decisively downward to profit and leaves little room for assignment avoidance.

Most traders match the premium on each leg—buying a cheaper put and selling an expensive call—to achieve near-zero net cost. Some intentionally create a net debit (paying cash upfront) in exchange for wider strikes or better protection; others engineer a net credit by skewing strikes, though this increases call assignment risk.

The location of the short call strike is particularly sensitive. If set too close to the current price, assignment becomes likely and forces unexpected selling. If set too far out, the premium shrink and may not fully offset the put's cost.

## Volatility dynamics and the timing problem

A short combo thrives when implied volatility is high at entry and declines afterward. Elevated vol makes the call premium juicy to sell, and falling vol boosts both options' decay—both work in your favour.

However, a volatility spike after entry harms the position. Rising vol inflates the call's value (which you're short), creating losses, while also raising the put's value (which you own), a gain that rarely offsets the call's rise. The net effect is typically negative.

For this reason, short combos are best established when [volatility](/historical-volatility/) is elevated—such as after a market shock—and the trader expects normalization. Entering into a period of rising volatility often leads to losses.

## Rolling and early adjustment

Few traders hold a short combo to expiration. If the stock rallies sharply toward the call strike, closing early and rolling to higher strikes preserves capital and extends the trade.

If the stock falls, closing the position early locks in profit before the put expires worthless. Rolling to lower strikes allows you to extend the position and capture additional decay.

Rolling is preferable to taking assignment, which triggers trading costs, potential tax consequences, and operational friction. By rolling, you maintain the strategy's leverage while adapting to new prices.

## Capital requirements and margin

Short combos frequently require margin buying power, particularly for the short call. Brokers calculate margin reserve as the full call strike price times 100 shares (per contract). If you lack sufficient margin, you may be unable to establish the position.

Similarly, assignment on the short call demands the ability to deliver shares or settle in cash. Brokers typically settle assignments within one business day, so ensure you can meet that obligation before entering.

## See also

<div class="wiki-seealso">

### Closely related

- [Long Combo](/long-combo/) — the opposite bet, buying a call and selling a put for bullish exposure
- [Strap Strategy](/strap-strategy/) — buying two calls and one put at the same strike for bullish volatility
- [Strip Strategy](/strip-strategy/) — buying two puts and one call at the same strike for bearish volatility
- [Put Option](/put-option/) — the right to sell an asset at a set price
- [Call Option](/call-option/) — the right to buy an asset at a set price
- [Implied Volatility](/implied-volatility/) — the market's expectation of future price swings
- [Option Premium](/option-premium/) — the cost of buying or income from selling an option

### Wider context

- Derivatives — financial instruments whose value depends on an underlying asset
- [Option](/option/) — a contract giving the right (not obligation) to buy or sell
- [Protective Put](/protective-put/) — buying a put to hedge downside on a stock position
- [Hedge Fund](/hedge-fund/) — an actively managed investment fund often using leverage and derivatives

</div>
---
title: "Vega Hedging in an Options Portfolio"
description: "How traders hedge vega exposure by buying or selling options to neutralise sensitivity to implied volatility changes."
keywords:
  - vega hedging options
  - vega exposure options portfolio
  - vega neutral portfolio
  - implied volatility hedge
  - long vega short vega
  - options portfolio volatility management
---

*Traders managing portfolios of options often carry unwanted exposure to changes in [implied volatility](/implied-volatility/) — a risk called **vega**. **Vega hedging** offsets this sensitivity by buying or selling options in different strikes or maturities to create a portfolio that is indifferent to volatility swings, leaving only directional or other Greeks to manage.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Vega Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Vega hedging isolates volatility risk so traders can focus on the bets they actually want to make.</div>

|   |   |
|---|---|
| **What vega measures** | P&L change per 1% change in implied volatility |
| **Hedging method** | Buy or sell options to offset net vega |
| **Common hedge vehicles** | Variance swaps, volatility ETFs, option spreads |
| **Vega scaling** | Vega depends on strike, maturity, and moneyness |
| **Cross-gamma risk** | Vega hedges can create delta or gamma mismatches |

</aside>

## What vega is and why it matters

[Vega](/vega/) is one of the five canonical Greeks — [delta](/delta/), [gamma](/gamma/), [theta](/theta/), vega, and [rho](/rho/) — that summarise an option's sensitivity to market moves. While [delta](/delta/) captures directional price risk and [gamma](/gamma/) captures the curvature of that risk, vega captures the impact of changes in implied volatility.

Concretely: if a [call option](/call-option/) has a vega of 0.05, and implied volatility rises by 1%, the option's price will rise by approximately 0.05 times the option's contract multiplier. An option with vega of 0.15 will rise by 0.15 per 1% volatility move — three times the sensitivity. Long options (owned calls or puts) carry positive vega; short options (sold calls or puts) carry negative vega.

For traders running complex option portfolios, vega risk can swamp the bets they intended to make. A trader might construct a portfolio designed to profit from a directional move in the stock, but if implied volatility suddenly collapses, the portfolio's losses from vega can dwarf the directional gain. Conversely, a trader betting on volatility expansion might be short vega when they meant to be long, exposing them to losses if volatility compresses. Vega hedging eliminates this drift.

## The mechanics of vega hedging

Vega hedging works by matching long and short vega across the portfolio. The simplest example: a trader who is long 100 shares of stock buys an [out-of-the-money call](/call-option/) to cap upside losses (a [protective call](/protective-put/), though with a call). The call is long vega — if volatility rises, the call becomes more valuable, providing a buffer. But if the trader only cares about downside protection and doesn't want to bet on volatility, they can short vega elsewhere. They might sell an equally maturity-matched [out-of-the-money put](/put-option/) with the same [strike price](/strike-price/); the short put has negative vega and offsets the long call's vega. The result: a position that is delta-positive (profits if the stock rises), gamma-negative (profits if the stock stays near the strikes), and vega-neutral (indifferent to volatility changes).

In more sophisticated portfolios, vega hedging uses:

- **Variance swaps:** Direct contracts on realized volatility. A trader long realized volatility exposure can sell a variance swap to offset vega in their option positions.
- **Volatility-linked ETFs:** Products tracking volatility indices like the VIX can be shorted to offset long vega.
- **Option spreads:** A [covered call](/covered-call/) (long stock, short call) has negative vega; a short [put spread](/put-option/) (short put, long put) has negative vega. Matching strikes and maturities across long and short options neutralizes vega.

## Vega scaling and the maturity problem

Vega is not constant across all options on the same underlying. It varies with [strike price](/strike-price/), time to [expiration](/expiration-date/), and the current stock price relative to the strike (moneyness). Options deep in the money or far out of the money have lower vega than at-the-money options. Longer-dated options (further from [expiration](/expiration-date/)) have higher vega than short-dated ones — a 6-month call at the money has roughly 2–3 times the vega of a 1-month call.

This matters for hedging because a trader cannot simply sell one option to offset the vega of a long position in another option. A trader long 1,000 shares and long one 6-month at-the-money [call option](/call-option/) (vega ≈ 0.30) cannot simply sell one 1-month at-the-money [put option](/put-option/) (vega ≈ 0.10) to hedge. The short put's vega is too small. The trader would need to sell roughly three 1-month puts to match the long call's vega.

The maturity mismatch creates a secondary problem. A 6-month option's vega decays toward zero as time passes and the option approaches [expiration](/expiration-date/). A 1-month option's vega decays faster. If a trader hedges a 6-month long vega position with short 1-month vega, the hedge will be imperfect in 30 days when the shorts expire; the trader will have to rebalance, incurring transaction costs and market slippage.

Sophisticated traders often hedge long vega in long-dated options by selling vega in similarly-dated options, accepting the cost of rolling hedges rather than the friction of mismatched maturities.

## Vega hedging and gamma tension

A subtle trap in vega hedging is the relationship between vega and [gamma](/gamma/). Options that are in the money or out of the money have high [gamma](/gamma/) (high curvature) and low vega. Options at the money have high vega and low [gamma](/gamma/). A trader who hedges vega by buying or selling options at different strikes inadvertently takes on [gamma](/gamma/) exposure.

Example: a trader is long vega via a long at-the-money [call option](/call-option/) (high vega, low [gamma](/gamma/)) and shorts vega via an out-of-the-money [call option](/call-option/) (low vega, high [gamma](/gamma/)). The portfolio is now vega-neutral but [gamma](/gamma/)-long — it profits if the stock moves sharply in either direction. The trader has traded vega risk for [gamma](/gamma/) risk. This can be deliberate (if the trader believes in volatility compression but expects big moves) or accidental. Either way, the hedge is incomplete; the trader must manage the secondary Greek exposure.

Some traders resolve this by using [variance swaps](/derivatives-hedging/) or pure volatility hedges that do not introduce directional or [gamma](/gamma/) mismatches, though these instruments are available only in liquid, large-cap markets.

## Rebalancing and slippage costs

Vega hedges rarely stay hedged indefinitely. As underlying prices move, [implied volatility](/implied-volatility/) term structures shift, and time passes, vega positions drift. A portfolio that was vega-neutral yesterday may be long or short vega by today. Rebalancing the hedge — selling or buying more options to restore vega neutrality — incurs costs: bid-ask [spreads](/bid-ask-spread/), slippage, and commissions.

Active vega hedging is most common among large options dealers and quantitative funds with deep capital, low execution costs, and sophisticated risk measurement. A typical hedge fund or individual trader often hedges vega less frequently or uses coarser hedges (e.g., quarterly rebalancing or tolerance bands of ±10% vega drift) to reduce costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Vega](/vega/) — the Greek measuring sensitivity to implied volatility
- [Implied Volatility](/implied-volatility/) — the market's forecast of future price moves, embedded in option prices
- [Call Option](/call-option/) — long calls carry positive vega
- [Put Option](/put-option/) — long puts carry positive vega
- [Gamma](/gamma/) — curvature risk; vega hedges can inadvertently create gamma exposure
- [Delta](/delta/) — directional risk; separate from vega but often managed together
- [Covered Call](/covered-call/) — a strategy that is naturally short vega

### Wider context

- [Option Premium](/option-premium/) — the component of option price sensitive to volatility
- [Derivatives Hedging](/derivatives-hedging/) — broader framework for managing option portfolio risks
- [Volatility Smile](/volatility-smile/) — the pattern in implied volatility across strikes, complicating vega management
- [Historical Volatility](/historical-volatility/) — actual realized moves; distinct from implied and affect vega decay
- [Value at Risk](/value-at-risk/) — risk measurement framework that includes vega exposure

</div>

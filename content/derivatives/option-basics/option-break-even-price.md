---
title: "Option Break-Even Price"
description: "The underlying asset price at which an option position reaches zero profit or loss at expiration; critical for trading decisions."
keywords:
  - break-even analysis
  - option pricing
  - strike price
  - profit threshold
  - expiration value
image: "/svg/derivatives.svg"
---

*The **break-even price** of an option is the underlying asset's price at expiration where the buyer neither gains nor loses money. For any option buyer, this threshold sits between the strike price and the cost of entry; once the underlying moves beyond it, profit becomes real. For sellers, break-even is where risk shifts into their favour.*

## How break-even works for calls

A [call option](/option/) buyer pays a [premium](/option-premium/) upfront for the right to buy the underlying at a fixed [strike price](/strike-price/). Say you pay £3 for a call with a £50 strike. Your break-even is £53: at expiry, if the underlying closes at exactly £53, you can exercise (buy at £50) and immediately sell at market price (£53), netting £3—exactly the premium paid, washing out to zero.

Below break-even, the call is worthless to exercise (the underlying price is still below strike), so you simply lose the premium. Above it, every pound the underlying rises yields profit: at £54 underlying, you profit £1.

## How break-even works for puts

A [put option](/put-option/) buyer pays a premium for the right to sell at a fixed strike. With a £50 strike, a £3 premium cost, and the underlying at £47 at expiry, you exercise (sell at £50) and pocket the difference of £3—recovering your premium cost, breaking even at £47.

Below £47 (further below strike), profit accumulates. Above break-even, the put decays to loss: if the underlying rises to £49, you either sell at £50 (a £1 gain) but gave up £3 in premium, netting a £2 loss on the position.

## Break-even for covered calls and protective puts

A [covered call](/covered-call/) writer already owns the underlying and sells a call to collect premium. If you own a stock at £50 and sell a call at £3 premium, your break-even on the complete position drops to £47. You've traded upside potential (the stock rises above £53) for income, but protected your entry point.

A protective put buyer owns the underlying and buys a put to hedge downside. Long the stock at £50, you buy a £50 strike put for £3 premium. Your break-even on the combined position is £53: the stock must rise that high to offset the put cost. Below £53, the put provides insurance; the stock can't fall below £50 (you'll exercise the put to sell at £50).

## Break-even in spreads

Multi-leg spreads have multiple break-even points. A [bull call spread](/bull-call-spread/)—buying a £50 call for £4 and selling a £55 call for £2—has a net cost of £2 and a break-even of £52. Your maximum profit caps at £3 (the £5 strike width minus £2 cost), achieved once the underlying rises to £55 or beyond.

Iron condors, straddles, and other complex structures have two break-even points, above and below the strike range. Between those points, profit exists; beyond them, losses grow.

## The break-even formula

For a call: **Call Break-Even = Strike Price + Premium Paid**

For a put: **Put Break-Even = Strike Price − Premium Paid**

These formulas hold at expiration, assuming no transaction costs, dividends, or interest. Real trading includes bid-ask spreads and fees, which shift break-even modestly against the buyer.

## Why break-even matters for trading decisions

Break-even is the threshold between speculative loss and profitable trade. An option trader must forecast: does the underlying have *enough room to move* past break-even before expiry? A call buyer betting on upside must see credible catalysts that push the price above strike + premium. If the underlying drifts sideways, [time decay](/time-decay-theta/) erodes the position and break-even never arrives.

Smart traders also use break-even to size risk. Knowing that a put needs the underlying to drop 8% to break even helps clarify whether the move is probable—and whether the 3% premium reward is worth the risk.

## Break-even vs. intrinsic value

At any point before expiry, the option's market price is higher than its [intrinsic value](/intrinsic-value/). A call worth £3 intrinsically (underlying £3 above strike) may cost £4 because of time value. You'd pay £4 and need a larger move just to break even. This is why premature exercise (closing out early) often requires the underlying to move *beyond* break-even, not just to it.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational contracts conveying a right to buy or sell at a fixed price
- [Strike Price](/strike-price/) — the underlying price at which the option buyer chooses to transact
- [Option Premium](/option-premium/) — the upfront cost to purchase the option right
- [Time Decay](/time-decay-theta/) — how an option loses value as expiry approaches
- [Intrinsic Value](/intrinsic-value/) — the immediate economic gain if exercised now
- [In the Money](/in-the-money/) — when the underlying makes the option profitable to exercise

### Wider context

- [Covered Call](/covered-call/) — selling calls against a long stock position
- [Protective Put](/protective-put/) — buying puts as insurance for a long stock position
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — foundational framework for valuing future cash flows

</div>

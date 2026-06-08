---
title: "What Happens When an Option Expires Out of the Money"
description: "What happens when an option expires out of the money: the buyer loses the full premium paid, the seller keeps it, and the contract becomes worthless with no asset delivery."
keywords:
  - out of the money option expiration
  - otm option expires worthless
  - option premium loss
  - option seller profit
  - expiration contracts
image: /svg/derivatives.svg
---

*When an **option** reaches its [expiration date](/expiration-date/) and the underlying asset's price has moved against the buyer — meaning the [exercise price](/exercise-price/) is worse than the market price — the option expires **out of the money (OTM)** and becomes worthless, the buyer forfeits the entire [premium](/option-premium/) paid upfront, and the [option](/option/) writer pockets that premium as pure profit.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OTM Option at Expiration — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Buyer loses premium; seller keeps it; contract expires worthless.</div>

|   |   |
|---|---|
| **Buyer outcome** | Zero; loses premium paid upfront |
| **Seller outcome** | Receives and keeps the entire premium |
| **Intrinsic value** | Zero; contract has no cash-settlement value |
| **Settlement** | Automatic expiration; no asset delivery |
| **Profit threshold** | Buyer needs price movement to at least break even |
| **Time decay** | Works entirely in seller's favor near expiration |

</aside>

## Definition: Out of the Money at Expiration

An [option](/option/) is out of the money at expiration if exercising it would lose money relative to the current market price. For a call option, this means the stock price has fallen below the strike price. For a put option, the stock price has risen above the strike price. In either case, the buyer has no incentive to exercise, so the contract expires unexercised.

Because the buyer will not exercise, the seller of the option has no obligation to deliver the underlying asset. The contract simply terminates. The buyer's loss is the full premium paid at inception; the seller's gain is that same premium, since no offsetting cost occurs.

## A Worked Example: Call Option

Suppose an investor buys a call [option](/option/) on XYZ stock with a [strike price](/strike-price/) of $100, paying a $3 premium per share (or $300 for a standard 100-share contract). The stock needs to rise above $103 for the buyer to break even — that is, the $3 profit per share from exercising offsets the premium paid.

At expiration, suppose XYZ is trading at $95. The call is out of the money by $5 per share ($95 market price minus $100 strike). The buyer would never exercise (buying at $100 when the market price is $95 makes no sense). The contract expires worthless. The buyer loses $300 (the premium paid). The seller of the call, who pocketed the $300 premium when the trade was opened, keeps it entirely and has no liability.

If the stock had risen to $103 at expiration, the call would be at-the-money-or-in-the-money, the buyer would exercise (buying at $100, selling immediately at $103 for a $3 profit per share), offsetting the $3 premium. At $105, the buyer nets $2 per share of profit ($5 intrinsic value minus $3 premium). At $95 (the example above), the loss is $300.

## A Worked Example: Put Option

Consider a put [option](/option/) on the same XYZ stock with a strike of $90, costing $2 per share ($200 for 100 shares). The put gives the right to sell at $90. For the buyer to break even, XYZ must fall to $88 (so the $2 profit from selling at $90 versus $88 market price offsets the $2 premium).

At expiration, XYZ is at $92. The put is out of the money by $2. The buyer would not sell at $90 when the market price is $92 — that would forfeit $2 per share. The contract expires worthless. The buyer loses the $200 premium. The put seller keeps it as profit.

If XYZ had fallen to $88, the put buyer would exercise (selling at $90, which is $2 better than the $88 market price), netting zero profit after the $2 premium. At $80, the buyer would net $8 per share of intrinsic value minus $2 premium = $6 per share profit. At $92, the loss is $200.

## Why OTM Expiration Matters

This outcome is the core risk-return trade-off for option buyers. The premium paid is the maximum loss. If the market does not move enough — or moves in the wrong direction — the entire bet is lost. This is why options are sometimes called "wasting assets": [time decay](/time-decay-theta/) works against the buyer as expiration approaches and the option falls further out of the money.

For the seller, an OTM expiration is the best outcome. The premium is pure profit, with zero cost or liability. This is why [covered call](/covered-call/) strategies and other income-generating option strategies rely on the expectation that many positions will expire OTM.

## Automatic Settlement and No Delivery

Modern options are cash-settled or automatically exercised if in the money at expiration. If the option is OTM, no settlement transaction occurs — the contract simply ceases to exist. There is no delivery of the underlying asset, no cash transfer, and no further obligations. The buyer has already borne the full loss (the premium); the seller has already realized the full gain.

In some equity options, exercise is automatic if the contract is in the money by more than a negligible amount (e.g., $0.01) at expiration, even if the buyer does not actively exercise. However, if the option is out of the money, automatic exercise does not occur. The buyer cannot force the seller to incur a loss by exercising an OTM option.

## How Time Decay Drives OTM Outcomes

As expiration approaches, an option's [time value](/time-value/) decays toward zero. An out-of-the-money option with three months to expiration might retain some extrinsic value — the possibility that the price will move in the buyer's favor. At expiration, that possibility collapses to zero if the price has not moved enough.

This is why sellers often prefer short-dated or OTM options: time decay works entirely in their favor. A buyer might lose money even if the underlying asset barely moves, simply because time has expired. Conversely, a buyer needs either a large and timely price move or the passage of less time (to preserve time value) to profit.

## Implications for Option Strategy

Understanding OTM expiration helps explain why options are suited to specific goals. For buyers, they are a leveraged bet on directional movement, with capped downside (the premium). For sellers, they are a way to harvest time decay and collect income, accepting the capped downside of assignment risk in exchange for high probability of profit if the option expires OTM.

Traders assess whether the probability of an option remaining out of the money is worth the income (premium) they earn. This calculus depends on [volatility](/historical-volatility/), time to expiration, and conviction about price direction. An OTM expiration is not a loss for the seller — it is the success outcome.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — contract giving the right to buy or sell an asset at a fixed price
- [Exercise Price](/exercise-price/) — strike price at which the option may be exercised
- [Option Premium](/option-premium/) — upfront cost to buy the option or income from selling it
- [In the Money](/in-the-money/) — option with intrinsic value (opposite of out of the money)
- [Time Decay Theta](/time-decay-theta/) — loss of option value as expiration approaches
- [Covered Call](/covered-call/) — sell call options against held stock, profit from OTM expiration
- [Expiration Date](/expiration-date/) — date when the option contract ceases to exist

### Wider context

- [Protective Put](/protective-put/) — buy put options as insurance; loss occurs if stock rises above strike
- [Call Option](/call-option/) — right to buy; profits if underlying rises above strike plus premium
- [Put Option](/put-option/) — right to sell; profits if underlying falls below strike minus premium
- [Strike Price](/strike-price/) — agreed price at which option may be exercised
- [Volatility Smile](/volatility-smile/) — option pricing effects based on strike selection

</div>

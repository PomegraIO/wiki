---
title: "Calculating Option Break-Even at Expiration: Worked Examples"
description: "How to calculate option break-even price at expiration for calls and puts. Step-by-step formulas with dollar examples for long and short positions."
keywords:
  - option break-even price
  - break-even calculation
  - call option break-even
  - put option break-even
  - option expiration profit
  - strike price and premium
---

*The **break-even price** on an [option](/option/) at [expiration](/expiration-date/) is the underlying asset price at which the buyer recovers the [premium](/option-premium/) paid and begins to profit. For calls and puts, the calculation is straightforward: strike price plus (or minus) the premium. Below are worked examples for each strategy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Break-Even — formulas and examples</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Break-even tells you the price your position needs to turn profitable.</div>

|   |   |
|---|---|
| **Long [call](/call-option/) break-even** | Strike price + premium paid |
| **Long [put](/put-option/) break-even** | Strike price − premium paid |
| **Short call break-even** | Strike price + premium received |
| **Short put break-even** | Strike price − premium received |
| **Key principle** | Break-even is always where profit = $0 |
| **After break-even** | Every $1 move in your favour = gain; every $1 move against = loss |

</aside>

## The core principle

An option buyer pays cash upfront (the premium). At [expiration](/expiration-date/), the option either has value or it does not. The break-even point is the underlying asset price at which the option's intrinsic value exactly equals the premium paid. Any movement beyond break-even generates a profit.

For a seller, it is the reverse: they receive the premium. They are profitable as long as the underlying stays within a range. If the underlying moves beyond that range, the profit shrinks and disappears.

## Long Call Example

You buy a call [option](/option/) on Apple stock:
- [Strike price](/strike-price/): $150
- [Premium](/option-premium/) paid: $5 per share

At expiration, the break-even price is **$155** ($150 + $5).

Here is what happens at different prices:

| Underlying Price | [Intrinsic Value](/intrinsic-value/) | Profit/Loss |
|---|---|---|
| $145 | $0 | −$5 (premium lost) |
| $150 | $0 | −$5 (premium lost) |
| **$155** | **$5** | **$0 (break-even)** |
| $160 | $10 | +$5 |
| $165 | $15 | +$10 |

You need Apple to rise to at least $155 just to recover your $5 premium. If it only reaches $152, you lose money ($2 intrinsic value − $5 premium paid = −$3 loss).

## Long Put Example

You buy a put [option](/option/) on Microsoft stock:
- Strike price: $300
- Premium paid: $8 per share

Break-even price: **$292** ($300 − $8).

If Microsoft is below $292 at expiration, you are in profit:

| Underlying Price | Intrinsic Value | Profit/Loss |
|---|---|---|
| $285 | $15 | +$7 |
| **$292** | **$8** | **$0 (break-even)** |
| $300 | $0 | −$8 (premium lost) |
| $310 | $0 | −$8 (premium lost) |

The put gives you the right to sell at $300. If Microsoft is $292, you exercise, sell at $300, and pocket $8, which recovers your premium. Below $292, you gain. Above $300, the option is worthless and you lose the entire $8.

## Short Call Example

You sell (write) a call [option](/option/) on Tesla stock:
- Strike price: $220
- Premium received: $7 per share

Break-even price: **$227** ($220 + $7).

As the seller, you *want* the stock to stay below the strike. You keep the premium as profit. But if it rises too high, your profit disappears:

| Underlying Price | Your Profit/Loss |
|---|---|
| $210 | +$7 (full premium kept) |
| $220 | +$7 (full premium kept) |
| **$227** | **$0 (break-even)** |
| $235 | −$8 |
| $245 | −$18 |

You receive $7 when you sell the call. If Tesla stays at $220 or below, you keep it. If it rises to $227, the buyer exercises and you are forced to sell at $220 (losing $7), offset by the $7 premium you received. Above $227, you lose money.

## Short Put Example

You sell a put [option](/option/) on Nvidia:
- Strike price: $400
- Premium received: $12 per share

Break-even price: **$388** ($400 − $12).

| Underlying Price | Your Profit/Loss |
|---|---|
| $410 | +$12 (full premium kept) |
| $400 | +$12 (full premium kept) |
| **$388** | **$0 (break-even)** |
| $380 | −$8 |
| $370 | −$18 |

You pocket $12 upfront. If Nvidia stays at $400 or above, you keep the full amount. If it falls to $388, the buyer exercises, forcing you to buy at $400 (losing $12), but the premium covers it. Below $388, you lose money.

## Why break-even matters

Break-even is your margin of safety. It tells you how much the underlying must move for your trade to pay off. For a long position, you need the underlying to move your way past break-even. For a short position, you are profitable as long as the underlying stays within a range around the strike.

Traders also use break-even to compare [option](/option/) strategies. A straddle (buying both a call and a put) has two break-even points: one above the strike, one below. A [covered call](/covered-call/) (selling a call against stock you own) has a break-even based on your stock cost plus the premium paid, minus the premium you received from the call.

## Time decay and break-even before expiration

The examples above show break-even at expiration, when the option has only intrinsic value left. Before expiration, an [option](/option/) has time value, and break-even shifts. An out-of-the-money call might have zero intrinsic value but still be worth something because there is time for the underlying to move. For practical trading, track both the at-expiration break-even and the current market value of the option.

## Key takeaway

The break-even formula is simple enough to memorize:

- Long call: Strike + Premium
- Long put: Strike − Premium
- Short call: Strike + Premium
- Short put: Strike − Premium

The logic is always the same: a buyer needs the option to move in their direction far enough to cover what they paid. A seller needs the underlying to stay within a range to keep their profit. Once you know the break-even, you can instantly assess whether a trade is worth the risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the fundamentals of calls and puts
- [Intrinsic Value](/intrinsic-value/) — the cash value of an option at expiration
- [Strike Price](/strike-price/) — the price at which you can buy or sell the underlying
- [Option Premium](/option-premium/) — what you pay or receive to enter an option position
- [Call Option](/call-option/) — the right to buy at a fixed price
- [Put Option](/put-option/) — the right to sell at a fixed price

### Wider context

- [Expiration Date](/expiration-date/) — when options stop existing
- [Time Decay](/time-decay-theta/) — how option value erodes as expiration approaches
- [Derivatives Hedging](/derivatives-hedging/) — using options to manage risk
- [Black-Scholes Model](/black-scholes-model/) — a formula for pricing options before expiration

</div>

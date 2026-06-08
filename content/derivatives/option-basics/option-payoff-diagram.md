---
title: "Option Payoff Diagram"
description: "A graph showing profit and loss across different prices of the underlying asset at option expiration."
keywords:
  - payoff diagram
  - profit loss graph
  - option profit chart
  - break-even price
image: "/svg/derivatives.svg"
---

*An **option payoff diagram** is a graph that plots profit or loss on the vertical axis against the price of the underlying asset on the horizontal axis, showing the outcome of an [option](/option/) position at [expiration](/expiration-date/). Reading these graphs correctly is essential for understanding which price movements make you money and where your maximum gain or loss sits.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Payoff Diagram — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">A payoff diagram lets you see profit and loss zones at a glance.</div>

|   |   |
|---|---|
| **What it shows** | Profit/loss as underlying price moves from zero to infinity |
| **Also called** | Payoff graph, P&L diagram, profit diagram |
| **Horizontal axis** | Price of the underlying asset at expiration |
| **Vertical axis** | Profit or loss in dollars (or per-share basis) |
| **Break-even point** | Where the profit line crosses the horizontal axis |
| **Payoff at expiration** | Intrinsic value only; [time value](/time-value/) is zero |

</aside>

## The axes and the break-even line

The horizontal axis represents the price of the underlying [stock](/stock/) at the moment of [expiration](/expiration-date/). The vertical axis represents your profit (positive) or loss (negative) on the [option](/option/) position, usually expressed per share. The break-even price is the underlying price at which your position returns exactly zero profit or loss; it sits where the payoff line crosses the horizontal axis.

For a [call option](/call-option/) buyer paying $3 [premium](/option-premium/) for a $100 [strike price](/strike-price/), the break-even price is $103. If the stock closes at $103 at expiration, the option is worth $3 ([call option](/call-option/) intrinsic value of $3, minus the $3 [premium](/option-premium/) paid), netting zero. Below $103, you lose money. Above $103, you profit $1 for every dollar the stock rallies past $103.

## Long call: rising line above strike

A [long call](/call-option/) payoff diagram shows a line that is flat (at a loss equal to the [premium](/option-premium/) paid) below the [strike price](/strike-price/), then rises linearly above it. The slope of the rising line is always 45 degrees (or close to it, depending on the axis scale) because a $1 move in the underlying translates to a $1 move in your profit (after you have recovered the [premium](/option-premium/) paid).

The maximum loss is the [premium](/option-premium/) you paid. Your maximum gain is theoretically unlimited; as the stock rallies, your profit grows without bound. The break-even point is the [strike price](/strike-price/) plus the [premium](/option-premium/) paid. Buy a $100 call for $3, your break-even is $103.

## Long put: falling line below strike

A [long put](/put-option/) payoff diagram is an upside-down version. The line is flat (at a loss equal to the [premium](/option-premium/) paid) above the [strike price](/strike-price/), then falls (becomes more profitable) as the underlying price drops below it. The slope is negative: a $1 drop in the underlying makes your profit rise by $1.

The maximum loss is still the [premium](/option-premium/) you paid (you lose it all if the stock rallies infinitely). Your maximum gain is capped at the [strike price](/strike-price/) minus the [premium](/option-premium/) paid (the stock falls to zero). The break-even is the [strike price](/strike-price/) minus the [premium](/option-premium/) paid.

## Short call: inverted profit zone

A [short call](/call-option/) payoff is the mirror image of the long call. The line starts high (your max profit equals the [premium](/option-premium/) collected) below the [strike price](/strike-price/) and falls as the underlying rises. At the [strike price](/strike-price/), the line crosses the horizontal axis, moving into loss territory. The slope is negative (profit decreases as the stock rises).

Your maximum profit is the [premium](/option-premium/) you collected, earned if the stock stays below the [strike price](/strike-price/). Your maximum loss is theoretically unlimited as the stock rallies—the payoff line extends downward forever. This is why [naked option](/naked-option/) sellers of calls are exposed to catastrophic risk.

## Short put: inverted loss zone

A [short put](/put-option/) payoff is the inverse of the long put. The line starts high (your max profit) above the [strike price](/strike-price/) and falls as the underlying drops below it, crossing into loss at the [strike price](/strike-price/). Your profit decreases as the stock falls.

Maximum profit is the [premium](/option-premium/) collected. Maximum loss is capped at the [strike price](/strike-price/) (if the stock falls to zero, you lose that amount per share). A [naked option](/naked-option/) seller writing a $100 put can lose up to $100 per share, or $10,000 per contract—still brutal but not infinite.

## Multi-leg strategies: combining payoffs

The power of payoff diagrams emerges when you stack multiple [option](/option/) positions. A [covered call](/covered-call/) (long stock, short call) combines an upward-sloping line (from the stock) with a downward-sloping line (from the short call). The result is a "capped upside" line: you profit if the stock rises, but only to the [strike price](/strike-price/) of the call; above that, the short call eats your gains.

A [protective put](/protective-put/) (long stock, long put) layers a downward-sloping line (the put) onto the stock's upward-sloping line. The result is a "downside insurance" payoff: you keep all upside above the [strike price](/strike-price/), but the put floors your loss below it.

A [bull call spread](/option/) (long call at lower strike, short call at higher strike) produces a flat line below the lower strike (loss of the net [premium](/option-premium/) paid), then an upward slope between the two strikes, then flat again above the higher strike (max profit is the difference between strikes, minus the net [premium](/option-premium/)). The payoff is limited on both ends—less risk, less reward.

## Reading the diagram correctly

When you see a payoff diagram, ask four questions:

1. **Where is my break-even?** Find where the payoff line crosses zero.
2. **What is my max gain?** Is it unlimited (open-ended line) or capped (flat line)?
3. **What is my max loss?** Is it the [premium](/option-premium/) paid (for a buyer) or something larger (for a seller)?
4. **What price range favours me?** Does the line stay positive above or below a certain price?

A trader who buys a [call option](/call-option/) and sketches the payoff diagram will see immediately: "If the stock stays flat, I lose my [premium](/option-premium/). If it rallies, I make money. My loss is capped; my gain is not." Conversely, a [short call](/call-option/) seller sees the inverse: "I keep the [premium](/option-premium/) if the stock stays flat. If it rallies, I get destroyed."

## Time decay does not appear on payoff diagrams

One critical limitation: payoff diagrams show the position only at [expiration](/expiration-date/). They do not capture [time decay](/time-decay-theta/)—the erosion of [option](/option/) value as days pass. An [out-of-the-money](/out-of-the-money/) [option](/option/) that you bought decays in value daily, even if the stock price does not move. The payoff diagram at day 1 looks different from the payoff at day 60 (a month before expiration), and different again at [expiration](/expiration-date/). Traders must remember that the diagram is a snapshot at the final moment, not a guide to what happens in between.

## Using diagrams to plan strategy

Professional traders sketch payoff diagrams before entering any multi-leg position. A portfolio manager protecting a large stock holding sketches the [protective put](/protective-put/) payoff to see the insurance cost (the [put](/put-option/) [premium](/option-premium/)) and the protection floor. A hedger enters a [collar](/option/) (long put, short call) and sees graphically that upside is capped but downside is protected—a reasonable compromise.

For retail traders, drawing these diagrams trains intuition about risk and reward. It removes the mystery from [option](/option/) trading and forces clarity before capital is at risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Break-Even Price](/strike-price/) — the underlying price at which the option position returns zero profit
- [Intrinsic Value](/intrinsic-value/) — the payoff at expiration; all [time value](/time-value/) evaporates
- [Time Decay](/time-decay-theta/) — erosion of option premium not captured in the payoff diagram
- [Call Option](/call-option/) — upward-sloping payoff below the strike, unlimited upside
- [Put Option](/put-option/) — downward-sloping payoff below the strike, capped loss
- [Covered Call](/covered-call/) — combines stock and short call for a capped-upside payoff
- [Protective Put](/protective-put/) — combines stock and long put for a downside-protected payoff

### Wider context

- [Option](/option/) — contracts whose payoff depends on the price of the underlying
- [Expiration Date](/expiration-date/) — the date when the payoff diagram becomes reality
- [In-the-Money](/in-the-money/) — positive payoff at expiration
- [Out-of-the-Money](/out-of-the-money/) — zero payoff at expiration

</div>

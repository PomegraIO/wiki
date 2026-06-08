---
title: "Long Option vs Short Option: Rights, Obligations, and Risk"
description: "Long option vs short option: buyers hold rights with defined risk; writers assume obligations with unlimited loss. Covers P&L, margin, and Greeks."
keywords:
  - long option vs short option
  - short option obligation
  - long option rights
  - option buyer risk
  - option writer risk
image: /svg/derivatives.svg
---

*A **long option** grants the buyer a right to buy (call) or sell (put) at a fixed price, with losses capped at the [option premium](/option-premium/) paid. A **short option** obligates the seller (writer) to honor that right if exercised, with gains capped at the premium but losses potentially unlimited (on calls) or substantial (on puts).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Long vs Short Options — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Buyer has a choice; seller has a duty—and bears the asymmetry in risk and reward.</div>

|   |   |
|---|---|
| **Long position** | Owns the right; pays the premium; limited downside |
| **Short position** | Issued the obligation; received the premium; limited upside, potentially unlimited loss |
| **Max gain (call long)** | Unlimited (as underlying price rises) |
| **Max loss (call long)** | Premium paid |
| **Max gain (call short)** | Premium collected |
| **Max loss (call short)** | Unlimited (theoretically) |
| **Margin requirement** | Long: premium paid upfront; Short: substantial, rising if position moves against writer |
| **Breakeven (call)** | Long: Strike + Premium; Short: Strike + Premium |

</aside>

## The Core Asymmetry: Right vs. Obligation

The distinction is categorical. The buyer of an [option](/option/) owns a **right**—an unrestricted choice. If the option finishes in-the-money, the buyer exercises. If it finishes out-of-the-money, the buyer lets it expire. No obligation attaches.

The seller (writer) of an [option](/option/) assumes an **obligation**. If the buyer decides to exercise, the writer must perform: deliver the stock (on a call) or buy it at the stated price (on a put), regardless of market conditions. The writer has no choice.

This imbalance drives the price asymmetry. The buyer pays a premium for the right; the writer receives a premium for accepting the obligation. The premium is the option's price, and it represents the buyer's maximum loss and the writer's maximum gain—but only in favorable scenarios for each.

## Long Calls and Puts: Limited Downside, Asymmetric Upside

A long call gives the holder the right to buy stock at the [strike price](/strike-price/) on or before [expiration](/expiration-date/). Suppose a call on ABC stock has a strike of USD 100 and costs USD 5 (the [option premium](/option-premium/)).

The buyer's P&L table:

| Stock Price at Expiration | Intrinsic Value | Premium | Net Profit |
|--------------------------|-----------------|---------|-----------|
| USD 90 | USD 0 | −USD 5 | −USD 5 |
| USD 100 | USD 0 | −USD 5 | −USD 5 |
| USD 105 | USD 5 | −USD 5 | USD 0 |
| USD 110 | USD 10 | −USD 5 | USD 5 |
| USD 150 | USD 50 | −USD 5 | USD 45 |

The buyer's maximum loss is USD 5 (the premium), incurred if the stock falls to zero or stays below USD 100. The maximum gain is unlimited—if ABC stock rises to USD 500, the buyer profits USD 395 per share.

A long put (the right to sell) works symmetrically. If the [strike](/strike-price/) is USD 100 and the premium is USD 3, the buyer profits if the stock falls below USD 97. Maximum loss is USD 3; maximum gain is USD 97 per share (if the stock falls to zero, the buyer sells it at USD 100).

The key insight: long options are **asymmetric bets**. They pay off in one direction (unbounded upside on calls, unbounded downside on puts) while capping losses at the premium. This asymmetry comes at a cost—buyers must pay the premium upfront.

## Short Calls and Puts: Capped Gain, Uncapped Risk

A short call obligates the writer to deliver stock at the strike if the buyer exercises. Suppose the writer sells a call with a strike of USD 100 and collects a USD 5 premium.

The writer's P&L table:

| Stock Price at Expiration | Intrinsic Value | Premium | Net Profit |
|--------------------------|-----------------|---------|-----------|
| USD 90 | USD 0 | USD 5 | USD 5 |
| USD 100 | USD 0 | USD 5 | USD 5 |
| USD 105 | USD 5 | USD 5 | USD 0 |
| USD 110 | USD 10 | USD 5 | −USD 5 |
| USD 150 | USD 50 | USD 5 | −USD 45 |

The writer's maximum gain is USD 5 (the premium), achieved if the stock stays at or below USD 100. If the stock rises above USD 105, the writer loses money—and the loss grows without limit as the stock rises. A short call is an **unbounded liability**.

A short put has bounded downside. If the writer sells a put with a strike of USD 100 and collects USD 3, the writer's maximum loss is USD 97 (if the stock falls to zero). The writer must buy at USD 100 even if the stock is worthless, absorbing a loss of USD 100 less the USD 3 premium collected.

The core asymmetry: short options have **capped gains but unbounded or substantial losses**. Writers earn a steady, limited income from premiums but face tail risks that can overwhelm gains from dozens of successful expirations.

## Breakeven and the Probability of Profit

For a long call, breakeven is the strike plus the premium paid. On a USD 100 strike with a USD 5 premium, breakeven is USD 105. The buyer needs the stock to rise 5% just to recover the premium; any further gain is profit.

For a short call, breakeven is also the strike plus the premium collected. At USD 105, the writer's profit is zero. Below USD 105, the writer is profitable.

This is why short options are attractive to sellers: most options expire worthless (or out-of-the-money), and selling them collects premium with high probability. A writer of call options on a broad index might see 70–80% of sold calls expire profitably. But the 20–30% that do expire in-the-money can erase months of premium income.

## Margin, Collateral, and Risk Management

A buyer of a long option pays the full premium upfront (for American-listed [options](/option/), this is typically one-hundredth of the strike times 100, plus commissions). No additional margin is required; losses are capped at the premium paid.

A writer of a short option must post collateral to ensure they can meet their obligation. For a naked short call, exchanges typically require margin equal to 20% of the underlying stock price plus the option premium (though volatility adjusts this). For a short put, margin is roughly 20% of the strike plus the premium.

As a position moves against the writer—the underlying rises for a short call, falls for a short put—the required margin rises. A writer who sold a call at USD 100 strikes may face a margin call if the stock rallies to USD 150, forcing additional cash to be posted or the position to be closed.

This margin requirement is a practical check on short [option](/option/) writing. A writer cannot indefinitely maintain a short call on an unbounded rising stock without infinite capital.

## Greeks and Hedging

Buyers and writers manage [option](/option/) risk using the [Greeks](/delta/)—[delta](/delta/), [gamma](/gamma/), [theta](/theta/), and [vega](/vega/). A long call has positive delta (gains if the stock rises), positive [gamma](/gamma/) (acceleration on large rallies), negative [theta](/theta/) (loses value as expiration approaches), and positive [vega](/vega/) (gains if volatility rises).

A short call has the opposite signs on most Greeks. Negative [theta](/theta/) is the writer's friend—each day that passes erodes the option's value, and the writer keeps more of the premium. But negative [gamma](/gamma/) is the writer's enemy—big rallies accelerate losses faster than the time decay benefit accumulates.

Professional traders hedge short options by owning the underlying or buying offsetting options. A naked short call is rare among institutional writers; most use [covered calls](/covered-call/) (selling calls against long stock) to limit upside loss to opportunity cost, or collars (long puts plus short calls) to cap both sides of a position.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — Foundational definition and mechanics
- [Strike price](/strike-price/) — The fixed price at which long and short options are exercised
- [Option premium](/option-premium/) — The price buyer pays and writer receives
- [In-the-money](/in-the-money/) — When a long option has intrinsic value and exercise becomes valuable
- [Delta](/delta/) — Greek measuring directional sensitivity; opposite for long vs. short
- [Theta](/theta/) — Time decay; positive for short options (writer benefits), negative for long (buyer loses)

### Wider context

- [Call option](/call-option/) — Specific long and short call mechanics
- [Put option](/put-option/) — Specific long and short put mechanics
- [Protective put](/protective-put/) — Pairing long puts with stock ownership to limit downside
- [Covered call](/covered-call/) — Selling calls against owned stock to cap upside but collect premium
- [Margin call](/margin-call-forex/) — Risk management tool forcing short-option writers to post additional capital

</div>

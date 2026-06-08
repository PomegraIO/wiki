---
title: "Fixed-Strike vs Floating-Strike Lookback Options"
description: "Understand the difference between fixed-strike and floating-strike lookback options, where the payoff depends on historical prices reached during the option's life."
keywords:
  - fixed strike vs floating strike lookback option
  - lookback option payoff
  - floating strike lookback
  - fixed strike lookback
  - exotic option comparison
  - path-dependent option
image: "/svg/derivatives.svg"
---

*A **fixed-strike vs floating-strike lookback option** distinction separates two ways to build an option whose payoff hinges on the best (or worst) price an asset reached during its lifetime, not just the final price. Fixed-strike uses a predetermined strike; floating-strike sets the strike retroactively to the price that would have maximized profit. Both eliminate some regret, but at different costs and with different use cases.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lookback Options — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Lookback options pay based on the asset's historical extremum, offering a second chance at perfect timing.</div>

|   |   |
|---|---|
| **Fixed-strike lookback** | Strike set in advance; payoff is max(S_max – K, 0) for call or max(K – S_min, 0) for put |
| **Floating-strike lookback** | Strike is the historical minimum (call) or maximum (put); payoff is S_max – S_min for call |
| **Path-dependency** | Both depend on the entire price path, not just spot or strike |
| **Call payoff (fixed)** | max(highest price reached – strike, 0) |
| **Call payoff (floating)** | Highest price reached – lowest price reached |
| **Put payoff (fixed)** | max(strike – lowest price reached, 0) |
| **Put payoff (floating)** | Highest price reached – lowest price reached |
| **Typical use** | Regret-minimization; capture extreme moves without predicting direction perfectly |

</aside>

## What Is a Lookback Option?

A lookback [option](/option/) is an exotic derivative where the payoff depends not just on today's price or tomorrow's price, but on the _extreme price_ the underlying asset touched during the option's entire life. If you buy a lookback call on a stock, you profit from the maximum price the stock hit since inception—not the closing price on expiration. This design lets traders "look back" across the entire period and benefit from the most favorable moment, even if they didn't time it perfectly.

Standard (vanilla) options ignore history. A vanilla call on a $50 stock with a $50 strike is worthless on expiration if the stock closes at $49, regardless of whether it rose to $120 intraday. A lookback call would have been deeply in the money if the stock touched $120 at any point. This historical awareness—the path-dependency—is the defining feature.

## Fixed-Strike Lookback: Strike Set in Advance

A **fixed-strike lookback call** has a pre-agreed strike price, set when the option is written. Its payoff at expiration is:

**max(S_max – K, 0)**

where S_max is the highest price the asset reached during the option's life, and K is the fixed strike.

Example: You buy a fixed-strike lookback call on a stock with strike K = $50. During the six-month life of the option, the stock touches a high of $75 (intraday), but closes at $60 on expiration. Your payoff is max(75 – 50, 0) = $25 per share, regardless of the $60 closing price. You capture the entire gain from $50 to the $75 peak.

For a **fixed-strike lookback put**:

**max(K – S_min, 0)**

where S_min is the lowest price reached during the option's life.

If you hold a fixed-strike put with K = $50, and the stock bottoms at $30 (but closes at $40), your payoff is max(50 – 30, 0) = $20 per share. You benefit from the full downside move to the lowest point.

Fixed-strike lookback options are still directional bets—you're speculating that the asset will move meaningfully in your chosen direction. But you get a safety margin: you don't have to catch the exact peak or trough to profit maximally. As long as the asset exceeds your strike (call) or falls below it (put), you win the full spread.

## Floating-Strike Lookback: Strike Is the Extremum

A **floating-strike lookback call** has no pre-set strike. Instead, the strike is automatically the _lowest_ price the asset reached during the option's life. The payoff is simply:

**S_max – S_min**

Example: A stock starts at $50, bottoms at $40, and peaks at $70 during the option's six-month life, closing at $65. The floating-strike lookback call payoff is 70 – 40 = $30. You pocket the spread between the highest and lowest points, regardless of where the stock closes.

For a **floating-strike lookback put**:

The strike is the highest price reached, and the payoff is still:

**S_max – S_min**

(The put payoff formula is symmetric; the difference between high and low is the same whether you're long a call or put.)

Floating-strike lookbacks are path-dependent but direction-agnostic. You don't care whether the stock goes up or down, only that it travels. If the stock is highly volatile and swings between $40 and $70, a floating-strike lookback call is worth roughly $30, period. A sideways market where the stock stays between $50 and $52 yields nearly zero.

## Pricing and Premium Differences

Fixed-strike lookback options are cheaper than floating-strike ones, all else equal. Why? Because in a fixed-strike call, your strike might be set at $100 (e.g., at-the-money initially), and if the stock never reaches $100, you get nothing—even if it moves from $50 to $90. A floating-strike call would have paid off on the $40 spread (90 – 50).

Floating-strike lookbacks are essentially short volatility risk: they profit from the full range, so they're more expensive. They're priced using path-dependent models (Monte Carlo, numerical PDE solvers, or closed-form approximations under certain assumptions). Fixed-strike lookbacks can sometimes be priced more simply if the strike is conventional.

In either case, lookback [options](/option/) are pricier than vanilla options with the same underlying and tenor because they eliminate timing risk. You're paying a premium for the certainty of capturing the extremum.

## When Each Is Used

**Fixed-strike lookback** calls and puts are favored when you have a directional view but want insurance against poor market timing. A trader bullish on oil but nervous about entry points might buy a fixed-strike call with strike at current levels. If oil rallies, he gets the full move from his entry strike to the peak. If oil trades sideways or grinds slightly higher, he might still profit if it touched a higher intraday price.

**Floating-strike lookback** options appeal to volatility traders and market-neutral investors. If you believe an asset will be volatile but have no strong directional bias, a floating-strike lookback profits from the range—the wider the swing, the bigger the payoff. These are sometimes sold to risk-averse investors who want exposure to an asset's volatility without directional bet risk, though the high premium can make this expensive.

## Real-World Constraints

Lookback options are over-the-counter (OTC) derivatives, not exchange-traded. They're typically offered by investment banks on major currencies, equity indices, and commodities. The monitoring is continuous: the dealer tracks intraday prices, not just closing prices, to compute the true historical maximum and minimum.

Practically, tracking can use daily, weekly, or continuous sampling, depending on the contract. If sampling is discrete (daily closes only), the dealer misses intraday extrema, which slightly reduces the option's value but simplifies accounting and reduces litigation risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — contract granting the right, not obligation, to buy or sell an underlying asset
- [Call Option](/call-option/) — right to buy an asset at a fixed price
- [Put Option](/put-option/) — right to sell an asset at a fixed price
- Exotic Option — non-standard option with complex payoff rules
- Path-Dependent Derivative — derivative whose payoff depends on the price path, not just final spot
- Volatility — measure of price fluctuation intensity over time
- [Black-Scholes Model](/black-scholes-model/) — foundational framework for vanilla option pricing

### Wider context

- [Strike Price](/strike-price/) — predetermined price at which an option can be exercised
- [Intrinsic Value](/intrinsic-value/) — immediate profit if the option were exercised
- [Time Value](/time-value/) — extra premium reflecting optionality over remaining life
- [Derivatives Hedging](/derivatives-hedging/) — use of derivatives to offset risk
- [Over-The-Counter Market](/over-the-counter-market/) — decentralized trading of bespoke contracts between counterparties

</div>

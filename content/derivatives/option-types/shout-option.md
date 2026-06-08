---
title: "Shout Option"
description: "An option that grants the holder a single right to lock in a minimum payoff at any point before expiry."
keywords:
  - shout option
  - exotic option
  - path-dependent option
  - derivatives
image: "/svg/derivatives.svg"
---

*A **shout option** is an [option](/option/) that lets its holder freeze a minimum payoff at one moment of the holder's choosing during the contract's life, then continue to participate in further upside until expiry. If the underlying asset rallies after the "shout," the holder captures the additional gain on top of the locked-in floor. If it falls, the holder keeps the frozen payoff.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Shout Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured contracts." />

<div class="wiki-infobox-caption">A flexible exotic option that lets the holder call one reset moment.</div>

|   |   |
|---|---|
| **What it is** | An option with the right to lock in a guaranteed payoff once, then keep playing upside |
| **Also called** | Shout option, one-time reset option |
| **Payoff at expiry** | Max(asset price at expiry, locked-in price at shout date) |
| **Holder's choice** | When to exercise the "shout" right during the option's life |
| **Common underlyings** | Stocks, [indices](/sp-500-index/), [currencies](/us-dollar/), [commodities](/crude-oil/) |
| **Key difference from vanilla** | Can lock in a floor partway through; vanilla options have fixed strike only |
| **Key difference from cliquet** | One discretionary reset date chosen by holder; cliquet resets automatically on a schedule |

</aside>

## The single reset decision

Unlike a standard [call option](/call-option/) with a fixed [strike price](/strike-price/), the shout option holder has complete discretion over when to invoke the "shout." That moment freezes a floor—specifically, the difference between the asset price on the shout date and the original strike price. Once the shout is triggered, the option behaves like a vanilla [call option](/call-option/) for the remainder of its life, but with a synthetic strike price that has been lowered (for a call) to wherever the asset happened to be when the holder shouted.

Suppose a trader buys a one-year shout call on a stock with a 100 strike price. The stock rallies to 120 by month 6; the trader shouts, locking in a 20 payoff floor. If the stock then crashes to 90 by expiry, the holder still receives 20. But if the stock reaches 140 by expiry, the holder receives 40 (the full move from the original 100 strike). The shout has effectively ratcheted the strike down from 100 to 120, capturing the early rally while keeping a claim on any further upside.

## The timing problem

The shout option's appeal lies in its simplicity: one binary decision, at a time of the holder's choosing. The challenge is that real-world investors don't know when the best time to shout is—they lack perfect foresight. A trader who shouts after the stock rallies 15%, only to watch it soar another 50%, might regret the early lock-in. But delaying the shout exposes the holder to drawdown risk.

The economic value of this optionality—the right to choose the shout date—is what differentiates the shout option's [premium](/option-premium/) from a plain vanilla call. The longer the option's life and the higher the underlying's [volatility](/historical-volatility/), the more valuable the shout right becomes. A highly volatile stock offers more opportunities for the holder to shout at a favorable time.

## Valuation via simulation and path dependence

Shout options are **path-dependent** derivatives: their value depends not just on the asset price at expiry, but on the maximum price reached during the option's life (or at least the optimal shout level). Closed-form pricing formulas do not exist; dealers and traders typically use [Monte Carlo simulation](/discounted-cash-flow-valuation/) to estimate fair value.

The valuation algorithm simulates thousands of possible price paths over the option's life. For each path, a backward-induction algorithm determines the optimal shout date (the moment that maximizes the option's payoff conditional on future prices). The average payoff across all paths, discounted to present value, gives the option's theoretical price. This approach is computationally intensive but flexible: it accommodates [interest rate](/interest-rate/) changes, [dividend](/dividend/) yields, and nonlinear [volatility](/historical-volatility/) surfaces.

## Why investors buy shout options

A shout option appeals to traders and portfolio managers who expect strong trends but worry about timing the peak. Rather than buying a vanilla [call](/call-option/) and hoping to sell it at the right moment (or hold through a crash), the shout holder can lock in a meaningful gain and let the next leg of the rally remain unhedged. The upfront cost is lower than buying two separate calls (one for the early move, one for the late move).

[Equity fund managers](/value-investing/) sometimes use shout options on benchmark indices as a cost-effective way to reduce drawdown risk. A manager bullish on the market can buy a shout call on the [S&P 500](/sp-500-index/), shout when it pops 15%, and then participate in additional rallies without the anxiety of seeing a hard-won gain evaporate in a correction.

For [currency traders](/currency-risk/) and commodity players, the shout option offers a middle ground between the rigidity of a fixed-strike option and the complexity of a [cliquet option](/cliquet-option/) with multiple resets. One decision, one moment—simplicity with a benefit.

## The premium and the early-exercise temptation

Shout options tend to be quoted at a modest premium to a standard vanilla [call](/call-option/)—typically 5 to 15% higher, depending on [implied volatility](/implied-volatility/) and time to expiry. The exact markup reflects how much traders value the optionality to choose the reset date.

One subtle danger: if an underlying rallies sharply early, the temptation to shout immediately—and lock in the gain—can override a trader's long-term conviction. Psychologically, the shout option's design can trigger early profit-taking, even when the fundamental outlook remains bullish. Conversely, in a consolidating market, the shout right may never feel urgent, and the holder might let the option expire with little use made of the flexibility.

## Variations

Some structures include multiple shout rights (though these are rarely called "shout options" anymore—they edge toward [cliquet](/cliquet-option/) territory). Others cap the shout payoff or tie the locked-in floor to a percentage of spot price rather than an absolute level. A **shout put** works symmetrically: it lets the holder lock in a maximum loss at a chosen moment, then benefit if the underlying falls further.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational right to buy or sell at a fixed price
- [Call Option](/call-option/) — the right to purchase an asset at the strike price
- [Strike Price](/strike-price/) — the fixed price at which an option can be exercised
- [Option Premium](/option-premium/) — the upfront price of the option
- [Implied Volatility](/implied-volatility/) — the expected price swings embedded in the option price
- [Cliquet Option](/cliquet-option/) — similar exotic option with automatic periodic resets instead of discretionary ones
- [Power Option](/power-option/) — exotic option with a nonlinear payoff
- [Passport Option](/passport-option/) — exotic option on profits from a trading account

### Wider context

- [Exotic Option](/option/) — family of nonstandard derivatives
- [Path Dependency](/option/) — when a derivative's value depends on the price history, not just the final price
- [Derivatives](/option/) — financial contracts tied to an underlying asset
- [Monte Carlo Simulation](/discounted-cash-flow-valuation/) — numerical method for valuing complex instruments
- [Volatility Smile](/volatility-smile/) — structure of implied volatilities across strikes

</div>
